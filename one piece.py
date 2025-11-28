# Characters
dict_characters = {1: {"name": "Luffy", "category": 1, "weapons": [1, 1], "strength": 6, "speed":
    7, "experience": 0},
                   2: {"name": "Zoro", "category": 1, "weapons": [4], "strength": 5, "speed": 6, "experience":
                       0},
                   3: {"name": "Sanji", "category": 1, "weapons": [1, 3], "strength": 4, "speed":
                       6, "experience": 0},
                   4: {"name": "Buggy", "category": 2, "weapons": [3], "strength": 2, "speed": 4,
                       "experience": 0},
                   5: {"name": "Mr3", "category": 2, "weapons": [5], "strength": 3, "speed": 2, "experience"
                   : 0},
                   6: {"name": "Xebec", "category": 3, "weapons": [1, 3], "strength": 6, "speed": 5,
                       "experience": 0},
                   7: {"name": "Kaido", "category": 3, "weapons": [4], "strength": 8, "speed": 3,
                       "experience": 0},
                   8: {"name": "Mama grande", "category": 3, "weapons": [5], "strength": 7, "speed": 1,
                       "experience": 0},
                   9: {"name": "Akainu", "category": 4, "weapons": [2], "strength": 6, "speed": 4,
                       "experience": 0},
                   10: {"name": "Kizaru", "category": 4, "weapons": [1, 3], "strength": 5, "speed": 8,
                        "experience": 0},
                   11: {"name": "Fujitora", "category": 4, "weapons": [5], "strength": 5, "speed": 4,
                        "experience": 0},
                   12: {"name": "Garp", "category": 5, "weapons": [2], "strength": 6, "speed": 3,
                        "experience": 0},
                   13: {"name": "Smoker", "category": 5, "weapons": [5], "strength": 5, "speed": 5,
                        "experience": 0},
                   14: {"name": "Koby", "category": 6, "weapons": [4], "strength": 3, "speed": 4,
                        "experience": 0},
                   15: {"name": "Tashigi", "category": 6, "weapons": [3], "strength": 4, "speed": 4,
                        "experience": 0},
                   }
# Weapons
dict_weapons = {1: {"name": "Sword", "strength": 3, "speed": 5, "two_hand": False},
                2: {"name": "Greatsword", "strength": 5, "speed": 3, "two_hand": True},
                3: {"name": "Gun", "strength": 2, "speed": 6, "two_hand": False},
                4: {"name": "Rifle", "strength": 3, "speed": 4, "two_hand": True},
                5: {"name": "Chuchi", "strength": 4, "speed": 4, "two_hand": True},
                }
# Crews
dict_crews = {1: {"name": "Straw hat", "members": [8, 6]},
              2: {"name": "Pirates Buggy", "members": [1, 3, 5]},
              3: {"name": "Pirates Rocks", "members": [2, 4, 7, ]}
              }
# Ranks
dict_ranks = {1: {"name": "Admiral", "members": [9, 10, 11]},
              2: {"name": "ViceAdmiral", "members": [12, 13]},
              3: {"name": "Lieutenant", "members": [14, 15]}
              }
dict_categorys = {1: "Straw hat", 2: "Pirates Buggy", 3: "Pirates Rocks", 4: "Admiral", 5: "ViceAdmiral",
                  6: "Lieutenant"}

# Menus
menu = "Menu 0 (One Piece)".center(40,
                                   "=") + "\n\n" + "1)Play" + "\n" + "2)Create" + "\n" + "3)Edit" + "\n" + "4)List" + "\n" + "5)Exit" + "\n"
menu1 = "Not Implemented".center(40, "=") + "\n" + "1)Go back"
menu2 = "Menu 02 Create".center(40,
                                "=") + "\n\n" + "1) Crete Character" + "\n" + "2) Create  Weapon" + "\n" + "3) Go back"
menu3 = "Menu 03 (Edit Menu) ".center(40,
                                      "=") + "\n\n" + "1)Edit character" + "\n" + "2)Edit weapon" + "\n" + "3)Go back"
menu31 = "Menu 031 (Select Character to Edit) ".center(60, "=") + "\n\n"
menu32 = "Menu 032 (Select Weapon to Edit) ".center(60, "=") + "\n\n"
menu31X = "Menu 031X (Character Feature to Edit) ".center(60,
                                                          "=") + "\n\n" + "1)Name" + "\n" + "2)Weapon" + "\n" + "3)Go back"
