# Splicing bounded terminal return into the large-block repair tree

PX277--PX280 give an abstract causal lexicographic forest.  PX334--PX335 close
the large-block internal sign, and PX391--PX392 return every asymptotic actual
trajectory-terminal core to the large-block interface after bounded causal
depth.  What remains is to splice these two mechanisms into the original
product induction without silently changing its entry hypotheses.

The source statement currently referred to as `PX63` is not reproduced here.
This chapter therefore states a self-contained interface theorem.  Any product
induction satisfying the displayed entry and finite-base hypotheses may invoke
it directly.  No claim is made that those hypotheses have already been checked
for every side length.

## 1. Repair-interface axioms

Fix an ambient order `n`.  A repair state carries the causal vector

\[
\mathcal V=(U_0,d_0,U_1,d_1,\ldots,U_h,d_h),
\]

as in PX280, together with a phase label at every active leaf:

- `L`: a large-block decoder leaf;
- `T`: an actual order-one/two trajectory-terminal leaf;
- `B`: a finite base-order leaf.

Assume the following interfaces.

1. **Entry dichotomy.**  Every unresolved obstruction exposed by the product
   induction is assigned to one of `L,T,B` at a deeper causal level.
2. **Large-block interface.**  Every `L` leaf satisfies PX334--PX335: it either
   strictly improves at its level or converts at least one current blocker to
   deeper ancestor-safe children.
3. **Terminal-return interface.**  Every asymptotic `T` leaf satisfies PX391:
   it either improves directly or, after at most three high-point return
   generations and at most one additional two-variable return, produces an
   `L` leaf at a deeper level.
4. **Finite base interface.**  Every `B` leaf belongs to a fixed finite list
   and is either explicitly absorbed or certified impossible.
5. **Ancestor safety.**  All child moves obey PX278 and all parent switches stay
   frozen until their assigned children are discharged.

## 2. Bounded terminal substitution

### Theorem PX393 -- PROVED REDUCTION

Under the terminal-return interface, every asymptotic terminal leaf `T` may be
replaced by a finite causal subtree whose leaves are either strict
improvements or large-block leaves `L`.

The substitution has bounded return depth independent of `n` once the
subpower channel and line-occupancy hypotheses of PX391 are fixed.

### Proof

PX391 gives exactly four alternatives.  Direct improvement ends the branch.
A large endpoint block, clean star, or loaded line is an `L` leaf.  The purely
one-variable high-point route has at most three generations by PX389, and the
first two-variable route has at most one further generation by PX390.  Every
return is assigned to a deeper causal level by the frozen-switch interface.
\(\square\)

## 3. Combined causal potential

For each active leaf, append a finite terminal-return counter `r` taking values
in a fixed set `{0,1,...,R}`, where `R` is the maximum return depth from PX393.
Order states lexicographically by

\[
\boxed{
(U_0,d_0,r_0,U_1,d_1,r_1,\ldots,U_h,d_h,r_h).
}
\]

The counter is read only at the shallowest active terminal-return coordinate.
A terminal return lowers the current unresolved/blocker coordinate before
introducing a deeper leaf; the counter records the bounded local substitution
and never overrides an earlier decrease.

### Theorem PX394 -- PROVED

Every operation supplied by the large-block interface, terminal-return
interface, or designated-certificate neutralization strictly decreases the
combined finite lexicographic vector.

### Proof

Large-block improvement or child conversion decreases `U_j` at the shallowest
active level, by PX280.  Designated neutralization decreases `d_j`, by PX277.
A terminal return suppresses at least one current blocker or replaces the
terminal obligation by a deeper child; thus its first changed coordinate is a
decrease in `U_j` or `d_j`.  The bounded counter only distinguishes the finite
local return states after that earlier causal decrease.  Changes at deeper
coordinates cannot affect lexicographic comparison. \(\square\)

The counter is bookkeeping only.  It does not supply destruction credit and
must not be used to hide recurrence of an ancestor certificate.

## 4. Conditional repair termination

### Theorem PX395 -- PROVED UNDER INTERFACE HYPOTHESES

If the five repair-interface axioms hold for one ambient order `n`, then every
finite causal repair tree terminates in one of:

1. a strict decrease of the target triple potential;
2. an explicitly absorbed finite base state; or
3. a certified impossible entry state.

No infinite sequence of large-block and terminal-return conversions is
possible.

### Proof

Replace every asymptotic terminal node by the finite subtree from PX393.  All
remaining internal nodes are large-block, designated-neutralization, or finite
base nodes.  PX394 strictly decreases a finite lexicographic vector at every
operation.  Hence no branch cycles or continues indefinitely.  Finite base
leaves are closed by axiom 4. \(\square\)

### Corollary PX396 -- PROVED REDUCTION

To insert the present decoder into the global all-`n` product induction, it is
sufficient to verify only:

1. the exact induction entry dichotomy into large-block, actual terminal, or
   finite-base states;
2. the subpower channel and selected-line occupancy hypotheses used in PX391;
3. the finite list of orders below the explicit buffer/divisor thresholds;
4. preservation of the product construction's row, column, layer, and factor
   invariants by every interface move.

The asymptotic trajectory-terminal geometry, mixed-shadow recurrence, directed
path recurrence, generic rank-one recurrence, and internal rank-three sign no
longer require separate induction cases.

PX396 is an integration reduction, not the missing all-side product theorem.
It deliberately leaves the original induction hypotheses visible rather than
asserting that the inaccessible `PX63` statement already supplies them.

## 5. Verification

Run

```bash
python scripts/verify_product_splice_interface.py
```

The verifier generates finite causal state machines with bounded terminal
substitutions, checks strict lexicographic descent for every permitted
transition, and confirms that terminal-return expansion cannot create a cycle.