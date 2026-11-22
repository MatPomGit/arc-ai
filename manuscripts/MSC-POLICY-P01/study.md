# MSC-POLICY-P01 — Kosztowo kalibrowana abstencja w systemach asystujących: XR, AAL i symulowane HRI

**Program:** `arc-ai` · **obszar:** `portable-uncertainty-abstention` · **rodzaj:** `IDEA` · **etap źródłowy:** `NEW_CROSS_DOMAIN_IDEA_HOLD`.

## Projekt badania

**Przedmiot:** Kosztowo kalibrowana abstencja w systemach asystujących: XR, AAL i symulowane HRI.

- **Proponowany wynik główny:** Nie określono dotychczas w rejestrze. Należy zdefiniować estymand, miarę i jednostkę analizy przed akwizycją.
- **Zakres i odrębność:** Wymaga odrębnego przeglądu nowości i porównania ze źródłowym protokołem.
- **Metodologia:** hipotezy, dobór próby lub scenariuszy, kryteria jakości, plan statystyczny i analiza wrażliwości wymagają potwierdzenia we właściwym projekcie. Ten plik nie potwierdza uzyskania wyników.
- **Powiązane MSC:** `MSC-AFFECT-P06`, `MSC-AR-P17`, `MSC-AR-P25`, `MSC-AAL-P04`, `MSC-HRI-P07`.

## Stanowisko badawcze

**`ST-00`**. Klasyfikacja `PROPOSED_BY_SCOPE`; kwalifikacja aparatury `NOT_VERIFIED`. Jest to propozycja organizacyjna, nie dowód gotowości stanowiska.

## Aplikacje

- **`app-hri-console`** (`APP-ARC-08`): rola `OPTIONAL`, decyzja `RESEARCH_GO`; status repozytorium `PLANNED_NOT_CREATED`.
- **`app-carehome`** (`APP-ARC-09`): rola `OPTIONAL`, decyzja `RESEARCH_GO`; status repozytorium `PLANNED_NOT_CREATED`.

## Biblioteki

- **`lib-adapt`**: status `PLANNED_NOT_CREATED`, proponowana zależność przez `app-carehome`. Brak potwierdzonej integracji.
- **`lib-audio`**: status `SCOPE_CONSOLIDATED_PLAN`, proponowana zależność przez `app-hri-console`. Brak potwierdzonej integracji.
- **`lib-events`**: status `PLANNED_NOT_CREATED`, proponowana zależność przez `app-hri-console`, `app-carehome`. Brak potwierdzonej integracji.
- **`lib-ros`**: status `SCAFFOLD_EXISTS`, proponowana zależność przez `app-hri-console`. Brak potwierdzonej integracji.
- **`lib-sim`**: status `PLANNED_NOT_CREATED`, proponowana zależność przez `app-hri-console`, `app-carehome`. Brak potwierdzonej integracji.
- **`lib-track`**: status `NEW_SCAFFOLD_EXISTS`, proponowana zależność przez `app-hri-console`. Brak potwierdzonej integracji.
- **`lib-vis`**: status `RENAMED_ARCHITECTURE_ONLY`, proponowana zależność przez `app-hri-console`. Brak potwierdzonej integracji.
- **`lib-vlm`**: status `SCAFFOLD_EXISTS`, proponowana zależność przez `app-hri-console`, `app-carehome`. Brak potwierdzonej integracji.

## Proweniencja i warunki realizacji

Szczegółowa proweniencja materiałów źródłowych, odwołania do repozytoriów niepublicznych i numery rewizji są przechowywane poza publiczną kartą.

Przed wykonaniem badania należy sprawdzić prawa do danych, kompletność protokołu, zgodę etyczną (jeżeli dotyczy), bezpieczeństwo aparatury oraz niezależność wyniku wobec innych manuskryptów. Wpisy biblioteczne i aplikacyjne są **planem**, nie deklaracją działającego API. Brak wyników oznacza `NOT_VERIFIED`, a nie wynik zerowy.
