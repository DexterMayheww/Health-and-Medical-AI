# Health and Medical AI
There are two main components to this web app:
* AI Diagnostics for diseases like Cancer, Pneumonia and Tuberculosis
* AI Chatbot for people struggling with bad mental health

# Features
* AI Diagnostics: Upload an X-Ray or CT Scan image and choose the type of disease to diagnose and press analyze scan to get the analysis
    * Three different diseases available to be diagnosed: Cancer, Pneumonia and Tuberculosis
* AI Chatbot: Just send a message about your mental health in the message box to get a tailored response from the AI

# Technologies Used
* Language: Python, HTML, CSS, JS
* Libraries:
    * Tensorflow
    * Flask
    * Pillow
    * Langchain
    * Dotenv
* All additional requirements specified in requirements.txt

# Installation and Setup
## Prerequisites
* Pip
* Python 3.11 venv

## Steps
1. Clone/download the repository
```
git clone https://github.com/DexterMayheww/Health-and-Medical-AI.git
cd Health-and-Medical-AI
```
2. Activate venv and install requirements
```
python -m venv .venv
pip install -r requirements.txt
```
3. Run the app
```
python app.py
```
4. Open `http://127.0.0.1:5000/` in your browser of choice

# Licence
This project is licensed under the MIT License.