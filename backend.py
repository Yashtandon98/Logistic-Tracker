import sqlite3

def connect():
    conn=sqlite3.connect("tracking.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS ITEMLIST (date text,mrr integer,vno text,oname text, delno integer, lp text, ulp text"
                ",rst integer, ld text, lw real, uw real, mrd text, ad integer, dltr real, drs real, uc integer, oa integer"
                ",remark text,rate integer, fr integer, comm integer, bal integer)")
    conn.commit()
    conn.close()

def insert(date, mrr, vno, oname, delno, lp, ulp, rst, ld, lw, uw, mrd, ad, dltr, drs, uc, oa, remark, rate, fr, comm, bal):
    conn=sqlite3.connect("tracking.db")
    cur=conn.cursor()
    cur.execute("INSERT OR IGNORE INTO ITEMLIST VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(date, mrr, vno, oname, delno, lp, ulp, rst, ld, lw, uw, mrd, ad, dltr, drs, uc, oa, remark, rate, fr, comm, bal))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("tracking.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM ITEMLIST")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(date = "", mrr = "", vno = "", oname = "", delno = "", lp = "", ulp = "", rst = "", ld = "", lw = "", uw = "", mrd = "", ad = "", dltr = "", drs = "", uc = "", oa = "", remark = "", rate = "", fr = "", comm = "", bal = ""):
    conn=sqlite3.connect("tracking.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM ITEMLIST WHERE date = ? OR mrr = ? OR vno = ? OR oname = ? OR delno = ? OR lp = ? OR ulp = ? OR rst = ? OR ld = ? OR lw = ? OR uw = ? OR mrd = ? OR ad = ? OR dltr = ? OR drs = ? OR uc = ? OR oa = ? OR remark = ? OR rate = ? OR fr = ? OR comm = ? OR bal = ?",(id,name,price,quantity))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(date):
    conn=sqlite3.connect("tracking.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM ITEMLIST WHERE date=?",(date,))
    conn.commit()
    conn.close()

def update(id,name,price,quantity):
    conn=sqlite3.connect("tracking.db")
    cur=conn.cursor()
    cur.execute("UPDATE ITEMLIST SET name=?,price=?,quantity=? WHERE id=?",(name,price,quantity,id))
    conn.commit()
    conn.close()

connect()
#update(21,"stellseries",25000,65)
#insert(2,"genegr",21,992)
print(view())
#print(search(quantity=1))
#delete(2121)
