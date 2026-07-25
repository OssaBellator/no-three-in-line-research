# Target destruction converts recurrent owner witnesses into the next closure bank

CMR691--CMR697 reduce every unbounded strict factor execution to recurrence of
one exact owner edge or one exact forced certificate. This chapter attaches
those final recurrence endpoints to the inherited target-load closure.

The key point is elementary but exact. If a saturated-state transition destroys
`D` designated old triples and does not lower potential, it must create at least
`D` genuinely new triples. Every new triple contains an entering selected cell.
One entering cell therefore carries a positive fraction of the destroyed target
load, and a four-endpoint move centred at that cell destroys the whole assigned
family in every completion.

Fix two saturated selected states `S` and `S'` of the same cardinality. Put

\[
A=S'\setminus S,
\qquad
B=S\setminus S',
\]

and write

\[
c=|A|=|B|.
\]

Let `Phi(S)` denote the number of real collinear triples in `S`. Let
`mathcal Q` be a family of `D>=1` distinct real triples contained in `S` and not
contained in `S'`.

## 1. Exact target-destruction identity

For any state `U`, let `mathcal T(U)` be its set of real collinear triples.
Define

\[
\mathcal N(S',S)
=
\mathcal T(S')\setminus\mathcal T(S),
\qquad
\mathcal L(S,S')
=
\mathcal T(S)\setminus\mathcal T(S').
\]

### Theorem CMR698 -- PROVED

One has

\[
\boxed{
\Phi(S')-\Phi(S)
=
|\mathcal N(S',S)|-|\mathcal L(S,S')|
}.
\]

Moreover every triple in `mathcal N(S',S)` contains an entering cell from `A`.
Since `mathcal Q` is a subset of `mathcal L(S,S')`, if

\[
\Phi(S')\ge\Phi(S),
\]

then

\[
\boxed{|\mathcal N(S',S)|\ge D.}
\]

### Proof

The real triples in the two states split into their common part, those present
only in `S`, and those present only in `S'`. Subtracting the two cardinalities
gives the identity. A triple contained in `S'` but not in `S` must use at least
one cell of `S'\setminus S=A`. Finally, every designated target belongs to the
lost family, so nonnegative potential change forces at least as many new triples
as lost triples and hence at least `D`. ∎

This is the current-state analogue of the baseline-difference identity CMR133.

## 2. One entering cell inherits target load

For an entering cell `e` in `A`, put

\[
\ell(e)
=
|\{T\in\mathcal N(S',S):e\in T\}|.
\]

### Theorem CMR699 -- PROVED

Under the nonimproving hypothesis of CMR698, one entering cell satisfies

\[
\boxed{
\ell(e)\ge
\left\lceil\frac{D}{c}\right\rceil.
}
\]

More generally, if `N=|mathcal N(S',S)|`, then some entering cell has load at
least `ceil(N/c)`.

### Proof

Assign every new triple to one entering cell which it contains. The `N`
assignments are distributed over the `c` entering cells. Averaging gives one
cell with at least `ceil(N/c)` assigned triples, and CMR698 gives `N>=D`. ∎

Thus target destruction and selected-state churn obey an exact concentration
law rather than an anonymous potential inequality.

## 3. Edge-centred four-endpoint handoff

Let `U` be any saturated current state, let `e` be a selected cell of `U`, and let

\[
\mathcal T_e
\subseteq
\mathcal T(U)
\]

be any family of `d'>=1` current triples, every one containing `e`. Assume the
ambient saturated board has side at least four.

### Theorem CMR700 -- PROVED

There is a four-endpoint alternating bank in the permutation layer containing
`e` such that every bank state

1. moves `e`;
2. preserves saturation and layer disjointness;
3. destroys every triple in `mathcal T_e`.

Consequently the bank has certified target load `d'`. Applied to the cell and
assigned family supplied by CMR699, one may take

\[
\boxed{d'\ge\left\lceil\frac{D}{c}\right\rceil.}
\]

### Proof

Choose `e` and three further selected points in its permutation layer. The
forbidden matching board consists of their four old cells together with cells
occupied by the opposite layer, so every board row and column has forbidden
degree at most two. CMR128 supplies an allowed perfect matching. Every allowed
state moves all four chosen endpoints, in particular removing `e`. Every triple
in `mathcal T_e` contains `e`, so all are destroyed. ∎

The new target family is simultaneous in one current state; it is not assembled
from triples occurring at different historical times.

## 4. Internal handoff or strict envelope expansion

Assume the bank of CMR700 is installed as a closure-compatible rematching and
let `E` be the closure envelope immediately before that bank. Assume the column
of `e` already lies in `E`, as it does for the entering cell supplied by CMR699
after its transition.

### Theorem CMR701 -- PROVED

Exactly one of the following implementations is available.

1. **Internal handoff.** If `E` contains at least four columns, choose all four
   endpoints of CMR700 inside `E`. The closure envelope does not change.
2. **Strict expansion.** If `E` contains fewer than four columns but the ambient
   board has side at least four, any four-endpoint padding uses a column outside
   `E`. The next closure envelope strictly expands and its depth decreases.
3. **Finite base.** If the ambient board itself has side below four, the state is
   one of the finite base cases outside the universal CMR128 range.

### Proof

A saturated permutation layer contains one selected point in every column. In
the first branch, choose the three padding columns inside `E`; adding no moved
column outside the current envelope leaves its least containing prefix block
unchanged. In the second branch, three additional distinct endpoint columns
cannot all lie inside `E`, so the moved-column history gains a column outside
`E`; CMR174 gives strict depth decrease. The final branch is definitional. ∎

Hence target handoff either remains under the same inherited parent or spends
one unit of the finite closure-envelope budget.

## 5. Multiplicative target-load loss is paid by churn

Consider a sequence of nonimproving target handoffs. At step `i`, let `D_i` be
the destroyed target load, let `c_i>=1` be the number of entering cells, and let
`D_{i+1}` be the certified load selected by CMR700.

### Theorem CMR702 -- PROVED

For every step,

\[
\boxed{D_i\le c_iD_{i+1}.}
\]

Consequently, after `r` handoffs,

\[
\boxed{
D_0
\le
D_r\prod_{i=0}^{r-1}c_i.
}
\]

Whenever `D_r<D_0`, the logarithmic loss obeys

\[
\boxed{
\log\frac{D_0}{D_r}
\le
\sum_{i=0}^{r-1}\log c_i
\le
\sum_{i=0}^{r-1}(c_i-1).
}
\]

The entering edges also carry exact labelled nonroot full-token incidence

\[
\boxed{
(p+1)(h-1)\sum_i c_i.
}
\]

### Proof

CMR700 gives `D_{i+1}>=ceil(D_i/c_i)`, hence `D_i<=c_iD_{i+1}`.
Multiply over the steps. Taking logarithms gives the first displayed
inequality; `log x<=x-1` gives the second. The token formula is CMR413 applied
with multiplicity. ∎

In particular, a one-edge nonimproving handoff cannot reduce target load.

## 6. Forced child certificates are target banks, not terminal loops

Let `T` be the forced cross-child certificate from CMR684. Thus `T` is a real
collinear triple contained in every state of one fixed child product.

### Theorem CMR703 -- PROVED

Choose any product state and any cell `e` in `T`. CMR700 with target family
`{T}` gives a four-endpoint bank of certified target load one. The bank is
internal to the current envelope when four columns are available there, and
otherwise spends a strict envelope expansion as in CMR701.

Therefore the forced-certificate branch of CMR690 enters the existing
four-endpoint one-target closure. It is terminal only inside the fixed product
class, not in the full alternating closure.

### Proof

The certificate is present in the chosen saturated state. Moving any one of its
three cells destroys it. Apply CMR700 and then CMR701. ∎

This conversion does not assert that the next bank immediately improves; it
places the obstruction back into the inherited target-load mechanism.

## 7. Productive recurrent owner edges have finite triple stock

Fix one owner stage in an ambient board of side `N` and one physical entering
cell `e`. Call an episode **productive** when a nonimproving target-destroying
transition canonically assigns to `e` one new real triple containing `e`.

### Theorem CMR704 -- PROVED

The number of physical triple signatures containing `e` is at most

\[
\boxed{
\binom{N^2-1}{2}.
}
\]

For every integer `lambda>=2`, a history of `J` productive episodes using the
same owner edge `e` satisfies at least one of:

1. one exact physical triple occurs in at least `lambda` episodes;
2. 
   \[
   \boxed{
   J
   \le
   (\lambda-1)\binom{N^2-1}{2}.
   }
   \]

At the first occurrence of any selected triple in a current saturated state,
CMR700 already supplies the next target bank. Exact recurrence merely prevents
the same triple from being charged as fresh under the same owner.

### Proof

After fixing `e`, choose the other two cells of the triple from the remaining
`N^2-1` physical grid cells. This overcounts noncompatible and noncollinear
choices. The recurrence alternative is the pigeonhole principle. The handoff
statement is CMR700. ∎

A recurrent routing edge which is never productive cannot support a
nonimproving transition that destroys a positive target family, by CMR698.

## 8. Descending-path potential-conversion endpoint

### Corollary CMR705 -- PROVED

Consider a canonical descending execution CMR697 embedded in an alternating
closure, with the additional bank hypothesis that every installed product state
destroys the current positive designated target family. Every continuation
reaches at least one of the following.

1. A saturated state of strictly lower triple potential.
2. A finite matching-preserving deletion, contraction, or routing-history stock.
3. Strict recursion into a smaller child factor and smaller prefix envelope.
4. A forced certificate converted by CMR703 into a target-load-one bank.
5. A nonimproving target-destroying transition converted by CMR699--CMR701 into a
   new target bank of load at least `ceil(D/c)`.
6. A recurrent productive owner edge or exact triple signature, already
   owner-labelled by CMR694 and CMR704.
7. A strict closure-envelope expansion, available at most `h` times.

All target-load loss in branches 4--6 is paid by entering-edge churn through
CMR702. Hence the remaining prime-power gap is confined to repeated internal
target handoffs inside one fixed envelope after the finite structural, routing,
and expansion stocks are exhausted.

### Proof

Apply CMR697. Any installed product state which improves gives branch 1. Finite
structural alternatives give branch 2, and strict child descent gives branch 3.
Convert forced certificates using CMR703. For every other nonimproving
target-destroying transition apply CMR698--CMR701. CMR704 handles owner-edge
recurrence and CMR174 bounds strict envelope expansions. The churn payment is
CMR702. ∎

This does not prove the all-`n` conjecture. It removes the forced-certificate and
recurrent-owner-edge endpoints as anonymous loops. The active theorem is now a
fixed-envelope target-bank aggregation: show that repeated internal handoffs
force inherited target-load descent, protected-reserve depletion, permanent
deletion ancestry, full-token return, or a baseline improvement.

The finite set identities, load concentration, edge-centred destruction,
multiplicative target ledger, and triple-stock arithmetic are checked in
[`scripts/verify_prime_power_target_handoff_conversion.py`](../scripts/verify_prime_power_target_handoff_conversion.py).
