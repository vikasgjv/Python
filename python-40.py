st = input("enter a message :  ")
word = st.split(" ")

def code(st):
    nwords = []
    if (len(st)>=3):
        r1 = 'fid'
        r2 = 'nso'
        str = r1 + st[1:]+st[0]+r2
        nwords.append(str)
    else:
        return nwords.append(word[::-1])
    print(" ".join(nwords))

def decode():
    if (st<3):
        return st.reverse()
    else:
        dc1 = st[3:] 
        dc2 = dc1[:-3]

print(code(st))

        


