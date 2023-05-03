import streamlit as st
from utils.multipage import Multipage
from utils import dbManager
from pages import APPEP


app=MultiPage()
db= dbManager.DbManager('mongodb:27017')

st.set-page-config(
    page_title = "BIENVENIDO A APPEP",
    page_icon =":book:",
    layout = 'centered',
    initial_sidebar_state = "auto",)
    
st.tittle("APPPEP") 
  
  st.markdown("""
              