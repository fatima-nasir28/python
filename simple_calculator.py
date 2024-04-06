f=int(input("enter first number: "))
n=int(input("enter second number: "))
oper=input("enter the operation you want to perform(+,-,*,/,,sqrt,exponent): ")
result=0

if oper=="+":
  result=f+n
elif oper=="-":
  result=f-n
elif oper=="/":
   result=f/n
elif oper=="sqrt":
   result=f or n **0.5
elif oper=="exponent":
  result=f ** n or n** f
else :
    print("invalid input")
print("your answer is: ",result)