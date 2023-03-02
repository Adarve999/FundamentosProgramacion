
def es_volcal(c):
    c.lower
    return c=="a" or c=="e" or c=="i" or c=="o" or c=="u"


def _codificar(s,i):
    if i < len(s):
        if es_volcal(s[i]) and i>0:
            s=s[:i-1]+s[i]+s[i-1]+s[i+1:]
        s=_codificar(s,i+1)
    return s

def codificar(s):
    return _codificar(s,0)

print(codificar("esta en leon"))