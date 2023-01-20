from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///kayu.db'

db = SQLAlchemy(app)
migrate = Migrate(app,db)

#model
class Kayu(db.Model):
    id=db.Column(db.Integer,primary_key = True)
    jenis=db.Column(db.String(50))
    berat=db.Column(db.Integer())
    harga=db.Column(db.Integer())

    def __repr__(self) -> str:
        return self.nama

@app.route('/k')
def list_kayu():
    listkayu=Kayu.query.all()
    return render_template('list_kayu.html',  lk = listkayu)

@app.route('/tambah_kayu')
def tambah_kayu():
    return render_template('tambah_kayu.html')



if "__main__"==__name__:
    app.run(debug=True, port = 2000)