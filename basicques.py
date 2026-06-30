# TO find the grade of the student


# mark=int(input("Enter the mark:"))
# if mark>=90:
#     print("Grade :A")
# elif mark>=80:
#     print("Grade :B")
# elif mark>=70:
#     print("Grade :C")
# elif mark>=50:
#     print("Grade :D")
# else:
#     print("Fail")

# Leap year or not

# year=int(input("Enter the year:"))
# if (year%4==0 and year%100!=0) or (year%400==0):
#     print(year,"is a leap year")
# else:
#     print(year,"is not a leap year")
    
    
#Reversed string

# def reverse_str(str):
#     rev=""
#     for i in range (len(str)-1,-1,-1):
#         rev+=str[i]
#     return rev
# str=input("Enter the string:")
# print("Reversed string is:",reverse_str(str))         

#Reverse the string using Slicing operator

# str=input("Enter the string:")
# print("Reversed String is :",str[::-1]) 

#Count the vowels in the string

# def count_vowels(str):
#     count=0
#     vowels="aeiouAEIOU"
#     for i in str:
#         if i in vowels:
#             count+=1
#     return count
# str=input("Enter string:")
# print("Vowels are:",count_vowels(str))

#Find whether the  number is prime or not

# def prime(num):
#     if num<=1:
#         return False
#     for i in range(2,num):
#         if num%i==0:
#             return False
#     return True
# print(prime(6))

# Find the factorial of the number 

# def factorial(num):
#     fact=1
#     for i in range(1,num+1):
#         fact*=i
#     return fact
# num=int(input("Enter the number:"))
# print("Factorial of", num, "is:", factorial(num))

# check Anagram


# str1=input("Enter the first string:")
# str2=input("Enter the second string:")
# if sorted(str1)==sorted(str2):
#     print("Anagram")
# else:
#     print("Not Anagram")

# ///////////////////////////////////////////////

# from collections import Counter
# s1=input("Enter the first string:")
# s2=input("Enter the second string:")
# if Counter(s1)==Counter(s2):
#     print("Anagram")
# else:
#     print("Not Anagram")


# Reverse the string
 
# str=input("Enter the string:")
# rev=""
# for i in range(len(str)-1,-1,-1):
#     rev+=str[i]
# print("Reversed String is:",rev)

#///////////////////////////////////

# str=input("Enter the string:")
# print("Reversed string is:",str[::-1])
 
# Remove duplicates in the list

# list=[1,1,2,4,5,7,7,3,8,4]
# og_list=[]
# for i in list:
#     if i not in og_list:
#         og_list.append(i)
# print("List after removing duplicates:",og_list)

# Palindrome or not

# str=input("Enter the string:").lower()
# if str==str[::-1]:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# //////////////////////////////////////

# str=input("Enter the string:").lower()
# rev=""
# for i in range(len(str)-1,-1,-1):
#     rev+=str[i]
# if str==rev:
#     print("Palindrome")
# else:
#     print("Not palindrome")

# Find the Largest Element in the list

# list=[1,2,4,5,6,9,7]
# largest=0
# for i in list:
#     if i>largest:
#         largest=i
# print("Largest Element in the list is:",largest)

# List Comprehensions

# number=[]
# for i in range(1,11):
#     number.append(i)
# print(number)

# /////////////////////////

# print([i for i in range(1,11)])

# move duplicates from the list without using set
# list=[1,2,2,4,7,5,6,1]
# seen=[]
# result=[x for x in list if not(x in seen or seen.append(x))]
# print(result)

# Find the Second largest number

# nums=sorted(set(list),reverse=True)
# print(nums[1])
# x=33
# result="yes" if x > 0 else "No"
# print(result)

# Enumerate means loop with index

# a=["car","bike","van","auto"]
# for i,val in enumerate(a):
#     print(i,val)

# for i,val in enumerate(a,start=1):
#     print(i,val)

# b=[10,3,4,5,6,77,8,43]
# target=6
# for i,v in enumerate(b):
#     if v==target:
#         print(f"Found {target} at {i} th index")
#         break
d = {"apple": 50, "banana": 20, "mango": 80}
for key, val in d.items():
    print(key, val)