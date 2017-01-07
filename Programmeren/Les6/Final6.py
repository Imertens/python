def onversleuteld(invoerstring):
    versleuteld = ''
    for char in invoerstring:
        versleuteld = versleuteld + chr(ord(char)+3)
    return versleuteld



invoer = input('Voer je naam, het begin station en het eindstation in:')
print(onversleuteld(invoer))



