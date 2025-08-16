def check_python_syntax(filepath):
    '''
    Reads a Python script from the given filepath and checks its syntax.

    Args:
        filepath (str): The full path to the Python (.py) file.
    '''
    try:
        # Read the entire content of the script using file handling.
        with open(filepath, 'r') as file:
            script_content = file.read()

        # Use the compile() function to validate the syntax.
        # A try-except block is used to catch syntax errors. 
        try:
            compile(script_content, filepath, 'exec')
            # If no errors are found, display a success message. 
            print("\nSuccess! No Syntax Errors Found in '{}'.".format(filepath))
        except SyntaxError as e:
            # If a syntax error is detected, display the error message with the line number. 
            print("\nSyntax Error Found:")
            print("File: '{}'".format(e.filename))
            print("Line: {}".format(e.lineno))
            print("Error: {}".format(e.msg))

    except FileNotFoundError:
        print("\nError: The file '{}' was not found.".format(filepath))
    except Exception as e:
        print("\nAn unexpected error occurred: {}".format(e))

def main():
    '''
    Main function to run the syntax checker tool.
    '''
    # Accept the file path of a Python script from the user. 
    file_path = input("Enter the path of the Python script to check: ")
    check_python_syntax(file_path)

if __name__ == "__main__":
    main()
