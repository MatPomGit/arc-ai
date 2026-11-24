# Audyt usunięcia repozytorium ARC Affective

**Wynik: BLOCKED.** Stan źródła: `MatPomGit/arc-affective@876f1d4e71b41cac0d415f2d262824480ccbf607`. Przedmiotem tej kontroli jest ryzyko utraty informacji po fizycznym usunięciu repozytorium GitHub, a nie stan gotowości naukowej artykułów.

## Zrealizowane przekazanie

| MSC | Właściciel | Materiał |
| --- | --- | --- |
| P01 i P08 | [ARC AI](../../manuscripts/README.md) | Kanoniczne manuskrypty, kopie IEEE, plany, 52 wspólnych plików wykonawczych E0, testy CI |
| P02, P03, P04 i P06 | [ARC AI](../../manuscripts/README.md) | Manuskrypty koncepcyjne i plany, bez zweryfikowanych eksperymentów |
| P05 | [ARC Neuro](https://github.com/MatPomGit/arc-neuro/tree/main/papers/affect/MSC-AFFECT-P05) | Przekazany plan naukowy |
| P07 | [ARC Robo](https://github.com/MatPomGit/arc-robo/tree/main/manuscripts/MSC-AFFECT-P07) | Przekazany plan naukowy |

Oryginał ma 118 plików Git (łącznie z dokumentacją i historyczną infrastrukturą). Przejęcie wszystkich ośmiu prac nie oznacza pełnego odtworzenia jego historii Git ani dyskusji GitHub. Wspólny kod P01/P08 jest zachowany w `research/affective/`, ale cztery testy źródłowego repozytorium nie należą do pakietu wykonywalnego.

## Wyniki audytu informacji i zależności

- **73 Issues**: 69 otwartych i 4 zamknięte. Ich treści i **61 komentarzy** zapisano jako [snapshot JSON](issues-and-comments.json). Jest to kopia treści, a nie przeniesienie aktywnego śledzenia zadań.
- **33 zamknięte PR**, 0 otwartych PR. [Rejestr PR i SHA plików](prs-and-tree.json) utrwala tytuły, stan, commit scalenia i spis plików, ale **nie** zachowuje pełnych diffów, oryginalnych commitów, przeglądów ani historii Git.
- W wyszukiwaniu kodu GitHub fraza `arc-affective` występuje w **co najmniej 53 plikach innych repozytoriów**; najbardziej w ARC AI, ARC Robo, ARC Neuro, Research Autopilot i `self`. Część tych referencji jest niezmienną historią proweniencji, część to aktywne linki `blob/main` i stare adresy Issues. Usunięcie repozytorium przerwie te adresy.
- GitHub API: `has_pages=true`, ale dostępność opublikowanego adresu Pages nie została potwierdzona. Nie deklarujemy, że strona jest aktualnie aktywna.
- Repozytorium nie jest obecnie archiwizowane (`archived=false`); brak otwartych PR, gałąź tylko `main`, zero wydanych Releases. Samo to nie stanowi zgody na usunięcie.
- `LICENSING.md` w źródle rozdziela Apache-2.0 dla kodu od CC BY 4.0 dla autorskich prac naukowych. Repozytoria docelowe mają odrębne polityki licencji; po migracji nie można zmieniać historycznych praw lub usuwać informacji o autorach.

## Niespełnione bramki bezpieczeństwa

1. Utworzyć i **niezależnie od GitHub** zweryfikować pełny `git clone --mirror` / `git bundle` z commitami, tagami, refs i sumą kontrolną. Obecny katalog plików i snapshot PR **nie zastępują** pełnej historii.
2. Zachować albo przenieść wszystkie **69 otwartych zadań** do ich właścicieli ARC AI/Neuro/Robo; nie zmieniać automatycznie ich naukowego statusu i nie gubić 61 komentarzy.
3. Przepisać aktywne odwołania do `MatPomGit/arc-affective` na istniejące docelowe ścieżki. Odwołania do nienaruszalnych oryginałów należy zachować wraz z dostępnym, trwałym archiwum.
4. Zweryfikować Pages, gałęzie, Releases, workflow, licencje, dostępne pliki i linki po przekierowaniu. Jeśli adres historyczny ma pozostać działający, samo **usunięcie** nie spełni tego warunku.
5. Dopiero po sprawdzeniu powyższych warunków wykonać operację administracyjną w GitHub, po udokumentowanym sprawdzeniu backupu i odczytu nowych repozytoriów. Zalecanym wariantem jest **archiwizacja GitHub** zamiast natychmiastowego usunięcia.

**Decyzja:** `DELETE_NOT_SAFE`. Nie usuwać `arc-affective`, nie zamykać hurtowo Issues i nie przedstawiać kopii metadanych jako zweryfikowanego backupu repozytorium.
