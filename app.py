from flask import Flask, render_template, request
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload directory exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        image = request.files['image']
        if image:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
            image.save(filepath)
            # Dummy analysis (pretend to analyze image)
            result = "No forgery detected"
            return render_template('index.html', result=result, image_name=image.filename)
    return render_template('index.html', result=None)

if __name__ == '__main__':
    app.run(debug=True)
