import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np
from pathlib import Path
from datetime import datetime
import datetime as dt
import streamlit_authenticator as stauth
import plotly.express as px
import mysql.connector
from mysql.connector import Error
from io import BytesIO
import xlsxwriter

st.set_page_config(page_title="Decode Trading Competition", page_icon=":bar_chart:", layout="wide")

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>

"""

hide_dataframe_row_index = """
<style>
.row_heading.level0 {display:none}
.blank {display:none}
</style>

"""
st.markdown(hide_dataframe_row_index, unsafe_allow_html=True)


def hide_anchor_link():
    st.markdown("""
        <style>
        .css-15zrgzn {display: none}
        </style>
        """, unsafe_allow_html=True)
        
hide_anchor_link()
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 


col1, col2, col3 = st.columns([120,120,120])
with col1:
    st.write("")
with col2:
    st.image("/Users/decod/Desktop/logo.png", width = 500)
    st.title("Trading Competition Ranking")
with col3:
    st.write("")
    
hide_img_fs = '''
<style>
button[title="View fullscreen"]{
    visibility: hidden;}
</style>
'''

st.markdown(hide_img_fs, unsafe_allow_html=True)
data = pd.read_excel('C:/Users/decod/Desktop/check 1.xlsx', sheet_name='Sheet1').astype(str)
st.table(data)


