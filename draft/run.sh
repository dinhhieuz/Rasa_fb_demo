#---- Run Ngrok
pushd D:\HieuCali\File of Hieu\Project\DSA Company\Project\ChatBox_RASA\dsa_demo_sell_materia\draft
http ngrok 5005

#---- Run action
pushd D:\HieuCali\File of Hieu\Project\DSA Company\Project\ChatBox_RASA\dsa_demo_sell_materia\chatbot_demo
conda activate envchatbot
rasa run actions

#---- Run Rasa
pushd D:\HieuCali\File of Hieu\Project\DSA Company\Project\ChatBox_RASA\dsa_demo_sell_materia\chatbot_demo
conda activate envchatbot
rasa train && rasa shell --debug

#---- Run Rasa Server
pushd D:\HieuCali\File of Hieu\Project\DSA Company\Project\ChatBox_RASA\dsa_demo_sell_materia\chatbot_demo
conda activate envchatbot
rasa run --endpoints endpoints.yml --credentials credentials.yml --cor '*' --debug
