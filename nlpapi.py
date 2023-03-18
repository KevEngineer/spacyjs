import spacyextractor
#import python flask to create a rest API
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   pageResult=spacyextractor.extractEntities("Mass action: Kioni faction allows Jubilee Party employees to take Monday off")
   return pageResult

if __name__ == '__main__':
   app.run()