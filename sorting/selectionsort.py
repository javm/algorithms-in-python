from random import randint

INPUT_SIZE = 10
MAX_VAL = 50
input_list = []


#Intializing the input
for i in range(INPUT_SIZE):
    input_list.append(randint(0, MAX_VAL))


def minIndex(i, input):
    index = i
    for j in range(i+1, len(input)):
        if(input[j] < input[index] ):
            index = j
    return index

def swap(i,j, input):
    temp = input[i]
    input[i] = input[j]
    input[j] = temp

def selectionsort(input):
    for i in range(len(input)-1):
        j = minIndex(i, input)
        swap(i,j,input)

for i in range(INPUT_SIZE):
    print input_list[i]

print "Selection sort..."
selectionsort(input_list)

for i in range(INPUT_SIZE):
    print input_list[i]
