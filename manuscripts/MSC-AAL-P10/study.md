# MSC-AAL-P10 — plan badania i powiązania

**Temat:** Obserwowalność czynności ADL przy minimalnym zestawie czujników i ich awariach

**Program:** `arc-ai`. **Obszar:** `adl-observability-sensor-placement`. **Typ:** `IDEA` (CANDIDATE). **Stan źródła:** `NEW_CROSS_PROGRAM_IDEA_HOLD`. **Tryb integracji:** `INDEX_ONLY_NO_NEW_FOLDER`.

## Cel, wynik główny i granice badania

Przedmiot badania: Obserwowalność czynności ADL przy minimalnym zestawie czujników i ich awariach. Kandydatura, bez zatwierdzonego odrębnego protokołu.

- **Główny wynik proponowany:** Minimalna liczba sensorów przy gwarancji określonej identyfikowalności działań
- **Odrębność naukowa:** Dobór infrastruktury, nie klasyfikacja anomalii ani przypisanie osób.
- **Uzasadnienie klasyfikacji:** [Nowa propozycja burzy mózgów 2026-11-20, priorytet A] Porównać identyfikowalność zdarzeń przy ograniczaniu konfiguracji sensorów z jawnym brakiem rozróżnialności części trajektorii; FPR/sensitivity/czujniki i awaria jednego. Wymaga map sensorów i danych z etykietami; odrębne od P03 architektury detektora i P05 drift. Wkład i nowość niezatwierdzone; nie tworzyć manuskryptu przed audytem. Repozytorium programu ARC AI jeszcze nie istnieje: pełny opis w prywatnym źródle przejściowym. | Proponowane doprecyzowanie zakresu portfolio 2026-11-20, wymaga zatwierdzenia naukowego: Dobór infrastruktury, nie klasyfikacja anomalii ani przypisanie osób. Głó
- **Powiązane rekordy:** `MSC-AAL-P03` (carehome-aal:AAL-P03), `MSC-AAL-P05` (carehome-aal:AAL-P05)

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

- **UID źródłowy:** `arc-ai:AI-IDEA-03`; repozytorium `MatPomGit/research-autopilot`, identyfikator `AI-IDEA-03`.
- **Ścieżka źródłowa:** `docs/portfolio/reorganizacja-systemu-badan/arc_ai_research_proposals.md`.
- **Materiał:** [źródło projektu](https://github.com/MatPomGit/research-autopilot/blob/d8495d70fc73d275ae359e15942f542575faad40/docs/portfolio/reorganizacja-systemu-badan/arc_ai_research_proposals.md).
- **Rejestr MSC:** [kanoniczna macierz](https://github.com/MatPomGit/research-autopilot/blob/main/docs/portfolio/reorganizacja-systemu-badan/publication_matrix.csv).

Przed badaniem wymagane są niezależny wynik i plan analizy, źródła literaturowe, ocena nowości, kontrola praw do danych/oprogramowania, ocena bezpieczeństwa i kwalifikacja etyczna, jeżeli dotyczy. Szkic nie zawiera danych empirycznych ani nie potwierdza dostępności stanowiska.
