import czifile
import math
import numpy as np
import os
from PIL import Image
def import_image(image_path):
    img = czifile.imread(image_path)
    return img[0,0,0,:,:,0]

def decompose_image(image,photo_dim = 1024, start = (0,0)):
    dim=image.shape
    dim_ceil = (math.ceil(dim [0]/ photo_dim) *photo_dim ,math.ceil(dim [1]/ photo_dim)*photo_dim)
    img=np.pad(image, (dim_ceil[0] - dim[0],dim_ceil[1] - dim[1]))
    h_num_photo = int(dim_ceil[0] / photo_dim)
    v_num_photo = int(dim_ceil[1] / photo_dim)
    fig3D = []
    for i in range(h_num_photo):
        for j in range(v_num_photo):
            arr = img[start[0]+i*photo_dim:start[0]+(i+1)*photo_dim,start[1]+j*photo_dim:start[1]+(j+1)*photo_dim]
            fig3D.append(arr)
    return fig3D
def  save_images(fig3D, dir,image_name):
    num_images = len(fig3D)
    for i in range(num_images):
        filename = image_name + "_" + str(i) + ".jpeg"
        img = Image.fromarray(fig3D[i],"L")
        img.save(os.path.join(dir,filename))
        
        