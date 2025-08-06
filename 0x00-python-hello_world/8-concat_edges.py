#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
<<<<<<< HEAD
 language that combines remarkable power with very clear syntax"
str = str[39:66] + str[-23:-17] + str[:6]
print(str)
=======
    language that combines power with very clear syntax"
str = "object oriented programming"
print(str)
>>>>>>> de9e906 (update from ubuntu)
