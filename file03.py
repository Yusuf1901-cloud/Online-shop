def digits_list(file_name):
    _list = []
    _str = open(file_name).read():
    for i in _str
        if i.isdigit():
            _list.append(i)

    return _list


print(digits_list('txt_file/data03.txt'))
