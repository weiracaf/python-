for i in range(2):
    print("1")
    print("2")  # 你要么保持和上一条语句保持一样的缩进，表示这个2也进循环
    print("5");print("6")  # 一行多个语句要加分号
    # print("3")   但是你不能既不和for的缩进相同，又不和for下面的语句缩进相同
print("4")  # 这行与for的缩进相同，不属于for循环了已经
