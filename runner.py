from typing import List, Tuple, Union, Optional
from lexer import Lexer
from tokenizer import Token
from handlers import Error

def run(fname: str, text: str) -> Union[Tuple[List[Token], None], Tuple[None, Error]]:
    """
    Processes the given text with the Lexer and returns the generated tokens and any errors.

    Parameters:
    - fname: The name of the file containing the text to be processed.
    - text: The actual text content to be tokenized.

    Returns:
    A tuple containing either a list of tokens and None if no error occurred, or None and an error object.
    """
    lexer = Lexer(fname, text)
    tokens, error = lexer.make_tokens()

    return tokens, error
