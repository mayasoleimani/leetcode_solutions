def isomorphic():

    s_alp={}
    t_alp={}
    x=0

    while x < len(s):

        s_alp[s[x]]=t[x]
        t_alp[t[x]]=s[x]

        x+=1

    if list(s_alp.keys()) != list(t_alp.values()):
        return False
    else:
        return True
