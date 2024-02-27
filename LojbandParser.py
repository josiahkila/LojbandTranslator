
from enum import Enum

# Define the TokenType enum for different kinds of tokens
class TokenType(Enum):
    STATEMENT_START = 'i'  # Start of a new statement
    NAME = 'name'          # Names
    NUMBER = 'number'      # Numbers
    PREDICATE_WORD = 'predicate_word'  # Predicate words
    SHORT_WORD = 'short_word'  # Short words (like "lo", "ku", etc.)
    EOF = 'EOF'            # End of file/input

# Token class to represent each token with type and value
class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        return f"Token({self.type}, {self.value})"

# Lexer class to tokenize the input
class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0

    def get_next_token(self):
        # Tokenization logic to split input into tokens
        if self.pos >= len(self.text):
            return Token(TokenType.EOF, None)
        
        # Simplified tokenization logic for demonstration
        current_char = self.text[self.pos]
        
        if current_char.isalpha():
            token = self.handle_word()
            return token
        elif current_char.isdigit():
            token = self.handle_number()
            return token
        elif current_char == 'i':
            self.pos += 1
            return Token(TokenType.STATEMENT_START, 'i')
        
        self.pos += 1
        return Token(TokenType.EOF, None)

    def handle_word(self):
        # Handle word tokenization (simplified)
        start_pos = self.pos
        while self.pos < len(self.text) and self.text[self.pos].isalpha():
            self.pos += 1
        word = self.text[start_pos:self.pos]
        # Simplified logic to classify words
        if len(word) <= 2:
            return Token(TokenType.SHORT_WORD, word)
        else:
            return Token(TokenType.PREDICATE_WORD, word)

    def handle_number(self):
        # Handle number tokenization
        start_pos = self.pos
        while self.pos < len(self.text) and self.text[self.pos].isdigit():
            self.pos += 1
        number = self.text[start_pos:self.pos]
        return Token(TokenType.NUMBER, number)

# Parser class to parse the tokens
class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def eat(self, token_type):
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            raise Exception(f"Invalid syntax: expected {token_type}, got {self.current_token.type}")

    def parse(self):
        # Parse the entire input
        statements = []
        while self.current_token.type != TokenType.EOF:
            statements.append(self.parse_statement())
        return statements

    def parse_statement(self):
        # Parse a single statement (simplified for demonstration)
        self.eat(TokenType.STATEMENT_START)
        # Assuming a simple structure for statements here for demonstration
        parts = []
        while self.current_token.type in [TokenType.NAME, TokenType.NUMBER, TokenType.PREDICATE_WORD]:
            parts.append(self.current_token.value)
            self.eat(self.current_token.type)
        return parts

# Assuming the input is a simple string for demonstration
input_text = "i bridi lo prenu ku"

# Create a lexer and parser
lexer = Lexer(input_text)
parser = Parser(lexer)

# Parse the input
parsed_output = parser.parse()

print("Parsed Output:", parsed_output)
