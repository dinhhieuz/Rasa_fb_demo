from act_process_data.database import DB_TAU

class Authorized_user():
    def __init__(self, send_id) -> None:
        df = DB_TAU.GET_TAU(('authorized', None, None, None, send_id))
        if len(df) > 0 :
            self.idfb_user = df['ID User'][0]
            self.f_name = df['First name'][0]
            self.l_name = df['Last name'][0]
            self.act_permission = df['Action permission'][0].split(', ')
        else:
            self.idfb_user = None
            self.f_name = None
            self.l_name = 'bạn'
            self.act_permission = []
        
    def position():
        #? -> Phân theo cấp độ, xuất database là 1 chức vụ, thì sữ dụng chức vụ để đưa ra quyền hạn
        #? -> Ví dụ: Xuất database = "Giám đốc" -> hàm sẽ trả  về 1 tập các actions được sữ dụng
        return