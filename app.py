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

@app.route('/tambah_kayu/save', methods = ['POST'])
def tambah():
    if request.method == 'POST': 
        f_jenis = request.form.get("jenis")
        f_berat = request.form.get("berat")
        f_harga = request.form.get("harga")

    p=Kayu(jenis=f_jenis,berat=f_berat,harga=f_harga)
    db.session.add(p)
    db.session.commit()
    return redirect ('/k')
    
@app.route("/k/<id>/edit")
def edit_pendaftar(id):
    kayu = Kayu.query.filter_by(id=id).first()
    return render_template('edit_kayu.html',kayu = kayu)


@app.route('/k/<id>/update', methods=['post'])
def update_kayu(id):
    kayu = Kayu.query.filter_by(id=id).first()
    kayu.jenis= request.form.get("jenis")
    kayu.berat= request.form.get("berat")
    kayu.harga= request.form.get("harga")
    db.session.add(kayu)
    db.session.commit()
    return redirect("/k")


if "__main__"==__name__:
    app.run(debug=True, port = 2000)