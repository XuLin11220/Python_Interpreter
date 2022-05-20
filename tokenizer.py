import re

class Tokenizer:
    # match space, remove space from input
    space = re.compile(r'\s+')
    
    # dictionary that contains all the tokens
    tokens = {
        'Identifier': re.compile(r'[a-zA-Z_]([a-zA-Z_]|[0-9])*'),
        'Literal': re.compile(r'0|[1-9][0-9]*'),
        '=': re.compile(r'='),
        ';': re.compile(r';'),
        '+': re.compile(r'\+'),
        '-': re.compile(r'-'),
        '*': re.compile(r'\*'),
        '(': re.compile(r'\('),
        ')': re.compile(r'\)'),
        'Invalid': re.compile('.')}

    def __init__(self, file_text):
        self.file_text = re.sub(self.space, '', file_text)
        self.curr_index = 0
        self.last_index = len(self.file_text)

    def next_token(self):
        # read read from 0 to last
        if self.curr_index < self.last_index:
            for token in self.tokens:
                # check for a match at current position with the token dictionary
                check = self.tokens[token].match(self.file_text, self.curr_index)
                if check:
                    # print error if found anything invalid
                    if token == 'Invalid':
                        raise Exception("Invalid Token")
                    else:
                        # return token as string form and token type
                        self.curr_index = check.end()
                        return {'token': self.file_text[check.start():check.end()], 'type': token}
        else:
            # EOF End of file
            return {'token': '', 'type': 'EOF'}
