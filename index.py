from flask import Flask, render_template, request
from flask_cors import CORS
import os
from luxand import luxand

client = luxand("9c5fdf210f8e41a086b92d65508bc884")


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
    result = client.detect(photo = os.path.join('./outputs',image.filename))

    res = []
    for i in range(len(result)):
        res.append(result[i]['rectangle'])
    
    return {'len':len(res), 'list':res}

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0', port = 3000)