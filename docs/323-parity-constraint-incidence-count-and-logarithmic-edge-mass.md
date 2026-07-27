# Parity-constraint incidence count and logarithmic edge mass

`docs/322` removes owner pairs that forbid both XOR values.  The remaining
pairwise parity predicates are individually consistent but may form a frustrated
signed cycle.  This chapter counts those one-XOR predicates at the directed-
assignment level and shows that a uniform Hamilton cycle sees only logarithmic
parity-edge mass.

No signed-cycle elimination or asymptotic seed theorem is claimed.

## 1. Secant incidences hosted by one orbit square

Use the centered coordinates of PP3bmn.  For one assignment `(u,v)`, write

```text
g=gcd(u,v),
A=max(u,v).
```

### Proposition PP3bmr -- PROVED / HOSTED INCIDENCE BOUND

The number of other directed assignments having a centered orbit vertex on a
secant of `Q(u,v)` is

```text
O(1+m g/A).
```

The implicit constant is absolute and includes both orientation choices and
coordinate swap.

#### Proof

For either diagonal, the positive odd coordinate pair of the second assignment
is a positive multiple of the primitive direction `(u/g,v/g)` or its coordinate
swap.  There are `O(1+mg/A)` such multiples in the centered box.

For a side, use the representative equation

```text
(u-v)X+(u+v)Y=u^2+v^2.
```

The integer solutions form an arithmetic progression with step vector

```text
((u+v)/d, -(u-v)/d),
d=gcd(u-v,u+v)<=2g.
```

At least one step coordinate has magnitude at least `A/(2g)`, so a box of side
`O(m)` contains `O(1+mg/A)` solutions.  The other three sides, the reflected
orientation, and the conversion from centered vertices to directed assignments
cost only an absolute factor. ∎

This counts an incidence with the owner supplying the two secant points as the
host.  Every two-owner flaw has at least one such host.

## 2. Total number of one-XOR assignment pairs

Let `C_m` be the number of compatible directed-assignment pairs for which exactly
one relative orientation parity is bad.  Pairs forbidding both parities are not
included.

### Theorem PP3bms -- PROVED / GLOBAL CONSTRAINT-PAIR COUNT

```text
C_m=O(m^2 log m).
```

#### Proof

Sum PP3bmr over all positive odd centered pairs `(u,v)` with `u,v<=2m-1` and
`u!=v`.  It remains to bound

```text
sum_(u,v) gcd(u,v)/max(u,v).
```

Write `u=da`, `v=db` with `gcd(a,b)=1` and `B=max(a,b)`.  The summand is `1/B`,
and the scale has `O(m/B)` choices.  There are `O(B)` ordered primitive pairs on
the shell `max(a,b)=B`.  Therefore

```text
sum_(u,v) gcd(u,v)/max(u,v)
 = O(sum_(B<=2m) B*(m/B)*(1/B))
 = O(m log m).
```

Multiplying by the outer factor `m` in PP3bmr and adding the `O(m^2)` constant
terms gives the result.  Charging each pair to either host only overcounts by a
constant factor. ∎

The same estimate includes pairs that cannot occur together in a Hamilton
cycle, so it is safe for the probability bound below.

## 3. A uniform Hamilton cycle has logarithmic parity-edge mass

For a Hamilton cycle `rho`, let `q(rho)` be the number of owner pairs carrying a
single consistent XOR constraint.  Locally impossible pairs are counted
separately.

### Corollary PP3bmt -- PROVED / LOGARITHMIC FIRST MOMENT

For a uniform directed Hamilton cycle,

```text
E q(rho)=O(log m).
```

#### Proof

A fixed compatible pair of directed assignments either has zero Hamilton
completions or is a two-edge directed path forest.  In the latter case its exact
cylinder probability is

```text
1/[(m-1)(m-2)].
```

Sum the indicator probabilities over `C_m=O(m^2 log m)` one-XOR pairs. ∎

This improves the earlier `O(m)` estimate for two-owner atomic flaws: many atomic
collinear triples collapse to one parity edge.

## 4. A pair-safe logarithmic-edge Hamilton cycle exists

### Corollary PP3bmu -- PROVED / SPARSE PARITY INSTANCE EXISTS

For every sufficiently large `m`, there is a Hamilton cycle satisfying both:

1. no owner pair forbids both XOR values;
2. its signed parity graph has `O(log m)` edges.

#### Proof

By PP3bmq, the probability of any locally impossible pair is `o(1)`.  Hence a
uniform Hamilton cycle is pair-safe with probability `1-o(1)`.  By PP3bmt,
`E q=O(log m)`, and conditioning on an event of probability `1-o(1)` preserves
this order.  Therefore some pair-safe cycle has at most the conditional average,
which is `O(log m)`. ∎

This is the first asymptotic nonemptiness statement for the reduced parity
frontier.  It does not say that the `O(log m)` signed graph is consistent.

## 5. Exact incidence audit through `m=60`

The exact assignment constraint graph was reconstructed at selected sizes through
`m=60`.  At `m=60` it has

```text
24,404 one-XOR compatible pairs,
44 locally impossible pairs,
maximum assignment degree 168,
36,150 Hamilton-compatible constraint triangles,
33,954 frustrated compatible triangles.
```

Compile and run

```bash
g++ -O3 -std=c++17 \
  scripts/check_hamilton_parity_constraint_incidence_growth.cpp \
  -o /tmp/check_hamilton_parity_constraint_incidence_growth
/tmp/check_hamilton_parity_constraint_incidence_growth
```

The ledger is

```text
experiments/hamilton-parity-constraint-incidence-growth-audit.json.
```

## 6. Revised signed-cycle frontier

The pair-safe cycle supplied by PP3bmu has only logarithmically many parity
edges.  The next steps are therefore finite-defect rather than dense-graph
problems:

1. prove that a pair-safe `O(log m)` parity graph can be made consistent by a
   bounded or logarithmic number of clean successor rotations;
2. bound the probability or expected number of frustrated signed cycles, not
   merely parity edges;
3. classify the high-degree assignment vertices visible in the exact audit;
4. construct a biased Hamilton measure suppressing the remaining frustrated
   cycle patterns while retaining exact path-forest cylinders;
5. combine sparse parity instances with the weighted merged-charge transport
   problem.
