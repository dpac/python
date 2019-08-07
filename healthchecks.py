#!/usr/local/bin/python3.6
import os
from f5.bigip import ManagementRoot
import getpass
import requests
requests.packages.urllib3.disable_warnings()
from netmiko import ConnectHandler


class F5:
    sslnnp220_interface="1"
    sslnnp220_srv="62"
    sslekp220_interface="1"
    sslekp220_srv="62"
    lbseks241_interface="3"
    lbseks241_srv="43"
    SSL222VP002400_interface="3"
    SSL222VP002400_srv="56"
    SSL224VP222001_interface="3"
    SSL224VP222001_srv="56"
    SSL224VP002400_interface="6"
    SSL224VP002400_srv="56"
    fwlnnp152_interface="12"
    fwlnnp152_srv="62"
    lbsekp242_interface="6"
    lbsekp242_srv="56"
    lbsnnp243_interface="5"
    lbsnnp243_srv="41"
    lbsekp243_interface="5"
    lbsekp243_srv="41"
    SSL222VP222001_interface="4"
    SSL222VP222001_srv="56"
    sslnnp240_interface="3"
    sslnnp240_srv="60"
    sslekp240_interface="3"
    sslekp240_srv="61"
    glbekp241_interface="3"
    glbekp241_srv="53"
    ssl220vp002400_interface="3"
    ssl220vp002400_srv="56"
    ssl220vp222001_interface="3"
    ssl220vp222001_srv="56"
    GLBEKP220_interface="5"
    GLBEKP220_srv="58"
    GLBNNP220_interface="6"
    GLBNNP220_srv="59"
    GLBNNP241_interface="3"
    GLBNNP241_srv="47"
    lbs2nnpp0501_interface="8"
    lbs2nnpp0501_srv="56"
    LBSEKP241_interface="6"
    LBSEKP241_srv="56"
    FWLNNP151_interface="12"
    FWLNNP151_srv="63"
    FWLEKP151_interface="8"
    FWLEKP151_srv="65"
    lbs2nnpp0500_interface="8"
    lbs2nnpp0500_srv="56"
    FWLEKP152_interface="8"
    FWLEKP152_srv="65"
    ssl224vp222001_interface="3"
    ssl224vp222001_srv="56"
    ssl224vp002400_interface="3"
    ssl224vp002400_srv="56"
    glbnnp241_iquery="24"
    glbekp241_iquery="24"
    glbnnp220_iquery="16"
    glbekp220_iquery="16"
    AWS001VP222001fw01_bgpcount="93"
    AWS001VP222001fw02_bgpcount="1"
    fwlnns201_intcount="43"
    fwlnns202_intcount="43"
    fwleks201_intcount="18"
    fwleks202_intcount="18"

hostnames=['SSL222VP002400','ssl224vp222001','ssl224vp002400','lbseks241','fwlnnp152','lbsekp242','lbsnnp243','lbsekp243','SSL222VP222001','sslnnp240','sslekp240','glbekp241','ssl220vp002400','ssl220vp222001','GLBEKP220','GLBNNP220','GLBNNP241','lbs2nnpp0501','LBSEKP241','FWLNNP151','FWLEKP151','lbs2nnpp0500','FWLEKP152']
for i in hostnames:
     mgmt = ManagementRoot(i, 'admin','w&EB48E+')
     command='tmsh show net interface all | grep -i up | wc -l'
     cmd = "-c \'" + command + "\'"
     x = mgmt.tm.util.bash.exec_cmd('run', utilCmdArgs=cmd)
    # print("Checking number of up intefaces on %s"% i)
     print(x.commandResult,file=open("/home/DC081072/scripts/F5/F5-DIR/"+str(i)+"_int.txt", "w"))

hostnames=['SSL222VP002400','ssl224vp222001','ssl224vp002400','lbseks241','fwlnnp152','lbsekp242','lbsnnp243','lbsekp243','SSL222VP222001','sslnnp240','sslekp240','glbekp241','ssl220vp002400','ssl220vp222001','GLBEKP220','GLBNNP220','GLBNNP241','lbs2nnpp0501','LBSEKP241','FWLNNP151','FWLEKP151','lbs2nnpp0500','FWLEKP152']
for i in hostnames:
     mgmt = ManagementRoot(i, 'admin','w&EB48E+')
     command='bigstart status | grep -i run | wc -l'
     cmd = "-c \'" + command + "\'"
     x = mgmt.tm.util.bash.exec_cmd('run', utilCmdArgs=cmd)
    # print("Checking number of running F5 services on %s" % i)
     print(x.commandResult,file=open("/home/DC081072/scripts/F5/F5-DIR/"+str(i)+"_srv.txt", "w"))

print("****************************************\n F5 INTERFACES CHECKS \n****************************************")

hostnames=['SSL222VP002400','ssl224vp222001','ssl224vp002400','lbseks241','fwlnnp152','lbsekp242','lbsnnp243','lbsekp243','SSL222VP222001','sslnnp240','sslekp240','glbekp241','ssl220vp002400','ssl220vp222001','GLBEKP220','GLBNNP220','GLBNNP241','lbs2nnpp0501','LBSEKP241','FWLNNP151','FWLEKP151','lbs2nnpp0500','FWLEKP152']
for i in hostnames:
 with open("/home/DC081072/scripts/F5/F5-DIR/"+str(i)+"_int.txt") as file: #Read the content of a file
     data =file.readline().strip()
     if data == getattr(F5,str(i)+'_interface'):
         print ("Interface checks for "+str(i)+" is Green\n")
     else:
         print ("Interface checks for "+str(i)+" is FAILED\n")

print("****************************************\n F5 SERVICE CHECKS \n****************************************")

