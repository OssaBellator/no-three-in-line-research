# All-n route C: product and composition constructions

**Branch:** `research/all-n-product-construction`

This branch is independent of prime patching and composite-ring conics. It seeks a composition rule that turns saturated no-three-in-line configurations at smaller side lengths into one at a product or other composite side length.

A naive Cartesian or block product fails because points from different blocks can form new long lines. The central work is an exact cross-block collinearity theorem.

## Progress ledger

The detailed proofs and counterexamples are in
[`docs/27-all-n-product-construction.md`](../docs/27-all-n-product-construction.md),
with exact finite checks and SAT search in
[`scripts/verify_product_construction.py`](../scripts/verify_product_construction.py).

| Item | Status | Current result |
|---|---|---|
| PC1 | **COMPLETE** | Independent cycle phases give two disjoint permutation layers for all four global coarse/fine radix orientations, in `O(mn)` time. |
| PC2 | **PARTIAL** | A general four-term determinant identity, all four coarse/fine multiplicity types, and the exact weighted-direction form of type `(2,2)` are proved. |
| PC3 | **OPEN / GLOBAL RADIX-PHASE ROUTE REFUTED** | One `2x3` factor pair defeats all 16 phase states in each of all four radix orientations. Phase feasibility is now an exact width-three CNF. |
| PC4 | **OPEN** | No useful no-three multiplicative closure theorem is proved. |
| PC5 | **OPEN** | Arithmetic coverage cannot start until a closure or extension theorem is available. |
| PC6 | **PARTIAL** | Cycle flips are executable factor-protected trades. The full factor-product host has line cap `4 min(m,n)` and pair codegree at most `4 min(m,n)-2`; arithmetic carry concentration remains open. |

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
`tau_0,tau_1`. On each orbit `C` of `tau_1^{-1} tau_0`, choose an independent
phase bit for each output layer and coarse row.

Each scalar coordinate may be flattened coarse-major or fine-major:

\[
X_c(i,u)=ni+u,\qquad X_f(i,u)=mu+i,
\]

\[
Y_c(j,v)=nj+v,\qquad Y_f(j,v)=mv+j.
\]

For every orientation `theta in {cc,cf,fc,ff}`, define

\[
\Pi_r^\theta(X_{\theta_x}(i,u))
=
Y_{\theta_y}\left(
\sigma_r(i),
\tau_{\varepsilon_{r,i,C(u)}}(u)
\right).
\]

Theorem PX1 proves that both layers are permutations and are cell-disjoint for
all four orientations.

## PC2 — Cross-block line classification

**Status: PARTIAL via Theorems PX2--PX4.**

### Target statement

Classify every possible collinear triple in the product encoding according to its coarse block coordinates and fine within-block coordinates. Prove that a triple would force at least one of:

1. a forbidden triple in `S_m`;
2. a forbidden triple in `S_n`;
3. a finite list of mixed carry equations;
4. an explicit resonance between block scales.

The mixed carry equations must be eliminated by the encoding or absorbed by a finite phase choice.

### Result

For one orientation, write

\[
F_\theta(i,j,u,v)
=
(a_i i+a_u u,\ a_j j+a_v v),
\]

where each coefficient pair is `(n,1)` in a coarse-major coordinate and `(1,m)`
in a fine-major coordinate. Then

\[
\det F_\theta
=
a_i a_j\Delta_{ij}
+a_i a_v\Delta_{iv}
+a_u a_j\Delta_{uj}
+a_u a_v\Delta_{uv}.
\]

This identity simultaneously covers all four radix orientations.

When both factors are no-three, every bad triple has exactly one of the four
coarse/fine distinct-point types

\[
(2,2),\ (2,3),\ (3,2),\ (3,3).
\]

Each type is obtained by setting the corresponding factor determinant to zero
or nonzero in the displayed identity.

For type `(2,2)`, after relabelling the points as three corners

\[
F_\theta(c_0,f_0),\quad
F_\theta(c_0,f_1),\quad
F_\theta(c_1,f_0),
\]

the exact obstruction is

\[
\det\bigl(B(f_1-f_0),A(c_1-c_0)\bigr)=0,
\]

where `A` and `B` are the diagonal coarse and fine scale matrices. Thus the
first resonance is precisely equality of weighted factor-secant directions.

In the ordinary `cc` orientation, the fine determinant is `n kappa` with

\[
|\kappa|\le n-2,
\]

and the carry normal form is

\[
n\Delta_{ij}+\Delta_{iv}+\Delta_{uj}+\kappa=0.
\]

The remaining task is to eliminate or absorb the four explicit resonance
families.

## PC3 — Scale-separation or phase theorem

**Status: OPEN; all global radix orientations with independent cycle phases are REFUTED.**

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
factor, the fine alternating graph is one cycle. There are four phase variables,
hence sixteen phase states in each radix orientation.

The verifier finds an explicit real integer collinearity in all

