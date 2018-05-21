#coding:utf-8
#!/usr/bin/env python

db = {}
def newuser():
    prompt = 'login desired:'
    while True:
        name = raw_input(prompt)
        if db.has_key(name):
            prompt = 'name taken, try another:'
            continue    #回头验证一下，continue怎么运行的
        else:
            break
    pwd = raw_input('passwd:')
    db [name] = pwd

def olduser():
    name = raw_input('login:')
    pwd = raw_input('passwd:')
    passwd = db.get(name)
    if passwd == pwd:
        print 'Welcome back', name
    else:
        print 'login incorrect'

def showmenu():
    prompt = """
    (N)ew User Login
    (E)xiting User Login
    (Q)uit
    
    Enter choice:"""

    done = False
    while not done:

        chosen = False
        while not chosen:
            try:
                choice = raw_input(prompt).strip()[0].lower()
            except (EOFError, KeyboardInterrupt):
                choice = 'q'
            print '\nYou picked:[%s]' % choice
            if choice not in 'neq':
                print 'invalid option, try again'
            else:
                chosen = True

        if choice == 'q':done = True
        if choice == 'n':newuser()
        if choice == 'e':olduser()

if __name__ == '__main__':
    showmenu()