# All-n route C: product and composition constructions

**Branch:** `research/all-n-product-construction`

This branch is independent of prime patching and composite-ring conics. It seeks a composition rule that turns saturated no-three-in-line configurations at smaller side lengths into one at a product or other composite side length.

A naive Cartesian or block product fails because points from different blocks can form new long lines. The central work is an exact cross-block collinearity theorem.

## PC1 — Saturation-preserving product encoding

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

## PC2 — Cross-block line classification

### Target statement

Classify every possible collinear triple in the product encoding according to its coarse block coordinates and fine within-block coordinates. Prove that a triple would force at least one of:

1. a forbidden triple in `S_m`;
2. a forbidden triple in `S_n`;
3. a finite list of mixed carry equations;
4. an explicit resonance between block scales.

The mixed carry equations must be eliminated by the encoding or absorbed by a finite phase choice.

## PC3 — Scale-separation or phase theorem

### Target statement

Choose block offsets, slopes, digit permutations, or phase labels so that no mixed resonance from PC2 is possible. Candidate forms include:

- lexicographic scale separation;
- Sidon-type block offsets;
- affine phase choices attached to one factor;
- random permutations with an exact local-lemma proof;
- Chinese-remainder digit maps followed by a real-lift carry analysis.

The theorem must preserve the square side length `mn`; it may not enlarge the ambient grid by an uncontrolled factor.

## PC4 — Product closure theorem

### Target statement

For a specified class `C` of side lengths,

\[
m,n\in C\Longrightarrow mn\in C,
\]

where membership means an exact saturated no-three-in-line configuration exists. Provide an explicit polynomial-time coordinate construction from the factor configurations.

A weaker theorem allowing one factor from a special absorber class is also useful.

## PC5 — Arithmetic coverage

### Target statement

Combine PC4 with base constructions to cover every sufficiently large integer. Possible routes:

- prove all prime powers are base cases and use multiplicative closure;
- prove a finite generating set of admissible factors;
- combine product closure with a bounded additive extension gadget;
- cover all smooth numbers by product and the remaining integers by a second base family.

State exactly which integers remain uncovered and provide finite constructions where possible.

## PC6 — Product-compatible repair machinery

### Target statement

If the raw product is only a bounded-syndrome saturated seed, show that the current alternating-core or degree-constrained selection machinery respects the product decomposition. In particular:

- repair states remain row-column preserving in mixed-radix coordinates;
- cross-block carries have bounded signature multiplicity;
- the repair process cannot destroy the factor-level no-three property.

## Candidate starting cases

- product of two affine permutation pairs;
- product of subgroup-coset absorbers with coprime orbit orders;
- one factor used only to assign phases to blocks of the other;
- tensoring two perfect matchings, then selecting two of the four layer products by a phase rule.

## Mandatory falsification

- three points in distinct blocks aligned by coarse block centres;
- collinear triples created by base-`n` carries;
- duplicated rows or columns after flattening mixed-radix coordinates;
- products that work toroidally but fail after integer lifting;
- resonance when factor slopes are rationally related.

## Completion criterion

This branch is complete when PC1–PC6 give a rigorous closure operation and an arithmetic coverage theorem sufficient to derive `D(n)=2n` for all large `n`, followed by exact treatment of the remaining finite sizes.