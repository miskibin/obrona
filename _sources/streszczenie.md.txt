# streszczenie

## Pojęcie algorytmu; typy, własności i przykłady algorytmów. ✅

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
1. Każde odpalenie symulacji odbywa się dla innych realizacji zmiennych losowych.
2. Dla 2 uruchomień sym. Zmienne $y_p$ są niezależne, ale pochodzą z tego samego rozkładu. ( $y_{p1}$ i $y_{p2}$) możemy określić średnią, wariancję i przedział ufności dla średniej.
3. trudność: *określenie kiedy model jest "rozgrzany"* 
4. Testy statystyczne, wizualizacje etc.

## [6 Pojęcie fuzji danych oraz główne obszary jej wykorzystania.](https://docs.google.com/document/d/1rC8y8PmERfAr4ZLPY1JeiOymnQPmSi06ohv6GTbu5rE/edit#heading=h.qq5zh8o6wqzs)

1. Są to metody umożliwiające łączenie i przetwarzanie danych z różnych źródeł
2. Etapy: porządkowanie i kojarzenie danych, działania korekcyjne, algorytm realizujący fuzję danych
3. typy: fuzja współpracy, współzawodnictwa, uzupełniająca
4. obszary wykorzystania: 
   - medycyna: diagnoza chorób, monitorowanie stanu zdrowia
   - rolnictwo: dane z satelitów, dronów i czujników terenowych do zarządzania zasobami wodnymi, nawożeniem, ochroną roślin
5. przykłady zastosowań: monitorowanie stanów mostów, optymalizacja tras w logistyce, wykrywanie pożarów lasów.


## 7. Metody estymacji parametrów systemów dynamicznych Estymacja zmiennych stanu. Liniowy i rozszerzony filtr Kalmana. 

1. Techniki wykorzystywane do oceny i przewidywania stanu dynamicznych systemów w czasie rzeczywistym.
2. zalozenia: wejscie i wyjscie dostepne pomiarowo, zaklucenia maja rozklad normalny, wektroy szumow i pomiarow sa niezalezne
3. filtr kalmana: Etapy: predykcja, korekcja
4. Typy: Liniowy i Rozszerzony dla systemów nieliniowych.
5. Obszary wykorzystania:
    - nawigacja i śledzenie: precyzyjne śledzenie pozycji i orientacji w przestrzeni,
    - robotyka: estymacja trajektorii ruchu robotów,
    - finanse: prognozowanie trendów rynkowych i ocena ryzyka.


## [8. Metody identyfikacji obiektów statycznych w warunkach probabilistycznych. Identyfikacja parametryczna i nieparametryczna.](https://docs.google.com/document/d/1rC8y8PmERfAr4ZLPY1JeiOymnQPmSi06ohv6GTbu5rE/edit#heading=h.qei58dcu7gr7) 

1. Monte carlo (losowo)
2. bayes
3. metody regresji (liniowa, wielomianowa, wykladnicza, logarytmiczna)
4. identyfikacja parametryczna: modele zdefiniowane przez określone parametry, np. model liniowy
5. id. nieparametryczna: modele niezdefiniowane przez parametry, np. sieci neuronowe. bardziej elastyczne, ale trudniejsze do interpretacji.


## 9. Analityczne metody optymalizacji z ograniczeniami. Numeryczne metody optymalizacji bez i z ograniczeniami. 
1. analityczne:  met. lagrangea, met. karusha-kahna-tuckera, met. podzialu i ograniczen
1. numeryczne:  Obliczeniowe podejście do problemu optymalizacji. Działają iteracyjnie
2. metody numeryczne:  algorytm genetyczny, algorytm wspinaczkowy – stochastyczny, symulowane wyżarzanie, algorytm mrówkowy, algorytm pszczeli, algorytm roju cząstek

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

## 14. ...

## 15. Sieci usług, sieci sensorowe, systemy Internetu rzeczy ? analiza wydajności, zarządzanie, bezpieczeństwo i zastosowania

1. Sys internetu rzeczy analiza wydajności
- prędkość internetu (5g)
- w 2020 25-50 mld urządzeń w sieci
- domy ze smart iot zuzywaja 14-22% mniej energii

2. Procesy zarządzania Iot: instalacja, konfiguracja, monitorowanie, aktualizacja, naprawa, utylizacja
3. technologie: Prot komunikacjyne eg. (mqqt), platforma zarządzania (AWS), narzędzia do analiz danych, firewalle/szyfrowanie danych.
4. Zastosowania: wearables, smart houses, pompy insulinowe, stacje metorologiczne etc.


