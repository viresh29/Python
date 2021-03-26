import socket as s

my_hostname = s.gethostname()
print('Your Hostname is: ' + my_hostname)

my_ip = s.gethostbyname(my_hostname)
print('Your IP Address is: ' + my_ip)

host = 'google.com'

ip = s.gethostbyname(host)
print('The IP Address of ' + host + ' is: ' + ip)
