import io
from flask import Flask, request, render_template, jsonify
from PIL import Image
from tensorflow.keras.models import load_model
import numpy as np
import base64

tb_model = load_model('models/tb-model.h5')
cancer_model = load_model('models/cancer-model.h5')
pneumonia_model = load_model('models/pneumonia-model.h5')

app = Flask(__name__, template_folder='templates')

print(app.url_map)


@app.route('/', methods=['GET', 'POST'])
def index():
    print(app.url_map)
    return render_template('index.html')

@app.route('/disease-detection', methods=['GET'])
def diseaseDetection():
    print(app.url_map)
    return render_template('disease-detection.html')

@app.route('/disease-detection', methods=['POST'])
def upload():
    print(app.url_map)
    if 'image' not in request.files:
        error = 'No image provided'
        return render_template('disease-detection.html', error=error)

    file = request.files['image']
    if file.filename == '':
        error = 'No selected image'
        return render_template('disease-detection.html', error=error)
    
    selected_disease = request.form.get('disease')

    try:
        image = Image.open(io.BytesIO(file.read()))
        
        if selected_disease == 'tb':
            image = image.resize((96, 96))
            image = image.convert('RGB')
            buffered = io.BytesIO()
            image.save(buffered, format="JPEG")
            img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')
            image_array = (np.array(image).reshape(-1, 96, 96, 3) / 127.5) - 1
            prediction = tb_model.predict(image_array)
            formatted_tb = round(prediction[0][0] * 100, 2)
            formatted_normal = round(prediction[0][1] * 100, 2)
            classification = ['Tuberculosis', 'Normal'][np.argmax(prediction)]
            return render_template(
                'disease-detection.html',
                tb_classification=classification,
                tb=formatted_tb,
                normal=formatted_normal,
                image_data=img_str
            )

        elif selected_disease == 'cancer':
            image = image.resize((50, 50))
            image = image.convert('RGB')
            buffered = io.BytesIO()
            image.save(buffered, format="JPEG")
            img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')
            image_array = (np.array(image).reshape(-1, 50, 50, 3) / 127.5) - 1
            prediction = cancer_model.predict(image_array)
            formatted_cancer = round(prediction[0][0] * 100, 2)
            formatted_benign = round(prediction[0][1] * 100, 2)
            classification = ['Cancer', 'Benign'][np.argmax(prediction)]
            return render_template(
                'disease-detection.html',
                cancer_classification=classification,
                cancer=formatted_cancer,
                benign=formatted_benign,
                image_data=img_str
            )

        elif selected_disease == 'pneumonia':
            image = image.resize((224, 224))
            image = image.convert('RGB')
            buffered = io.BytesIO()
            image.save(buffered, format="JPEG")
            img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')
            image_array = (np.array(image).reshape(-1, 224, 224, 3) / 127.5) - 1
            prediction = pneumonia_model.predict(image_array)
            formatted_viral = round(prediction[0][0] * 100, 2)
            formatted_pn_normal = round(prediction[0][1] * 100, 2)
            formatted_bacterial = round(prediction[0][2] * 100, 2)
            classification = ['Bacterial', 'Viral', 'Normal'][np.argmax(prediction)]
            return render_template(
                'disease-detection.html',
                pn_classification=classification,
                viral=formatted_viral,
                pn_normal=formatted_pn_normal,
                bacterial=formatted_bacterial,
                image_data=img_str
            )
        else:
            error = 'Invalid disease selection'
            return render_template('disease-detection.html', error=error)

    except Exception as e:
        error = str(e)
        return render_template('disease-detection.html', error=error)

if __name__ == '__main__':
    app.run(debug=True)