## [16. Modele cyklu życia oprogramowania. Metody zbierania wymagań w projektowaniu systemów informatycznych.](https://docs.google.com/document/d/1rC8y8PmERfAr4ZLPY1JeiOymnQPmSi06ohv6GTbu5rE/edit#heading=h.knhu879ppg9x) 

- model kaskadowy: planowanie, analiza, projektowanie, implementacja, testowanie, konserwacja. Zaklada poprawnosc wyniku (nie wraca sie do poprzednich faz). Uzywany gdy wymagania sa jasne i niezmienne.
- model V: rozszerzenie modelu kaskadowego, które podkreśla znaczenie testowania. Fazy: wymagania uzytkowe, wymagania systemowe, projekt architektury, projekt szczegółowy, implementacja | test jednostkowy, test integracyjny, testowanie systemu i testy akceptacyjne. Uzywany gdy ryzyko jest wyższe i testowanie jest wazne.
- model szybkiego prototypownia: ten model polega na tworzeniu prototypów systemu w celu zrozumienia wymagań użytkowników i szybkiego uzyskania informacji zwrotnej. Fazy: identyfikacja wymagań, szybkie projektowanie, budowa prototypu, ewaluacja klienta, ulepszanie prototypu. Jest to iteracyjny proces, który kończy się, gdy klient jest zadowolony z prototypu.

- wymagania: ogólne, funkcjonalne, niefunkcjonalne, ograniczenia srodowiska systemu
- zbieranie wymagan: analiza istniejacych rozwian, kwestionariusze, demonstracja prototypow by zebrac opinie, wywiady.
- problemy przy zbieraniu wymagań: niejasne lub niekompletne wymagania od klienta, zmieniające się wymagania, trudności w komunikacji między zespołem a klientem, brak zrozumienia kontekstu biznesowego
  
## 17. Style interakcji człowiek-komputer. Continuum Miligrama (Środowisko Realne - Środowisko Wirtualne). Cechy wirtualnej rzeczywistości (VR). 

- interakcja człowiek komputer: sposób w jaki użytkownik komunikuje się z komputerem
- kluczowo modalny (np vim.)
- bezposredniej manipulacji, np upuszczanie plikow w eksploratorze (graficznie)
- lingwistyczny np siri
- NUI - naturalny interfejs użytkownika, np gesty, mowa, mimika
- wirtualna rzeczywistosc

## 18. Typy testów oprogramowania. Definicja i metody badania użyteczności. 

- testy: jednostkowe, integracyjne, systemowe, akceptacyjne, wydajności, bezpieczeństwa
- badanie uzytecznosci: ocena heurystyczna, testy uzytecznosci, badania partyzanckie

## [19. Specyfika przetwarzania operacyjnego (OLTP) oraz strategicznego (OLAP), proces eksploracji oraz prezentacji danych w systemach Business Intelligence. ](https://docs.google.com/document/d/1rC8y8PmERfAr4ZLPY1JeiOymnQPmSi06ohv6GTbu5rE/edit#heading=h.o47lmdsjttjn)

- OLTP: szybkie przetwarzanie transakcji bieżących
- OLAP: przetwarzanie danych historycznych, analiza danych, raportowanie
- eksploracja danych: odkrywanie ukrytych wzorców w danych (klastrowanie, odkrywanie asocjacji, wykrywanie zmian i odchyleń, odkrywanie klasyfikacji)
- prezentacja: Selekcja danych, Wizualizacja danych, Analiza danych, Prezentacja wyników (raporty, wykresy, tabele)

## 20 Proces i architektura hurtowni danych, wielowymiarowy model danych.
- hurtownia danych: zorienatowana na temat, nieulotna, zintegrowana, zroznicowana czasowo
- proces: ekstrakcja danych, transformacja danych, ładowanie danych
- architektura: warstwa prezentacji, warstwa integracji, warstwa magazynu danych
- model danych: wymiar, fakty, hierarchia, poziom agregacji
  - gwiazda: wymiary wokol faktu
  - platek śniegu: fakty w srodku, wymiary do wymiarow.
  - konstelacja: polaczone platki sniegu.

## 21. Zagrożenia i zarządzanie ryzykiem w procesie ochrony infrastruktury krytycznej oraz metody ochrony infrastruktury krytycznej

