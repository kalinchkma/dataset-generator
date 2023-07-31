import sys
import numpy as np
import matplotlib.pyplot as plt
import cv2

import torch
import torchvision
from segment_anything import sam_model_registry, SamAutomaticMaskGenerator, SamPredictor


## Get Device
device = "cpu"
if torch.cuda.is_available():
    device = "cuda"

## Setup SAM model
sam_checkpoint = "./models/sam_vit_h_4b8939.pth"
model_type = "vit_h"

## Register sam model
sam = sam_model_registry[model_type](checkpoint=sam_checkpoint)
sam.to(device=device)

## Create a predictor for segment
predictor = SamPredictor(sam)
