# A minimum-robust target creates positive new-triple surplus

CMR982--CMR989 isolate the remaining local target branch.  A physical target `T`
is common to the expanded minimum face, while a feasible four-endpoint bank state
`Q` destroys `T` but lies strictly above the minimum.  The strict integer energy
gap has an exact combinatorial meaning.

For any transition, the potential difference is the number of new triples minus
the number of lost triples.  If `Q` destroys `D` designated targets and has gap
`g>=1` above the minimum, it creates at least `D+g`, hence at least `D+1`, new
triples.  Every new triple contains a physical cell absent from the old state and
therefore an entering labelled edge.

This produces an entering-edge/new-triple signature.  The signature universe is
polynomially finite at fixed side.  A long robust history therefore has an
explicit episode bound or repeats one exact edge--triple signature, which enters
the established support-atom, target-handoff, selected-state churn, and
protected-line ledgers.

Let `S,Q` be saturated labelled two-layer states on the same physical board.  Let
`\mathcal T(S)` be the physical collinear triples of `S`.  Put

\[
\mathcal N(S,Q)=\mathcal T(Q)\setminus\mathcal T(S),
\qquad
\mathcal L(S,Q)=\mathcal T(S)\setminus\mathcal T(Q),
\]

and write

\[
N=|\mathcal N(S,Q)|,
\qquad
L=|\mathcal L(S,Q)|.
\]

## 1. Exact energy-gap identity

### Theorem CMR990 -- PROVED

For every transition,

\[
\boxed{
\Phi(Q)-\Phi(S)=N-L.
}
\]

### Proof

Triples common to both states cancel.  The remaining triples are partitioned into
new and lost triples. ∎

This is the target-handoff identity CMR698 without dropping the strict gap.

## 2. Robust target destruction gives one extra new triple

Assume `S` has minimum value `m`, and let `Q` destroy `D>=1` designated target
triples of `S`.  Suppose

\[
\Phi(Q)=m+g,
\qquad
g\ge1.
\]

### Theorem CMR991 -- PROVED

One has

\[
\boxed{
N=L+g\ge D+g\ge D+1.
}
\]

In particular, a bank state destroying one minimum-robust target creates at least
two new physical triples.

### Proof

Every designated destroyed target is a lost triple, so `L>=D`.  Apply CMR990 and
rearrange. ∎

The extra unit is forced by integrality of the potential gap.

## 3. Every new triple has entering-edge support

Let

\[
E^+(S,Q)=Q\setminus S
\]

be the set of entering labelled selected edges, and put `c=|E^+(S,Q)|`.

### Theorem CMR992 -- PROVED

Every triple `U\in\mathcal N(S,Q)` contains the physical cell of at least one edge
of `E^+(S,Q)`.  Consequently one entering edge supports at least

\[
\boxed{
\left\lceil\frac{N}{c}\right\rceil
\ge
\left\lceil\frac{D+g}{c}\right\rceil
}
\]

new triples.

### Proof

If all three physical cells of `U` already belonged to `S`, then their
collinearity would make `U` a triple of `S`, independent of layer labels.  Thus
`U` contains a physical cell absent from `S`; its unique selected label in `Q`
is an entering edge.  Assign every new triple to its first such edge and average.
∎

Equal-cardinality selected states guarantee `c>0` whenever a new physical cell
appears.

## 4. Cumulative robust surplus

Consider robust episodes `(S_i,Q_i)` with designated loads `D_i>=1`, gaps
`g_i>=1`, new counts `N_i`, and entering counts `c_i`.

### Theorem CMR993 -- PROVED

\[
\boxed{
\sum_iN_i
\ge
\sum_i(D_i+g_i)
\ge
\sum_iD_i+K,
}
\]

where `K` is the number of episodes.  The same lower bound holds for the total
number of assigned entering-edge/new-triple incidences, one incidence per new
triple.

### Proof

