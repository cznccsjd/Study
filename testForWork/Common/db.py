#!/usr/bin/env python3
#coding:utf-8

import pymysql

class DB():
    def connect(self, table='talk'):
        conn = pymysql.connect(host="172.16.70.20", port=3306, user="rd_user", password="NTHXDF7czYwi", database=table)
        cur = conn.cursor()
        return cur

    def close(self):
        db = DB()
        cur = db.connect()
        cur.close()

    def selectSql(self, select='*', table='talk.user', where='1=1'):
        sql = "SELECT %s FROM %s WHERE %s" % (select, table, where)
        return sql

    def doSelect(self, select , table, where):
        db = DB()
        sql = db.selectSql(select, table, where)
        cur = db.connect()
        cur.execute(sql)
        result = cur.fetchall()
        cur.close()
        return result


if __name__ == '__main__':
    d = DB()
    d.select()