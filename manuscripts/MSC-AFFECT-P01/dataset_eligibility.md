# P01: audyt kwalifikowalności korpusów i bramki przed eksperymentem

**Data przeglądu:** 2026-11-22. **Status:** metadata-only / NOT_RUN dla sygnałów EEG. Żaden plik uczestników nie został pobrany ani przeanalizowany. Niniejszy dokument nie jest prerejestracją i nie zmienia `protocol_frozen: false`.

## Priorytet 1: FACED / NEMAR `nm000112`, wersja `v1.1.4`

- **Źródło kanoniczne:** https://nemar.org/dataset/nm000112?v=v1.1.4 ; DOI https://doi.org/10.82901/nemar.nm000112 .
- **Metadane wydawcy:** 123 uczestników, 28 filmów, 32 kanały EEG (10-10), samoopisy na 12 wymiarach, w tym walencja i pobudzenie. W publikacji źródłowej skala ocen ma zakres 0–7.
- **Licencja widoczna u dostawcy:** CC BY 4.0 dla wydania NEMAR. Odróżnić wydanie NEMAR/BIDS od oryginalnego zbioru na Synapse. Sprawdzić licencje poszczególnych materiałów, w szczególności filmów i plików pochodnych.
- **Wersja i koszty zasobów:** v1.1.4 (19 października 2026); pełen zbiór według portalu ~31,4 GB, archiwum ~22,7 GB. Nie pobierać całości na potrzeby wstępnej kwalifikacji.
- **Wymagane przed statusem ELIGIBLE:** zarchiwizowane i zahashowane metadane BIDS `dataset_description.json`, `participants.tsv`, `channels.tsv`, `electrodes.tsv`/układ 10-10, pliki zdarzeń i mapowanie self-report do prób. Zweryfikować, czy w wersji BIDS są dostępne oryginalne **oceny walencji uczestnika per film**, a nie jedynie docelowe kategorie emocji przypisane bodźcom.
- **Bramka:** sam odczyt metadanych nie dowodzi kompletności skali, praw do sygnału, zgodności referencji ani jakości segmentów. Status `METADATA_VERIFIED / EEG_UNAUDITED / NOT_ELIGIBLE_YET`.

## Priorytet 2: GAMEEMO / Mendeley Data, historyczna wersja `v3`

- **Kanoniczna historyczna publikacja:** https://data.mendeley.com/datasets/b3pn4kwpmn/3 ; DOI https://doi.org/10.17632/b3pn4kwpmn.3 .
- **Metadane wydawcy v3:** 28 uczestników, 14-kanałowy Emotiv EPOC+, cztery gry po ok. pięć minut, SAM po rozgrywce, sygnały surowe i przetworzone w formatach CSV/MAT; licencja wpisu v3: CC BY 4.0.
- **Istotna zmiana wersji:** serwis pokazuje także **v5 opublikowaną 12 października 2026, objętą embargiem do 13 października 2027**. W P01 nie należy zastępować dostępnej v3 przez v5, zakładać dostępu do plików v5 ani mieszać wersji.
- **Główne ryzyko metodologiczne:** kilka samoopisowych punktów SAM na uczestnika może nie zapewniać wiarygodnej estymacji CCC (szczególnie przy stałych odpowiedziach). Nie traktować etykiety „boring/calm/horror/funny” jako samoopisu walencji. Najpierw zweryfikować liczbę par ocen, zakres skali, powiązanie z EEG i częstość CCC niezdefiniowanego.
- **Bramka:** `METADATA_VERIFIED / TRIAL_LABEL_MAPPING_UNAUDITED / NOT_ELIGIBLE_YET`. Ewentualny model kategoryczny tylko jako oddzielne, jawnie zadeklarowane pytanie badawcze.

## Deterministyczny protokół dopuszczenia danych (bez sygnałów w Git)

1. **Provenance/rights:** zapisać wersję, DOI, licencję dostawcy, wymagane atrybucje, warunki ponownego użycia sygnałów i metadanych, sha256 pobieranych artefaktów oraz datę dostępu. Nie zamieszczać danych osobowych.
2. **Labels:** wyznaczyć dokładny klucz `participant_id + stimulus_id + trial_id`, skalę, kierunek i moment pomiaru walencji. Zweryfikować 1:1 przypisanie do fragmentu EEG i brak wielokrotnego liczenia tej samej oceny z epok jako niezależnych prób.
3. **Montage:** zweryfikować kanały, pozycje, odniesienie, jednostki i historię przetwarzania. Redukcję elektrod badać najpierw **wewnątrz jednego korpusu**, gdzie referencja jest wspólna. Mapowanie między korpusami wymaga oddzielnego uzasadnienia.
4. **Splits:** z góry ustalić foldy niezależne od uczestnika; osobno wrażliwość na nowe filmy; żaden uczestnik ani jego epoki nie mogą być w treningu i teście jednocześnie. Selekcja kanałów i hiperparametrów wyłącznie na danych treningowych.
5. **Feasibility:** policzyć liczbę uczestników z co najmniej dwiema różnymi wartościami walencji oraz liczbę dopasowanych prób dla full/sparse. Uczestnicy z jedną próbą lub stałą walencją zachowują MSE, a CCC jest `undefined`.
6. **Freeze:** zamrozić konkretne wybory przed analizą predykcyjną. Nie używać wyników testowych do doboru zbioru, progów, elektrod ani modelu. Utrwalać manifest splitów bez rzeczywistych identyfikatorów osobowych.
7. **Go/no-go:** jeśli prawa, mapowanie lub metadane nie są potwierdzone, zatrzymać benchmark dla danego korpusu jako `UNAVAILABLE` lub `NOT_ESTIMABLE`, a nie wymuszać publikacji wyniku.

