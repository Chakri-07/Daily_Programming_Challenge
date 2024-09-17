import ast
def longest_prefix(str):
    if not str:
        return "[]"
    prefix = str[0]
    for s in str[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return "[]"
    return prefix
input_str = input("Enter the complete input string: ")
str = ast.literal_eval(input_str)
print(longest_prefix(str))