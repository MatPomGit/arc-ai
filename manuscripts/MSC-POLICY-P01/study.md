# MSC-POLICY-P01 — plan badania i powiązania

**Temat:** Kosztowo kalibrowana abstencja w systemach asystujących: XR, AAL i symulowane HRI

**Program:** `arc-ai`. **Obszar:** `portable-uncertainty-abstention`. **Typ:** `IDEA` (CANDIDATE). **Stan źródła:** `NEW_CROSS_DOMAIN_IDEA_HOLD`. **Tryb integracji:** `INDEX_ONLY_NO_NEW_FOLDER`.

## Cel, wynik główny i granice badania

Przedmiot badania: Kosztowo kalibrowana abstencja w systemach asystujących: XR, AAL i symulowane HRI. Kandydatura, bez zatwierdzonego odrębnego protokołu.

- **Główny wynik proponowany:** Nieokreślony w rejestrze. Wymaga zdefiniowania metryki, estymandu i jednostki analizy przed rozpoczęciem badania.
- **Odrębność naukowa:** Należy porównać źródłowy protokół z pokrewnymi manuskryptami przed formalizacją hipotezy.
- **Uzasadnienie klasyfikacji:** Nowy pomysł na przekrojowy algorytm z testem selektywnego ryzyka i kosztu błędnej interwencji; nie duplikować regulatora bezpieczeństwa M07 ani istniejących progów P06/AAL P04. Wymaga formalnej nowości i niezależnych testów wielodomenowych. Nie kontrolować robotów/domowych aktuatorów fizycznie.
- **Powiązane rekordy:** `MSC-AFFECT-P06` (arc-affective:P06), `MSC-AR-P17` (arc-xr:XR-IDEA-11), `MSC-AR-P25` (arc-xr:XR-IDEA-19), `MSC-AAL-P04` (carehome-aal:AAL-P04), `MSC-HRI-P07` (arc-hri-safety:M07)

## Stanowisko badawcze

**Wstępne powiązanie:** `ST-00`. To propozycja na podstawie domeny, a nie potwierdzenie uruchomienia aparatury.

[Stanowiska ARC](https://github.com/MatPomGit/research-autopilot/blob/main/docs/portfolio/reorganizacja-systemu-badan/shared_research_platforms.md); [inwentarz prywatny `devices`](https://github.com/MatPomGit/devices).

## Powiązane aplikacje APP

- `app-hri-console` (`APP-ARC-08`), `OPTIONAL`, profil `ros2-replay`, bramka `RESEARCH_GO`.
- `app-carehome` (`APP-ARC-09`), `OPTIONAL`, profil `aal-simulator`, bramka `RESEARCH_GO`.

## Powiązane biblioteki LIB

- `lib-adapt`: planowana zależność pośrednia przez `app-carehome`; brak dowodu integracji.
- `lib-asr`: planowana zależność pośrednia przez `app-hri-console`; brak dowodu integracji.
- `lib-audio`: planowana zależność pośrednia przez `app-hri-console`; brak dowodu integracji.
- `lib-events`: planowana zależność pośrednia przez `app-hri-console`, `app-carehome`; brak dowodu integracji.
- `lib-image` (historyczna nazwa; wymaga uzgodnienia z `lib-vis`): planowana zależność pośrednia przez `app-hri-console`; brak dowodu integracji.
- `lib-llm` (historyczna nazwa; wymaga uzgodnienia z `lib-vlm`): planowana zależność pośrednia przez `app-carehome`; brak dowodu integracji.
- `lib-ros`: planowana zależność pośrednia przez `app-hri-console`; brak dowodu integracji.
- `lib-sim`: planowana zależność pośrednia przez `app-hri-console`, `app-carehome`; brak dowodu integracji.
- `lib-vlm`: planowana zależność pośrednia przez `app-hri-console`, `app-carehome`; brak dowodu integracji.

Relacje APP i LIB pochodzą odpowiednio z `app_publication_links.csv` i `component_dependencies.csv`. Są kandydaturami, nie dowodami wykonania prac. Aktualność nazw `lib-signals`, `lib-image` i `lib-llm` wymaga osobnego uzgodnienia z nowymi repozytoriami.

## Proweniencja, metodologia i bramki

- **UID źródłowy:** `cross-arc:CROSS-ARC-01`; repozytorium `MatPomGit/research-autopilot`, identyfikator `CROSS-ARC-01`.
- **Ścieżka źródłowa:** `docs/portfolio/reorganizacja-systemu-badan/shared_research_platforms.md`.
- **Materiał:** [źródło projektu](https://github.com/MatPomGit/research-autopilot/blob/c397169d8630090f38bacf091947cc47083f006c/docs/portfolio/reorganizacja-systemu-badan/shared_research_platforms.md).
- **Rejestr MSC:** [kanoniczna macierz](https://github.com/MatPomGit/research-autopilot/blob/main/docs/portfolio/reorganizacja-systemu-badan/publication_matrix.csv).

Przed badaniem wymagane są niezależny wynik i plan analizy, źródła literaturowe, ocena nowości, kontrola praw do danych/oprogramowania, ocena bezpieczeństwa i kwalifikacja etyczna, jeżeli dotyczy. Szkic nie zawiera danych empirycznych ani nie potwierdza dostępności stanowiska.
