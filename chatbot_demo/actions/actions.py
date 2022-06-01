# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from _typeshed import NoneType
from ast import Pass
from email import message
from re import L, S
from typing import Any, Text, Dict, List
# from MySQLdb import Date
from matplotlib.pyplot import text
from pyrsistent import b

from rasa_sdk.events import FollowupAction, SlotSet, ReminderScheduled
from rasa_sdk import Action, Tracker

from rasa_sdk.executor import CollectingDispatcher

import gc
import datetime

from act_help import config as cf
from act_help.get_param_intent import Seek_param_intent
from act_help.conv_image import conv_image
from act_help.iteracv_github import iteracv_GitHub
from act_help.button_rand import button_rand
from act_help.authorized import Authorized_user

# from handle.process_data.connect_tau import Data_TAU
from act_process_data.database import DB_TAU
from act_process_data.connect_tau import Data_TAU
import requests
import yaml
import json
# Multi stream
import asyncio


''' Other functions'''
def inf_user(id_user):
    ''' Lấy tên người dùng '''
    # Đọc file YAML để lấy access token
    with open("credentials.yml") as fh:
        rd_acstoken = yaml.load(fh, Loader=yaml.FullLoader)
        
    profile_user = requests.get("https://graph.facebook.com/{}?fields=first_name,last_name,profile_pic&access_token={}".format(id_user, rd_acstoken["facebook"]["page-access-token"]))
    if str(profile_user) == "<Response [400]>":
        return "bạn"
    else:
        profile_user = profile_user.json() 
        return profile_user['last_name']
    
    ''' Notify forbidden Account '''
def notify_forbidden(dispatcher):
    dispatcher.utter_message(
        text = 'Rất tiết :( , tài khoản của bạn không thể thực hiện chức năng này!!!',
    )
    return

''' Xin chào '''
class act_greet(Action):
    def name(self) -> Text:
        return "act_greet"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        print('[%s] <- %s' % (self.name(), tracker.latest_message['text']))
        # profile_user = inf_user(tracker.sender_id)
        
        button = []
        # Phân quyền
        user = Authorized_user(send_id = tracker.sender_id)
        if len(user.act_permission) > 0 :
            if 'full_controls' in user.act_permission:
                button.append({
                    "type": "postback",
                    "title": "Doanh thu",
                    "payload": "Có những loại doanh thu nào"
                }) 
                button.append({
                    "type": "postback",
                    "title": "Chi tiết bán",
                    "payload": "Có những loại chi tiết bán nào"
                }) 
                # button.append({
                #     "type": "postback",
                #     "title": "Dashboard test",
                #     "payload": "Dashboard dùng để test"
                # })
            else:
                if 'act_dthu' in user.act_permission:
                    button.append({
                        "type": "postback",
                        "title": "Doanh thu",
                        "payload": "Có những loại doanh thu nào"
                    }) 
                if 'act_ctiet_ban' in user.act_permission:
                    button.append({
                        "type": "postback",
                        "title": "Chi tiết bán",
                        "payload": "Có những loại chi tiết bán nào"
                    }) 
                # if 'act_dashboard' in user.act_permission: 
                #     button.append({
                #         "type": "postback",
                #         "title": "Dashboard test",
                #         "payload": "Dashboard dùng để test"
                #     })
            button.append({
                "type": "postback",
                "title": "Bảng lương",
                "payload": "Tôi muốn trợ giúp bảng lương"
            })
        
        text = "Xin chào {} 👋👋👋 \nRất vui được nói chuyện với bạn, tôi có thể giúp gì cho bạn nào? ".format(user.l_name)
        if len(button) != 0: text + '\nĐây là những gợi ý' 
        
        dispatcher.utter_message(
            text = text,
            buttons = button
        )

        del text, button, user
        gc.collect()

        return []

