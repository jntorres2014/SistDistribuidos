# File: Ntpclient.py
>>> import ntplib
from socket import AF_INET, SOCK_DGRAM
import sys
import socket
import struct #, time
from time import ctime

# # Set the socket parameters 

 c = ntplib.NTPClient()
 response = c.request('europe.pool.ntp.org', version=3)
 response.offset
response.version
ctime(response.tx_time)
ntplib.leap_to_text(response.leap)
response.root_delay
ntplib.ref_id_to_text(response.ref_id)
