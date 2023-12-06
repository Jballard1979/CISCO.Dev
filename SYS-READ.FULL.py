#!/usr/bin/env python
#
# **********************************************************************:
# Author:	JBallard (JEB)												:
# Date:		2017.6.29													:
# Script:	SYSTEM-READ.FULL.py											:
# Purpose:	Extrapolate the configuration data from the Cisco Device	:
# Version:	1.0															:
# **********************************************************************:
#
# *** IMPORT THE NCCLIENT LIBRARY & XML LIBRARIES:
from ncclient import manager
import xml.dom.minidom
#
# DEVICE CONNECTION DETAILS:
HOST = '10.165.10.171'
PORT = 830
USER = 'administrator'
PASS = 'Sc@d@0216'
#
# ESTABLISH A CONNECTION TO THE HOST DEVICE:
netconf_connection = manager.connect(host=HOST, 
	port=PORT, 
	username=USER, 
	password=PASS, 
	hostkey_verify=FALSE)
#
# RETRIEVE FULL CONFIGURATION:
config = netconf_connection.get_config("running")
#
# PRINT DATA TO DISPLAY:
print(xml.dom.minidom.parseString(config.xml).toprettyxml())
#
# CLOSE THE CONNECTION:
netconf_connection.close_session()
#
# **********************************************************************:
# *** END OF PYTHON SCRIPT												:
# **********************************************************************: