# MSC-AFFECT-P01 — Odporność niskokanałowych reprezentacji EEG na zmianę montażu i zbioru

**Program:** `arc-ai` · **obszar:** `eeg-representation` · **rodzaj:** `MANUSCRIPT` · **etap źródłowy:** `DRAFT`.

## Projekt badania

**Przedmiot:** Odporność niskokanałowych reprezentacji EEG na zmianę montażu i zbioru.

- **Proponowany wynik główny:** CCC Lina między predykcją a ciągłą oceną samoopisową walencji, liczony na poziomie pozostawionego poza treningiem uczestnika i jego prób. Roboczy kontrast: sparowany spadek CCC po redukcji elektrod względem pełnego montażu, przy identycznych próbach i kwalifikowalności. Dla stałych ocen walencji CCC raportuje się jako niezdefiniowany. Drugorzędowo MSE względem średniej treningowej. Decyzje nie są jeszcze zamrożone.
- **Zakres i odrębność:** proponowany wkład dotyczy identyfikowalności efektu redukcji kanałów przy zmianie montażu, referencji i domeny. Sama klasyfikacja emocji z EEG lub adaptacja domenowa nie stanowi nowości. Konieczny przegląd porównawczy względem aktualnych prac oraz replikacja baseline.
- **Metodologia:** ocena niezależna od uczestnika (zewnętrzne LOSO i wewnętrzna walidacja grupowa); pełny i z góry określony rzadki montaż; kontrola zgodności współrzędnych, referencji i semantyki ocen; modele średniej treningowej i ridge; permutacje etykiet wyłącznie w treningu oraz baseline bodźcowy. Oddzielne scenariusze nowych bodźców i nowych korpusów. Wnioskowanie populacyjne dopiero po wyborze metody uwzględniającej zależność nakładających się zbiorów treningowych.
- **Powiązane MSC:** brak jawnego powiązania w rejestrze.

## Stanowisko badawcze

**`ST-01`**. Klasyfikacja `PROPOSED_BY_SCOPE`; kwalifikacja aparatury `NOT_VERIFIED`. Jest to propozycja organizacyjna, nie dowód gotowości stanowiska.

## Aplikacje

- **`app-eeg-neurolyze`** (`APP-ARC-03`): rola `SIGNAL_SOURCE`, decyzja `DEVICE_RIGHTS`; status repozytorium `ALTERNATE_EXISTING_APP`, istniejący odpowiednik `eeg-neurolyze`.

## Biblioteki

- **`lib-events`**: status `PLANNED_NOT_CREATED`, proponowana zależność przez `app-eeg-neurolyze`. Brak potwierdzonej integracji.
- **`lib-sig`**: status `RENAMED_PARTIAL_CORE`, proponowana zależność przez `app-eeg-neurolyze`. Brak potwierdzonej integracji.
- **`lib-sim`**: status `PLANNED_NOT_CREATED`, proponowana zależność przez `app-eeg-neurolyze`. Brak potwierdzonej integracji.

## Proweniencja i warunki realizacji

Źródłowe materiały rozwija publiczny projekt [`arc-affective`](https://github.com/MatPomGit/arc-affective); oryginalny identyfikator `P01`.

Przed wykonaniem badania należy sprawdzić prawa do danych, kompletność protokołu, zgodę etyczną (jeżeli dotyczy), bezpieczeństwo aparatury oraz niezależność wyniku wobec innych manuskryptów. Wpisy biblioteczne i aplikacyjne są **planem**, nie deklaracją działającego API. Brak wyników oznacza `NOT_VERIFIED`, a nie wynik zerowy.
