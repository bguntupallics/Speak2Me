WORD_TO_OP = {
    "add": "+", "plus": "+",
    "subtract": "-", "minus": "-",
    "multiply": "*", "times": "*",
    "divide": "/", "divided": "/",
}

WORD_TO_NUMBER = {
    "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
    "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
    "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13,
    "fourteen": 14, "fifteen": 15, "sixteen": 16, "seventeen": 17,
    "eighteen": 18, "nineteen": 19, "twenty": 20,
}

ORDINAL_TO_NUMBER = {
    "square": 2, "cube": 3, "fourth": 4, "fifth": 5,
    "sixth": 6, "seventh": 7, "eighth": 8, "ninth": 9,
}


def _try_parse_number(word: str) -> float | None:
    lower = word.lower()
    if lower in WORD_TO_NUMBER:
        return float(WORD_TO_NUMBER[lower])
    try:
        return float(word)
    except ValueError:
        return None


def parse(text: str) -> list[float | str]:
    words = text.lower().split()
    tokens: list[float | str] = []

    i = 0
    while i < len(words):
        word = words[i]

        # Skip filler words
        if word in ("and", "by", "the", "of", "to"):
            i += 1
            continue

        # Operators from words
        if word in WORD_TO_OP:
            tokens.append(WORD_TO_OP[word])
            i += 1
            continue

        # Operator symbols
        if word in ("+", "-", "*", "/", "^"):
            tokens.append("**" if word == "^" else word)
            i += 1
            continue

        # "squared" → ** 2
        if word == "squared":
            tokens.append("**")
            tokens.append(2.0)
            i += 1
            continue

        # "cubed" → ** 3
        if word == "cubed":
            tokens.append("**")
            tokens.append(3.0)
            i += 1
            continue

        # "power" → next number is the exponent
        if word == "power":
            tokens.append("**")
            i += 1
            continue

        # "<ordinal> root <number>" e.g. "cube root 27" or "square root 16"
        if word in ORDINAL_TO_NUMBER and i + 1 < len(words) and words[i + 1] == "root":
            n = ORDINAL_TO_NUMBER[word]
            tokens.append(float(1 / n))
            tokens.append("root")
            i += 2  # skip "root"
            continue

        # "root" alone (default square root)
        if word == "root":
            tokens.append(0.5)
            tokens.append("root")
            i += 1
            continue

        # Numbers
        num = _try_parse_number(word)
        if num is not None:
            tokens.append(num)
            i += 1
            continue

        # Skip unrecognized words
        i += 1

    return tokens


def calculate(tokens: list[float | str]) -> float:
    if len(tokens) == 0:
        raise ValueError("Empty expression")

    if len(tokens) == 1:
        if isinstance(tokens[0], (int, float)):
            return float(tokens[0])
        raise ValueError(f"Cannot evaluate: {tokens}")

    if len(tokens) < 3:
        raise ValueError(f"Incomplete expression: {tokens}")

    a = tokens[0]
    op = tokens[1]
    b = tokens[2]

    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError(f"Expected numbers, got: {a} {op} {b}")

    if op == "+":
        return float(a + b)
    elif op == "-":
        return float(a - b)
    elif op == "*":
        return float(a * b)
    elif op == "/":
        if b == 0:
            raise ValueError("Division by zero")
        return float(a / b)
    elif op == "**":
        return float(a ** b)
    elif op == "root":
        return float(b ** a)
    else:
        raise ValueError(f"Unknown operator: {op}")
