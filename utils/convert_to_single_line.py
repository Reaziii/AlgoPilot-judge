import re


def convert_to_single_line(code_string):
    code_string = re.sub("\w", "\\w", code_string)
    return code_string
