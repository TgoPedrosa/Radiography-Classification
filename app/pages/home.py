import streamlit as st
from PIL import Image

def write():
    
    st.title('Radiography Classification') 
    st.markdown('### The Coronavirus disease 2019 (COVID-19) presents open questions in how we clinically diagnose and assess disease course. In this study, I developed a deep learning convolutional neural network (CNN) that uses the entire chest CT/X-ray volume to automatically classify COVID-19 positive cases along with normal and viral pneumonia. ')

    image = Image.open('images/xray.png')

    st.image(image, use_column_width=True)

    col1, col2 = st.beta_columns([1, 20])
    with col1:
        st.markdown('''
                    <a href="https://github.com/TgoPedrosa/Radiography-Classification">
                        <img src="images/GitHub-Mark-64px.png" />
                    </a>''', unsafe_allow_html=True)
    with col2:
         st.markdown('''
                    <a href="https://www.linkedin.com/in/tgopedrosa/?locale=en_US">
                        <img src="images/linkedin.png" />
                    </a>''', unsafe_allow_html=True)


