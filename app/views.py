from flask import render_template,request,send_file,redirect,make_response
from app import app
import os
import io
import csv
import pandas as pd

app.config["DATA_UPLOADS"] = "app/static/data/uploads"




@app.route('/')
def index():
    return render_template("index.html")




@app.route('/', methods=['POST'])
def get_vtu_no():
    vtuno=request.form['text']
    text = open('app/static/data/uploads/seatplanning.csv','r+')
    #content = text.read()
    #text.close()
    #procesed=("Dear Student %s,You don't have any exam today,go attend ur classes.\n Thank You!!!"%vtuno)
    content=find(vtuno,text)
    return render_template("index.html",content=content)




def find(vtuno,text):
    lines=text.readlines()
    result=""
    flag=0
    for i in lines:
        dd=list(i.split(','))
        if(dd[0]==vtuno):
            result+=dd[1]
            flag=1
    if(flag==0):
        return("Dear Student %s,You don't have any exam today,go attend ur classes.\n Thank You!!!"%(vtuno))
    else:
        return("You Have Exam in Room No:%s"%(result))







@app.route("/upload-data", methods=["GET", "POST"])
def upload_data():
    if request.method == "POST":

        if request.files:

            image = request.files["image"]


            image.save(os.path.join(app.config["DATA_UPLOADS"], image.filename))
            return redirect(request.url)
    return render_template("upload_data.html")
#def importdata(file):




@app.route('/form')
def form():
    return """
        <html>
            <body>
                <h1>Transform a file demo</h1>

                <form action="/transform" method="post" enctype="multipart/form-data">
                    <input type="file" name="data_file" />
                    <input type="submit" />
                </form>
            </body>
        </html>
    """





@app.route('/transform', methods=["POST"])
def transform_view():
    file = request.files['data_file']
    if not file:
        return "No file"

    #stream = io.StringIO(f.stream.read().decode("UTF8"), newline=None)
    #csv_input = csv.reader(stream)
    #print("file contents: ", file_contents)
    #print(type(file_contents))
    #print(csv_input)
    #dict={}
    #for row in csv_input:
    #    dict[row[0]]=row[1]
    #THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    path="app/static/data/uploads"
    filename_path = os.path.join(path, file.filename)

    # Put input file in dataframe
    sheet = pd.read_csv(filename_path, encoding='cp1252')
    #stream.seek(0)
    #result = transform(stream.read())
    #sheet=pd.read_csv(f,encoding='cp1252')
    #response = make_response(result)
    #response.headers["Content-Disposition"] = "attachment; filename=result.csv"'''
    #return (dict)
    return(sheet)
    #return None


@app.route('/about')
def about():
    return("""
    <h1 style='color: red;'>Manendra Nath Shukla</h1>
    <p>I Love Python!!!!</p>
    <code>I am a <em>freelancer</em></code>
    """)

