# Fixed-envelope target chains have finite triple stock or recurrent cell payment

CMR698--CMR705 convert every nonimproving target-destroying transition into the
next target bank. The only remaining temporal concern is that target handoffs
might continue indefinitely inside one unchanged closure envelope. This chapter
shows that such a chain has finite physical target stock unless one exact target
triple is repeatedly recreated through one of its own cells.

Fix one closure-envelope epoch of side `q`. Consider an internal target-driven
sequence in which every target point has column in the envelope and each selected
physical target triple is destroyed by the next handoff bank. When a previously
used target is selected again, call the first transition after its previous
destruction at which it becomes present its **recreation transition**.

## 1. Finite physical target stock

### Theorem CMR706 -- PROVED

The number of physical real-triple signatures wholly supported in the envelope
is at most

\[
\boxed{
M(q)=\binom{2q^2}{3}.
}
\]

For every integer `lambda>=2`, a history of `J` target episodes in the epoch
satisfies at least one of:

1. one exact physical target occurs in at least `lambda` episodes;
2. 
   \[
   \boxed{J\le(\lambda-1)M(q).}
   \]

### Proof

CMR172 fixes one row set of size `q` for each of the two permutation layers over
the envelope. Across the epoch, every selected point with column in the envelope
therefore lies in the union of at most `2q^2` physical cells. Every internal
target is a three-cell subset of that universe, so the displayed binomial
coefficient is an upper bound. The recurrence alternative is the pigeonhole
principle. ∎

Compatibility and collinearity only reduce the stock.

## 2. Reusing a destroyed target requires an entering target cell

### Theorem CMR707 -- PROVED

Let `T` be a target selected once, destroyed by its handoff bank, and selected
again later in the same epoch. At the recreation transition of `T`, at least one
cell of `T` is an entering selected cell.

### Proof

Immediately after the earlier handoff, `T` is not contained in the selected
state. At its recreation transition it is contained in the new state but not in
the preceding state. Therefore it is a genuinely new triple for that transition.
CMR698, equivalently CMR418, says that every genuinely new selected triple
contains an entering cell. Since the triple is `T`, that entering cell belongs
to `T`. ∎

The witness is attached to the first recreation of `T`, not to an arbitrary
later state in which `T` happens to remain present.

## 3. Target recurrence forces one recurrent cell-target pair

### Theorem CMR708 -- PROVED

If one physical target `T` occurs in `lambda` target episodes, then its
`lambda-1` recreations can be assigned to cells of `T`. Consequently some cell
`e` in `T` witnesses at least

\[
\boxed{
\left\lceil\frac{\lambda-1}{3}\right\rceil
}
\]

recreations of that exact target.

### Proof

Apply CMR707 after each of the first `lambda-1` destructions and choose one
entering cell of `T` at the next recreation. There are three possible cells, so
averaging gives the bound. ∎

Thus repeated target signatures refine to repeated owner-labelled cell-target
pairs.

## 4. No recurrent cell implies a polynomial target-chain bound

Fix an integer `mu>=2`. Assume that, for every physical target `T` and every
cell `e` in `T`, the pair `(e,T)` witnesses at most `mu-1` target recreations in
the epoch.

### Theorem CMR709 -- PROVED

Every physical target occurs in at most

\[
\boxed{3\mu-2}
\]

target episodes. Hence the complete fixed-envelope target chain has length at
most

\[
\boxed{
J\le(3\mu-2)\binom{2q^2}{3}.
}
\]

### Proof

A target has one first occurrence. Each later occurrence requires one recreation
witness from one of its three cells by CMR707. Under the hypothesis, each cell
supplies at most `mu-1` witnesses, so there are at most `3(mu-1)` later
occurrences. Add the first occurrence and sum over the physical target stock
CMR706. ∎

This is a genuine finite-history theorem: the bound depends only on the envelope
side and the recurrence threshold.

## 5. Recurrent target cells pay exact reintroduction and token incidence

### Theorem CMR710 -- PROVED

Suppose one owner-labelled pair `(e,T)` witnesses `r` recreations of `T`. Then:

1. the physical cell `e` undergoes at least `r` absent-to-present selected-state
   transitions after destructions of `T`;
2. these transitions contribute at least `r` entering-edge incidences;
3. in a parent of side `p^h`, their exact labelled nonroot full-token incidence is
   
   \[
   \boxed{r(p+1)(h-1).}
   \]

The repeated pair therefore enters the existing absence-run, reintroduction,
packet-recreation, and full-token ledgers. It is not fresh target stock.

### Proof

At every assigned recreation, `e` is absent immediately before the recreation
transition and present immediately afterward, by the definition of an entering
cell. This gives the first two assertions. CMR413 assigns exactly
`(p+1)(h-1)` labelled nonroot token incidences to every entering physical edge,
with multiplicity. ∎

The statement does not claim monotone token consumption; CMR350 shows that
static no-return is false. It supplies the correct dynamic reintroduction
charge.

## 6. Aggregation across the envelope chain

A closure branch has at most `h+1` envelope epochs by CMR174--CMR175. Let the
ambient board have side `N=p^h`.

### Theorem CMR711 -- PROVED

Fix `mu>=2`. Along one closure branch, either

1. one owner-labelled cell-target pair witnesses at least `mu` recreations in one
   envelope epoch; or
2. the total number of internal target episodes over all envelope epochs is at
   most
   
   \[
   \boxed{
   (h+1)(3\mu-2)\binom{N^2}{3}.
   }
   \]

Independently, strict envelope expansion occurs at most `h` times.

### Proof

If the first alternative fails, apply CMR709 separately in every envelope epoch.
Every physical target lies in the ambient `N` by `N` grid, so each epoch has at
most `binom(N^2,3)` target signatures. There are at most `h+1` epochs. The
strict-expansion bound is CMR174. ∎

The coarse ambient-side bound is chosen to preserve absolute owner coordinates;
smaller epoch sides give sharper stocks automatically.

## 7. Fixed-envelope target-chain endpoint

### Corollary CMR712 -- PROVED

Combine CMR705 with the target-chain ledger above. Every target-driven
prime-power closure reaches at least one of:

1. a strict triple-potential improvement;
2. finite deletion, contraction, routing, owner, and target-signature stock;
3. strict child-factor descent;
4. one of the at most `h` envelope expansions;
5. one exact recurrent cell-target pair, paid by selected-edge reintroduction and
   exact full-token incidence.

Consequently no unbounded internal target chain can migrate anonymously among
physical triples. The remaining prime-power theorem is now the dynamic payment
of one recurrent cell-target pair: convert its repeated reintroduction into
protected-reserve depletion, permanent deletion ancestry, full-token return, or
a strict baseline improvement.

### Proof

CMR705 supplies the structural and target-handoff alternatives. Apply CMR711 to
every remaining internal target chain. CMR710 prices the recurrent pair. ∎

No all-`n` theorem is claimed. The target-stock, recreation-witness, recurrence,
and epoch-aggregation arithmetic are checked in
[`scripts/verify_prime_power_fixed_envelope_target_chain.py`](../scripts/verify_prime_power_fixed_envelope_target_chain.py).
