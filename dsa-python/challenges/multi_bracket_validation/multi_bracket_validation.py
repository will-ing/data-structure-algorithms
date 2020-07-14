def multi_bracket_validation(value):
    bracket_storage = []
    result = True

    for curr in str(value):
        if (curr == ')' or curr == '}' or curr == ']') and bracket_storage == None:
            return False
        else:
            if curr == '(' or curr == '{' or curr == '[':
                bracket_storage.append(curr)
            elif curr == ')' or curr == '}' or curr == ']':
                last = bracket_storage[-1]
                if last == '(' and curr == ')' or last == '[' and curr == ']' or last == '{' and curr == '}':
                    result = True
                    bracket_storage.pop()
                else:
                    return False
            else:
                result = False
    if bracket_storage != None:
        return result
    else:
        return result
