

def are_anagrams(str1,str2):
    #remove spaces and convert both strings to lowers case

    str1 = str1.replace(" ","").lower()    #replace syntax replace(old,new)
    str2 = str2.replace(" ","").lower()


    #check if sorted charcters of both strings arev same
    return sorted(str1) == sorted(str2)


str1 = "listen"
str2 = "silenT"

print(are_anagrams(str1, str2))