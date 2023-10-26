import pandas as pd

def tester(solutions):
    for i in range(1, 10):
        print(test_solution(solutions[i-1], i))
    return f"{'Bestanden' if Gesamtpunkte >= 30 else 'Durchgefallen'} mit {Gesamtpunkte}/60 Punkten"    
Gesamtpunkte = 0
def test_solution(solution, exercise):
    global Gesamtpunkte
    match exercise:
        case 1:
            punkte = 0
            if solution[0] == 5: punkte += 0.5
            if solution[1] == 3: punkte += 0.5
            if solution[2] == 8: punkte += 1.0
            Gesamtpunkte += punkte
            return f"Aufgabe 1: {punkte}/2.0 Punkten"
        case 2:
            # ["s", "f", "b", "i", "i", "i", "s"]
            punkte = 0
            if solution[0] == "s": punkte += 1.0
            if solution[1] == "f": punkte += 1.0
            if solution[2] == "b": punkte += 1.0
            if solution[3] == "i": punkte += 1.0
            if solution[4] == "i": punkte += 1.0
            if solution[5] == "i": punkte += 1.0
            if solution[6] == "s": punkte += 1.0
            Gesamtpunkte += punkte
            return f"Aufgabe 2: {punkte}/7.0 Punkten"
        case 3:
            #print(f"Deine Lösung: resultat = {solution}")
            punkte = 0
            if 4 in solution: punkte += 1.5
            if 6 in solution: punkte += 1.5
            Gesamtpunkte += punkte
            return f"Aufgabe 3: {punkte}/3.0 Punkten"
        case 4:
            #print(f"Deine Lösung: resultat = {solution}")
            punkte = 0
            if 0 in solution: punkte += 1.0
            if 10 in solution: punkte += 1.0
            if len(solution) == 11: punkte += 1.0
            Gesamtpunkte += punkte
            return f"Aufgabe 4: {punkte}/3.0 Punkten"
        case 5:
            #print(f"Deine Lösung: Input: 'Ein Esel lese nie.', resultat = {solution('Ein Esel lese nie.')}")
            punkte = 0
            if solution("As") == False: punkte += 2.0
            if solution("anna") == True: punkte += 2.0
            if (solution("Paliilap") == True): punkte += 2.0
            if (solution('Ein Esel lese nie.') == True): punkte += 4.0
            Gesamtpunkte += punkte
            return f"Aufgabe 5: {punkte}/10.0 Punkten"
        case 6:
            punkte = 0
            #print(f"Deine Lösung: Input: 6 resultat = {solution(6)}")
            if solution(6) == True: punkte += 2.5
            if solution(5) == False: punkte += 2.5
            Gesamtpunkte += punkte
            return f"Aufgabe 6: {punkte}/5.0 Punkten"
        case 7:
            punkte = 0
            #print(f"Deine Lösung: resultat = {solution('Student', 'Python', 'Programmieren')}")
            student = solution('Student', 'Python', 'Programmieren')
            if student: punkte += 2
            if student.name == "Student": punkte += 2.0
            if student.studiengang == "Python": punkte += 2.0
            if student.hobby == "Programmieren": punkte += 2.0
            if student.__str__() == "Student studiert Python und liebt Programmieren": punkte += 2.0
            Gesamtpunkte += punkte
            return f"Aufgabe 7: {punkte}/10.0 Punkten"
        case 8:
            punkte = 0
            if isinstance(solution[0], pd.Series): punkte += 1.0
            if "Mary" in solution[0].tolist(): punkte += 1.5
            if solution[1] == 1.54: punkte += 2.5
            if solution[2]["alter"] == 8: punkte += 2.5
            if isinstance(solution[3], pd.Series): punkte += 1.0
            if "Lena@mail.de" in solution[3].tolist(): punkte += 1.5
            Gesamtpunkte += punkte
            return f"Aufgabe 8: {punkte}/10.0 Punkten"
        case 9:
            punkte = 0
            if solution(10) in ["richtig", "größer", "kleiner"]: punkte += 10.0
            Gesamtpunkte += punkte
            return f"Aufgabe 9: {punkte}/10.0 Punkten"
    