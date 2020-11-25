#!/usr/local/bin/python3
#Added by Pandama 

import pysftp
from zipfile import ZipFile 

with pysftp.Connection('10.88.15.177', username='ETL_MOH_Srv1', private_key='/home/infaadm/.ssh/id_rsa') as sftp:

  # get paramiko SFTPClient object
  psftp = sftp.sftp_client

  # change remote directory
  sftp.chdir('/BCS')

  for attr in sftp.listdir():
    if (attr[-4:] == '.zip'):
      # download a remote file
      sftp.get(attr)
      # move it to processed folder
      psftp.rename('/BCS/' + attr, '/BCS/processed/' + attr)
      # unzip the file
      with ZipFile(attr) as myzip:
        for n in myzip.namelist():
          print (n)
        myzip.extractall()
        
