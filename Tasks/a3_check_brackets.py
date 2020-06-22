def check_brackets(brackets_row: str) -> bool:
    """
    Check whether input string is a valid bracket sequence
    Valid examples: "", "()", "()()(()())", invalid: "(", ")", ")("
    :param brackets_row: input string to be checked
    :return: True if valid, False otherwise
    """
    c = 0
    for b in brackets_row:
        if b == "(":
            c += 1
        elif b == ")":
            c -= 1
        if c < 0:
            return False
    return True if not c else False

# если исходить из того что:
#     открывающая скобка должна закрыться
#     закрывающая не существует без открывающей идущей ранее


