import czifile
def import_image(image_path):
    img = czifile.imread(image_path)
    return img[0,0,0,:,:,0]
