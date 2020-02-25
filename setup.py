


#################################################################
#  @author Dharmang Solanki
# Setup Script
# 
#################################################################


#################################################################
# IMPORTS 
#import pycurl
import requests as req
from os import path
import tarfile
import git
from git import Repo
import subprocess
#################################################################

nginx_url = "https://nginx.org/download/nginx-1.16.1.tar.gz"
quic_url = "https://github.com/cloudflare/quiche"
patch_repo = "../quiche/extras/nginx/nginx-1.16.patch"

##################################################################
# Download Nginx 
##################################################################
if path.exists("nginx-1.16.1.tar.gz") == False:
    res = req.get(nginx_url,stream = True)
    if res.status_code == 200:
        with open('./nginx-1.16.1.tar.gz','wb') as f:
            f.write(res.raw.read())
    else:
        print("!!!Error with Nginx website")

##################################################################
# Extract the files
##################################################################
untar_data = tarfile.open("nginx-1.16.1.tar.gz")

untar_data.extractall()
untar_data.close()
##################################################################
# Download QUIC protocol files
##################################################################
if path.exists("quiche") == False:
    git.Git(".").clone(quic_url)
    
# Delete the nginx-1.16.1 folder if error occurs
subprocess.call("bash quic_configuration.sh",shell=True)
