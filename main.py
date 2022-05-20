from interpreter import Interpreter

input_text = input('Enter test file name: ')
file_name = open(input_text, 'r')
print(f'Output from file:{input_text}')

try:
    program = Interpreter(file_name.read())
    for variable, value in program.symbol.items():
        print('%s = %i' % (variable, value))
except Exception as error:
    print(error)

file_name.close()