# Returned target edges expose deletion ancestry or essential contraction

CMR713--CMR719 delete a recurrent entering target cell at a fixed host owner.
The remaining possibility is that the same physical cell returns after the host
has changed. Store one perfect matching which avoided the cell at the deletion
time. On every later return, either that avoiding matching still survives and
the cell is deletable again, or one of its edges is missing. If the returned
cell has become essential, this missing edge is a mandatory deletion-ancestry
witness and the essential cell can be contracted exactly.

Fix an earlier balanced host `H_0`, a physical edge `e`, and a perfect matching

\[
M_0\in\operatorname{PM}(H_0-e).
\]

Let `H_1` be any later matchable host on the same labelled vertex sets which
contains `e`.

## 1. Surviving avoidance matching gives immediate redeletion

### Theorem CMR720 -- PROVED

If

\[
M_0\subseteq H_1,
\]

then `e` is nonessential in `H_1` and

\[
\boxed{
\left|\operatorname{PM}(H_1-e)\right|>0.
}
\]

Thus the returned target edge may be deleted again while preserving
matchability.

### Proof

The stored matching `M_0` is a perfect matching of `H_1` and avoids `e`. It
therefore survives in `H_1-e`. ∎

This response is independent of any newly added edges elsewhere in the host.

## 2. Failure of redeletion exposes an old matching edge which disappeared

### Theorem CMR721 -- PROVED

If the stored avoidance matching does not survive in `H_1`, then

\[
\boxed{\left|M_0\setminus E(H_1)\right|>0.}
\]

Choose one canonical edge

\[
f\in M_0\setminus E(H_1).
\]

The edge `f` is a deletion-ancestry witness for the return of `e`: relative to
the earlier deletion owner, the old explicit escape from `e` has been blocked by
the absence of `f`.

### Proof

A matching survives exactly when all its edges remain present. If `M_0` is not a
perfect matching of `H_1`, at least one of its edges is absent. ∎

The theorem does not claim that one missing edge is the only reason every
avoidance matching fails; it gives one exact witness from the stored escape.

## 3. Essential return always has a deletion-ancestry witness

### Theorem CMR722 -- PROVED

If `e` is essential in the later host `H_1`, then the redeletion branch CMR720 is
impossible. Consequently at least one edge of `M_0` is absent from `H_1`.

### Proof

If `M_0` survived, it would be a perfect matching of `H_1` avoiding `e`, contrary
to essentiality. Apply CMR721. ∎

Thus a previously nonessential target edge cannot become essential without
breaking the stored avoiding matching.

## 4. Finite blocking-witness stock or recurrence

The stored matching `M_0` has side `m` and therefore exactly `m` edges. Assign
every later essential-return episode of `e` the first absent edge of `M_0` in a
fixed ordering.

### Theorem CMR723 -- PROVED

For every integer `mu>=2`, a history of `K` essential-return episodes satisfies
at least one of:

1. one exact old matching edge `f` in `M_0` is absent in at least `mu` episodes;
2. 
   \[
   \boxed{K\le(\mu-1)m.}
   \]

### Proof

There are exactly `m` possible canonical witnesses. If none occurs `mu` times,
each occurs at most `mu-1` times. ∎

The witness stock is linear in the factor side, not quadratic in the host edge
universe.

## 5. Repeated blocking is absence-run or reintroduction payment

Fix one recurrent witness edge `f` from CMR723. Across the selected episodes,
record whether `f` is absent or present in the evolving host.

### Theorem CMR724 -- PROVED

Let `rho(f)` be the number of maximal absence runs of `f`, and let `I(f)` be the
number of absent-to-present reintroductions of `f`. Then

\[
\boxed{\rho(f)\le1+I(f).}
\]

Hence repeated blocking by `f` either

1. is covered by a bounded number of continuous-absence intervals; or
2. pays repeated reintroduction of `f`, with the exact token and entering-edge
   charges already established in CMR517--CMR521 and CMR413--CMR421.

### Proof

This is the binary absence-run identity CMR519 applied to the fixed physical
edge `f`. Every new absence run after the first requires a preceding
absent-to-present transition. ∎

No static no-return claim is used.

## 6. Essential target-edge contraction transfers rank at most two

Suppose `e` is essential in `H_1`. Let `T` be a current target triple containing
`e`.

### Theorem CMR725 -- PROVED

Contracting the endpoints of `e` gives the exact factorisation

\[
\boxed{
\operatorname{PM}(H_1)
\cong
\{e\}\times\operatorname{PM}(H_1-V(e)).
}
\]

After contraction, occurrence of `T` is controlled by the residual prescription

\[
T\setminus\{e\},
\]

which has rank at most two. It therefore enters the anchored-deletion,
essential-transfer, or fixed-certificate alternatives CMR636--CMR653.

### Proof

Essential contraction is CMR636. The target has three cells and one is the
contracted edge, leaving at most two unfixed cells. ∎

Thus essential return reduces side length or transfers the target into the
already normalised low-rank recursion.

## 7. Target-edge return endpoint

### Corollary CMR726 -- PROVED

Every return of a target edge previously deleted by CMR714 reaches at least one
of the following.

1. The stored avoiding matching survives and the edge is deleted again.
2. One explicit edge of the stored avoiding matching is absent.
3. Repeated absence of one witness edge lies in one continuous absence run.
4. Repeated absence runs of one witness edge pay reintroduction and exact full-token
   incidence.
5. The returned target edge is essential, contracts exactly, and transfers the
   target to rank at most two.
6. The host, factor, routing, or envelope owner changes, consuming the finite
   owner stock already recorded in CMR693 and CMR716.

Consequently the recurrent target-edge branch is reduced to monotone deletion,
linear deletion ancestry, dynamic reintroduction, or strict contraction. The
remaining prime-power frontier is to aggregate the continuous-absence and
reintroduction branches with protected reserve and full-token return capacity,
not to classify another matching-space obstruction.

### Proof

Apply CMR720 if the stored matching survives. Otherwise use CMR721. Essential
returns satisfy CMR722 and contract by CMR725. Repeated missing-edge witnesses
are controlled by CMR723--CMR724, and owner changes use the existing owner
ledger. ∎

No all-`n` theorem is claimed. Stored-avoidance survival, essential-return
witnesses, and recurrence arithmetic are checked in
[`scripts/verify_prime_power_target_edge_return_ancestry.py`](../scripts/verify_prime_power_target_edge_return_ancestry.py).
