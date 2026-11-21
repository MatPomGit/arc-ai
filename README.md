# ARC AI

**Program naukowy dotyczący metod sztucznej inteligencji i adaptacyjnych systemów obliczeniowych.**

Badania obejmują reprezentacje sygnałów EEG, uczenie multimodalne, odporność na uszkodzenia sensorów, Edge AI, ochronę prywatności, synchronizację czasową, ocenę polityk adaptacyjnych oraz niezawodne systemy asystujące. Głównym kryterium przypisania pracy jest nowy wkład metodologiczny lub algorytmiczny, nie samo wykorzystanie AI.

## Manuskrypty i koncepcje

[Rejestr MSC](portfolio/papers.json) rozróżnia stan badań od etapu przygotowania publikacji. [Katalog artykułów](manuscripts/README.md) przedstawia indywidualne prace i ich zakres. Każda pozycja ma odrębny folder z plikiem LaTeX, hipotezami i planem ewaluacji. Brak wyników oznaczono jawnie, a przytoczone źródła pierwotne nie są traktowane jako wykonana walidacja.

## Linie badawcze

Opis zakresu znajduje się w [RESEARCH.md](RESEARCH.md), a [klasyfikacja tematów](areas/index.json) wskazuje osiem linii badawczych: EEG, fuzja, Edge AI, adaptacja, synchronizacja, AAL, agenci i transfer między domenami.

## Reprodukowalność

[Zasady odtwarzalności](REPRODUCIBILITY.md) i [architektura](ARCHITECTURE.md) rozdzielają źródła naukowe od kodu aplikacyjnego oraz zasobów pomiarowych. Dotychczasowe prace zachowują odniesienia do historycznych commitów. Szkice nie stanowią potwierdzenia uzyskania wyników, formalnej prerejestracji ani decyzji redakcyjnej.

[Strona informacyjna](pages/index.md) pozostaje oddzielona od katalogów badawczych; wpisy `public_listing=false` nie są automatycznie umieszczane na stronie programu.

## Wykonywalne protokoły P01 i P08

[Sklonowane źródła metod badawczych](research/affective/README.md) obejmują kod Python, testy i raporty QC dla `MSC-AFFECT-P01` oraz `MSC-AFFECT-P08`, zachowane z historycznego `arc-affective` bez modyfikacji treści. [Manifest 52 plików](research/affective/source_manifest.json) wiąże każdy plik z dokładnym Git blob SHA. Testy CI sprawdzają integralność i uruchamiają deterministyczne scenariusze syntetyczne; nie stanowią walidacji na rzeczywistym EEG ani pomiarów czasu wykonania urządzenia.
