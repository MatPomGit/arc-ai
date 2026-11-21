# MSC-AAL-P05 — plan badania i powiązania

**Temat:** Uczenie ciągłe indywidualnych rutyn ADL przy dryfie i brakach danych czujników

**Program:** `arc-ai`. **Obszar:** `continual-learning-adl`. **Typ:** `IDEA` (CANDIDATE). **Stan źródła:** `NEW_UNVERIFIED_IDEA`. **Tryb integracji:** `INDEX_ONLY_NO_NEW_FOLDER`.

## Cel, wynik główny i granice badania

Przedmiot badania: Uczenie ciągłe indywidualnych rutyn ADL przy dryfie i brakach danych czujników. Kandydatura, bez zatwierdzonego odrębnego protokołu.

- **Główny wynik proponowany:** Nieokreślony w rejestrze. Wymaga zdefiniowania metryki, estymandu i jednostki analizy przed rozpoczęciem badania.
- **Odrębność naukowa:** Należy porównać źródłowy protokół z pokrewnymi manuskryptami przed formalizacją hipotezy.
- **Uzasadnienie klasyfikacji:** Nowa propozycja z 2026-11-20. Główny wkład: adaptacja do zmiany rutyny i awarii sensorów; porównać static/naive/adaptive; wynik: fałszywe alarmy dziennie przy założonej czułości, dryf, utrata wcześniejszych wzorców. P03 pozostaje właścicielem podstawowej detekcji.
- **Powiązane rekordy:** `MSC-AAL-P03` (carehome-aal:AAL-P03)

## Stanowisko badawcze

**Wstępne powiązanie:** `ST-06`. To propozycja na podstawie domeny, a nie potwierdzenie uruchomienia aparatury.

[Stanowiska ARC](https://github.com/MatPomGit/research-autopilot/blob/main/docs/portfolio/reorganizacja-systemu-badan/shared_research_platforms.md); [inwentarz prywatny `devices`](https://github.com/MatPomGit/devices).

## Powiązane aplikacje APP

- `app-carehome` (`APP-ARC-09`), `OPTIONAL`, profil `aal-simulator`, bramka `RESEARCH_GO`.

## Powiązane biblioteki LIB

- `lib-adapt`: planowana zależność pośrednia przez `app-carehome`; brak dowodu integracji.
- `lib-events`: planowana zależność pośrednia przez `app-carehome`; brak dowodu integracji.
- `lib-llm` (historyczna nazwa; wymaga uzgodnienia z `lib-vlm`): planowana zależność pośrednia przez `app-carehome`; brak dowodu integracji.
- `lib-sim`: planowana zależność pośrednia przez `app-carehome`; brak dowodu integracji.
- `lib-vlm`: planowana zależność pośrednia przez `app-carehome`; brak dowodu integracji.

Relacje APP i LIB pochodzą odpowiednio z `app_publication_links.csv` i `component_dependencies.csv`. Są kandydaturami, nie dowodami wykonania prac. Aktualność nazw `lib-signals`, `lib-image` i `lib-llm` wymaga osobnego uzgodnienia z nowymi repozytoriami.

## Proweniencja, metodologia i bramki

- **UID źródłowy:** `carehome-aal:AAL-P05`; repozytorium `MatPomGit/research-autopilot`, identyfikator `AAL-P05`.
- **Ścieżka źródłowa:** `docs/portfolio/reorganizacja-systemu-badan/carehome_aal_concept.md`.
- **Materiał:** [źródło projektu](https://github.com/MatPomGit/research-autopilot/blob/24600e13ffd23c5ac25e7d9e288341ad4b8c5114/docs/portfolio/reorganizacja-systemu-badan/carehome_aal_concept.md).
- **Rejestr MSC:** [kanoniczna macierz](https://github.com/MatPomGit/research-autopilot/blob/main/docs/portfolio/reorganizacja-systemu-badan/publication_matrix.csv).

Przed badaniem wymagane są niezależny wynik i plan analizy, źródła literaturowe, ocena nowości, kontrola praw do danych/oprogramowania, ocena bezpieczeństwa i kwalifikacja etyczna, jeżeli dotyczy. Szkic nie zawiera danych empirycznych ani nie potwierdza dostępności stanowiska.
