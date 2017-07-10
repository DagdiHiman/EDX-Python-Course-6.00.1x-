d = {1:10, 2:20, 3:30, 4:30}
def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    
    inv_map = {}
    for k, v in d.items():
        inv_map[v] = inv_map.get(v, [])
        inv_map[v].append(k)
        inv_map[v] = sorted(inv_map[v])
    return inv_map
x = dict_invert(d)
print(x)