# All-n route C: product and composition constructions

**Branch:** `research/all-n-product-construction`

This branch is independent of prime patching and composite-ring conics. It seeks a composition rule that turns saturated no-three-in-line configurations at smaller side lengths into one at a product or other composite side length.

A naive Cartesian or block product fails because points from different blocks can form new long lines. The central work is an exact cross-block collinearity theorem.

## Progress ledger

The detailed proofs and counterexamples are in
[`docs/27-all-n-product-construction.md`](../docs/27-all-n-product-construction.md),
with finite checks in
[`scripts/verify_product_construction.py`](../scripts/verify_product_construction.py).

| Item | Status | Current result |
|---|---|---|
| PC1 | **COMPLETE** | Cycle-wise phase encoding gives exactly two disjoint permutation layers on `[mn]^2` in `O(mn)` time. |
| PC2 | **PARTIAL** | Exact determinant `n^2 Delta_c + nM + Delta_f` and four cross-block multiplicity types are proved; resonance elimination is open. |
| PC3 | **OPEN / SIMPLE PHASE ROUTE REFUTED** | A `2x3` factor pair defeats every cycle-wise phase state. Stronger offsets, digit maps, or repairs are required. |
| PC4 | **OPEN** | No no-three multiplicative closure theorem is proved. |
| PC5 | **OPEN** | Arithmetic coverage cannot start until a closure or extension theorem is available. |
| PC6 | **PARTIAL** | Single cycle-bit flips are executable row-column-preserving trades and preserve both factor projections; carry-signature multiplicity is open. |

The completion criterion at the end of this file is **not** met.

## PC1 — Saturation-preserving product encoding

**Status: COMPLETE via Theorem PX1.**

### Target statement

Given saturated configurations `S_m subseteq [m]^2` and `S_n subseteq [n]^2`, define a set

\[
S_{mn}\subseteq[mn]^2
\]

with exactly two points in every row and column. Coordinates may be encoded as mixed radix pairs

\[
(x_1,x_2),\qquad(y_1,y_2),
\]

but the final object must be an ordinary integer grid set.

The construction should use exactly `2mn` distinct cells and retain a decomposition into two permutation layers.

### Result

Write the factor configurations as permutation pairs `sigma_0,sigma_1` and
`tau_0,tau_1`. On each orbit `C` of `tau_1^{-1} tau_0`, choose a phase bit for
each coarse row. The two flattened layers are

\[
\Pi_r(ni+u)
=
n\sigma_r(i)+\tau_{r\mathbin{\mathrm{xor}}\varepsilon_{i,C(u)}}(u).
\]

Theorem PX1 proves that both `Pi_r` are permutations and are cell-disjoint.

## PC2 — Cross-block line classification

**Status: PARTIAL via Theorems PX2 and PX3.**

### Target statement

Classify every possible collinear triple in the product encoding according to its coarse block coordinates and fine within-block coordinates. Prove that a triple would force at least one of:

1. a forbidden triple in `S_m`;
2. a forbidden triple in `S_n`;
3. a finite list of mixed carry equations;
4. an explicit resonance between block scales.

The mixed carry equations must be eliminated by the encoding or absorbed by a finite phase choice.

### Result

For flattened points `P_t=(ni_t+u_t,nj_t+v_t)`, the exact determinant is

\[
\det(P_0,P_1,P_2)=n^2\Delta_c+nM+\Delta_f.
\]

A bad triple has `Delta_f=n kappa`, `|kappa|<=n-2`, and satisfies

\[
n\Delta_c+M+\kappa=0.
\]

When both factors are no-three, every bad triple has exactly one of the four
coarse/fine distinct-point types `(2,2)`, `(2,3)`, `(3,2)`, `(3,3)`. The
remaining task is to eliminate their explicit resonance equations.

## PC3 — Scale-separation or phase theorem

**Status: OPEN; cycle-wise phases alone are REFUTED.**

### Target statement

Choose block offsets, slopes, digit permutations, or phase labels so that no mixed resonance from PC2 is possible. Candidate forms include:

- lexicographic scale separation;
- Sidon-type block offsets;
- affine phase choices attached to one factor;
- random permutations with an exact local-lemma proof;
- Chinese-remainder digit maps followed by a real-lift carry analysis.

The theorem must preserve the square side length `mn`; it may not enlarge the ambient grid by an uncontrolled factor.

### Falsification result

For one saturated no-three `2x2` factor and one saturated no-three `3x3`
factor, the fine alternating graph is one cycle and all four possible
cycle-phase states contain an explicit three-point line. Thus phase labels
attached only to alternating cycles cannot prove PC3 in the raw lexicographic
lift.

## PC4 — Product closure theorem

**Status: OPEN.**

### Target statement

For a specified class `C` of side lengths,

\[
m,n\in C\Longrightarrow mn\in C,
\]

where membership means an exact saturated no-three-in-line configuration exists. Provide an explicit polynomial-time coordinate construction from the factor configurations.

A weaker theorem allowing one factor from a special absorber class is also useful.

## PC5 — Arithmetic coverage

**Status: OPEN.**

### Target statement

Combine PC4 with base constructions to cover every sufficiently large integer. Possible routes:

- prove all prime powers are base cases and use multiplicative closure;
- prove a finite generating set of admissible factors;
- combine product closure with a bounded additive extension gadget;
- cover all smooth numbers by product and the remaining integers by a second base family.

State exactly which integers remain uncovered and provide finite constructions where possible.

## PC6 — Product-compatible repair machinery

**Status: PARTIAL via Theorem PX4.**

### Target statement

If the raw product is only a bounded-syndrome saturated seed, show that the current alternating-core or degree-constrained selection machinery respects the product decomposition. In particular:

- repair states remain row-column preserving in mixed-radix coordinates;
- cross-block carries have bounded signature multiplicity;
- the repair process cannot destroy the factor-level no-three property.

### Result

Toggling one phase bit on one fine alternating cycle removes and inserts the
same number of cells in two coarse blocks, preserves every row and column
exactly, and keeps all coarse and fine projections inside the original factor
configurations. The unresolved PC6 item is a useful bound on the multiplicity
of the four PC2 resonance signatures under sequences of such toggles.

## Candidate starting cases

- product of two affine permutation pairs;
- product of subgroup-coset absorbers with coprime orbit orders;
- one factor used only to assign phases to blocks of the other;
- tensoring two perfect matchings, then selecting two of the four layer products by a phase rule.

The last two candidates, when restricted to cycle-wise phases in the raw
mixed-radix lift, are insufficient by PX5.

## Mandatory falsification

- three points in distinct blocks aligned by coarse block centres;
- collinear triples created by base-`n` carries;
- duplicated rows or columns after flattening mixed-radix coordinates;
- products that work toroidally but fail after integer lifting;
- resonance when factor slopes are rationally related.

The verifier now checks row/column duplication, the exact base-`n` carry
identity, and explicit rational-slope resonances for all small factor pairs in
its configured range.

## Completion criterion

This branch is complete when PC1–PC6 give a rigorous closure operation and an arithmetic coverage theorem sufficient to derive `D(n)=2n` for all large `n`, followed by exact treatment of the remaining finite sizes.

**Current verdict:** not complete. PC1 is closed, PC2 and PC6 have exact partial
theorems, and the simplest PC3 phase mechanism is refuted.
