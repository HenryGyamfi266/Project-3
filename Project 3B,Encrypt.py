def encrypt_file():
    try:
        file = input("Enter the file you want to encrypt: ")
        name = input("Enter the name of the output file: ")
        key = int(input("Enter the key for your encryption (0-255): "))

        if not (0 <= key <= 255):
            print("Error: Key must be between 0 and 255.")
            return

        with open(file, "r") as f, open(name, "w") as w:
            for line in f:
                for char in line:
                    if "a" <= char <= "z" or "A" <= char <= "Z":  # Encrypt both lowercase and uppercase letters
                        x = ord(char)  # Convert to Unicode
                        x = x ^ key    # XOR with the key
                        newChar = chr(x)
                        w.write("~")   # Indicate encrypted character
                        w.write(newChar)
                    else:
                        w.write(char)  # Write non-encrypted characters as-is

        print(f"Encryption completed. Output written to '{name}'.")

    except FileNotFoundError:
        print("Error: The specified input file does not exist.")
    except ValueError:
        print("Error: Invalid key. Please enter an integer value.")

encrypt_file()
