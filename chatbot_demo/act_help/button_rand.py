''' Random Button for the other actions'''
import random

class button_rand():
    ''' Doanh thu - thời gian '''
    def dthu_time():
        temp_button_list = []

        temp_button_list.append({
            "type": "postback",
            "title": "Hôm nay",
            "payload": "Doanh thu hôm nay?"
        })
        temp_button_list.append({
            "type": "postback",
            "title": "Hôm qua",
            "payload": "Doanh thu hôm qua?"
        })
        temp_button_list.append({
            "type": "postback",
            "title": "Tuần này",
            "payload": "Doanh thu tuần này?"
        })
        temp_button_list.append({
            "type": "postback",
            "title": "Tuần trước",
            "payload": "Doanh thu tuần trước?"
        })
        temp_button_list.append({
            "type": "postback",
            "title": "Tháng này",
            "payload": "Doanh thu tháng này?"
        })
        temp_button_list.append({
            "type": "postback",
            "title": "Tháng trước",
            "payload": "Doanh thu tháng trước?"
        })
        temp_button_list.append({
            "type": "postback",
            "title": "Quý 1",
            "payload": "Doanh thu của quý 1?"
        })
        temp_button_list.append({
            "type": "postback",
            "title": "Quý 2 năm trước",
            "payload": "Doanh thu của quý 2 năm trước?"
        })
        temp_button_list.append({
            "type": "postback",
            "title": "Năm trước",
            "payload": "Doanh thu của năm trước?"
        })
        temp_button_list.append({
            "type": "postback",
            "title": "Năm nay",
            "payload": "Doanh thu của năm nay?"
        })
        temp_button_list.append({
            "type": "postback",
            "title": "Tháng này cửa hàng CH3",
            "payload": "Doanh thu tháng này của cửa hàng CH1 ?"
        })
        temp_button_list.append({
            "type": "postback",
            "title": "Tuần này cửa hàng CH1",
            "payload": "Doanh thu tuần này của cửa hàng CH1?"
        })
        temp_button_list.append({
            "type": "postback",
            "title": "Thứ 2 tuần này",
            "payload": "Doanh thu thứ 2 tuần này?"
        })
        temp_button_list.append({
            "type": "postback",
            "title": "Thứ 3 tuần trước",
            "payload": "Doanh thu thứ 3 tuần trước?"
        })
        temp_button_list.append({
            "type": "postback",
            "title": "Thứ 5 tuần vừa rồi",
            "payload": "Doanh thu thứ 5 tuần vừa rồi của cửa hàng CH1 ?"
        })
        temp_button_list.append({
            "type": "postback",
            "title": "ngày 3 tháng 1 năm 2022",
            "payload": "Doanh thu của ngày 3 tháng 1 năm 2022 ?"
        })
        temp_button_list.append({
            "type": "postback",
            "title": "Tháng 12 năm 2021 đến bây giờ",
            "payload": "Doanh thu của tháng 1 năm 2022 đến bây giờ?"
        })
        return random.sample(temp_button_list, k=3)

    ''' Doanh thu - cửa hàng '''
    def dthu_store():
        temp_button_list = []

        temp_button_list.append({
            "type": "postback",
            "title": "Cửa hàng CH1", 
            "payload": "Doanh thu cửa hàng CH1"
        })
        temp_button_list.append({
            "type": "postback",
            "title": "Cửa hàng CH3 hôm nay", 
            "payload": "Doanh thu cửa hàng CH3 hôm nay"
        })
        temp_button_list.append({
            "type": "postback",
            "title": "Cửa hàng CH2 tuần nay", 
            "payload": "Doanh thu cửa hàng CH2 trong tuần nay"
        })
        temp_button_list.append({
            "type": "postback",
            "title": "C.hàng CH1 năm nay", 
            "payload": "Doanh thu cửa hàng CH1 trong năm nay"
        })
        temp_button_list.append({
            "type": "postback",
            "title": "C.hàng CH3 năm trước", 
            "payload": "Doanh thu cửa hàng CH3 trong năm trước"
        })
        temp_button_list.append({
            "type": "postback",
            "title": "C.hàng CH2 thứ 5 tuần này", 
            "payload": "Doanh thu cửa hàng CH2 trong thứ 5 tuần này"
        })
        temp_button_list.append({
            "type": "postback",
            "title": "C.hàng CH3 thứ 2 tuần trước", 
            "payload": "Doanh thu cửa hàng CH3 trong thứ 2 tuần trước"
        })
        temp_button_list.append({
            "type": "postback",
            "title": "C.hàng CH2 thứ 3 tuần trước", 
            "payload": "Doanh thu cửa hàng CH2 trong thứ 3 tuần trước"
        })
        temp_button_list.append({
            "type": "postback",
            "title": "C.hàng CH2 so CH1 tuần trước", 
            "payload": "Doanh thu cửa hàng CH2 so CH1 trong tuần trước"
        })
        temp_button_list.append({
            "type": "postback",
            "title": "C.hàng CH2, CH1, CH3 tháng này", 
            "payload": "Doanh thu cửa hàng CH1, CH2 và CH3 trong tuần trước"
        })
        temp_button_list.append({
            "type": "postback",
            "title": "C.hàng CH2 so CH1 tuần này", 
            "payload": "Doanh thu cửa hàng CH2 so CH1 trong tuần này"
        })
        temp_button_list.append({
            "type": "postback",
            "title": "C.hàng CH2, CH1, CH3 tháng trước", 
            "payload": "Doanh thu cửa hàng CH1, CH2 và CH3 trong tháng trước"
        })
        temp_button_list.append({
            "type": "postback",
            "title": "C.hàng CH1 quý 1",
            "payload": "Doanh thu cửa hàng CH1 của quý 1?"
        })
        temp_button_list.append({
            "type": "postback",
            "title": "C.Hg CH3 quý 2 năm trước",
            "payload": "Doanh thu cửa hàng CH1 của quý 2 năm trước?"
        })
        temp_button_list.append({
            "type": "postback",
            "title": "C.Hg CH3 tháng 1 năm 2022",
            "payload": "Doanh thu cửa hàng CH1 của tháng 1 năm 2022 ?"
        })
        temp_button_list.append({
            "type": "postback",
            "title": "C.Hg CH3 tháng 1 đến nay",
            "payload": "Doanh thu cửa hàng CH1 của tháng 1 đến nay ?"
        })
        temp_button_list.append({
            "type": "postback",
            "title": "C.Hg CH3 quý 2 năm trước",
            "payload": "Doanh thu cửa hàng CH1 của quý 2 năm trước?"
        })
        return random.sample(temp_button_list, k=3)
        
    ''' Chi tiết bán - cửa hàng '''
    def ctiet_ban_store():
        temp_button_list = []

        temp_button_list.append({
            "type": "postback",
            "title": "Cửa hàng CH1",
            "payload": "Thông tin chi tiết bán của cửa hàng CH1"
        })
        temp_button_list.append({
            "type": "postback",
            "title": "Cửa hàng CH2",
            "payload": "Thông tin chi tiết bán của cửa hàng CH2"
        })
        temp_button_list.append({
            "type": "postback",
            "title": "Cửa hàng CH3",
            "payload": "Thông tin chi tiết bán của cửa hàng CH3"
        })

        temp_button_list.append({
            "type": "postback",
            "title": "Cửa hàng CH1 tuần trước",
            "payload": "Thông tin chi tiết bán của cửa hàng CH1 trong tuần nay"
        })
        temp_button_list.append({
            "type": "postback",
            "title": "Cửa hàng CH2 tuần trước",
            "payload": "Thông tin chi tiết bán của Cửa hàng CH2 trong tuần trước"
        })
        temp_button_list.append({
            "type": "postback",
            "title": "C.hàng CH3 thứ 3 tuần trước",
            "payload": "Thông tin chi tiết bán của cửa hàng CH3 thứ 3 tuần trước"
        })

        temp_button_list.append({
            "type": "postback",
            "title": "C.hàng CH1 thứ 2 tuần này",
            "payload": "Thông tin chi tiết bán của cửa hàng CH1 trong thứ 2 tuần này"
        })
        temp_button_list.append({
            "type": "postback",
            "title": "Cửa hàng CH2 tháng này",
            "payload": "Thông tin chi tiết bán của Cửa hàng CH2 trong tháng này"
        })
        temp_button_list.append({
            "type": "postback",
            "title": "Cửa hàng CH3 tháng trước",
            "payload": "Thông tin chi tiết bán của cửa hàng CH3 trong tháng trước"
        })
        temp_button_list.append({
            "type": "postback",
            "title": "C.Hg CH3 quý 2 năm trước",
            "payload": "Thông tin chi tiết bán cửa hàng CH1 của quý 2 năm trước?"
        })
        temp_button_list.append({
            "type": "postback",
            "title": "C.Hg CH3 tháng 1 đến nay",
            "payload": "Thông tin chi tiết bán cửa hàng CH1 của tháng 1 đến nay?"
        })
        temp_button_list.append({
            "type": "postback",
            "title": "C.Hg CH3 quý 2 năm trước",
            "payload": "Thông tin chi tiết bán cửa hàng CH1 của quý 2 năm trước?"
        })

        temp_button_list.append({
            "type": "postback",
            "title": "Cửa hàng CH1 năm nay",
            "payload": "Thông tin chi tiết bán của cửa hàng CH1 trong năm nay"
        })
        temp_button_list.append({
            "type": "postback",
            "title": "Cửa hàng CH2 năm trước",
            "payload": "Thông tin chi tiết bán của Cửa hàng CH2 trong năm trước"
        })
        temp_button_list.append({
            "type": "postback",
            "title": "C.hàng CH3 ngày 03/01/2021",
            "payload": "Thông tin chi tiết bán của cửa hàng CH3 trong ngày 03/01/2021"
        })
        return random.sample(temp_button_list, k=3)
        