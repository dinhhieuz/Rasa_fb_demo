# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from _typeshed import NoneType
from typing import Any, Text, Dict, List

from rasa_sdk.events import FollowupAction
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

import gc
import datetime

from act_help import config as cf
from act_help.get_param_intent import Seek_param_intent
# from handle.process_data.connect_tau import Data_TAU
from act_process_data.database import DB_TAU
from act_process_data.connect_tau import Data_TAU



''' Xin chào '''
class act_greet(Action):
    def name(self) -> Text:
        return "act_greet"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        print('[%s] <- %s' % (self.name(), tracker.latest_message['text']))

        text = "Xin chào bạn 👋👋👋 \nRất vui được nói chuyện với bạn, tôi có thể giúp gì cho bạn nào? \nĐây là những gợi ý"
        button_revenue = {
            "type": "postback",
            "title": "Doanh thu",
            "payload": "Có những loại doanh thu nào"
        }
        button_details = {
            "type": "postback",
            "title": "Chi tiết bán",
            "payload": "Có những loại chi tiết bán nào"
        }
        dispatcher.utter_message(
            text = text,
            buttons = [button_revenue, button_details]
        )
        del button_revenue, button_details, text
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

        return []
#*--------------------------------------THỜI GIAN----------------------
''' Doanh thu theo thời gian '''
class act_dthu(Action):
    def name(self) -> Text:
        return "act_dthu_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        button1 = {
            "type": "postback",
            "title": "Hôm nay",
            "payload": "Doanh thu hôm nay?"
        }
        button2 = {
            "type": "postback",
            "title": "Tuần này",
            "payload": "Doanh thu tuần này?"
        }
        # button3 = {
        #     "type": "postback",
        #     "title": "Doanh thu tháng này",
        #     "payload": "Doanh thu tháng này?"
        # }
        button3 = {
            "type": "postback",
            "title": "Tuần này cửa hàng CH1",
            "payload": "Doanh thu tuần này của cửa hàng CH1?"
        }

        dispatcher.utter_message(
            text = "Doanh thu có thể xem theo thời gian: "
            , buttons = [button1, button2, button3]
        )

        del button1, button2, button3
        gc.collect()

        return []

''' Doanh thu theo thời gian - request '''
class act_dthu_time_req(Action):
    def name(self) -> Text:
        return "act_dthu_time_req"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        print('[%s] <- %s' % (self.name(), tracker.latest_message['text']))

        text = tracker.latest_message['text'].lower().replace('?','')
        text_result = 'Rất tiết chúng tôi không tìm thấy, hãy thử lại!!'
        num, df = None, None
        req, original_time, error = Seek_param_intent.intent_Dthu(text)

        #--- So sánh nhiều Cửa hàng

        if error is None:
            for item_store in req[2]:
                item_store = None if item_store == '~' else item_store

                df = DB_TAU.GET_TAU(('doanh_thu', req[0], req[1], item_store))
                if df["sum_dthu"][0] != None:
                    item_store = ' của cửa hàng ' + item_store.upper() if item_store is not None else ''
                    if original_time is not None:
                        original_time = f'{original_time}'
                    else:
                        if req[0] is not None and req[1] is not None:
                            t_start = Seek_param_intent.convert_date_sql_to_show(req[0])
                            t_end = Seek_param_intent.convert_date_sql_to_show(req[1])
                            original_time = f'từ {t_start} đến {t_end}'
                        elif req[0] is not None and req[1] is None:
                            req[0] = Seek_param_intent.convert_date_sql_to_show(req[0])
                            original_time = f'ngày {t_start}'
                        elif req[0] is None and req[1] is not None:
                            req[1] = Seek_param_intent.convert_date_sql_to_show(req[1])
                            original_time = f'ngày {t_end}'
                        else:
                            original_time = ''

                    num = int(df["sum_dthu"][0])
                    text_result = f'Doanh thu {original_time}{item_store} là: {num:,}'
                    dispatcher.utter_message(
                        text = text_result
                    )
                else:
                    text_result = f'Rất tiết chúng tôi không tìm thấy thông tin thời gian bạn muốn tìm , hãy thử lại!!'
                    dispatcher.utter_message(
                        text = text_result
                    )
            
        else:
            text_result = error
            dispatcher.utter_message(
                text = text_result
            )

        del text, text_result, req, df, num, original_time, error
        gc.collect
        return []

