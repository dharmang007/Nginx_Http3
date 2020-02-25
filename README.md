# Nginx_Http3
Automated Build Script for Nginx with HTTP/3
The script is only for ubuntu

## Dependencies which must be installed
- Python3
- gitpython
- zlib-1.2.11
- golang
- rust

## Steps
- Extract the files into /home/<user> directory
- Install zlib-1.2.11 in /home/<user> directory
- Run setup.py
- Run sudo make install
- Replace the given nginx.conf in nginx.1.16.1/configure folder
