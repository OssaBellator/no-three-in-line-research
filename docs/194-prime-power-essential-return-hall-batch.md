# Essential target-edge returns expose Hall-deficiency deletion batches

CMR720--CMR726 attach one missing edge of a stored avoiding matching to every
essential return of a previously deleted target edge. Hall's theorem gives a
stronger certificate. Removing the essential returned edge leaves a
nonmatchable host. Any Hall-deficient source set then cuts not just one but the
full deficiency number of distinct edges from the stored avoiding matching.

Fix a balanced bipartite vertex set of side `m`. Let `M_0` be a stored perfect
matching avoiding a physical edge `e`. Let `H` be a later matchable host in
which `e` is essential. Put

\[
G=H-e.
\]

Then `G` has no perfect matching.

## 1. Hall witness after removing the essential returned edge

### Theorem CMR727 -- PROVED

There is a nonempty source set `X` with neighbour set

\[
Y=N_G(X)
\]

such that

\[
\boxed{|Y|<|X|.}
\]

Writing

\[
\delta=|X|-|Y|,
\]

one has `delta>=1`.

### Proof

Since `e` is essential in the matchable host `H`, deleting it destroys all
perfect matchings. Hall's theorem applied to `G=H-e` supplies `X` with the
stated deficiency. ∎

The set `(X,Y)` is an exact later-host obstruction, not an inherited geometric
approximation.

## 2. The stored avoiding matching contains a deleted batch of size delta

For the Hall witness CMR727, define

\[
F_{X,Y}
=
\{(x,M_0(x)):x\in X,\ M_0(x)\notin Y\}.
\]

### Theorem CMR728 -- PROVED

The set `F_{X,Y}` is a matching contained in the old stored matching `M_0`, every
edge of it is absent from the later host `H`, and

\[
\boxed{|F_{X,Y}|\ge\delta.}
\]

### Proof

The `|X|` matching targets `M_0(X)` are distinct. At most `|Y|` of them lie in
`Y`, so at least `|X|-|Y|=delta` lie outside `Y`. This proves the cardinality
bound and the matching property.

If `(x,M_0(x))` with `x` in `X` and `M_0(x)` not in `Y` belonged to `H`, then it
would belong to `G` because it is not `e`—the stored matching avoids `e`. Its
target would then lie in `N_G(X)=Y`, a contradiction. Thus every edge of the
batch is absent from `H`. ∎

An essential return therefore carries a deletion batch whose size is the Hall
deficiency.

## 3. Large deletion batch or thin Hall wall

Fix an integer threshold `r>=1`.

### Theorem CMR729 -- PROVED

Every essential return reaches exactly one of the following structural regimes.

1. **Large deletion ancestry.** The Hall deficiency satisfies `delta>=r`, and
   `F_{X,Y}` contains at least `r` distinct missing edges of `M_0`.
2. **Thin Hall wall.** One has `1<=delta<r`; the later avoiding host `G` has an
   explicit Hall-deficient cut of width `delta`, together with `delta` distinct
   missing stored-matching edges across the cut.

### Proof

Apply CMR728 and split according to the integer value of `delta`. ∎

The thin branch enters the existing Hall-wall, peeling, essential-factorisation,
and low-width signature machinery CMR199--CMR218 and CMR271--CMR305 whenever
its inherited geometric hypotheses are invoked.

## 4. Repeated large-deficiency episodes pack or concentrate

Consider `K` essential-return episodes relative to the same stored matching
`M_0`. In episode `j`, choose one Hall batch `F_j` from CMR728 and assume

\[
|F_j|\ge r.
\]

### Theorem CMR730 -- PROVED

For every integer `lambda>=2`, at least one of the following holds.

1. One exact edge of `M_0` belongs to at least `lambda` Hall batches.
2. 
   \[
   \boxed{
   K
   \le
   \left\lfloor
   \frac{(\lambda-1)m}{r}
   \right\rfloor.
   }
   \]

### Proof

The batch incidence is at least `Kr`. If no stored matching edge occurs
`lambda` times, each of the `m` edges contributes at most `lambda-1`
incidences. Therefore `Kr<=(lambda-1)m`. ∎

Thus many essential returns cannot repeatedly expose large deficiency without
concentrating on one old matching edge.

## 5. A recurrent Hall-batch edge is continuous absence or reintroduction

Fix the recurrent stored edge `f` from CMR730. Record its absent/present status
through the return history.

### Theorem CMR731 -- PROVED

Let `rho(f)` be the number of maximal absence runs and `I(f)` the number of
absent-to-present reintroductions. Then

\[
\boxed{\rho(f)\le1+I(f).}
\]

Consequently repeated Hall-batch concentration on `f` yields either

1. one long interval where `f` remains continuously absent; or
2. repeated reintroduction of `f`, with exact entering-edge and full-token
   payment.

### Proof

Apply the absence-run identity CMR519. ∎

The first branch is a persistent Hall-wall certificate; the second is dynamic
edge payment.

## 6. Persistent Hall deficiency is stable under further deletions

### Theorem CMR732 -- PROVED

Suppose an interval uses only further edge deletions and endpoint contractions
inside the same owner and never restores any edge of one Hall batch
`F_{X,Y}`. Then no later uncontracted host on the same vertex cut can recover a
perfect matching across that cut without changing the owner or restoring at
least one missing batch edge or another edge from `X` to the target complement
of the current neighbour set.

### Proof

Further deletions cannot enlarge `N_G(X)`. Endpoint contractions either remove
vertices and reduce the owner or preserve the deficiency on the surviving cut.
A perfect matching on the same uncontracted vertex sets would require Hall's
condition, hence at least one new edge enlarging the deficient neighbour set.
Such an edge is a genuine restoration or owner-changing addition. ∎

The statement is deliberately owner-local; contraction is counted as strict
side descent rather than as persistence of an unchanged cut.

## 7. Essential-return Hall endpoint

### Corollary CMR733 -- PROVED

Every essential return of a previously deleted target edge reaches at least one
of the following.

1. A Hall batch of many distinct old matching-edge deletions.
2. A thin Hall wall entering the established low-width signature machinery.
3. Finite Hall-batch history.
4. One recurrent old matching edge which is continuously absent.
5. Reintroduction of a recurrent old edge, with exact token payment.
6. Strict contraction or owner change.

Therefore the essential-return branch is no longer represented by one anonymous
missing edge. It exposes a deficiency-sized matching batch and reduces repeated
returns to Hall-wall persistence, dynamic reintroduction, or strict descent.
The remaining prime-power frontier is the geometric/payment conversion of a
persistent thin Hall wall inside one fixed envelope into protected-reserve
depletion, full-token return, or baseline improvement.

### Proof

Use CMR727--CMR729 for one episode, CMR730 for repeated large-deficiency
episodes, CMR731 for recurrence, and CMR732 for the persistent owner-local
branch. ∎

No all-`n` theorem is claimed. Hall witnesses, exact stored-matching batches,
and incidence bounds are checked in
[`scripts/verify_prime_power_essential_return_hall_batch.py`](../scripts/verify_prime_power_essential_return_hall_batch.py).
