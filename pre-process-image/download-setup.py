import os
import gdown

os.makedirs("./models", exist_ok=True)

gdown.download(
    "https://dl.fbaipublicfiles.com/segment_anything/sam_vit_h_4b8939.pth",
    "./models/sam_vit_h_4b8939.pth",
    quiet=False,
)
