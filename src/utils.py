import scipy.misc, numpy as np, os, sys
import cv2

"""
def save_img(out_path, img):
    img = np.clip(img, 0, 255).astype(np.uint8)
    #scipy.misc.imsave(out_path, img)
    img_bgr = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    cv2.imwrite(out_path, img_bgr)
"""
def scale_img(style_path, style_scale):
    scale = float(style_scale)
    #o0, o1, o2 = scipy.misc.imread(style_path, mode='RGB').shape
    o0, o1, o2 = cv2.imread(style_path, mode='RGB').shape
    scale = float(style_scale)
    new_shape = (int(o0 * scale), int(o1 * scale), o2)
    style_target = get_img(style_path, img_size=new_shape)
    return style_target

def get_img(src, img_size=False):
   #img = scipy.misc.imread(src, mode='RGB') # misc.imresize(, (256, 256, 3))
   img_bgr = cv2.imread(src) # misc.imresize(, (256, 256, 3)) 
   try:
    img = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
   except:
    img = cv2.imread('./images/commig_soon.png')

   if not (len(img.shape) == 3 and img.shape[2] == 3):
       img = np.dstack((img,img,img))
   if img_size != False:
       img = scipy.misc.imresize(img, img_size)
   return img

def exists(p, msg):
    assert os.path.exists(p), msg

def list_files(in_path):
    files = []
    for (dirpath, dirnames, filenames) in os.walk(in_path):
        files.extend(filenames)
        break

    return files