#*--------------------------------------CỬA HÀNG----------------------
''' Doanh thu theo cửa hàng '''
class act_dthu(Action):
    def name(self) -> Text:
        return "act_dthu_store"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        button1 = {
            "type": "postback",
            "title": "Cửa hàng CH1", 
            "payload": "Doanh thu cửa hàng CH1"
        }
        button2 = {
            "type": "postback",
            "title": "Cửa hàng CH3 hôm nay", 
            "payload": "Doanh thu cửa hàng CH3 hôm nay"
        }
        button3 = {
            "type": "postback",
            "title": "Cửa hàng CH2 tuần nay", 
            "payload": "Doanh thu cửa hàng CH2 trong tuần nay"
        }

        dispatcher.utter_message(
            text = "Doanh thu có thể xem theo cửa hàng: ",
            buttons= [button1, button2, button3]
        )

        del button1, button2, button3
        gc.collect()

        return []
''' Doanh thu theo cửa hàng - request '''
class act_dthu_store_req(Action):
    def name(self) -> Text:
        return "act_dthu_store_req"
    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        print('[%s] <- %s' % (self.name(), tracker.latest_message['text']))

        text = tracker.latest_message['text'].lower().replace('?','')
        text_result = 'Rất tiết chúng tôi không tìm thấy, hãy thử lại!!'
        num, df = None, None
        req, original_time, error = Seek_param_intent.intent_Dthu(text)
        print(req)
        #--- So sánh nhiều Cửa hàng

        if error is None:
            for item_store in req[2]:
                item_store = None if item_store == '~' else item_store

                df = DB_TAU.GET_TAU(('doanh_thu', req[0], req[1], item_store))
                if df["sum_dthu"][0] != None:
                    item_store = ' của cửa hàng ' + item_store.upper() if item_store is not None else ''
                    if original_time is not None:
                        original_time = f'{original_time}'
                    else:
                        if req[0] is not None and req[1] is not None:
                            t_start = Seek_param_intent.convert_date_sql_to_show(req[0])
                            t_end = Seek_param_intent.convert_date_sql_to_show(req[1])
                            original_time = f'từ {t_start} đến {t_end}'
                        elif req[0] is not None and req[1] is None:
                            req[0] = Seek_param_intent.convert_date_sql_to_show(req[0])
                            original_time = f'ngày {t_start}'
                        elif req[0] is None and req[1] is not None:
                            req[1] = Seek_param_intent.convert_date_sql_to_show(req[1])
                            original_time = f'ngày {t_end}'
                        else:
                            original_time = ''

                    num = int(df["sum_dthu"][0])
                    text_result = f'Doanh thu{item_store} {original_time} là: {num:,}'
                    dispatcher.utter_message(
                        text = text_result
                    )
                else:
                    item_store = ('cửa hàng '+ item_store.upper())
                    text_result = f'Rất tiết chúng tôi không tìm thấy cửa hàng {item_store}, hãy thử lại!!'
                    dispatcher.utter_message(
                        text = text_result
                    )
            
        else:
            text_result = error
            dispatcher.utter_message(
                text = text_result
            )

        del text, text_result, req, df, num, original_time, error
        gc.collect
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

        button_time = {
            "type": "postback",
            "title": "📅 Thời gian",
            "payload": "Doanh thu theo thời gian"
        }
        button_store = {
            "type": "postback",
            "title": "🏪 Cửa hàng",
            "payload": "chi tiết bán theo thông tin cửa hàng"
        }
        dispatcher.utter_message(
            text = "Thông tin chi tiết bán tìm theo loại bao gồm:"
            , buttons=[button_time,button_store]
        )
        del button_time, button_store
        gc.collect()

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
        
        #- Xuất các buttons 
        button_time = {
            "type": "account_link",
            "url": "https://accounts.google.com/signin/v2/identifier?hl=vi&passive=true&continue=https%3A%2F%2Fwww.google.com%2F&ec=GAZAmgQ&flowName=GlifWebSignIn&flowEntry=ServiceLogin"
        }
        dispatcher.utter_message(
            text = "Thông tin chi tiết bán tìm theo loại bao gồm:"
            , buttons=[button_time]
        )
        del button_time
        gc.collect()

        return []


''' Chi tiết bán theo cửa hàng - request '''
class act_ctiet_ban_store_req(Action):
    def name(self) -> Text:
        return "act_ctiet_ban_store_req"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        print('[%s] <- %s' % (self.name(), tracker.latest_message['text']))
        
        #- Xuất ra kết quả tìm kiếm

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

        url = "https://www.google.com.vn/search?q='" + tracker.latest_message['text'].replace(" ", "%20") + "'"
        search = {
            "type": "web_url",
            "url": f"{url}",
            "title": "Search Google",
        }
        dispatcher.utter_message(
            text="Xin lỗi bạn vì hiện tại tôi chưa hiểu bạn muốn gì! Bạn hãy bấm vào đây để tôi nhờ chị Google giải đáp nhé: "
            , buttons= [search])
        
        del url, search
        gc.collect()

        return []
