from flask import Flask
# from configuration import DevelopmentConfig

app = Flask(__name__)
# app.config['DEBUG'] = True
# app.config.from_object(DevelopmentConfig)
app.config.from_object('configuration.DevelopmentConfig') # Using the module path

@app.route('/')
def hello_world():
    return 'Hello to the world from flask!'

if __name__ == '__main__':
    app.run()

