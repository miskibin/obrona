# streszczenie

## Pojęcie algorytmu; typy, własności i przykłady algorytmów.

1. Algorytm: Skończony zestaw czynności do rozwiązania problemu.
1. Warunki algorytmu: Dane wejściowe/wyjściowe, określoność, skuteczność, skończoność.
1. Formy przedstawiania: Opis słowny, lista kroków, schemat blokowy, program komputerowy.
1. Typy algorytmów: Sortujące, wyszukiwania, haszowania, programowania dynamicznego, operacje na ciągach znaków, testowanie pierwszości.
1. Przykłady algorytmów: Wyszukiwanie binarne, sortowanie bąbelkowe, BFS, DFS, Quicksort, Kruskal, Dijkstra, sortowanie przez wstawianie, przez scalanie, Euklidesa.

## 2. Diagramy i ich rola w języku SysML; różnice w językach SysML i UML

1. SysML to język modelowania systemów z różnymi typami diagramów.
2. Diagramy SysML służą do projektowania i komunikacji w zespole.
3. Przykłady diagramów SysML: sekwencji, przypadków użycia, definicji bloków.
4. SysML, rozszerzenie UML, skupia się na szerokim zakresie systemów.
5. SysML obejmuje więcej niż UML, w tym aspekty mechaniczne i elektryczne.

## 3. Modele w przestrzeni stanów. Ocena jakości i porównanie modeli

1. Modele w przestrzeni stanów: Reprezentacja systemu przez stany i zmienne stanu, umożliwiająca przewidywanie przyszłości systemu.
2. Rodzaje modeli: dynamiczne/ciągłe (równania różniczkowe) i dyskretne (równania różnicowe).
3. Stan równowagi: System pozostający stabilny lub wracający do pierwotnego stanu po zaburzeniu.
4. Ocena modeli: różne metody, w tym najmniejsze kwadraty, maksymalna wiarygodność, i metoda Bayesa, służące do oceny jakości i dopasowania modelu.

## 4 Metody modelowania systemów dyskretnych. 
1. Rownania stanu, wektor stanu
2. rownania roznicowe 
3. transmitancja

## 5. Statystyczna analiza wyników symulacji. 

!!! NIE ROZUMIEM
1. Kluczowy element symulacji
2. 

## [6 Pojęcie fuzji danych oraz główne obszary jej wykorzystania.](https://docs.google.com/document/d/1rC8y8PmERfAr4ZLPY1JeiOymnQPmSi06ohv6GTbu5rE/edit#heading=h.qq5zh8o6wqzs)

1. Są to metody umożliwiające łączenie i przetwarzanie danych z różnych źródeł
2. Etapy: porządkowanie i kojarzenie danych, działania korekcyjne, algorytym realizujący fuzję danych
3. typy: fuzja współpracy, współzawodnictwa, uzupełniająca
4. obszary wykorzystania: 
   - medycyna: diagnoza chorób, monitorowanie stanu zdrowia
   - rolnictwo: dane z satelitów, dronów i czujników terenowych do zarządzania zasobami wodnymi, nawożeniem, ochroną roślin
5. przykłady zastosowań: monitorownanie stanów mostów, optymalizacja tras w logistyce, wykrywanie pożarów lasów.


## 7. Metody estymacji parametrów systemów dynamicznych Estymacja zmiennych stanu. Liniowy i rozszerzony filtr Kalmana. 

1. Techniki wykorzystywane do oceny i przewidywania stanu dynamicznych systemów w czasie rzeczywistym.
2. zalozenia: wejscie i wyjscie dostepne pomiarowo, zaklucenia maja rozklad normalny, wektroy szumow i pomiarow sa niezalezne
3. filtr kalmana: Etapy: predykcja, korekcja
4. Typy: Liniowy i Rozszerzony dla systemów nieliniowych.
5. Obszary wykorzystania:
    - nawigacja i śledzenie: precyzyjne śledzenie pozycji i orientacji w przestrzeni,
    - robotyka: estymacja trajektorii ruchu robotów,
    - finanse: prognozowanie trendów rynkowych i ocena ryzyka.

## 9. Analityczne metody optymalizacji z ograniczeniami. Numeryczne metody optymalizacji bez i z ograniczeniami. 

1. def:  Obliczeniowe podejście do problemu optymalizacji. Działają iteracyjnie
2. charakterystyka: przybliżone rozw. , gdy nie ma rozw. analitycznego.
3. metody numeryczne:  algorytm genetyczny, algorytm wspinaczkowy – stochastyczny, symulowane wyżarzanie, algorytm mrówkowy, algorytm pszczeli, algorytm roju cząstek

## [10. Zastosowania programowania liniowego.](https://docs.google.com/document/d/1rC8y8PmERfAr4ZLPY1JeiOymnQPmSi06ohv6GTbu5rE/edit#heading=h.9uges9gkw738) 

...


## [9. Systemy wieloagentowe. Architektura agenta. Komunikacja, koordynacja, kooperacja i konkurencja.](https://docs.google.com/document/d/1rC8y8PmERfAr4ZLPY1JeiOymnQPmSi06ohv6GTbu5rE/edit#heading=h.e4a6x4j90auy) 

- sklad systemu: srodowisko, agent, obiekty, relacje
- cechyy: autonomiczni agenci, otwartosc, srodowisko okresla rodzaj komunikacji
- typy agentow: logiczny, reakcyjny BDI, warstwowy
- architektura: sensory, modul percepcji, modul planowania, modul komunikacji, modul wykonawczy
- srodowiska: dostepne/niedostepne, statyczne/dynamiczne, deterministyczne/niedeterministyczne, epizodyczne/nieepizodyczne 

