import ast
def group_anagrams(str):
    anagram_dict = {}
    for word in str:
        sorted_word = ''.join(sorted(word))
        if sorted_word not in anagram_dict:
            anagram_dict[sorted_word] = []
        anagram_dict[sorted_word].append(word)
    return list(anagram_dict.values())
input_str = input("Enter the complete string array: ")
str = ast.literal_eval(input_str)
print(group_anagrams(str))