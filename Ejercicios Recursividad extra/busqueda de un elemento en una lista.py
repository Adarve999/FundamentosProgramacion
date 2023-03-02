
def _buscar_elem(v,ini,fin,acu):
    if ini>fin:
        res=-1
    else:
        if v[ini]==acu:
            res=v[ini]
        else:
            res=_buscar_elem(v,ini+1,fin,acu+v[ini])
    return res

def busqueda(v):
    return (_buscar_elem(v,0,len(v)-1,0))


v=[5,3,2,1,7,6,32,21,2]
print(busqueda(v))