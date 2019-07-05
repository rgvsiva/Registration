from adding_id_pwd import *

#signin for existing user
def signin(UD):
    users=data()
    i=1
    while i <= 3:
        userid = input("Enter userid: ")  # asking userid
        ind = 0
        if userid in users:
            # print('Userid:',userid)
            ind = users.index(userid)
            # print('index: ',ind)
            pswd = input("Enter Password: ")
            # print('pswd:',UD[ind][1])
            if pswd == UD[ind][1]:
                print('Access Granted...Yurekhaa...')
                break
            else:
                print('Enter Valid Password---\n---', 3 - i,' attempts remaining...')
                i=i+1
                continue
            break
        else:
            print("Enter Valid Userid---\n---", 3 - i, ' attempts remaining...')
            i = i + 1
    if i==4:
        print("---User doesn't Exists---")
        while True:
            value = input("Do you want to register as new user ?:(Enter 'Y'):\n--Enter any other key to exit--::")
            if value.lower() == 'y':
                signup(UD)
                break
            else:
                break

#-------------------------------------------------------------
#print(users)
def signup(UD):
    ud=UD
    users=data()
    new=[]
    j=1
    while j<=3:
        print('---use combo of alphabets and numbers only---')
        userid=input("Set your Userid: ")
        if userid not in users:
            if userid.isalnum():
                new.append(userid)
                #print('valid:', new)
                i=1
                while i<=3:
                    print('---use combo of alphabets and numbers only---')
                    pswd=input("Set Your Password: ")
                    if pswd.isalnum():
                        new.append(pswd)
                        #print('valid: ', new)
                        break
                    else:
                        i=i+1
                break
            else:
                j=j+1
        else:
            print('---Userid is alredy Existed---')
            j=j+1
    while j<=3:
        if len(new) == 2:
            add_userid(new[0])
            add_pswd(new[1])
            ud.append(new)
            break
        else:
            print('---Invalid Input---Try Again---')
            signup(UD)
   # print(ud)
    while j<=3:
        val=input("---Do You Want To Signin...---('Y' or'N'):\n--Enter any other key to exit--:: ")
        if val.lower()=='y':
            signin(ud)
            break
        elif val.lower()=='n':
            reg=input("Do you want to register as new user ?:(Enter 'Y'):\n--Enter any other key to exit--::")
            if reg.lower()=='y':
                signup(ud)
                break
            else:
                break
        else:
            break
#-------------------------------------------------------------------------------------------------------
