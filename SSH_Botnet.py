import pexpect

botNet=[]

class Client:
    def __init__(self,username,ip,password):
        self.username=username
        self.ip=ip
        self.password=password
        self.session=self.connect()
    
    def connect(self):
        conStr='ssh'+self.username+'@'+self.ip
        child=pexpect.spawn(conStr)
        child.sendline('yes')
        child.sendline(self.password)
        return child 
    
    def send_command(self,cmd):
        self.session.prompt()
        self.session.sendline(cmd)
        return self.session.before


def botnet_command(command):
    for client in botNet:
        output=self.send_command(command)
        print('[*]Output for:'+self.username+':'+output)
    



def add_to_botnet(username,ip,password):
    client=Client(username,ip,password)
    botNet.append(client)


add_to_botnet('root','x.x.x.x','zzzz')
add_to_botnet('toor','x.x.x.x','zzzz')
add_to_botnet('user1','x.x.x.x','zzzz')

botnet_command('xxx')