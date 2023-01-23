from flask import Flask,render_template,request
import sqlite3 as sql

app=Flask("__name__")

@app.route("/")
def show():
    conn=sql.connect("db.db")
    conn.row_factory=sql.Row
    cur=conn.cursor()
    cur.execute("select * from t")
    data=cur.fetchall()
    return render_template("show.html",data=data)

@app.route("/insert",methods=["post","get"])
def Insert():
    if request.form.get("id")!=None:
        id=request.form.get("id")
        name=request.form.get("name")

        conn=sql.connect("db.db")
        conn.row_factory=sql.Row
        cur=conn.cursor()
        cur.execute("insert into t (id,name) values (?,?)",(id,name))
        conn.commit()

        return render_template("insert.html")
    return render_template("insert.html")

@app.route("/update/<id>",methods=["post","get"])
def Update(id):
    if request.form.get("id")!=None:
        id=request.form.get("id")
        name=request.form.get("name")

        conn=sql.connect("db.db")
        conn.row_factory=sql.Row
        cur=conn.cursor()
        cur.execute("update t set name=? where id=?",(name,id))
        conn.commit()

        cur.execute("select * from t")
        data=cur.fetchall()
        return render_template("show.html",data=data)
    id=int(id)
    conn=sql.connect("db.db")
    conn.row_factory=sql.Row
    cur=conn.cursor()
    cur.execute("select * from t where id=?",(id,))
    data=cur.fetchone()

    return render_template("update.html",data=data)

@app.route("/delete/<id>")
def Delete(id):
    conn=sql.connect("db.db")
    conn.row_factory=sql.Row
    cur=conn.cursor()
    cur.execute("delete from t where id=?",(id,))
    conn.commit()

    cur.execute("select * from t")
    data=cur.fetchall()

    return render_template("show.html",data=data)


if __name__=="__main__":
    app.run(debug=True)