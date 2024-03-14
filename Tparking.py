from datetime import datetime, timedelta
import streamlit as st
import sqlite3
import requests
from pytz import timezone

conn=sqlite3.connect("./db/bmdb.db")

# 要發送的訊息
message = '\n'
# LINE Notify 權杖
#token = "wQjVbOiFr8DPS014YuPxdUWyCzmw5JoLrtPhBZvlSdd"; #//安防群組
token = "QXrWt5K73eJVZkgQK7nnXEIecoAD4T4maO6L6GDK4CY" #我的剪貼簿

st.set_page_config(page_title="臨時停車", page_icon="🚗")
st.markdown("## 臨時停車登記")

# 設定台灣台北時區
#tz = timezone('Asia/Taipei')
# 取得目前時間
now = datetime.now() + timedelta(hours=8)

def sendLineNotify(innow,inleveloption,inparkingNo,incarNo,imessage):
  
  myday=innow.strftime('%Y-%m-%d')
  mytime=innow.strftime('%H:%M:%S')
 
  # HTTP 標頭參數與資料
  headers = {"Authorization": "Bearer " + token}
  imessage+=f'日期：{myday}\n時間：{mytime}\n車位：{inleveloption}-{inparkingNo}\n車牌：{incarNo}'
  data = {'message': imessage}
  # 以 requests 發送 POST 請求
  requests.post("https://notify-api.line.me/api/notify",headers=headers, data=data)
  writetoSQLite(inparkingNo,inleveloption,incarNo,innow)
  return  

def writetoSQLite(inparkingNo,inleveloption,incarNo,indatetime):
   try:
       # 建立資料庫連線 SQLite
       cursor=conn.cursor()
       sqlstr='INSERT INTO 臨停車位 (車牌號碼,車位號碼,填表日期) VALUES (?,?,?);'
       cursor.execute(sqlstr,(incarNo,inleveloption+'-'+inparkingNo,indatetime.strftime('%Y-%m-%d %H:%M:%S')))
       conn.commit()
   except Exception as e:
      print("Error: %s" % e) 
   #Close the cursor and delete it
   cursor.close()
   del cursor 
   return  

with st.form("my_form"):
   #st.write("Inside the form")
   mynow=now.strftime('%Y-%m-%d %H:%M:%S')
   st.markdown(f'日期：{mynow}')

   leveloption = st.selectbox('停放樓層',("B2","B3"))
   parkingNo=st.text_input('車位號碼：')
   carNo=st.text_input('輸入車牌：')
   # Every form must have a submit button.
   submitted = st.form_submit_button("確定")

if submitted & ((parkingNo != "") & (carNo != "")):
  #st.write(f'{leveloption}-{parkingNo}：{carNo}')
  st.write(f'已登記 :red[{carNo}] 臨停於 :red[{leveloption}-{parkingNo}] 車位，感謝您的配合!')
  #Line Notify
  sendLineNotify(now,leveloption,parkingNo,carNo,message)



