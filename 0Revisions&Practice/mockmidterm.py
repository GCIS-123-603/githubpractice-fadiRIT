

def recursivePower(base,exponent):
    if exponent<1:
      return 1
    else:
       return base * recursivePower(base,exponent-1)
    
call = recursivePower(2,4)
print(call)