# Splicing the audited PX63 entry into the repair tree

PX277--PX280 give an abstract causal lexicographic forest.  PX334--PX335 close
the large-block internal sign, PX397--PX403 verify the actual PX63 entry
dichotomy, and PX404--PX410 return every asymptotic actual trajectory-terminal
core to the large-block interface using the line occupancy supplied by PX64.
This chapter splices those mechanisms into one conditional repair theorem.

The entry statement is now explicit.  PX63 supplies a factor-compatible
rectangle state with `O(n log n)` bad triples.  PX397--PX403 convert every
nonzero bad-triple set into a large/nested column-permutation block or an actual
order-one/two terminal block, with explicit destruction and fixed-rank spread.
The selected-line hypothesis is likewise explicit: PX64 gives
`K=n^(1/3+o(1))`, and PX404--PX410 prove that this polynomial cap still yields
bounded terminal return.  The remaining hypotheses are kept visible below.

## 1. Repair-interface axioms

Fix an ambient order `n`.  A repair state carries the causal vector

\[
\mathcal V=(U_0,d_0,U_1,d_1,\ldots,U_h,d_h),
\]

as in PX280, together with a phase label at every active leaf:

- `L`: a large or nested matching-block decoder leaf;
- `T`: an actual order-one/two trajectory-terminal leaf;
- `B`: a finite below-threshold base-order leaf.

Use the following interfaces.

1. **Audited PX63 entry.**  PX397--PX403 apply to the PX63 rectangle seed.
   Either the seed is already no-three, or it supplies an `L` leaf or an actual
   `T` leaf.  For a nonterminal entry block of order `c`, the good derangement
   bank remains factor-compatible, has cylinder bound `9/(c)_r`, and destroys
   at least `D/18` old bad triples in every state.
2. **Large/nested-block interface.**  Every quantitatively large `L` leaf
   satisfies PX334--PX335: it either strictly improves at its level or converts
   at least one current blocker to deeper ancestor-safe children.  Smaller
   nonterminal entry blocks follow the nested recurrence PX263--PX266 until
   they become large-decoder or terminal leaves.
3. **Actual terminal-return interface.**  Every asymptotic `T` leaf satisfies
   PX409.  Assuming `q_ch=n^(o(1))`, it either improves directly, produces a
   large endpoint block, reaches a loaded line, or produces a clean star above
   the square-root ambient threshold after bounded return depth.  The
   `K=n^(1/3+o(1))` selected-line bound needed here is supplied by PX64; no
   subpower line-occupancy assumption is imposed.
4. **Finite base interface.**  Every `B` leaf belongs to a fixed finite list of
   ambient orders below the explicit buffer/divisor thresholds and is either
   explicitly absorbed or certified impossible.
5. **Ancestor safety.**  All child moves obey PX278, all parent switches stay
   frozen until their assigned children are discharged, and suppression credit
   is assigned only once through the causal ledger PX235--PX239.
6. **Product-invariant preservation.**  Every non-rectangle endpoint, packet,
   and buffer move used by an `L` or `T` leaf preserves row/column saturation,
   disjoint permutation layers, factor-host membership, and all inherited
   historical-position constraints required by its descendants.

Axioms 1 and the selected-line part of axiom 3 are now proved by PX403 and
PX410.  The remaining open interface checks are the subpower channel bound,
finite base orders, and product-invariant preservation for later moves.

## 2. Bounded terminal substitution

### Theorem PX393 -- PROVED REDUCTION

Under the revised terminal-return interface PX409, every asymptotic terminal
leaf `T` may be replaced by a finite causal subtree whose leaves are either
strict improvements or large/nested-block leaves `L`.

The substitution has bounded return depth independent of `n` once the subpower
channel hypothesis is fixed.  With the actual PX64 line cap, a purely
one-variable route uses at most three high-point amplifications and one
rank-one conversion; a two-variable route needs at most one additional return.

### Proof

PX409 gives the alternatives.  Direct improvement ends the branch.  A large
endpoint block, clean star, or loaded line is an `L` leaf.  PX407 bounds the
one-variable route, and PX408 bounds the first two-variable occurrence.  Every
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

Every operation supplied by the audited entry interface, large/nested-block
interface, terminal-return interface, or designated-certificate neutralization
strictly decreases the combined finite lexicographic vector.

### Proof

The PX403 entry creates the first active leaf and is not a repair transition.
Large-block improvement or child conversion decreases `U_j` at the shallowest
active level, by PX280.  Designated neutralization decreases `d_j`, by PX277.
A terminal return suppresses at least one current blocker or replaces the
terminal obligation by a deeper child; thus its first changed coordinate is a
decrease in `U_j` or `d_j`.  The bounded counter only distinguishes finite local
return states after that earlier causal decrease.  Changes at deeper
coordinates cannot affect lexicographic comparison. \(\square\)

The counter is bookkeeping only.  It does not supply destruction credit and
must not be used to hide recurrence of an ancestor certificate.

## 4. Conditional repair termination

### Theorem PX395 -- PROVED UNDER INTERFACE HYPOTHESES

If the six repair-interface axioms hold for one ambient order `n`, then the
PX63 seed admits a finite causal repair tree terminating in one of:

1. a strict decrease of the target triple potential;
2. an explicitly absorbed finite base state; or
3. a certified impossible entry state.

No infinite sequence of large-block, nested-block, and terminal-return
conversions is possible.

### Proof

PX403 supplies the initial `L`, `T`, or exact leaf.  Replace every asymptotic
terminal node by the finite subtree from PX393.  All remaining internal nodes
are large/nested-block, designated-neutralization, or finite-base nodes.  PX394
strictly decreases a finite lexicographic vector at every operation.  Hence no
branch cycles or continues indefinitely.  Finite base leaves are closed by
axiom 4. \(\square\)

### Corollary PX396 -- PROVED REDUCTION, ENTRY AUDITED

The original PX63 entry dichotomy and selected-line return bound are no longer
open.  To insert the present decoder into exact all-side product doubling it is
sufficient to verify:

1. the subpower layer--channel bound `q_ch=n^(o(1))` along every descendant;
2. the finite list of ambient orders below the explicit buffer/divisor
   thresholds;
3. preservation of factor-host membership, row/column saturation, layer
   disjointness, and historical-position constraints by every later endpoint,
   packet, and buffer move;
4. that every strict potential decrease remains inside the same
   factor-compatible side-`2n` state space until the potential reaches zero.

The asymptotic trajectory-terminal geometry, selected-line growth,
mixed-shadow recurrence, directed-path recurrence, generic rank-one recurrence,
internal rank-three sign, and original PX63 entry no longer require separate
induction cases.

PX396 remains an integration reduction, not the missing all-side product
theorem.

## 5. Verification

Run

```bash
python scripts/verify_product_splice_interface.py
python scripts/verify_product_px63_entry_derangement.py
python scripts/verify_product_px64_return_depth.py
```

The first verifier checks strict lexicographic descent under bounded terminal
substitutions.  The second verifies the exact `4/9` one-hit entry compression,
derangement spread, and `D/18` good-bank destruction.  The third checks the
actual PX64 line-cap exponents and revised bounded return depth.
