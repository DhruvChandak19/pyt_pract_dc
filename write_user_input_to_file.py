# Program to write multiple user input lines to a file

with open("output.txt", "w") as f:
    while True:
        line = input("Enter text (type 'stop' to end): ")
        
        if line.lower() == "stop":
            break
        
        f.write(line + "\n")

print("Data written successfully to output.txt")
