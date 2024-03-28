from typing import List, Tuple, Union, Optional
from constants import *
from handlers import Position, IllegalCharError
from tokenizer import Token

class Lexer:
    def __init__(self, fname: str, text: str) -> None:
        self.fname: str = fname
        self.text: str = text
        self.pos: Position = Position(-1, 0, -1, fname, text)
        self.curr_char: Optional[str] = None
        self.advance()

    def advance(self) -> None:
        """Advances the position and updates the current character."""
        self.pos.advance(self.curr_char)
        self.curr_char = self.text[self.pos.idx] if self.pos.idx < len(self.text) else None

    def make_number(self) -> Token:
        """Handles number creation, both integers and floats."""
        num_str: str = ''
        dot_count: int = 0

        while self.curr_char is not None and (self.curr_char.isdigit() or self.curr_char == "."):
            if self.curr_char == ".":
                if dot_count == 1: break  # Ensures only one dot is present for valid floats
                dot_count += 1
            num_str += self.curr_char
            self.advance()

        if dot_count == 0:
            return Token(TT_INT, int(num_str))
        else:
            return Token(TT_FLOAT, float(num_str))

    def make_tokens(self) -> Union[List[Token], Tuple[None, IllegalCharError]]:
        """Tokenizes the input text."""
        tokens: List[Token] = []

        # Mapping of single-character tokens to their types
        token_map: Dict[str, str] = {
            '+': TT_PLUS,
            '-': TT_MINUS,
            '*': TT_MUL,
            '/': TT_DIV,
            '(': TT_LPAREN,
            ')': TT_RPAREN,
        }

        while self.curr_char is not None:
            # Skip whitespace
            if self.curr_char in " \t":
                self.advance()
                continue

            # Number detection
            if self.curr_char.isdigit() or (self.curr_char == '.' and self.peek() in DIGITS):
                tokens.append(self.make_number())
                continue

            # Single-character token detection
            elif self.curr_char in token_map:
                tokens.append(Token(token_map[self.curr_char]))
                self.advance()
                continue

            # Illegal character error handling
            else:
                pos_start: Position = self.pos.copy()
                illegal_char: str = self.curr_char
                self.advance()
                return [], IllegalCharError(pos_start, self.pos, f"'{illegal_char}'")

        return tokens, None

    def peek(self) -> Optional[str]:
        """Peeks at the next character without advancing the lexer position."""
        peek_pos: int = self.pos.idx + 1
        if peek_pos < len(self.text):
            return self.text[peek_pos]
        return None
