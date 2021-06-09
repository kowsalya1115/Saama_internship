from spellchecker import SpellChecker
spell = SpellChecker()
sentence=input("Enter the sentence :")
sentence_val=sentence.split()
print(sentence_val)
misspelled = spell.unknown(sentence_val)
for word in misspelled:
    print(spell.correction(word))
    print(spell.candidates(word))
