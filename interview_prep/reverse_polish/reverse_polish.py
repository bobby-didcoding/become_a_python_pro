"""
Reverse Polish Notation Calculator

Reverse polish notation is a way of writing a sequence of arithmetic operations
without relying on brackets to disambiguate the order (which you would need
with standard infix operators).

The operator follows two operands (which may be the result of a previous
evaluated expression). So "1 1 +" is equivalent "1 + 1", i.e. evaluates to "2".

Examples:
i)   20 10 4 - 3 * +                == 20 10 4 - 3 * +
                                    == 20 6 3 * +
                                    == 20 18 +
                                    == 38

ii)  87 19 * 10 - 30 9 * 4 - 10 + - == 1367
"""

operators = ["+", "-", "*"]

def calc(a, o, b):
    if o == "+":
        return a + b
    elif  o == "-":
        return a - b
    else:
        return a * b


def first(validated_str):

    val_length = len(validated_str)

    for r in range(val_length):
        if validated_str[r] in operators:

            temp = calc(int(validated_str[r-2]), validated_str[r], int(validated_str[r-1]))

            start = validated_str[:r-2]
            end = validated_str[r+1:]

            new = start + [temp] + end
            return new


def evaluate(reverse_polish_expression):
    """
    Returns the result from evaluating the string reverse_polish_expression.

    Assume that the expression is syntactically valid, that all operands are
    integers, and that the operators available are {+, -, *}.
    """
    
    validated_str = reverse_polish_expression.split(" ")

    print(first(validated_str))

    

            

    return(print(validated_str))

evaluate('20 10 4 - 3 * +')
