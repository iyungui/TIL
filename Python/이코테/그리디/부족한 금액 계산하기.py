def solution(price, money, count):
    for i in range(count):
        tmp = price
        tmp *= (i + 1)
        money -= tmp

    if (money < 0):
        return -money
    else:
        return 0
        
print(solution(3, 20, 4))
