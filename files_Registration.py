
#-------------------Registration process--------------------------
from files_signup_signin import *
#------------------------------------------------------------------
def files():
    a=open('a')
    b=open('b')
    c=a.read()
    d=b.read()
    e=c.split(';')
    f=d.split(';')
    userid_pswd_list=[]
    for i in range(len(e)):
        g=[e[i],f[i]]
        userid_pswd_list.append(g)
    return userid_pswd_list

u = files()
print(u)
#----------------------------------------------------------------------
ask=input("----User Signin/Signup program----\nFor SignUp--Press 'Y':\nFor SignIn--Press 'N': ")
i=1
while i<=3:
    if ask.lower()=='y':
        print('-----Signup-----')
        signup(u)
        break
    elif ask.lower()=='n':
        print('-----signin-----')
        signin(u)
        break
    else:
        ask=input("Plz...Enter 'Y' or 'N': ")
        i=i+1

