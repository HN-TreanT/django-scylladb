import netifaces as ni
ip = ni.ifaddresses('wlp164s0')[ni.AF_INET][0]['addr']
print(ip) 