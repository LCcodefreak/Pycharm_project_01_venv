#!/usr/bin/env python3

"""
Shebang Line Explanation:

The shebang line `#!/usr/bin/env python3` is a special directive used in Unix-like operating systems (including macOS and Linux) to specify the interpreter for executing a script.

Simplified Breakdown:

-   `#!`:  This is the "shebang" - a special character sequence that tells the system that the rest of the line specifies an interpreter.
-   `/usr/bin/env`: This is a program called `env` that is typically found in the `/usr/bin` directory. The `env` program's job is to find and run another program based on the user's environment.
-   `python3`: This is the name of the interpreter we want to use. `env` will search the user's `PATH` environment variable to find the location of the `python3` executable.

In essence, this line says: "Use the `python3` interpreter (wherever it's located in the user's environment) to execute this script."

Why use `/usr/bin/env python3` instead of a direct path like `/usr/bin/python3`?

-   **Portability:** The location of the `python3` interpreter can vary from system to system. Using `env` makes the script more portable because it relies on the user's environment to find the correct `python3`.
-   **Virtual Environments:** When you're working with virtual environments, `env` will automatically find the `python3` interpreter within the active virtual environment.

In summary, the shebang line makes the script directly executable and ensures that the correct Python 3 interpreter is used, regardless of its specific location on the system.
"""

import sys
from sys import path  # Import path from sys

"""
This is a template for a Python script with a shebang, the if __name__ == "__main__" block,
and the ability to add directories to the Python module search path.
"""

# 01.
# sys.path.append(''):
# Add a directory to the Python module search path.
# Example: path.append('/path/to/your/directory')
# Replace '/path/to/your/directory' with the actual path you want to add:
path.append('/Users/luiscordeiro/Ambientes_Virtuais/Pycharm_IDE/pycharm_project_1/pycharm_project_1_modules')

# 02.
# main function invoked only when the file runs as a script ( not when it's imported as a module) :
def main():
    """
    This is the main function where your script's logic will reside.
    """
    # 02.1
    print("Hello from the main function!")

    # 02.2
    # Command Line Arguments
    # The script template_python_script.py must be executable.
    # Open a terminal and use the command > to make the script executable:
    # $ chmod +x my_script.py
    # $ ./my_script.py arg1 arg2 arg3
    # This will output "You provided these arguments: ['arg1', 'arg2', 'arg3']"
    if len(sys.argv) > 1:
        print(f"You provided these arguments: {sys.argv[1:]}")
    else:
        print("No command-line arguments provided.")

    # Add your code here to use this as a script with arguments

    pass

#----------------------------------------------------------------------------------------------------------------------#

# 03.
# condition that activates the main function when the script is executed directly:
if __name__ == "__main__":
    """
    This block ensures that the main function is called only when the script is executed directly,
    not when it's imported as a module.
    """
    # 03.1
    # Call the "main" function:
    main()


#----------------------------------------------------------------------------------------------------------------------#
#NOTES :

# A. Gemini Code Assistant:
# shortcut - command + \ and it opens "Gemini Code Assist Quick Pick menu"
# /generate tag to use Gemini

# B. Explanation of the Template:

# B.1. shebang (#!/usr/bin/env python3):
# - This line is crucial for making your script executable directly from the command line (e.g., ./script.py).
# - #! is the shebang.
# - /usr/bin/env python3 tells the system to use the python3 interpreter found in the user's environment. This is generally preferred over a hardcoded path like /usr/bin/python3 because it's more portable.

# B.2. sys.path modifications:
# - This code snippet is used to add a directory to Python's module search path.
# - This allows you to import modules from that directory, even if it's not in the standard locations.

# B.3. docstring ("""..."""):
# - The triple-quoted string at the beginning is a docstring. It's good practice to describe what your script does.

# B.4. import sys:
# - This line imports the sys module, which is commonly used for interacting with the system.
# - It's included here because you'll often want to access command-line arguments (sys.argv) or exit the script with a specific status code (sys.exit()).
# - You can remove it if you don't need it.

# B.5. main() Function:
# - This is where you'll put the core logic of your script.
# - It's a good practice to encapsulate your code within a function, especially for larger scripts.
# - The example shows how to print a message and how to handle command-line arguments.

# B.6. if __name__ == "__main__": Block:
# - This is the most important part of the template > __name__ is a special variable in Python.
# - When you run a script directly (e.g., python script.py), __name__ is set to "__main__".
# - When you import a script as a module, __name__ is set to the module's name.
# - The if __name__ == "__main__": block ensures that the "main()" function (or any other code within the block) is only executed when the script is run directly, not when it's imported.
# - This is a good practice because it allows you to reuse your code in other scripts without running the main logic.

# B.7. How to Use:
# - Save: Save this code as a .py file (e.g., my_script.py).
# - Make Executable: Open your terminal and run: chmod +x my_script.py (This makes the script executable).
# - Run: You can now run it directly: ./my_script.py or python3 my_script.py
# - Run with arguments: ./my_script.py arg1 arg2 arg3
# - Modify: Replace the placeholder comments and the print() statements in the main() function with your actual code.
# - Import: You can import this script in another script, and the main function will not be executed.