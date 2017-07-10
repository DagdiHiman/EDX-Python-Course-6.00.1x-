s="This is great!"
def print_without_vowels(s):
    '''
    s: the string to convert
    Finds a version of s without vowels and whose characters appear in the 
    same order they appear in s. Prints this version of s.
    Does not return anything
    '''
    new=''
    v=['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for letter in s:
        if letter not in v:
            new+=letter
            #print(new)
    return new

x=print_without_vowels(s)     
print(x)     