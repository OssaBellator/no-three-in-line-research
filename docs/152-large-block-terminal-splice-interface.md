# Splicing the audited PX63 entry into the rectangle-label repair tree

PX277--PX280 give the causal lexicographic forest.  PX397--PX403 verify the
actual PX63 entry, PX404--PX410 audit the line occupancy supplied by PX64,
PX411--PX444 lift every indexed decoder move to exact rectangle label
permutations, and PX445--PX450 retune the large-block constants and state the
asymptotic repair loop.

The formerly hidden interfaces are now explicit:

- entry comes from the one-hit derangement theorem;
- selected-line growth is paid using the actual `n^(1/3+o(1))` PX64 cap;
- layer/channel pigeonholing is replaced by the two label variables `t,r`;
- clean-star, radial, loaded-line, packet, and mixed-shadow children remain in
  the factor-compatible rectangle state space.

The remaining obligations are a common numerical cutoff, below-cutoff orders,
and a mechanical dependency audit of the label-lift reductions.

## 1. Repair-interface axioms

Fix an ambient order `n`.  A repair state carries

\[
\mathcal V=(U_0,d_0,U_1,d_1,\ldots,U_h,d_h)
\]

as in PX280, together with one phase label at every active leaf:

- `L`: a large or nested rectangle-label block;
- `T`: a weighted high-source rectangle-label child;
- `B`: a below-cutoff finite-order leaf.

Use the following interfaces.

1. **Audited PX63 entry.**  PX397--PX403 apply to every positive-potential
   rectangle state.  They give an `L` leaf or a weighted source set.  The good
   entry bank is factor-compatible, destroys at least `D/18`, and has cylinder
   bound `9/(c)_r`.
2. **Large/nested label interface.**  PX445--PX447 give a host-compatible
   strict-sign-or-child theorem above the square-root ambient threshold.
   Smaller nonterminal blocks follow PX263--PX266 in label space.
3. **Channel-free terminal return.**  PX411--PX419 compress blocker debt over
   `t,r`, use host-compatible label transpositions at high sources, and return
   in bounded depth to an `L` leaf or strict improvement.  PX404--PX410 and
   PX418 use the actual PX64 line cap; no channel or subpower-line hypothesis is
   imposed.
4. **Finite base interface.**  Every `B` leaf lies below one common explicit
   cutoff and must be absorbed, ruled out, or connected to the asymptotic
   range.
5. **Ancestor safety.**  Child moves obey PX278, parent switches remain frozen,
   and suppression credit is assigned only once through PX235--PX239.
6. **Rectangle product invariants.**  PX412, PX427, PX436, and PX444 implement
   terminal, first-generation, packet, mixed-shadow, and recurrence moves as
   permutations of `t,r`.  They preserve the PX43 rectangle normal form,
   saturation, factor compatibility from PX61, and inherited label-position
   constraints.

Axioms 1, 2, 3, 5, and 6 are proved or reduced to the paired label interfaces
indexed through PX449.  Axiom 4 and the dependency/cutoff audit remain open.

## 2. Bounded terminal substitution

### Theorem PX393 -- PROVED REDUCTION, REVISED

Every weighted high-source terminal leaf `T` may be replaced by a finite causal
subtree whose leaves are strict improvements or large/nested label leaves `L`.

The substitution uses no external channel parameter.  A purely one-variable
route has at most three high-source amplifications before its rank-one output
crosses the square-root threshold; a two-variable route needs at most one
additional return.

### Proof

PX417 gives the large-label-block/high-source dichotomy.  PX418 gives the exact
amplification recurrence and the `7/8`, `13/24`, and `2/3` exponents.  A loaded
line enters the cubic-destruction interface.  Every return is assigned to a
deeper causal level and is host-compatible by PX412 and PX444. \(\square\)

## 3. Combined causal potential

Append a finite return counter `r` to each active level and order states by

\[
\boxed{
(U_0,d_0,r_0,U_1,d_1,r_1,\ldots,U_h,d_h,r_h).
}
\]

The counter distinguishes only the bounded local return states after an earlier
unresolved or designated coordinate has decreased.

### Theorem PX394 -- PROVED

Every entry-child conversion, large/nested label move, terminal return, or
designated-certificate neutralization strictly decreases the combined finite
lexicographic vector.

### Proof

PX448 creates the first active leaf and is not itself a repair transition.
Large-block improvement or child conversion decreases the shallowest `U_j`.
Designated neutralization decreases `d_j`.  A terminal return suppresses a
current blocker or replaces it by a deeper child.  The return counter never
precedes that decrease, and deeper coordinates cannot affect the comparison.
\(\square\)

The counter supplies no destruction credit and cannot hide ancestor recurrence.

## 4. Conditional repair termination

### Theorem PX395 -- PROVED UNDER INTERFACE HYPOTHESES, REVISED

For every ambient order satisfying the common asymptotic cutoff and the paired
label-interface hypotheses, every positive factor-compatible rectangle state
has a finite causal repair subtree ending in a strict decrease of the integer
bad-triple potential.

### Proof

PX448 supplies a large label block or high-source child.  Replace every
high-source node by PX393.  The remaining internal nodes are large/nested label
moves and designated neutralizations.  PX394 strictly decreases a finite
lexicographic vector at every operation.  PX449 records the resulting strict
subtree. \(\square\)

### Corollary PX396 -- PROVED REDUCTION, ENTRY AND INVARIANTS AUDITED

The original PX63 entry, selected-line growth, channel count, and product-host
membership of the indexed repair moves are no longer independent open
hypotheses.  Exact all-side product doubling now reduces to:

1. instantiate one common finite cutoff satisfying every paired spread,
   divisor, label-degree, and terminal-transposition inequality;
2. verify or absorb the finitely many orders below that cutoff, or provide an
   independent construction chain into the asymptotic range;
3. mechanically audit PX397--PX449 to ensure every dependency edge uses the
   paired label lift and its stated constants;
4. after that audit, promote the repeated strict-decrease loop PX450 to the
   global theorem index.

PX396 remains an integration reduction.  PX450 is an asymptotic exact-doubling
reduction, not unconditional all-side closure.

## 5. Verification

Run

```bash
python scripts/verify_product_splice_interface.py
python scripts/verify_product_px63_entry_derangement.py
python scripts/verify_product_px64_return_depth.py
python scripts/verify_product_channel_free_label_return.py
python scripts/verify_product_first_generation_label_lift.py
python scripts/verify_product_paired_label_packet.py
python scripts/verify_product_paired_label_mixed_shadow.py
python scripts/verify_product_paired_large_block_margin.py
```

The remaining implementation target is a repository-wide dependency/cutoff
verifier rather than another local geometric decoder.
