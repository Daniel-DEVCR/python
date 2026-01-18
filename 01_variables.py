# Variables

'''

my_strvar = 'My String variable 1.0'
print(my_strvar)

my_intvar = 5
print(my_intvar)

my_boolvar = True
print(my_boolvar)

#Concatenación de variables en un print
print(my_boolvar, my_intvar, my_strvar)
print("Este es el valor de:", my_boolvar)


# Function usage str() len()

my_intvar = 5
print(my_intvar)
print(type(my_intvar))

int_to_spr_var = str(my_intvar)
print(int_to_spr_var)
print(type(int_to_spr_var))

print(len(my_strvar))

# Variables en una sola line (no deberia usarse asi)

name, surname, alias, age = "Daniel", "Fernandez", "Dani", 26

print("me llamo", name, surname, "tengo", age, "y mi alias es", alias)


# Variables with input

first_name = input('What is your name?')
age = input('How old are you?')

print(first_name)
print(age)


# Python es flexible por que lee la ultima var definida, no en compilacion, cambia el tipo y valor


name, surname, alias, age = "Daniel", "Fernandez", "Dani", 26

print("me llamo", name, surname, "tengo", age, "y mi alias es", alias)

name = 26
age = 'Daniel'
print(name, age)
# Python printeara las variables name y age como ultima vez definidas (name: 26, age: Daniel)
# A pesar de que ya habian sido definidas antes 

'''

address: str = 'mi direccion'
address = 32
print(type(address))

# A pesar de que definimos address como str, pasa a ser un int por su ultima definicion


