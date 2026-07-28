# Barrier conservation on exact changed-signature recycling cycles

**Branch:** `research/sparse-algebraic-spread`

SAS5gu--SAS5gx reduce every long composed-output recycling trajectory to immediate reverse payment, a new finite signature, or one simple changed-signature cycle of length at most `K_rec`. The remaining cycle-local issue is energy payment. This note shows that an exact physical lift of such a cycle has zero net energy: every positive creator or opposite-swap barrier is paid one-for-one by actual descending edges on the same cycle.

## Exact physical cycle lift

Let

`sigma_0 -> sigma_1 -> ... -> sigma_l=sigma_0`

be one simple directed recycling-signature cycle, with `2<=l<=K_rec`. Assume the **complete cycle-lift contract**:

1. every signature edge has one legal chronological physical transition `kappa_(j-1)->kappa_j`;
2. the lifted path returns to the exact complete physical state, `kappa_l=kappa_0`;
3. the nonnegative integer energy `T` is evaluated from the complete exact record ledger at every state;
4. every creator, opposite-destroyer, repair, current-payment and boundary field affecting the transition is part of the lifted edge address;
5. failure of exact physical return exposes the least changed resource, record, operation, legality, boundary or context field, which must be added to the recycling signature.

Put

`Delta_j=T(kappa_j)-T(kappa_(j-1))`,

`B_+=sum_j (Delta_j)_+`,

`B_-=sum_j (-Delta_j)_+`.

## SAS5gy -- exact cycle energy telescoping -- PROVED

Every exact physical cycle lift satisfies

`sum_(j=1)^l Delta_j=0`.

### Proof

The sum telescopes to `T(kappa_l)-T(kappa_0)=0` because the complete physical state returns. QED.

## SAS5gz -- positive barriers equal physical descent stock -- PROVED

For every exact physical cycle,

`B_+=B_-`.

Thus aggregate creator, opposite-swap and composed barriers on the cycle are paid without loss by the total energy decrease of descending cycle edges.

### Proof

Write `Delta_j=(Delta_j)_+-(-Delta_j)_+` and sum. SAS5gy makes the total zero. QED.

This is an energy identity, not an assertion that the positive and negative records have the same physical signatures.

## SAS5ha -- one quantitative descending edge -- PROVED

If `B_+>0`, one cycle edge decreases energy by at least

`B_+/l>=B_+/K_rec`.

More generally, if a specified collection of cycle barriers has total weight at least `H`, then one descending edge has gain at least `H/K_rec`.

### Proof

SAS5gz gives total descending gain `B_-=B_+`. Pigeonhole over the at most `l` descending-edge positions, then use `l<=K_rec`. A specified positive subcollection of total `H` implies `B_+>=H`. QED.

## SAS5hb -- local-minimum cycles are energy-neutral -- PROVED

If every lifted edge is nonimproving from its own source state, so `Delta_j>=0` for all `j`, then

`Delta_j=0`

for every edge. Hence the cycle is an exact energy-neutral physical return.

Under the existing capacity-one chord-ticket contract, such a nonterminal recurrent traversal spends one chord ticket; otherwise it is quotient-erased, independently descending in another rank, impossible, or an outer reset.

### Proof

A sum of nonnegative integers can vanish only when every summand is zero. Apply SAS5gy. The recurrence alternatives are the existing SAS5gw cycle contract. QED.

## SAS5hc -- changed-signature cycle barrier router -- PROVED UNDER THE DECLARED CONTRACTS

Every simple changed-signature recycling cycle has one continuation:

1. positive aggregate barrier gives one physical descending edge of gain at least `B_+/K_rec`;
2. at state-local minimum every edge has zero energy increment and the exact cycle uses its chord-ticket, quotient, secondary-rank or reset route;
3. the signature cycle fails to lift to the same complete physical state, returning the least omitted field and strictly refining the finite recycling signature;
4. or one edge-legality, complete-ledger, creator, opposite-destroyer, repair, interaction or boundary contract fails.

Thus positive creator/opposite-swap barriers cannot circulate indefinitely around one exact recycling cycle without producing a quantitatively comparable physical descent.

## Corrected SAS6 frontier

Exact changed-signature cycles now pay their aggregate positive barriers internally: a positive cycle barrier yields descent at scale `1/K_rec`, while a state-local-minimum cycle is entirely energy-neutral and enters the finite chord-ticket router.

The remaining sparse work is controlling signature refinement when the physical lift does not close, proving creator/opposite-destroyer legality for every arithmetic word family, batching neutral outputs under failed incidence caps, positive-base-row realization, boundary/high-incidence profiles and balanced standard-grid compression.

## Finite check

`scripts/verify_sparse_signature_cycle_barrier_payment.py` samples exact closed physical energy cycles and signature-only nonclosed lifts. It checks telescoping, equality of positive barriers and descending stock, the `1/K_rec` edge bound, local-minimum neutrality and omitted-field refinement.
