def convert_to_single_line(code_string):
    code_string = code_string.replace('"', '\\"')
    # code_string = code_string.replace('\n', '\\n')
    # code_string = code_string.replace('\\xttt', '\n')
    return code_string
