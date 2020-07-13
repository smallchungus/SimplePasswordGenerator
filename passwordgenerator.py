# Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of
# lowercase letters, uppercase letters, numbers, and symbols.
# The passwords should be random, generating a new password every time the user asks for a new password.
# Include your run-time code in a main method.import random
# Extra:
# Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.
# weak password length, choosing a password

import random


whatyouwant = input("Type 'strong', 'medium' or 'weak' for the strength of the password.")
# weak password length, choosing from a list of words
if whatyouwant == 'weak':
    a = ["monkey", "blue", "microphone", "promise", "honest", "babe", "faraway"]
    print(random.choice(a))
    quit()

# medium password length, having a range of 5
# assign randomly a number 0-3 that corresponds to symbols, uppercase, lowercase, and numbers

if whatyouwant == "medium":
    rplacemedium = [random.randrange(0, 3) for i in range(5)]
    for placeholdermedium in rplacemedium:
        lsymbols = ["!", "@", "#", "$", "%", "^", "&", "*"]
        symbolsaddedmed = [random.choice(lsymbols) if placeholdermedium ==0 else placeholdermedium for placeholdermedium in rplacemedium]
        for symbolsaddedinlist in symbolsaddedmed:
            lnumbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
            numbersaddedmed = [random.choice(lnumbers) if symbolsaddedinlist ==1 else symbolsaddedinlist for symbolsaddedinlist in symbolsaddedmed]
            for numbersaddedinlist in numbersaddedmed:
                luppercase = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T","U", "V", "W", "X", "Y", "Z"]
                uppercaseaddedmed = [random.choice(luppercase) if numbersaddedinlist ==2 else numbersaddedinlist for numbersaddedinlist in numbersaddedmed]
                for uppercaseaddedinlist in uppercaseaddedmed:
                    llowercase = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                                  "u", "v", "w", "x", "y", "z"]
                    lowercaseaddedmed = [random.choice(llowercase) if uppercaseaddedinlist ==3 else uppercaseaddedinlist for uppercaseaddedinlist in uppercaseaddedmed]
                    str(lowercaseaddedmed)
                    print("".join(lowercaseaddedmed))
                    quit()


# strong password length, having a range of 10
if whatyouwant == 'strong':
    rplacelarge = [random.randrange(0, 3) for i in range(10)]
    for placeholderlarge in rplacelarge:
        lsymbolslarge = ["!", "@", "#", "$", "%", "^", "&", "*"]
        symbolsaddedlarge = [random.choice(lsymbolslarge) if placeholderlarge ==0 else placeholderlarge for placeholderlarge in rplacelarge]
        for symbolsaddedinlarge in symbolsaddedlarge:
            lnumberslarge = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
            numbersaddedlarge = [random.choice(lnumberslarge) if symbolsaddedinlarge ==1 else symbolsaddedinlarge for symbolsaddedinlarge in symbolsaddedlarge]
            for numbersaddedinlarge in numbersaddedlarge:
                luppercaselarge = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T","U", "V", "W", "X", "Y", "Z"]
                uppercaseaddedlarge = [random.choice(luppercaselarge) if numbersaddedinlarge ==2 else numbersaddedinlarge for numbersaddedinlarge in numbersaddedlarge]
                for uppercaseaddedinlarge in uppercaseaddedlarge:
                    llowercaselarge = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
                    lowercaseaddedlarge = [random.choice(llowercaselarge) if uppercaseaddedinlarge ==3 else uppercaseaddedinlarge for uppercaseaddedinlarge in uppercaseaddedlarge]
                    str(lowercaseaddedlarge)
                    print ("".join(lowercaseaddedlarge))
                    quit()