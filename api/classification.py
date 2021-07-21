import cv2
from PIL import Image
from model import ConvNet
import numpy as np
import torch
import torch.nn.functional as F
from torchvision import transforms

class Classification(object):
    ''' Class to image preprocessing and classification .
    '''
    def __init__(self):

        self.data_transforms = transforms.Compose([
                               transforms.Resize([64, 64]),
                               transforms.ToTensor()])

        self.model = ConvNet(3)
        self.model.load_state_dict(torch.load("../notebooks/output/rad_classifier.pt"))
        self.model.eval()
   
    def Predict(self,img):
        with torch.no_grad():
            img_processed = self.PreProcessing(img)
            
            output = self.model(img_processed)
            prediction = int(torch.max(output.data, 1)[1].numpy())
            predicted_class = ''
            if (prediction == 0):
                predicted_class = "Covid-19"
            if (prediction == 1):
                predicted_class = "Normal"
            if (prediction == 2):
                predicted_class = "Viral Pneumonia"

            #predicted_class = np.argmax(prediction)
            probs = F.softmax(output, dim=1)
            probs = probs.numpy()[0][prediction]

            return predicted_class, probs

    def PreProcessing(self, img, cliplimit=40):
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Equalizing the contrast of a given grayscale image
        img = cv2.equalizeHist(img)
        # CLAHE Contrast Limited Adaptive Histogram Equalization
        clahe=cv2.createCLAHE(clipLimit=cliplimit)
        img=clahe.apply(img)

        # AdaptiveThreshold
        img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 13, 5)
        # OpenCV to PIL
        img = Image.fromarray(img)

        img = self.data_transforms(img)

        img = img.view(1, 1, 64,64)

        return img