\[
4\cdot16=64
\]

phase/orientation states. Thus changing only whether each coordinate is
coarse-major or fine-major does not repair the independent cycle-phase route.

### Exact computational endpoint

For fixed factor pairs and a fixed orientation, Theorem PX7 builds a CNF with

\[
2mc
\]

variables, where `c` is the number of fine alternating cycles, clause width at
most three, and at most

\[
8\binom{2mn}{3}
\]

clauses. Its satisfying assignments are exactly the no-three phase states.

This turns finite PC3 testing into a reproducible exact SAT problem rather than
raw enumeration. The current script includes a standard-library DPLL model
counter and cross-checks it against direct enumeration on the smallest cases.

## PC4 — Product closure theorem

**Status: OPEN.**

### Target statement

For a specified class `C` of side lengths,

\[
m,n\in C\Longrightarrow mn\in C,
\]

where membership means an exact saturated no-three-in-line configuration exists. Provide an explicit polynomial-time coordinate construction from the factor configurations.

A weaker theorem allowing one factor from a special absorber class is also useful.

### Current evidence

Some small factor pairs have successful phase states in selected orientations:

- `(2,2)` has successes in all four orientations;
- `(3,2)` has successes only in the two crossed orientations among the tested states;
- `(2,4)` has successes in `ff`;
- `(4,2)` has successes in `cc`, `cf`, and `fc`.

However, `(2,3)`, `(3,3)`, `(3,4)`, `(4,3)`, `(2,5)`, and `(5,2)` have no
successful states in any global orientation in the exhaustive configured
range. These finite positives do not form a closure class.

## PC5 — Arithmetic coverage

**Status: OPEN.**

### Target statement

Combine PC4 with base constructions to cover every sufficiently large integer. Possible routes:

- prove all prime powers are base cases and use multiplicative closure;
- prove a finite generating set of admissible factors;
- combine product closure with a bounded additive extension gadget;
- cover all smooth numbers by product and the remaining integers by a second base family.

State exactly which integers remain uncovered and provide finite constructions where possible.

No arithmetic coverage statement follows from the current finite successes.

## PC6 — Product-compatible repair machinery

**Status: PARTIAL via Theorems PX5 and PX6.**

### Target statement

If the raw product is only a bounded-syndrome saturated seed, show that the current alternating-core or degree-constrained selection machinery respects the product decomposition. In particular:

- repair states remain row-column preserving in mixed-radix coordinates;
- cross-block carries have bounded signature multiplicity;
- the repair process cannot destroy the factor-level no-three property.

### Results

Toggling one phase bit on one fine alternating cycle removes and inserts the
same number of cells in one coarse factor point, preserves every row and column
exactly in all four orientations, and keeps all coarse and fine projections
inside the original factor configurations.

For the full factor-product host

\[
\mathcal H^\theta_{m,n}
=
\{F_\theta(c,f):c\in S_m,\ f\in S_n\},
\]

Theorem PX6 proves:

- at most two points of a fixed coarse projection lie on one real line;
- at most two points of a fixed fine projection lie on one real line;
- every line contains at most `4 min(m,n)` host points;
- every fixed pair has at most `4 min(m,n)-2` third-point candidates.

This supplies a uniform projection-signature and pair-codegree bound. The
unresolved PC6 work is sharper concentration by the actual arithmetic carry
values in PX2, followed by a repair/termination theorem using that structure.

## Candidate starting cases

- phase choices beyond complete alternating cycles, while preserving each
  block matching;
- non-global digit bijections rather than only `cc`, `cf`, `fc`, `ff`;
- product of subgroup-coset absorbers with coprime orbit orders;
- a local-lemma or resampling theorem applied to the PX7 clause system using
  PX6 codegree bounds;
- one factor used only to assign structured offsets to blocks of the other.

The raw four-layer tensor host is impossible: PX4 shows that common horizontal
and vertical factor directions create immediate type-`(2,2)` triples.

## Mandatory falsification

- three points in distinct blocks aligned by coarse block centres;
- collinear triples created by base-`n` carries;
- duplicated rows or columns after flattening mixed-radix coordinates;
- products that work toroidally but fail after integer lifting;
- resonance when factor slopes are rationally related;
- apparent successes caused by incomplete phase enumeration.

The verifier now checks all four global radix orientations, row/column
duplication, the exact general determinant identity, the ordinary carry
identity, SAT/direct-enumeration equivalence, and explicit real collinearities.

## Completion criterion

This branch is complete when PC1–PC6 give a rigorous closure operation and an arithmetic coverage theorem sufficient to derive `D(n)=2n` for all large `n`, followed by exact treatment of the remaining finite sizes.

**Current verdict:** not complete. PC1 is closed; PC2 and PC6 now have stronger
exact partial theorems; PC3 has an exact SAT endpoint but the enlarged global
radix-phase route is refuted; PC4 and PC5 remain open.
