# Recurrent target cells are matching-preserving deletion responses

CMR706--CMR712 reduce every unbounded internal target chain to one exact
owner-labelled cell-target pair `(e,T)` which is recreated through `e` many
times. At a fixed matching host this pair is not terminal. The fact that `e`
is entering already supplies a perfect matching which avoids it, so `e` is
nonessential and may be deleted while preserving matchability.

This chapter separates two cases which must not be conflated:

- recurrence inside one unchanged host owner, where deletion is immediate;
- recurrence after the host owner changes or the edge is re-added, where the
  existing reintroduction and entering-edge ledgers pay the return.

## 1. Every entering edge is nonessential in a fixed host

Let `H` be a balanced bipartite host and let `M,N` be perfect matchings of `H`.

### Theorem CMR713 -- PROVED

If

\[
e\in N\setminus M,
\]

then `e` is nonessential in `H`. In particular,

\[
\boxed{
\left|\operatorname{PM}(H-e)\right|>0.
}
\]

### Proof

The perfect matching `M` avoids `e` and remains a perfect matching after `e` is
deleted. Hence `e` does not belong to every perfect matching of `H`. ∎

No alternating-cycle construction is required; the preceding matching is the
avoidance certificate.

## 2. Deleting the entering target cell kills the whole target star

Let `T` be a current real triple containing the entering edge `e` of CMR713.
More generally, let `mathcal A_e` be any family of current candidate conflicts
all containing `e`.

### Theorem CMR714 -- PROVED

Deleting `e` from the fixed host

1. preserves at least one perfect matching;
2. makes `T` inactive;
3. makes every member of `mathcal A_e` inactive;
4. cannot activate any previously inactive matching prescription.

### Proof

The first assertion is CMR713. Every listed conflict requires `e`, so none can
occur in a matching of `H-e`. Finally, every perfect matching of `H-e` was
already a perfect matching of `H`; passing to a subhost cannot create a new
extendable prescription. ∎

This is a matching-preserving deletion response, not a claim that the surviving
matching immediately improves the global potential.

## 3. Monotone permanence until genuine reintroduction

### Theorem CMR715 -- PROVED

After the deletion in CMR714, suppose later stages use only further edge
deletions and endpoint contractions and never re-add `e`. Then the physical
target `T` can never recur.

If a later owner state contains `T`, then `e` has been genuinely reintroduced or
the process has moved to a different owner whose host contains `e`. In the
first case the return is an absent-to-present edge event and enters the CMR517--
CMR521 reintroduction ledger.

### Proof

Every later monotone subhost still omits `e`, and `T` contains `e`. Thus `T`
cannot be selected. Any later occurrence of `T` requires a host containing
`e`; relative to the deletion owner this is either explicit edge re-addition or
an owner change. ∎

The owner label is essential: the same physical cell in a genuinely different
factor or envelope stage is not silently identified with the deleted host edge.

## 4. Finite owner-labelled cell-target stock

Let `mathcal O(d,lambda)` be the owner-routing stage stock from CMR693 along one
strict factor-descent path. Let the ambient board have side `N`.

### Theorem CMR716 -- PROVED

At one owner stage, the number of physical cell-target pairs `(e,T)` with
`e` in `T` is at most

\[
\boxed{
3\binom{N^2}{3}.
}
\]

Consequently the complete owner-labelled pair stock on the path is at most

\[
\boxed{
\mathcal P(d,\lambda;N)
=
3\mathcal O(d,\lambda)\binom{N^2}{3}.
}
\]

### Proof

There are at most `binom(N^2,3)` physical triples, and every triple has three
choices of distinguished cell. Multiply by the owner-routing stage stock. ∎

The bound is coarse because it retains absolute parent-grid coordinates and
allows triples using fixed points outside the current factor.

## 5. Pair recurrence or finite target history

### Theorem CMR717 -- PROVED

For every integer `nu>=2`, a history of `J` owner-labelled cell-target episodes
along the descent path reaches at least one of:

1. one exact owner-labelled pair occurs in at least `nu` episodes;
2. 
   \[
   \boxed{
   J
   \le
   (\nu-1)\mathcal P(d,\lambda;N).
   }
   \]

### Proof

Apply the pigeonhole principle to the finite stock CMR716. ∎

Thus recurrence cannot migrate anonymously through factor, envelope, routing,
or host owners.

## 6. Canonical deletion depth at one owner

At a fixed host owner of side `m`, respond to the first repeated productive pair
`(e,T)` by deleting `e` as in CMR714.

### Theorem CMR718 -- PROVED

This response can occur at most

\[
\boxed{|E(H)|\le m^2}
\]

times before the host owner changes or a previously deleted edge is re-added.
One deletion may eliminate several recurrent targets sharing the same cell.

### Proof

Every response removes one physical host edge which is not restored inside the
monotone owner stage. There are at most `m^2` host edges. CMR714 shows that all
targets containing the deleted edge disappear simultaneously. ∎

This deletion count is already compatible with the host-edge stock used in
CMR653, CMR680, and CMR691.

## 7. Recurrent-target deletion endpoint

### Corollary CMR719 -- PROVED

Combine CMR712 with the deletion response above. Every target-driven
prime-power execution reaches at least one of:

1. a strict triple-potential improvement;
2. finite structural, routing, target, and owner-pair stock;
3. strict child-factor descent;
4. a bounded closure-envelope expansion;
5. matching-preserving deletion of the recurrent entering target cell;
6. genuine reintroduction of a previously deleted target cell, with entering-edge
   and exact full-token payment;
7. a different owner stage, charged to the finite owner stock CMR693.

Therefore one recurrent cell-target pair is not an unpriced terminal obstruction.
Inside a fixed owner it is deleted; outside that owner its return pays
reintroduction or owner change. The remaining prime-power frontier is to sum
those paid reintroductions and owner changes against the protected line reserve,
permanent deletion ancestry, full-token return capacity, and the global target-
load potential.

### Proof

CMR712 gives the recurrent pair. Apply CMR713--CMR714 at a fixed host owner.
CMR715 handles later recurrence, CMR716--CMR717 prevent owner migration from
being counted as fresh, and CMR718 bounds monotone deletion responses. ∎

No all-`n` theorem is claimed. Entering-edge nonessentiality, deletion
preservation, and owner-stock arithmetic are checked in
[`scripts/verify_prime_power_recurrent_target_edge_deletion.py`](../scripts/verify_prime_power_recurrent_target_edge_deletion.py).
