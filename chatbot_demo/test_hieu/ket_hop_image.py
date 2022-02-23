from logging import error, exception
import numpy as np
import PIL
from PIL import Image

# def merge_image(list_img = [], name_img = '', type = None):
#     try:
#         imgs = [ PIL.Image.open(i) for i in list_img ]
#         # pick the image which is the smallest, and resize the others to match it (can be arbitrary image shape here)
#         min_shape = sorted( [(np.sum(i.size), i.size ) for i in imgs])[0][1]
#         imgs_comb = np.hstack( (np.asarray( i.resize(min_shape) ) for i in imgs ) )
#         if type == 'vertical':
#         # merge image by chìu dọc
#             imgs_comb = np.vstack( (np.asarray( i.resize(min_shape) ) for i in imgs ) )
#             imgs_comb = PIL.Image.fromarray( imgs_comb)
#             imgs_comb.save(name_img)
#         if type == 'horizontal':
#         # merge image by chìu ngang
#             imgs_comb = PIL.Image.fromarray(imgs_comb)
#             imgs_comb.save(name_img)   
#         return 1 
#     except Exception as error:
#         print('[Merge_image]: <-- '+ error)
#         return 0
# import datetime as date
# begin = date.datetime.today()
# merge_image(list_img = ['2.png', '1.png', '3.png'], name_img='test1.png', type='vertical')
# print(date.datetime.today()-begin)


    

#!-----------------------------------------------------
import datetime
begin = datetime.datetime.today()

from PIL import Image
def merge_image(imgs = [], name_img = ''):
    # imgs = [r'1.png', r'2.png', r'3.png']
    total_width, total_height, max_width, max_height = 0, 0, 0, 0
    ix =[]
    for img in imgs:
        im = Image.open(img)
        size = im.size
        w, h = size[0], size[1]
        total_width += w 
        total_height += h
        if h > max_height: max_height = h
        if w > max_width: max_width = w
        ix.append(im)
    target_horizon = Image.new('RGB', (total_width, max_height))
    pre_w, pre_h = 0, 0 
    for img in ix:
        target_horizon.paste(img, (pre_w, pre_h, pre_w+img.size[0], pre_h + img.size[1]))
        pre_w += img.size[0]
    target_horizon.save(name_img, 'PNG', optimize = False, quality=95)
    
merge_image(imgs = ['1.png', '2.png', '3.png'], name_img= 'horizon.png')
print(datetime.datetime.today() - begin)

