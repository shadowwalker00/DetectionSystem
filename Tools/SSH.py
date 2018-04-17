import paramiko
class SSH:
    def __init__(self, add, user, passwd):
        self.address = add
        self.user = user
        self.port = '22'
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
        ssh.connect(hostname=self.address,port = self.port, username=self.user, password=self.password)
        return ssh
    def do_execution(self, ssh, command):
        """
        根据command内容在指定session中执行command命令
        :return: 执行的返回结果
        """
        #返回标准输入，输出以及报错情况
        stdin, stdout, stderr = ssh.exec_command(command)
        return stdout.read().decode()

    def put_file(self,local_path,remote_path):
        """
        向服务器端指定路径上传文件
        :return:
        """

        """
        实现sftp的方式可以总结为四步走
        1. 建立transport实例
        2. 登陆transport实例
        3. 将登陆后的transport对象传入sftpClient当中
        4. 通过sftp.put()上传文件/ sfpt.get()下载文件
        """
        transport = paramiko.Transport((self.address, int(self.port)))
        transport.connect(username=self.user, password=self.password)
        sfpt = paramiko.SFTPClient.from_transport(transport)
        sfpt.put(local_path,remote_path)
        transport.close()
        print('上传成功')

    def get_file(self,remote_path,local_path):
        """
        从服务器端下载文件到本地
        :return:
        """
        transport = paramiko.Transport((self.address, int(self.port)))
        transport.connect(username=self.user, password=self.password)
        sfpt = paramiko.SFTPClient.from_transport(transport)
        sfpt.get(remote_path, local_path)
        transport.close()
        print ('下载成功')