from st_login import Login
import streamlit as st
from streamlit_option_menu import option_menu
from st_login import Login
from main import run


class CustomLogin(Login):
    def nav_sidebar(self):
        """
        Creates the side navigaton bar
        """
        main_page_sidebar = st.sidebar.empty()
        with main_page_sidebar:
            selected_option = option_menu(
                menu_title='User Info',
                menu_icon='list-columns-reverse',
                icons=['box-arrow-in-right', 'person-plus', 'x-circle', 'arrow-counterclockwise'],
                options=['Login','Create Account', 'Forgot Password?','Reset Password'],
                styles={
                    "container": {"padding": "5px"},
                    "nav-link": {"font-size": "14px", "text-align": "left", "margin": "0px"}})
        return main_page_sidebar, selected_option


is_login = CustomLogin(auth_token='OTFjYjhlNzQtMDVkYy00N2U2LWE2ZTgtZjk2YzAxYjdjNzQy',
                       company_name="Osthailyd Bautista",
                       width=200, height=250,
                       logout_button_name='Logout', hide_menu_bool=True,
                       hide_footer_bool=False,
                       lottie_url='https://assets2.lottiefiles.com/packages/lf20_jcikwtux.json').build_login_ui()

if is_login is True:
    run()
    