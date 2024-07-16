# python program for calculator

#function for addition 

def addition(*number):
    total = 0
    for num in number:
        total += num
    return total


# Function for subtract 

def subtract(*number):
    diff = number[0]
    for num in number[1:]:
        diff = diff - num
    return diff



    
    
    
    
                                                  
# Function  for multiply
def multiply(*number):
    product = 1
    for num in number:
        product *= num
    return product
    
    


# Function for modulus
def modulus (*number):
    rem = number[0]
    if number [1]!=0:
        if rem > number[1]:
            return rem % number[1]
        elif rem < number [1]:
            return  number[1] % rem
    else:
      print("error")
    