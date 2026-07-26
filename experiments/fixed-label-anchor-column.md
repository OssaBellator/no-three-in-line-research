# Fixed-label anchor-column diagnostic

Run

```text
python scripts/check_fixed_label_anchor_column.py \
  experiments/fixed-label-anchor-column-example.json
```

The stored fixed refill-label column uses

```text
W=100,
R=10,000.
```

Its physical controller--anchor graph is the disjoint union of four copies of
`K_(99,99)`.  Because the refill label is fixed, every physical pair determines
at most one movement label and therefore contributes one unit of column mass.

The exact output is

```text
W 100
R 10000
fixed-label anchor column mass 39204
column threshold 30000.0
maximum source degree 99
exact endpoint matching 396
matching lower bound 196.02
one-layer anchor bank 100
batch puncture ratio 0.01
outcome fixed_label_anchor_endpoint_bank
```

The maximum source degree is below the star threshold `W`; the endpoint-disjoint
matching branch remains large enough after source-layer pigeonholing to give a
size-`W` anchor bank.  Puncturing every selected anchor in one macro would cost
only one percent of the stored controller pool.

The checker verifies fixed-label physical-pair uniqueness, the star-or-matching
bound, the common-layer bank, and the batch-puncture scale.
