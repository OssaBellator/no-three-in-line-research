# Sequential local lemma for row-lift reservoir banks

The row-lift bank from PP3i has strong spread, but its full support may contain
many geometric certificates. This chapter replaces the global first-moment
support count by a local, prefix-dependent selection theorem.

The key point is that no product-space dependency theorem is needed. The four
permutation layers are exposed one at a time. At each stage, the ordinary
Lu--Szekely negative dependency graph for one random permutation is applied to
exactly those certificates completed by the current layer.

## 1. Four unconditioned permutation layers

Use the notation of the row-lift construction. Before imposing any collision
restrictions, expose four independent permutations:

1. a red movement bijection from the red deleted points to the new rows;
2. a blue movement bijection from the blue deleted points to the new rows;
3. a first refill bijection from the deleted old rows to the new columns;
4. a second refill bijection on the same domain and codomain.

A layer assignment is an edge

\[
(\ell,i,j),
\]

meaning that domain element `i` in layer `ell` is sent to codomain element `j`.
It determines one grid cell.

Define the following layer-labelled canonical certificates:

- a red and blue deleted point from the same old column sent to the same new
  row;
- the two refill layers sending one old row to the same new column;
- a selected cell on a secant through two retained points;
- two selected cells whose line contains a retained point;
- three selected cells in distinct rows and columns that are collinear.

In the last three cases, include every compatible choice of layer assignments
realising the projected cells. Each certificate contains at most three
permutation edges. A complete four-layer state is an executable no-three patch
if and only if it contains none of these certificates.

## 2. One-stage canonical avoidance

Let a single layer be a uniformly random permutation of `[t]`. Let `mathcal E`
be a family of distinct nonempty partial matchings in `K_{t,t}`, each of size
at most three. For a domain or codomain vertex `v`, define

\[
L(v)=
\sum_{E\in\mathcal E:\,v\in V(E)}
\frac1{(t)_{|E|}}.
\]

### Lemma PP3k -- PROVED

If

\[
\max_v L(v)\le\frac1{24},
\]

then some permutation contains none of the partial matchings in `mathcal E`.

#### Proof

For `E in mathcal E`, let `A_E` be the event that a uniform permutation
contains `E`. Then

\[
\Pr(A_E)=\frac1{(t)_{|E|}}.
\]

The canonical conflict graph is a negative dependency graph in permutation
space. Put

\[
x_E=2\Pr(A_E).
\]

Each event uses at most six domain/codomain vertices. Any conflicting event
meets one of those vertices, so

\[
\sum_{F\sim E}x_F
\le
2\sum_{v\in V(E)}L(v)
\le
12\cdot\frac1{24}
=
\frac12.
\]

Therefore

\[
x_E\prod_{F\sim E}(1-x_F)
\ge
2\Pr(A_E)
\left(1-\sum_{F\sim E}x_F\right)
\ge
\Pr(A_E).
\]

The lopsided Lovasz local lemma gives a permutation avoiding every event. ∎

## 3. Activated certificates under a prefix

Fix an order `lambda_1,...,lambda_4` of the four layers. A prefix is a choice of
permutations in the first `s-1` layers. It is **legal** when it contains no
certificate supported entirely in those exposed layers.

For a legal prefix at stage `s`, a certificate is **activated** when:

- its latest layer in the chosen order is `lambda_s`; and
- every assignment belonging to an earlier layer is present in the prefix.

Delete the already fixed assignments from every activated certificate. The
remaining assignments form a nonempty partial matching in the current layer.
Identical partial matchings are identified, since avoiding one avoids every
certificate that produced it.

Let `L_s(v;P)` be the PP3k vertex load of this activated event family for legal
prefix `P`.

### Theorem PP3l -- PROVED

Suppose an ordering of the four row-lift layers satisfies

\[
\boxed{
\max_{s,P,v} L_s(v;P)\le\frac1{24},
}
\]

where `P` ranges over every legal prefix before stage `s`. Then the row-lift
reservoir has an executable no-three-in-line patch.

#### Proof

Proceed through the chosen layer order. The empty prefix is legal. Given a
legal prefix before stage `s`, apply PP3k to the distinct activated partial
matchings in layer `lambda_s`. The load hypothesis gives a permutation avoiding
all of them.

Appending this permutation preserves legality: every certificate whose latest
layer is `lambda_s` would have produced one of the avoided activated events,
and certificates using later layers are not yet complete. Induction chooses
all four layers. The final state contains no duplicate-cell or geometric
certificate, so it is an executable patch. ∎

This is stronger in form than PP3j. PP3j pays for every certificate in the
whole support. PP3l only pays for the distinct current-layer events activated
by one legal prefix, and measures their maximum local assignment load.

### Corollary PP3m -- PROVED

If a row-lift reservoir has no clean state, then for every ordering of its four
layers there are a stage, a legal prefix, and a permutation vertex with

\[
L_s(v;P)>\frac1{24}.
\]

Thus failure produces a localized assignment obstruction rather than merely a
large global support count.

## 4. Exact finite obstruction at side three

The script `scripts/analyze_row_lift_sequential_loads.py` constructs all
layer-labelled certificates, enumerates every legal prefix, and evaluates the
load in PP3l. It is exhaustive for two or three reservoir rows.

### Proposition PP3n -- PROVED BY EXHAUSTIVE FINITE CHECK

For the stored side-three certificate, delete all three old rows and use the
full width-three row-lift bank. Then:

- the canonical layer-labelled family has `290` distinct certificates;
- no complete clean four-layer state exists;
- every one of the `24` layer orders violates the PP3l threshold;
- the best order has maximum activated vertex load `13/6`;
- in that order, the legal-prefix counts are `1,4,4,0`, so the obstruction is
  completed before the fourth layer.

The certificate family consists of `9` movement-collision events, `9`
refill-collision events, and `272` compatible internal-triple events. There are
no retained-core events because all old points are deleted.

### Candidate design PP3-R3 -- REFUTED

The unrestricted full row-lift bank is not automatically clean, even when the
retained core is empty. The side-three instance above has no state avoiding all
internal triples.

This does not refute the row-lift architecture. It isolates the required
additional ingredient: choose reservoir rows with controlled directions, or
restrict each permutation layer so the activated local loads stay below the
PP3l threshold.

## 5. Revised geometric target

A successful row-lift PP3 theorem may now use either of two quantified routes:

1. prove the global certificate inequality PP3j for a direction-pruned support;
2. prove the sequential local-load inequality PP3l for some layer order.

The second route can tolerate many certificates globally when they are not
simultaneously activated at one permutation vertex. It is therefore the more
promising endpoint for structured algebraic or tomographic subbanks.
