from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add-student')
def add_student():
    return render_template('student_form.html')

@app.route('/submit-student', methods=['POST'])
def submit_student():
    student_data = {
        'student_id': request.form['student_id'],
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'dob': request.form['dob'],
        'gender': request.form['gender'],
        'email': request.form['email'],
        'phone_no': request.form['phone_no'],
        'address': request.form['address'],
        'department': request.form['department'],
        'skills': request.form['skills'],
    }
    image = request.files['image']
    image_path = os.path.join(UPLOAD_FOLDER, image.filename)
    image.save(image_path)
    
    print("Student Data:", student_data)
    print("Image saved to:", image_path)
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
