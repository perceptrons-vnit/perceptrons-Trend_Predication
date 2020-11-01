from flask import Flask,render_template,url_for,Response,request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
import sqlite3
import os

app=Flask(__name__)
APP_ROUTE = os.path.dirname(__file__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///testdb.db'
# db=SQLAlchemy(app)
# Base = automap_base()
# Base.prepare(db.engine, reflect=True)
# Product = Base.classes.trytbl_info

@app.route("/") 
def s():
    return render_template('s.html')

@app.route("/trends", methods = ['GET', 'POST'])
def trends():
    images = ['2020031900h41m08s.jpg.png', '2020031918h58m24s.jpg.png', '2020032001h02m42s.jpg.png', '2020093016h48m18s.jpg.png', '2020093017h16m02s.jpg.png', '2020093018h00m13s.jpg.png', '2020093021h39m49s.jpg.png', '2020100107h22m02s.jpg.png', '2020100113h53m29s.jpg.png', '2020100114h43m03s.jpg.png', '2020100115h49m17s.jpg.png', '2020100116h33m09s.jpg.png']
    if request.method == 'POST':
        conn = sqlite3.connect('myntra.db')
        c = conn.cursor()
        images = []


        filter_att = request.form.getlist('typeof')
        for query in filter_att:
            for row in conn.execute(f"SELECT id FROM attributes WHERE {query} = 1"):
                images.append(row[0])

        conn.close()

        conn = sqlite3.connect('colors.db')
        c = conn.cursor()


        filter_color = request.form.getlist('colourval')
        print(filter_color)
        for query in filter_color:
            for row in conn.execute(f"SELECT id FROM colors WHERE {query} = 1"):
                images.append(row[0])

        conn.close()
    
    #Remove duplicates
    images = list(set(images))
    print(images)
    return render_template("trends.html", images = images)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/trial")
def trial():
    conn = sqlite3.connect('myntra.db')
    c = conn.cursor()

    image_list = [row[0] + ".jpg" for row in c.execute("SELECT id, midi FROM attributes WHERE mini_length = 1 AND id <= 4")][:12]
    print(image_list)
    return render_template("trial.html",image_list = image_list)

if __name__=='__main__':
    app.run()

#set FLASK_APP=app.py
#python -m flask run
#http://127.0.0.1:5000/ 
#http://127.0.0.1:5000/trends
#http://127.0.0.1:5000/foryou
#http://127.0.0.1:5000/about
#http://127.0.0.1:5000/trial