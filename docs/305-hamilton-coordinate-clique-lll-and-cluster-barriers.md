# Hamilton coordinate-clique barriers for LLL and cluster expansion

The exact Hamilton cylinder probabilities from `docs/302` invite a local-lemma
argument on bad triple events.  This chapter shows that the naive dependency
graph based only on shared source or target pair coordinates retains the same
logarithmic obstruction as the earlier permutation models.  The obstruction is
stronger than failure of the symmetric Lovasz local lemma: the standard
cluster-expansion criterion fails on one large coordinate clique even with
arbitrary event weights.

## 1. The coordinate-overlap event graph

Let `E_n` be the family of strongly generic same-layer collinear triple events
from PP3bje in the signed Hamilton measure.  Every event prescribes three signed
directed pair edges and therefore uses three source-pair coordinates and three
target-pair coordinates.

Define the coordinate-overlap graph `G_n` by joining two events whenever their
source sets intersect or their target sets intersect.

### Proposition PP3bjq -- PROVED

The graph `G_n` contains a clique of size

```text
Q_n = Omega(n^3 log n).
```

Every event in the full Hamilton measure has probability

```text
p_n = 1/[8(m-1)_3] = Theta(n^-3),
```

where `m=n/2`.  Consequently

```text
p_n Q_n = Omega(log n).
```

The same conclusion holds in the one-fixed near-Hamilton measure, uniformly over
strongly generic events.

#### Proof

PP3bje gives

```text
|E_n| = Theta(n^4 log n).
```

Every event has three source coordinates, so the total number of event-source
incidences is `3|E_n|`.  There are `m=n/2` source coordinates.  Some source
coordinate therefore belongs to at least

```text
3|E_n|/m = Omega(n^3 log n)
```

events.  Those events form a clique in `G_n`.  PP3bjc gives the displayed full
Hamilton probability.  PP3bjd gives probability `Theta(n^-3)` uniformly in the
one-fixed model because a strongly generic triple uses between four and six pair
vertices. ∎

## 2. Symmetric local lemma failure

### Corollary PP3bjr -- PROVED / LOGARITHMIC BARRIER

The symmetric Lovasz local lemma applied to `G_n` fails by a factor
`Omega(log n)` in both Hamilton measures.

#### Proof

An event in the clique of PP3bjq has dependency degree at least `Q_n-1`.  The
usual symmetric criterion requires

```text
e p_n (Q_n) <= 1.
```

But `p_n Q_n=Omega(log n)`. ∎

This does not rule out a substantially smaller lopsided graph.

## 3. Arbitrary-weight cluster-expansion failure on the same graph

### Theorem PP3bjs -- PROVED / COORDINATE-GRAPH BARRIER

The standard cluster-expansion local-lemma criterion cannot certify the event
family on `G_n`, even with arbitrary positive event weights.

#### Proof

Let `C` be the coordinate clique from PP3bjq, of size `Q_n`.  Suppose positive
weights `y_A` satisfy a cluster-expansion criterion of the form

```text
Pr(A) <= y_A / Psi_A(y),
```

where `Psi_A` is the independent-set polynomial of the closed neighborhood of
`A`.  For every `A in C`, the closed neighborhood contains all of `C`.  Since
`C` is a clique, its empty set and all singleton sets contribute, so

```text
Psi_A(y) >= 1 + sum_(B in C) y_B.
```

Put `S=sum_(B in C)y_B`.  In the full Hamilton measure all events in `C` have the
same probability `p_n`.  Summing the criterion over `A in C` gives

```text
Q_n p_n <= S/(1+S) < 1,
```

contradicting `Q_n p_n=Omega(log n)` for large `n`.

In the one-fixed measure, all strongly generic event probabilities are bounded
below by a constant multiple of `n^-3`; the same sum with the minimum clique
event probability gives the same contradiction. ∎

## 4. Revised cluster frontier

The exact path-forest cylinders remain useful, but a successful cluster or
lopsided argument must discard almost all coordinate-sharing adjacencies or
change the measure.  In particular it must exploit geometric facts beyond the
six source/target coordinates of an event, such as:

1. incompatibility or negative correlation between different slopes;
2. cancellation from cyclic separation of the prescribed edges;
3. a biased cyclic-order measure suppressing high-incidence coordinates; or
4. a repair-generated witness structure smaller than the static overlap graph.

The theorem does not rule out such refined dependency notions, Shearer-optimal
criteria on a smaller graph, or algorithmic cluster arguments coupled to the
switching kernel.
