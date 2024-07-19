# __init__.py  
import streamlit as st  
from knowledge_gpt.components import main_app, sidebar, uploader  
from knowledge_gpt.utils import page_config  
  
# Set page configuration  
page_config.setup()  
  
# Hide default formatting  
page_config.hide_default_format()  
  
# Build the sidebar  
sidebar.build()  
  
# Main application  
main_app.run()  