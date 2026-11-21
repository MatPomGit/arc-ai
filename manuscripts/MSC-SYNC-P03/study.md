# MSC-SYNC-P03 — plan badania i powiązania

**Temat:** Wiek telemetrii ROS 2 a błędy aktualności decyzji bezpieczeństwa humanoida

**Program:** `arc-ai`. **Obszar:** `multimodal-temporal-alignment`. **Typ:** `IDEA` (CANDIDATE). **Stan źródła:** `IDEA_REVIEW`. **Tryb integracji:** `INDEX_ONLY_NO_NEW_FOLDER`.

## Cel, wynik główny i granice badania

Przedmiot badania: Wiek telemetrii ROS 2 a błędy aktualności decyzji bezpieczeństwa humanoida. Kandydatura, bez zatwierdzonego odrębnego protokołu.

- **Główny wynik proponowany:** Odsetek decyzji podejmowanych na nieaktualnych danych oraz rozkład data age
- **Odrębność naukowa:** Wyłącznie HRI i strumienie sensorów humanoida; nie ogólny algorytm synchronizacji dla każdej modalności.
- **Uzasadnienie klasyfikacji:** WŁĄCZYĆ do metod; bez kolejnego paperu o clock alignment. [Klasyfikacja portfolio 2026-11-20] Jeżeli powstanie odrębny wkład, będzie to ogólna metoda estymacji synchronizacji i niepewności multimodalnych zdarzeń, a nie specyficzna interwencja robotyczna; współdzielona z F-ADHD-02 i F-GAZE-02. Na razie tylko metoda pomocnicza, bez osobnego paperu. KLASTER SYNCHRONIZACJI: trzy źródłowe zapisy jednego potencjalnego artykułu; nie planować trzech manuskryptów. | Proponowane doprecyzowanie zakresu portfolio 2026-11-20, wymaga zatwierdzenia naukowego: Wyłącznie HRI i strumienie sensorów humanoida; nie ogólny algorytm synchronizacji dla każdej modaln
- **Powiązane rekordy:** `MSC-SYNC-P04` (arc-adhd-game:S01), `MSC-SYNC-P01` (arc-adhd-game:F-ADHD-02), `MSC-SYNC-P02` (arc-mobile-eyetracking:F-GAZE-02)

## Stanowisko badawcze

**Wstępne powiązanie:** `ST-00`. To propozycja na podstawie domeny, a nie potwierdzenie uruchomienia aparatury.

[Stanowiska ARC](https://github.com/MatPomGit/research-autopilot/blob/main/docs/portfolio/reorganizacja-systemu-badan/shared_research_platforms.md); [inwentarz prywatny `devices`](https://github.com/MatPomGit/devices).

## Powiązane aplikacje APP

- `app-hri-console` (`APP-ARC-08`), `OPTIONAL`, profil `ros2-replay`, bramka `RESEARCH_GO`.

## Powiązane biblioteki LIB

- `lib-asr`: planowana zależność pośrednia przez `app-hri-console`; brak dowodu integracji.
- `lib-audio`: planowana zależność pośrednia przez `app-hri-console`; brak dowodu integracji.
- `lib-events`: planowana zależność pośrednia przez `app-hri-console`; brak dowodu integracji.
- `lib-image` (historyczna nazwa; wymaga uzgodnienia z `lib-vis`): planowana zależność pośrednia przez `app-hri-console`; brak dowodu integracji.
- `lib-ros`: planowana zależność pośrednia przez `app-hri-console`; brak dowodu integracji.
- `lib-sim`: planowana zależność pośrednia przez `app-hri-console`; brak dowodu integracji.
- `lib-vlm`: planowana zależność pośrednia przez `app-hri-console`; brak dowodu integracji.

Relacje APP i LIB pochodzą odpowiednio z `app_publication_links.csv` i `component_dependencies.csv`. Są kandydaturami, nie dowodami wykonania prac. Aktualność nazw `lib-signals`, `lib-image` i `lib-llm` wymaga osobnego uzgodnienia z nowymi repozytoriami.

## Proweniencja, metodologia i bramki

- **UID źródłowy:** `arc-hri-safety:F-HRI-03`; repozytorium `MatPomGit/arc-hri-safety`, identyfikator `F-HRI-03`.
- **Ścieżka źródłowa:** `manuscripts/FUTURE_RESEARCH_PROPOSALS.md`.
- **Materiał:** [źródło projektu](https://github.com/MatPomGit/arc-hri-safety/blob/main/manuscripts/FUTURE_RESEARCH_PROPOSALS.md).
- **Rejestr MSC:** [kanoniczna macierz](https://github.com/MatPomGit/research-autopilot/blob/main/docs/portfolio/reorganizacja-systemu-badan/publication_matrix.csv).

Przed badaniem wymagane są niezależny wynik i plan analizy, źródła literaturowe, ocena nowości, kontrola praw do danych/oprogramowania, ocena bezpieczeństwa i kwalifikacja etyczna, jeżeli dotyczy. Szkic nie zawiera danych empirycznych ani nie potwierdza dostępności stanowiska.