#!------------------------------------------ DOANH THU ------------------------------------------------------------
''' Doanh thu '''
class act_dthu(Action):
    def name(self) -> Text:
        return "act_dthu"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Phân quyền
        user = Authorized_user(send_id = tracker.sender_id)
        if self.name() in user.act_permission or 'full_controls' in user.act_permission :

            button_time = {
                "type": "postback",
                "title": "📅 Thời gian",
                "payload": "Doanh thu theo thời gian"
            }
            button_store = {
                "type": "postback",
                "title": "🏪 Cửa hàng",
                "payload": "Doanh thu theo cửa hàng"
            }
            dispatcher.utter_message(
                text = "Thông tin doanh thu tìm theo loại bao gồm:"
                , buttons=[button_time,button_store]
            )
            del button_time, button_store
            gc.collect()
        
        else:
            notify_forbidden(dispatcher)

        return []
#*--------------------------------------THỜI GIAN----------------------
''' Doanh thu theo thời gian '''
class act_dthu_time(Action):
    def name(self) -> Text:
        return "act_dthu_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Phân quyền
        user = Authorized_user(send_id = tracker.sender_id)
        if self.name() in user.act_permission or 'full_controls' in user.act_permission :
            
            buttons = button_rand.dthu_time()
            dispatcher.utter_message(
                text = "Doanh thu có thể xem theo thời gian: "
                , buttons = buttons
            )
            del buttons
            gc.collect()
        else:
            notify_forbidden(dispatcher)
        

        return []

''' Doanh thu theo thời gian - request '''
class act_dthu_time_req(Action):
    def name(self) -> Text:
        return "act_dthu_time_req"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Phân quyền
        user = Authorized_user(send_id = tracker.sender_id)
        if self.name() in user.act_permission or 'full_controls' in user.act_permission :

            check = False
            print('[%s] <- %s' % (self.name(), tracker.latest_message['text']))
            # now = datetime.datetime.now()
            text = tracker.latest_message['text'].lower().replace('?',' ').replace(',',' ')
            text_result = 'Rất tiết chúng tôi không tìm thấy, hãy thử lại!!'
            req, original_time, error = Seek_param_intent.intent_Dthu(text)
            if error is None:   
                if req is not None:
                    db_result = ''
                    df = DB_TAU.GET_TAU(('doanh_thu', req[0], req[1], req[2], None))
                    if len(df) > 0:
                        if req[2] is not None:   
                            db_result += '\n'
                            for item_store in req[2].split('/'):
                                dff = df[df.isin([item_store]).any(1)].reset_index()
                                if len(dff) > 0:
                                    num = int(dff["Tổng doanh thu"][0])
                                    db_result += f'- {item_store.upper()}: ' + f'{num:,}' + '\n'
                                else:
                                    db_result += f'- {item_store.upper()}: ' + 'Không có' + '\n'
                        else:
                            num = int(df["Tổng doanh thu"][0])
                            db_result += str(f'{num:,}').replace(',','.')
                        check = True
                    else:
                        db_result += 'Không có dữ liệu cho kết quả tìm kiếm'
                    text_result = f'Doanh thu{original_time}: '+ db_result + ' VNĐ'
                else:
                    text_result = "Chúng tôi không hiểu ý bạn\nbạn có thể tham khảo gợi!!!"
            else:
                text_result = error
            if check == True:
                dispatcher.utter_message(
                    text = text_result
                )
                del check, text, text_result, req, original_time, error
                del db_result, df, num
                if 'dff' not in locals(): pass
                else: del dff 
                gc.collect
                return []
            else:
                dispatcher.utter_message(
                    text = text_result
                )
                del check, text, text_result, req, original_time, error
                if 'db_result' not in locals(): pass
                else: del db_result 
                if 'df' not in locals(): pass
                else: del df 
                if 'dff' not in locals(): pass
                else: del dff 
                if 'num' not in locals(): pass
                else: del num
                gc.collect
                #-> Chuyển sang action: act_dthu_time để gợi ý
                return [FollowupAction(name='act_dthu_time')]

        else:
            notify_forbidden(dispatcher)
        return []

#*--------------------------------------CỬA HÀNG----------------------
''' Doanh thu theo cửa hàng '''
class act_dthu_store(Action):
    def name(self) -> Text:
        return "act_dthu_store"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Phân quyền
        user = Authorized_user(send_id = tracker.sender_id)
        if self.name() in user.act_permission or 'full_controls' in user.act_permission :

            buttons = button_rand.dthu_store()
            dispatcher.utter_message(
                text = "Gợi ý thông tin doanh thu theo loại cửa hàng có thể là: ",
                buttons= buttons
            )
            del buttons
            gc.collect()

        else:
            notify_forbidden(dispatcher)
        return []