menu32X = "Menu 032X (Weapon Feature to Edit) ".center(60,
                                                       "=") + "\n\n" + "1)Name" + "\n" + "2)Plus Strength" + "\n" + "3)Plus speed" + "\n" + "4)Go back"
menu4 = "Menu 04 (List)".center(40,
                                "=") + "\n\n" + "1)List characters" + "\n" + "2)List weapons" + "\n" + "3)List side" + "\n" + "4)List range" + "\n" + "5)Go back"
menu41 = "Menu 041 (List Character)".center(40,
                                            "=") + "\n\n" + "1)List by ID" + "\n" + "2)List by name" + "\n" + "3)List Strangth" + "\n" + "4)List by speed" + "\n" + "5)Go back"
menu42 = "Menu 042 (List Weapons)".center(40,
                                          "=") + "\n\n" + "1)List by ID" + "\n" + "2)List by name" + "\n" + "3)List Strangth" + "\n" + "4)List by speed" + "\n" + "5)Go back"

# Cositas tipo menu
cabecerachid = "Characters ordered by Id".center(60, "=")
cabecerachn = "Characters ordered by Name".center(60, "=")
cabecerachs = "Characters ordered by Strength".center(60, "=")
cabecerachspe = "Characters ordered by Speed".center(60, "=")
cabecerach = "\n{:<10}{:<17}{:<13}{:<10}{:<10}".format("Id", "name", "strength", "speed", "experience")
cabecerawpid = "Weapon ordered by Id".center(60, "=")
cabecerawp = "\n{:<10}{:<17}{:<13}{:<12}{:}".format("Id", "name", "strength", "speed", "two hand")
cabecerawpn = "Weapon ordered by Name".center(60, "=")
cabecerawps = "Weapon ordered by Strength".center(60, "=")
cabeceracwppe = "Weapon ordered by Speed".center(60, "=")

# VARIABLES DE CREACION DE PERSONAJE
new_character = {}
new_nombre = ""
datos_character = ""

