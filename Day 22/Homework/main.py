def manual_max(max):
    o=max[0]
    for i in max:
        if i >o:
            o=i
    return o

def manual_replace(a,b,c):
    for i in range(len(a)):
        if a[i] == b:
            a[i] = b
    return a


def manual_append(b,d):
    b+=[d]
    return b