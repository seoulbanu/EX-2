                                                                       #EXCHANGE TWO VALUES
#1.USING NAIVE APPROACH:
x=10
y=50
temp=x
x=y
y=temp
print("value of x:",x)
print("value of y:",y)
#2.USING COMMA(,)OPERATOR
x=10
y=50
x,y=y,x
print("value of x:",x)
print("value of y:",y)
#3.USING ARITHMETIC OPERATOR
x=10
y=50
x=x+y
y=x-y
x=x-y
print("value of x:",x)
print("value of y:",y)
#4.USING XOR OPERATOR
x=10
y=50
x=x^y
y=x^y
x=x^y
print("value of x:",x)
print("value of y:",y)
                                                                      #CIRCULATING THE LIST OF VALUES
#1.USING IN-BUILT FUNCTIONS
n=3
a=[1,2,3,4,5,6]
a=(a[len(a)-n:len(a)]+a[0:len(a)-n])
print("a after circulating:",a)
#2.USING SLICING OPERATOR
n=3
b=[1,2,3,4,5,6]
if n>len(b):
    n=int(n%len(b))
b=(b[-n:]+b[:-n])
print("b after circulating:",b)
                                                                      #CALCULATING THE DISTANCE BETWEEN TWO POINTS
x1=int(input("enter x1:"))
x2=int(input("enter x2:"))
y1=int(input("enter y1:"))
y2=int(input("enter y2:"))
result=((((x2-x1)**2)+((y2-y1)**2))**0.5)
print("distance between",(x1,x2),"and",(y1,y2),"is:",result)



