# Final-state shadow path diagnostic

Run

```text
python scripts/check_final_state_shadow_path.py \
  experiments/final-state-shadow-path-example.json
```

The stored path starts from seven original source points.  The first trade
inserts four points.  The second trade removes two of those first-step points and
inserts one replacement, so the final source has three genuinely new points.
Every intermediate and final state is no-three-in-line.

The exact output is:

```text
stage count                         2
stage-1 new points                  4
stage-1 simple support            116
stage-2 final new points            3
stage-2 final simple support       75
union intermediate support        117
transient-only support             42
final unary incidence weight       72
final unary simple support         72
final binary simple support         3
binary general domain bound         6
combined general domain bound      78
exact maximum final domain loss     4
base domain size                  600
post-shadow lower bound           596
allocation threshold             400
outcome            final_state_direct_allocation
```

The 42 transient-only entries are present after the first trade but absent from
the final source.  They therefore cause no final domain deletion, regardless of
how much dynamic `Xi` multiplicity they carried in the intermediate state.

The final state contains three new points, so PP3ahx permits binary domain loss
at most

```text
3(3-1)=6.
```

The exact binary support contains only three candidate entries.  Adding the 72
final unary incidences gives the conservative bound

```text
72+6=78 <= xi R=200.
```

The exact maximum loss from one macro-label-pair domain is only four.  Hence the
post-shadow domain has at least `596` values, well above the allocation threshold
`gamma R=400`.

The checker accepts any finite stage list.  It rejects a stage that removes an
absent point, reinserts a point still present, or creates a collinear triple.  It
reports `next_generation_unary_star` when the final unary fibre exceeds the
`xi R/(2S)` threshold and the direct margin test fails.