import streamlit as st
import pages.home
import pages.predict


MENU = {
    "Home" : pages.home,
    "Predict" : pages.predict
}

def main():

    st.sidebar.title("Chest X-ray classifier")
    menu_selection = st.sidebar.radio("Choose an option", list(MENU.keys()))
    with st.sidebar:
        col1, col2 = st.beta_columns([1, 5])
        with col1:
            st.markdown('''
                        <a href="https://github.com/TgoPedrosa/" target="_blank" title="GitHub">
                            <img src="https://raw.githubusercontent.com/TgoPedrosa/Radiography-Classification/devel/app/images/GitHub-Mark-64px.png" widht=32 height=32/>
                        </a>''', unsafe_allow_html=True)
        with col2:
            st.markdown('''
                        <a href="https://www.linkedin.com/in/tgopedrosa/?locale=en_US" target="_blank" title="Linkedin">
                            <img src="https://raw.githubusercontent.com/TgoPedrosa/Radiography-Classification/devel/app/images/linkedin.png"  widht=32 height=32/>
                        </a>''', unsafe_allow_html=True)
    menu = MENU[menu_selection]
    with st.spinner(f"Loading {menu_selection} ..."):
        menu.write()
        
    
if __name__ == "__main__":
    main()