- **Infrastruktura krytyczna**: Systemy i usługi, których zakłócenie lub zniszczenie może mieć poważne konsekwencje dla funkcjonowania społeczeństwa i gospodarki.
- **Zagrożenia**: Klęski żywiołowe, wypadki, cyberataki, terroryzm.
- **Zarządzanie ryzykiem**: Analiza ryzyka, planowanie odpowiedzi, szkolenia i ćwiczenia.
- **Metody ochrony**: Bezpieczeństwo fizyczne (zapory, monitoring, kontrola dostępu), bezpieczeństwo cybernetyczne (firewalle, antywirusy, autentykacja), gotowość na sytuacje kryzysowe (plany awaryjne, szkolenia kryzysowe), odporność i redundancja (redundancja systemów, elastyczność operacyjna, zapasowe źródła zasilania).
 
## 22. Cykl życia przedsiębiorstwa
- Powstawanie Wzrost Dojrzałość Spadek Przekształcenie

## 23 Cele i funkcje zarządzania.
- cele: Osiągnięcie celów organizacji, Efektywne wykorzystanie zasobów i ludzi, tworzenie srodowiska pracy
- funkcje: Planowanie, Organizowanie, Zatrudnianie , Kontrolowanie, koordynowanie
  
## 24. Struktura organizacyjna - uwarunkowania i kierunki ewolucji. 

- **Definicja**: Struktura organizacyjna to zbiór reguł minimalizujących dowolność i nieprzewidywalność zachowań ludzi w organizacji. Wynika z konieczności podziału pracy.
- **Analiza budowy organizacji**: Składa się z ustalenia elementów organizacji, wielkości poszczególnych części, podstawy organizacyjnego zróżnicowania, relacji hierarchicznych między elementami organizacji.
- **Uwarunkowania struktury organizacji**: Czynniki wewnętrzne (cele i strategia organizacji, wielkość organizacji, technologia organizacji) i czynniki zewnętrzne (ekonomiczne warunki działania organizacji, cechy psychospołeczne, prawo i regulacje, konkurencja i otoczenie organizacji).
- **Współczesne struktury organizacji**: Zarządzanie kreujące wiedzę, lean management, organizacja skoncentrowana na procesach, organizacja ucząca się, organizacja wirtualna.
- **Kierunki ewolucji**: Nowe formy organizacyjne, wsparcie dla innowacyjności i elastyczności przedsiębiorstwa, zawężanie specjalizacji, wzrost pracy zespołowej, niska standaryzacja, ograniczanie formalizacji do minimum, rozwój struktury sieciowej.

## 25. Analiza popytu i podaży; rodzaje działalności gospodarczej; koszty w przedsiębiorstwie.

1. **Analiza popytu**: Bada wpływ różnych czynników na ilość żądanych dóbr przez konsumentów. Wzrost ceny zwykle zmniejsza popyt, a jego zmiana może wynikać ze zmian cen dóbr powiązanych, dochodów, gustów, czy zmian prawnych.
2. **Analiza podaży**: Ocenia, jak różne czynniki wpływają na ilość dóbr, które producenci mogą dostarczyć. Zwykle wzrost ceny zwiększa podaż, a jej zmiana może być efektem zmian w technologii, kosztach produkcji czy polityce państwa.
3. **Rodzaje działalności gospodarczej**: Obejmuje jednoosobową działalność, spółki cywilne, kapitałowe i osobowe. Wybór formy zależy od opodatkowania, rodzaju i rozmiaru działalności, kapitału, możliwości przekształceń oraz prowadzenia księgowości.
4. **Koszty w przedsiębiorstwie**: Koszt całkowity obejmuje wartość zużytych zasobów. Koszty stałe nie zależą od produkcji, zmienne rosną z produkcją. Koszt przeciętny to koszt na jednostkę produktu, a koszt krańcowy to koszt zwiększenia produkcji o jednostkę.

## [26. Prawne i podatkowe aspekty prowadzenia działalności gospodarczej. ](https://docs.google.com/document/d/1rC8y8PmERfAr4ZLPY1JeiOymnQPmSi06ohv6GTbu5rE/edit#heading=h.63objqhxecc)

1. spółki osobowe: spółka jawna, spółka partnerska, spółka komandytowa, spółka komandytowo-akcyjna
2. spółki kapitałowe: spółka z ograniczoną odpowiedzialnością, spółka akcyjna
3. Koncesja, zezwolenie
4. prawa: pracy, konsumenckie, handlowe
5. podatki pośrednie (vat, akcyza), pośrednie (dochodowy, od czynności cywilnoprawnych, od spadków i darowizn)


