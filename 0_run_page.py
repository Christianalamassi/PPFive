import streamlit as st
from app_pages.multiple_page import Multiple

from app_pages.summary_page import summery_page
from app_pages.leaf_visualizer import leaf
from app_pages.mildew_detector import mildew
from app_pages.performance_metric import perfomance

# Create an instance
app = Multiple(app_name ="Mildew Detection in Cherry Leaves")

# Add your app pages here using .add_page()
app.app_page("Summary page", summery_page)
app.app_page("Cherry  leaf visualizer", leaf)
app.app_page('Mildew detector', mildew)
app.app_page('Performance metric', perfomance)

app.run()