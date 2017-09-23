
import sqlite3
import datetime


class Sql:
    def __init__(self, data_name):
        self.data_name = data_name

    def add_table(self, cur, table):
        cur.executescript(table)


    def connect(self):
        return sqlite3.connect(self.data_name)

    def cursor(self, con):
        return  con.cursor()


    @staticmethod
    def add_line(cur, ins, seq):
        cur.execute(ins, seq)

    def close(self, con, curs):
        con.commit()
        curs.close()
        con.close()


if __name__ == '__main__':
    pass