## 27. Inicjowanie i definiowanie projektów. Ocena wykonalności projektów. Analiza ryzyka projektów. Określanie struktury projektów. 

## 28. Planowanie przebiegu i zasobów projektu. Budżetowanie projektu. Sterowanie przebiegiem projektu. Organizacja zespołu projektowego.

## 1. Metody maszynowego uczenia się

1. **Definicja**: Zbiór technik pozwalających komputerom na uczenie się bez wyraźnego programowania.
2. Uczenie nadzorowane: regresje, sieci neuronowe, klasyfikacja, drzewa decyzyjne, algorytmy genetyczne.
3. Uczenie nienadzorowane: klasteryzacja, analiza skupień, metoda k średnich, PCA
4. Uczenie ze wzmocnieniem: uczenie przez interakcję z otoczeniem i otrzymywanie nagród.

## 2. Systemy wizyjne, metody przetwarzania obrazów. 

- podstawowe problemy: klasyfikacja, segmentacja, detekcja obieków, generowanie obrazów, redukcja wymiarów.
- metody:
  -  klasyfikacja (KNN, regresja logistyczna, HOG)
  - sieci głębokie (CNN, RNN, GAN)

## 3. Złożoność obliczeniowa. Algorytmy dokładne, aproksymacyjne i heurystyczne. 

- typy: czasowa, pamieciowa
- pesymistyczna, oczekiwana, optymistyczna
- klasy: stała, liniowa, logarytmiczna, liniowo-logarytmiczna, kwadratowa, wykładnicza, silnia
- klasy złożoności: łatwe(P), trudne(NP)
- algorytmy: dokładne, aproksymacyjne, heurystyczne
- jednostka czasowa: 1 operacja dominujaca.

## 4. [Niestacjonarność w strumieniach danych. Algorytmy detekcji zmian w strumieniach danych.](https://docs.google.com/document/d/1rC8y8PmERfAr4ZLPY1JeiOymnQPmSi06ohv6GTbu5rE/edit#heading=h.hm8e9r8ywjjh)


## [5. Koncepcja i zastosowania próbkowania oszczędnego.](https://docs.google.com/document/d/1rC8y8PmERfAr4ZLPY1JeiOymnQPmSi06ohv6GTbu5rE/edit#heading=h.vnoevyj8d0wk)

- metoda redukcji danych, która wybiera podzbiór danych do analizy, aby zmniejszyć rozmiar danych.
- częstotliwość nyquista: maksymalna częstotliwość składowych widmowych sygnału poddawanego procesowi próbkowania, które mogą zostać odtworzone z ciągu próbek bez zniekształceń
- zastosowania: - przetwarzanie obrazów, Internet Rzeczy, przetwarzanie video

## 6. Metody fuzji i asymilacji danych. (slabe opracowanie)

- poziomy: czujników, cech, decyzji, przestrzeni i czasu
- techniki: Komplementarne, redundantne, kooperatywne
- asymilacja danych: asymilacja zmiennej stanu, kalmana, danych wielkoskalowych
- procesy: sprawdzenie danych, uzgodnienie danych

## 7. Modelowanie i analiza sieci złożonych.
- Sieć = graf + dynamika = graf agentów   

## 8. Systemy autonomiczne. Problemy alokacji i sterowania w systemach wielorobotowych. Podejście scentralizowane i rozproszone. 

- alokacja zasobów w systemach wielorobotowych: rozkładanie zadań, rozkładanie energii.
- sterowanie wielorobotowe: koordynacja ruchu, komunikacja między robotami, rozpoznawanie zadań
- podejście scentralizowane: (jeden robot steruje wszystkimi) / rozproszone
-  

## [10. Obliczenia miękkie, systemy niepewne. ](https://docs.google.com/document/d/1rC8y8PmERfAr4ZLPY1JeiOymnQPmSi06ohv6GTbu5rE/edit#heading=h.u0218rc8n0r1)

1. zbior rozmyty, funkcja przynaleznosci, operacje na zbiorach rozmytych    
2. Obliczenia miekkie, definicja, składniki, zastosowania
3. Systemy niepewne definicja, zastosowania
4. niepewnosc Epistemiczna, Stochastyczna
5. metody radzenia z niepewnoscia

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

