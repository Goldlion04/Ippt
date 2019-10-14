x = float(input("Число №1"))
y = float(input("Число №2"))
operation = input("Введіть операцію")

result = None

if operation == '+' :
    result = x + y
elif operation == '-' :
    result = x - y
elif operation == '*' :
    result = x * y
elif operation == '/' :
    result = x / y
else:
    print('Unsupported operation')

if result is not None:
    print ('Результат:', result)
    
    
    
