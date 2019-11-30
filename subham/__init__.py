#shubham
##1
a=100
b=200

"""
def fun(a,b):
    c=a
    a=b
    b=c
    print(a,b)

fun(a,b)

##2

def rev(x):
    y=str()
    for i in range(round(len(x)/2)):
        y[i]=x[len(x)-i-1]
    print(y)

x="asdf"

rev(x)
   """ 


##3
def nll(a,b):
    q=[a,b]
    print(q)
    return q
    
    

def nl(x,y):
    for i in range(len(x)):
        nll(x[i],y[i])

x=[2,3,7,4]
y=[5,8,9,7]
nl(x,y)

def fct(n):
    ft=1
    for i in range(1,n+1):
        ft=i*ft
    print(ft)
fct(5)


def fbncy(n):
    a=0
    b=1
    print(a);print(b)
    for i in range(n):
        c=a+b
        print(c)
        a=b
        b=c
fbncy(10)
    


def rvrs(l):
    for i in range(round(len(l)*0.5)):
        tmp=l[i]
        l[i]=l[len(l)-i-1]
        l[len(l)-i-1]=tmp
l=[1,2,3,4,5]
rvrs(l)
print(l)





l=[1,2,3,4,5,2,3]
k=[0]*len(l)
for i in range(len(l)):
    c=0
    for j in range(len(l)):
        if l[i]==l[j]:
            c=c+1
    k[i]=c

for i in range(len(l)):
    if k[i]==1:
        print(l[i])
        
        


inputstr="time now is 10:54 am"
isdigit2=lambda ch: True if ch in "0123456780" else False
output2= [ch for ch in inputstr if indigit2(ch)]
print



def myfunction():
    status = True
    fp1 = None
    try:
        mydata = [100,200,300]
        print(mydata[1])
        fp1 = open("some_file.txt")    
        return status
        a = 100
        b = 0
        print(a/b)
    except ZeroDivisionError as er1:
        print("error first block", er1)
        print("closing file")
        fp1.close()
    except (FileNotFoundError, IndexError) as er:
        print("error second block",er)
        status = False
    except Exception as e3:
        print("general error block",e3)
        status = False
    else:
        print("all is well")
        status = False
    finally:
        print("closing file pointer")
        if fp1:
            fp1.close()
    
    return status

call_status = myfunction()
print(call_status)
