#N

# from math import gcd

# n = int(input("Enter your number: "))
# count = 0

# for a in range(1, int(n**0.5) + 1):
#     if n % a == 0:
#         b = n // a
#         if a < b and gcd(a, b) == 1 and a * b <= n:
#             count += 1
#             if a != b: 
#                 count += 1

# print(count)

#O

# k = int(input('>>>'))
# a = []

# for h in range(2, k+1):
#     p = sum(i for i in range(1, h) if h % i == 0)
#     if p <= k and p > h:
#         l = sum(i for i in range(1, p) if p % i == 0)
#         if l == h:
#             a.append((h, p))

# for m in a:
#     print(m[0], m[1])
