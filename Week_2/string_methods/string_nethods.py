#This file shows some string method implementations
#Return a copy of the string with its first character capitalized and the rest lowercased.
demo_sentence = "steve is     a data     scientist"
capitaliz = demo_sentence.capitalize()
print(capitaliz)
#Return a casefolded copy of the string. Casefolded strings may be used for caseless matching. in other words it turns them to lower case
casefold_word = demo_sentence.casefold()
print(casefold_word)
#Return a copy of the string with all the cased characters 4 converted to uppercase.
uppercase_sentence = demo_sentence.upper()
print(uppercase_sentence)
#Return a titlecased version of the string where words start with 
#an uppercase character and the remaining characters are lowercase.
title_sentence = demo_sentence.title()
print(title_sentence)
#Return a copy of the string with uppercase characters converted to lowercase and vice versa
swapcase_sentence = demo_sentence.swapcase()
print(swapcase_sentence)
#Return a copy of the string with the leading and trailing characters removed. In this case we strip white spaces
strip_sentence = demo_sentence.strip(" ")
print(strip_sentence)
#split
split_sentence = demo_sentence.split()
print(split_sentence)
new_str = "The cow jumped over the moon."
new_str.split()
