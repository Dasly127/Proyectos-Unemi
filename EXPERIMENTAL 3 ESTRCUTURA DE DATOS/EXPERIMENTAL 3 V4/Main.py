
'''
Utilizando POO, cree una clase PILAS_NUM que permita llenar 2 pilas con 5 y 7
elementos numéricos cada una, con esa base, desde el programa principal usted deberá poder
elegir entre intercalarlos en una nueva pila o sumarlas entre sí (estos métodos deben ser parte
de su clase PILAS_NUM).
Como criterio de combinación siempre se debe iniciar con la lista que ene mayor número de
elementos, aquellos elementos sobrantes se colocarán al final de la estructura.
Los elementos de las estructuras se presentan en formato de 1 fila. Cuando presente la
combinación de los elementos, a manera de información debe presentar el contenido de los
datos de cada pila original que u lizó
'''


##En esta versión realizamos un control de excepciones para 
##evitar posibles conflictos en el programa y deje de Funcionar


from pilas_num import PILAS_NUM

### Creamos una instancia de la clase PILAS_NUM
def main():
    pilas = PILAS_NUM()
    ### Llenamos las pilas con elementos ingresados por el usuario
    pilas.llenar_pilas()
    
    while True: ##Bucle While para crear el menú de opciones
        print("\nMenú de Opciones:")
        print("1. ···Intercalar pilas···")
        print("2. ··· Sumar pilas···")
        print("3. ···Mostrar pilas···")
        print("4. ···Salir del programa y finalizar···")
        
        try: ##Leemos la opción escogida por el usuario
            opcion = int(input("Elige una opción: "))
        except ValueError: ##Control de excepciones para evitar fallos
            print("Opción no válida, intenta de nuevo.")
            continue
        
        if opcion == 1: ## Intercala las pilas
            pilas.intercalar_pilas()  

        elif opcion == 2: ## Suma las pilas
            pilas.sumar_pilas()

        elif opcion == 3: ## Muestra las pilas, incluidas las sumadas o intercaladas
            pilas.mostrar_pilas()

        elif opcion == 4: ## Finaliza el programa
            break
        else:
            print("Opción no válida, intenta de nuevo.") 
        ##Control de excepciones en caso de que el usuario escoja una opción incorrecta

if __name__ == "__main__":
    main()
