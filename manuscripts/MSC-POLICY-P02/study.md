# MSC-POLICY-P02 — plan badania i powiązania

**Temat:** Stronniczość oceny polityk adaptacyjnych przy brakach pomiaru zależnych od interwencji

**Program:** `arc-ai`. **Obszar:** `adaptive-policy-evaluation-mnar`. **Typ:** `IDEA` (CANDIDATE). **Stan źródła:** `NEW_CROSS_PROGRAM_IDEA_HOLD`. **Tryb integracji:** `INDEX_ONLY_NO_NEW_FOLDER`.

## Cel, wynik główny i granice badania

Przedmiot badania: Stronniczość oceny polityk adaptacyjnych przy brakach pomiaru zależnych od interwencji. Kandydatura, bez zatwierdzonego odrębnego protokołu.

- **Główny wynik proponowany:** Obciążenie estymatora wartości polityki i pokrycie przedziałów wobec prawdy symulacyjnej
- **Odrębność naukowa:** Wkład metodologiczny dotyczy MNAR związanego z decyzją; nie ogólne kontrfaktyczne porównanie adaptacji XR.
- **Uzasadnienie klasyfikacji:** [Nowa propozycja burzy mózgów 2026-11-20, priorytet A] Stosować symulację z jawną latentną prawdą i porównać error w ocenie polityki oraz pokrycie CI; różnica od modelowania braków sensorów: tu błąd w estymacji efektu interwencji. Sprawdzić literaturę MNAR/off-policy evaluation, nie zakładać identyfikowalności przy braku positivity. Wkład i nowość niezatwierdzone; nie tworzyć manuskryptu przed audytem. Repozytorium programu ARC AI jeszcze nie istnieje: pełny opis w prywatnym źródle przejściowym. AUDYT DUPLIKACJI: rozdzielić bias przez informatywne braki pomiaru od ogólnej kontrfaktycznej oceny interwencji XR-IDEA-14. | Proponowane doprecyzowa
- **Powiązane rekordy:** `MSC-AFFECT-P02` (arc-affective:P02), `MSC-AFFECT-P06` (arc-affective:P06), `MSC-AAL-P05` (carehome-aal:AAL-P05), `MSC-POLICY-P01` (cross-arc:CROSS-ARC-01), `MSC-AR-P20` (arc-xr:XR-IDEA-14)

## Stanowisko badawcze

**Wstępne powiązanie:** `ST-00`. To propozycja na podstawie domeny, a nie potwierdzenie uruchomienia aparatury.

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

- **UID źródłowy:** `arc-ai:AI-IDEA-01`; repozytorium `MatPomGit/research-autopilot`, identyfikator `AI-IDEA-01`.
- **Ścieżka źródłowa:** `docs/portfolio/reorganizacja-systemu-badan/arc_ai_research_proposals.md`.
- **Materiał:** [źródło projektu](https://github.com/MatPomGit/research-autopilot/blob/d8495d70fc73d275ae359e15942f542575faad40/docs/portfolio/reorganizacja-systemu-badan/arc_ai_research_proposals.md).
- **Rejestr MSC:** [kanoniczna macierz](https://github.com/MatPomGit/research-autopilot/blob/main/docs/portfolio/reorganizacja-systemu-badan/publication_matrix.csv).

Przed badaniem wymagane są niezależny wynik i plan analizy, źródła literaturowe, ocena nowości, kontrola praw do danych/oprogramowania, ocena bezpieczeństwa i kwalifikacja etyczna, jeżeli dotyczy. Szkic nie zawiera danych empirycznych ani nie potwierdza dostępności stanowiska.
