#Verilen listenin elemanlarını tersine döndüren fonksiyon
def ters(liste):
    liste.reverse()
    for i in liste:
        if type(i) is list:
            ters(i)
    return liste

myList=[1,2,3,["car1","car2","car3",[8,9,10]],150,152,153]
print(ters(myList))
