from flask import render_template,request,send_file,redirect,make_response,url_for
from app import app
import os
import io
import csv
import pandas as pd
import numpy as np

#for saving the uploaded to uploads folder

app.config["DATA_UPLOADS"] = "app/static/data/uploads"


#main page

@app.route('/')
def index():
    return render_template("index.html")

#for receving the data from homepage

@app.route('/', methods=['GET','POST'])
def get_vtu_no():
    select = request.form.get('comp_select')
    option=str(select)
    date=request.form['examdate']
    vtuno=request.form['text']
    l=list(date.split('-'))
    date1=str(l[2])+"-"
    date1+=str(l[1])+"-"
    date1+=str(l[0])
    if(option=="CSE"):
        text = open('app/static/data/uploads/seatplanningCSE.csv','r')
        content=find(vtuno,text,date1)
    if(option=="CIVIL"):
        text = open('app/static/data/uploads/seatplanningCIVIL.csv','r')
        content=find(vtuno,text,date1)

    if(option=="ECE"):
        text = open('app/static/data/uploads/seatplanningECE.csv','r')
        content=find(vtuno,text,date1)
    if(option=="MECH"):
        text = open('app/static/data/uploads/seatplanningMECH.csv','r')
        content=find(vtuno,text,date1)
    if(option=="AERO"):
        text = open('app/static/data/uploads/seatplanningAERO.csv','r')
        content=find(vtuno,text,date1)
    if(option=="EEE"):
        text = open('app/static/data/uploads/seatplanningEEE.csv','r')
        content=find(vtuno,text,date1)
    if(option=="IT"):
        text = open('app/static/data/uploads/seatplanningIT.csv','r')
        content=find(vtuno,text,date1)

    inputquery=""
    inputquery+=str(date)
    inputquery+=" "
    inputquery+=str(vtuno)
    #content=find(vtuno,text,date1)
    newdate=""
    newdate+="Exam Date: "+date
    newOption="";newOption+="Department: "+option
    return render_template("index.html",exa=newdate,newOption=newOption,content=content)


#for seaching the data

def find(vtuno,text,date1):
    lines=text.readlines()
    room=name=vtu=date=cc=cn=seatno=""
    flag=0
    t=" "
    for i in lines:
        dd=list(i.split(','))
        if(dd[1]==vtuno and dd[0]==date1):
            date+=dd[0]+t
            room+=dd[5]+t
            name+=dd[2]+t
            vtu+=dd[1]+t
            cc+=dd[3]+t
            cn+=dd[4]+t
            seatno+=dd[6]+t
            flag=1
            break

    if(flag==0):
        return("Data Not Found!!!")
    else:
        return(" VTU No: %s \n Student Name: %s \n Course Code: %s \n Course Name: %s \n Room No: %s \n Seat No: %s "%(vtu,name,cc,cn,room,seatno))




#For login data page

@app.route('/login',methods=['GET','POST'])
def login():
    #userdata = pd.read_csv('app/static/data/uploads/userdata.csv')
    userdata=open('app/static/data/uploads/userdata.csv','r')
    lines=userdata.readlines()

    error=None
    f=0
    if(request.method=='POST'):
        #for d in lines:
        #    ll=list(d.split(','))
        if((request.form['username'] != 'admin') or (request.form['password'] != 'pass')):
                #f=1
            error='Invalid Credential. Please try again.'

        else:
            return redirect(url_for('upload'))

    return render_template('login.html',error=error)






#for uploading the data file

@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "POST":

        if request.files:

            image = request.files["image"]


            image.save(os.path.join(app.config["DATA_UPLOADS"], image.filename))
            return redirect(request.url)
    return render_template("upload.html")





@app.route('/about')
def about():
    return("""
    <h1 style='color: red;'>Manendra Nath Shukla</h1>
    <p>I Love Python!!!!</p>
    <code>I am a <em>freelancer</em></code>
    """)
