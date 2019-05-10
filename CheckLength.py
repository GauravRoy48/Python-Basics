def give_length(a):
    if type(a) is int:
        return "ERROR!!\n|Sorry integers don't have length.|"
    elif type(a) is float:
        return "ERROR!!\n|Sorry floats don't have length.|"
    else:
        return len(a)

var = 23.9
print("\nLength of string is "+str(give_length(var)))