''' Doanh thu theo cửa hàng - request '''
class act_dthu_store_req(Action):
    def name(self) -> Text:
        return "act_dthu_store_req"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        print('[%s] <- %s' % (self.name(), tracker.latest_message['text']))

        # Phân quyền
        user = Authorized_user(send_id = tracker.sender_id)
        if self.name() in user.act_permission or 'full_controls' in user.act_permission :

            check = False
            now = datetime.datetime.now()
            text = tracker.latest_message['text'].lower().replace('?',' ').replace(',',' ')
            text_result = 'Rất tiết chúng tôi không tìm thấy, hãy thử lại!!'
            URL_img_table = ''
            req, original_time, error = Seek_param_intent.intent_Dthu(text)
            if error is None: 
                #--- So sánh nhiều Cửa hàng
                if req is not None:
                    db_result = ''
                    df = DB_TAU.GET_TAU(('doanh_thu', req[0], req[1], req[2], None))
                    if len(df) > 0:
                        if req[2] is not None:
                            for item_store in req[2].split('/'):
                                dff = df[df.isin([item_store]).any(1)].reset_index()
                                if len(dff) > 0:
                                    num = int(dff["Tổng doanh thu"][0])
                                    db_result += f'- {item_store.upper()}: ' + f'{num:,}' + '\n'
                                else:
                                    db_result += f'- {item_store.upper()}: ' + 'Không có' + '\n'

                            name_img_table = "assets/" + "dthu_store_chart_" + "{:%Y-%m-%d_%Hh-%Mm-%Ss}".format(now)+".png"
                            result_img_table = conv_image.bar_chart(    
                                                                        data = df, x_label = 'Cửa hàng', y_bar = ['Tổng doanh thu'], 
                                                                        color_bar = ['#02b4f0'], width =  .40, 
                                                                        name_img = name_img_table, title = f'Doanh thu của cửa hàng{original_time}'
                                                                    )
                            # --Commiting image in the github
                            # result_git= iteracv_GitHub.commit(file_list=[name_img_table], commit_message='Doanh thu của cửa hàng', path_git='assets/')
                            
                            # if result_git == 1:
                            #     URL_img_table = f'https://raw.githubusercontent.com/dinhhieuz/Rasa_fb_demo/master/{name_img_table}'
                            URL_img_table = iteracv_GitHub.public_image(path = '/', name = name_img_table )
                            check = True
                        else:
                            db_result = 'Không tìm thấy cửa hàng'
                    else:
                        db_result += 'Không có dữ liệu cho kết quả tìm kiếm'
                    text_result = f'Doanh thu của cửa hàng{original_time} (Vnđ):\n'+ db_result
                else:
                    text_result = "Chúng tôi vẫn không hiểu ý bạn\nbạn có thể tham khảo gợi!!!"
            else: 
                text_result = error

            if check == True:
                dispatcher.utter_message(
                    text = text_result,
                    image = URL_img_table 
                )
                #-- Del Object in funcion
                del text, text_result, req, original_time, error, check, now
                del df, num, db_result, dff, URL_img_table, name_img_table, result_img_table

                gc.collect()
                return []
            else:
                dispatcher.utter_message(
                    text = text_result
                )
                del text, text_result, req, original_time, error, check, now
                if 'df' not in locals(): pass
                else: del df 
                if 'num' not in locals(): pass
                else: del num 
                if 'db_result' not in locals(): pass
                else: del db_result 
                if 'dff' not in locals(): pass
                else: del dff
                if 'num' not in locals(): pass
                else: del num
                if 'name_img_table' not in locals(): pass
                else: del name_img_table
                if 'URL_img_table' not in locals(): pass
                else: del URL_img_table
                if 'result_img_table' not in locals(): pass
                else: del result_img_table

                gc.collect()
                return [FollowupAction(name='act_dthu_store')]

        else:
            notify_forbidden(dispatcher)
            return []

