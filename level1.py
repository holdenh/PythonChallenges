import string

# take the given string
sourceString = '''g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'''
alphabet = 'abcdefghijklmnopqrstuvwxyz'
specials = ["'", " ", "(", ")", "."]
#hints given
# K->M
# O->Q
# E->G
# need to shift all letters left two spots.
outputstring = ''
for char in sourceString :
    if char in specials :
        outputstring +=(char)
        continue
    #do the shift.
    newLocation = alphabet.index(char) + 2
    #check if new location needs to be wrapped to beginning.
    if newLocation > len(alphabet)-1 :
        rollback = newLocation - (len(alphabet)-1) - 1
        outputstring +=(alphabet[rollback])
    else :
        outputstring +=(alphabet[newLocation])
#print the final output.
print(outputstring)
