## Importing Modules and Namespaces

* Modules help organize code for reusability.
* Namespaces avoid naming conflicts between code parts.
* Importing modules and using namespaces improve code efficiency and maintainability.

## Importing a Module

* Use the `import` keyword followed by the module name.
* Access module functions, variables, and classes with dot notation (`.`).

* Example:
```python
import math
print(math.sin(math.pi / 2))  # Output: 1.0
```

## Importing Specific Functions from a Module

* Import specific functions/variables with `from module import names`.
* Improves code readability and avoids naming conflicts.

* Example:
```python
from math import sin, pi
print(sin(pi / 2))  # Output: 1.0
```

## Importing All Functions from a Module (Caution Advised)

* Use `from module import *` to import all functions.
* **Not recommended** due to potential namespace pollution and conflicts.

* Example (Not recommended):
```python
from math import *
print(sin(pi / 2))  # Output: 1.0 (but may cause issues with other modules)
```

## Using an Alias for a Module

* Use an alias for a module name with `import module as alias`.
* Helpful for long module names or avoiding conflicts.

* Example:
```python
import math as math_functions
print(math_functions.sin(math_functions.pi / 2))  # Output: 1.0
```

## Renaming Functions When Importing

* Rename functions/variables with `from module import name as alias`.
* Useful to avoid conflicts with existing names in your code.

* Example:
```python
from math import pi as PI, sin as sine
print(sine(PI / 2))  # Output: 1.0
```

## Python Module Index

https://docs.python.org/3/py-modindex.html

## How to Write Your Own Module

* **Modules:** Individual Python files containing functions, classes, or variables.

* **Creating a module:** Simply create a Python file (usually with a `.py` extension) and define the functionality you want to encapsulate within that file.

```python
# my_functions.py
def greet(name):
    print(f"Hello, {name}!")

# main.py
from my_functions import greet
greet("Alice")
```

## Conditional Imports with `__name__`

* **`__name__`:** Special variable that holds the name of the current module.
* **Conditional execution:** Use `if __name__ == "__main__":` to check if the module is being run directly or imported. This allows for code to behave differently depending on the context.  For example, you might want to include some test code within a module that only executes when the module is run directly, not when imported by another script.

```python
# my_functions.py
def my_function():
  print(f"Running my_function from {__name__}")

if __name__ == "__main__":
  # Code to be executed only when the module is run directly
  print("Running the module directly")
  my_function()

# main.py
from my_functions import my_function

print("Running the module in main script")
my_function()
```

## What are Python Packages?

* **Reusable and manageable code components:** Organize your code into logical units that can be easily reused across different parts of your project.
* **Organized using directories (packages) and modules (.py files):** Packages are directories that contain related Python modules. Modules are individual Python files containing functions, classes, or variables. This structure promotes better code organization and maintainability.
* **Improve code structure, maintainability, and avoid naming conflicts:** By using packages, you can keep your code well-organized, easier to understand, and less prone to naming conflicts as your project grows.

## How to Write Your Own Module in a Package

* **Packages:** Collections of related modules organized within a directory structure.
* **__init__.py:** An empty file within a package directory that tells Python it's a package (can be optional but recommended). This file can also be used to initialize the package or contain configuration options.
* **Creating a package:** Create a directory for your package and place your Python module files inside that directory. Include an empty `__init__.py` file within the package directory.

```
├── my_package/  # Create a directory for your package
│   ├── __init__.py  # Empty file to mark the directory as a package
│   └── my_functions.py  # Your module file goes here
└── main.py  # Usage your module
```

```python
# my_functions.py (inside my_package directory)
def calculate_area(length, width):
  return length * width

# main.py (assuming the package is in the same directory)
from my_package.my_functions import calculate_area
area = calculate_area(5, 3)
print(f"Area of rectangle: {area}")
```

## Importing Modules from Relative Paths

* **`sys.path.append`:** Method to add custom module directories to the search path. This can be useful when your project has a specific directory structure for organizing your code.
* **Relative imports:** Useful for organizing code within a project structure and avoiding circular imports. You can specify relative paths to modules within your package structure instead of relying on Python's default search path.

```python
# main.py

import sys
sys.path.append('./modules')  # Add the modules directory to the search path

from my_package.my_functions import my_function

# Use the imported function
my_function()
```

By using these concepts, you can create well-structured, maintainable, and reusable code in Python.

## Python Package Installer (PIP)

* Manages software packages for Python
* PyPI (Python Package Index) a centralized repository of all available software packages for Python: https://pypi.org/
* Accessible through `pip`

## Verifying PIP installation

* Open command prompt (Windows) or terminal (Mac/Linux)
* Type: `pip --version`
* This will display the installed pip version

```commandline
PS C:\Users\aniap\PycharmProjects\python-lectures> pip --version
pip 24.0 from C:\Users\lukaszp\AppData\Local\Programs\Python\Python312\Lib\site-packages\pip (python 3.12)

```

## PIP functionalities

* `pip help <operation>` - Provides brief description of pip operations
* `pip list` - Lists currently installed packages
* `pip show <package_name>` - Shows information about a specific package, including dependencies
* Searches PyPI for packages containing the specified string: https://pypi.org/search/

```commandline
pip help install
pip show pygame
```

## Package Installation

* `pip install <package_name>` - Installs a package system-wide (requires administrative rights)
* `pip install --user <package_name>` - Installs a package for the current user only

Pygame is a popular library for creating games in Python

```commandline
pip install pygame
```

```commandline
PS C:\Users\lukaszp\PycharmProjects\python-lectures> pip install pygame
Collecting pygame
  Downloading pygame-2.5.2-cp312-cp312-win_amd64.whl.metadata (13 kB)
Downloading pygame-2.5.2-cp312-cp312-win_amd64.whl (10.8 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 10.8/10.8 MB 17.7 MB/s eta 0:00:00
Installing collected packages: pygame
Successfully installed pygame-2.5.2
```

**Example: Using Pygame**

```python
import pygame

run = True
width = 400
height = 100
pygame.init()
screen = pygame.display.set_mode((width, height))
font = pygame.font.SysFont(None, 48)
text = font.render("Welcome to pygame", True, (255, 255, 255))
screen.blit(text, ((width - text.get_width()) // 2, (height - text.get_height()) // 2))
pygame.display.flip()
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT \
                or event.type == pygame.MOUSEBUTTONUP \
                or event.type == pygame.KEYUP:
            run = False
pygame.quit()
```

## Package Updates and Uninstallation

* `pip install -U <package_name>` - Updates a previously installed package
* `pip uninstall <package_name>` - Uninstalls a previously installed package

```commandline
pip install -U pygame
pip uninstall pygame
```

## Installing Specific Versions

* `pip install <package_name>==<version_number>` - Installs a specific version of a package

```commandline
pip install pygame==2.2.3
```

## PIP Summary

* PIP is a powerful tool for managing Python packages
* Use PIP to install, update, and uninstall packages
* PIP simplifies the process of working with external libraries in Python projects