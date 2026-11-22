# MSC-SYNC-P02 — Niepewność opóźnienia kamery Android w synchronizacji spojrzenia ze zdarzeniami gry 2D

**Program:** `arc-ai` · **obszar:** `multimodal-temporal-alignment` · **rodzaj:** `IDEA` · **etap źródłowy:** `IDEA_HOLD`.

## Projekt badania

**Przedmiot:** Niepewność opóźnienia kamery Android w synchronizacji spojrzenia ze zdarzeniami gry 2D.

- **Proponowany wynik główny:** Błąd wyrównania czasowego zdarzeń spojrzenia względem bodźców gry
- **Zakres i odrębność:** Mobilna kamera i rejestr zdarzeń gry; nie badanie zegarów EEG ani bezpieczeństwa robota.
- **Metodologia:** hipotezy, dobór próby lub scenariuszy, kryteria jakości, plan statystyczny i analiza wrażliwości wymagają potwierdzenia we właściwym projekcie. Ten plik nie potwierdza uzyskania wyników.
- **Powiązane MSC:** `MSC-SYNC-P04`, `MSC-SYNC-P01`, `MSC-SYNC-P03`.

## Stanowisko badawcze

**`ST-00`**. Klasyfikacja `PROPOSED_BY_SCOPE`; kwalifikacja aparatury `NOT_VERIFIED`. Jest to propozycja organizacyjna, nie dowód gotowości stanowiska.

## Aplikacje

- **`app-eye-mobile`** (`APP-ARC-04`): rola `SIGNAL_SOURCE`, decyzja `CROSS_PLATFORM`; status repozytorium `PLANNED_NOT_CREATED`.

## Biblioteki

- **`lib-events`**: status `PLANNED_NOT_CREATED`, proponowana zależność przez `app-eye-mobile`. Brak potwierdzonej integracji.
- **`lib-eye`**: status `SCAFFOLD_EXISTS`, proponowana zależność przez `app-eye-mobile`. Brak potwierdzonej integracji.
- **`lib-vis`**: status `RENAMED_ARCHITECTURE_ONLY`, proponowana zależność przez `app-eye-mobile`. Brak potwierdzonej integracji.

## Proweniencja i warunki realizacji

Źródłowe materiały rozwija publiczny projekt [`arc-mobile-eyetracking`](https://github.com/MatPomGit/arc-mobile-eyetracking); oryginalny identyfikator `F-GAZE-02`.

Przed wykonaniem badania należy sprawdzić prawa do danych, kompletność protokołu, zgodę etyczną (jeżeli dotyczy), bezpieczeństwo aparatury oraz niezależność wyniku wobec innych manuskryptów. Wpisy biblioteczne i aplikacyjne są **planem**, nie deklaracją działającego API. Brak wyników oznacza `NOT_VERIFIED`, a nie wynik zerowy.
