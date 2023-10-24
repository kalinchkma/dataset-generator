import glob
from rembg import removeBackground

## test bg remove
# removeBackground(sourceFolder="test/im_vs", destinationFolder="test/vs")
# /home/nanashi/Desktop/Datasets/Data of Early Coinage of Bengal/filtered data/real data/anonymous
# /home/nanashi/Desktop/Datasets/Data of Early Coinage of Bengal/filtered data/real data/our collection/Bracteates

# /home/nanashi/Desktop/Datasets/Data of Early Coinage of Bengal/filtered data/real data/anonymous_clean
# /home/nanashi/Desktop/Datasets/Data of Early Coinage of Bengal/filtered data/real data/our collection/Bracteates_clean

real_data_path = "/home/nanashi/Desktop/Datasets/Data of Early Coinage of Bengal/filtered data/real data"


fake_data_path = "/home/nanashi/Desktop/Datasets/Data of Early Coinage of Bengal/filtered data/fake data"


post_gupta_path = "/home/nanashi/Desktop/Datasets/Data of Early Coinage of Bengal/filtered data/real data/our collection/Post-Gupta/"

samatata_path = "/home/nanashi/Desktop/Datasets/Data of Early Coinage of Bengal/filtered data/real data/our collection/Samatata/"


def multi_size_images(path):
    folder_names = [
        folder
        for folder in glob.glob(f"{path}/*/")
        if not folder.endswith("__pycache__/")
    ]
    for i in folder_names:
        removeBackground(
            sourceFolder=f"{i}",
            destinationFolder=f"{i}",
        )


def single_size_image(dir_path):
    removeBackground(
        sourceFolder=f"{dir_path}",
        destinationFolder=f"{dir_path}",
    )


def single_size_image_with_dst(dir_path, dir_dst):
    removeBackground(
        sourceFolder=f"{dir_path}",
        destinationFolder=f"{dir_dst}",
    )


# multi_size_images(samatata_path)
# single_size_image(f"{real_data_path}/anonymous/")
# single_size_image(f"{real_data_path}/Chandra dynasty/")
# single_size_image(f"{real_data_path}/Puri-kushana/")
# multi_size_images(f"{real_data_path}/Samatata")
# single_size_image(f"{real_data_path}/Samatata/Gupta copies")

# multi_size_images(f"{fake_data_path}")
# single_size_image(
#     f"/home/nanashi/Desktop/Datasets/Data of Early Coinage of Bengal/coinage data/anonymous"
# )

single_size_image_with_dst(
    "/home/nanashi/Desktop/test_dataset/fake/to process",
    "/home/nanashi/Desktop/test_dataset/fake/processed",
)
