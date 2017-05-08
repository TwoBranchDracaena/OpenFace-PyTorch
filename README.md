# OpenFace-PyTorch

# Introduction
Here we provide [PyTorch](http://pytorch.org/) version for [OpenFace](https://github.com/cmusatyalab/openface)'s facial feature extraction model.
The original model is written in Torch.
The conversion is mostly done by clarwin's [convert_torch_to_pytorch](https://github.com/clcarwin/convert_torch_to_pytorch), with some added layers, e.g. Inception.

# Usage
First, download binary model files(.pth) from BaiduPan or DropBox.
Second, refer to test.py for how to use the model.

In short, net.py contains model structure, and net.pth contains model parameters.
They are converted from 'nn4.small2.v1.t7' which is the default model of OpenFace project.
More models from OpenFace can be found under \models folder.