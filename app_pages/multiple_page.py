import streamlit as st

class Multiple:

    def __init__(self, app_name) -> None:
        self.page = []
        self.app_name = app_name

        st.set_page_config(
            page_title = self.app_name
        )

    def app_page(self, title, function) -> None:
        """ Appends title"""
        self.page.append({'title':title, 'function':function})

    def run(self):
        st.title(self.app_name)
        pages = st.sidebar.radio('Menu',self.page, format_func= lambda pages:pages['title'])
        pages['function']()