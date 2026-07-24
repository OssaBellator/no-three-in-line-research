# Row-lift pruning barriers and static sequential endpoints

This chapter isolates what a scalable row-lift preparation theorem must prune.
It proves that the global support-count criterion cannot certify the full bank,
removes legal-prefix enumeration from the sequential local-load endpoint, and
gives a collision-conditioned sequential first-moment alternative.

Throughout, the four row-lift permutation layers are denoted

1. `red-move`;
2. `blue-move`;
3. `refill-a`;
4. `refill-b`.

The two movement layers form one collision pair and the two refill layers form
the other.

## 1. Full-support candidate triples are an asymptotic barrier

For a width-`t` row-lift reservoir, the union of the supports of either refill
layer is the full rectangle

\[
X^+\times Y,
\]

which is a translated copy of `[t]^2`.

### Proposition PP3o -- PROVED

Let `mathcal T` be the set of nonaxis collinear triples with distinct rows and
columns in the support of the unpruned row-lift bank. Then

\[
|\mathcal T|=\Omega(t^4\log t).
\]

Consequently the PP3j support-count expression satisfies

\[
\frac{72|\mathcal T|}{(t)_3}=\Omega(t\log t),
\]

and is larger than one for every sufficiently large `t`. Thus PP3j cannot
certify the unpruned full row-lift bank asymptotically, even when the retained
core contributes no blocked cells or anchored pairs.

#### Proof

The refill support contains a translated full `t x t` grid. The candidate-only
triple lower bound S3, applied at density one, gives
`Omega(t^4 log t)` nonaxis collinear triples; the logarithmic contribution comes
from nonaxis primitive direction scales.

Every such triple has distinct old rows and distinct new columns. It therefore
has a compatible layer realisation using the two refill permutation layers:
assign any two cells to one refill layer and the third to the other. The two
same-layer assignments have distinct domains and codomains. Hence every triple
is represented in the row-lift canonical family and contributes to
`mathcal T`. Dividing by `(t)_3` gives the second assertion. ∎

This does not refute row-lift banks. It refutes a constant-density, unpruned
support combined with a global first-moment count. A scalable bank must restrict
its layer supports or use activated local structure.

## 2. Static latest-layer local loads

Fix an ordering `lambda_1,...,lambda_4` of the four layers. For every canonical
certificate `C`, let its **terminal stage** be the largest position of a layer
appearing in `C`. At that stage delete all assignments in earlier layers and
retain the nonempty partial matching in the terminal layer.

For stage `s`, let `mathcal R_s` be the set of all distinct residual partial
matchings obtained this way, without requiring that their earlier assignments
occur together in one legal prefix. For a domain or codomain vertex `v` of the
current permutation, put

\[
\Lambda_s(v)=
\sum_{E\in\mathcal R_s:\,v\in V(E)}\frac1{(t)_{|E|}}.
\]

### Corollary PP3p -- PROVED

If some layer order satisfies

\[
\boxed{
\max_{s,v}\Lambda_s(v)\le\frac1{24},
}
\]

then the row-lift reservoir contains an executable no-three-in-line patch.

#### Proof

For any legal prefix before stage `s`, the activated event family from PP3l is
a subset of `mathcal R_s`: PP3p includes residual events even when their earlier
assignments are absent or mutually incompatible. Therefore every activated
vertex load is at most `Lambda_s(v)`. The hypothesis implies the PP3l condition,
which completes the four layers sequentially. ∎

PP3p is more conservative than PP3l but is static. It requires no enumeration
of legal prefixes and can be checked for substantially larger widths.

## 3. Conditioning away duplicate-cell constraints

The local-load theorem PP3l treats movement and refill collisions as bad events.
They have additional structure and can instead be removed from the sampling
space.

Call an order **pair-respecting** when, in each collision pair, one layer is
designated first and its partner is exposed later. The first layer is chosen
from all permutations. Once it is fixed, the second layer is chosen uniformly
from permutations avoiding the induced forbidden-position matching:

- for movement, matched red and blue points from the same old column may not use
  the same new row;
- for refill, the two layers may not send one old row to the same new column.

The forbidden positions form a matching. PP3g therefore gives, for every
compatible current-layer partial matching `E`,

\[
\Pr(E)\le
\begin{cases}
1/(t)_{|E|},&\text{for the first layer of its pair},\\
3/(t)_{|E|},&\text{for the conditioned second layer}.
\end{cases}
\]

Let `mathcal G_s(P)` be the distinct activated **geometric** residual events at
stage `s` under a legal prefix `P`; duplicate-cell certificates are omitted
because the conditioned sampling spaces already exclude them. Put `kappa_s=1`
for a first layer and `kappa_s=3` for a conditioned second layer, and define

\[
\Phi_s(P)=
\sum_{E\in\mathcal G_s(P)}
\frac{\kappa_s}{(t)_{|E|}}.
\]

### Theorem PP3q -- PROVED

Suppose a pair-respecting layer order satisfies

\[
\boxed{
\max_{s,P}\Phi_s(P)<1,
}
\]

where `P` ranges over every legal prefix generated in the conditioned sampling
spaces. Then the row-lift reservoir contains an executable no-three-in-line
patch.

#### Proof

Proceed through the layer order. For a legal prefix before stage `s`, sample the
current layer uniformly from all permutations if it is first in its pair, and
from the appropriate one-matching-avoiding permutations if it is second.

Let `Z_s` count activated geometric residual events contained in the sampled
permutation. By the ordinary permutation probability and PP3g respectively,

\[
\mathbb E Z_s\le\Phi_s(P)<1.
\]

Since `Z_s` is a nonnegative integer, some allowed permutation has `Z_s=0`.
Appending it keeps the prefix legal: collision certificates are excluded by the
sampling space, geometric certificates terminal at this stage were avoided,
and certificates using later layers are incomplete. Induction selects all four
layers. ∎

Unlike PP3l, this theorem has threshold one and does not pay singleton load for
the two collision matchings. It uses a global activated-event mass rather than
a local vertex load.

## 4. Static conditioned mass

For a pair-respecting order, let `mathcal G_s^*` contain every distinct geometric
residual event whose terminal layer is the stage-`s` layer, again without
requiring its earlier assignments to occur in one prefix. Define

\[
\Phi_s^*=\sum_{E\in\mathcal G_s^*}
\frac{\kappa_s}{(t)_{|E|}}.
\]

### Corollary PP3r -- PROVED

If some pair-respecting order satisfies

\[
\boxed{
\max_s\Phi_s^*<1,
}
\]

then the row-lift reservoir contains an executable no-three-in-line patch.

#### Proof

For every legal prefix, `mathcal G_s(P)` is a subset of `mathcal G_s^*`, so
`Phi_s(P)<=Phi_s^*`. Apply PP3q. ∎

The script `scripts/analyze_row_lift_static_pruning.py` computes PP3p and PP3r
for all layer orders without enumerating permutations or legal prefixes.

## 5. Revised scalable target

The full row-lift support cannot pass PP3j because one refill rectangle already
has the candidate-only logarithmic triple accumulation. The remaining viable
row-lift targets are therefore:

1. a sparse or algebraic restriction of each permutation layer whose static
   terminal loads pass PP3p;
2. a collision-conditioned bank whose static mass passes PP3r;
3. a less uniform bank that fails both static tests but passes the prefix-aware
   PP3l or PP3q criterion.

This turns “prune the bank” into two explicit quantities: terminal vertex load
and terminal conditioned event mass.