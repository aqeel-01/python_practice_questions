

def count_vowels(input_string):
    vowels = "aeiouAEIOU"

    count = 0

    for char in input_string:
        if char in vowels:
            count += 1
    return count


input_str = "hello World !"
output = count_vowels(input_str)
print(output)