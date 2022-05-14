import sys
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')

print("Witaj w tym prostym kalkulatorze, co chciałbyś policzyć?")
działanie = input("Podaj działanie, posługując się odpowiednią liczbą:  \n1- dodawanie,  \n2- odejmowanie,  \n3- mnożenie,  \n4- dzielenie:  \n")
def kalkulator(działanie):
    liczba1 = int(input("Podaj składnik 1: "))
    liczba2 = int(input("Podaj składnik 2: "))
    if działanie == "1":
        logging.info("Wykonasz dodawanie %s i %s" % (liczba1, liczba2))
        print("Wynik to:", liczba1+liczba2)
    elif działanie == "2":
        logging.info("Wykonasz odejmowanie %s i %s" % (liczba1, liczba2))
        print("Wynik to:", liczba1-liczba2)
    elif działanie == "3":
        logging.info("Wykonasz mnożenie %s i %s" % (liczba1, liczba2))
        print("Wynik to:", liczba1*liczba2)
    elif działanie == "4":
        logging.info("Wykonasz dzielenie %s i %s" % (liczba1, liczba2))
        print("Wynik to:", liczba1/liczba2)

kalkulator(działanie)
