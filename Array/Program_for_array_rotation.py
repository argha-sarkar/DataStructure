def rotate(l, d):
    k = l.index(d)
    temp = l[k + 1:] + l[0:k + 1]
    return temp


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7]
    d = 2

    arr = rotate(arr, d)
    for i in arr:
        print(i, end="  ")
