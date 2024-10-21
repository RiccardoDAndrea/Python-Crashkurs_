# Arbeitsblatt: Umgang mit if, elif und else-Anweisungen


# - Ziel: 
#       In diesem Arbeitsblatt lernst du, wie du if, elif und else-Anweisungen verwendest, um verschiedene Entscheidungen im Code zu treffen.

# - Aufgabe:
#       Entwickle ein Szenario, eine Geschichte oder eine Situation, in der du eine Benutzereingabe erwartest. Verwende if, elif und else, um auf diese Eingabe zu 
#       reagieren und verschiedene Ergebnisse zu erzeugen.

#- Erklärung:
#       input("Hier steht eine Frage oder ein Text"): Ermöglicht es dem Benutzer, über das Terminal eine Eingabe zu machen.
#       .lower(): Wandelt alle Buchstaben eines eingegebenen Strings in Kleinbuchstaben um, um fehlerhafte Eingaben durch Groß- und Kleinschreibung zu vermeiden.

# Du kannst gerne weiter machen bei "Es war ein mal.." oder fängst von vorne an und schreibst eine neue Geschichte.

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Benutzer nach Name und Alter fragen
user_name = input("Wie heißt du: ")
user_age = int(input("Wie alt bist du: "))
age_req = int(18)
health = 20

# Überprüfen, ob der Benutzer volljährig ist
if user_age >= 18:
    print(f"Willkommen, {user_name}!")
    print("Du bist volljährig und kannst dich auf die Reise ins Horror-Haus begeben.")
    
    # Benutzer fragen, ob er bereit ist
    user_ready = input("Bist du bereit für die Reise? [j/n]: ").lower()

    if user_ready == "j":
        print("Dann lass uns loslegen. Entscheide deine Bewaffnung")
        weapon = input("Welche Waffe willst du mit nehmen trage ein [Axt/Schwert/Teddybär]")

        if weapon == "Axt":
            print(f"Gute Wahl die {weapon} zu wählen")
            enter_house = input(f"{user_name} sieht ein Verlassenes Haus willst du es betreten [j/n]").lower()

            if enter_house == "j":    
                print("Du hörst ein selstames Geräusch aus des Boden, ein Gestalt nährt sich.")
                monster = input("Spricht du es an oder verlässt du das Haus [j/n]")

                if monster == "j":
                    print("Du siehst in der Ferne wie ein Monster angestürmt kommt und dich verletzt.")
                    print(f"Du verlierst 10 Lebenspunkte. Du hast nur noch {health - 10} Lebenspunkte")
                    run_away = input("Versucht du zu kämpfen oder wegzulaufen ? [kampf/weglaufen]: ").lower()
                
                    if run_away == "kampf":
                        print("")

                    elif run_away == "weglaufen":
                        print("Du versuchst wegzulaufen und landest im Keller.")
                        input("Versuch du dich im Schrank oder läufst du weiter [Schrank/weiter]")
                    
                    else: 
                        print(f"Du entscheidest dich nichts zu machen und du verlierst {health - 10}") 
                        print(f"{user_name} wurde niemals gefunden")   
            
        if weapon == "Schwert":
            print(f"Gute Wahl das {weapon} zu wählen")
            enter_house = input(f"{user_name} sieht ein Verlassenes Haus willst du es betreten [j/n]").lower()

            if enter_house == "j":    
                print("Du hörst ein selstames Geräusch aus des Boden, ein Gestalt nährt sich.")
                monster = input("Spricht du es an oder verlässt du das Haus [j/n]")

                if monster == "j":
                    print("Du siehst in der Ferne wie ein Monster angestürmt kommt und dich verletzt.")
                    print(f"Du verlierst 10 Lebenspunkte. Du hast nur noch {health - 10} Lebenspunkte")
                    run_away = input("Versucht du zu kämpfen oder wegzulaufen ? [kampf/weglaufen]: ").lower()
                
                    if run_away == "kampf":
                        print("")

                    elif run_away == "weglaufen":
                        print("Du versuchst wegzulaufen und landest im Keller.")
                        input("Versuch du dich im Schrank oder läufst du weiter [Schrank/weiter]")
                    
                    else: 
                        print(f"Du entscheidest dich nichts zu machen und du verlierst {health - 10}") 
                        print(f"{user_name} wurde niemals gefunden")   
            
        if weapon == "Teddybär":
            print("")



        if enter_house == "j":    
            print("Du hörst ein selstames Geräusch aus des Boden, ein Gestalt nährt sich.")
            monster = input("Spricht du es an oder verlässt du das Haus [j/n]")

            if monster == "j":
                print("Du siehst in der Ferne wie ein Monster angestürmt kommt und dich verletzt.")
                print(f"Du verlierst 10 Lebenspunkte. Du hast nur noch {health - 10} Lebenspunkte")
                run_away = input("Versucht du zu kämpfen oder wegzulaufen ? [kampf/weglaufen]: ").lower()
            
                if run_away == "kampf":
                    print("")

                elif run_away == "weglaufen":
                    print("Du versuchst wegzulaufen und landest im Keller.")
                    input("Versuch du dich im Schrank oder läufst du weiter [Schrank/weiter]")
                
                else: 
                    print(f"Du entscheidest dich nichts zu machen und du verlierst {health - 10}") 
                    print(f"{user_name} wurde niemals gefunden")   
            
            elif monster == "n":
                print(f"Du verlässt das Haus und siehst eine weitere Kreatur aus den Garten schuppen die dich an stürmt")
                
            
            else:
                print("Fehlerhafte eingabe")
        
        else:
            print("Du betritts das Haus nicht und entscheidest dich um das Haus herumzulaufen")
            garden = input("Du siehst ein umrisse eines Gartenschuppen betrittst du es [j/n]").lower()

            if garden == "j":
                print("Auf den Weg zum Gartenschuppen verlässt eine Gestalt den Gartenschuppen")
                print("Und stürmt auf dich zu")
                print(f"{user_name} verliert 5 Lebenspunkte sei vorsichtig du hast nur noch: {health - 5} Lebenspunkte")
            
            elif garden == "n":
                print("Du verlässt das Grundstück und bist wieder auf der Straße")                   

    else:
        print("Schade, vielleicht ein andermal!")

else:
    print(f"Es tut mir leid, {user_name}, du bist noch nicht 18.")
    print(f"Du bist erst {user_age} bitte komm wieder in {age_req - user_age} Jahren, wenn du alt genug bist!")







