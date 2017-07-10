d = {1:10, 2:20, 3:30, 4:30}
#{v: k for k, v in d.items()}
new_dict = { d[k]: k for k in d}
print(new_dict)