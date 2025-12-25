import sys

text = sys.stdin.read()

dict = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

counter = [0] * 26

for alph in text:
    if alph.islower():
        counter[ord(alph) - ord("a")] += 1

max_num = 0
print_char = ""

for idx, count in enumerate(counter):
    if count >= max_num:
        if count > max_num:
            print_char = dict[idx]
            max_num = count
        else:
            print_char += dict[idx]


print(print_char)