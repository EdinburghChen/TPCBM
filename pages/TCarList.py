import streamlit as st
import sqlite3

conn=sqlite3.connect("./db/bmdb.db")

def QueryTParking():
    try:
        cursor=conn.cursor()
        sqlQueryStr="SELECT 車牌號碼,車位號碼,填表日期 FROM 臨停車位;"
        cursor.execute(sqlQueryStr)    
        for row in cursor.fetchall():
            st.write(row)
        cursor.close()
        del cursor

    except Exception as e:
        st.write("Error: %s" % e)


st.set_page_config(page_title="臨時停車即時資訊", page_icon="📈")

st.markdown("### 臨時停車即時資訊")
st.sidebar.header("臨時停車即時資訊")
QueryTParking()

