#!/usr/bin/env python3
# -*- coding: Latin-1 -*-
#--
#-- **************************************************************************************************************:
#-- ************************************************* CISCO CONFIG ***********************************************:
#-- **************************************************************************************************************:
#-- Author:  JBALLARD (JEB)                                                                                       :
#-- Date:    2019.6.18                                                                                            :
#-- Script:  CISCO-NET.CONFIG.py                                                                                  :
#-- Purpose: A python script that connects to & updates multiple Cisco UCS devices.                               :
#-- Version: 1.0                                                                                                  :
#-- **************************************************************************************************************:
#-- **************************************************************************************************************:
#--
#-- **************************************************:
#-- DEFINE PARAMETERS & CONFIGURATION PATHS           :
#-- **************************************************:
#--
import paramiko
import time
#--
IPAddress = "10.165.10.101"
USRName = "JBallardAdmin"
PASSWord = "Sc@d@0216"
#--
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=IPAddress,USRName=USRName,PASSWord=PASSWord)
#--
print (" *** CONNECTION SUCCESSFUL ***: ", IPAddress)
#--
remote_connection = ssh_client.invoke_shell()
remote_connection.send("CONFIGURE TERMINAL:\n")
remote_connection.send("SMTP-SERVER\n")
remote_connection.send("SMTP-SERVER HOST 10.50.10.21:25\n")
remote_connection.send("line vty 0 4\n")
remote_connection.send("exec-timeout 60\n") 
remote_connection.send("end\n")
#--
time.sleep(1)
output = remote_connection.recv(65535)
print(output)
#--
fname = r"ipadd.txt"
file = open(fname,'r')
teststr = file.read()
print ("LIST OF ADDRESSES\n",teststr)
#--
ssh_client.close
#--
#-- **************************************************:
#-- END OF SCRIPT                                     :
#-- **************************************************:
