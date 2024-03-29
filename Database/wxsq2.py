# In the name of God
#! use/bin/env python

import sqlite3
import os
from Config.Init import *
from wx import MessageBox,OK,ICON_WARNING

class WXDB(object):
    def __init__(self,database=":memory:",pathdb=os.getcwd()):
        self.database=pathdb+database
        #print pathdb
        self.connect()

    def connect(self):
        #print self.database
        try :
           self.connection=sqlite3.connect(self.database)
           self.cursor=self.connection.cursor()
        except:
           MessageBox(u'No Database find',u'Error',OK | ICON_WARNING)
        self.connected=True
        self.statement=''
        return self.connection

    def close(self):
        self.commit()
        self.connection.close()
        self.connected=False

    def commit(self):
        return self.connection.commit()

    def execute(self,statments):
        #with self.connect():
        self.cursor.execute(statments)
        return self.fetchall()
        #result = self.cursor.fetchall()
        #return result
    
    def execute1(self,statments,*data):
        if len(data) > 0:
            self.cursor.execute(statments,data[0])
        self.commit()
        return self.fetchall()
        

    def execone(self,statments,*data):
        #with self.connect():
        #print statments
        #print data,data[0],data[0][0]
        if data == None:
            self.cursor.execute(statments)
        else:
            self.cursor.execute(statments,data[0])
        #result = self.cursor.fetchall()
        #print result
        #return result
        return self.fetchone()    

    def executemany(self,statments,*data):
        if data == None:
            return self.cursor.executemany(statments)
        else:
            return self.cursor.executemany(statments,data[0])
        
    def executscript(self,statments):
        return self.cursor.executscript(statments)
    def total_changes(self):
        pass
    def rollback(self):
        return self.cursor.rollback()
    def fetchone(self):
        return self.cursor.fetchone()
    def fetchall(self):
        return self.cursor.fetchall()
    def fetchmany(self,size):
        return self.cursor.fetchmany()
    
class SQLite(object):
    def __init__(self,tables,fields,values):
        self.tables=tables
        self.fields=fields
        self.values=values
        
    def create(self,**karg):
        sql = 'create table {t} ({f} {p})'.format(t=str(self.tables),f=str(self.fields),p=str(values))
        return sql


    def insert(self,**karg):
        sql = 'insert into '+str(self.tables)
        sql = sql+ '('+str(self.fields)+')'
        
        
        sql = sql +' values '+'('+'?,'*(len(self.fields.split(','))-1)+'?)'
        
        #print sql
        return sql

    def select(self,*arg,**karg):
        
        #sql =  ' select '+self.fields+' from '+self.tables
        sql = "select {f} from {t} ".format(f=self.fields,t=self.tables)
        return sql

    def selectd(self,*arg,**karg):
        
        sql =  ' select distinct'+self.fields+' from '+self.tables+' where '+self.values
        #sql = "select distinct {f} from {t} where {v} ".format(f=self.fields,t=self.tables,v=self.values)
        #print sql
        return sql

    def update(self,**karg):

        sql = ' update '+self.tables+' set '+self.fields
        #sql = " update {t} set {f} ".format(t=self.tables,f=self.fields)
        #print sql
        return sql
    
    def update2(self,**karg):

        sql = ' update '+self.tables+' set '+self.fields+' where '+self.values
        #sql = " update {t} set {f}  where {v}".format(t=self.tables,f=self.fields , v=self.values)
        #print sql
        return sql

    def delete(self,**karg):
        sql = ' delete from '+self.tables+' where '+self.values
        #sql = " delete from {t} where {v} ".format(t=self.tables,v=self.values)
        return sql
    
    def delall(self,**karg):
        #sql = ' delete from '+self.tables+' where '+self.values
        sql = " delete from {t} ".format(t=self.tables)
        return sql
    
def MyDB_Path(database):
    return WXDB(database,DATABASE_PATH)

def wxsqsel(database,tabels,fields='*',condition=''):
            
    Mydb = MyDB_Path(database)
    Mydb.connect()
    sql = SQLite(tabels,fields,condition)
    sql1 = sql.select(fields,tabels)
       
    mylist = Mydb.execute(sql1)
    return mylist


def wxsqseld(database,tabels,fields='*',condition=''):
         
    Mydb = MyDB_Path(database)
    Mydb.connect()
    sql = SQLite(tabels,fields,values=condition)
    sql1 = sql.selectd(fields,tabels,values=condition)
    #print sql1   
    mylist = Mydb.execute(sql1)
    return mylist


def wxsqltxt(database,text):
    
    Mydb = MyDB_Path(database)
    mylist = Mydb.execute(text)
    return mylist

    
def wxsqins(database,tabels,fields,data):
    
    Mydb = MyDB_Path(database)
    sql = SQLite(tabels,fields,values=data)
    sql1 = sql.insert()
    #print sql
    mylist = Mydb.execone(sql1,data)
    #Mydb.commit()
    Mydb.close()
    #print mylist
    return mylist

def wxsqins2(database,tabels,fields,data):
    
    Mydb = MyDB_Path(database)
    sql = SQLite(tabels,fields,values=data)
    sql1 = sql.insert()
    #print sql
    mylist = Mydb.executemany(sql1,data)
    #Mydb.commit()
    Mydb.close()
    #print mylist
    return mylist
    
def wxsqlup(database,tabels,fields,data):
    
    Mydb = MyDB_Path(database)
    sql = SQLite(tabels,fields,values=data)
    sql1 = sql.update()
    
    mylist = Mydb.execone(sql1,data)
    #Mydb.commit()
    Mydb.close()
    #print mylist
    return mylist

def wxsqlup2(database,tabels,fields,data):
    
    Mydb = MyDB_Path(database)
    sql = SQLite(tabels,fields,values=data)
    sql1 = sql.update2()
    
    mylist = Mydb.executemany(sql1,data)
    #Mydb.commit()
    Mydb.close()
    #print mylist
    return mylist 

def wxsqdel(database,tabels,data):
    
    Mydb = MyDB_Path(database)
    sql = SQLite(tabels,fields='',values=data)
    sql1 = sql.delete()
    
    mylist = Mydb.execute(sql1)
    #Mydb.commit()
    Mydb.close()
    #print mylist
    return mylist

def wxsqdall(database,tabels):
    
    Mydb = MyDB_Path(database)
    sql = SQLite(tabels,fields='',values='')
    sql1 = sql.delall()
    
    mylist = Mydb.execute(sql1)
    #Mydb.commit()
    Mydb.close()
    #print mylist
    return mylist



def wxsqsnd(database,tabel,field1,field2,data):
    
    Mydb = MyDB_Path(database)
    mylist = Mydb.execute('select '+tabel+'.'+field1+' from '+tabel+' where '+tabel+'.'+field2+" = '%s' "%data)
    #print mylist
    return mylist



