list = ['E',1,0,'a','A','b','c','B','d',4,5,6,'e']
def letter(max,min):
    first_input = max
    second_input = min
    if type(first_input) == str:
        first_input = ord(first_input)
        if(first_input>91):
            first_norm = first_input - 97
        else:
            first_norm = first_input - 65
    else:
        first_norm = first_input
    if type(second_input) == str:
        second_input = ord(second_input)
        if(second_input>91):
            second_norm = second_input - 97
        else:
            second_norm = second_input - 65
    else:
        second_norm = second_input
    if first_norm == second_norm and type(min) != str:
        return True
    elif(first_norm == second_norm and first_input < second_input and type(max) != str):
        return False
    elif(first_norm == second_norm and first_input < second_input):
        return True
    elif(first_norm > second_norm):
        return True
    return False
    
def part(list,min,max):
    pivot = list[min]
    i = max+1
    for j in range(max,min,-1):
        if (letter(list[j] , pivot)) :
            i -= 1
            temp = list[j]
            list[j] = list[i]
            list[i] = temp

    temp = list[i-1]
    list[i-1] = list[min]
    list[min] = temp
    return (i-1)
def quickSort(list,min,max) :
    if (min<max) :
        partIndex = part(list,min,max)
        quickSort(list,min,partIndex-1)
        quickSort(list,partIndex+1,max)
    
quickSort(list,0,len(list)-1)
print(list)