def factorial(fac):
    r=1
    for item in range(fac,1,-1):
        r*=item
    return r

print(factorial(3))
print(factorial(5))