#!------------------------------------------ CHI TIẾT BÁN ------------------------------------------------------------
# chi tiết bán theo thông tin cửa hàng
''' Doanh thu theo cửa hàng '''
class act_ctiet_ban(Action):
    def name(self) -> Text:
        return "act_ctiet_ban"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        print('[%s] <- %s' % (self.name(), tracker.latest_message['text']))

        # Phân quyền
        user = Authorized_user(send_id = tracker.sender_id)
        if self.name() in user.act_permission or 'full_controls' in user.act_permission :
        
            button_time = {
                "type": "postback",
                "title": "📅 Thời gian",
                "payload": "Chi tiết bán theo thời gian"
            }
            button_store = {
                "type": "postback",
                "title": "🏪 Cửa hàng",
                "payload": "chi tiết bán theo thông tin cửa hàng"
            }
            dispatcher.utter_message(
                text = "Thông tin chi tiết bán tìm theo loại bao gồm:"
                , buttons=[button_store]
            )
            del button_time, button_store
            gc.collect()
            return []

        else:
            notify_forbidden(dispatcher)
            return []
        



# chi tiết bán theo thông tin cửa hàng
''' Chi tiết bán theo cửa hàng '''
class act_ctiet_ban_store(Action):
    def name(self) -> Text:
        return "act_ctiet_ban_store"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        print('[%s] <- %s' % (self.name(), tracker.latest_message['text']))
        
        # Phân quyền
        user = Authorized_user(send_id = tracker.sender_id)
        if self.name() in user.act_permission or 'full_controls' in user.act_permission :
            
            #- Xuất các buttons 
            buttons = button_rand.ctiet_ban_store()

            dispatcher.utter_message(
                text = "Gọi ý thông tin chi tiết bán theo cửa hàng có thể là:"
                , buttons = buttons
            )
            del buttons
            gc.collect()
            return []

        else:
            notify_forbidden(dispatcher)
            return []

