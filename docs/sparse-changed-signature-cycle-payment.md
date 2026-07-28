# Cycle-local energy payment for changed recycling signatures

**Branch:** `research/sparse-algebraic-spread`

SAS5gu--SAS5gx reduce repeated sparse recycling to one exact simple cycle in a finite decorated
signature graph.  The remaining issue is local payment of the energy barriers carried by that cycle.
This note lifts one signature cycle to its physical transitions and uses exact energy telescoping:
positive barrier on the cycle is matched by equal negative descent elsewhere on the same cycle.

## Physical cycle-lift model

Fix one simple directed recycling-signature cycle

`sigma_0 -> sigma_1 -> ... -> sigma_ell=sigma_0`,

with `2<=ell<=K_rec`.  Let `kappa_j` be a physical state realizing `sigma_j`, and let the edge
transition from `kappa_(j-1)` to `kappa_j` have exact integer energy increment

`Delta_j=T(kappa_j)-T(kappa_(j-1))`.

Assume the **physical cycle-lift contract**:

1. every decorated signature edge is realized by its declared legal physical transition;
2. the complete energy ledger contains every changed exact record;
3. either `kappa_ell=kappa_0`, or the least differing physical boundary/resource field is returned;
4. aliases and changed records are aggregated before edge-energy evaluation;
5. a changed legality law, omitted field or incomplete ledger is a named failure or outer reset.

Put

`B_+=sum_j (Delta_j)_+`,

`B_-=sum_j (-Delta_j)_+`.

## SAS5gy -- exact cycle energy telescoping -- PROVED

If the physical lift closes, then

`sum_j Delta_j=0`

and therefore

`B_+=B_-`.

### Proof

Sum the state-function differences around the closed physical cycle.  The terms telescope to
`T(kappa_ell)-T(kappa_0)=0`.  Splitting the sum into positive and negative parts gives the second
identity. QED.

## SAS5gz -- positive barriers force cycle-local descent -- PROVED

If `B_+>0`, one edge of the same cycle satisfies

`Delta_j<=-B_+/ell<=-B_+/K_rec`.

Thus every positive aggregate recycling barrier is paid by an actual improving transition on the
same physical cycle.

### Proof

SAS5gy gives total negative magnitude `B_-=B_+`.  At most `ell` negative edges share that magnitude,
so one has magnitude at least `B_+/ell`.  Use `ell<=K_rec`. QED.

No global averaging over unrelated signatures is used.

## SAS5ha -- local-minimum zero-cycle collapse -- PROVED

If every edge of the physical cycle is nonimproving, `Delta_j>=0`, then

`Delta_j=0`

for every edge.

### Proof

Nonnegative increments with zero total sum must all vanish. QED.

Hence a physically closed cycle at edge-local minimum is an exact zero-energy recurrence, not a
positive-barrier obstruction.

## SAS5hb -- cycle ticket or changed-boundary router -- PROVED

Every simple changed-signature cycle has one continuation:

1. a negative-energy edge with descent at least `B_+/K_rec` when `B_+>0`;
2. an all-zero-energy physical recurrence when every edge is nonimproving;
3. a least changed physical boundary/resource field when the signature cycle does not lift to a closed
   physical state;
4. or one legality, complete-ledger, alias, record, signature or outer-reset field fails.

The all-zero branch enters the existing least-chord ticket, quotient, lineage or reset closure.

### Proof

Use SAS5gy--SAS5ha in the physically closed case.  The cycle-lift contract supplies the least changed
field or named failure otherwise. QED.

## SAS5hc -- finite cycle-local payment budget -- PROVED UNDER THE DECLARED CONTRACTS

Suppose recurrent signature cycles consume capacity-one chord tickets as in SAS5gw, with stock

`mu_rec=E-K+c`.

Then before a descent, changed-boundary exit or reset, at most `mu_rec` all-zero recurrent cycle
traversals occur.  Every positive-barrier traversal instead supplies an immediate descent of at least
its barrier divided by `K_rec`.

### Proof

SAS5hb sends every closed nonimproving cycle to the all-zero branch.  SAS5gw bounds distinct
least-chord tickets by `mu_rec`.  Positive-barrier cycles use SAS5gz and do not spend a zero-cycle
ticket. QED.

## Corrected SAS6 frontier

Changed-signature recycling cycles no longer retain unpaid positive energy.  Exact physical closure
forces barrier/descent equality, while edge-local minimality collapses the whole cycle to zero energy
and a finite chord-ticket recurrence.

The remaining sparse work is physical cycle-lift verification for every arithmetic word family,
global payment of creator/opposite-swap barriers that do not lie on closed recycling cycles, batching
neutral outputs under failed incidence caps, base-state single-swap admissibility, positive base-row
realization, heavy-parameter comparison and high-incidence or reflected-boundary profiles.

## Finite check

`scripts/verify_sparse_changed_signature_cycle_payment.py` samples integer-energy signature cycles,
checks exact telescoping, equality of positive barrier and negative descent, the `1/K_rec` improving
edge bound, zero-energy collapse at local minimum and the chord-ticket traversal budget.
