def ethiopian(x, y):
    _dict = {}
    while x != 1:
        x //= 2
        y *= 2
        if x % 2 != 0:
            _dict[x] = y
    value = list(_dict.values())
    return sum(value)

if __name__ == '__main__': # main 파일 내에서만 작동
    print(ethiopian(14, 7))
