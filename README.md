# workout-assistant
Asystant siłowni 

### Uruchamianie
Aktywuj wirtualne środowisko utworzone przez Poetry:
- `poetry shell`

Uruchom migracje bazy danych:
- `python manage.py makemigrations`
- `python manage.py migrate` 

Uruchom serwer deweloperski Django:
- `python manage.py runserver`

### Dodatkowe kroki

Utwórz aplikacje Django:
- `python manage.py startapp myapp`

Dodaj aplikacje do INSTALLED_APPS w pliku settings.py:
(nowe appki dodawać na końcu installed_apps)
- ```
  INSTALLED_APPS = [
    ...,
    'myapp',
  ]
  ```


### Kalendarz
- Widok kalendarza z zaznaczonymi dniami treningowymi
- Opcja dodania treningu
  - Dodanie cyklu treningów np. 3 dni treningowe, 1 dzień przerwy na cały miesiąc/rok
  - Dodanie pojedynczego treningu
- Opcja edycji treningu
- Opcja usunięcia treningu
- Opcja rozpoczęcia treningu: po kliknięciu w trening przenosi do zakładki Trening

### Trening
- Podział na trening i rozgrzewkę (low pyro)
- Widok listy ćwiczeń na dany trening pod nazwą ćwiczenia
  - Kafelki na które można kliknąć, zależnie od tego jak ustawiliśmy trening:
    - Pusty kafelek, gdzie wpisujemy ciężar x powtórzenia
    - Kafelki z wcześniej ustalonym ciężarem x powtórzeniami podczas planowania treningu
  - Kliknięcie w kafelek włącza minutnik wcześniej ustalonej przerwy
- Nad kafelkiem wyświetlają się wyniki z poprzedniego treningu
- Opcja dodania notatki do ćwiczenia

### Profil
- Informacje podstawowe:
  - Waga
  - Wiek
  - Wzrost
  - Płeć

### Historia
- Podzielona na treningi i ćwiczenia
  - Treningi:
    - Informacja o liczbie wykonanych treningów
    - Porównanie ilości treningów miesiąc do miesiąca, tydzień do tygodnia
    - Informacja o liczbie podniesionych kilogramów - miesiąc do miesiąca, tydzień do tygodnia
    - Lista wykonanych treningów
      - Po kliknięciu porównanie treningów z tej samej kategorii, jakaś lista mniej więcej jak w moich notatkach
  - Ćwiczenia:
    - Lista wykonanych ćwiczeń
      - Po kliknięciu porównanie wyników z danego ćwiczenia, może wykres

### Ustawienia


# Notatki

custom users:
- https://testdriven.io/blog/django-custom-user-model/

superuser:
- email: test@test.com
- hasło: test

user:
- email: testuser@test.com
- hasło: Pomidor123.

### ruff:
uruchamianie:
- `ruff check`

wprowadznie korekty:
- `check --fix`


# TODO

29.05
- home.html nie działało z tut poprawione 
- db.sqlite3 
- ruff.toml