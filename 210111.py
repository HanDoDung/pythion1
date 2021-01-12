#리스트 =[]
# 튜플 = ()
# 딕셔너리 = {} -- 해시맵
n =3
m = 3

#x= [ [0,1] , [3,2] , [1,0] ]
x= [ 0 ,2 , 1 ] 
x = [one*2 for one in x]
print(x)
print(x)

print(''.join(str(x)))




list_t = []
for i in range(n) :
  list_z = []
  for j in range(m) :
    list_z.append(j)
  list_t.append(list_z)
  
list_t[1][2] =5

#print(list_t)




list_x = [[3, 5, 7] , [1 ,2 ,3] , [7,9,8]]
#for i in range(n) :
#  list_y = list(map(int , input().split()))
#  list_x.append(list_y)
#print(list_x)  

#print(list_x[1][1])