# 求电阻的电导和
def g(*x):
    sum = 0
    for t in x:
        sum = sum + 1/t
    return sum

n = int(input('输入电阻(电容)个数'))
L = []
while n > 0:
    t = float(input('输入电阻(电容)'))
    L.append(t)
    n = n - 1
    pass
# print('求和的电阻',L)
G=g(*L)
R = g(G)
print('求得并联电阻(电容)%.2f' % R)
