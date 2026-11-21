# MSC-SYNC-P01 — plan badania i powiązania

**Temat:** Dryf zegarów smartfonu i EEG a dokładność czasowych miar samoregulacji

**Program:** `arc-ai`. **Obszar:** `multimodal-temporal-alignment`. **Typ:** `IDEA` (CANDIDATE). **Stan źródła:** `DEFER`. **Tryb integracji:** `INDEX_ONLY_NO_NEW_FOLDER`.

## Cel, wynik główny i granice badania

Przedmiot badania: Dryf zegarów smartfonu i EEG a dokładność czasowych miar samoregulacji. Kandydatura, bez zatwierdzonego odrębnego protokołu.

- **Główny wynik proponowany:** Bezwzględny błąd czasu zdarzeń i jego wpływ na czas recovery
- **Odrębność naukowa:** Zadania regulacyjne dziecka, synchronizacja smartfon–EEG; odrębnie od mobilnej okulografii i ROS 2.
- **Uzasadnienie klasyfikacji:** Pomysł współdzielony, nie trzeci artykuł o tym samym problemie. [Klasyfikacja portfolio 2026-11-20] Wspólna międzyprojektowa idea algorytmiczna: estymacja i niepewność wyrównania zdarzeń Android/EEG/kamera/robot. To ten sam temat co F-GAZE-02 i F-HRI-03, nie trzy zatwierdzone publikacje; GO tylko po nowej metodzie i niezależnym benchmarku. KLASTER SYNCHRONIZACJI: trzy źródłowe zapisy jednego potencjalnego artykułu; nie planować trzech manuskryptów. | Proponowane doprecyzowanie zakresu portfolio 2026-11-20, wymaga zatwierdzenia naukowego: Zadania regulacyjne dziecka, synchronizacja smartfon–EEG; odrębnie od mobilnej okulografii i ROS 2. Główny
- **Powiązane rekordy:** `MSC-SYNC-P04` (arc-adhd-game:S01), `MSC-SYNC-P02` (arc-mobile-eyetracking:F-GAZE-02), `MSC-SYNC-P03` (arc-hri-safety:F-HRI-03)

## Stanowisko badawcze

**Wstępne powiązanie:** `ST-00`. To propozycja na podstawie domeny, a nie potwierdzenie uruchomienia aparatury.

[Stanowiska ARC](https://github.com/MatPomGit/research-autopilot/blob/main/docs/portfolio/reorganizacja-systemu-badan/shared_research_platforms.md); [inwentarz prywatny `devices`](https://github.com/MatPomGit/devices).

## Powiązane aplikacje APP

- `app-regulation-mobile` (`APP-ARC-02`), `SIGNAL_SOURCE`, profil `android-native`, bramka `RESEARCH_GO`.
- `app-eeg-neurolyze` (`APP-ARC-03`), `SIGNAL_SOURCE`, profil `python-eeg`, bramka `DEVICE_RIGHTS`.

## Powiązane biblioteki LIB

- `lib-adapt`: planowana zależność pośrednia przez `app-regulation-mobile`; brak dowodu integracji.
- `lib-events`: planowana zależność pośrednia przez `app-regulation-mobile`, `app-eeg-neurolyze`; brak dowodu integracji.
- `lib-signals` (historyczna nazwa; wymaga uzgodnienia z `lib-sig`): planowana zależność pośrednia przez `app-eeg-neurolyze`; brak dowodu integracji.
- `lib-sim`: planowana zależność pośrednia przez `app-eeg-neurolyze`; brak dowodu integracji.

Relacje APP i LIB pochodzą odpowiednio z `app_publication_links.csv` i `component_dependencies.csv`. Są kandydaturami, nie dowodami wykonania prac. Aktualność nazw `lib-signals`, `lib-image` i `lib-llm` wymaga osobnego uzgodnienia z nowymi repozytoriami.

## Proweniencja, metodologia i bramki

- **UID źródłowy:** `arc-adhd-game:F-ADHD-02`; repozytorium `MatPomGit/arc-adhd-game`, identyfikator `F-ADHD-02`.
- **Ścieżka źródłowa:** `manuscripts/FUTURE_RESEARCH_PROPOSALS.md`.
- **Materiał:** [źródło projektu](https://github.com/MatPomGit/arc-adhd-game/blob/main/manuscripts/FUTURE_RESEARCH_PROPOSALS.md).
- **Rejestr MSC:** [kanoniczna macierz](https://github.com/MatPomGit/research-autopilot/blob/main/docs/portfolio/reorganizacja-systemu-badan/publication_matrix.csv).

Przed badaniem wymagane są niezależny wynik i plan analizy, źródła literaturowe, ocena nowości, kontrola praw do danych/oprogramowania, ocena bezpieczeństwa i kwalifikacja etyczna, jeżeli dotyczy. Szkic nie zawiera danych empirycznych ani nie potwierdza dostępności stanowiska.
