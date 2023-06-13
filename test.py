import profanitylib as pf
import pandas as pd
from flask import Flask,request, redirect, url_for
app = Flask(__name__)
@app.route("/",methods = ['POST'])
def profanity_filter():
    text=request.json["query"]
    status=pf.contains_profanity(text)
    mask=pf.censor(text)
    # print({"originalText":text,"profanityStatus":status,"maskText":mask})
    return {"originalText":text,"profanityStatus":status,"maskText":mask}

if __name__ == '__main__':
    app.run()




