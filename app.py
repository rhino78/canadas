from flask import Flask, render_template, url_for

app = Flask(__name__)

# Route for the main page
@app.route('/')
def home():
    return render_template('index.html')

# Running the Flask application
if __name__ == '__main__':
    app.run(debug=True)

