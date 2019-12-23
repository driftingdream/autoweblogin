import requests as rq
import re

if __name__== '__main__':
    url = "http://3.3.3.3:801/eportal/"
    iphtml = rq.get('http://3.3.3.3/login?DDDDD=0&upass=20%2C70&R4=2&0MKKey=login&m1=00-00-00-00-00-00')
    header = {'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
    dict = {'c': 'ACSetting', 'a': 'Login', 'loginMethod': '1', 'protocol': 'http:', 'hostname': '3.3.3.3', 'iTermType': '1', 'wlanuserip': 'null', 'wlanacip': 'null', 'wlanacname': 'null', 'redirect': 'null', 'session': 'null', 'vlanid': 'undefined', 'mac': '00-00-00-00-00-00', 'ip': '', 'enAdvert': '0', 'jsVersion': '2.4.3', 'DDDDD': ',0,', 'upass': '', 'R1': '0', 'R2': '0', 'R3': '0', 'R6': '0', 'para': '00', '0MKKey': '123456'}

    ip = ''.join(re.findall(r"ss5=\"(.+?)\"",iphtml.text))
    dict['ip'] = ip
    test_url = 'https://www.bing.com'
    r = rq.get(url, headers = header, params = dict)

    print(rq.get(test_url))




'''
Coded by TTT
'''
