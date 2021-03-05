# StavaTestProject

#### Zadanie testowe polegające na opracowaniu web aplikacji opartej o Python Django wraz z Vue.js 

#### Punkt 1
W celach podania punktów był stworzony frontend interfejs napisany w Vue.js.
##### Opis:
Po lewej stronie interfejsu znajdują się:
* mapa — która umożliwia wyświetlenie punktów oraz nawigacji pomiędzy nimi.
* wyniki obliczeń:
* odległość pomiędzy wszystkimi podanymi markerami w metrach
* czas trwania obliczenia odległości
* forma do podania parametru REQUEST_ID
* przycisk Calculate, który spowoduje wysłanie wszystkich punktów do obliczenia na serwer.

Po prawej stronie interfejsu znajdują się:
* lista z wszystkimi punktami — klikniecie punktu spowoduje przeniesienie środka mapy do tego punktu.
* Przycisk do usuwania dowolnych punktów
* forma do wprowadzenia nowego punktu. Zakres wartości Longtitude ±[0; 180]; Latitude ±[0;90]


#### Punkt 2
Aplikacja udostępnia POST endpoint @/api/mapper przyjmujący {distance:<JSON>, REQUEST_ID:'str'} i zwraca {Distance:<float>,  "Execution Time":<float>}
  
Parametr distance jest przekazany do endpointu jest w postaci 
```javascript
JSON.stringify([
['lat1,long1','lat2,long2'],
['lat2,long2','lat3,long3'],
])
```

![alt text](https://i.postimg.cc/5yFJCc0T/Screenshot-2021-03-05-stavafrontend-1.png)
