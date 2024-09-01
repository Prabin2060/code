# cook your dish here
import sys
wdata= sys.stdin.read().strip()
data= wdata.split()
t= int(data[0])

    
def para(s):
    stack=[]
    
    for char in s:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if stack:
                stack.pop()
            else:
                return 0
    
    return 1 if not stack else 0
    
results= []
for i in range(1,t+1):
    s= data[i]
    results.append(para(s))

for result in results:
    print(result)
    


