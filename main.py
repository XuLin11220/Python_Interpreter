from interpreter import Interpreter

#1.python main.py
#2.test_cases/filename.txt
input_text = input('Enter test file name: ')
file_name = open(input_text, 'r')
print(f'Output from file:{input_text}')

try:
    program = Interpreter(file_name.read())
    for variable, value in program.var.items():
        #variable = value
        print('%s = %i' % (variable, value))
except Exception as error:
    print(error)

file_name.close()