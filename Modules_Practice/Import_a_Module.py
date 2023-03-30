import Arithmetic_Module

print('Enter 2 No.s:',end=' ')
x,y=map(int,input().split())

print('Addition:',Arithmetic_Module.add(x, y))
print('Subtraction:',Arithmetic_Module.sub(x, y))
print('Division:',Arithmetic_Module.div(x, y))
print('Multiplication:',Arithmetic_Module.mul(x, y))