Sum CMR991 and assign every new triple as in CMR992. ∎

Thus every robust episode contributes at least one unit beyond target
replacement.

## 5. Finite edge--triple signature stock

A signature is a pair `(e,U)` where `e` is a labelled selected edge and `U` is a
physical triple containing the cell of `e`.

### Theorem CMR994 -- PROVED

On an `n\times n` board the complete signature stock is at most

\[
\boxed{
\mathcal S_n
=
2n^2\binom{n^2-1}{2}.
}
\]

Restricting `U` to actual collinear triples only lowers this number.

### Proof

Choose one of `2n^2` labelled edge copies.  Its physical cell is fixed; choose the
other two physical cells of the triple from the remaining `n^2-1` cells. ∎

## 6. Robust episode bound or recurrent signature

For each robust episode, assign every new triple to one entering edge as in
CMR992.  Fix `\lambda>=2`.

### Theorem CMR995 -- PROVED

At least one of the following holds.

1. One exact signature `(e,U)` occurs in at least `\lambda` assigned incidences.
2. 
   \[
   \boxed{
   \sum_i(D_i+g_i)
   \le
   (\lambda-1)\mathcal S_n.
   }
   \]

In particular, for one-target robust episodes,

\[
\boxed{
K
\le
\left\lfloor
\frac{(\lambda-1)\mathcal S_n}{2}
\right\rfloor
}
\]

unless one exact signature recurs `\lambda` times.

### Proof

CMR993 gives at least `\sum_i(D_i+g_i)` assigned incidences.  If no signature has
multiplicity `\lambda`, each of the at most `\mathcal S_n` signatures contributes
at most `\lambda-1`.  For `D_i,g_i>=1`, each episode contributes at least two.
∎

## 7. Recurrent signatures enter existing geometric ledgers

### Theorem CMR996 -- PROVED

If one signature `(e,U)` recurs, then:

1. the same physical triple `U` is repeatedly created as a new target candidate;
2. the same physical cell and layer label `e` support those creations;
3. conditioning on `e` transfers `U` to one fixed rank-two residual pair;
4. deleting `e` removes every associated occurrence;
5. selected-state or routing reuse of `e` enters the existing churn/support
   ledgers, while host absence generations enter the physical restoration ledger.

### Proof

The first two statements are the signature definition.  The binary edge split and
rank-two transfer are CMR889--CMR893.  The final statement distinguishes selected
matching churn from genuine host restoration and invokes the corresponding
CMR416--CMR421, CMR671--CMR676, or CMR777--CMR925 ledger. ∎

No selected-state entry is silently called a physical restoration.

## 8. Minimum-robust target surplus endpoint

### Corollary CMR997 -- PROVED

A history of minimum-robust four-endpoint target escapes reaches at least one of:

1. strict potential improvement;
2. an explicit finite weighted episode bound CMR995;
3. one recurrent exact new triple;
4. one recurrent labelled support edge and rank-two residual pair;
5. support-atom concentration, target handoff, pair-bank, selected-churn, or
   physical-restoration payment;
6. protected-line/reserve or envelope exit.

Thus the positive energy barrier has been converted into extra geometric
incidence rather than treated as an opaque local minimum.  The remaining frontier
is to aggregate recurrent signatures across envelope owners and prove that their
rank-two descendants or line supports exhaust a global reserve, force strict
minimum decrease, or enter a finite closure-envelope expansion.

### Proof

Combine CMR990--CMR996 with the minimum-face target response CMR982--CMR989 and the
support-batching and historical-pair ledgers CMR755--CMR893. ∎

No all-`n` theorem is claimed.  Energy-gap identities, surplus inequalities,
entering support, signature stocks, recurrence bounds, and rank-two transfer are
checked in
[`scripts/verify_prime_power_minimum_robust_target_surplus.py`](../scripts/verify_prime_power_minimum_robust_target_surplus.py).
