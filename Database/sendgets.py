# -*- coding: cp1256 -*-
# In the name of God
# Send and Gets data from Database SQL 
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import Database.wxsq2 as sq

class GetData:
    def __init__(self,send,gets):
        self.send = send
        self.gets = gets

    '''
    def getprice(self,devlbl):
        return 

    def getcustm(self,devlbl):
        return (data[0][0],data[0][1])

    def getcustname(self,custcode):
        return sq.wxsqsnd(,custcode)
    def getcustcode(self,name):
        return sq.wxsqsnd(,name)
    def Accname(self,accid):
        return sq.wxsqsnd(,accid)
    def Acccode( self , name):
        return sq.wxsqsnd(,name)
    def getcode(self,name):
        return sq.wxsqsnd(,name)
    def Acccust(self,custcode):
        return sq.wxsqsnd(,custcode)
    
    def Accspcy(self,custcode):
        return sq.wxsqsnd(,custcode)
    '''
    def gropshft(self,code=u''):
        return sq.wxsqltxt('employee.db',"""select empfile.employid , empfile.groupid , empfile.workid
                                           from empfile
                                           where empfile.employid = %s
                                           """ %code)

    def ateencod(self,code=u''):
        return sq.wxsqltxt('employee.db',"""select attend.employid ,attend.date, attend.enterit , attend.exitit
                                           from attend
                                           where attend.employid = %s
                                           and attend.exitit = ''
                                           order by  attend.enterit desc """%code )



    def shiftlist(self):
        return sq.wxsqsel('employee.db','Shifts','*')
    def groplist(self):
        return sq.wxsqsel('employee.db','Groups','*')
    
    def showrecord(self,code=u''):
        return sq.wxsqltxt('employee.db',"""select empfile.employid,employ.name,employ.family,Groups.groupname,Shifts.Shiftname,empfile.picpath
                                                     from empfile,employ,Groups,Shifts
                                                     where empfile.employid = %s
                                                     and empfile.employid = employ.employid
                                                     and empfile.groupid = Groups.Groupid
                                                     and empfile.workid = Shifts.Shiftid
                                                  """ %code)

    def gLBac(self):
        return sq.wxsqltxt('ABR.db',""" select distinct B.Rev,Backup.Bacfile,Backup.Bacdir,Backup.Bacdate,Backup.Bactime
                                        from B,Backup
                                        where B.Bac = Backup.Bac
                                    """)
    def gLRes(self):
        return sq.wxsqltxt('ABR.db',""" select distinct R.Rev,Restor.Resfile,Restor.Resdir,Restor.Resdate,Restor.Restime
                                        from R,Restor
                                        where R.Res = Restor.Res
                                    """)

    def gCmpny(self):
        return sq.wxsqsel('ABR.db','Company')
    def gReven(self):
        return sq.wxsqsel('ABR.db','Revenu')

    def lsrev(self,code=u''):
        return sq.wxsqltxt('ABR.db',"""select distinct Revenu.Reven,Company.Dir
                                        from Company,Revenu
                                        where Revenu.Rev = Company.Rev
                                        and Company.id = '%s' """%code)
    

    '''
    def chstyp( self , select = u'' ):
        return sq.wxsqltxt( %select)
    def showrecord2dev(self,code=u''):
        #print code
        return sq.wxsqltxt( %code)
    def showrecordAcc(self,code):
        #print code
        return sq.wxsqltxt( %code)
   
    def fillgrid(self,data):
        return sq.wxsqltxt(%data)
    def showrecord5(self,myday):
        #print myday
        return sq.wxsqltxt( %myday )
    
    def listrecord(self,code):
        return sq.wxsqltxt(%code)

    

    def Specyname(self,spcyid):
        return sq.wxsqseld(%spcyid)
    def Specyfamil(self,spcyid):
        return sq.wxsqseld(%spcyid)
    def Specymobil(self,spcyid):
        return sq.wxsqseld('','',''," Titlid = '1001A003' and Specid =  '%s'"%spcyid)
    '''


class SetData:
    def __init__(self,DB,data):
        self.DB = DB
        #self.send = send
        self.data = data

    def InBack(self,send,data):
        #sq.wxsqins('ABR.db','B',send,data)
        sq.wxsqins('ABR.db','Backup',send,data)
        return 1
    def InRest(self,send,data):
        #sq.wxsqins('ABR.db','R',send,data)
        sq.wxsqins('ABR.db','Restor',send,data)
        return 1
    def InABRc(self,send,data):
        sq.wxsqins('ABR.db','Company',send[0],data[0])
        sq.wxsqins('ABR.db','Revenu',send[1],data[1])    
    
