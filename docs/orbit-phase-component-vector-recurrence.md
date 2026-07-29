# Finite vector recurrence for normalized component shifts

**Branch:** `research/orbit-phase-expansion`

OP4ag and OP4am--OP4ao give exact additive orders for one cycle holonomy and one path endpoint displacement.  A rank-at-most-three source-coset profile may have several path/cycle components.  This note closes their simultaneous quotient recurrence.

Fix one complete normalized physical profile with `kappa` components.  After gauge normalization, let

\[
\Omega=(\Omega_1,\ldots,\Omega_\kappa)
\in (\mathbb Z/h\mathbb Z)^\kappa
\]

be the vector of endpoint displacements and cycle holonomies.  All source/target cosets, component types, physical roots, scales, owners, legality and context fields are fixed.  Reusing the same normalized profile adds `Omega` componentwise; a changed retained field is an outer reset.

## OP4ap -- exact component-vector orbit -- PROVED

After `j` repeated traversals, the accumulated normalized invariant vector is

\[
\boxed{j\Omega\pmod h.}
\]

Its exact additive order is

\[
\boxed{
\operatorname{ord}_h(\Omega)
=
\operatorname{lcm}_{1\le i\le\kappa}
\frac{h}{\gcd(h,\Omega_i)}
=
\frac{h}{\gcd(h,\Omega_1,\ldots,\Omega_\kappa)}.
}
\]

The all-zero vector has order one.

### Proof

The vector returns to zero exactly when `j Omega_i=0 mod h` for every component.  The least such positive `j` is the least common multiple of the component orders.  Since every component modulus is the same `h`, prime-valuation comparison gives the final gcd formula. QED.

## OP4aq -- capacity-one vector-phase tickets -- PROVED UNDER THE FIXED-PROFILE CONTRACT

Assign one capacity-one ticket to each noninitial vector phase in the orbit of `Omega`.  A reset-free recurrence of the same complete normalized profile has at most

\[
\boxed{
\operatorname{ord}_h(\Omega)-1
}
\]

nontrivial first visits before returning to the initial vector.

At return, one of the following must occur:

1. physical current payment or absorption;
2. strict lower arithmetic or denominator descent;
3. consumption of a separately justified return ticket;
4. a changed owner, occurrence, scale, carry, legality, boundary or context field;
5. an exact stutter.

### Proof

Before closure the vector phases `j Omega` are distinct by definition of the additive order.  Capacity one bounds their first visits.  Closure repeats the complete normalized quotient address, so only the declared physical continuations remain. QED.

## OP4ar -- simultaneous component router -- PROVED

Every normalized active source-coset profile now has one exact quotient continuation:

1. `Omega=0`: every component is shift-trivial and the profile enters physical payment/absorption or a non-gauge-invariant obstruction;
2. `Omega!=0`: the entire profile has one finite vector orbit of size `h/gcd(h,Omega_1,...,Omega_kappa)`;
3. any changed component or physical field is an exact reset.

This is sharper than multiplying independent component budgets: simultaneous recurrence is governed by one cyclic orbit whose size is at most `h`.

## Corrected OP5 frontier

Normalized internal shift arithmetic is fully finite for individual and simultaneous components.  Remaining work is physical payment of zero-vector profiles, justification of the return branch at one closed finite vector orbit, non-gauge-invariant physical fields, incomplete fibres, and scale imbalance or dispersion.

## Finite check

`scripts/verify_phase_component_vector_recurrence.py` exhausts subgroup orders through twelve and vectors of up to four components, checking the lcm/gcd order identity, distinct pre-return phases and the `order-1` ticket count.
