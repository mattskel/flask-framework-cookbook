from flask import Flask
# from configuration import DevelopmentConfig

# Load the instance from the instance folder
app = Flask(__name__,
        static_folder='/static',
        instance_relative_config=True)
# app.config['DEBUG'] = True
# app.config.from_object(DevelopmentConfig)
# app.config.from_object('configuration.DevelopmentConfig') # Using the module path
app.config.from_pyfile('config.cfg')

@app.route('/')
def hello_world():
    return 'Hello to the world from flask!'

if __name__ == '__main__':
    app.run()

