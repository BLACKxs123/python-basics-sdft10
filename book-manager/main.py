from flask import Flask

# create an instance of my flask class so as to generate a new flask app
app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to my first Flask Book Manager app!"


if __name__ == '__main__':
    app.run(debug=True)