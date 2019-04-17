from f5.bigip import ManagementRoot
import re, requests, json
from pprint import pprint as pp
import os
import time
from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/success/<name><com>')
def success(name,com):
 file = open("tmsh_commandlist.txt","w")
 file.write("tmsh create sys crypto key "+name +" common-name " +com + " key-size 2048 gen-csr country AU state NSW organization XYZ ou XYZ city Sydney")
 file.close()

 time.sleep(2)
 os.system("/usr/local/bin/python3.6 /home/DC081072/scripts/F5/F5-tmsh.py ")

 time.sleep(2)
 cmd ="sshpass -p 'password' ssh admin@sslekp224 find /config/filestore/files_d/Common_d/certificate_signing_request_d -name *" + str(name) + "* -exec cat  {} +"

 ps=os.popen(cmd).read()

 return  ps

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      cu  = request.form['cm']
      return redirect(url_for('success',name = user , com = cu ))

   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))

if __name__ == '__main__':
   app.run('0.0.0.0',debug = True)
