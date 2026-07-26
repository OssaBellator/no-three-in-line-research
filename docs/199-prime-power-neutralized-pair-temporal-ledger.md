# Neutralised target-pair reserves have finite stock or recurrent edge payment

CMR755--CMR762 convert one saturated protected-line reserve into a current
saturated state in which many historical target signatures are globally absent.
The temporal accounting must use physical **absence runs**. Several
neutralisations made while one cell stays continuously absent may share the same
later return, so raw episode-to-return charging would overcount.

Fix one closure-envelope epoch of side `q`. Let `U_E` be the union of the two
invariant layer boards over the envelope. Then

\[
|U_E|\le 2q^2.
\]

A **neutralisation certificate key** is

\[
\sigma=(\text{epoch owner},T,\ell,P),
\]

where `T` is one exact historical target triple, `ell` is the chosen majority
layer, and `P` is its chosen same-layer pair. In a particular neutralisation
episode the key is accompanied by a nonempty witness set

\[
W\subseteq P
\]

whose cells are globally absent in the neutralising state. The witness set is
episode data, not part of the finite certificate key.

## 1. Finite owner-labelled certificate stock

### Theorem CMR763 -- PROVED

At one envelope epoch, the number of neutralisation certificate keys is at most

\[
\boxed{S(q)=6\binom{2q^2}{3}.}
\]

### Proof

Every target triple is a three-cell subset of `U_E`, giving at most
`binom(2q^2,3)` physical signatures. A fixed triple has at most two layer labels
and three unordered pairs. ∎

## 2. Neutralisation is permanent until a witness returns

### Theorem CMR764 -- PROVED

Let a certificate key be neutralised in state `S_0` with witness set `W`.

1. As long as one cell of `W` remains absent, the exact target cannot occur.
2. If the target occurs later, every cell of `W` has undergone an
   absent-to-present transition after `S_0`.
3. A one-cell certificate therefore requires one return, while a compatible
   two-cell certificate requires both distinct cells to return before recurrence.

### Proof

The witness set is contained in the stored target pair and hence in the target.
Every witness is absent in `S_0`, while a later target occurrence contains every
one of its cells. ∎

## 3. Canonical fresh-certificate discipline

### Theorem CMR765 -- PROVED

There is a canonical accounting in which an owner-labelled certificate key is
charged as fresh at most once while it remains inactive.

After its first neutralisation, exactly one of the following happens before it
can be selected as fresh again.

1. It remains inactive for the rest of the epoch and consumes one unit of
   `S(q)`.
2. Its target recurs, and CMR764 records the required witness returns.
3. The owner changes and the key enters a new owner namespace already charged by
   the finite owner ledgers.

### Proof

Order the keys lexicographically. Mark a key retired at its first
neutralisation, and do not select it again while any recorded witness remains
absent. Reactivation requires the returns in CMR764. ∎

This discipline prevents repeated selection of the same historical target during
one continuous witness absence.

## 4. Cell--absence-run slots

For a physical cell `e`, let `rho(e)` be its number of maximal absence runs in
the epoch and let `I(e)` be its number of absent-to-present returns.

### Theorem CMR766 -- PROVED

One has

\[
\boxed{\rho(e)\le1+I(e).}
\]

Consequently the total number of cell--absence-run slots in the epoch satisfies

\[
\boxed{
\sum_{e\in U_E}\rho(e)
\le
2q^2+\sum_{e\in U_E}I(e).
}
\]

If no cell is reintroduced `lambda` times, then

\[
\boxed{
\sum_{e\in U_E}\rho(e)
\le
2\lambda q^2.
}
\]

### Proof

The first inequality is CMR519. Sum over at most `2q^2` cells. If every
`I(e)<=lambda-1`, then the total return count is at most
`(lambda-1)2q^2`. ∎

The slot, not the episode, is the correct unit for persistent neutralisation.

## 5. A run slot carries only finite fresh certificate stock

### Theorem CMR767 -- PROVED

Fix one cell `e` and one maximal absence run `R` of that cell. Under the fresh
certificate discipline, at most

\[
\boxed{S(q)}
\]

neutralisation incidences can use `e` as a witness during `R`.

More generally, if `K` neutralisation episodes each record at least `W>=1`
pairwise distinct witness cells, then

\[
\boxed{
KW
\le
S(q)
\sum_{e\in U_E}\rho(e).
}
\]

Hence, unless one cell is reintroduced at least `lambda` times,

\[
\boxed{
K
\le
\left\lfloor
\frac{2\lambda q^2 S(q)}{W}
\right\rfloor.
}
\]

### Proof

A fixed certificate key cannot be selected twice as fresh while `e` remains
continuously absent: after its first selection it is inactive, and reactivation
would require `e` to return, ending the run. Thus the incidences attached to one
cell--run slot have distinct keys and are bounded by `S(q)`.

Double-count the episode witness incidences over cell--run slots. Apply CMR766 for
the final bound. ∎

For a compatible pair bank of size `R`, one may take `W=2R`. For a distinct-cell
wall branch one may take `W=C-2` when this is positive.

## 6. Repeated-cell stars use the same run ledger

A repeated-cell target star from CMR757 has one cell `z` belonging to many stored
signatures. CMR758 makes `z` globally absent.

### Theorem CMR768 -- PROVED

Across `K` repeated-cell-star neutralisation episodes at one epoch owner,

\[
\boxed{
K
\le
S(q)
\sum_{e\in U_E}\rho(e).
}
\]

In particular, for every `lambda>=2`, either one star cell is reintroduced in at
least `lambda` absence runs or

\[
\boxed{K\le2\lambda q^2S(q).}
\]

### Proof

Charge each episode to its globally absent star cell and the absence run
containing that episode. The fresh discipline makes the attached certificate
keys distinct within one slot, so CMR767 applies with one witness per episode.
Use CMR766 for the threshold form. ∎

One return of `z` may reactivate several target signatures. It is counted once,
through the end of one absence run, exactly as required.

## 7. Exact token payment and corrected endpoint

### Theorem CMR769 -- PROVED

Suppose one physical witness cell `e` is reintroduced `r` times in an ambient
prime-power parent of side `p^h`. Then

1. the returns contribute `r` entering-edge incidences;
2. their exact labelled nonroot full-token incidence is

   \[
   \boxed{r(p+1)(h-1);}
   \]

3. they create at most `r+1` absence runs of `e`.

Consequently repeated protected-reserve saturation in one fixed envelope reaches
one of:

- finitely many cell--absence-run slots, each carrying at most `S(q)` fresh
  certificate keys;
- one physical cell with many distinct reintroduction runs and exact token
  payment;
- matching-preserving deletion or returned-edge ancestry for that cell;
- strict contraction, owner change, envelope expansion, or potential
  improvement.

### Proof

The token incidence is CMR413 and the run count is CMR519. Combine
CMR763--CMR768 with CMR713--CMR747. ∎

No all-`n` theorem is claimed. The certificate stock, absence-run slots, fresh-key
capacity, episode bounds, and token arithmetic are checked in
[`scripts/verify_prime_power_neutralized_pair_temporal_ledger.py`](../scripts/verify_prime_power_neutralized_pair_temporal_ledger.py).
