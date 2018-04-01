print("""
===========================================
  Welcome to the TwitchScript Transpiler!
  =======================================
Type in the .twitch file you'd like to run.
===========================================
""")
inputfile = open(input(), 'r')
print("""
===========================================
  Where would you like to save this file?
         (include a .js extension!)
===========================================
""")
outputfile = open(input(), 'w+')

for line in inputfile.readlines():
    editedline = line.replace(" Squid3 ", "=")
    editedline = editedline.replace(" BigBrother ",".")
    editedline = editedline.replace(" TheIlluminati ",",")
    editedline = editedline.replace(" MorphinTime ",";")
    editedline = editedline.replace(" CurseLit ","'")
    editedline = editedline.replace(" TwitchLit ",'"')
    editedline = editedline.replace(" GivePLZ ","(")
    editedline = editedline.replace(" TakeNRG ",")")
    editedline = editedline.replace(" Squid4 ",">")
    editedline = editedline.replace(" DoritosChip ", "<")
    editedline = editedline.replace(" PogChamp ", "const")
    editedline = editedline.replace(" DansGame ", "express")
    editedline = editedline.replace(" Kappa ", "app")
    editedline = editedline.replace(" HotPokket ", "get")
    editedline = editedline.replace(" Mau5 ", "require")
    editedline = editedline.replace(" OPFrog ", "req")
    editedline = editedline.replace(" OhMyDog ", "res")
    editedline = editedline.replace(" HeyGuys ", "listen")
    editedline = editedline.replace(" KappaPride ", "send")
    editedline = editedline.replace(" MrDestructoid", "console")
    outputfile.write(editedline + '\n')
inputfile.close()
outputfile.close()
