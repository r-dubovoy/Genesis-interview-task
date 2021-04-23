import imageio
import requests
import bz2
import os
from PIL import Image
import torch
import torchvision.transforms as transforms
import dlib
from pix2pixHD.data.base_dataset import __scale_width
from pix2pixHD.models.networks import define_G
import pix2pixHD.util.util as util
from aligner import align_face
from flask import Flask, request, jsonify, render_template
import pickle


import matplotlib.pyplot as plt

img_url = 'https://images.unsplash.com/photo-1508214751196-bcfd4ca60f91?ixid=MnwxMjA3fDB8MHxzZWFyY2h8NHx8d29tYW58ZW58MHx8MHx8&ixlib=rb-1.2.1&w=1000&q=80'
img_filename = 'image.jpg'
imageio.imwrite(img_filename, imageio.imread(img_url))

def unpack_bz2(src_path):
    data = bz2.BZ2File(src_path).read()
    dst_path = src_path[:-4]
    with open(dst_path, 'wb') as fp:
        fp.write(data)
    return dst_path

def download(url, file_name):
    with open(file_name, "wb") as file:
        response = requests.get(url)
        file.write(response.content)

def align(img_filename):
    shape_model_url = 'http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2'
    shape_model_path = 'landmarks.dat'
    download(shape_model_url, shape_model_path)
    shape_predictor = dlib.shape_predictor(unpack_bz2(shape_model_path))
    aligned_img = align_face(img_filename, shape_predictor)[0]
    return aligned_img

def get_eval_transform(loadSize=512):
    transform_list = []
    transform_list.append(transforms.Lambda(lambda img: __scale_width(img,
                                                                      loadSize,
                                                                      Image.BICUBIC)))
    transform_list += [transforms.ToTensor()]
    transform_list += [transforms.Normalize((0.5, 0.5, 0.5),
                                            (0.5, 0.5, 0.5))]
    return transforms.Compose(transform_list)

config_G = {
    'input_nc': 3,
    'output_nc': 3,
    'ngf': 64,
    'netG': 'global',
    'n_downsample_global': 4,
    'n_blocks_global': 9,
    'n_local_enhancers': 1,
    'norm': 'instance',
}

def transfer_style(weights_path, aligned_img, save_as):

    model = define_G(**config_G)
    pretrained_dict = torch.load(weights_path)
    model.load_state_dict(pretrained_dict)
    model.cuda();

    transform = get_eval_transform()
    img = transform(aligned_img).unsqueeze(0)

    with torch.no_grad():
        out = model(img.cuda())

    out = util.tensor2im(out.data[0])
    imageio.imsave(os.path.join('static/uploads/', save_as), out)

    return out;