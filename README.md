# Algorytm Dijkstry

---
## Co robi

---
Algorytm Dijkstry służy do znalezienia minimalnej odległości między wybranym węzłem grafu a pozostałymi

## Jak użyć

---
Aby użyć program potrzebny jest plik .json z danymi grafu w formie:<br>
````python
[["A", "B", 2], ...]
````
Gdzie "A" i "B" to nazwy węzłów grafu a 2 to waga krawędzi między nimi<br><br>
Należy pamiętać, by dla grafów nieskierowanych zamieścić krawędzie w obie strony, np.<br>
````python
[["A", "B", 2], ["B", "A", 2]]
````
Nie można również zapomnieć, że algorytm działa tylko dla krawędzi o nieujemnych wagach<br><br>
Po uruchomieniu programu należy podać nazwę pliku .json oraz węzeł źródłowy<br><br>
Wynikiem działania programu jest tabela, w której w pierwszym rzędzie wypisane zostają wszystkie węzły grafu,<br>
w drugim znajduje się minimalny dystans od węzła źródłowego do powyższego węzła, a w trzecim poprzedzający go węzeł
 
## Technologie

---
Program został napisany używając:
* Python 3.7
* numpy 1.20.1
* tabulate 0.8.9
