#!/usr/bin/env python
#
# **********************************************************************:
# Author:	JBallard (JEB)												:
# Date:		2017.6.29													:
# Script:	SYSTEM-CISCO.YANK.py										:
# Purpose:	Reading Operational Data using YANG Models					:
# Version:	1.0															:
# **********************************************************************:
#
# READ DATA W/NCClient & CONVERT TO PYTHON DICTIONARY:
resp = xmltodict.parse(str(nc_get(GET_BGP_NEIGHBORS)))
#
# EXTRACT BGP NEIGHBORS FROM THE RETURNED RPC MESSAGE:
neighbors = resp['rpc-reply']['data']['bgp-state']['neighbors']['neighbor']
#
# LOOP THROUGH LIST & PRINT NEIGHBOR ID(s):
for neighbor in neighbors:
print neighbor['neighbor-id']
#
# **********************************************************************:
# *** END OF PYTHON SCRIPT												:
# **********************************************************************: