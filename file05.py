_str = open('txt_file/data05.txt').read()
_list_dig = list()
_list_str = list()
for i in _str:
    if i.isdigit():
        _list_dig.append(i)
    else:
        _list_str.append(i)
print(len(_list_str), len(_list_dig))
