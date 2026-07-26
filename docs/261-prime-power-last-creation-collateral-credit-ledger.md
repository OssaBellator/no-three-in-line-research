# Live triples have unique last-creation credits owned by physical cells

CMR1214--CMR1221 assign every newly created triple to one labelled entering edge.
For a history, the corresponding physical cell gives a persistent credit owner.
This chapter records the exact dynamic ledger.  It separates genuine triple
reproduction from layer relabelling and makes later target destruction retire
previous collateral credits rather than count them again.

Consider a finite sequence of saturated physical states

\[
S_0,S_1,\ldots,S_T.
\]

At each transition, assign every new triple in
`mathcal T(S_i) setminus mathcal T(S_{i-1})` to the CMR1215 least entering labelled
edge and then forget only its layer label, retaining the absolute physical owner
cell.

## 1. Every live triple has a last creation time

### Theorem CMR1254 -- PROVED

For every `i>=0` and every triple `U in mathcal T(S_i)`, exactly one of the
following holds.

1. `U` was present in `S_0` and has remained present through every state up to `i`.
2. There is a unique largest index `j<=i` such that
   \[
   U\notin\mathcal T(S_{j-1}),
   \qquad
   U\in\mathcal T(S_j),
   \]
   and `U` remains present from `S_j` through `S_i`.

### Proof

Inspect the finite binary presence history of `U`.  If it is constantly one, use
branch one.  Otherwise its final zero-to-one transition before time `i` is unique
and is the largest such index. ∎

Call `j` the last creation time of `U`; root-persistent triples have creation time
zero.

## 2. Every nonroot credit has one physical owner

### Theorem CMR1255 -- PROVED

At its last creation transition, every nonroot live triple `U` receives one unique
labelled entering-edge owner by CMR1215 and therefore one unique absolute physical
owner cell

\[
\boxed{c(U).}
\]

The owner cell belongs to `U`.

### Proof

CMR1214 gives a nonempty entering-edge set inside `U`, and the fixed total order
chooses one edge.  Taking its physical cell is a function and preserves membership
in `U`. ∎

The creation layer may later change; the physical owner cell does not.

## 3. Exact live-credit partition of the potential

At time `i`, let `mathcal C_i^0` be the root-persistent triples and, for `j>=1`, let
`mathcal C_i^j` be the triples whose last creation time is `j` and which remain
live at time `i`.

### Theorem CMR1256 -- PROVED

\[
\boxed{
\mathcal T(S_i)
=
\bigsqcup_{j=0}^{i}\mathcal C_i^j,
}
\]

and hence

\[
\boxed{
\Phi(S_i)
=
\sum_{j=0}^{i}|\mathcal C_i^j|.
}
\]

Refining by physical owner cells gives

\[
\boxed{
\Phi(S_i)
=
|\mathcal C_i^0|
+
\sum_c C_i(c),
}
\]

where `C_i(c)` is the number of live nonroot credits owned by `c`.

### Proof

CMR1254 assigns every live triple one last creation time.  Distinct times are
disjoint.  CMR1255 further partitions every nonroot class by its owner cell. ∎

No live triple is charged at every structural ancestor or every later state.

## 4. Exact transition update

Let

\[
L_i
=
|\mathcal T(S_{i-1})\setminus\mathcal T(S_i)|,
\qquad
N_i
=
|\mathcal T(S_i)\setminus\mathcal T(S_{i-1})|.
\]

### Theorem CMR1257 -- PROVED

At transition `i`:

1. exactly `L_i` live credits are retired;
2. exactly `N_i` new credits are created and assigned to entering physical cells;
3. every surviving credit keeps its previous creation time and owner; and
4.
   \[
   \boxed{
   \Phi(S_i)-\Phi(S_{i-1})=N_i-L_i.
   }
   \]

### Proof

A triple present before and absent after retires its unique live credit.  A triple
absent before and present after receives a new last-creation record.  A triple
present in both states has no zero-to-one transition and keeps its record.  Count
the three disjoint transition classes. ∎

This is the target-versus-collateral identity as a literal credit update.

## 5. Owner credits are current target load

For a physical selected cell `c` in `S_i`, let

\[
D_{S_i}(c)
=
|\{U\in\mathcal T(S_i):c\in U\}|.
\]

### Theorem CMR1258 -- PROVED

\[
\boxed{
C_i(c)\le D_{S_i}(c).
}
\]

More precisely, every credit counted by `C_i(c)` is a distinct current target
containing `c`.

### Proof

The owner cell belongs to its triple at creation.  While the credit remains live,
the same physical triple and all three cells remain selected.  Distinct credits are
distinct triples. ∎

Thus collateral created at one step is immediately available as target load for a
later response through its owner cell.

## 6. Removing an owner cell retires all of its credits

### Theorem CMR1259 -- PROVED

Suppose a later response removes the physical cell `c`, meaning neither layer
selects it.  Then every live credit owned by `c` is retired at that transition.
Consequently the destroyed load is at least

\[
\boxed{C_i(c).}
\]

### Proof

Every owned live triple contains `c` by CMR1258.  If `c` is absent after the
transition, none of those triples survives. ∎

The fixed-target banks CMR1158 and CMR1175 remove the chosen physical target cell
in exactly this sense.

## 7. Layer reassignment is not credit reproduction

### Theorem CMR1260 -- PROVED

If a physical triple remains selected across a transition but one or more of its
cells change permutation-layer labels, the triple creates no new credit and keeps
its previous physical owner.

A new credit is issued only after an actual physical absence followed by
reappearance.

### Proof

The credit ledger is defined from physical triple membership.  Continuous physical
presence has no zero-to-one transition.  Reappearance after absence has one and is
processed by CMR1254--CMR1255. ∎

This is the triple analogue of owner-independent physical restoration.

## 8. Collateral-credit endpoint

### Corollary CMR1261 -- PROVED

Every target-driven history has an exact live-credit interpretation.

1. Root triples supply initial credits.
2. Every created triple receives one last-entering physical owner.
3. Current potential is the number of live credits.
4. Destroyed triples retire their previous credits.
5. New triples issue new credits.
6. Removing an owner cell retires every live credit assigned to it.
7. Layer relabelling and structural refactorisation do not reproduce credits.

The remaining target-versus-collateral theorem may therefore be sought as a
subcritical reproduction inequality for these credits.  The local-envelope
concentration CMR1249--CMR1251 identifies physical cells carrying large offspring
loads, and CMR1259 makes them legitimate next-generation targets.

No all-`n` theorem is claimed.  Last-creation uniqueness, credit partitions,
transition updates, owner-load bounds and layer-reassignment invariance are checked
in
[`scripts/verify_prime_power_collateral_credit_ledger.py`](../scripts/verify_prime_power_collateral_credit_ledger.py).
