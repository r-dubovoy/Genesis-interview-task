# Roman's Dubovyi Genesis interview task solution.

Hi, this is the solution for task:

Create rest api by next requirements:
Review the following [repository](https://github.com/EvgenyKashin/stylegan2-distillation), it has 2 pretrained models included.
You need to create an api which will have an image of a person's face as input, and will perform gender swap on it both ways(to male and to female). Then you need to return both results to a user. API must be deployable at your local machine. Deploying it with docker will be considered as a strong advantage.

# Prerequisites
Based on [stylegan2](https://github.com/NVlabs/stylegan2) and [pix2pixHD](https://github.com/NVIDIA/pix2pixHD) repos. To use it, you must install their requirements.

# How to use
If you have Windows you first need to enable GPU support for WSL2 explained [here](https://docs.nvidia.com/cuda/wsl-user-guide/index.html).

If you have CUDA10 - build Docker image from Dockerfile.

**If you have GPU series 3000 which only supports CUDA11 - build Docker image from Dockerfile-cuda11.** 

![how to use](https://i.ibb.co/gVLqFQK/Capture.png)

**[----->Video example <-----](https://drive.google.com/file/d/1r0HHL8LH5BvzXFSaF7DySfSCnN8gKVUr/view?usp=sharing)** - Google drive link of me using this soft.
