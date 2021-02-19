from flask import Flask, render_template, request
from flask_cors import CORS
import os
from luxand import luxand


import sys
import numpy as np
import matplotlib.pyplot as plt

import matplotlib.patches as patches
import os
from PIL import Image
import cv2
import warnings
warnings.filterwarnings("ignore")

import os
import xmltodict

import torch
from torchvision import datasets,transforms,models
from torch.utils.data import Dataset,DataLoader

import torch.optim as optim
from mtcnn import MTCNN

from PIL import Image
import requests
from io import BytesIO


#client = luxand("9c5fdf210f8e41a086b92d65508bc884")


def trans(bndbox,newimage):
    a,b,c,d=bndbox["box"]
    image_crop=transforms.functional.crop(newimage, b,a,d-b,c-a)
    my_transform=transforms.Compose([transforms.Resize((226,226)),
                                     transforms.RandomCrop((224,224)),
                                     transforms.ToTensor()])(image_crop)
    return my_transform

def tag_plot(bndbox,filepath,predicted):
    configut=["with_mask","without_mask","mask_weared_incorrect"]
    x=plt.imread(filepath)
    fig,ax=plt.subplots(1)
    ax.axis("off")
    fig.set_size_inches(15,10)
    for i,j in zip(bndbox,predicted):
        a,b,c,d=i["box"]
        patch=patches.Rectangle((a,b),c,d,linewidth=1, edgecolor='r',facecolor="none",)
        ax.imshow(x)
        ax.add_patch(patch)

def testing(filepath):
    configut=["with_mask","without_mask","mask_weared_incorrect"]
    img = cv2.cvtColor(cv2.imread(filepath), cv2.COLOR_BGR2RGB)
    newimage=Image.open(filepath).convert("RGB")
    bndbox=detect.detect_faces(img)
    if len(bndbox)==1:
        image_pred=trans(bndbox[0],newimage).unsqueeze(0)
        _, pred=torch.max(model(image_pred.to(device)),1)
        tag_plot(bndbox,filepath,predicted=pred)
    else:
        predicted=[]
        for i in bndbox:
            image_pred=trans(i,newimage).unsqueeze(0)
            _, pred=torch.max(model(image_pred.to(device)),1)
            predicted.append(pred)
        tag_plot(bndbox,filepath,predicted)
    
    return bndbox

device = torch.device("cpu")
model = torch.load(open("./resnet_model_face", "rb"), map_location=device)

detect = MTCNN()
model = model.eval()


app = Flask(__name__, static_folder='templates')
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
@app.route("/")
def hello():
    return render_template('index.html')
 
@app.route('/api', methods = ['GET', 'POST'])
def upload_file():
    image = request.files['uploadFile']
    image.save(os.path.join('./outputs',image.filename))
    photo = os.path.join('./outputs',image.filename)
    result = testing(photo);

    res = []
    for i in range(len(result)):
        res.append({'left':result[i]['box'][0], 'top':result[i]['box'][1], 
                    'right':result[i]['box'][0]+result[i]['box'][2], 
                    'bottom':result[i]['box'][1]+result[i]['box'][3]})
        
    print(res)
    return {'len':len(res), 'list':res}

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0', port = 3000)