## [10. Zastosowania programowania liniowego.](https://docs.google.com/document/d/1rC8y8PmERfAr4ZLPY1JeiOymnQPmSi06ohv6GTbu5rE/edit#heading=h.9uges9gkw738) 

- Metoda matematyczna do optymalizacji modelu z liniowymi relacjami, służąca do uzyskania najlepszego wyniku, np. maksymalnego zysku lub minimalnego kosztu.
- Funkcja celu, ograniczenia, zmienne decyzyjne
1. Minimalizacja kosztów transportu w firmie logistycznej poprzez optymalizację tras dostaw.
2. Maksymalizacja zysków w fabryce poprzez efektywne zarządzanie czasem pracy maszyn i surowców.
3. Zarządzanie zapasami w sklepie detalicznym, aby zminimalizować koszty magazynowania przy jednoczesnym zaspokajaniu popytu klientów.
4. Planowanie upraw w gospodarstwie rolnym w celu maksymalizacji wydajności przy ograniczonych zasobach.

## [11. Systemy podejmowania i wspomagania decyzji ? definicje, metody i algorytmy wyznaczania decyzji, zastosowania.](https://docs.google.com/document/d/1rC8y8PmERfAr4ZLPY1JeiOymnQPmSi06ohv6GTbu5rE/edit#heading=h.oqirun7nbv2q) 

...

## 12. Reprezentacje wiedzy i wnioskowanie w warunkach niepewności.

1. reprezentacja wiedzy (logiki, grafów, drzew, reguł.)
2. Logiczna reprezentacja wiedzy - sposób reprezentacji wiedzy w postaci formuł logicznych. (o różnych rzędach)
3. rzędy (zerowy, 1, 2, wyższe)
4. formuła logiczna - ( prosta(atomowa), złożona)
5. zdanie logiczne - daje wynik 1/0
6. systemy ekpertowe.
7. ZA, ZD, ZPD
8. Wnioskowanie w war. niepewności - decyzje gdy brakuje dolkadnych danych lub sa niepewne.
9. teoria bayesa, logika rozmyta


## algorytmy sztucznej inteligencji
modele, algorytmy i narzędzia służące do formułowania i rozwiązywania trudnych problemów, wymagających wiedzy i inteligencji

Algorytmy sztucznej inteligencji:

1. Skupiają się na symulowaniu ludzkiego rozumowania i uczenia się.
2. Wykorzystują techniki takie jak uczenie maszynowe, głębokie uczenie, sieci neuronowe.
3. Stosowane w rozpoznawaniu wzorców, przetwarzaniu języka naturalnego, robotyce.
4. Uczą się z danych, dostosowując swoje działania do nowych informacji.

typy: 

1. Uczenie nadzorowane: Algorytmy uczące się na podstawie etykietowanych danych.
2. Uczenie nienadzorowane: Analiza i klasteryzacja danych bez uprzednich etykiet.
3. Uczenie ze wzmocnieniem: Algorytmy uczące się poprzez interakcję z otoczeniem i otrzymywanie nagród.
4. Sieci neuronowe: Symulacja procesów mózgu, stosowana w głębokim uczeniu.
5. Algorytmy ewolucyjne: Naśladują procesy ewolucyjne do optymalizacji i rozwiązywania problemów.

## [10. Obliczenia miękkie, systemy niepewne. ](https://docs.google.com/document/d/1rC8y8PmERfAr4ZLPY1JeiOymnQPmSi06ohv6GTbu5rE/edit#heading=h.u0218rc8n0r1)

1. zbior rozmyty, funkcja przynaleznosci, operacje na zbiorach rozmytych    
2. Obliczenia miekkie, definicja, skladniki, zastosowania
3. Systemy niepewne definicja, zastosowania
4. niepewnosc Epistemiczna, Stochastyczna
5. metody radzenia z niepewnoscia
6. 
### [11. Modele chmur i mgieł obliczeniowych. Rozwiązania hybrydowe. ](https://docs.google.com/document/d/1rC8y8PmERfAr4ZLPY1JeiOymnQPmSi06ohv6GTbu5rE/edit#heading=h.kistf3nqciy0)

1. Definicja, zastosowania
2. Infrastructure as a Service (IaaS), Platform as a Service (PaaS), Software as a Service (SaaS), Function as a Service (FaaS)
3. mgła obliczeniowa: charakterystyka, zastosowania
4. Mist Computing, Fog Computing, Edge Computing

### 13. Systemy rozproszone i wirtualne. 

1. system rozproszony: Współdzielenie zasobów , Przetwarzanie równoczesne, Skalowalność, Transparentność
2.  system scentralizowany a system rozproszonego
3. rodzaje: Klient-serwer,Architektura wielopoziomowa, architektura peer-to-peer, System wirtualny
4. systemy wirtualne:  Hypervisor, VM
5. Wirtualizacja pelna, na poziomie systemu operacyjnego
###  Definicje i własności grafów. Modele grafowe.

1. wierzchołek (węzeł), krawędź, stopień wierzchołka, bliskość, droga, droga prosta, ścieżka, cykl, droga acykliczna, najkrótsza ścieżka, drzewo
2. las, drzewo rozpinające, droga zamknięta, most, pętla, rząd (stopien) grafu, rozmiar grafu, srednica grafu, spójna składowa, k-spojny, graf r-regularny, macierz sąsiedztwa, macierz incydencji
3. Drzewo Spójny graf acyklicznyGraf acykliczny (skierowany)acyklicznyGraf cykliczny (skierowany)Graf dwudzielnyGraf pełnyGraf planarnyGraf prosty Graf spójnyKoło