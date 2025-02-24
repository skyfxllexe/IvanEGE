# def dividers(n): # dividers - от английского делители
#     dividers = []

#     for i in range(1,int(n**0.5)+1):
#         if n%i == 0:
#             dividers.append(i)
#             if n//i != i:
#                 dividers.append(n//i)

#     return dividers


# # for i in range(int(100_000_000**0.5), int(200_000_000**0.5)+1):
# #     if len(dividers(i)) == 2:
# #         print(i**2)



# # ровно пять делителей. (alpha1+1)...(alphaN+1) = 5
# # alpha_i + 1 = 1
# # alpha_j + 1 = 5 (j!=i) => alpha_j = 4
# # A = p^4
# # 

# for i in range(int(100_000_000**0.25), int(200_000_000**0.25)+1):
#     if len(dividers(i)) == 2:
#         print(i**4)



"""
Найдите все натуральные числа N, принадлежащие отрезку [200 000 000; 400 000 000],
 которые можно представить в виде N  =  2^m · 3^n, где m  — чётное число, n  — нечётное число. В ответе запишите все найденные числа в порядке возрастания.
"""

for m in range(0,100,2):
    for n in range(1,100,2):
        N = 2**m * 3**n
        if N >= 200_000_000 and N<=400_000_000:
            print(N)