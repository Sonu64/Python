# import recipes.flavors

# print(f"Printing flavor: {recipes.flavors.masalaChai()}")

# Avoid importing everything from a package 
# from recipes import *
# from utils import *

"""
The core difference between 'import moduleName' and 'from moduleName import *'is what gets added 
to your current namespace.

import math imports the entire math module as a single object named math. 
You must prefix all module functions with math.(e.g., math.sqrt(25)).
from math import * imports all public names (functions, variables, etc.) from the math module 
directly into your current namespace. You can then use them without a prefix (e.g., sqrt(25)).
"""

from recipes.flavors import masalaChai, gingerChai
print(f"Printing flavor: {masalaChai()}")
print(f"Printing new flavor: {gingerChai()}")