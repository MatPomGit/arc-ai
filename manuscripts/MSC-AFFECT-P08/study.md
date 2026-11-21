# MSC-AFFECT-P08 — plan badania i powiązania

**Temat:** Niezawodne wnioskowanie multimodalne Edge przy selektywnym braku sensorów

**Program:** `arc-ai`. **Obszar:** `edge-inference`. **Typ:** `MANUSCRIPT` (MANUSCRIPT). **Stan źródła:** `DRAFT`. **Tryb integracji:** `LINK_ONLY`.

## Cel, wynik główny i granice badania

Przedmiot badania: Niezawodne wnioskowanie multimodalne Edge przy selektywnym braku sensorów. Istnieje ślad źródłowego manuskryptu; stan dowodów wymaga weryfikacji.

- **Główny wynik proponowany:** Trafność/latencja przy dropout oraz koszt planowania zadań na węźle edge
- **Odrębność naukowa:** Odporność i sterowanie zmiennym obciążeniem, nie tylko pomiar stałego kosztu RGB/LWIR.
- **Uzasadnienie klasyfikacji:** Istnieje szkic LaTeX, brak zmierzonego benchmarku fizycznego. | Proponowane doprecyzowanie zakresu portfolio 2026-11-20, wymaga zatwierdzenia naukowego: Odporność i sterowanie zmiennym obciążeniem, nie tylko pomiar stałego kosztu RGB/LWIR. Główny wynik do prerejestracji: Trafność/latencja przy dropout oraz koszt planowania zadań na węźle edge. Tytuł źródłowy zachowano w original_title_pl. Nie zmienia to zatwierdzonego tytułu manuskryptu źródłowego ani zamrożonego protokołu.
- **Powiązane rekordy:** Nie zarejestrowano.

## Stanowisko badawcze

**Wstępne powiązanie:** `ST-05`. To propozycja na podstawie domeny, a nie potwierdzenie uruchomienia aparatury.

[Stanowiska ARC](https://github.com/MatPomGit/research-autopilot/blob/main/docs/portfolio/reorganizacja-systemu-badan/shared_research_platforms.md); [inwentarz prywatny `devices`](https://github.com/MatPomGit/devices).

## Powiązane aplikacje APP

- `app-eeg-neurolyze` (`APP-ARC-03`), `SIGNAL_SOURCE`, profil `python-eeg`, bramka `DEVICE_RIGHTS`.
- `app-eye-desktop` (`APP-ARC-05`), `SIGNAL_SOURCE`, profil `desktop-webcam`, bramka `DEVICE_RIGHTS`.

## Powiązane biblioteki LIB

- `lib-events`: planowana zależność pośrednia przez `app-eeg-neurolyze`, `app-eye-desktop`; brak dowodu integracji.
- `lib-eye`: planowana zależność pośrednia przez `app-eye-desktop`; brak dowodu integracji.
- `lib-image` (historyczna nazwa; wymaga uzgodnienia z `lib-vis`): planowana zależność pośrednia przez `app-eye-desktop`; brak dowodu integracji.
- `lib-signals` (historyczna nazwa; wymaga uzgodnienia z `lib-sig`): planowana zależność pośrednia przez `app-eeg-neurolyze`; brak dowodu integracji.
- `lib-sim`: planowana zależność pośrednia przez `app-eeg-neurolyze`; brak dowodu integracji.

Relacje APP i LIB pochodzą odpowiednio z `app_publication_links.csv` i `component_dependencies.csv`. Są kandydaturami, nie dowodami wykonania prac. Aktualność nazw `lib-signals`, `lib-image` i `lib-llm` wymaga osobnego uzgodnienia z nowymi repozytoriami.

## Proweniencja, metodologia i bramki

- **UID źródłowy:** `arc-affective:P08`; repozytorium `MatPomGit/arc-affective`, identyfikator `P08`.
- **Ścieżka źródłowa:** `manuscripts/P08/plan.md`.
- **Materiał:** [źródło projektu](https://github.com/MatPomGit/arc-affective/blob/main/manuscripts/P08/plan.md).
- **Rejestr MSC:** [kanoniczna macierz](https://github.com/MatPomGit/research-autopilot/blob/main/docs/portfolio/reorganizacja-systemu-badan/publication_matrix.csv).

Przed badaniem wymagane są niezależny wynik i plan analizy, źródła literaturowe, ocena nowości, kontrola praw do danych/oprogramowania, ocena bezpieczeństwa i kwalifikacja etyczna, jeżeli dotyczy. Szkic nie zawiera danych empirycznych ani nie potwierdza dostępności stanowiska.
