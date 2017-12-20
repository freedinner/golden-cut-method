def f(x):
    return x*x+10*x
erro=input("请输入误差范围：")
erro=float(erro)
a=input("请输入区间a:")
a=float(a)
b=input("请输入区间b:")
b=float(b)
c=b-0.618*(b-a)
d=a+0.618*(b-a)
while abs(b-a)>erro:
    f1=f(c)
    f2=f(d)
    if f1<f2:
        b=d
        c=b-0.618*(b-a)
        d=a+0.618*(b-a)
    if f1>f2:
        a=c
        c=b-0.618*(b-a)
        d=a+0.618*(b-a)
e=0.5*(a+b)        
print(e)
print(f(e))
    
            
   
    
