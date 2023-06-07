# CURREX

Platforma pozwalająca na serię prostych operacji na walutach takich jak porównywarka walut. Aplikacja została stworzona z użyciem publicznego API
dostarczanego przez serwis https://v6.exchangerate-api.com.

## Prawa autorskie

Autorzy:

- Michał Piszczek
- Adam Burzyński

Projektu można używać zgodnie z warunkami licencji **MIT**

## Technologie

- Python
- Flask
- Bulma

## Specyfikacja wymagań

- ID
- Nazwa
- Opis
- Priorytet (1 – wymagane, 2 – przydatne, 3 – opcjonalne)

### Wymaganie funkcjonalne

1. **Kalkulator walutowy**
   - Opis: Funkcja pozwala użytkownikowi na przeliczenie wybranej ilości pieniędzy z jednej waluty na drugą.
   - Priorytet: 1
2. **Wyświetlenie kursu**
   - Opis: Funkcja pokazuje jaki jest aktualny kurs wybranej waluty w odniesieniu do wszystkich innych.
   - Priorytet: 1
3. **Wyświetlanie wykresów**
   - Opis: Razem z aktualnym kursem wyświetlany będzie wykres pokazujący wartości z poprzednich kilku dni.
   - Priorytet: 2
4. **Porównywanie więcej niż dwóch walut jednocześnie**
   - Opis: Dostępna będzie opcja dodania kilku dodatkowych walut do wyboru, by porównywać wiele różnych jednocześnie.
   - Priorytet: 3

### Wymagania niefunkcjonalne

1. **Kompatybilność**
   - Opis: Użytkownik ma możliwość korzystania z aplikacji zarówno na telefonie jak i komputerze. Aplikacja powinna być responsywna.
   - Priorytet: 1
2. **Kustomizacja**
   - Opis: Aplikacja będzie miała dostępne różne motywy kolorystyczne.
   - Priorytet: 3
