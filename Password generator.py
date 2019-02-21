import string
from random import *
characters = string.ascii_letters + string.punctuation  + string.digits
password =  "".join(choice(characters) for x in range(randint(50, 60)))
print (password)
Goodby = input("Thanks your using the best password generator ever")
