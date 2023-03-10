import getopt, sys

# Remove 1st argument from the
# list of command line arguments
argumentList = sys.argv[1:]

def test_funk(arg):
    return print(f'worked - {arg}')

test_funk(argumentList)