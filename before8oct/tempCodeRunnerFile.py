def Lsearh(listdata, arg):
    i = 0
    while i < len(listdata) and listdata[i] == arg:
        i += 1
    if i < len(listdata):
        return i
    else:
        return False


size = int(input("enter the size of list"))
arr = [0] * size

i = 0
while i < len(arr):
    arr[i] = int(input(f"enter {i}th element"))
    i += 1
flag = True
while flag:
    search = int(input("enter element to searh"))
    index = Lsearh(arr, search)
    if index:
        print(f"the (index,position) is ({index,index+1})")
        flag = int(input("enter 0 to stop"))
    else:
        print("no such element exist")
        # print(index)
