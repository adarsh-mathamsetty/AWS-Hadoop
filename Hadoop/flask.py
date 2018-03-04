
from flask import Flask, make_response, request, render_template
import csv

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def form():
    return render_template("index.html")


@app.route('/runhadoop', methods=['POST', 'GET'])
def form1():
    data=[]

    with open('/home/ubuntu/states.csv') as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            data.append(row)
            print(row)

    return render_template("index.html",data=data)


@app.route('/timetaken', methods=['POST', 'GET'])
def timetaken():

    tme=[]
    with open('/home/ubuntu/timetaken.csv') as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            tme.append(row)


    tdiff="".join(str(v) for v in tme)
    str_tme=tdiff.replace('[','')
    tme2=str_tme.replace(']','')
    tme3=tme2.replace("'","")
    timediff=tme3.replace(',','')

    return render_template("index.html",timediff=timediff)

@app.route('/dynamic', methods=['POST', 'GET'])
def dynamic():
    mappers=int(request.form['mappers'])
    reducers=int(request.form['red'])
    writeintocsv = open("/home/ubuntu/flaskapp/states.csv", 'wb')
    writeobj = csv.writer(writeintocsv, quoting=csv.QUOTE_ALL)
    ma=(mappers," ")
    writeobj.writerow(ma)
    re=(reducers," ")
    writeobj.writerow(re)

    data1 = []

    with open('/home/ubuntu/states.csv') as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            data1.append(row)
            print(row)

    return render_template("index.html",data1=data1)

@app.route('/range', methods=['POST', 'GET'])

def range():
    mappers = int(request.form['maprange'])
    reducers = int(request.form['redrange'])
    writeintocsv = open("/home/ubuntu/flaskapp/states.csv", 'wb')
    writeobj = csv.writer(writeintocsv, quoting=csv.QUOTE_ALL)
    ma = (mappers, " ")
    writeobj.writerow(ma)
    re = (reducers, " ")
    writeobj.writerow(re)



    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
