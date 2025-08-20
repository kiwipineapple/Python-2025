# --------------------------------------------
# Temperaturprüfung – Einfache Bedingung
# --------------------------------------------
# Bsp. 1 : Nur mit if

temperature = 40 # Ändere auf z. B. 40, um andere Ausgabe zu sehen

if temperature > 30:
    print('Es ist heiß!!!!')


print('-'*40)


# Bsp. 2 : Nur mit if/ else

temperature = 20 # Ändere auf z. B. 40, um andere Ausgabe zu sehen

if temperature > 30:
    print('Es ist heiß!!!!')
else:
    print('Es is kühl!!!') 


print('-'*40)

# -------------------
# Erweiterte Bedingung mit mehreren Bereichen
#-----------------

temperature = 15
if temperature >= 30:
    print('Es ist heiß!!!!')

elif temperature > 30 and temperature >=20:
    print('Es ist warm')

elif temperature < 20 and temperature >= 10:
    print('Es ist kalt')

else:
    print('Es is sehr kalt!!!') 

print('-'*40)    
# -------------------
# Erweiterte Bedingung mit mehreren Bereichen (Kompakter Ausdruck)
#-----------------

temperature = 15
if temperature >= 30:
    print('Es ist heiß!!!!')

elif 20 <= temperature < 30 :
    print('Es ist warm')

elif 10 <= temperature < 20:
    print('Es ist kalt')

else:
    print('Es is sehr kalt!!!') 


print('-'*40)    
# -------------------
# Erweiterte Bedingung mit mehreren Bereichen (Vereinfachter Ausdruck)
#-----------------

temperature = 15
if temperature >= 30:
    print('Es ist heiß!!!!')

elif temperature >= 20 :
    print('Es ist warm')

elif temperature >=10:
    print('Es ist kalt')

else:
    print('Es is sehr kalt!!!') 


#----------------- 
# #Verschartelte if
#--------------------
x = 0
if x >= 0: 
    if x % 2 == 0: 
        print("x ist positiv und gerade") 
    else: 
        print("x ist positiv aber ungerade") 
else: 
    print("x ist nicht positiv")