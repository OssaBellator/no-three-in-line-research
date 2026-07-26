# Controller-puncture history localization diagnostic

Run

```text
python scripts/check_controller_puncture_history_localization.py \
  experiments/controller-puncture-history-localization-example.json
```

The stored history has

```text
144 puncture centres,
12 designated incidences per centre,
1728 chronological records.
```

The first synthetic branch places one common exact candidate entry in every
star fibre.  Its right degree is `144`, above the threshold `12`, realizing the
candidate-recapture stack.

The second branch gives every record a distinct candidate, partner, controller,
and label resource.  The expected output is

```text
puncture centres 144
designated width per centre 12
history incidence records 1728
threshold 12
repeated exact candidate degree 144
diffuse maximum candidate degree 1
diffuse centre-entry matching 144
candidate theorem lower bound 72.000000
maximum matched partner degree 1
maximum matched controller degree 1
maximum matched label degree 1
full chronological resource matching 144
resource theorem lower bound 2.000000
outcome repeated_candidate_or_full_chronological_matching
```

Thus the repeated branch greatly exceeds the target degree.  In the diffuse
branch the centre--entry matching is twice the PP3apg lower bound, and the full
resource matching is far larger than the PP3aph guarantee.
