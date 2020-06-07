import os
import io
import sys
import pickle
import getpass
import getopt

class Maintenance:
    def __init__(self):
        self.__user_dat = "user.dat"
        self.__hosts = []

    def sshpass(self,argv):
        os.execlp("sshpass","sshpass","-p",argv[1],"ssh",argv[0])

    def save_userinfo(self):
        with open(self.__user_dat,"wb") as f:
            pickle.dump(self.__hosts,f)
            f.close()

    def load_userinfo(self):
        try:
            with open(self.__user_dat,"rb") as f:
                self.__hosts = pickle.load(f);
                f.close()
        except EOFError as e:
            print("EOFError: \n" +
                  '\t' + str(e.args))

    def list_userinfo(self):
        s = io.BytesIO()
        num = 1
        base = 4
        for item in self.__hosts:
            s.write((str(num) + ') ' + item[0] + ' \t').encode())
            num += 1
            if(num%base == 0):
                s.write('\n'.encode())

        s.write((str(num) + ') ' + "new ssh server" + '\t').encode())
        print(s.getvalue().decode())
        
    def login(self):
        num = int(input("select ssh server number:"))
        threshold = len(self.__hosts) + 1
        if num > 0:
            if num < threshold:
                self.sshpass(self.__hosts[num - 1])
            elif num == threshold:
                userinfo = input("please input ssh server infomation: ")
                pwd = getpass.getpass("password: ")
                self.__hosts.append([userinfo,pwd])
                self.save_userinfo()
                print("num (%d)" %(num))
                print(self.__hosts)
                self.sshpass(self.__hosts[num - 1])
            else:
                print("invalid number.")
        elif num < 0:
            abs_value = abs(num)
            if abs_value < threshold:
                print("delete ssh server infomation: \n\t"
                      + str(abs_value) +") " + str(self.__hosts[abs_value-1][0]))
                del self.__hosts[abs_value - 1]
                self.save_userinfo()
            else:
                print("invalid number.")
        else:
            print("invalid number.");

    def update_userinfo(self):
        num = int(input("update ssh server infomation: "))
        if num < len(self.__hosts):
            userinfo = input("please input ssh server information: ")
            pwd = getpass.getpass("password: ")
            print("update ssh server[ %d) %s ] infomation." %(num,userinfo))
            self.__hosts[num] =  [userinfo,pwd]
        else:
            print("invalid number.")

    def usage(self):
        print('''maintenance is a python script,use sshpass to login ssh server ,and save pwd.

maintenance [-luh]
\t-l,--login\tlogin ssh server
\t-u,--update\tupdate ssh server information
\t-h,--help\tusage
''')

    def getopt(self):
        try:
            opts,args = getopt.getopt(sys.argv[1:],"luh",["login","update","help"])
            for opt , arg in opts:
                if opt in ('-h','--help'):
                    self.usage();
                elif opt in ('-u','--update'):
                    self.list_userinfo()
                    self.update_userinfo()
                elif opt in ('-l','--login'):
                    self.list_userinfo()
                    self.login()
        except getopt.GetoptError as e:
            print("GetoptError \n\t" +
                  e.args)

    def run(self):
        self.load_userinfo()
        self.getopt()
        
    
if __name__ == "__main__":
    maintenance = Maintenance()
    maintenance.run()








































































































































































