''' Chi tiết bán theo cửa hàng - request '''
class act_ctiet_ban_store_req(Action):
    def name(self) -> Text:
        return "act_ctiet_ban_store_req"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        print('[%s] <- %s' % (self.name(), tracker.latest_message['text'])) 

        # Phân quyền
        user = Authorized_user(send_id = tracker.sender_id)
        if self.name() in user.act_permission or 'full_controls' in user.act_permission :
                
            now = datetime.datetime.now()
            check = False
            text = tracker.latest_message['text'].lower().replace('?',' ').replace(',',' ')
            text_result = 'Rất tiết chúng tôi không tìm thấy, hãy thử lại!!'
            req, original_time, error = Seek_param_intent.intent_Dthu(text)
            if error is None:
                if req is not None:
                    if req[2] is None:
                        text_result = 'không tìm thấy cửa hàng, vui lòng thử lại'
                    elif len(req[2].split('/')) == 1:
                        # req[0], req[1] = '2020-01-01', '2025-01-01' if req[0] is None
                        df = DB_TAU.GET_TAU(('chitiet_ban', req[0], req[1], req[2], None))
                        if len(df) > 0:
                            req[2] = ' của cửa hàng ' + req[2].upper() if req[2] is not None else ''
                            text_result = f'Chi tiết bán{req[2]}{original_time}'
                            # --Loading Table to respone user
                            name_img_table = "assets/" + "chitiet_ban_table_" + "{:%Y-%m-%d_%Hh-%Mm-%Ss}".format(now)+".png"
                            result_img_table = conv_image.table(df = df, name_img = name_img_table, title=text_result)
                            #--Loading chart to respone user
                            name_img_chart = "assets/" + "chitiet_ban_chart_" + "{:%Y-%m-%d_%Hh-%Mm-%Ss}".format(now)+".png"
                            result_img_chart = conv_image.bar_line_chart(   
                                                                            data = df, 
                                                                            x_label = 'Thời gian', y_bar = ['Doanh thu','Chi phí'], y_line = 'Lợi nhuận', 
                                                                            color_bar = ['#02b4f0', '#cf4f25' ], color_line='#045220', width =  .40,
                                                                            title = text_result, name_img= name_img_chart
                                                                        )
                            # --Commiting image in the github
                            # result_git= iteracv_GitHub.commit(file_list=[name_img_table, name_img_chart], commit_message='chi tiết bán', path_git='assets/')
                            name_img = "assets/" + "chitiet_ban_" + "{:%Y-%m-%d_%Hh-%Mm-%Ss}".format(now)+".png"
                            result_merge = iteracv_GitHub.merge_image_2(imgs = [f'../{name_img_table}', f'../{name_img_chart}'], name_img = name_img)
                            # URL_img = ''
                            URL_img = iteracv_GitHub.public_image(path = '/', name = name_img )
                            # URL_img_table = iteracv_GitHub.public_image(path = '/ChatBox_RASA/dsa_demo_sell_materia/', name = name_img_table )
                            # URL_img_chart = iteracv_GitHub.public_image(path = '/ChatBox_RASA/dsa_demo_sell_materia/', name = name_img_chart )

                            if result_img_table == 1 and result_img_chart == 1:
                                text_result = "Vui lòng đợi, đang xử lý ảnh..."
                                check = True
                            else:
                                text_result = 'Đã gặp sự cố trong quá trình xử lý bảng, vui lòng thử lại!!!'
                        else:
                            text_result = 'Dữ liệu không tồn tại, vui lòng thử lại!!!'
                    else: 
                        text_result = 'Chỉ được phép tìm một cửa hàng cho tìm kiếm chi tiết bán, vui lòng thử lại!!!'
                else:
                    text_result = "Chúng tôi vẫn không hiểu ý bạn\nbạn có thể tham khảo gợi!!!"
                #-> Chuyển sang action: act_dthu_store để gợi ý
            else: 
                text_result = error
            #respond 
            if check == True:
                dispatcher.utter_message(
                    text = text_result,
                    image = URL_img
                )
                #-- Del Object in funcion
                del text, text_result, req, original_time, error, now, check
                del df, name_img_table, result_img_table, name_img_chart, URL_img
                gc.collect()
                return []
            else:
                dispatcher.utter_message(
                    text = text_result
                )
                del text, text_result, req, original_time, error, now, check
                if 'df' not in locals(): pass
                else: del df 
                if 'name_img_table' not in locals(): pass
                else: del name_img_table 
                if 'result_img_table' not in locals(): pass
                else: del result_img_table 
                if 'name_img_chart' not in locals(): pass
                else: del name_img_chart 
                if 'result_img_chart' not in locals(): pass
                else: del result_img_chart 
                if 'URL_img' not in locals(): pass
                else: del URL_img 
                if 'result_img_chart' not in locals(): pass
                else: del result_img_chart
                gc.collect()

                return [FollowupAction(name='act_ctiet_ban_store')]

        else:
            notify_forbidden(dispatcher)
            return []
 
''' Chi tiết bán theo thời gian '''
class act_ctiet_ban_time(Action):
    def name(self) -> Text:
        return "act_ctiet_ban_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        print('[%s] <- %s' % (self.name(), tracker.latest_message['text']))
        # Phân quyền
        user = Authorized_user(send_id = tracker.sender_id)
        if self.name() in user.act_permission or 'full_controls' in user.act_permission :
                
            #- Xuất các buttons 
            buttons = button_rand.ctiet_ban_store()

            dispatcher.utter_message(
                text = "Gọi ý thông tin chi tiết bán theo thời gian có thể là:"
                , buttons = buttons
            )
            del buttons
            gc.collect()

            return []

        else:
            notify_forbidden(dispatcher)
            return []
''' Chi tiết bán theo thời gian - request '''
class act_ctiet_ban_time_req(Action):
    def name(self) -> Text:
        return "act_ctiet_ban_time_req"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        print('[%s] <- %s' % (self.name(), tracker.latest_message['text'])) 
        return [FollowupAction('act_ctiet_ban_store')]
#!------------------------------------------ DASHBOARD ----------------------------------
''' Dashboard '''
class act_dashboard(Action):
    def name(self) -> Text:
        return "act_dashboard"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Open a file: file
        print('[%s] <- %s' % (self.name(), tracker.latest_message['text']))
        dispatcher.utter_message(
            text = 'Chức năng đang được phát triển, hãy thử lại sau')
        gc.collect()
        return []


