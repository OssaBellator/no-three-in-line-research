# Alternating-core import of scalar-cycle termination

**Branch:** `research/alternating-core-chain`

BDA5as--BDA5au close every transition cycle made solely from physical
`h <-> h+q` moves and strict effective-denominator descent.  This note imports
that result into the alternating-core transition graph and identifies the
remaining cycle edges exactly.

## AC3hu -- adjacent radial moves form ticketed forests -- PROVED

Fix one occurrence-faithful ordinary radial profile, or one reflected profile
with separately proved physical radial support.  For every anchor and exact
role decoration, the graph of represented physical scales with edges
`{h,h+q}` is a forest.

Every clean-pair, missing-support completion or adjacent radial transition
uses the same capacity-one unordered support ticket

\[
(P,\{h,h+q\},q,d,u,v,\text{decorations}).
\]

Therefore no alternating-core trajectory can contain a directed cycle using
only adjacent radial transitions at fixed denominator and fixed role profile.

### Proof

This is BDA5as--BDA5at together with the AC3ef ticket identity. QED.

## AC3hv -- strict denominator/scalar epochs terminate -- PROVED

Let `q_0` be the initial denominator of one exact arithmetic epoch and let `R`
be the total number of adjacent-support tickets in its finite anchor/profile
universe.  On every transition which is either:

1. strict effective-denominator descent; or
2. a new adjacent radial edge traversal,

use the BDA5au potential

\[
\boxed{
\Xi_{\rm scal}
=
(R+1)(\Omega_{\rm pf}(q_0)-\Omega_{\rm pf}(q))+c.
}
\]

It strictly increases and has ceiling

\[
(R+1)\Omega_{\rm pf}(q_0)+R.
\]

Hence the epoch terminates and cannot recycle.

### Proof

BDA5au applies verbatim.  AC3hu identifies every physical adjacent move with
one ticket counted by `c`. QED.

## AC3hw -- localization of every remaining arithmetic cycle -- PROVED

Consider the finite AC transition quotient after adding:

- AC2d support descent;
- decorated pivot signatures;
- physical pivot-cell exposure;
- line and axis saturation routers;
- current-anchor and pair-core rematching;
- ordinary occurrence-faithful radial pairs;
- strict effective-denominator descent.

Any surviving directed cycle must contain at least one transition which changes
a finite non-scalar profile field without strict denominator descent.  One of
the following fields changes:

1. primitive direction or projective slope;
2. scalar residue or reduced unit;
3. current/new rank or channel word;
4. anchor, context, closure or blocker role;
5. carry, RI or other external arithmetic label;
6. realized bank type.

It cannot be a pure support-descent cycle, pivot-signature cycle, pivot-cell
cycle, historical line/fixed-pair cycle, adjacent-scale cycle or strict
denominator-descent cycle.

### Proof

AC3d excludes pure support descent.  AC3gq and AC3he exclude cycles containing
only support descent plus new pivot signatures or cells.  AC3hl--AC3hp close
the historical line/fixed-pair topologies.  AC3hu--AC3hv exclude pure adjacent
scale and denominator transitions.  Therefore a surviving cycle must use an
edge outside all these classes, which is exactly a change in one of the listed
finite profile fields. QED.

## Consequence

The AC4 cycle frontier is no longer “all finite BDA/RI transitions.”  It is the
strictly smaller directed graph of same-denominator, non-scalar arithmetic
profile changes.  Every edge in that graph carries an explicit primitive
direction, residue/unit, rank/channel, anchor/context and external role label.

Raw reflected `CD` scalar pairs contribute only their strict denominator
descents here; their nonradial execution is AC3ht.

## Finite check

`scripts/verify_ac_scalar_cycle_import.py` checks the ticketed path model,
prime-factor descent height, the combined potential bounds and an abstract
transition alphabet in which every unclosed cycle necessarily contains one of
the six residual profile-change labels.
