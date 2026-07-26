# Simultaneous finite-family sunflower-host diagnostic

Run

```text
python scripts/check_simultaneous_finite_sunflower_host.py \
  experiments/simultaneous-finite-sunflower-host-example.json
```

The stored instance has

```text
N=100,
b=4,
two omitted optional-core indices,
two empty-core support families.
```

The first empty-core family consists of six disjoint pairs.  The second consists
of four disjoint triples.  The two families overlap with one another, as allowed
by PP3ani.

There are

```text
binom(97,3)=147440
```

uniform helper blocks after removing the marked centre and two optional-core
indices.  Exact enumeration gives

```text
N 100
b 4
omitted optional cores 2
available helpers 97
empty-core families 2
uniform helper blocks 147440
exact target-support expectation 0.003893109061
formula target-support expectation 0.003893109061
coarse 2Lb^2/N bound 0.640000000000
zero-target block fraction 0.996106890939
maximum target supports in one block 1
residual objective 0.600000000000
combined objective 0.603893109061
outcome simultaneous_finite_sunflower_host
```

The exact expectation is

```text
6 (3)_2/(97)_2 + 4 (3)_3/(97)_3
=287/73720.
```

More than `99.6%` of helper blocks contain no target support from either family,
even though the two support systems overlap.  Adding the stored residual
objective remains below one, so the finite first-moment criterion selects a block
that simultaneously avoids every target family and leaves room for source-valid
paid completion.
