#appending userids and passwords
def add_userid(userid):
    fa=open('a','a')
    fa.write(';'+userid)
    fa.close()
def add_pswd(pswd):
    fb=open('b','a')
    fb.write(';'+pswd)
    fb.close()
def data():
    a = open('a')
    c = a.read()
    users = c.split(';')
    return users