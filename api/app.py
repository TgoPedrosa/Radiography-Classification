import cv2
import numpy as np
import json
from flask import Flask, jsonify, request, Response
from classification import Classification

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'

classification = Classification()
@app.route('/')
def home():
    return '''<h1>Radiography Classification</h1>
              <p>Radiography Classification for COVID-19 positive cases along with Normal and Viral Pneumonia Use of CNN to detect COVID-19 through radiography and/or computed tomography images</p>'''


@app.route('/predict', methods=['POST'])
def getClassification():
    r = request
    # convert string of image data to uint8
    nparr = np.fromstring(r.data, np.uint8)
    # decode image
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    predict, proba = classification.Predict(img)
    
    response = {'class':predict, 'proba': str(proba)}

    return Response(response=json.dumps(response), status=200, mimetype="application/json")

@app.errorhandler(404)
def not_found(e):
    ''' Function to return error 404.

        :rtype: json

    '''
    """Page not found."""
    return jsonify(error=str(e)), 404


if __name__ == '__main__':
      app.run(host="0.0.0.0", port=5000)