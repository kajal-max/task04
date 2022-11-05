# Question - 1
# s = "1234abcd"
# print(s[::-1])


# Question - 2
# str1 = "abcSdefPghijQkl"
# l = 0
# u = 0
# for i in str1:
#   if i .islower():
#        l = l + 1
#   elif i.isupper():
#        u = u + 1
# print('The number of upper case letter :', (u))
# print('The number of lower case letter :', (l))


# Question - 3
# list = [1, 4, 5, 3, 2, 3, 4, 5, 4]
# unique_list = []
# for a in list:
#    if a not in unique_list:
#        unique_list.append(a)
# print(unique_list) 


# Question - 4
# print("enter a hyphen seperated sequence of words: ")
# lst = [n for n  in input ().split('-')]
# lst.sort()
# print("sorted string is: ")
# print('-'.join(lst))


# Question - 5
# st = "Hello world Practice makes man perfect"
# print(st.upper())


# Question - 6    
# def calculatesum (a,b):
#     s = int(a) + int(b)
#     return s
# num1 = "10"
# num2 = "20"
# sum = calculatesum (num1,num2)
# print("sum = ", sum)


# Question - 7                       
# def max_len_str(s1,s2):
#   len1 = len(s1)
#   len2 = len (s2)
#   if len1 > len2:
#     print(s1)
#   elif len1 < len2:
#     print(s2)
#   elif len1 == len2:
#     print("both strings have same length")
    
# s1 = input("enter the name :")
# s2 = input("enter the name :")
# max_len_str(s1,s2)


# def max_len_str(s1,s2):

#   len1 = len(s1)
#   len2 = len(s2)
#   result = " "
#   if len1 > len2:
#         result = s1
#   elif len1 < len2:
#         result = s2
#   elif len1 == len2:
#         result = "both strings have same length"
#   return result
# s1 = input("enter the name : ")
# s2 = input("enter the name : ")
# print(max_len_str(s1,s2))


# Question - 8
# my_list = [1, 2, 3, 4, 5]
# print ("The list is ")
# print(my_list)
# print("The resultant tuple is : ")
# my_result = [(val, pow(val,2))for val in my_list]
# print(my_result)


# Question - 9         
# def shownumber(limit):
#     # limit=3
#     for i in range(0,limit+1):
#         if i == 0:
#             print(i, end="")
#             print("even")
#         elif i%2 == 0:
#             print(i,end = "") 
#             print("even") 
#         else:
#             print(i,end="") 
#             print("odd") 
# shownumber(3)

                                 
# Question - 10
# def even(x):
#   return x % 2 == 0
# a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] 
# result = filter(even, a) 
# print('original list:',a)
# print('filtered list:', list(result))

# lis1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# def is_even(x): return x % 2 == 0
# lis2 = list(filter(is_even, lis1))
# print(lis2)


# Question - 11                                                    
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# eve_num = map(lambda x: x**2,
#     filter(lambda x: x%2==0, my_list))
# print(list(eve_num))
                                        

# Question - 12
# 12
# def division1():
#   try:
#       result = 5/0
#   except ZeroDivisionError:
#       print("number 5 is not divisible by 0")
#   finally:
#       print("anyways this is executed")
# division1()


# Question - 13
# from functools import reduce
# l=reduce(lambda a,d: 10*a+d, [1,2,3,4,5,6,7,8], 0)
# print(l)


# Question - 14                                             
# n1 = []
# for x in range(1,50):
#   if (x/3!=0) and (x%7==0):
#     n1.append(str(x))
#   print(','.join(n1))  


# Question - 15
# def multiply(n):
#     return n*n
# numbers = (1,2,3,4) 
# result = map (multiply,numbers)
# print(list(result))   


# Question - 16
# def foo():
#   try:
#     return 1
#   finally:
#     return 2
# k = foo()
# print(k)


# def f(a,b):
#     pass
# def a():
#   try:
#     # x = 10
#     f(x,4)
#   finally:
#     print('after f')
#     print('after f?')
# a()
# NameError: name 'f' is not defined
             