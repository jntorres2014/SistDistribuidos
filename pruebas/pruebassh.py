from pexpect import pxssh
s = pxssh.pxssh()
if not s.login ('localhost', 'myusername', 'mypassword'):
       print "SSH session failed on login."
       print str(s)
else:
       print "SSH session login successful"
       s.sendline ('ls -l')
       s.prompt()         # match the prompt
       print s.before     # print everything before the prompt.
       s.logout()
       secuencia=1337 1337 2600 2600
       iptables -A INPUT -s %IP% -p tcp --dport 22 -j ACCEPT   
       unsleep(20)
       tcpflags = syn
       if unsleep 60
			iptables -D INPUT -s %IP% -p tcp --dport 22 -j ACCEPT 
            