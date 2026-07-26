# Ambient binary positive-support link diagnostic

Run

```text
python scripts/check_ambient_binary_link_decomposition.py \
  experiments/ambient-binary-link-decomposition-example.json
```

The stored instance conditions on one ambient resource in a bank with

```text
Q=30,
q=4,
tau=0.30.
```

It uses the complete graph and complete 3-uniform hypergraph on the other 29
endpoint indices as the rank-three and rank-four positive signature links.

The exact output is

```text
Q 30
q 4
tau 0.3
p3 0.001231527094
p4 0.000045612115
rank3 signatures 406
rank4 signatures 3654
positive-support expectation 0.666666666667
rank3 lower threshold 121.800
rank4 lower threshold 3288.600
rank3 maximum degree 28
rank3 greedy matching 14
rank4 maximum vertex degree 378
rank4 hypergraph threshold 238
rank4 greedy triple matching 9
nested graph-link edges 378
nested graph maximum degree 27
nested threshold 16
nested graph matching 14
rank4 outcome fixed_two_partner_pencil
outcome ambient_binary_positive_support_localized
```

The conditioned two-arc probabilities agree with PP3ama:

```text
p3=1/((Q-1)(Q-2)),
p4=(q-3)/((Q-1)(Q-2)(Q-3)).
```

Both signature counts exceed their PP3amc density thresholds.  The rank-three
link realizes the fixed-partner star branch.  The rank-four 3-link has maximum
vertex degree above `ceil(E_4^(2/3))`; its graph link then has maximum degree above
`ceil(E_4^(1/3))`, realizing the fixed-two-partner pencil branch.

The script also computes greedy graph and triple matchings and verifies the exact
alternative bounds when the maximum-degree branches are absent.
