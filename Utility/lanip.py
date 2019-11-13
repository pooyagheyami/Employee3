###########################################################################
## Class Testlan
###########################################################################

#In the name of God
#!/usr/bin/env python

from socket import *
import os
from subprocess import *
import re
#from netaddr import *
from Config.Init import *


class testlan(object):
    def __init__(self,addr1,addr2,port):
        self.addr1 = addr1
        self.addr2 = addr2
        self.prot = port
        self.network = addr1.split('.')[0]+'.'+addr1.split('.')[1]+'.'+addr1.split('.')[2]+'.'


    def pingit(self,addr):
        try:
            p = check_output("ping -n 1 -w 1 "+addr,shell=True)
            #print p.find('0% ')
            return True
        except:
            #print 'error',addr
            return False

    def openport(self,addr):
        for i in [23,25,80,135,445,902]:
            sok = socket(AF_INET, SOCK_STREAM)
            sok.settimeout(0.1)
            if sok.connect_ex((addr,i)) == 0 :
                #print addr,i
                sok.close()
                return i
            else:
                sok.close()
                continue
        return 0

    def is_up(self,addr):
        s = socket(AF_INET, SOCK_STREAM)
        s.settimeout(0.1)    ## set a timeout of 0.01 sec
        self.port=self.openport(addr)
        #print self.port,'  ',addr
        if  self.port == 0:
            #print addr,self.port
            if self.pingit(addr):
                s.close()
                return 1
            else:
                s.close()
                #print self.port
                return 0
        elif not s.connect_ex((addr,self.port)) :  # connect to the remote host on port 135
            #s.bind((addr,port))
            #s.send("GET /HTTP /1.0\n\n")
            #print s.listen()
            s.close()    ## (port 135 is always open on Windows machines, AFAIK)
            return 1
        else:
            s.close()
            return 0

    def getmac(self,addr):
        arp_out =check_output(['arp','-a',addr])
        if len(arp_out)>30:
            m=re.search("([0-9a-fA-F]{2}-){5}[0-9a-fA-F]{2}",arp_out)
            mac1= arp_out.splitlines()[3]
            mac = arp_out.splitlines()[3].split('    ')[2].lstrip(' ')
            #mac =  EUI(arp_out.splitlines()[3].split('     ')[1].lstrip(' '))
            #mac.dialect = mac_unix_expanded
            #print mac,mac1,m
            return mac
        else:
            arp_out =check_output(['getmac','-V'],shell=True)
            m=re.search("([0-9a-fA-F]{2}-){5}[0-9a-fA-F]{2}",arp_out)
            #print arp_out.splitlines()
            return m.group()


    def run2(self,addr):
        #print addr
        #print self.is_up(addr)
        data = []    
        if self.is_up(addr):
           data.append(unicode(getfqdn(addr)))
           data.append(unicode(addr))
           data.append(unicode(self.getmac(addr)))
           data.append(unicode('Active'))
           data.append(unicode('Now'))
        return data   
                
            
            


    def run(self,addr1,addr2):
        a=int(addr1.split('.')[3])
        b=int(addr2.split('.')[3])
        self.all =  int(addr2.split('.')[3])-int(addr1.split('.')[3])
        network = self.network
        i = 0
        data = []
        for ip in xrange(a,b):
            self.addr = network + str(ip)
            #print self.addr
            if self.is_up(self.addr):
                #print '%s \t- %s' %(self.addr, getfqdn(self.addr))
                #print self.getmac(self.addr)
                data.append((unicode(getfqdn(self.addr)),unicode(self.addr),unicode(self.getmac(self.addr))))
                #data.append(unicode(self.addr))
                #data.append(unicode(self.getmac(self.addr)))
                #data.append(unicode('Active'))
                #data.append(unicode('Now'))
        #print data
        return data       
