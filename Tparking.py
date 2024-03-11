import datetime
import streamlit as st
import sqlite3
import requests

# 要發送的訊息
message = '\n'
# LINE Notify 權杖
token = "wQjVbOiFr8DPS014YuPxdUWyCzmw5JoLrtPhBZvlSdd"; //安防群組
#token = "QXrWt5K73eJVZkgQK7nnXEIecoAD4T4maO6L6GDK4CY" #我的剪貼簿

st.set_page_config(page_title="臨時停車", page_icon="🚗")
st.markdown("## 臨時停車登記")

with st.form("my_form"):
   #st.write("Inside the form")
   st.markdown(f'日期：{datetime.date.today()}')

   leveloption = st.selectbox('停放樓層',("B2","B3"))
   parkingNo=st.text_input('車位號碼：')
   carNo=st.text_input('輸入車牌：')
   # Every form must have a submit button.
   submitted = st.form_submit_button("確定")

if submitted:
  #st.write(f'{leveloption}-{parkingNo}：{carNo}')
  st.write(f'已登記 :red[{carNo}] 臨停於 :red[{leveloption}-{parkingNo}] 車位，感謝您的配合!')
  #Line Notify
  # HTTP 標頭參數與資料
  #tmpdate=datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
  myday=datetime.datetime.today().strftime('%Y-%m-%d')
  mytime=datetime.datetime.today().strftime('%H:%M:%S')
  headers = {"Authorization": "Bearer " + token}
  message+=f'日期：{myday}\n時間：{mytime}\n車位：{leveloption}-{parkingNo}\n車牌：{carNo}'
  data = {'message': message}
  # 以 requests 發送 POST 請求
  requests.post("https://notify-api.line.me/api/notify",headers=headers, data=data)
