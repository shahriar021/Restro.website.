from flask import Flask, render_template, request
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = client["mydatabase"]
student = mydb["Student"]
student2 = mydb["Student2"]

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
@app.route('/home.html', methods=['GET', 'POST'])
def home():

    return render_template("home.html", **locals())

@app.route('/alldata.html', methods=['GET', 'POST'])
@app.route('/input', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        id = request.form['id']
        name = request.form['name']
        age = request.form['age']
        phone = request.form['phone']


        data = {"id": id, "name": name, "age": age, "phone": phone}
        student.insert_one(data)

    return render_template("alldata.html", **locals())

@app.route('/stdinfo.html', methods=['GET', 'POST'])
@app.route('/show', methods=['GET', 'POST'])
def input_show():
    list = []
    for st in student.find():
        list.append(st)
    return render_template("stdinfo.html", **locals())


@app.route('/another.html', methods=['GET', 'POST'])
def order():

    return render_template("another.html", **locals())


@app.route('/signup.html', methods=['GET', 'POST'])
def signup():

    return render_template("signup.html", **locals())

@app.route('/login.html', methods=['GET', 'POST'])
def login():

    return render_template("login.html", **locals())

@app.route('/timer.html', methods=['GET', 'POST'])
def timer():

    return render_template("timer.html", **locals())

@app.route('/booking.html', methods=['GET', 'POST'])
@app.route('/book', methods=['GET', 'POST'])
def booking():
    if request.method == 'POST':
        bkname = request.form['bkname']
        bknmbr = request.form['bknmbr']
        bkevent = request.form['bkevent']
        bkphone = request.form['bkphone']
        gender = request.form['gender']
        bkname2 = request.form['bkname2']
        bknmbr2 = request.form['bknmbr2']
        bkamount = request.form['bkamount']



        lata = {"bkname": bkname, "bknmbr": bknmbr, "bkevent": bkevent, "bkphone": bkphone,"gender": gender, "bkname2": bkname2, "bknmbr2": bknmbr2, "bkamount": bkamount, }
        student2.insert_one(lata)
    return render_template("booking.html", **locals())


if __name__ == '__main__':
    app.run(debug=True)
