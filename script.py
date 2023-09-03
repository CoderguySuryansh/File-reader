def read_file(filename):
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            print("File Contents:")
            print(contents)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Get input from the user
filename = input("Enter the name of the file to read: ")

# Read and display the file contents
read_file(filename)
