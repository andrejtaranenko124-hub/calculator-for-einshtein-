print('Салам Алекум, вы используете калькулятор от крутого \'Андрея\'®')
print('выберите язык: english or russian')
language = input()
if language == 'english':
    print('Easter egg list = Einstein, Smart, kalculator')
    print('Choose option (+, -, *, /, ** (exponentiation), ** 0,5 (the square root)')
    operation = input()
elif language == 'russian':
    print('Лист пасхалок = Einstein, Smart, kalculator')
    print('выберете опцию (+, -, *, /, ** (степень), ** 0,5 (квадратный корень)')
    operation = input()
    print(operation)
else:
    print('error')

    
