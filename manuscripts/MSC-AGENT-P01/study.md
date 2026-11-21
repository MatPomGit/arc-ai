# MSC-AGENT-P01 — plan badania i powiązania

**Temat:** Czasowo-przyczynowa proweniencja decyzji agentów przy asynchronicznych zdarzeniach AAL i HRI

**Program:** `arc-ai`. **Obszar:** `causal-event-provenance-toctou`. **Typ:** `IDEA` (CANDIDATE). **Stan źródła:** `NEW_CROSS_PROGRAM_IDEA_HOLD`. **Tryb integracji:** `INDEX_ONLY_NO_NEW_FOLDER`.

## Cel, wynik główny i granice badania

Przedmiot badania: Czasowo-przyczynowa proweniencja decyzji agentów przy asynchronicznych zdarzeniach AAL i HRI. Kandydatura, bez zatwierdzonego odrębnego protokołu.

- **Główny wynik proponowany:** Nieokreślony w rejestrze. Wymaga zdefiniowania metryki, estymandu i jednostki analizy przed rozpoczęciem badania.
- **Odrębność naukowa:** Należy porównać źródłowy protokół z pokrewnymi manuskryptami przed formalizacją hipotezy.
- **Uzasadnienie klasyfikacji:** [Nowa propozycja burzy mózgów 2026-11-20, priorytet A] W deterministycznej symulacji zbadać niewykryte nieaktualne przesłanki decyzji przy przestawianiu eventów, restartach i TOCTOU; porównać snapshot/versioned happens-before z poprawnym baseline transakcyjnym. Nie równać synchronizacji czasu z semantyczną poprawnością pochodzenia decyzji; bez fizycznych aktuatorów. Wkład i nowość niezatwierdzone; nie tworzyć manuskryptu przed audytem. Repozytorium programu ARC AI jeszcze nie istnieje: pełny opis w prywatnym źródle przejściowym.
- **Powiązane rekordy:** `MSC-SYNC-P01` (arc-adhd-game:F-ADHD-02), `MSC-AAL-P04` (carehome-aal:AAL-P04), `MSC-HRI-P07` (arc-hri-safety:M07), `MSC-POLICY-P01` (cross-arc:CROSS-ARC-01)

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

- **UID źródłowy:** `arc-ai:AI-IDEA-04`; repozytorium `MatPomGit/research-autopilot`, identyfikator `AI-IDEA-04`.
- **Ścieżka źródłowa:** `docs/portfolio/reorganizacja-systemu-badan/arc_ai_research_proposals.md`.
- **Materiał:** [źródło projektu](https://github.com/MatPomGit/research-autopilot/blob/d8495d70fc73d275ae359e15942f542575faad40/docs/portfolio/reorganizacja-systemu-badan/arc_ai_research_proposals.md).
- **Rejestr MSC:** [kanoniczna macierz](https://github.com/MatPomGit/research-autopilot/blob/main/docs/portfolio/reorganizacja-systemu-badan/publication_matrix.csv).

Przed badaniem wymagane są niezależny wynik i plan analizy, źródła literaturowe, ocena nowości, kontrola praw do danych/oprogramowania, ocena bezpieczeństwa i kwalifikacja etyczna, jeżeli dotyczy. Szkic nie zawiera danych empirycznych ani nie potwierdza dostępności stanowiska.
