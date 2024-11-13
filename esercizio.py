nome_città = input("Inserisci il nome della tua città d'origine ")
nome_animale = input("Inserisci il nome tuo animale domestico ")
nome_band = nome_città + nome_animale
if nome_città == "Bastardo": # provincia di Perugia
    print(f"Forse dovresti lasciar stare...")
elif nome_animale == "Assassino":
    print(f"Ma che nome è?!")
else:
    print(f"Il nome della band potrebbe essere : {nome_band}")