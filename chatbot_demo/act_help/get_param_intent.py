from calendar import c
from distutils.log import error
from tabnanny import check
from act_help import config as cf
# from handle.process_data.connect_tau import Data_TAU
from act_process_data.database import DB_TAU
from act_process_data.connect_tau import Data_TAU
from datetime import date
import datetime
import numpy as np
import re
import dateutil.relativedelta as date_rel

#-Nhận diện ngôn ngữ
import speech_recognition as sr
#-Convert audio content to conformity  
from moviepy.editor import *
#- Convert text to audio

from gtts import gTTS
#-Send API of website
import requests
#-Interactive systems
import os


class Seek_param_intent():
    def intent_Dthu(text_result):
        cuahang = ['ch1','ch2','ch3']
        req = [None, None, None]
        time, original_time = None, None
        error = None
        #--> find type value "TIME"
        for item_time in cf.time.keys():
            if text_result.find(item_time) != -1:
                time, original_time = cf.time[item_time].split('/'), item_time
                req[0] = time[0]
                req[1] = time[1]
                break
        if req[0] is None and req[1] is None:
            i = 0
            for item_time in text_result.split(' '):
                if item_time.find('/') != -1:
                    try:
                        tx_date =  item_time.split('/')
                        if len(tx_date) == 3:
                            convert_date = datetime.datetime(int(tx_date[2]), int(tx_date[1]), int(tx_date[0]))
                            req[i] = "{:%Y-%m-%d}".format(convert_date)
                            i += 1
                            if i == 2:
                                break   
                        else:
                            error = 'Ngày không chính xác, vui lòng nhập đủ theo "ngày/tháng/năm" !'
                    except Exception as Error:
                        print(Error) 
                        error = 'Ngày không chính xác, vui lòng nhập đủ theo "ngày/tháng/năm" !'

            #-- tìm format: ngày 1 tháng 1, quý 1, năm 2021
            if req[0] is None and req[1] is None and error is None:
                # try:
                    #lấy ngày hiện tại để làm mặc định
                    now = datetime.date.today()
                    l = {
                        'ngày' : None,
                        'tháng': None,
                        'quý': None,
                        'năm' : None
                    }
                    # tìm có chữ ngày/tháng/năm hay k, nếu có thì lấy ô trước kí tự tìm đc 1 đơn vị
                    date_text = text_result.split(' ')
                    check_time = False
                    for i in range(len(date_text)):
                        if date_text[i] == 'ngày' and re.search('[0-9]',date_text[i+1]): 
                            l['ngày'] = int(date_text[i+1])
                            check_time = True
                        if date_text[i] == 'tháng' and re.search('[0-9]',date_text[i+1]): 
                            l['tháng'] = int(date_text[i+1])
                            check_time = True
                        if date_text[i] == 'quý' and re.search('[0-9]',date_text[i+1]): 
                            l['quý'] = int(date_text[i+1])
                            check_time = True
                        if date_text[i] == 'năm' and re.search('[0-9]',date_text[i+1]): 
                            l['năm'] = int(date_text[i+1])
                            check_time = True
                        
                    # ngày Exist, tháng None, năm None
                    if l['ngày'] is not None and l['tháng'] is None and l['năm'] is None: 
                        req[0] = date(now.year, now.month, l['ngày'])
                        req[1] = req[0]
                    # ngày None, tháng Exist, năm None
                    elif l['ngày'] is None and l['tháng'] is not None and l['năm'] is None: 
                        req[0] = date(now.year, l['tháng'], 1)
                        req[1] = req[0] + date_rel.relativedelta(months = 1, days = -1)
                    # quý Exist, năm None
                    elif l['quý'] is not None and l['năm'] is None:
                        print(2)
                        switcher = {
                            1:[date(now.year,1,1), date(now.year,3,31)],
                            2:[date(now.year,4,1), date(now.year,6,30)],
                            3:[date(now.year,7,1), date(now.year,9,30)],
                            4:[date(now.year,10,1), date(now.year,12,31)]
                        }
                        req[0] = switcher.get(l['quý'])[0]
                        req[1] = switcher.get(l['quý'])[1]
                    # quý Exist, năm None
                    elif l['quý'] is not None and l['năm'] is not None:
                        print(1)
                        switcher = {
                            1:[date(l['năm'],1,1), date(l['năm'],3,31)],
                            2:[date(l['năm'],4,1), date(l['năm'],6,30)],
                            3:[date(l['năm'],7,1), date(l['năm'],9,30)],
                            4:[date(l['năm'],10,1), date(l['năm'],12,31)]
                        }
                        req[0] = switcher.get(l['quý'])[0]
                        req[1] = switcher.get(l['quý'])[1]
                    # ngày None, tháng None, year Exist
                    elif l['ngày'] is None and l['tháng'] is None and l['năm'] is not None:
                        req[0] = date(l['năm'], 1, 1)
                        req[1] = req[0] + date_rel.relativedelta(years = 1, days = -1)
                    # ngày Exist, tháng Exist, năm None
                    elif l['ngày'] is not None and l['tháng'] is not None and l['năm'] is None: 
                        req[0] = date(now.year, l['tháng'], l['ngày'])
                        req[1] = req[0]
                    # # ngày Exist, tháng None, năm Exist
                    # elif l['ngày'] is not None and l['tháng'] is None and l['năm'] is not None: 
                    #     req[0] = date(l['năm'], now.month, l['ngày'])
                    #     req[1] = req[0]
                    # ngày None, tháng Exist, năm Exist
                    elif l['ngày'] is None and l['tháng'] is not None and l['năm'] is not None: 
                        req[0] = date(l['năm'], l['tháng'], 1)
                        req[1] = req[0] + date_rel.relativedelta(months = 1, days = -1)
                    
                    
                    
                    # ngày, tháng, năm: Exits
                    else:
                        req[0] = date(l['năm'], l['tháng'], l['ngày'])
                        req[1] = req[0]
                    # Hợp mãng để tìm xem có 'đến nay' or 'bay giờ' không
                    date_text = ' '.join(date_text)
                    if date_text.find('đến nay') != -1 and date_text.find('quý') == -1 or date_text.find('bây giờ') != -1 and date_text.find('quý') == -1:
                        req[1] = now

                    if check_time == True and req[0] <= now:
                        req[0], req[1] = "{:%Y-%m-%d}".format(req[0]), "{:%Y-%m-%d}".format(req[1])
                    else:
                        req[0], req[1] = None, None
                        error = 'Vui lòng nhập thời gian nhỏ hoặc bằng ngày hiện tại'

                # except Exception as Error:
                #     print(Error)
                #     error = 'Vui lòng nhập rõ ngày, tháng, năm !!! \n Vd: Ngày 1 tháng 1'

        #--> find type value "STORE"
        list_store = []
        for item_store in text_result.split(' '):
            if item_store in cuahang:
                list_store.append(item_store)
        def unique(list1):
            x = np.array(list1)
            return np.unique(x)
        list_store = unique(list_store)
        list_store = "/".join(list_store)
        req[2] = list_store if list_store != '' else None 

        #--> change type value "TIME" to TEXT 
        if original_time is not None:
            original_time = f' {original_time}'
        else:
            req[0], req[1] = str(req[0]), str(req[1])
            if req[0] is not None and req[1] is not None:
                t_start = Seek_param_intent.convert_date_sql_to_show(req[0])
                t_end = Seek_param_intent.convert_date_sql_to_show(req[1])
                original_time = f' từ {t_start} đến {t_end}'
            elif req[0] is not None and req[1] is None:
                t_start = Seek_param_intent.convert_date_sql_to_show(req[0])
                original_time = f' ngày {t_start}'
            elif req[0] is None and req[1] is not None:
                t_end = Seek_param_intent.convert_date_sql_to_show(req[1])
                original_time = f' ngày {t_end}'
            else:
                original_time = ''
        #--> Tất cả giá trị NONE
        
        count = 0
        for i in range(len(req)):
            if req[i] is None: count += 1
        if count == len(req): req = None

        return req, original_time, error
        
    ''' Chuyển đổi kiểu show cho khách hàng sang dạng Date SQL '''
    def convert_date_show_to_sql(tx_date):
        tx_date = tx_date.split('/')
        convert_date = datetime.datetime(int(tx_date[2]), int(tx_date[1]), int(tx_date[0]))
        result = "{:%Y-%m-%d}".format(convert_date)
        return result
        
    ''' Chuyển đổi kiểu dạng SQL sang kiểu show cho khách hàng '''
    def convert_date_sql_to_show(tx_date):

        tx_date = tx_date.split('-')
        convert_date = datetime.datetime(int(tx_date[0]), int(tx_date[1]), int(tx_date[2]))
        result = "{:%d/%m/%Y}".format(convert_date)
        return result

    '''Chuyển đội giộng nói sang text'''
    def speech_to_text(audio):
        try:
            # the audio content of customer  
            # audio = 'https://cdn.fbsbx.com/v/t59.3654-21/273435150_630569734868930_5045159025695793697_n.mp4/audioclip-1644285883000-2810.mp4?_nc_cat=104&ccb=1-5&_nc_sid=7272a8&_nc_ohc=YMt5zfXNsrAAX91XOm9&_nc_ht=cdn.fbsbx.com&oh=03_AVI4Pdo8xhUyNTTuEa8_lD5cRP3E05AvK9zF3Jy_r4AX_g&oe=6203A2A6'
            # take the audio by URL
            r = requests.get(audio)
            
            # Open content and convert to wav
            with open("voice.wav", "wb") as handle:
                for data in r.iter_content():
                    handle.write(data)
            # concentrate(nén) audio and convert to conformity type
            sound = AudioFileClip("voice.wav")
            sound.write_audiofile("voice.wav", 44100, 2, 2000,"pcm_s16le")
            # initialize(khởi động) the recognizer(nhận diện)
            r = sr.Recognizer()
            # open the file
            with sr.AudioFile("voice.wav") as source:
                # listen for the data (load audio to memory)
                audio_data = r.record(source)
                # recognize (convert from speech to text) -> Result
                text = r.recognize_google(audio_data,language="vi-VI")
            os.remove("voice.wav")
        except Exception as error:
            print('[speech_to_text]->' + error)
            text = None
        return text
    
    '''Chuyển đổi text sang voice'''
    def text_to_speech(text = '', path = '', name = ''):
        try:
            # myText = 'Doanh thu tháng 5 trong ngày 03/05/2021: 3,000,000 Vnđ'
            output = gTTS(
                text = text, 
                lang = 'vi', 
                slow = False
            )
            output.save(path+name)
            check = True
        except Exception as Error:
            print('[text_to_speech]->' + Error)
            check = False

        return check
                                  
