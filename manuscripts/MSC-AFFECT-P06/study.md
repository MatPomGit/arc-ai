# MSC-AFFECT-P06 — Zamkniętopętlowy kontroler adaptacyjnej gry z bramkowaniem niepewności

**Program:** `arc-ai` · **obszar:** `adaptive-control` · **rodzaj:** `MANUSCRIPT` · **etap źródłowy:** `PLANNED`.

## Projekt badania

**Przedmiot:** Zamkniętopętlowy kontroler adaptacyjnej gry z bramkowaniem niepewności.

- **Proponowany wynik główny:** Nie określono dotychczas w rejestrze. Należy zdefiniować estymand, miarę i jednostkę analizy przed akwizycją.
- **Zakres i odrębność:** Wymaga odrębnego przeglądu nowości i porównania ze źródłowym protokołem.
- **Metodologia:** hipotezy, dobór próby lub scenariuszy, kryteria jakości, plan statystyczny i analiza wrażliwości wymagają potwierdzenia we właściwym projekcie. Ten plik nie potwierdza uzyskania wyników.
- **Powiązane MSC:** brak jawnego powiązania w rejestrze.

## Stanowisko badawcze

**`ST-03`**. Klasyfikacja `PROPOSED_BY_SCOPE`; kwalifikacja aparatury `NOT_VERIFIED`. Jest to propozycja organizacyjna, nie dowód gotowości stanowiska.

## Aplikacje

- **`app-2d-desktop`** (`APP-ARC-01D`): rola `OPTIONAL`, decyzja `RESEARCH_GO`; status repozytorium `PLANNED_NOT_CREATED`.
- **`app-regulation-mobile`** (`APP-ARC-02`): rola `OPTIONAL`, decyzja `RESEARCH_GO`; status repozytorium `PLANNED_NOT_CREATED`.

## Biblioteki

- **`lib-adapt`**: status `PLANNED_NOT_CREATED`, proponowana zależność przez `app-regulation-mobile`. Brak potwierdzonej integracji.
- **`lib-events`**: status `PLANNED_NOT_CREATED`, proponowana zależność przez `app-2d-desktop`, `app-regulation-mobile`. Brak potwierdzonej integracji.
- **`lib-eye`**: status `SCAFFOLD_EXISTS`, proponowana zależność przez `app-2d-desktop`. Brak potwierdzonej integracji.
- **`lib-study`**: status `PLANNED_NOT_CREATED`, proponowana zależność przez `app-2d-desktop`. Brak potwierdzonej integracji.
- **`lib-vis`**: status `RENAMED_ARCHITECTURE_ONLY`, proponowana zależność przez `app-2d-desktop`. Brak potwierdzonej integracji.

## Proweniencja i warunki realizacji

Źródłowe materiały rozwija publiczny projekt [`arc-affective`](https://github.com/MatPomGit/arc-affective); oryginalny identyfikator `P06`.

Przed wykonaniem badania należy sprawdzić prawa do danych, kompletność protokołu, zgodę etyczną (jeżeli dotyczy), bezpieczeństwo aparatury oraz niezależność wyniku wobec innych manuskryptów. Wpisy biblioteczne i aplikacyjne są **planem**, nie deklaracją działającego API. Brak wyników oznacza `NOT_VERIFIED`, a nie wynik zerowy.
