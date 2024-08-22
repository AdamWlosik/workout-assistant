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
- Opcja edycji treningudocker-compose up -d --build
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


### type checking class
`if TYPE_CHECKING:
    from django.forms import EmailField`

### ruff:
uruchamianie:
- `ruff check`

wprowadznie korekty:
- `check --fix`

### makefile:

instalacja makefile na linux
- `sudo apt-get install make`

utworzenie pliku makefile w folderze na którym najczesciej pracuje

4 pierwsze linie zawsze default

wcięcie tab nie 4 spacje

### TODO my notes
- poprawić informacje o wymagach hasła bo niewidoczne czarne na czarnym
- dodać uzupełnianie profilu przy rejstracji
- przygotować dockerfile 
  - https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/ https://docs.djangoproject.com/en/5.0/howto/deployment/


# TODO

29.05
- home.html logout z użyciem post, login a href (get)
- db.sqlite3 w settingsach wskazaliśmy miejsce na win zamist na wsl
- ruff.toml ustawienia ruffa w puproject.toml

05.06
- users/managers.py pytanie o klase
- users/test.py
- users/models.py
- users/views.py
- trainings/models.py na razie dodalem TCH004 do ingnora bo bład sie powtarzał
- czy moge mieć tak templates, nie w apkach
- czy do makefile można dodać jakoś (dodawanie nazwy apki) python manage.py startapp ""

05.06 po poprawkach 
- users/test.py
- users/views.py, users/managers/py na razie dodalem TCH004 do ingnora bo bład sie powtarzał
- trainings/models.py
- settings.py
- czy moge mieć tak templates, nie w apkach
- czy do makefile można dodać jakoś (dodawanie nazwy apki) python manage.py startapp ""

12.06
- docker, czy przenosimy appke na dockera?
- trainings/models.py dodać możliwość wyboru kilku kategorii do treningu

20.06
- czy powinienem utworzyć osobna apke events
- templates/calendary_wiew.html linia 27 jak skorzystać z mojej clasy css 

27.06
- dodałem pobierania dnia z +, dnia który wybraliśmy w kalendarzy do formularza tworzenia eventu i zmergowałem do main

04.07
- calendary/views.py poprawki wdg ruffa do zaakceptowania zakomentowany wcześniejszy kod wraz z błędem z ruff

22.08
- problem z migracją, logi po zmienie z categories na categroy w trainings/models.py
- nie da się utworzyć treniengu w Trainings List