#!------------------------------------------- SALARY -----------------------------------
''' List option of bảng lương '''
class act_salary(Action):
    def name(self) -> Text:
        return "act_salary"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        print('[%s] <- %s' % (self.name(), tracker.latest_message['text']))
        now = datetime.datetime.now()
        button = [
            {
                "type":"postback",
                "title":f"⭐ Đăng kí gửi lương ({now.month}/{now.year})",
                "payload": "bảng lương tự động"
            },
            {
                "type":"postback",
                "title":"Nhập lương ZALO",
                "payload":"Nhập lương ZALO cho nhân viên để demo"
            },
            {
                "type":"postback",
                "title":"Nhập bảng lương (demo)",
                "payload":"insert table salary to demo"
            },
            # {
            #     "type":"postback",
            #     "title":"📞 Liên hệ nhân sự",
            #     "payload":" Liên hệ phòng nhân sự"
            # },
            # {
            #     "type":"postback",
            #     "title":"chính sách",
            #     "payload": "chính sách bảng lương"
            # }
        ]

        dispatcher.utter_message(
            text = "Gọi ý thông tin lương cá nhân có thể là:"
            , buttons = button
        )

        del button, now
        gc.collect()

        return []

''' Auto send salary to staff'''
class act_salary_auto(Action):
    def name(self) -> Text:
        return "act_salary_auto"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # logs contents
        print('[%s] <- %s' % (self.name(), tracker.latest_message['text']))
        Row_count = DB_TAU.SALARY((tracker.sender_id), check_otp=True)
        #-> Check có mã hay chưa
        if Row_count > 0:
            dispatcher.utter_message(text="Bạn đã đăng kí bảng lương cho tháng này :) hãy đăng kí lại sau nhá")
        else:
            res = {
                "attachment": {
                    "type": "template",
                    "payload": {
                        "template_type": "one_time_notif_req",
                        "title": "Đăng ký gữi",
                        "payload": "đăng ký gữi tự động lương"
                    }
                }
            }
            dispatcher.utter_message(json_message=res)
            del res
        # schedule = datetime.datetime.now() + datetime.timedelta(minutes=1)
        # dispatcher.utter_message(text= 'Bạn sẽ nhận được lương sau 1p nữa')
        # ReminderScheduled(
        #             intent_name='ask_salary_auto_send', 
        #             trigger_date_time = schedule, 
        #             name = 'salary_auto:' + str(schedule), 
        #             kill_on_user_message=True)
        del Row_count
        gc.collect()
        return []

''' Registered to Auto send salary to staff'''
class act_salary_auto_send(Action):
    def name(self) -> Text:
        return "act_salary_auto_send"

    async def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # logs contents
        print('[%s] <- %s' % (self.name(), tracker.latest_message['text']))
        # Lấy mã token
        token_notif = tracker.latest_message['text'].split(' | ')[1]
        # Đăng kí trong database
        Row_count = DB_TAU.SALARY((tracker.sender_id, token_notif))
        # Kiểm tra đăng kí có thành công không
        if Row_count == -1:
            dispatcher.utter_message(text="Đăng ký thất bại :( \nVui lòng thử lại!!!")
            FollowupAction('act_salary_auto')
        elif Row_count == 0:
            dispatcher.utter_message(text="Bạn đã đăng kí bảng lương cho tháng này :) hãy đăng kí lại sau nhá")
        else:
            dispatcher.utter_message(text="Đăng ký thành công <3 \nChúng tôi sẽ thông báo lương cho bạn vào tháng tới, hãy đợi nhé!!!")
        
        # đăng ký gữi tự động lương | 7089066037755021622
        del token_notif, Row_count
        gc.collect()
        return []


'''Create data row in table to demo with customer'''
class act_insert_salary_demo(Action):
    def name(self) -> Text:
        return "act_insert_salary_demo"

    async def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        print('[%s] <- %s' % (self.name(), tracker.latest_message['text']))
        # dispatcher.utter_message(text="Thêm bảo lương mẫu thành công\n bảng lương sẽ được gữi cho bạn khi đã đăng kí")
        
        # Lấy mã token
        # Đăng kí trong database
        Row_count = DB_TAU.SALARY((), insert_demo= True)

        del Row_count
        gc.collect()
        return [] 

