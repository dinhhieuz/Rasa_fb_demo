from act_process_data.connect import Connect_SQLServer
from act_process_data.connect_tau import Data_TAU
''' Connection Information '''

host = 'localhost'
port = '2022'
server_name = "DESKTOP-9ES2I9R"
db_name = "test_chatbot"
uid = "sa"
pwd = "hieuvippro123"


# host = 'localhost'
# port = '1433'
# server_name = "dsa-server"
# db_name = "test_chatbot"
# uid = "sa"
# pwd = "Dsa@12345"




DB_TAU = Data_TAU(host, port, server_name, db_name, uid, pwd)