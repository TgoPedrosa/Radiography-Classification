import streamlit as st
import cv2
import requests
import json
import numpy as np
from PIL import Image
from pathlib import Path

# Funcao para gerar a lista das correlacoes
def makePredict(img, extension):
    #addr = 'http://172.17.0.8:5000'
    addr = 'https://rad-class-api.herokuapp.com/'
    test_url = addr + '/predict'

    # prepare headers for http request
    content_type = 'image/'+extension.split('.')[1]
    headers = {'content-type': content_type}

    image = Image.open(img)
    img_array = np.array(image)

    # encode image 
    _, img_encoded = cv2.imencode(extension, img_array)
    # send http request with image and receive response
    response = requests.post(test_url, data=img_encoded.tostring(), headers=headers)
    result = json.loads(response.text)
    return result



def write():

    st.markdown('''
    # Classification of chest X-Ray using CNN 

    Radiography Classification for COVID-19 positive cases along with Normal and Viral Pneumonia Use of CNN to detect COVID-19 through radiography and/or computed tomography images 

    ''')
   

    file = st.file_uploader("Upload File",type=['png','jpeg','jpg'], accept_multiple_files=False)
    
    if file == None:
        st.warning('No file selected.')
    else:
        file_contents = file.getvalue()
        st.markdown("### File")
        st.image(file_contents)

        if st.button("Predict"):
            extension = Path(file.name).suffix
            result = makePredict(file, extension)
            st.markdown('### Result: ' + result['class'])
            st.markdown('### Probability: ' + result['proba'])
