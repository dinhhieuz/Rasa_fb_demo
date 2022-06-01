import sqlmlutils
host = 'localhost'
port = '2022'
server_name = "DESKTOP-9ES2I9R"
db_name = "test_chatbot"
uid = "sa"
pwd = "hieuvippro123"
connection = sqlmlutils.ConnectionInfo(server = server_name, database = db_name, uid= uid , pwd = pwd)
sqlmlutils.SQLPackageManager(connection).install("html2image")