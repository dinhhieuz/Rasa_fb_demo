import base64
from github import Github
from github import InputGitTreeElement

from logging import error, exception
import numpy as np
import PIL
from PIL import Image
# Multi stream
import asyncio
# System opeare
import os


# Code token git
token = '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'
# Domain to public source
url = 'https://910a-117-2-120-199.ngrok.io'

class iteracv_GitHub:
    def commit (file_list=[], commit_message = '', path_git = ''):
        # iteracv_GitHub.commit(file_list=[name_img_table, name_img_chart], commit_message='chi tiết bán', path_git='assets/')
        try:
            # name repository
            g = Github(token)
            repo = g.get_user().get_repo('Rasa_fb_demo')
            master_ref = repo.get_git_ref('heads/master')
            master_sha = master_ref.object.sha
            base_tree = repo.get_git_tree(master_sha)
            element_list = list()
            file = []
            for x in file_list : file.append('../'+ x )
            for entry in file:
                with open(entry, 'rb') as input_file:
                    data = input_file.read()
                if entry.endswith('.png'):
                    data = base64.b64encode(data).decode('utf-8')
                element = InputGitTreeElement(entry[3:], '100644', 'blob', data)
                element_list.append(element)
            tree = repo.create_git_tree(element_list, base_tree)
            parent = repo.get_git_commit(master_sha)
            commit = repo.create_git_commit(commit_message, tree, [parent])
            master_ref.edit(commit.sha)
            """ An egregious hack to change the PNG contents after the commit """
            for entry in file:
                with open(entry, 'rb') as input_file:
                    data = input_file.read()
                if entry.endswith('.png'):
                    old_file = repo.get_contents(entry[3:])
                    commit = repo.update_file(old_file.path, 'Update PNG content', data, old_file.sha)
            return 1
        except Exception as error:
            print(error)
            return 0

    ''' Public source '''
    def public_image (path = '', name = ''):
        URL_img = f'{url}{path}{name}'
        return URL_img
    
    def public_audio (path = '', name = ''):
        URL_audio = f'{url}{path}{name}'
        return URL_audio

    ''' Merge image '''
    def merge_image(list_img = [], name_img = '', type = None):
        try:
            imgs = [ PIL.Image.open(i) for i in list_img ]
            # pick the image which is the smallest, and resize the others to match it (can be arbitrary image shape here)
            min_shape = sorted( [(np.sum(i.size), i.size ) for i in imgs])[0][1]
            imgs_comb = np.hstack( (np.asarray( i.resize(min_shape) ) for i in imgs ) )
            if type == 'vertical':
            # merge image by chìu dọc
                imgs_comb = np.vstack( (np.asarray( i.resize(min_shape) ) for i in imgs ) )
                imgs_comb = PIL.Image.fromarray( imgs_comb)
                imgs_comb.save('../'+ name_img)   
            if type == 'horizontal':
            # merge image by chìu ngang
                imgs_comb = PIL.Image.fromarray(imgs_comb)
                imgs_comb.save('../'+ name_img)   
            return 1 

        except Exception as error:
            print('[Merge_image]: <-- '+ str(error))
            return 0
    
    def merge_image_2(imgs = [], name_img = ''):
        try:
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
            target_horizon.save('../'+ name_img, 'PNG', optimize = False, quality=95)
            return 1 
        except Exception as error:
            print('[Merge_image]: <-- '+ str(error))
            return 0

    ''' System Interactive '''
    async def remove_file(delay = 3, path = ''):
        # Delay task
        await asyncio.sleep(delay)
        # Remove file in system
        os.remove(path)