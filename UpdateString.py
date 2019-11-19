def UpdateString (string1, string2, index):
    new_string = string1[:index] + string2 + string1[index+1:]
    print(new_string)
