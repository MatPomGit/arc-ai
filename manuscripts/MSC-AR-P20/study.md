# MSC-AR-P20 — plan badania i powiązania

**Temat:** Kontrfaktyczna wartość interwencji XR przy kontrolowanej dostępności logów

**Program:** `arc-ai`. **Obszar:** `counterfactual-adaptation`. **Typ:** `IDEA` (CANDIDATE). **Stan źródła:** `IDEA_UNREVIEWED`. **Tryb integracji:** `INDEX_ONLY_NO_NEW_FOLDER`.

## Cel, wynik główny i granice badania

Przedmiot badania: Kontrfaktyczna wartość interwencji XR przy kontrolowanej dostępności logów. Kandydatura, bez zatwierdzonego odrębnego protokołu.

- **Główny wynik proponowany:** Błąd oceny wartości alternatywnej polityki w scenariuszach z pełną obserwacją
- **Odrębność naukowa:** Działanie polityk XR przy kompletnych logach; AI-IDEA-01 bada odrębnie braki pomiaru wywołane interwencją.
- **Uzasadnienie klasyfikacji:** Metodyczna estymacja kontrfaktyczna i niepewność policy evaluation. XR jako środowisko oceny. AUDYT DUPLIKACJI: sprawdzić, czy po uwzględnieniu selekcji obserwacji temat nie stanie się tym samym pytaniem co AI-IDEA-01. | Proponowane doprecyzowanie zakresu portfolio 2026-11-20, wymaga zatwierdzenia naukowego: Działanie polityk XR przy kompletnych logach; AI-IDEA-01 bada odrębnie braki pomiaru wywołane interwencją. Główny wynik do prerejestracji: Błąd oceny wartości alternatywnej polityki w scenariuszach z pełną obserwacją. Tytuł źródłowy zachowano w original_title_pl.
- **Powiązane rekordy:** `MSC-POLICY-P02` (arc-ai:AI-IDEA-01)

## Stanowisko badawcze

**Wstępne powiązanie:** `ST-03`. To propozycja na podstawie domeny, a nie potwierdzenie uruchomienia aparatury.

[Stanowiska ARC](https://github.com/MatPomGit/research-autopilot/blob/main/docs/portfolio/reorganizacja-systemu-badan/shared_research_platforms.md); [inwentarz prywatny `devices`](https://github.com/MatPomGit/devices).

## Powiązane aplikacje APP

- `app-xr` (`APP-ARC-07`), `OPTIONAL`, profil `unity-openxr`, bramka `RESEARCH_GO`.

## Powiązane biblioteki LIB

- `lib-asr`: planowana zależność pośrednia przez `app-xr`; brak dowodu integracji.
- `lib-events`: planowana zależność pośrednia przez `app-xr`; brak dowodu integracji.
- `lib-image` (historyczna nazwa; wymaga uzgodnienia z `lib-vis`): planowana zależność pośrednia przez `app-xr`; brak dowodu integracji.
- `lib-unity`: planowana zależność pośrednia przez `app-xr`; brak dowodu integracji.
- `lib-vlm`: planowana zależność pośrednia przez `app-xr`; brak dowodu integracji.
- `lib-voice`: planowana zależność pośrednia przez `app-xr`; brak dowodu integracji.
- `OptiCore`: planowana zależność pośrednia przez `app-xr`; brak dowodu integracji.

Relacje APP i LIB pochodzą odpowiednio z `app_publication_links.csv` i `component_dependencies.csv`. Są kandydaturami, nie dowodami wykonania prac. Aktualność nazw `lib-signals`, `lib-image` i `lib-llm` wymaga osobnego uzgodnienia z nowymi repozytoriami.

## Proweniencja, metodologia i bramki

- **UID źródłowy:** `arc-xr:XR-IDEA-14`; repozytorium `MatPomGit/arc-xr`, identyfikator `XR-IDEA-14`.
- **Ścieżka źródłowa:** `docs/pomysly.md`.
- **Materiał:** [źródło projektu](https://github.com/MatPomGit/arc-xr/blob/main/docs/pomysly.md).
- **Rejestr MSC:** [kanoniczna macierz](https://github.com/MatPomGit/research-autopilot/blob/main/docs/portfolio/reorganizacja-systemu-badan/publication_matrix.csv).

Przed badaniem wymagane są niezależny wynik i plan analizy, źródła literaturowe, ocena nowości, kontrola praw do danych/oprogramowania, ocena bezpieczeństwa i kwalifikacja etyczna, jeżeli dotyczy. Szkic nie zawiera danych empirycznych ani nie potwierdza dostępności stanowiska.
