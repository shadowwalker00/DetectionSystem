import paramiko
class SSH:
    def __init__(self, add, user, passwd):
        self.address = add
        self.user = user
        self.password = passwd
    def createSession(self):
        """
        根据实例address，password创建ssh对象
        :return: ssh对象
        """
        # 创建ssh对象
        ssh = paramiko.SSHClient()
        # 把要连接的机器添加到known_hosts文件中
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        #连接服务器
        ssh.connect(hostname=self.address,port = 22, username=self.user, password=self.password)
        return ssh
    def do_execution(self, ssh, command):
        """
        根据command内容在指定session中执行command命令
        :return: 执行的返回结果
        """
        #返回标准输入，输出以及报错情况
        stdin, stdout, stderr = ssh.exec_command(command)
        print(stdin)
        print(stdout)
        print(stderr)


