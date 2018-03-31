print("""
=======================================|
   Welcome to the TwitchScript Maker!  |
   Input the file you want converted.  |
=======================================|
""")
inputfile = open(input(), 'r')
print("""
========================================
What to call the output file? (No Ext.)
========================================
""")
outputfile = open((input() +".twitch"), 'w')
for line in inputfile.readlines():
    editedline = line.replace("="," Squid3 ")
    editedline = editedline.replace(".", " BigBrother ")
    editedline = editedline.replace(",", " TheIlluminati ")
    editedline = editedline.replace(";", " MorphinTime ")
    editedline = editedline.replace("'", " CurseLit ")
    editedline = editedline.replace('"', " TwitchLit ")
    editedline = editedline.replace("(", " GivePLZ ")
    editedline = editedline.replace(")", " TakeNRG ")
    editedline = editedline.replace(">", " Squid4 ")
    editedline = editedline.replace("<", " DoritosChip ")
    editedline = editedline.replace("const", " PogChamp ")
    editedline = editedline.replace("express", " DansGame ")
    editedline = editedline.replace("app", " Kappa ")
    editedline = editedline.replace("get", " HotPokket ")
    editedline = editedline.replace("require", " Mau5 ")
    editedline = editedline.replace("req", " OPFrog ")
    editedline = editedline.replace("res", " OhMyDog ")
    editedline = editedline.replace("listen", " HeyGuys ")
    editedline = editedline.replace("send", " KappaPride ")
    editedline = editedline.replace("console", " MrDestructoid ")
    outputfile.write(editedline + '\n')
inputfile.close()
outputfile.close()
