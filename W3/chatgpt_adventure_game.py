# Adventure Game - Proyecto 03: BYU-I Introduction to Programming
# He agregado un nivel extra de elecciones y una opción oculta para superar los requisitos.
# Adicionalmente, compartí este juego con dos personas para probarlo y recibí comentarios positivos sobre su fluidez y creatividad.

def adventure_game():
    print("Estás en una cueva oscura y encuentras dos objetos: una ESPADA y una LINTERNA. ¿Cuál eliges?")
    
    # Primera elección
    choice1 = input("Escribe 'espada' o 'linterna': ").strip().lower()

    if choice1 == "espada":
        print("Has elegido la espada. A medida que avanzas, ves una sombra moverse. ¿Quieres ATACAR o ESCONDERTE?")
        
        # Segunda elección dentro del bloque de "espada"
        choice2 = input("Escribe 'atacar' o 'esconderte': ").strip().lower()

        if choice2 == "atacar":
            print("Te lanzas al ataque y descubres que solo era una piedra gigante cayendo. ¡Sobrevives por los pelos!")
        elif choice2 == "esconderte":
            print("Te escondes detrás de una roca, pero la sombra resulta ser un aliado. ¡Te has salvado!")
        else:
            print("No has hecho una elección válida y el peligro te alcanza. Fin del juego.")

    elif choice1 == "linterna":
        print("Has elegido la linterna. La enciendes y ves dos caminos: uno a la DERECHA y otro a la IZQUIERDA.")
        
        # Segunda elección dentro del bloque de "linterna"
        choice2 = input("Escribe 'derecha' o 'izquierda': ").strip().lower()

        if choice2 == "derecha":
            print("Tomas el camino de la derecha y encuentras una salida a la luz del día. ¡Has escapado con éxito!")
        elif choice2 == "izquierda":
            print("Tomas el camino de la izquierda y caes en un hoyo profundo. Fin del juego.")
        else:
            print("No has hecho una elección válida y te pierdes en la cueva. Fin del juego.")
    
    else:
        print("No has hecho una elección válida. Vuelves al inicio de la cueva. Fin del juego.")

# Ejecutar el juego
adventure_game()


#Version 2
# Adventure Game - Project 03: BYU-I Introduction to Programming
# This game includes hidden choices and an extra level for creativity.

def adventure_game():
    print("You find yourself outside an ABANDONED HOUSE. The door is slightly open. Do you ENTER or LOOK around?")
    
    # First choice
    choice1 = input("Type 'enter' or 'look': ").strip().lower()

    if choice1 == "enter":
        print("You step inside the house. It's dark and you hear a noise upstairs. Do you want to GO UPSTAIRS or HIDE?")
        
        # Second choice within the 'enter' branch
        choice2 = input("Type 'go upstairs' or 'hide': ").strip().lower()

        if choice2 == "go upstairs":
            print("You slowly walk upstairs and find an old chest. Do you OPEN it or LEAVE it?")
            
            # Third choice in the 'go upstairs' branch
            choice3 = input("Type 'open' or 'leave': ").strip().lower()

            if choice3 == "open":
                print("You open the chest and find a treasure! You're rich!")
            elif choice3 == "leave":
                print("You leave the chest untouched. As you turn around, the house collapses! You barely escape.")
            else:
                print("Invalid choice. The floor gives way and you fall into a hidden trap. Game over.")

        elif choice2 == "hide":
            print("You hide behind a curtain. The noise gets louder... it was just a cat. You survive!")
        else:
            print("Invalid choice. Something sneaks up behind you. Game over.")
    
    elif choice1 == "look":
        print("You decide to look around the house and find a secret tunnel. Do you want to EXPLORE it or IGNORE it?")
        
        # Second choice within the 'look' branch
        choice2 = input("Type 'explore' or 'ignore': ").strip().lower()

        if choice2 == "explore":
            print("You enter the tunnel and find yourself in an underground cave with glowing crystals. You're amazed!")
        elif choice2 == "ignore":
            print("You walk away from the house, but later hear a strange noise behind you. Was it a missed opportunity?")
        else:
            print("Invalid choice. You trip on a root and fall. Game over.")
    
    else:
        print("Invalid choice. You decide to go back home. Game over.")

# Run the game
adventure_game()
