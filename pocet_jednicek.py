#napis program, ktery vrati pocet jednicek v zadanem cisle
#zkusit i bez prace s retezci
def pocet_jednicek(cislo):
    pocet=0
    while cislo>0:
        zbytek=cislo procento 10
        if zbytek==1:
            pocet=cislo//10
        cislo=cislo//10
    return pocet

cislo=int(input("Zadej cislo: "))

pocet=pocet_jednicek(cislo)

print("Pocet jednicek v cisle {} je {}".format(cislo, pocet))



#########
