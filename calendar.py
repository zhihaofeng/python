# 计算到某月一日星期几
def we(m, n=4):
    L = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    s, t = 0, 1
    while t < m:
        s = s + L[t-1]
        t = t + 1
    return (s+n+1) % 7


# 进行日期输出
def p(n, m):
    L = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for x in range(n):
        print('   ', end='')
    for x in range(1, L[m]+1):
        if (x+n) % 7 == 0:
            print('%3s' % x)
        else:
            print('%3s' % x, end='')

x = int(input('输入月:'))
n = we(x)
print(' 日 一 二 三 四 五 六')
p(n, x-1)
