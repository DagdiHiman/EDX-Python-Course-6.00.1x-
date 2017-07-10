mydict = {1:10, 2:20, 3:30, 4:30}
'''
inverted_dict = dict([[v,k] for k,v in mydict.items()])

print(inverted_dict["red"])'''


def dict_invert(d):
    from collections import defaultdict
    inv_map = defaultdict(list)
    for k, v in d.items():
        inv_map[v].append(k)
    dict2= []
    dict2 = inv_map
    x=type(dict2)
    print(x)
    dict1={}
    #dict1 += dict2.pop(1)
    return dict2
print(dict_invert(mydict))