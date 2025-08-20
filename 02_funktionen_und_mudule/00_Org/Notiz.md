**List Entpacken**  
<code>
```python
def infos(name, stadt):  
    print(f"{name} lebt in {stadt}")  

daten_liste = ["Anna", "Berlin"]  
infos(*daten_liste)
```
entspricht: infos("Anna", "Berlin")  

**Dic Entpacken**  
<code>
```python
def infos(name, stadt):  
    print(name)
    print(f"{name} lebt in {stadt}")

daten_dict = {"name": "Tom", "stadt": "Hamburg"}    
infos(**daten_dict)
```

**List in Funktion**  
map(Funktion, Liste)  
<code>
```python
def verdoppeln(x):
    return x * 2

zahlen = [1, 2, 3, 4]
ergebnis = map(verdoppeln, zahlen)
print(list(ergebnis))
```
Ausgabe: [2, 4, 6, 8]