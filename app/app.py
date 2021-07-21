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

    menu = MENU[menu_selection]
    with st.spinner(f"Loading {menu_selection} ..."):
        menu.write()


if __name__ == "__main__":
    main()