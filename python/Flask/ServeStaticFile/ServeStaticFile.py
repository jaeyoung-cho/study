from flask import Flask

# app = Flask(__name__, static_url_path='')
app = Flask(__name__, static_url_path='/test')

@app.route('/')
def root():
    return app.send_static_file('index.html')


if __name__ == '__main__':
    app.run()