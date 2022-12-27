def string_reverse(str1):
    rev =""
    x=len(str1)
    while x>0:
        rev+=str1[x-1]
        x=x-1
    return rev
print(string_reverse("1234abcd"))
    
