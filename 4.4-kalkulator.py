import sys
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s', filename="kalkulator-log.log")

print("Witaj w tym prostym kalkulatorze, co chciałbyś policzyć?")
działanie = input("Podaj działanie, posługując się odpowiednią liczbą: 1- dodawanie, 2- odejmowanie, 3- mnożenie, 4- dzielenie: ")
def kalkulator(działanie):
    liczba1 = ("Podaj składnik 1: ")
    liczba2 = ("Podaj składnik 2: ")
    if działanie == "1":
        print("Wykonasz dodawanie")
    elif działanie == "2":
        print("Wykonasz odejmowanie")
    elif działanie == "3":
        print("Wykonasz mnożenie")
    elif działanie == "4":
        print("Wykonasz dzielenie")

kalkulator(działanie)
