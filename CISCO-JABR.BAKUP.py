#!/usr/bin/env python3
# -*- coding: Latin-1 -*-
#--
#-- **************************************************************************************************************:
#-- ********************************************* CISCO JBR BACKUPS **********************************************:
#-- **************************************************************************************************************:
#-- Author:  JBALLARD (JEB)                                                                                       :
#-- Date:    2017.2.11                                                                                            :
#-- Script:  CISCO-JABR.BAKUP.py                                                                                  :
#-- Purpose: A python script that backsup all CISCO Jabber Conversations.                                         :
#-- Version: 1.0                                                                                                  :
#-- **************************************************************************************************************:
#-- **************************************************************************************************************:
#--
#-- **************************************************:
#-- DEFINE PARAMS & CONFIG PATHS                      :
#-- **************************************************:
import os
import shutil
#--
#-- BACKUP DIRECTORY:
BACKUP_DIR="D:\0_REPO\1_JABBER"
#--
#-- CREATE BACKUP DIR:
if not os.path.exists(BACKUP_DIR):
    os.makedirs(BACKUP_DIR)
#--
#-- RETRIEVE LIST OF JABBER CONVERSATIONS:
CONVERSATIONS = [f for f in os.listdir(os.path.expanduser("~/Library/Application Support/Cisco Jabber/")) if f.endswith(".chatlog")]
#--
#-- BACKUP ALL CONVERSATIONS:
for conversation in CONVERSATIONS:
    source_path = os.path.join(os.path.expanduser("~/Library/Application Support/Cisco Jabber/"), conversation)
    dest_path = os.path.join(BACKUP_DIR, conversation)
    shutil.copy2(source_path, dest_path)
#--
print("CISCO JABBER - COMPLETED ALL BACKUP EFFORTS")
#--
#-- **************************************************:
#-- END OF SCRIPT                                     :
#-- **************************************************: