# Neutralised target-pair reserves have finite stock or recurrent edge payment

CMR755--CMR762 convert one saturated protected-line reserve into a current
saturated state in which many historical target signatures are globally absent.
This chapter supplies the temporal bookkeeping. A neutralised signature is not
fresh on its next occurrence: one of its recorded absent cells must have returned.
Across repeated reserve-saturation episodes, either a finite owner-labelled
certificate stock is permanently retired or one exact physical cell is
reintroduced many times.

Fix one closure-envelope epoch of side `q`. Let `U_E` be the union of the two
invariant layer boards over the envelope. Then

\[
|U_E|\le 2q^2.
\]

A **neutralisation certificate** records

\[
\sigma=(\text{epoch owner},T,\ell,P,W),
\]

where `T` is one exact historical target triple, `ell` is the chosen majority
layer, `P` is its chosen same-layer pair, and `W` is the nonempty set of physical
witness cells made globally absent by the neutralising state. In the compatible
pair branch `W=P`; in a wall or repeated-cell branch `W` may be one chosen cell.

## 1. Finite owner-labelled certificate stock

### Theorem CMR763 -- PROVED

At one envelope epoch, the number of neutralisation certificates is at most

\[
\boxed{
S(q)=6\binom{2q^2}{3}.
}
\]

### Proof

Every target triple is a three-cell subset of `U_E`, giving at most
`binom(2q^2,3)` physical target signatures. For a fixed triple there are at most
two chosen layer labels and three unordered target pairs. The deterministic
neutralisation rule chooses at most one witness set for each such labelled pair.
Multiplying gives the displayed coarse stock. ∎

The factor six deliberately keeps the layer owner; it avoids identifying two
historical uses of the same physical triple with different layer assignments.

## 2. Neutralisation is permanent until a witness returns

### Theorem CMR764 -- PROVED

Let `sigma=(owner,T,ell,P,W)` be neutralised in a state `S_0`, so every cell of
`W` is absent from `S_0`.

1. As long as every cell of `W` remains absent, the exact target `T` cannot occur.
2. If `T` occurs later, every cell of `W` which belongs to the stored pair `P`
   has undergone an absent-to-present transition after `S_0`.
3. In particular, a one-cell certificate pays at least one reintroduction and a
   compatible two-cell certificate pays at least two distinct reintroductions
   before its target can recur.

### Proof

The witness set is a subset of the stored target pair, hence a subset of `T`.
An occurrence of `T` requires every target cell to be selected. Every witness was
absent at `S_0`, so it must return before or at the first later occurrence. The
two cells of a compatible pair are distinct. ∎

A certificate which never returns is genuinely retired target stock.

## 3. Canonical fresh-certificate discipline

### Theorem CMR765 -- PROVED

There is a canonical accounting in which an owner-labelled certificate is
charged as fresh at most once.

After its first neutralisation, exactly one of the following happens before it
can be charged again.

1. It remains absent forever in the epoch and consumes one unit of the finite
   stock `S(q)`.
2. Its target recurs, and CMR764 records the required witness-cell
   reintroduction before any later neutralisation of the same certificate.
3. The envelope or host owner changes, and the certificate enters a new owner
   namespace already charged by the finite envelope and owner ledgers.

### Proof

Order certificates lexicographically. Mark a certificate retired at its first
neutralisation and do not call it fresh again while it remains inactive. If it
becomes active, CMR764 supplies the return payment. If the owner changes, retain
the physical signature but replace the owner label, which is exactly the owner
transition already counted elsewhere. ∎

Thus repeated line discovery cannot silently recycle the same historical target.

## 4. Distinct-witness episode packing

Consider `K` neutralisation episodes at the same epoch owner. Suppose episode
`j` records a family of certificates with `w_j` pairwise distinct absent witness
cells, and every recorded certificate in that family later recurs.

### Theorem CMR766 -- PROVED

For every integer `lambda>=2`, at least one of the following holds.

1. One exact physical witness cell is reintroduced in at least `lambda`
   certificate returns.
2. The total witness mass satisfies

   \[
   \boxed{
   \sum_{j=1}^{K}w_j
   \le
   (\lambda-1)2q^2.
   }
   \]

If every episode has `w_j>=W>=1`, then

\[
\boxed{
K\le
\left\lfloor
\frac{(\lambda-1)2q^2}{W}
\right\rfloor.
}
\]

### Proof

CMR764 assigns at least one absent-to-present occurrence to every distinct
recorded witness cell in each episode. There are at most `2q^2` physical cells
in the epoch universe. If no cell receives `lambda` incidences, each receives at
most `lambda-1`. Double counting gives the first bound; divide by `W` for the
second. ∎

For a compatible pair bank of size `R`, one may take `w_j=2R`. For a wall branch
with `C-2` distinct witnesses, one may take `w_j=C-2`.

## 5. Permanent retirement or paid episode history

Assume every neutralisation episode is built using the fresh-certificate
discipline CMR765. Fix `W>=1`, and suppose each episode either

- permanently retires at least one fresh certificate; or
- has at least `W` distinct witness cells attached to certificates which later
  recur.

### Theorem CMR767 -- PROVED

For every integer `lambda>=2`, at least one of the following holds.

1. One exact witness cell is reintroduced in at least `lambda` returns.
2. The number of episodes is at most

   \[
   \boxed{
   K
   \le
   S(q)
   +
   \left\lfloor
   \frac{(\lambda-1)2q^2}{W}
   \right\rfloor.
   }
   \]

### Proof

Charge an episode with a permanently retired certificate to the first such
certificate in the fixed order. CMR765 makes those charges injective, so there
are at most `S(q)` of them. Every remaining episode is paid by at least `W`
distinct reintroduced witness cells, and CMR766 bounds their number unless one
cell recurs `lambda` times. ∎

This bound allows an episode to contain both permanent and returning
certificates; one permanent certificate is enough to use the finite-stock charge.

## 6. Repeated-cell stars have the same temporal endpoint

A repeated-cell target star from CMR757 has one cell `z` belonging to many stored
target-pair signatures. CMR758 makes `z` globally absent.

### Theorem CMR768 -- PROVED

Across `K` repeated-cell-star neutralisation episodes at one epoch owner, for
every `lambda>=2`, at least one of the following holds.

1. At least `K-(\lambda-1)2q^2` episodes permanently retire a fresh target
   certificate.
2. One exact physical star cell is reintroduced in at least `lambda` episodes.
3. One has

   \[
   \boxed{K\le S(q)+(\lambda-1)2q^2.}
   \]

### Proof

In each episode, if none of the neutralised star targets ever returns, charge one
fresh certificate permanently. Otherwise the common cell `z` must return by
CMR764. There are at most `S(q)` permanent charges and at most
`(lambda-1)2q^2` nonrecurrent cell-return charges. ∎

A single return of `z` may permit several stored targets to become active, but it
is still one exact owner-cell reintroduction and is not counted as fresh stock.

## 7. Exact token and absence-run payment

### Theorem CMR769 -- PROVED

Suppose one physical witness cell `e` is reintroduced `r` times in an ambient
prime-power parent of side `p^h`. Then

1. the `r` returns contribute `r` entering-edge incidences;
2. their exact labelled nonroot full-token incidence is

   \[
   \boxed{r(p+1)(h-1);}
   \]

3. if `rho(e)` is the number of maximal absence runs and `I(e)` the number of
   absent-to-present returns, then

   \[
   \boxed{\rho(e)\le1+I(e).}
   \]

Consequently repeated reserve saturation in one fixed envelope reaches one of:

- finite permanent target-certificate retirement;
- finite distinct-witness episode stock;
- one recurrent physical witness cell with exact token payment;
- matching-preserving deletion or returned-edge ancestry for that cell;
- strict contraction, owner change, envelope expansion, or potential
  improvement.

### Proof

The incidence statements are CMR413 and CMR519 applied with multiplicity. Combine
CMR763--CMR768 with the recurrent-target deletion and returned-edge alternatives
CMR713--CMR747. ∎

No all-`n` theorem is claimed. The certificate-stock, retirement, witness
incidence, episode-packing, and star-history arithmetic are checked in
[`scripts/verify_prime_power_neutralized_pair_temporal_ledger.py`](../scripts/verify_prime_power_neutralized_pair_temporal_ledger.py).
