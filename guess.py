import random

myNumber = random.randrange(0, 100, 1)

print("Ich habe mir eine Zahl von 0 bis 100 überlegt. Versuche sie zu erraten!")

while True:
    try:
        guessedNumber = int(input())
        if guessedNumber < myNumber:
            print("Meine Zahl ist größer.")
        if guessedNumber > myNumber:
            print("Meine Zahl ist kleiner.")
        if guessedNumber == myNumber:
            break
    except:
        print("Die Eingabe muss eine ganze Zahl sein.")

print("Herzlichen Glückwunsch! Du hast die Zahl erraten!")
