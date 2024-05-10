import numpy as np

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

# L1=[1,2,3]
# print(L1)
# print(id(L1))

# L1[0:3]=[4,5,6]
# print(L1)
# print(id(L1))

# L1=["가영","나영","다영"]
# print(L1)
# print(id(L1))

# print(" ".join(L1))

# class Calculator :
#     def __init__(self) :
#         self.result = 0

#     def add (self , num) :
#         self.result += num
#         return self.result
    
# a = Calculator()

# print(a.add(4))
# print(a.add(4))
# print(a.add(4))

# class FourCal :
#     def __init__(self, num1, num2) :
#         self.num1 = num1
#         self.num2 = num2

#     def setdeta (self , num1 , num2) :
#         self.num1 = num1
#         self.num2 = num2

#     def add (self) :
#         result = self.num1 + self.num2 
#         return result
# a = FourCal(10, 222)

# # a.setdeta(2,5)
# print(a.add())


# class MoreFourCal(FourCal) :
#     def pow (self) :
#         result = self.num1 ** self.num2
#         return result

# b = MoreFourCal(2, 8)
# print(b.pow())

# a = np.array(range(1, 11)) + np.array(range(10, 101, 10))
# print(a.shape)
# print(a.size)

def choice_number__(number,key2):
    global dic_List
    if number!=1 and number!=2 :
        print("메뉴에서 고르세요.")
        choice_number2=int(input("1과 2 중에 선택하세요.:"))
        choice_number__(choice_number2,key2)
    elif number==1:
        for i in key2:
            for j in range(2,len(key)+1):
                if i%j==0:
                    del dic_List[i]
    elif number==2:
        for i in key2:
            for j in range(2,len(key)+1):
                if i%j!=0:
                    del dic_List[i]

choice_number__()