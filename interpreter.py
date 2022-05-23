from tokenizer import Tokenizer

class Interpreter:
    def __init__(self, file_text):
        self.file_text = Tokenizer(file_text)
        self.curr_token = {}
        self.var = {}
        self.program()
        # Program starts

    def program(self):
        while True:
            # read and store it into curr_token
            self.curr_token = self.file_text.next_token()
            # if it's end of file, it means nothing to read, end of program.
            if self.curr_token['type'] == 'EOF':
                break
            if self.curr_token['type'] == 'Identifier':
                variable = self.curr_token['token']
                # read and store it into curr_token
                self.curr_token = self.file_text.next_token()
                # match = 
                self.match_token('=')
                expression = self.expression()
                # match ;
                self.match_token(';')
                self.var[variable] = expression

    def match_token(self, valid_token):
        # check if token type is exist or not
        if self.curr_token['type'] != valid_token:
            raise Exception('Error, invalide token')

    def expression(self):
        term = self.term()   
        result = self.expression_prime() + term
        return result

    def expression_prime(self):
        # eliminate left recursion
        if self.curr_token['type'] == '-':
            term = self.term()
            result = self.expression_prime() + (-1 * term)
            return result
        elif self.curr_token['type'] == '+':
            term = self.term()
            result = self.expression_prime() + term
            return result
        else:
            return 0

    def term(self):
        factor = self.factor()
        result = self.term_prime() * factor
        return result

    # eliminate left recursion
    def term_prime(self):
        # read and store it into curr_token
        self.curr_token = self.file_text.next_token()
        if self.curr_token['type'] == '*':
            factor = self.factor()
            result = self.term_prime() * factor
            return result
        else:
            return 1

    def factor(self):
        # read and store it into curr_token
        self.curr_token = self.file_text.next_token()
        if self.curr_token['type'] == '+':
            return self.factor()
        elif self.curr_token['type'] == '-':
            return self.factor() * -1
        elif self.curr_token['type'] == '(':
            result = self.expression()
            self.match_token(')')
            return result
        elif self.curr_token['type'] == 'Literal':
            return int(self.curr_token['token'])
        elif self.curr_token['type'] == 'Identifier':
            if self.curr_token['token'] in self.var:
                return self.var.get(self.curr_token['token'])
            else:
                raise Exception('Error, worng token')
