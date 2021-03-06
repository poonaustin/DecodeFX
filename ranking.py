import streamlit as st
import pandas as pd

st.set_page_config(page_title="Decode Trading Competition", page_icon=":bar_chart:", layout="wide")

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>

"""

def hide_anchor_link():
    st.markdown("""
        <style>
        .css-15zrgzn {display: none}
        </style>
        """, unsafe_allow_html=True)
        
hide_anchor_link()
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

hide_table_row_index = """
            <style>
            tbody th {display:none}
            .blank {display:none}
            </style>
            """

st.markdown(hide_table_row_index, unsafe_allow_html=True)


col1, col2, col3 = st.columns([120,130,120])
with col1:
    st.write("")
with col2:
    st.image("logo.png", width = 500)
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
data = pd.read_excel('check 1.xlsx', sheet_name='Sheet1')
st.table(data.style.set_precision(2))


