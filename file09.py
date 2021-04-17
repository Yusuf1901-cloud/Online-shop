def min_dig_file(file_name):
    _list = open(file_name).read().split(",")
    _min = int(_list[0])
    for i in _list:
        if _min > int(i):
            _min = int(i)
    return _min


print(min_dig_file('txt_file/data09.txt'))