## Minimalny pakiet dowodowy do uzupełnienia

| Pole | FACED v1.1.4 | GAMEEMO v3 |
| --- | --- | --- |
| Weryfikacja rekordu i DOI | Potwierdzona na stronie dostawcy | Potwierdzona na stronie dostawcy |
| Licencja wskazana przez dostawcę | CC BY 4.0 | CC BY 4.0 |
| Pobrane metadane + SHA-256 | NOT_RUN | NOT_RUN |
| Audyt indywidualnych ocen prób | NOT_RUN | NOT_RUN |
| Audyt kanałów/referencji | NOT_RUN | NOT_RUN |
| Kwalifikacja do CCC | NOT_ESTIMABLE_YET | NOT_ESTIMABLE_YET |
| Prawdziwa walidacja EEG | NOT_RUN | NOT_RUN |

**Źródła:** https://nemar.org/dataset/nm000112 ; https://www.nature.com/articles/s41597-023-02650-w ; https://data.mendeley.com/datasets/b3pn4kwpmn/3 ; https://data.mendeley.com/datasets/b3pn4kwpmn/5 .

## Kontrakt podziałów indeksowych (implementacja E0)

Moduł `research/p01_splits.py` generuje dwa typy podziałów na podstawie zewnętrznie zweryfikowanego **metadanych prób**, bez odczytu sygnałów EEG:

- `leave_one_participant_out(rows)`: zwraca pełne foldy participant-disjoint z indeksami `train_indices` i `test_indices`. Każda próba uczestnika testowego pozostaje w teście, nigdy w treningu.
- `participant_stimulus_block(rows, held_out_participant=..., held_out_stimuli=...)`: test obejmuje wyłącznie próby wybranego uczestnika i jawnie wybranego bloku bodźców. Trening wyklucza zarówno tego uczestnika, jak i bodźce testowe; pozostałe przecięcia są zwracane jako `excluded_indices`, a nie używane do szkolenia.
- Zwracane struktury nie zawierają identyfikatorów osobowych ani tekstowych kluczy prób. **Indeksy wierszy nie są trwałym manifestem**, jeżeli kolejność metadanych może się zmienić. Przed utrwaleniem podziału należy zamrozić wersję i SHA-256 uporządkowanej, zanonimizowanej tabeli wejściowej w chronionym środowisku; nie publikować surowych identyfikatorów ani niesolonych hashy identyfikatorów.
- Wymagane pola wejściowe: `participant_id`, `trial_id`, `stimulus_id`; unikaty `(participant_id, trial_id)`, brak wartości pustych. Funkcje nie wykrywają samodzielnie rodzinnych powiązań uczestników, sesji współdzielonych przez identyczne osoby między korpusami ani przecieku cech z preprocessingu. Te warunki wymagają niezależnego audytu.
- **E0 / SYNTHETIC_ONLY:** testy `tests/test_p01_splits.py` sprawdzają izolację, kompletność foldów i błędy metadanych na sztucznych rekordach. Brak rzeczywistych splitów FACED/GAMEEMO i brak modeli wytrenowanych na EEG.

## Adapter BIDS: bezpieczne wejście przed analizą sygnałów

`research/p01_bids_metadata.py` implementuje `build_trial_metadata(participants_tsv, events_tsv_by_participant, columns, valence_min, valence_max)`. Wymaga jawnego, zweryfikowanego mapowania kolumn `trial_id`, `stimulus_id`, `valence`, `onset`, `duration`. Dla każdego uczestnika z `participants.tsv` otrzymuje w pamięci jeden odpowiadający mu tekst `events.tsv`. Odrzuca brak danych, duplikaty identyfikatorów prób, nieznane osoby, niepoprawny czas i oceny walencji poza zadeklarowaną skalą. Zwraca rekordy prób zgodne z generatorem LOSO.

**Ograniczenia:** narzędzie nie rozpoznaje automatycznie struktury konkretnego wydania FACED, nie łączy bocznych plików ocen z eventami, nie odczytuje ścieżek BIDS, nie sprawdza rzeczywistych EEG, uprawnień/licencji ani relacji zdarzenia z segmentem sygnału. Nie wolno uznawać kategorii bodźca za indywidualny samoopis. Jeżeli oceny znajdują się w osobnym pliku, należy najpierw przeprowadzić niezależny, weryfikowalny join 1:1 z kontrolą unikatowości i śladu pochodzenia. Brak takiego joinu jest twardą blokadą, a nie zgodą na imputację.

Dane identyfikujące uczestników są przetwarzane wyłącznie w pamięci zaufanego środowiska; nie zapisywać wejściowych plików TSV z uczestnikami, surowych ID ani pseudonimów w publicznym repozytorium lub logach CI. Testy `tests/test_p01_bids_metadata.py` wykorzystują wyłącznie syntetyczne `sub-01`/`sub-02`; wynik PASS oznacza sprawność walidatora, a nie kwalifikację FACED. Formalne źródła, wersja, rzeczywiste nazwy pól, skala i test mapowania są nadal `NOT_RUN`.
