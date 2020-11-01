from flask import Flask,render_template,url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///testdb.db'
db=SQLAlchemy(app)

#apparel = db.Table('trytbl_info', db.metadata, autoload=True, autoload_with=db.engine)

Base = automap_base()
Base.prepare(db.engine, reflect=True)
Product = Base.classes.trytbl_info


@app.route("/") 
def s():
    r = db.session.query(Product).order_by(Product.id.desc()).all()

    for i in r:
        print(i.id)

    print("sanu!! :- ", )
    return render_template("s.html")


@app.route("/trends")
def trends():
    return render_template("trends.html")


@app.route("/foryou")
def foryou():
    # r = db.engine.execute('select name from trytbl_info').query.all()
    # for i in r:
    #     print(i)
    return render_template("foryou.html")


@app.route("/about")
def about():
    return render_template("about.html")


if __name__=='__main__':
    app.run()

#set FLASK_APP=app.py
#python -m flask run
#http://127.0.0.1:5000/ 
#http://127.0.0.1:5000/trends
#http://127.0.0.1:5000/foryou
#http://127.0.0.1:5000/about
#http://127.0.0.1:5000/trial