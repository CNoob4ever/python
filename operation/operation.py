import os
import sys
import pickle

def sshpass(argv):
    os.execlp("sshpass","sshpass","-p",argv[1],"ssh",argv[2])

print(sys.argv[1] + " " + sys.argv[2])
print(str(sys.argv))
print(len(sys.argv))

hosts = []
hosts.append(["redfinger@192.168.168.109","rf@123456"])
for i in hosts:
    print(i[0])
    print(i[1])

user_dat = "user.dat"

with open(user_dat,"wb") as f:
    pickle.dump(hosts,f)

with open(user_dat,"rb") as f:
    r = pickle.load(f);
    print(r)

