# State-churn concentration and constant-mask host drift

**Branch:** `research/alternating-core-chain`

AC3hx erases exact selected-state loops, while AC3ig--AC3ip control a fixed
cell once one removal/return cross recurs.  This note supplies the missing
quantitative bridge.  Every nontrivial change of a permutation matching inserts
at least two cells.  Hence a long simple two-layer history has large exact
layer-cell churn, and one physical layer-cell is repeatedly inserted and
removed.  Its removal episodes have only `L(n-1)^2` possible decorated cross
signatures, so the long-return router activates after an explicit polynomial
number of state changes.

The final theorem also separates strict monotone-mask growth from genuine
state-derived host drift.  Pure mask growth can occur only finitely many times.

## Churn notation

Let

\[
S_0,S_1,\ldots,S_N,
\qquad
S_t=(M_t^0,M_t^1),
\]

be an ordered two-layer history on an `n x n` board.  Consecutive states are
distinct.  For layer `ell` and cell `z`, let

\[
I_{\ell,z}
=
|\{t:z\in M_{t+1}^\ell\setminus M_t^\ell\}|
\]

and

\[
D_{\ell,z}
=
|\{t:z\in M_t^\ell\setminus M_{t+1}^\ell\}|.
\]

Let

\[
C^+=\sum_{\ell,z}I_{\ell,z}
\]

be total inserted layer-cell incidence.

## AC3iq -- every new two-layer state pays two cell insertions -- PROVED

For every nontrivial transition `S_t -> S_{t+1}`,

\[
\sum_{\ell=0}^1
|M_{t+1}^\ell\setminus M_t^\ell|
\ge2.
\]

Consequently

\[
\boxed{C^+\ge2N.}
\]

One exact layer-cell satisfies

\[
\boxed{
I_{\ell,z}
\ge
\left\lceil\frac{N}{n^2}\right\rceil.
}
\]

For every layer-cell,

\[
\boxed{D_{\ell,z}\ge I_{\ell,z}-1.}
\]

### Proof

If one permutation layer changes, the symmetric difference of its old and new
matchings is a nonempty union of even alternating cycles.  The shortest such
cycle has four edges, so the new matching inserts at least two cells.  At least
one layer changes in every nontrivial ordered-state transition.  Summing gives
`C^+>=2N`.

There are `2n^2` layer-cell identities, so one receives at least
`ceil(C^+/(2n^2))>=ceil(N/n^2)` insertions.

For a fixed layer-cell, presence along the linear history is a binary word.
Insertions and removals alternate, and their counts differ by at most one.
Thus `D>=I-1`. QED.

## AC3ir -- one fixed removal cross recurs -- PROVED

Assume every state-change episode carries one of `L` finite role labels.  Fix
the layer-cell from AC3iq and put

\[
T=L(n-1)^2.
\]

Every removal of that cell has one canonical AC3hy cross signature.  Therefore
one decorated removal cross occurs at least

\[
\boxed{
r
\ge
\left\lceil
\frac{(I_{\ell,z}-1)_+}{T}
\right\rceil
}
\]

times.

For this cross, AC3ig gives a long return cross occurring at least

\[
\boxed{
q
\ge
\left\lceil
\frac{(r-1-T)_+}{T}
\right\rceil
}
\]

times, unless the selected returns are absorbed by the finite capacity-one
rectangle-ticket stock.

### Proof

There are `n-1` choices for the new row in the fixed cell's column, `n-1`
choices for the new column in its row, and `L` role labels.  Pigeonhole the
`D>=I-1` removals over these `T` signatures.  Apply AC3ig to the selected
signature. QED.

## AC3is -- polynomial simple-history threshold -- PROVED

Fix an integer `lambda>=1` and put

\[
T=L(n-1)^2,
\]

\[
\boxed{
H(n,L,\lambda)
=
n^2\bigl(\lambda T^2+T+1\bigr).
}
\]

Every simple ordered two-layer history of `N` nontrivial changes satisfies one
of:

1. **Polynomially bounded history:**
   \[
   \boxed{N\le H(n,L,\lambda).}
   \]
2. **Repeated two-cross long return:** one exact layer-cell, one decorated
   removal cross and one decorated long return cross occur in at least
   \[
   \boxed{\lambda}
   \]
   selected return episodes.

The second output enters AC3ik and AC3ip: it yields a common-host executable
cycle menu or an explicit host-drift profile.

### Proof

Suppose the second alternative fails.  For the cell selected by AC3iq, AC3ir's
long-return multiplicity is below `lambda`.  Hence

\[
\left\lceil\frac{(r-1-T)_+}{T}\right\rceil
\le\lambda-1,
\]

so

\[
r\le\lambda T+1.
\]

Since

\[
r\ge
\left\lceil\frac{I-1}{T}\right\rceil,
\]

we obtain

\[
I\le\lambda T^2+T+1.
\]

AC3iq gives `ceil(N/n^2)<=I`, proving the displayed bound. QED.

The safe order is `O(lambda L^2 n^6)`.  No factorial state count is used.

## Constant-mask intervals

Let `R` be a finite unavailable-resource universe of size `B`, and let

\[
F_0\subseteq F_1\subseteq\cdots\subseteq F_N\subseteq R
\]

be the monotone masks of one fixed arithmetic/context and envelope epoch.  A
**strict mask step** has `F_t proper-subset F_{t+1}`.

There are at most `B` strict mask steps.  Removing those steps partitions the
remaining state changes into at most `B+1` constant-mask intervals.

## AC3it -- mask growth or fixed-mask host-drift localization -- PROVED

For every `lambda>=1`, put `H=H(n,L,lambda)`.  A fixed-context monotone-mask
epoch with `N` nontrivial state changes satisfies one of:

1. **Bounded epoch:**
   \[
   \boxed{
   N\le B+(B+1)H.
   }
   \]
2. **Repeated fixed-mask two-cross profile:** one constant-mask interval contains
   an exact removal/long-return two-cross profile of multiplicity at least
   `lambda`.

In alternative 2, AC3ip gives exactly one of:

- an executable arbitrary common-host cycle menu;
- a change of reference matching or opposite-layer exclusion between the
  historical occurrences;
- a state-derived allowed-host change not represented by the fixed mask.

Arithmetic/context and envelope-epoch changes are excluded by the theorem's
hypothesis; strict unavailable-mask growth has already been charged to the
finite budget `B`.  Thus the residual output is a literal state-derived host
profile, not generic mask drift.

### Proof

A strict inclusion adds at least one previously available resource to the mask,
so there are at most `B` strict steps.  If every constant-mask interval has at
most `H` nontrivial state changes, the total is at most `B+(B+1)H`.  Otherwise
one interval exceeds `H`; apply AC3is and then AC3ip. QED.

## Consequence

Inside one fixed arithmetic/context epoch, neither exact state loops, arbitrary
distinct-state churn nor monotone resource-mask growth remains an unquantified
AC4 obstruction.  A sufficiently long history returns one repeated two-cross
profile at fixed mask.  It then executes through a common-host cycle menu or
exposes a state-derived host change.

The next temporal target is finite ancestry/payment for those state-derived
host changes and for genuine arithmetic/context or envelope-epoch changes.

## Finite check

`scripts/verify_ac_state_churn_router.py` exhausts permutation changes through
side six, binary cell-presence histories, cross-signature pigeonholes,
polynomial threshold identities, monotone mask-size chains and every displayed
composition bound.
