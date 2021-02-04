file = input("Enter the file you want to decrypt: ")
name = input("Enter the name of file you want to write to: ")
key = int(input("Enter the key for your decryption: "))

f = open(file, "r")  ###opens and read file
w = open(name,"w")   ### name of file to decrypt to

for line in f:
    for i in range(len(line)):       ### it goes through every character in the line
        char = line[i]
        if char == "~":
            2+2==4             ###do nothing, just to avoid indentation syntax error 
        elif line[i-1] == "~":   ###character before this was a ~ 
            x = ord(char)        
            x = x ^ key
            newChar = chr(x)
            w.write(newChar)     ### write decrypted character
        else:
            w.write(char)

f.close()
w.close()        ###Closes the program           
              

