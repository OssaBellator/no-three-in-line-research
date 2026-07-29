# Heavy-neighborhood concentration for failed RI subbanks

**Branch:** `research/rational-inverse-expansion`

RI5br--RI5bu extract physical I6 subbanks from independent sets of the component conflict graph. This note gives an exact weighted witness when a requested subbank cardinality does not exist.

Let `J=(V,E)` be the RI component conflict graph. Give each component a nonnegative paid weight `w(v)` and write

\[
W=w(V)=\sum_{v\in V}w(v).
\]

For `v in V`, let `N[v]` denote its closed conflict neighborhood.

## RI5bv -- maximal independent neighborhoods cover the inventory -- PROVED

If `I` is a maximal independent set of `J`, then

\[
\boxed{V=\bigcup_{v\in I}N[v].}
\]

### Proof

If some vertex `x` lay outside every `N[v]`, then `x` would be nonadjacent to every member of `I`, so `I union {x}` would be independent, contradicting maximality. QED.

## RI5bw -- failed-cardinality neighborhood concentration -- PROVED

Fix an integer `q>=2`. If `J` has no independent set of size `q`, then there exists a component `v` with

\[
\boxed{w(N[v])\ge \frac{W}{q-1}.}
\]

More precisely, every maximal independent set `I` has `|I|<=q-1`, and one member `v in I` satisfies the displayed bound.

### Proof

By RI5bv the closed neighborhoods indexed by `I` cover every vertex. Therefore

\[
W\le\sum_{v\in I}w(N[v]).
\]

Since `|I|<=q-1`, one summand is at least `W/(q-1)`. QED.

## RI5bx -- degree/weight dichotomy inside a heavy neighborhood -- PROVED

Let `v` be returned by RI5bw and fix `0<theta<1`. Put

\[
W_v=w(N[v]),\qquad
H_v=\{u\in N[v]:w(u)\ge \theta W_v/|N[v]|\}.
\]

Then one of the following holds:

1. one component in `N[v]` has paid weight at least `theta W_v/|N[v]|`;
2. the complementary light components have total weight greater than `(1-theta)W_v` and every one of them has weight below `theta W_v/|N[v]|`.

In particular the failed subbank is localized either to one individually heavy conflicting component or to a quantitatively heavy cloud of individually small conflicts around one center.

### Proof

If `H_v` is nonempty, branch 1 holds. If it is empty, every component is below the threshold and the entire neighborhood is the light cloud, of weight `W_v>(1-theta)W_v`. The stated weaker lower bound follows. QED.

## RI5by -- heavy-neighborhood payment router -- PROVED

For a requested `q`-component physical bank, exactly one of the following holds:

1. an independent set of size at least `q` gives a physical I6 subbank by RI5br;
2. one closed conflict neighborhood has paid weight at least `W/(q-1)`;
3. one local replacement, injectivity, ownership or exterior-field hypothesis fails on an otherwise independent family.

The neighborhood output is a finite physical object: one center component, its conflicting components, and the least conflict type on every incident edge. It may be paid by overlap destruction, cross-constraint concentration, owner concentration or one capacity-one conflict ticket.

### Proof

Take a maximal independent set. If it has size at least `q`, use branch 1. Otherwise RI5bw gives branch 2. Any failure of the physical-bank hypotheses is branch 3. QED.

## Corrected RI6 frontier

The absence of a large disjoint RI bank is no longer a global graph failure. It produces one heavy closed conflict neighborhood carrying at least a `1/(q-1)` fraction of the total paid component weight. Remaining work is to pay or ticket that neighborhood by its overlap, cross-constraint, owner or occurrence labels, together with repeated-coset correlations, blocker repair and replenishable-source recurrence.

## Finite check

`scripts/verify_ri_conflict_neighborhood_concentration.py` exhausts small weighted conflict graphs, verifies maximal-neighborhood covering and the `W/(q-1)` concentration bound.