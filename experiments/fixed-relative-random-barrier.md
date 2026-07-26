# Fixed-relative random-permutation barrier diagnostic

Run:

```bash
python scripts/check_fixed_relative_random_barrier.py \
  experiments/fixed-relative-random-barrier-example.json
```

For the stored `n=12` relative derangement from the verified `p=13` seed, the
checker reports:

```text
maximal nonaxis lines:                 874
nonaxis collinear triples:            5052
admissible labelled layer patterns:  34000
permutation denominator (n)_3:        1320
exact expected bad triples:        25.757575...
row-conflict degree lower bound:      9654
symmetric-LLL expression lower bound: 19.8805...
```

The expectation is for a fresh uniform `sigma` with the relative derangement
held fixed.  The verified certificate itself is a specially selected
permutation and has zero bad triples.  The diagnostic quantifies why an
unconditioned first moment or the natural uniform symmetric permutation LLL
does not explain that certificate.