class act_insert_salary_demo_zalo(Action):
    def name(self) -> Text:
        return "act_insert_salary_demo_zalo"

    async def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        print('[%s] <- %s' % (self.name(), tracker.latest_message['text']))
        # dispatcher.utter_message(text="Thêm bảo lương mẫu thành công\n bảng lương sẽ được gữi cho bạn khi đã đăng kí")
        
        # Lấy mã token
        # Đăng kí trong database
        Row_count = DB_TAU.SALARY((tracker.sender_id), insert_demo_zalo= True)
        dispatcher.utter_message(text = 'Hãy check bảng lương tự động tại zalo của bạn !!')

        del Row_count
        gc.collect()
        return [] 

#!------------------------------------------- FALL BACK --------------------------------

''' Fall Back '''
class act_unknown(Action):
    def name(self) -> Text:
        return "act_unknown"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Open a file: file
        print('[%s] <- %s' % (self.name(), tracker.latest_message['text']))
        messeger_user = tracker.latest_message['text']
        ## ------> Speech-to-Text 
        if messeger_user.startswith("https://cdn.fbsbx.com/v/") and messeger_user.find('mp4') > -1:
            try:
                # Chuyển đổi audio sang text
                text = Seek_param_intent.speech_to_text(audio = messeger_user)
                if text is not None:
                    print('[%s] <- %s' % (self.name(), text))
                    # gữi request API tới Rasa cục bộ
                    url = 'http://localhost:7007/webhooks/rest/webhook'
                    payload = {
                            'sender': f'{tracker.sender_id}', 
                            'message': f'{text}'
                        }
                    # Send Methor API Post to Rasa to get the result 
                    response = requests.post(url, data=json.dumps(payload), headers={'content-type': 'application/json'}).json()[0]
                    dispatcher.utter_message(
                        text= response.get("text")
                        , buttons= response.get("buttons")
                    )
                    # convert text result to Voice and make them public 
                    now = datetime.datetime.now()
                    name_audio = 'voice_audio_{:%Y-%m-%d_%Hh-%Mm-%Ss}.mp3'.format(now)
                    check = Seek_param_intent.text_to_speech(text = response.get("text"), path = './assets/audio/', name = name_audio)

                    # Check if the conversion(chuyển đổi) is successful
                    if check == True:
                        URL_audio = iteracv_GitHub.public_audio(path='/chatbot_demo/assets/audio/', name = name_audio)
                        message = {
                                    "attachment": {
                                        "type": "audio",
                                        "payload":{
                                            "url":URL_audio
                                        }
                                    }
                                }
                        dispatcher.utter_message(json_message=message)
                        
                        #Remove file in second stream with delay 10 second 
                        loop = asyncio.get_event_loop()
                        loop.create_task(iteracv_GitHub.remove_file(delay=10, path= './assets/audio/'+ name_audio))
                        
                        del URL_audio, message
                    
                    del text, url, payload, response, now, check, name_audio
                else:
                    dispatcher.utter_message(
                        text= "Rất tiết, tôi không hiểu những gì bạn nói :( :( \nVui lòng nói rõ hơn!!!"
                    )
                
            except Exception as error:
                print(error)
                dispatcher.utter_message(
                    text= "Rất tiết, tôi không hiểu những gì bạn nói :( \nVui lòng nói rõ hơn!!!"
                )
        else:
            url = "https://www.google.com.vn/search?q='" + messeger_user.replace(" ", "%20") + "'"
            search = {
                "type": "web_url",
                "url": f"{url}",
                "title": "Search Google",
            }
            dispatcher.utter_message(
                text="Xin lỗi bạn vì hiện tại tôi chưa hiểu bạn muốn gì! Bạn hãy bấm vào đây để tôi nhờ chị Google giải đáp nhé: "
                , buttons= [search])

            del url, search, messeger_user

        gc.collect()
        return []


# ''' Fall Back '''
# class act_sendRasa(Action):
#     def name(self) -> Text:
#         return "act_sendRasa"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

