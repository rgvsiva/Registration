#-------------------SignIn/SignUp Procedure--------------------------
#signin for existing user.....
def signin(UD):
    users=[UD[i][0] for i in range(len(UD))]
    print(users)
    i=1
    while i <= 3:
        userid = input("Enter userid: ")  # asking userid
        ind = 0
        if userid in users:
            ind = users.index(userid)
            pswd = input("Enter Password: ")
            if pswd == UD[ind][1]:
                print('Access Granted...Yurekhaa...')
                cre=input('Do you wanna remove the credentials--Press ("Y")\n-->Press Enter to Exit: ')
                if cre.lower()=="y":
                    deleting(data,UD[ind])
                    print("Your credentials successfully removed")
                break
            else:
                print('Enter Valid Username/Password---\n---', 3 - i,' attempts remaining...')
                i+=1
        else:
            print("Enter Valid Userid---\n---", 3 - i, ' attempts remaining...')
            i+=1
    if i==4:
        print("---User not found---")
        val = input("-->Do you wanna register as new user--Press('Y'):\n-->Press Enter to exit--::")
        if val.lower() == 'y':
            signup(UD)
#-------------------------------------------------------------
#signup for new user......
def signup(UD):
    users=[UD[i][0] for i in range(len(UD))]
    new=[]
    j=1
    while j<=3:
        print('---use combo of alphabets and numbers only---')
        userid=input("Set your Userid: ")
        if userid and userid not in users:
            pswd = input("Set Your Password: ")
            if userid.isalnum() and pswd.isalnum() :
                new+=[userid,pswd]
                break
            else:
                j=j+1
        else:
            print('---Userid alredy Existed/invalid input---')
            j=j+1
    if len(new) == 2:
        fa = open('data', 'a')
        fa.write(new[0] + '-' + new[1]+'::')
        fa.close()
        UD.append(new)
        val = input("-->Do You Want To Signin--press('Y')\n-->Do you want to Signup--press('N')\n-->Press Enter to exit:: ")
        if val.lower() == 'y':
            signin(UD)
        elif val.lower() == 'n':
            signup(UD)
    else:
        print('-------------Try Again------------')
#-------------------------------------------------------------------------------------------------------
#deleting user credentials from database
def deleting(data,credentials):
    data.remove(credentials)
    fo=open('data','w')
    for i in data:
        fo.write('-'.join(i)+'::')
    fo.close()
#--------------------------------------------------------------------------------------------------
f = open('data')
fr = f.read()
data=[((i.strip()).split('-')) for i in fr.split('::')]
data.pop()
print(data)
ask=input("----User Signin/Signup procedure----\n-->For SignIn--Press ('Y')\n-->For SignUp--Press ('N')\n-->Press Enter to 'Exit'::")
if ask.lower() == 'y':
    print('-----SignIn-----')
    signin(data)
elif ask.lower() == 'n':
    print('-----SignUp-----')
    signup(data)
#------------------------------------------------------------------