from os import listdir
from PIL import Image as PImage
import re
from flask import Flask,jsonify, request
app=Flask(__name__)
import pytesseract

#Function to extract Receipt Date using regular expression

def found(text):

#List of all regular expressions required to extract date

    lists=["^[0-3][0-9]/[0-3][0-9]/(?:[0-9][0-9])?[0-9][0-9]$","([0-9]{1,2}\-[0-9]{1,2}\-[0-9]{2,4})","([0-9]{1,2}\/[0-9]{1,2}\/[0-9]{2,4})","^(1[0-2]|0?[1-9])/(3[01]|[12][0-9]|0?[1-9])/(?:[0-9]{2})?[0-9]{2}$","^(1[0-2]|0[1-9])/(3[01]|[12][0-9]|0[1-9])/[0-9]{4}$","^(3[01]|[12][0-9]|0?[1-9])/(1[0-2]|0?[1-9])/(?:[0-9]{2})?[0-9]{2}$","^(3[01]|[12][0-9]|0[1-9])/(1[0-2]|0[1-9])/[0-9]{4}$","^(?:(1[0-2]|0?[1-9])/(3[01]|[12][0-9]|0?[1-9])|(3[01]|[12][0-9]|0?[1-9])/(1[0-2]|0?[1-9]))/(?:[0-9]{2})?[0-9]{2}$","^(?:(1[0-2]|0[1-9])/(3[01]|[12][0-9]|0[1-9])|(3[01]|[12][0-9]|0[1-9])/(1[0-2]|0[1-9]))/[0-9]{4}$","([0-9]{1,2}\.[0-9]{1,2}\.[0-9]{2,4})","^[0-3]?[0-9].[0-3]?[0-9].(?:[0-9]{2})?[0-9]{2}$","^[0-3][0-9].[0-3][0-9].(?:[0-9][0-9])?[0-9][0-9]$","^(1[0-2]|0?[1-9]).(3[01]|[12][0-9]|0?[1-9]).(?:[0-9]{2})?[0-9]{2}$","^(1[0-2]|0[1-9]).(3[01]|[12][0-9]|0[1-9]).[0-9]{4}$","^(3[01]|[12][0-9]|0?[1-9]).(1[0-2]|0?[1-9]).(?:[0-9]{2})?[0-9]{2}$","^(3[01]|[12][0-9]|0[1-9]).(1[0-2]|0[1-9]).[0-9]{4}$","^(?:(1[0-2]|0?[1-9]).(3[01]|[12][0-9]|0?[1-9])|(3[01]|[12][0-9]|0?[1-9])/(1[0-2]|0?[1-9])).(?:[0-9]{2})?[0-9]{2}$","^(?:(1[0-2]|0[1-9]).(3[01]|[12][0-9]|0[1-9])|(3[01]|[12][0-9]|0[1-9]).(1[0-2]|0[1-9])).[0-9]{4}$","^(([0-9])|([0-2][0-9])|([3][0-1]))\/(Jan|jan|JAN|Feb|feb|FEB|Mar|MAR|mar|Apr|APR|apr|May|may|MAY|Jun|jun|JUN|Jul|jul|JUL|Aug|AUG|aug|Sep|sep|SEP|Oct|oct|OCT|Nov|NOV|nov|Dec|dec|DEC)\/\d{4}$","^(([0-9])|([0-2][0-9])|([3][0-1]))\s+(Jan|jan|JAN|Feb|feb|FEB|Mar|MAR|mar|Apr|APR|apr|May|may|MAY|Jun|jun|JUN|Jul|jul|JUL|Aug|AUG|aug|Sep|sep|SEP|Oct|oct|OCT|Nov|NOV|nov|Dec|dec|DEC)\s+\d{4}$","^(([0-9])|([0-2][0-9])|([3][0-1]))\-(Jan|jan|JAN|Feb|feb|FEB|Mar|MAR|mar|Apr|APR|apr|May|may|MAY|Jun|jun|JUN|Jul|jul|JUL|Aug|AUG|aug|Sep|sep|SEP|Oct|oct|OCT|Nov|NOV|nov|Dec|dec|DEC)\-\d{4}$","\d{2}-[A-z]{3}-\d{2}","\d{2}-[A-z]{3}\s+-\d{4}","\d{2}/[A-z]{3}\/\d{2}","\d{2}/[A-z]{3}\/\d{4}","\d{2}-[A-z]{3}\-\d{4}","\d{1}/[A-z]{3}\/\d{4}","\d{1}-[A-z]{3}\-\d{4}","[A-z]{3,9}\s+\d{1,2}\,\d{4}","\d{1,2}\s+[A-z]{3,9}\,\d{4}"]
    for i in lists:
        match=re.search(r'\b' + i  + r'\b', text)
        if(match):
            return(match.group())
    return("null") 




@app.route('/extract_date',methods=['POST'])

def dateExtract_post():
    if (request.method=='POST'):
        path = "Receipts/"
        image=request.json['base_64_image_content']
        img = PImage.open(path + image)
        text=pytesseract.image_to_string(img,lang="eng")
        ret=found(text)
        return jsonify({"date":ret})
        
        

@app.route('/extract_date/<image>',methods=['GET'])

def dateExtract_get(image):
    path = "Receipts/"
    img = PImage.open(path + image)
    # you can show every image
    text=pytesseract.image_to_string(img,lang="eng")
    ret=found(text)
    return jsonify({"date":ret})


if __name__=='__main__':
    app.run(debug=True) 
