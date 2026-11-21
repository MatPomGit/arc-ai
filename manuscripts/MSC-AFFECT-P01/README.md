# MSC-AFFECT-P01: Sparse-Channel EEG Affect Representation Under Cross-Dataset and Montage Shift

**Status badań:** szkic manuskryptu (draft). **Wyniki empiryczne:** brak potwierdzonej analizy.

Pytanie badawcze: Does a low-channel model remain calibrated on held-out people and across corpora when reference montage and acquisition domains change?

Własny [manuskrypt LaTeX](main.tex) określa metodę, hipotezy, porównania, wyniki planowane i ograniczenia. [Plan badań](study.yaml) zawiera sprawdzalny kontrakt. [Historyczny plan](source_plan.md) zachowano z oryginalnego repozytorium w wersji 0ff5f1531f03. [Metadane pochodzenia](provenance.json) wskazują dokładny blob Git oraz licencję źródła.

Zgoda na wykorzystanie danych, walidacja eksperymentów i decyzja o zgłoszeniu publikacji wymagają odrębnych dowodów. Nie należy utożsamiać syntetycznych testów oprogramowania z wynikami badawczymi.

## Pełny roboczy manuskrypt

Plik [main.tex](main.tex) kompiluje cztery merytoryczne sekcje ([introduction](sections/introduction.tex), [methods](sections/methods.tex), [results](sections/results.tex), [discussion](sections/discussion.tex)) oraz [bibliografię](references.bib). Rozwinięte źródła przeniesiono z historycznego szkicu IEEE, zachowując ich treść naukową i cytowania. Zmieniono tylko warstwę składu na standardową klasę `article`, aby umożliwić niezależną kompilację bez wymuszania docelowego czasopisma. Wszystkie historyczne pliki pozostają niezmienione w [original/](original/); wskazany wynik `Pending` nie jest wynikiem badania.

## Implementacja badań i kontrola odtwarzalności

[Pinned research code and QA](../../research/affective/README.md) contains the source evaluation methods, synthetic-only regression tests and documented limitations of the experimental pipeline. The code is kept byte-for-byte from the historical source; use the [manifest](../../research/affective/source_manifest.json) for exact Git blob provenance. This does not establish authorisation to analyse raw EEG or an empirical hardware benchmark.
