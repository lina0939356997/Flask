from flask import Flask

app = Flask(__name__)
app.config.from_pyfile('Flask_03_ConfigDemo.py', silent=True)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