# FLAGS
flg_00 = True
flg_01 = False
flg_02 = False
flg_021 = False
flg_022 = False
flg_03 = False
flg_031 = False
flg_032 = False
flg_031X = False
flg_032X = False
flg_04 = False
flg_041 = False
flg_042 = False
flg_043 = False
flg_044 = False
flg_05 = False
salir = False
# CODIGOOOO
while not salir:
    while flg_00:
        print(menu)
        opc = input("->Option: ")
        if not opc.isdigit():
            print("Opcion no numerica")
            input("Enter to continue")
        elif not (int(opc) in range(1, 6)):
            print("opcion numerica no valida")
            input("Enter to continue")
        else:
            opc = int(opc)
            if opc == 1:
                flg_00 = False
                flg_01 = True
            elif opc == 2:
                flg_00 = False
                flg_02 = True
            elif opc == 3:
                flg_00 = False
                flg_03 = True
            elif opc == 4:
                flg_00 = False
                flg_04 = True
            elif opc == 5:
                flg_00 = False
                salir = True
        # menu01 Finish
        while flg_01:
            print(menu1)
            opc = input("->Option: ")
            if not opc.isdigit():
                print("Opcion no numerica")
                input("Enter to continue")
            elif not (int(opc) in range(1, 2)):
                print("opcion numerica no valida")
                input("Enter to continue")
            else:
                opc = int(opc)
                if opc == 1:
                    flg_00 = True
                    flg_01 = False

        # menu02
        while flg_02:
            print(menu2)
            opc = input("->Option: ")
            if not opc.isdigit():
                print("Opcion no numerica")
                input("Enter to continue")
            elif not (int(opc) in range(1, 4)):
                print("opcion numerica no valida")
                input("Enter to continue")
            else:
                opc = int(opc)
                # CREACION DE PERSONAJE
                if opc == 1:

                    flg_02 = False
                    flg_021 = True
                    new_id = len(dict_characters)
                    new_nombre = input("Name of the new character")
                    while new_nombre == "":
                        print("The option is empty")
                        new_nombre = input("Name of the new character")

                    # MINI MENU DE ELECCION DE CREW
                    crew_choice = "Side of the new character" + "\n" + "1)Marine" + "\n" + "2)Pirate"
                    crew_option = input("-> Option:")
                    if not crew_option.isdigit():
                        print("Opcion no numerica")
                        input("Enter to continue")
                    elif not (int(crew_option) in range(1, 3)):
                        print("opcion numerica no valida")
                        input("Enter to continue")


                    else:
                        crew_option = int(crew_option)
                        if crew_option == 1:
                            # Marine y escoger el rango del miembro
                            print("Ahora lo quito")
                            print(
                                "Range or crew of the new character" + "\n" + "1) Admiral" + "\n" + "2)ViceAdmiral" + "\n" + "3) Lieutenant")

                        elif crew_option == 2:
                            # Pirata y escoger el equipo
                            print("Ahora lo quito")
                elif opc == 2:
                    flg_02 = False
                    flg_021 = True




                # BACK
                elif opc == 3:
                    flg_00 = True
                    flg_02 = False
        # menu03
        while flg_03:
            print(menu3)
            opc = input("->Option: ")
            if not opc.isdigit():
                print("Opcion no numerica")
                input("Enter to continue")
            elif not (int(opc) in range(1, 4)):
                print("opcion numerica no valida")
                input("Enter to continue")
            else:
                opc = int(opc)
                if opc == 1:
                    flg_03 = False
                    flg_031 = True
                    while flg_031:
                        print(menu31)
                        lista_ids = list(dict_characters.keys())
                        for pasada in range(len(lista_ids)):
                            for i in range(len(lista_ids) - 1 - pasada):
                                if lista_ids[i] > lista_ids[i + 1]:
                                    aux = lista_ids[i]
                                    lista_ids[i] = lista_ids[i + 1]
                                    lista_ids[i + 1] = aux
                        datos = ""
                        for id in lista_ids:
                            datos = datos + "ID: {},Name: {},Catergory: {},Weapon: {},Strength: {},Speed: {},Experience: {}".format(
                                id, dict_characters[id]["name"], dict_characters[id]["category"],
                                dict_characters[id]["weapons"], dict_characters[id]["strength"],
                                dict_characters[id]["speed"], dict_characters[id]["speed"],
                                dict_characters[id]["experience"]) + "\n"
                        print(datos)
                        id_editar_character = input("ID Weapon to edit\n")
                        if not id_editar_character.isdigit():
                            print("Invalid Option".center(50, "="))
                            input("Enter to continue")
                        elif not int(id_editar_character) in range(1, len(dict_characters) + 1):
                            print("Invalid Option".center(50, "="))
                            input("Enter to continue")
                        else:
                            id_editar_character = int(id_editar_character)
                            opc = int(opc)
                            flg_031 = False
                            flg_031X = True
                            persona_edit = dict_characters[id_editar_character]
                            while flg_031X:
                                print(menu31X)
                                opc = input("->Option: ")
                                if not opc.isdigit():
                                    print("Opcion no numerica")
                                    input("Enter to continue")
                                elif not (int(opc) in range(1, 4)):
                                    print("opcion numerica no valida")
                                    input("Enter to continue")
                                else:
                                    opc = int(opc)
                                    if opc == 1:
                                        cambiarnombrecharacter=input("Enter the new name:\n")
                                        cambiarnombrecharacterres=input("Do you want to change name {} by {} Y/N?".format(persona_edit["name"],cambiarnombrecharacter))
                                        if cambiarnombrecharacterres == "Y"or"y":
                                            persona_edit ["name"] = cambiarnombrecharacter.title()
                                            print("Saved")
                                        elif cambiarnombrecharacterres == "N"or"n":
                                            print("Not Saved")
                                        else:
                                            flg_031X = False
                                            flg_03 = True
                                    elif opc == 2:
                                        print("Weapon")
                                    elif opc == 3:
                                        flg_00 = True
                                        flg_031X = False
                elif opc == 2:
                    flg_03 = False
                    flg_032 = True
                    while flg_032:
                        print(menu32)
                        lista_ids = list(dict_weapons.keys())
                        for pasada in range(len(lista_ids)):
                            for i in range(len(lista_ids) - 1 - pasada):
                                if lista_ids[i] > lista_ids[i + 1]:
                                    aux = lista_ids[i]
                                    lista_ids[i] = lista_ids[i + 1]
                                    lista_ids[i + 1] = aux
                        datos = ""
                        for id in lista_ids:
                            datos = datos + "{}) {}, Strength: {}, Speed {}".format(id,
                                                                                    dict_weapons[id][
                                                                                        "name"],
                                                                                    dict_weapons[id][
                                                                                        "strength"],
                                                                                    dict_weapons[id][
                                                                                        "speed"]) + "\n"
                        print(datos)

                        id_editar_weapon = input("ID Weapon to edit\n")
                        if not id_editar_weapon.isdigit():
                            print("Invalid Option".center(50, "="))
                            input("Enter to continue")
                        elif not int(id_editar_weapon) in range(1, len(dict_weapons) + 1):
                            print("Invalid Option".center(50, "="))
                            input("Enter to continue")
                        else:
                            id_editar_weapon = int(id_editar_weapon)
                            opc = int(opc)
                            flg_032 = False
                            flg_032X = True
                            arma_edit = dict_weapons[id_editar_weapon]
                            while flg_032X:
                                print(menu32X)
                                print("Select feature to edit to weapon ID: {}, Name: {}".format(id_editar_weapon,arma_edit["name"]))
                                opc = input("->Option: ")
                                if not opc.isdigit():
                                    print("Opcion no numerica")
                                    input("Enter to continue")
                                elif not (int(opc) in range(1, 5)):
                                    print("opcion numerica no valida")
                                    input("Enter to continue")
                                else:
                                    opc = int(opc)
                                    if opc == 1:
                                        cambiarnombreweapon=input("Enter the new name:\n")
                                        cambiarnombreweaponres=input("Do you want to change name {} by {} Y/N?".format(arma_edit["name"],cambiarnombreweapon))
                                        if cambiarnombreweaponres == "Y"or"y":
                                            arma_edit ["name"] = cambiarnombreweapon.title()
                                            print("Saved")
                                        elif cambiarnombreweaponres == "N"or"n":
                                            print("Not Saved")
                                        else:
                                            flg_032X = False
                                            flg_03 = True




                                    elif opc == 2:
                                        cambiarfuerzaweapon=input("Enter the new Strength:\n")
                                        cambiarfuerzaweaponres=input("Do you want to change Strength {} by {} Y/N?".format(arma_edit["strength"],cambiarfuerzaweapon))
                                        if cambiarfuerzaweaponres == "Y"or"y":
                                            arma_edit ["strength"] = cambiarfuerzaweapon
                                            arma_edit["strength"] = int(arma_edit ["strength"] )
                                            print("Saved")
                                        elif cambiarfuerzaweaponres == "N"or"n":
                                            print("Not Saved")
                                        else:
                                            flg_032X = False
                                            flg_03 = True
                                    elif opc == 3:
                                        cambiarspeedweapon=input("Enter the new Strength:\n")
                                        cambiarspeedweaponres=input("Do you want to change Strength {} by {} Y/N?".format(arma_edit["speed"],cambiarspeedweapon))
                                        if cambiarspeedweaponres == "Y"or"y":
                                            arma_edit ["speed"] = cambiarspeedweapon
                                            arma_edit["speed"] = int(arma_edit ["speed"] )
                                            print("Saved")
                                        elif cambiarspeedweaponres == "N"or"n":
                                            print("Not Saved")
                                        else:
                                            flg_032X = False
                                            flg_03 = True
                                    elif opc == 4:
                                        flg_03 = True
                                        flg_032X = False


                elif opc == 3:
                    flg_00 = True
                    flg_03 = False

        # menu04 finish
        while flg_04:
            print(menu4)
            opc = input("->Option: ")
            if not opc.isdigit():
                print("Opcion no numerica")
                input("Enter to continue")
            elif not (int(opc) in range(1, 6)):
                print("opcion numerica no valida")
                input("Enter to continue")
            else:
                opc = int(opc)
                if opc == 1:
                    flg_04 = False
                    flg_041 = True
                    while flg_041:
                        print(menu41)
                        opc = input("->Option: ")
                        if not opc.isdigit():
                            print("Opcion no numerica")
                            input("Enter to continue")
                        elif not (int(opc) in range(1, 6)):
                            print("opcion numerica no valida")
                            input("Enter to continue")
                        else:
                            opc = int(opc)
                            if opc == 1:
                                lista_ids = list(dict_characters.keys())
                                for pasada in range(len(lista_ids)):
                                    for i in range(len(lista_ids) - 1 - pasada):
                                        if lista_ids[i] > lista_ids[i + 1]:
                                            aux = lista_ids[i]
                                            lista_ids[i] = lista_ids[i + 1]
                                            lista_ids[i + 1] = aux
                                datos = ""
                                for id in lista_ids:
                                    datos = datos + "\n{:<10}{:<17}{:^15}{:>3}{:>15}".format(id,
                                                                                             dict_characters[id][
                                                                                                 "name"],
                                                                                             dict_characters[id][
                                                                                                 "strength"],
                                                                                             dict_characters[id][
                                                                                                 "speed"],
                                                                                             dict_characters[id][
                                                                                                 "experience"]) + "\n"
                                print(cabecerachid, cabecerach + "\n" + "*" * 60, datos)
                            elif opc == 2:
                                lista_id = list(dict_characters.keys())
                                for pasada in range(len(lista_id)):
                                    for i in range(len(lista_id) - 1 - pasada):
                                        if dict_characters[lista_id[i]]["name"] > dict_characters[lista_id[i + 1]][
                                            "name"]:
                                            aux = lista_id[i]
                                            lista_id[i] = lista_id[i + 1]
                                            lista_id[i + 1] = aux
                                datos = ""

                                for id in lista_id:
                                    datos = datos + "\n{:<10}{:<17}{:^15}{:>3}{:>15}".format(id,
                                                                                             dict_characters[id][
                                                                                                 "name"],
                                                                                             dict_characters[id][
                                                                                                 "strength"],
                                                                                             dict_characters[id][
                                                                                                 "speed"],
                                                                                             dict_characters[id][
                                                                                                 "experience"]) + "\n"
                                print(cabecerachn, cabecerach + "\n" + "*" * 60, datos)
                            elif opc == 3:
                                lista_id = list(dict_characters.keys())
                                for pasada in range(len(lista_id)):
                                    for i in range(len(lista_id) - 1 - pasada):
                                        if dict_characters[lista_id[i]]["strength"] > dict_characters[lista_id[i + 1]][
                                            "strength"]:
                                            aux = lista_id[i]
                                            lista_id[i] = lista_id[i + 1]
                                            lista_id[i + 1] = aux
                                datos = ""

                                for id in lista_id:
                                    datos = datos + "\n{:<10}{:<17}{:^15}{:>3}{:>15}".format(id,
                                                                                             dict_characters[id][
                                                                                                 "name"],
                                                                                             dict_characters[id][
                                                                                                 "strength"],
                                                                                             dict_characters[id][
                                                                                                 "speed"],
                                                                                             dict_characters[id][
                                                                                                 "experience"]) + "\n"
                                print(cabecerachs, cabecerach + "\n" + "*" * 60, datos)
                            elif opc == 4:
                                lista_id = list(dict_characters.keys())
                                for pasada in range(len(lista_id)):
                                    for i in range(len(lista_id) - 1 - pasada):
                                        if dict_characters[lista_id[i]]["speed"] > dict_characters[lista_id[i + 1]][
                                            "speed"]:
                                            aux = lista_id[i]
                                            lista_id[i] = lista_id[i + 1]
                                            lista_id[i + 1] = aux
                                datos = ""

                                for id in lista_id:
                                    datos = datos + "\n{:<10}{:<17}{:^15}{:>3}{:>15}".format(id,
                                                                                             dict_characters[id][
                                                                                                 "name"],
                                                                                             dict_characters[id][
                                                                                                 "strength"],
                                                                                             dict_characters[id][
                                                                                                 "speed"],
                                                                                             dict_characters[id][
                                                                                                 "experience"]) + "\n"
                                print(cabecerachspe, cabecerach + "\n" + "*" * 60, datos)
                            elif opc == 5:
                                flg_041 = False
                                flg_04 = True
                elif opc == 2:
                    flg_04 = False
                    flg_042 = True
                    while flg_042:
                        print(menu42)
                        opc = input("->Option: ")
                        if not opc.isdigit():
                            print("Opcion no numerica")
                            input("Enter to continue")
                        elif not (int(opc) in range(1, 6)):
                            print("opcion numerica no valida")
                            input("Enter to continue")
                        else:
                            opc = int(opc)
                            if opc == 1:
                                lista_ids = list(dict_weapons.keys())
                                for pasada in range(len(lista_ids)):
                                    for i in range(len(lista_ids) - 1 - pasada):
                                        if lista_ids[i] > lista_ids[i + 1]:
                                            aux = lista_ids[i]
                                            lista_ids[i] = lista_ids[i + 1]
                                            lista_ids[i + 1] = aux
                                datos = ""
                                for id in lista_ids:
                                    if dict_weapons[id]["two_hand"] == 1:
                                        dict_weapons[id]["two_hand"] = "True"
                                    else:
                                        dict_weapons[id]["two_hand"] = "False"
                                    datos = datos + "\n{:<10}{:<17}{:^15}{:>3}{:>15}".format(id,
                                                                                             dict_weapons[id][
                                                                                                 "name"],
                                                                                             dict_weapons[id][
                                                                                                 "strength"],
                                                                                             dict_weapons[id][
                                                                                                 "speed"],
                                                                                             dict_weapons[id][
                                                                                                 "two_hand"]) + "\n"
                                print(cabecerawpid, cabecerawp + "\n" + "*" * 60, datos)

                            elif opc == 2:
                                lista_ids = list(dict_weapons.keys())
                                for pasada in range(len(lista_ids)):
                                    for i in range(len(lista_ids) - 1 - pasada):
                                        if dict_weapons[lista_ids[i]]["name"] > dict_weapons[lista_ids[i + 1]]["name"]:
                                            aux = lista_ids[i]
                                            lista_ids[i] = lista_ids[i + 1]
                                            lista_ids[i + 1] = aux
                                datos = ""
                                for id in lista_ids:
                                    if dict_weapons[id]["two_hand"] == 1:
                                        dict_weapons[id]["two_hand"] = "True"
                                    else:
                                        dict_weapons[id]["two_hand"] = "False"
                                    datos = datos + "\n{:<10}{:<17}{:^15}{:>3}{:>15}".format(id,
                                                                                             dict_weapons[id]["name"],
                                                                                             dict_weapons[id][
                                                                                                 "strength"],
                                                                                             dict_weapons[id]["speed"],
                                                                                             dict_weapons[id][
                                                                                                 "two_hand"]) + "\n"
                                print(cabecerawpid, cabecerawp + "\n" + "*" * 60, datos)
                            elif opc == 3:
                                lista_ids = list(dict_weapons.keys())
                                for pasada in range(len(lista_ids)):
                                    for i in range(len(lista_ids) - 1 - pasada):
                                        if dict_weapons[lista_ids[i]]["strength"] > dict_weapons[lista_ids[i + 1]][
                                            "strength"]:
                                            aux = lista_ids[i]
                                            lista_ids[i] = lista_ids[i + 1]
                                            lista_ids[i + 1] = aux
                                datos = ""
                                for id in lista_ids:
                                    if dict_weapons[id]["two_hand"] == 1:
                                        dict_weapons[id]["two_hand"] = "True"
                                    else:
                                        dict_weapons[id]["two_hand"] = "False"
                                    datos = datos + "\n{:<10}{:<17}{:^15}{:>3}{:>15}".format(id,
                                                                                             dict_weapons[id]["name"],
                                                                                             dict_weapons[id][
                                                                                                 "strength"],
                                                                                             dict_weapons[id]["speed"],
                                                                                             dict_weapons[id][
                                                                                                 "two_hand"]) + "\n"
                                print(cabecerawpid, cabecerawp + "\n" + "*" * 60, datos)
                            elif opc == 4:
                                lista_ids = list(dict_weapons.keys())
                                for pasada in range(len(lista_ids)):
                                    for i in range(len(lista_ids) - 1 - pasada):
                                        if dict_weapons[lista_ids[i]]["speed"] > dict_weapons[lista_ids[i + 1]][
                                            "speed"]:
                                            aux = lista_ids[i]
                                            lista_ids[i] = lista_ids[i + 1]
                                            lista_ids[i + 1] = aux
                                datos = ""
                                for id in lista_ids:
                                    if dict_weapons[id]["two_hand"] == 1:
                                        dict_weapons[id]["two_hand"] = "True"
                                    else:
                                        dict_weapons[id]["two_hand"] = "False"
                                    datos = datos + "\n{:<10}{:<17}{:^15}{:>3}{:>15}".format(id,
                                                                                             dict_weapons[id]["name"],
                                                                                             dict_weapons[id][
                                                                                                 "strength"],
                                                                                             dict_weapons[id]["speed"],
                                                                                             dict_weapons[id][
                                                                                                 "two_hand"]) + "\n"
                                print(cabecerawpid, cabecerawp + "\n" + "*" * 60, datos)
                            elif opc == 5:
                                flg_042 = False
                                flg_04 = True

                elif opc == 5:
                    flg_00 = True
                    flg_04 = False

