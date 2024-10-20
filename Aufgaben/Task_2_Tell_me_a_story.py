# Arbeitsblatt: Umgang mit if, elif und else-Anweisungen


# - Ziel: 
#       In diesem Arbeitsblatt lernst du, wie du if, elif und else-Anweisungen verwendest, um verschiedene Entscheidungen im Code zu treffen.

# - Aufgabe:
#       Entwickle ein Szenario, eine Geschichte oder eine Situation, in der du eine Benutzereingabe erwartest. Verwende if, elif und else, um auf diese Eingabe zu reagieren und verschiedene Ergebnisse zu erzeugen.

#- Erklärung:
#       input("Hier steht eine Frage oder ein Text"): Ermöglicht es dem Benutzer, über das Terminal eine Eingabe zu machen.
#       .lower(): Wandelt alle Buchstaben eines eingegebenen Strings in Kleinbuchstaben um, um fehlerhafte Eingaben durch Groß- und Kleinschreibung zu vermeiden.

# Du kannst gerne weiter machen bei "Es war ein mall.." oder fängst von vorne an und schreibst eine neue Geschichte.

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Benutzer nach Name und Alter fragen
user_name = input("Wie heißt du: ")
user_age = int(input("Wie alt bist du: "))
age_req = int(18)


# Überprüfen, ob der Benutzer volljährig ist
if user_age >= 18:
    print(f"Willkommen, {user_name}!")
    print("Du bist volljährig und kannst dich auf die Reise ins Horror-Haus begeben.")
    
    # Benutzer fragen, ob er bereit ist
    user_ready = input("Bist du bereit für die Reise? [j/n]: ").lower()

    if user_ready == "j":
        print("Dann lass uns loslegen!")
        print("Es war ein mal... ")
        enter_house = input(f"{user_name} sieht ein Verlassenes Haus willst du es betreten [j/n]").lower()

    else:
        print("Schade, vielleicht ein andermal!")
else:
    print(f"Es tut mir leid, {user_name}, du bist noch nicht 18.")
    print(f"Du bist erst {user_age} bitte komm wieder in {age_req - user_age} Jahren, wenn du alt genug bist!")







