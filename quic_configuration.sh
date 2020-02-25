#!/bin/bash
cd nginx-1.16.1
patch -p01  < ../quiche/extras/nginx/nginx-1.16.patch
./configure                          	\
    --prefix=$PWD                       	\
   	--with-http_ssl_module              	\
   	--with-http_v2_module               	\
  	--with-http_v3_module               	\
   	--with-openssl=../quiche/deps/boringssl \
   	--with-quiche=../quiche                 \
    --with-zlib=/home/dharmang/zlib-1.16.11
make