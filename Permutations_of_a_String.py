import itertools
def unique_permutations(s: str):
    return list(set([''.join(p) for p in itertools.permutations(s)]))

s = input("Enter String: ")
print(unique_permutations(s))
