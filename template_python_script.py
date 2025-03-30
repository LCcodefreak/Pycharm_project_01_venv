

#!/usr/bin/env python3

"""
This is a template for a Python script with a shebang, the if __name__ == "__main__" block,
and the ability to add directories to the Python module search path.
"""

import sys
from sys import path  # Import path from sys

# Add a directory to the Python module search path.
# Replace '/path/to/your/directory' with the actual path you want to add.
# Example: path.append('/Users/luiscordeiro/MyModules')
path.append('/Users/luiscordeiro/Ambientes_Virtuais/Pycharm_IDE/pycharm_project_1/pycharm_project_1_modules')

def main():
    """
    This is the main function where your script's logic will reside.
    """
    print("Hello from the main function!")

    # Example of using command-line arguments (if needed)
    if len(sys.argv) > 1:
        print(f"You provided these arguments: {sys.argv[1:]}")
    else:
        print("No command-line arguments provided.")

    # Add your code here...
    pass


if __name__ == "__main__":
    """
    This block ensures that the main function is called only when the script is executed directly,
    not when it's imported as a module.
    """
    main()


#Explanation of the Template:

#  1. shebang (#!/usr/bin/env python3):
#  - This line is crucial for making your script executable directly from the command line (e.g., ./script.py).
#  - #! is the shebang.
#  - /usr/bin/env python3 tells the system to use the python3 interpreter found in the user's environment. This is generally preferred over a hardcoded path like /usr/bin/python3 because it's more portable.

#  2. sys.path modifications:
#  - This code snippet is used to add a directory to Python's module search path.
#  - This allows you to import modules from that directory, even if it's not in the standard locations.

#  3. docstring ("""..."""):
#  - The triple-quoted string at the beginning is a docstring. It's good practice to describe what your script does.

#  4. import sys:
#  - This line imports the sys module, which is commonly used for interacting with the system.
#  - It's included here because you'll often want to access command-line arguments (sys.argv) or exit the script with a specific status code (sys.exit()).
#  - You can remove it if you don't need it.

#  5. main() Function:
#  - This is where you'll put the core logic of your script.
#  - It's a good practice to encapsulate your code within a function, especially for larger scripts.
#  - The example shows how to print a message and how to handle command-line arguments.

#  6. if __name__ == "__main__": Block:
#  - This is the most important part of the template > __name__ is a special variable in Python.
#  - When you run a script directly (e.g., python script.py), __name__ is set to "__main__".
#  - When you import a script as a module, __name__ is set to the module's name.
#  - The if __name__ == "__main__": block ensures that the main() function (or any other code within the block) is only executed when the script is run directly, not when it's imported.
#  - This is a good practice because it allows you to reuse your code in other scripts without running the main logic.

#  7. How to Use:
#  - Save: Save this code as a .py file (e.g., my_script.py).
#  - Make Executable: Open your terminal and run: chmod +x my_script.py (This makes the script executable).
#  - Run: You can now run it directly: ./my_script.py or python3 my_script.py
#  - Run with arguments: ./my_script.py arg1 arg2 arg3
#  - Modify: Replace the placeholder comments and the print() statements in the main() function with your actual code.
#  - Import: You can import this script in another script, and the main function will not be executed.