## Video 6 of Object Oriented Programming with Python (https://www.youtube.com/watch?v=xY__sjI5yVU)

import mod # Imports all of the Classes and Functions from the first file (mod.py -> 6_PublicPrivateClasses_mod.py)
from mod import NotPrivate # Imports only the "NotPrivate" class

test = NotPrivate("tim")
test.display()