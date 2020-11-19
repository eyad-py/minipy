
def customized_find(sentence,character): # here to find location of the character in the sentence
    return [i for i ,j in list(enumerate(sentence)) if j == character]

def customized_split(sentence,character):
    lst= customized_find(sentence,character)
    string=''
    final=[]
    string = sentence[:lst[0]] # from the beginning of the sentence to the first character 
    final.append(string) # add it to the new list "final"
    for i in range(len(lst)-1): # loop to get the rest of characters
        string =sentence[lst[i]+1:lst[i+1]]
        final.append(string)
    string = sentence[lst[-1]+1:] # the rest of the sentence after the last character
    final.append(string)
    return final # return the list 
