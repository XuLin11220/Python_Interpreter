from tokenizer import Tokenizer

class Interpreter:
    def __init__(self, file_text):
        self.file_text = Tokenizer(file_text)
        self.curr_token = {}
        self.symbol = {}
        self.program()

    def program(self):
        while True:
            self.curr_token = self.file_text.next_token()
            if self.curr_token['type'] == 'EOF':
                break
            if self.curr_token['type'] == 'Identifier':
                variable = self.curr_token['token']
                self.curr_token = self.file_text.next_token()
                self.match_token('=')
                expression = self.expression()
                self.match_token(';')
                self.symbol[variable] = expression

    def match_token(self, valid_token):
        # check if token type is exist or not
        if self.curr_token['type'] != valid_token:
            raise Exception('Error, invalide token')

    def expression(self):
        term = self.term()
        result = term + self.expression_prime()
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
        return self.term_prime() * factor

    # eliminate left recursion
    def term_prime(self):
        self.curr_token = self.file_text.next_token()
        if self.curr_token['type'] == '*':
            factor = self.factor()
            return self.term_prime() * factor
        else:
            return 1

    def factor(self):
        self.curr_token = self.file_text.next_token()
        if self.curr_token['type'] == 'Literal':
            return int(self.curr_token['token'])
        elif self.curr_token['type'] == 'Identifier':
            if self.curr_token['token'] in self.symbol:
                return self.symbol.get(self.curr_token['token'])
            else:
                raise Exception('Error, worng token')
        elif self.curr_token['type'] == '+':
            return self.factor()
        elif self.curr_token['type'] == '-':
            return -1 * self.factor()
        elif self.curr_token['type'] == '(':
            result = self.expression()
            self.match_token(')')
            return result
