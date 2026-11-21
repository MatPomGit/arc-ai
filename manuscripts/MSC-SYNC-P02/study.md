# MSC-SYNC-P02 — plan badania i powiązania

**Temat:** Niepewność opóźnienia kamery Android w synchronizacji spojrzenia ze zdarzeniami gry 2D

**Program:** `arc-ai`. **Obszar:** `multimodal-temporal-alignment`. **Typ:** `IDEA` (CANDIDATE). **Stan źródła:** `IDEA_HOLD`. **Tryb integracji:** `INDEX_ONLY_NO_NEW_FOLDER`.

## Cel, wynik główny i granice badania

Przedmiot badania: Niepewność opóźnienia kamery Android w synchronizacji spojrzenia ze zdarzeniami gry 2D. Kandydatura, bez zatwierdzonego odrębnego protokołu.

- **Główny wynik proponowany:** Błąd wyrównania czasowego zdarzeń spojrzenia względem bodźców gry
- **Odrębność naukowa:** Mobilna kamera i rejestr zdarzeń gry; nie badanie zegarów EEG ani bezpieczeństwa robota.
- **Uzasadnienie klasyfikacji:** Wspólna metoda; nie mnożyć manuskryptów między programami. [Klasyfikacja portfolio 2026-11-20] Uogólniona metoda estymacji dryfu i niepewności znaczników czasu różnych modalności; wspólne z F-ADHD-02/F-HRI-03. Zachować IDEA_HOLD; nie mnożyć równoległych artykułów. KLASTER SYNCHRONIZACJI: trzy źródłowe zapisy jednego potencjalnego artykułu; nie planować trzech manuskryptów. | Proponowane doprecyzowanie zakresu portfolio 2026-11-20, wymaga zatwierdzenia naukowego: Mobilna kamera i rejestr zdarzeń gry; nie badanie zegarów EEG ani bezpieczeństwa robota. Główny wynik do prerejestracji: Błąd wyrównania czasowego zdarzeń spojrzenia względem bodźców 
- **Powiązane rekordy:** `MSC-SYNC-P04` (arc-adhd-game:S01), `MSC-SYNC-P01` (arc-adhd-game:F-ADHD-02), `MSC-SYNC-P03` (arc-hri-safety:F-HRI-03)

## Stanowisko badawcze

**Wstępne powiązanie:** `ST-00`. To propozycja na podstawie domeny, a nie potwierdzenie uruchomienia aparatury.

[Stanowiska ARC](https://github.com/MatPomGit/research-autopilot/blob/main/docs/portfolio/reorganizacja-systemu-badan/shared_research_platforms.md); [inwentarz prywatny `devices`](https://github.com/MatPomGit/devices).

## Powiązane aplikacje APP

- `app-eye-mobile` (`APP-ARC-04`), `SIGNAL_SOURCE`, profil `android-native`, bramka `CROSS_PLATFORM`.

## Powiązane biblioteki LIB

- `lib-events`: planowana zależność pośrednia przez `app-eye-mobile`; brak dowodu integracji.
- `lib-eye`: planowana zależność pośrednia przez `app-eye-mobile`; brak dowodu integracji.
- `lib-image` (historyczna nazwa; wymaga uzgodnienia z `lib-vis`): planowana zależność pośrednia przez `app-eye-mobile`; brak dowodu integracji.

Relacje APP i LIB pochodzą odpowiednio z `app_publication_links.csv` i `component_dependencies.csv`. Są kandydaturami, nie dowodami wykonania prac. Aktualność nazw `lib-signals`, `lib-image` i `lib-llm` wymaga osobnego uzgodnienia z nowymi repozytoriami.

## Proweniencja, metodologia i bramki

- **UID źródłowy:** `arc-mobile-eyetracking:F-GAZE-02`; repozytorium `MatPomGit/arc-mobile-eyetracking`, identyfikator `F-GAZE-02`.
- **Ścieżka źródłowa:** `manuscripts/FUTURE_RESEARCH_PROPOSALS.md`.
- **Materiał:** [źródło projektu](https://github.com/MatPomGit/arc-mobile-eyetracking/blob/main/manuscripts/FUTURE_RESEARCH_PROPOSALS.md).
- **Rejestr MSC:** [kanoniczna macierz](https://github.com/MatPomGit/research-autopilot/blob/main/docs/portfolio/reorganizacja-systemu-badan/publication_matrix.csv).

Przed badaniem wymagane są niezależny wynik i plan analizy, źródła literaturowe, ocena nowości, kontrola praw do danych/oprogramowania, ocena bezpieczeństwa i kwalifikacja etyczna, jeżeli dotyczy. Szkic nie zawiera danych empirycznych ani nie potwierdza dostępności stanowiska.
