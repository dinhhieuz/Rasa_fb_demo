#!------------------------------------------------------------------------------------------------------------------------
#1---- Run action
pushd D:\HieuCali\File of Hieu\Project\DSA Company\Project\ChatBox_RASA\dsa_demo_sell_materia\chatbot_demo
conda activate envchatbot
rasa run actions

#2---- Run Rasa
pushd D:\HieuCali\File of Hieu\Project\DSA Company\Project\ChatBox_RASA\dsa_demo_sell_materia\chatbot_demo
conda activate envchatbot
rasa train && rasa shell --debug

#3---- Run Rasa Server
pushd D:\HieuCali\File of Hieu\Project\DSA Company\Project\ChatBox_RASA\dsa_demo_sell_materia\chatbot_demo
conda activate envchatbot
rasa run --endpoints endpoints.yml --credentials credentials.yml --cor '*' --debug

#-Run with port 5002 
# DESCRIPTION: sữ dụng port 5002 khác so với mặt định 5005 để sữ dụng cho bản thân Rasa tự tương tác với chúng
# nhầm mục đích trách bị xung đội trong quá trình gữi Port API với nhau
pushd D:\HieuCali\File of Hieu\Project\DSA Company\Project\ChatBox_RASA\dsa_demo_sell_materia\chatbot_demo
conda activate envchatbot
rasa run -m models --endpoints endpoints.yml --port 5002 --credentials credentials.yml

#!-----------------------------------
#4---- Run Ngrok
pushd D:\HieuCali\File of Hieu\Project\DSA Company\Project\ChatBox_RASA\dsa_demo_sell_materia\draft
ngrok authtoken 25GxQSVCB2LLMbAGyXSYIE8ROCU_3LPoxRnaf37Xfv3qzKRzo
ngrok http 5005
#?: <URL:https>/webhooks/facebook/webhook

#5---- Run Xampp
pushd D:\HieuCali\File of Hieu\Project\DSA Company\Project\ChatBox_RASA\dsa_demo_sell_materia\draft
ngrok authtoken 25GvKMP5MlN5WE5TWwJot1EJOqL_4CmGwfSwzSBsvFfKUPNcf 
ngrok http 80
