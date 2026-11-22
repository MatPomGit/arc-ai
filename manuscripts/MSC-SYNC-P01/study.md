# MSC-SYNC-P01 — Dryf zegarów smartfonu i EEG a dokładność czasowych miar samoregulacji

**Program:** `arc-ai` · **obszar:** `multimodal-temporal-alignment` · **rodzaj:** `IDEA` · **etap źródłowy:** `DEFER`.

## Projekt badania

**Przedmiot:** Dryf zegarów smartfonu i EEG a dokładność czasowych miar samoregulacji.

- **Proponowany wynik główny:** Bezwzględny błąd czasu zdarzeń i jego wpływ na czas recovery
- **Zakres i odrębność:** Zadania regulacyjne dziecka, synchronizacja smartfon–EEG; odrębnie od mobilnej okulografii i ROS 2.
- **Metodologia:** hipotezy, dobór próby lub scenariuszy, kryteria jakości, plan statystyczny i analiza wrażliwości wymagają potwierdzenia we właściwym projekcie. Ten plik nie potwierdza uzyskania wyników.
- **Powiązane MSC:** `MSC-SYNC-P04`, `MSC-SYNC-P02`, `MSC-SYNC-P03`.

## Stanowisko badawcze

**`ST-00`**. Klasyfikacja `PROPOSED_BY_SCOPE`; kwalifikacja aparatury `NOT_VERIFIED`. Jest to propozycja organizacyjna, nie dowód gotowości stanowiska.

## Aplikacje

- **`app-regulation-mobile`** (`APP-ARC-02`): rola `SIGNAL_SOURCE`, decyzja `RESEARCH_GO`; status repozytorium `PLANNED_NOT_CREATED`.
- **`app-eeg-neurolyze`** (`APP-ARC-03`): rola `SIGNAL_SOURCE`, decyzja `DEVICE_RIGHTS`; status repozytorium `ALTERNATE_EXISTING_APP`, istniejący odpowiednik `eeg-neurolyze`.

## Biblioteki

- **`lib-adapt`**: status `PLANNED_NOT_CREATED`, proponowana zależność przez `app-regulation-mobile`. Brak potwierdzonej integracji.
- **`lib-events`**: status `PLANNED_NOT_CREATED`, proponowana zależność przez `app-regulation-mobile`, `app-eeg-neurolyze`. Brak potwierdzonej integracji.
- **`lib-sig`**: status `RENAMED_PARTIAL_CORE`, proponowana zależność przez `app-eeg-neurolyze`. Brak potwierdzonej integracji.
- **`lib-sim`**: status `PLANNED_NOT_CREATED`, proponowana zależność przez `app-eeg-neurolyze`. Brak potwierdzonej integracji.

## Proweniencja i warunki realizacji

Szczegółowa proweniencja materiałów źródłowych, odwołania do repozytoriów niepublicznych i numery rewizji są przechowywane poza publiczną kartą.

Przed wykonaniem badania należy sprawdzić prawa do danych, kompletność protokołu, zgodę etyczną (jeżeli dotyczy), bezpieczeństwo aparatury oraz niezależność wyniku wobec innych manuskryptów. Wpisy biblioteczne i aplikacyjne są **planem**, nie deklaracją działającego API. Brak wyników oznacza `NOT_VERIFIED`, a nie wynik zerowy.
