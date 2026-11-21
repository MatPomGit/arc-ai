# MSC-AAL-P11 — plan badania i powiązania

**Temat:** Przypisanie aktywności konkretnemu mieszkańcowi przy nierozstrzygalności sygnałów ADL

**Program:** `arc-ai`. **Obszar:** `multi-resident-adl-identifiability`. **Typ:** `IDEA` (CANDIDATE). **Stan źródła:** `NEW_CROSS_PROGRAM_IDEA_HOLD`. **Tryb integracji:** `INDEX_ONLY_NO_NEW_FOLDER`.

## Cel, wynik główny i granice badania

Przedmiot badania: Przypisanie aktywności konkretnemu mieszkańcowi przy nierozstrzygalności sygnałów ADL. Kandydatura, bez zatwierdzonego odrębnego protokołu.

- **Główny wynik proponowany:** Ryzyko błędnego adresowania alertów przy selektywnej abstencji
- **Odrębność naukowa:** Atrybucja osoby, a nie obserwowalność aktywności przez zestaw czujników.
- **Uzasadnienie klasyfikacji:** [Nowa propozycja burzy mózgów 2026-11-20, priorytet B] Odrębny wynik: fałszywie zaadresowane osobnicze alarmy i selective coverage przy niepewności przypisania osoby, a nie sama rozpoznawalność aktywności. Publiczne dane CASAS wieloosobowe dopiero po audycie etykiet/licencji; rozbudowany prior art 2025–2026 wyklucza samo multi-resident classification jako nowość. Wkład i nowość niezatwierdzone; nie tworzyć manuskryptu przed audytem. Repozytorium programu ARC AI jeszcze nie istnieje: pełny opis w prywatnym źródle przejściowym. | Proponowane doprecyzowanie zakresu portfolio 2026-11-20, wymaga zatwierdzenia naukowego: Atrybucja osoby, a nie obse
- **Powiązane rekordy:** `MSC-AAL-P03` (carehome-aal:AAL-P03), `MSC-AAL-P05` (carehome-aal:AAL-P05), `MSC-POLICY-P01` (cross-arc:CROSS-ARC-01), `MSC-AAL-P10` (arc-ai:AI-IDEA-03)

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

- **UID źródłowy:** `arc-ai:AI-IDEA-05`; repozytorium `MatPomGit/research-autopilot`, identyfikator `AI-IDEA-05`.
- **Ścieżka źródłowa:** `docs/portfolio/reorganizacja-systemu-badan/arc_ai_research_proposals.md`.
- **Materiał:** [źródło projektu](https://github.com/MatPomGit/research-autopilot/blob/d8495d70fc73d275ae359e15942f542575faad40/docs/portfolio/reorganizacja-systemu-badan/arc_ai_research_proposals.md).
- **Rejestr MSC:** [kanoniczna macierz](https://github.com/MatPomGit/research-autopilot/blob/main/docs/portfolio/reorganizacja-systemu-badan/publication_matrix.csv).

Przed badaniem wymagane są niezależny wynik i plan analizy, źródła literaturowe, ocena nowości, kontrola praw do danych/oprogramowania, ocena bezpieczeństwa i kwalifikacja etyczna, jeżeli dotyczy. Szkic nie zawiera danych empirycznych ani nie potwierdza dostępności stanowiska.
