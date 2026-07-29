# Finite unit-class clocks after valuation return

**Branch:** `research/orbit-phase-expansion`

OP4as--OP4aw separate finite-prime-support scale motion into an additive valuation vector.  Nonzero valuation drift cannot recur.  This note restores the finite unit data omitted by the valuation quotient and gives the exact return clock when the valuation drift is zero.

## Complete scale decomposition

Fix a finite abelian unit-class group

\[
U=\mathbb Z/n_1\mathbb Z\times\cdots\times\mathbb Z/n_t\mathbb Z.
\]

A complete scale address is `(nu,u)`, where `nu in Z^S` is the prime-valuation vector and `u in U` is the retained unit/sign/coset class.

One repeated decoder block acts by

\[
(\nu,u)\longmapsto(\nu+d,u+g),
\]

for a valuation drift `d` and unit increment `g=(g_1,...,g_t)`.

Changing the prime support, unit group, decomposition convention or physical meaning of the unit class is an outer reset.

## OP4ax -- torsion-free valuation alternative -- PROVED

If `d!=0`, no positive number of block repetitions returns the exact complete scale.

### Proof

After `k` repetitions the valuation is `nu+kd`.  The group `Z^S` is torsion free, so `kd=0` with `k>0` implies `d=0`. QED.

## OP4ay -- exact unit return order -- PROVED

If `d=0`, the exact unit-class return time is

\[
\boxed{
T_U(g)=
\operatorname{lcm}_{1\le i\le t}
\frac{n_i}{\gcd(n_i,g_i)},
}
\]

with the factor interpreted as `1` when `g_i=0`.

### Proof

Coordinate `i` returns exactly when `k g_i=0 mod n_i`, whose least positive solution is `n_i/gcd(n_i,g_i)`.  All coordinates return at the least common multiple. QED.

## OP4az -- complete zero-valuation scale cycle -- PROVED

For `d=0`, the complete scale orbit has exactly `T_U(g)` distinct states before return.  It is a stutter precisely when `g=0`.

### Proof

The orbit is translation by `g` in the finite group `U`; its size is the order of `g`, given by OP4ay. QED.

## OP4ba -- product with holonomy clock -- PROVED

Suppose the same decoder residual also has normalized holonomy return time `T_H` from OP4an--OP4ar.  When valuation drift is zero, the combined quotient scale/phase return time is

\[
\boxed{T_{HU}=\operatorname{lcm}(T_H,T_U(g)).}
\]

No complete quotient recurrence occurs earlier.

### Proof

Both phase and unit class must return.  Their simultaneous return times are exactly the common multiples of their individual orders. QED.

## OP4bb -- complete scale-clock router -- PROVED UNDER THE COMPLETE-UNIT CONTRACT

Every finite-prime-support scale block has one continuation:

1. nonzero valuation drift, giving nonrecurrence or the guarded finite budget of OP4as--OP4aw;
2. zero valuation drift and a nontrivial finite unit clock of order `T_U(g)`;
3. simultaneous holonomy/unit return after `lcm(T_H,T_U(g))`, followed by the bounded physical restoration router;
4. trivial valuation and unit drift, giving an immediate physical-state return;
5. or a change of prime support, unit group, scale decomposition, owner or omitted unit-sensitive legality field, giving an outer reset.

Thus omitted finite unit data cannot hide an unbounded zero-valuation recurrence.

### Proof

Combine OP4ax--OP4ba with the existing valuation, holonomy and physical-state routers. QED.

## Finite check

`scripts/verify_op_unit_class_clock.py` enumerates finite abelian unit groups, verifies the exact element order and audits the least-common-multiple product with the holonomy clock.