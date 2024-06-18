def d(n, s):
    from itertools import product
    c = product(range(1, 7), repeat=n)
    ans = [comb for comb in c if sum(comb) == s]
    return ans


n = int(input("enter no of dice to roll:"))
s= int(input("enter sum :"))
result= d(n, s)
for i in result:
    print(i)
