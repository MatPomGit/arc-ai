# Reproducible research methods for MSC-AFFECT-P01 and P08

The `research/affective/` directory preserves software and QA documents from the exact historical Git commit `0ff5f1531f03270c4f9fdcc7f3af6d2e9aca85dd` of [ARC Affective](https://github.com/MatPomGit/arc-affective). The implementation remains under its historical Python package name `arc_affective` for reproducibility and compatibility. The original project is not modified.

P01 includes synthetic-only EEG evaluation, participant-grouped validation, montage and provenance audits, event alignment and uncertainty checks. P08 contains deterministic virtual-clock stream and queue scheduling with fault injection. The source package and independent tests are in `src/` and `tests/`; historical QA reports are in `reports/`.

Run the offline tests at the repository root:

```sh
python3 -B scripts/verify_affective_snapshot.py
python3 -B -m unittest discover -s research/affective/tests -p 'test_p*.py' -v
PYTHONPATH=research/affective/src python3 -B -m arc_affective.p08_benchmark --scenario combined
```

The archive was copied byte-for-byte and is checked by Git blob digests against [source_manifest.json](source_manifest.json). Preserve this source copy rather than rewriting it into a new algorithm version without explicit tests. All reported calculations here are labelled synthetic E0 or virtual-clock simulation; no genuine EEG-signal analysis, measured device latency or clinical inference has been established.

The six ARC-AI manuscripts retain separate scientific eligibility gates, described in `manuscripts/MSC-AFFECT-P01/` and `manuscripts/MSC-AFFECT-P08/`. The [historical source project's Apache 2.0 licence](../../manuscripts/ORIGINAL_LICENSE_APACHE_2.0) covers the imported files, subject to their original notices.
