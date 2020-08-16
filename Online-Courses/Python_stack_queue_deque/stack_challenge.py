'''

balanced parenthesis challenges
given a string of only opening and closing brackets , find whether it is balanced or not??
'''

from stack_class import Stack


def match_symbols(sbs):
    s = Stack()
    symbol_pairs = {
        '(': ')',
        '[': ']',
        '{': '}',
    }

    openers = symbol_pairs.keys()

    index = 0
    while index < len(sbs):
        symbol = sbs[index]
        if symbol in openers:
            s.push(symbol)
        else:
            if s.is_empty():
                return False
            else:
                top_item = s.pop()
                if symbol != symbol_pairs[top_item]:
                    return False

        index += 1

    if s.is_empty():
        return True

    return False


print(match_symbols('([{}])'))
print(match_symbols('(([{}]])'))


