# Here, I implement a decryption method to reverse the encryption process applied in the project 3B,Encrypt.py part.
def decrypt_file():
    try:
        file = input("Enter the file you want to decrypt: ")
        name = input("Enter the name of the output file: ")
        key = int(input("Enter the key for your decryption (0-255): "))

        if not (0 <= key <= 255):
            print("Error: Key must be between 0 and 255.")
            return

        with open(file, "r") as f, open(name, "w") as w:
            for line in f:
                i = 0
                while i < len(line):
                    char = line[i]
                    if char == "~":
                        i += 1  # Skip the "~" character
                        if i < len(line):
                            encrypted_char = line[i]
                            x = ord(encrypted_char)  # Geting Unicode value
                            x = x ^ key             # XOR with the decryption key
                            newChar = chr(x)        # Converting back to character
                            w.write(newChar)
                    else:
                        w.write(char)
                    i += 1

        print(f"Decryption completed. Output written to '{name}'.") # shows end of decryption

    except FileNotFoundError:
        print("Error: The specified input file does not exist.")
    except ValueError:
        print("Error: Invalid key. Please enter an integer value.")

decrypt_file()
       
              

