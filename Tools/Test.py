from Tools.SSH import SSH
import os
class Test:
    def __init__(self,sshObj):
        self.sshobj = sshObj

    def test(self, imagefile):
        """
        将待检测图片上传到服务器，然后执行服务器的demo程序，将测试结果下载
        :param imagefile: 文件在本地的路径
        :return:返回检测结果图片所在路径
        """
        filename = os.basename(imagefile)
        remote_dir = '/home/user2/chen_guang_hao/PeDetect/smallcorgi/Faster-RCNN_TF-master/client/picture'
        #图片上传到client/picture文件夹下
        self.sshobj.put_file(imagefile,os.path.join(remote_dir, filename))
        session = self.sshobj.createSession()
        #执行测试的程序
        command = 'cd chen_guang_hao/PeDetect/smallcorgi/Faster-RCNN_TF-master/;python test.py'
        result = self.sshobj.do_execution(session,command)
        print(result)
        #下载检测结果到本地
        self.sshobj.get_file(os.path.join(remote_dir,os.path.splitext(filename)[0]+'Detect.jpg'),'./picture/'+os.path.splitext(filename)[0]+'Detect.jpg')
        return './picture/'+os.path.splitext(filename)[0]+'Detect.jpg'



