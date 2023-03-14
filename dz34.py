def dict_sum(ndict):
    s = 0
    for _, element in enumerate(ndict.values()):
        if isinstance(element, dict):
            s += dict_sum(element)
        else:
            s += element
    return s
    
print(dict_sum({'a':10, 'b':{'c':2, 'd':{'e':13, 'g':12}}, 'f':4}))