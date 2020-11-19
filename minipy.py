
def customized_find(sentence,character):
    return [i for i ,j in list(enumerate(sentence)) if j == character]

def customized_split(sentence,character):
    lst= customized_find(sentence,character)
    string=''
    final=[]
    string = sentence[:lst[0]]
    final.append(string)
    for i in range(len(lst)-1):
        string =sentence[lst[i]+1:lst[i+1]]
        final.append(string)
    string = sentence[lst[-1]+1:]
    final.append(string)
    return final
