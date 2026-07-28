# Scale-valuation drift for orbit-phase residuals

**Branch:** `research/orbit-phase-expansion`

OP4an--OP4ar separate quotient holonomy from bounded physical recurrence. The remaining named outputs include incomplete fibres, one-root scale imbalance and scale dispersion. This note gives the exact finite-prime-support reduction: physical scales lift to integer valuation vectors, and a repeated residual block either changes that vector monotonically, exhausts a finite valuation guard, or returns it exactly.

The theorem requires a fixed finite prime support. Introduction of a new prime, a changed scale convention or an omitted unit field is an explicit outer reset.

## Finite-support scale address

Fix distinct primes

\[
 \mathcal P=\{p_1,\ldots,p_r\}.
\]

For a positive rational physical scale `s` whose numerator and denominator use only primes in `P`, define

\[
 \nu(s)=(\nu_{p_1}(s),\ldots,\nu_{p_r}(s))\in\mathbb Z^r.
\]

Retain separately the finite unit, quotient-coset, owner, completion, blocker and operation fields required by the physical branch.

A scale-dispersion record between two roots uses the relative vector

\[
 \nu(s_1/s_2)=\nu(s_1)-\nu(s_2).
\]

## OP4as -- valuation address is additive and exact -- PROVED

For finite-support scales `s,t`,

\[
 \boxed{
 \nu(st)=\nu(s)+\nu(t),
 \qquad
 \nu(s/t)=\nu(s)-\nu(t).
 }
\]

Moreover, after fixing the finite prime support and the retained unit convention, equality of complete scale addresses is equivalent to equality of the physical rational scales.

### Proof

Prime valuations are additive under multiplication and subtract under division. Unique factorization reconstructs the rational scale from its valuation vector together with the declared unit convention. QED.

## Repeated residual block

Fix one exact residual block which returns every finite non-scale field and changes the scale-valuation vector by

\[
 d\in\mathbb Z^r.
\]

After `k` traversals the vector is

\[
 v+k d.
\]

The same statement applies to a relative scale-dispersion vector.

## OP4at -- nonzero valuation drift forbids exact recurrence -- PROVED

If `d!=0`, then no positive number of repeated block traversals returns the complete scale address.

### Proof

If `v+kd=v` for some positive integer `k`, then `kd=0` in the torsion-free group `Z^r`, forcing `d=0`, contradiction. QED.

Thus a one-root scale imbalance or relative scale dispersion with nonzero net valuation drift is a strict arithmetic escape rather than a recurrent finite obstruction.

## OP4au -- exact guarded valuation budget -- PROVED

Suppose coordinate `i` has a retained lower guard `L_i` and upper guard `U_i`, allowing either bound to be infinite. If the block is legal from `v`, then every finite bound in the direction of `d_i` gives a first-failure count:

\[
 B_i=
 \begin{cases}
 \left\lfloor\dfrac{v_i-L_i}{-d_i}\right\rfloor+1,&d_i<0\text{ and }L_i> -\infty,\\[1.2ex]
 \left\lfloor\dfrac{U_i-v_i}{d_i}\right\rfloor+1,&d_i>0\text{ and }U_i<+\infty.
 \end{cases}
\]

The number of further legal traversals is at most the minimum finite `B_i`.

### Proof

Before traversal `k`, coordinate `i` equals `v_i+k d_i`. Solve the corresponding lower or upper inequality for the first integer `k` at which it fails. QED.

## OP4av -- zero drift returns the exact scale layer -- PROVED

If `d=0`, one block returns every retained scale valuation exactly. The residual recurrence therefore lies entirely in the finite unit/coset holonomy and bounded physical state already handled by OP4ad--OP4ar and OP4ai--OP4am.

### Proof

The valuation vector is unchanged. All non-scale fields return by the block hypothesis, so only the separately retained finite unit and physical fields remain. QED.

## OP4aw -- scale-imbalance router -- PROVED UNDER THE COMPLETE-SCALE CONTRACT

Every fixed-prime-support incomplete-fibre, one-root scale-imbalance or scale-dispersion block has one continuation:

1. nonzero unguarded valuation drift gives strict arithmetic escape;
2. nonzero guarded drift exhausts the exact budget from OP4au;
3. zero drift returns the exact scale layer and enters the finite holonomy/physical restoration router;
4. a prime, unit, field, owner, completion, blocker, lineage, operation or legality field changes, giving an explicit reset;
5. or the selected valuation transition carries current payment, strict denominator descent, physical impossibility or a capacity-one ticket.

Consequently finite-prime-support scale imbalance is not an independent recurrent obstruction. Remaining OP5 scale work requires dynamically growing prime support, omitted unit data, nonmultiplicative scale updates or payment of the exact zero-drift residual class.

## Finite check

`scripts/verify_op_scale_valuation_drift.py` samples finite valuation vectors and guarded drift blocks, verifies torsion-free nonrecurrence, exact zero-drift return and the displayed first-failure formula.