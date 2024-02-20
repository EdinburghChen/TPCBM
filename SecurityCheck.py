import streamlit as st
import sqlite3

#建立一個空串列用於存放結果
queryResult=[]

st.set_page_config(page_title="保全AI助理", page_icon="😎")
st.markdown("保全AI助理")

with st.form("my_form"):
   #st.write("Inside the form")
   queryName=st.text_input('輸入姓名：')

   # Every form must have a submit button.
   submitted = st.form_submit_button("查詢")
   if submitted:
       st.write( ":red["+queryName+"]" )
       #建立資料庫連線
       conn=sqlite3.connect("./bmdb.db")
       try:
          cursor=conn.cursor()
          sqlQueryStr="SELECT 姓名代號,姓名,單位代號,單位名稱,聯絡資訊 FROM 關懷人員 WHERE 姓名 like '%" + queryName  +"%';"
          cursor.execute(sqlQueryStr)

          #建立一個空串列用於存放結果
          #queryResult=[]
          queryResult=cursor.fetchall()
          #將查詢結果逐一加入串列
          #for row in cursor.fetchall():
          #   queryResult.append(row[0])

          cursor.close()
          del cursor
       except Exception as e:
         st.write("Error: %s" % e)
    
  
   if ( len(queryResult)>=1 ):
       st.write("建議處置：若該員識別證為 " + "**:red["+ queryResult[0][3] + "]** 員工，請聯繫 " +"**:red[" + queryResult[0][4] +"]** 協助處理。")
   else:
      st.write('請依大樓門禁管理要點辦理!!')  
#st.write("Outside the form")
