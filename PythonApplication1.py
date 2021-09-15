a = []
n = int(input('enter number of array\t'))
print("enter elements of array")
for i in range(n):
    a.append(int(input()))
liva = False
for i in range(0, n-1):
    p = i + 1
    if (a[i] > 0 and a[p] < 0) or (a[i] < 0 and a[p] > 0):
        liva = True
    else:
        liva = False
        break

sumar = 0
if liva == True :
    for i in range(n):
        if a[i] > 0:
            sumar += a[i]
    print("sum of positive elements is: ",sumar)

if liva == False :
    for i in range(n):
        if a[i] < 0:
            print("negative numbers is: ",a[i])