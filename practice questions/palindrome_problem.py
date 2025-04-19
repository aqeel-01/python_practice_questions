


def is_palindrome(s: str) -> bool:
    
    #remove any non-alphanumeric charcter ,convert into lowecase,then join each char with non-space
    cleaned_string = ''.join(char.lower() for char in s if char.isalnum())
    

    #check if the string is the same if we reverse it ,using slicing
    return cleaned_string == cleaned_string[::-1]


print(is_palindrome("madam"))
print(is_palindrome("hi"))


