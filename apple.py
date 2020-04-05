# 算法：100个苹果放进10个篮子里面，不能有空篮子，有多少种放法呢？


def share(apple, basket):
    if apple <= 0 or basket <= 0:
        return "输入苹果和篮子数必须大于0"

    elif apple < basket:
        return "输入的苹果数必须大于篮子数"

    else:
        return share(apple, basket - 1) + share(apple - basket, basket)


if __name__ == '__main__':
    print(share(100, 10))



