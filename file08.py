def max_list(file_name):
    _str = open(file_name).read()
    _list = list()
    for i in _str:
        if i.isdigit():
            _list.append(int(i))
    _max = _list[0]
    for i in _list:
        if _max < i:
            _max = i

    return _max


print(max_list('txt_file/data08.txt'))
