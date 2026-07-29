# Symmetric and antisymmetric ledgers on a two-lift terminal fibre

**Branch:** `research/rational-inverse-expansion`

RI5bh--RI5bq show that each fixed terminal active geometry has at most two physical lifts, and RI5br--RI5bv add the complete owner/coherence quotient. This note isolates the only arithmetic effect of the physical transposition.

## Two-lift ledger

Let the two ordered physical lifts be `u` and `v`. Attach exact additive ledger values

\[
w_u,w_v\in A
\]

in an abelian group `A`. Define the symmetric total and antisymmetric difference

\[
S=w_u+w_v,\qquad D=w_u-w_v.
\]

The physical transposition exchanges `u` and `v`.

## RI5bw -- symmetric invariance -- PROVED

Under the transposition,

\[
S\mapsto S.
\]

### Proof

Commutativity gives `w_v+w_u=w_u+w_v`. QED.

## RI5bx -- antisymmetric sign reversal -- PROVED

Under the transposition,

\[
D\mapsto-D.
\]

### Proof

The new difference is `w_v-w_u=-(w_u-w_v)`. QED.

## RI5by -- exact two-step cancellation -- PROVED

Over one complete nontrivial transposition orbit, every antisymmetric additive charge cancels:

\[
D+(-D)=0.
\]

Hence a two-step physical alternation can contribute only its symmetric ledger component.

## RI5bz -- immutable-fibre payment reduction -- PROVED

Suppose owner, lineage, coherence, scale and legality fields are immutable on a fixed two-lift fibre. Then:

1. the symmetric ledger is constant;
2. the antisymmetric ledger has zero net contribution over every complete transposition cycle;
3. any nonzero accumulated cycle charge must come from a declared symmetric payment term.

Thus the physical orientation ambiguity cannot create an unbounded hidden arithmetic debt.

## RI5ca -- owner-sensitive router -- PROVED UNDER THE COMPLETE LEDGER CONTRACT

For a recurrent terminal fibre, one of the following occurs:

- a symmetric owner/source term carries current payment;
- the antisymmetric contribution cancels over the transposition orbit;
- owner, lineage, coherence, scale or legality changes, exposing the restoration gate of RI5br--RI5bv;
- or a ledger field omitted from the complete address changes, giving an explicit reset.

The remaining RI6 obligation is therefore to pay or absorb one exact symmetric owner/source address, not an arbitrary alternating lift history.

## Finite check

`scripts/verify_ri_two_lift_antisymmetric_ledger.py` checks symmetric invariance, antisymmetric sign reversal and exact two-step cancellation on 120,000 integer-valued two-lift ledgers.