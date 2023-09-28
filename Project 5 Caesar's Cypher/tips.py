# Create a dictionary with the index starting from 0 for a and 25 for z. 
#? Functions like chr() which converts a number into a letter a==97, b==98 ... and ord() which converts a letter into number 97==a

# define a function encrypt which will accept two arguments text and cypher where text i a string with the text to encrypt and cypher is the number by which amount to shift the letters

# inside the function it is advisbale to convert all letters to lowercase

# initalize a variable result which will hold the encrypted result

# for each symbol in text if it is not a letter add it directly to result otherwise shift the index by amount specified in cypher and the add it to result
# You may need to use the modulo operator since it shouldn't be possible to get an index larger than 25 

#do the same for for decryption so define a function decrypt which will do everything the same and the only difference should be that it should subtract the amount which 
# is specified in cypher instead of adding it.

# Test your functions with some sample text and number