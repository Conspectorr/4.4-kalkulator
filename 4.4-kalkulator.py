from ast import Mult
import sys
import logging
import operator
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')

print("Witaj w tym prostym kalkulatorze, co chciałbyś policzyć?")
działanie = input("Podaj działanie, posługując się odpowiednią liczbą:  \nDodawanie: 1  \nOdejmowanie: 2  \nMnożenie: 3  \nDzielenie: 4\n")
def kalkulator(działanie):
    if działanie == "1":
      liczby_text=input("Podaj dodawane wartości, rozdzielając je przecinkiem:")
      liczby = liczby_text.split(',')
      liczby2=[int(i) for i in liczby]
      logging.info("Wykonujesz dodawanie %s" % liczby2)
      print("Wynik to:", sum(liczby2))
    elif działanie == "2":
        liczba1 = int(input("Podaj wartość 1: "))
        liczba2 = int(input("Podaj wartość 2: "))
        logging.info("Wykonujesz odejmowanie %s i %s" % (liczba1, liczba2))
        print("Wynik to:", liczba1-liczba2)
    elif działanie == "3":
        liczby_text=input("Podaj mnożone wartości, rozdzielając je przecinkiem:")
        liczby = liczby_text.split(',')
        liczby2=[int(i) for i in liczby]
        logging.info("Wykonujesz mnożenie %s" % liczby2)
        print("Wynik to:", sum(liczby2))
#Brak mi wbudowanej funkcji dla takiego działania chyba, więc trzeba własną...
    elif działanie == "4":
        liczba1 = int(input("Podaj wartość 1: "))
        liczba2 = int(input("Podaj wartość 2: "))
        logging.info("Wykonujesz dzielenie %s i %s" % (liczba1, liczba2))
        print("Wynik to:", liczba1/liczba2)
    else:
        print("Wybierz prawidłowe działanie!")

kalkulator(działanie)
print("Do zobaczenia w kolejnych działaniach!")