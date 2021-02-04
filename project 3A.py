def main():
    file = input("Enter the name of a python file: ")  ### request the file from the user
    countFor = 0              ### Count your If, While, For, Else
    countWhile = 0
    countIf = 0
    countElse = 0


    f = open(file, "r")             ### Opening and Reading the file the user entered
    allTheLines = f.readlines()      ### read all lines in the file
    
    for line in allTheLines:
        
        words = line.split()         ### split words in the line

        for word in words:              
            #print(word)
            if "#" in word:           ### Do not count any word with # before it
                break
            if word == "for":         ### count for in the words
                countFor += 1
            elif word == "while":     ### count while
                countWhile += 1
            elif word == "if":        ### count if
                countIf += 1
            elif word == "else:":     ### count else
                countElse += 1
    print("fors: "+str(countFor),end=" ")   ###Records the total number of for
    print("whiles: "+str(countWhile),end=" ")## Records the total number of While
    print("ifs: "+str(countIf),end=" ")        ### Records the total number of ifs
    print("elses: "+str(countElse),end="\n")   ### Records the total number of else

    if countElse > countIf:                   ### Checking if total number of Else is more than If
        print("every else needs an if")

main()

