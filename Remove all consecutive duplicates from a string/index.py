def removeDuplicate(text):
    text2 = [text[0]]
    n = len(text)
    for i in range(1,n):
        if(text[i]!=text[i-1]):
            text2.append(text[i])
    
    return ''.join(text2) # .join ifadesi listeyi string ifadesine çevirir
    # Bir string ifadeyi de listeye çevirmek için list(text) yapman lazım.
"""
JOin kullaniminin tam tersi olarak
l = ['m', 'e', 'r', 'h', 'a']
s = ''.join(l)
print(s)  # merha
"""

def useRecursive(s):
        if len(s) < 2:
            return s
        if s[0] != s[1]:
            return s[0] + useRecursive(s[1:])
        return useRecursive(s[1:])

text = "aaaaabcbbbbb"

print(useRecursive(text))
    
# Recursion usage 
