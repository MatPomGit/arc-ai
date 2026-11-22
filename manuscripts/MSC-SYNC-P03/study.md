# MSC-SYNC-P03 — Wiek telemetrii ROS 2 a błędy aktualności decyzji bezpieczeństwa humanoida

**Program:** `arc-ai` · **obszar:** `multimodal-temporal-alignment` · **rodzaj:** `IDEA` · **etap źródłowy:** `IDEA_REVIEW`.

## Projekt badania

**Przedmiot:** Wiek telemetrii ROS 2 a błędy aktualności decyzji bezpieczeństwa humanoida.

- **Proponowany wynik główny:** Odsetek decyzji podejmowanych na nieaktualnych danych oraz rozkład data age
- **Zakres i odrębność:** Wyłącznie HRI i strumienie sensorów humanoida; nie ogólny algorytm synchronizacji dla każdej modalności.
- **Metodologia:** hipotezy, dobór próby lub scenariuszy, kryteria jakości, plan statystyczny i analiza wrażliwości wymagają potwierdzenia we właściwym projekcie. Ten plik nie potwierdza uzyskania wyników.
- **Powiązane MSC:** `MSC-SYNC-P04`, `MSC-SYNC-P01`, `MSC-SYNC-P02`.

## Stanowisko badawcze

**`ST-00`**. Klasyfikacja `PROPOSED_BY_SCOPE`; kwalifikacja aparatury `NOT_VERIFIED`. Jest to propozycja organizacyjna, nie dowód gotowości stanowiska.

## Aplikacje

- **`app-hri-console`** (`APP-ARC-08`): rola `OPTIONAL`, decyzja `RESEARCH_GO`; status repozytorium `PLANNED_NOT_CREATED`.

## Biblioteki

- **`lib-audio`**: status `SCOPE_CONSOLIDATED_PLAN`, proponowana zależność przez `app-hri-console`. Brak potwierdzonej integracji.
- **`lib-events`**: status `PLANNED_NOT_CREATED`, proponowana zależność przez `app-hri-console`. Brak potwierdzonej integracji.
- **`lib-ros`**: status `SCAFFOLD_EXISTS`, proponowana zależność przez `app-hri-console`. Brak potwierdzonej integracji.
- **`lib-sim`**: status `PLANNED_NOT_CREATED`, proponowana zależność przez `app-hri-console`. Brak potwierdzonej integracji.
- **`lib-track`**: status `NEW_SCAFFOLD_EXISTS`, proponowana zależność przez `app-hri-console`. Brak potwierdzonej integracji.
- **`lib-vis`**: status `RENAMED_ARCHITECTURE_ONLY`, proponowana zależność przez `app-hri-console`. Brak potwierdzonej integracji.
- **`lib-vlm`**: status `SCAFFOLD_EXISTS`, proponowana zależność przez `app-hri-console`. Brak potwierdzonej integracji.

## Proweniencja i warunki realizacji

Szczegółowa proweniencja materiałów źródłowych, odwołania do repozytoriów niepublicznych i numery rewizji są przechowywane poza publiczną kartą.

Przed wykonaniem badania należy sprawdzić prawa do danych, kompletność protokołu, zgodę etyczną (jeżeli dotyczy), bezpieczeństwo aparatury oraz niezależność wyniku wobec innych manuskryptów. Wpisy biblioteczne i aplikacyjne są **planem**, nie deklaracją działającego API. Brak wyników oznacza `NOT_VERIFIED`, a nie wynik zerowy.
