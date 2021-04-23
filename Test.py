import Inference

aligned = Inference.align('static/uploads/result.jpg')
Inference.transfer_style("model_checkpoints/to_male_net_G.pth", aligned, "male_result.jpg")