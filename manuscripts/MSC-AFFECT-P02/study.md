# MSC-AFFECT-P02 — plan badania i powiązania

**Temat:** Fuzja afektu z kalibracją pewności przy awarii modalności

**Program:** `arc-ai`. **Obszar:** `representation-learning`. **Typ:** `MANUSCRIPT` (MANUSCRIPT). **Stan źródła:** `PLANNED`. **Tryb integracji:** `LINK_ONLY`.

## Cel, wynik główny i granice badania

Przedmiot badania: Fuzja afektu z kalibracją pewności przy awarii modalności. Istnieje ślad źródłowego manuskryptu; stan dowodów wymaga weryfikacji.

- **Główny wynik proponowany:** Nieokreślony w rejestrze. Wymaga zdefiniowania metryki, estymandu i jednostki analizy przed rozpoczęciem badania.
- **Odrębność naukowa:** Należy porównać źródłowy protokół z pokrewnymi manuskryptami przed formalizacją hipotezy.
- **Uzasadnienie klasyfikacji:** Klasyfikacja wg pytania badawczego: Nowa metoda odpornej na brakujące modalności kalibracji i fuzji modelu; klasyfikacja AI, nie kliniczny wynik afektu. Status źródła: PLANNED. Nie oznacza zatwierdzonych danych ani gotowości publikacji.
- **Powiązane rekordy:** Nie zarejestrowano.

## Stanowisko badawcze

**Wstępne powiązanie:** `ST-01`, `ST-02`. To propozycja na podstawie domeny, a nie potwierdzenie uruchomienia aparatury.

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

- **UID źródłowy:** `arc-affective:P02`; repozytorium `MatPomGit/arc-affective`, identyfikator `P02`.
- **Ścieżka źródłowa:** `manuscripts/P02/plan.md`.
- **Materiał:** [źródło projektu](https://github.com/MatPomGit/arc-affective/blob/main/manuscripts/P02/plan.md).
- **Rejestr MSC:** [kanoniczna macierz](https://github.com/MatPomGit/research-autopilot/blob/main/docs/portfolio/reorganizacja-systemu-badan/publication_matrix.csv).

Przed badaniem wymagane są niezależny wynik i plan analizy, źródła literaturowe, ocena nowości, kontrola praw do danych/oprogramowania, ocena bezpieczeństwa i kwalifikacja etyczna, jeżeli dotyczy. Szkic nie zawiera danych empirycznych ani nie potwierdza dostępności stanowiska.
