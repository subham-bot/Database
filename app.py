from flask import Flask, render_template, request, redirect, url_for, flash
import csv
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def save_to_csv(data, filename='checkup_data.csv'):
    file_exists = os.path.isfile(filename)
    
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        
        if not file_exists:
            writer.writerow(["Name", "Phone Number", "Sugar Level", "Blood Pressure", "Weight"])
        
        writer.writerow(data)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    phone = request.form['phone']
    sugar = request.form['sugar']
    bp = request.form['bp']
    weight = request.form['weight']
    
    if not (name and phone and sugar and bp and weight):
        flash("All fields are required", "error")
        return redirect(url_for('index'))
    
    user_data = [name, phone, sugar, bp, weight]
    save_to_csv(user_data)
    
    flash("Data saved successfully", "success")
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)