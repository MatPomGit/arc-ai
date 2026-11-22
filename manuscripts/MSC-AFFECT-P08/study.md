# MSC-AFFECT-P08 — Niezawodne wnioskowanie multimodalne Edge przy selektywnym braku sensorów

**Program:** `arc-ai` · **obszar:** `edge-inference` · **rodzaj:** `MANUSCRIPT` · **etap źródłowy:** `DRAFT`.

## Projekt badania

**Przedmiot:** Niezawodne wnioskowanie multimodalne Edge przy selektywnym braku sensorów.

- **Proponowany wynik główny:** Trafność/latencja przy dropout oraz koszt planowania zadań na węźle edge
- **Zakres i odrębność:** Odporność i sterowanie zmiennym obciążeniem, nie tylko pomiar stałego kosztu RGB/LWIR.
- **Metodologia:** hipotezy, dobór próby lub scenariuszy, kryteria jakości, plan statystyczny i analiza wrażliwości wymagają potwierdzenia we właściwym projekcie. Ten plik nie potwierdza uzyskania wyników.
- **Powiązane MSC:** brak jawnego powiązania w rejestrze.

## Stanowisko badawcze

**`ST-05`**. Klasyfikacja `PROPOSED_BY_SCOPE`; kwalifikacja aparatury `NOT_VERIFIED`. Jest to propozycja organizacyjna, nie dowód gotowości stanowiska.

## Aplikacje

- **`app-eeg-neurolyze`** (`APP-ARC-03`): rola `SIGNAL_SOURCE`, decyzja `DEVICE_RIGHTS`; status repozytorium `ALTERNATE_EXISTING_APP`, istniejący odpowiednik `eeg-neurolyze`.
- **`app-eye-desktop`** (`APP-ARC-05`): rola `SIGNAL_SOURCE`, decyzja `DEVICE_RIGHTS`; status repozytorium `PLANNED_NOT_CREATED`.

## Biblioteki

- **`lib-events`**: status `PLANNED_NOT_CREATED`, proponowana zależność przez `app-eeg-neurolyze`, `app-eye-desktop`. Brak potwierdzonej integracji.
- **`lib-eye`**: status `SCAFFOLD_EXISTS`, proponowana zależność przez `app-eye-desktop`. Brak potwierdzonej integracji.
- **`lib-sig`**: status `RENAMED_PARTIAL_CORE`, proponowana zależność przez `app-eeg-neurolyze`. Brak potwierdzonej integracji.
- **`lib-sim`**: status `PLANNED_NOT_CREATED`, proponowana zależność przez `app-eeg-neurolyze`. Brak potwierdzonej integracji.
- **`lib-vis`**: status `RENAMED_ARCHITECTURE_ONLY`, proponowana zależność przez `app-eye-desktop`. Brak potwierdzonej integracji.

## Proweniencja i warunki realizacji

Źródłowe materiały rozwija publiczny projekt [`arc-affective`](https://github.com/MatPomGit/arc-affective); oryginalny identyfikator `P08`.

Przed wykonaniem badania należy sprawdzić prawa do danych, kompletność protokołu, zgodę etyczną (jeżeli dotyczy), bezpieczeństwo aparatury oraz niezależność wyniku wobec innych manuskryptów. Wpisy biblioteczne i aplikacyjne są **planem**, nie deklaracją działającego API. Brak wyników oznacza `NOT_VERIFIED`, a nie wynik zerowy.