hostnames=['SSL222VP002400','ssl224vp222001','ssl224vp002400','lbseks241','fwlnnp152','lbsekp242','lbsnnp243','lbsekp243','SSL222VP222001','sslnnp240','sslekp240','glbekp241','ssl220vp002400','ssl220vp222001','GLBEKP220','GLBNNP220','GLBNNP241','lbs2nnpp0501','LBSEKP241','FWLNNP151','FWLEKP151','lbs2nnpp0500','FWLEKP152']
for i in hostnames:
 with open("/home/DC081072/scripts/F5/F5-DIR/"+str(i)+"_srv.txt") as file: #Read the content of a file
     data =file.readline().strip()
     if data == getattr(F5,str(i)+'_srv'):
         print ("F5 service health checks for "+str(i)+" is Green\n")
     else:
         print ("F5 service health checks for "+str(i)+" is FAILED\n")

hostnames=['glbnnp241','glbekp241','glbnnp220','glbekp220']
for i in hostnames:
    mgmt = ManagementRoot(i, 'admin','w&EB48E+')
    command='tmsh show gtm iquery all | grep -Ei "connected" | grep -Eiv "not-connected" | wc -l'
    cmd = "-c \'" + command + "\'"
    x = mgmt.tm.util.bash.exec_cmd('run', utilCmdArgs=cmd)
    #print("Checking number of up intefaces on %s"% i)
    print(x.commandResult,file=open("/home/DC081072/scripts/F5/F5-DIR/"+str(i)+"_iq.txt", "w"))

print("****************************************\n F5 DNS IQUERY CHECKS \n****************************************")

hostnames=['glbnnp241','glbekp241','glbnnp220','glbekp220']
for i in hostnames:
 with open("/home/DC081072/scripts/F5/F5-DIR/"+str(i)+"_iq.txt") as file: #Read the content of a file
     data =file.readline().strip()
     if data >= getattr(F5,str(i)+'_iquery'):
         print ("F5 GTM iquery checks for "+str(i)+" is Green\n")
     else:
         print ("F5 GTM iquery checks for "+str(i)+" is FAILED\n")


extproxies = {
    'http': 'http://dc081072:July@2019@internet-proxy.dc.vodafone.com.au:8080',
    'https': 'http://dc081072:July@2019@internet-proxy.dc.vodafone.com.au:8080',
}
s = requests.Session()
s.proxies = extproxies
r = s.get('https://ipchicken.com')
rr=s.get('http://www.guns.com')
print("****************************************\n PROXY INTERNET CHECKS \n****************************************")
print(r.status_code)
if r.status_code is 200:
 print("Internet access through proxy is Green")
else:
 print("Internet access through proxy  is FAILED")
print("****************************************\n PROXY FILTERING SERVICE CHECKS \n****************************************")
print(rr.status_code)
if rr.status_code == 403:
 print("Proxy filtering service health check is Green")
else:
 print("Proxy filtering service health check is FAILED")

print("****************************************\n AWS BGP CHECKS \n****************************************")
hostnames=['AWS001VP222001fw01','AWS001VP222001fw02']
for i in hostnames:
 cisco_asa = {
        'device_type': 'cisco_asa',
        'host': str(i),
        'username': 'dc081072',
        'password': 'July@2019',
        'secret': 'July@2019',
    }
 net_connect = ConnectHandler(**cisco_asa)
 output = net_connect.send_command("show bgp neighbors | in Established")
 print(output,file=open("/home/DC081072/scripts/F5/F5-DIR/"+str(i)+"_Nbgp.txt", "w"))
 os.system('cat /home/DC081072/scripts/F5/F5-DIR/'+str(i)+'_Nbgp.txt | wc -l > /home/DC081072/scripts/F5/F5-DIR/'+str(i)+'_count.txt')

hostnames=['AWS001VP222001fw01','AWS001VP222001fw02']
for i in hostnames:
 with open("/home/DC081072/scripts/F5/F5-DIR/"+str(i)+"_count.txt") as file: #Read the content of a file
     data =file.readline().strip()
     if data == getattr(F5,str(i)+'_bgpcount'):
         print ("AWS BGP checks for "+str(i)+" is Green\n")
     else:
         print ("AWS BGP checks for "+str(i)+" is FAILED\n")

print("****************************************\n ASA INTERFACE CHECKS \n****************************************")
hostnames=['fwlnns201','fwlnns202','fwleks201','fwleks202']
for i in hostnames:
 cisco_asa = {
        'device_type': 'cisco_asa',
        'host': str(i),
        'username': 'dc081072',
        'password': 'July@2019',
        'secret': 'July@2019',
    }
 net_connect = ConnectHandler(**cisco_asa)
 output = net_connect.send_command("show interface ip brief | i up")
 print(output,file=open("/home/DC081072/scripts/F5/F5-DIR/"+str(i)+"_intt.txt", "w"))
 os.system("sed '${/^$/d}' /home/DC081072/scripts/F5/F5-DIR/"+str(i)+"_intt.txt > /home/DC081072/scripts/F5/F5-DIR/"+str(i)+"_int.txt")
 os.system('cat /home/DC081072/scripts/F5/F5-DIR/'+str(i)+'_int.txt | wc -l > /home/DC081072/scripts/F5/F5-DIR/'+str(i)+'_count.txt')

hostnames=['fwlnns201','fwlnns202','fwleks201','fwleks202']
for i in hostnames:
 with open("/home/DC081072/scripts/F5/F5-DIR/"+str(i)+"_count.txt") as file: #Read the content of a file
     data =file.readline().strip()
     if data == getattr(F5,str(i)+'_intcount'):
         print ("ASA interface checks for "+str(i)+" is Green\n")
     else:
         print ("ASA interface  checks for "+str(i)+" is FAILED\n")
