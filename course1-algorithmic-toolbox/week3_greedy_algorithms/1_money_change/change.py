def change(money):
    num_coins = 0
    while money > 0:
        if money // 10 > 0:
            max_coin = 10
        elif money // 5 > 0:
            max_coin = 5
        else:
            max_coin = 1
        money = money - max_coin
        num_coins = num_coins + 1

    return num_coins


if __name__ == '__main__':
    m = int(input())
    num_coins = change(m)
    print(num_coins)
