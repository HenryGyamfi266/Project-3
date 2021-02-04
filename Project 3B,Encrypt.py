file = input("Enter the file you want to encrypt: ")
name = input("Enter the name of file you want to write to: ")
key = int(input("Enter the key for your encryption: "))

f = open(file, "r")     ###open and read file user want to encrypt 
w = open(name,"w")      ###opens the file the user wants to write the encryption to 

for line in f:
    for char in line:
        if "a" <= char and "z" >= char:     ###this checks for a lower case letter
            x = ord(char)                  ### converts to the unicode number
            x = x ^ key                    ###XOR of the key
            newChar = chr(x)
            w.write("~")                    ###it shows a character has been encrypted
            w.write(newChar)        
        else:
            w.write(char)             ###writes the normal character

f.close()
w.close()                      ###Closes my program
            

