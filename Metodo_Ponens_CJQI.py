premisa_1 = True  # Si está lloviendo (A), entonces llevaré un paraguas (B)
usuario = input("Esta lloviendo?(Y/N): ")
if usuario == "Y":
    premisa_2 = True  # Está lloviendo (A)
if usuario == "N":
    premisa_2 = False

if premisa_1 and premisa_2:
    llevar_paraguas = True  # Conclusión: Llevaré un paraguas (B)
    print("Deberias de llevar un paraguas")
else:
    llevar_paraguas = False  # Conclusión: No llevaré un paraguas (B)
    print("No te lleves el paraguas, solo lo vas a estar cargando")