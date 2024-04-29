# 2~ 부터 특정수 일일히 나누기

# 나누었을때 나머지가 1 , 0일때 합성수



# a = int(input("Enter the value :"))

# def prime (number) :
#     for i in range(2, number) :
#         if (number % i  == 0) :
#             return False
#         else :
#             return True

# print(prime(a))

# class Service :
#     def __init__(self, name) :
#         self.name = name
#         print ("Init")
#     def setname(self, name) :
#         self.name = name

# pey = Service("홍길동")
# print(pey.name)

# pey.setname("홍길동2")
# print(pey.name)

L1=[1,2,3]
print(L1)
print(id(L1))

L1[0:3]=[4,5,6]
print(L1)
print(id(L1))

L1=["가영","나영","다영"]
print(L1)
print(id(L1))

print(" ".join(L1))