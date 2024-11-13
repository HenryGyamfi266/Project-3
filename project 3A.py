def main():
    try:
        file = input("Enter the name of a Python file: ")  # Request the file from the user
        countFor = 0
        countWhile = 0
        countIf = 0
        countElse = 0

        with open(file, "r") as f:  # Open the file 
            allTheLines = f.readlines()

        for line in allTheLines:
            words = line.split()

            for word in words:
                if "#" in word:  # Skip comments
                    break
                if word == "for":
                    countFor += 1
                elif word == "while":
                    countWhile += 1
                elif word == "if":
                    countIf += 1
                elif word in ["else", "else:"]:  # Handle both 'else' and 'else:'
                    countElse += 1

        # Output the counts
        print(f"fors: {countFor} whiles: {countWhile} ifs: {countIf} elses: {countElse}")

        # Logic check for mismatched if-else statements
        if countElse > countIf:
            print("every else needs an if")

    except FileNotFoundError:
        print("The file does not exist. Please check the filename and try again.")  # confirm if file does not exist 

main()
