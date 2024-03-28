class Position:
    def __init__(self, idx: int, ln: int, col: int, fname: str, ftext: str) -> None:
        self.idx: int = idx
        self.ln: int = ln
        self.col: int = col
        self.fname: str = fname
        self.ftext: str = ftext

    def advance(self, current_char: str = None) -> "Position":
        self.idx += 1
        self.col += 1

        if current_char == '\n':
            self.ln += 1
            self.col = 0

        return self

    def copy(self) -> "Position":
        return Position(self.idx, self.ln, self.col, self.fname, self.ftext)

class Error:
    def __init__(self, pos_start: Position, pos_end: Position, error_name: str, details: str) -> None:
        self.pos_start: Position = pos_start
        self.pos_end: Position = pos_end
        self.error_name: str = error_name
        self.details: str = details

    def __str__(self) -> str:
        return (f"{self.error_name}: {self.details} \nFile {self.pos_start.fname}, "
                f"Line {self.pos_start.ln + 1}, at {self.pos_start.col}.")

class IllegalCharError(Error):
    def __init__(self, pos_start: Position, pos_end: Position, details: str) -> None:
        super().__init__(pos_start, pos_end, "Illegal Character", details)
