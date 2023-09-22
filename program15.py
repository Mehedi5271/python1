print('lamda function')
sum = (lambda a,b: a+b )(2,3)

print(sum)

print('----------')
print('Map funciton')

def squre(a):
    return  a*a

number = [1,2,3,4]

result = list ( map(squre,number))

print(result)




