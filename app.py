from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify, request

import requests


app = Flask(__name__)



@app.route('/')
def home():
    # Fetch JSON data from external API
    response = requests.get('https://aislyn.live/API/d-get.php')
    
    # Check if request was successful
    if response.status_code == 200:
        readings = response.json()  
       
    else:
        readings = {} 

    # Pass readings to the template
    return render_template('index.html', readings=readings)

if __name__ == '__main__':
    app.run(debug=True)
