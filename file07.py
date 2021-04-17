def sum_digits(file_name):
    sum = 0
    _str = open(file_name).read()
    _list = list()
    for i in _str:
        if i.isdigit():
            _list.append(int(i))
    for i in _list:
        sum += i
    return sum

print(sum_digits('txt_file/data07.txt'))
