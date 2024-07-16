
from package import math_cal as mo 
# alies (changing math_operation as mo)

values=[]

print("Enter the number's of calulation")
number = int(input())

for i in range (1,number+1):
    
    var = int(input(f"Enter the {i} numbers:"))
    values.append(var)
    tup = tuple(values)
    # print(values)
    


print("Please select operation -\n" \
        "1. +\n" \
        "2. -\n" \
        "3. *\n" \
        "4. /\n" \
        "4. %\n")

select = int(input("Select operations from 1, 2, 3, 4, 5:"))
    
    

if select == 1:
    print("Result:", mo.addition(*tup))
elif select == 2:
    print("Result:", mo.subtract(*tup))
elif select == 3:
    print("Result:", mo.multipy(*tup))
elif select == 4:
    print("Result:", mo.divide(*tup))
elif select == 5:
    if len(tup) == 2:  # modulus requires exactly 2 numbers
        print("Result:", mo.modulus(*tup))
    else:
        print("Modulus operation requires exactly 2 numbers.")
else:
    print("Invalid input")