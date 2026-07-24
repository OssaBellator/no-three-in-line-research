# All-n route C: product and composition constructions

**Branch:** `research/all-n-product-construction`

This branch is independent of prime patching and composite-ring conics. It seeks a composition rule that turns saturated no-three-in-line configurations at smaller side lengths into one at a product or other composite side length.

A naive Cartesian or block product fails because points from different blocks can form new long lines. The central work is an exact cross-block collinearity theorem.

## Progress ledger

The detailed proofs and counterexamples are in
[`docs/27-all-n-product-construction.md`](../docs/27-all-n-product-construction.md),
with exact finite checks and SAT search in
[`scripts/verify_product_construction.py`](../scripts/verify_product-construction.py).

| Item | Status | Current result |
|---|---|---|
| PC1 | **COMPLETE / STRENGTHENED** | Cycle phases work in all four radix orientations, and every degree-two subset of the full four-regular product host decomposes into two disjoint permutation layers. |
| PC2 | **PARTIAL** | The general determinant identity, four multiplicity types, and exact weighted type-`(2,2)` resonance are proved; simultaneous hybrid resonance elimination remains open. |
| PC3 | **OPEN / TWO RESTRICTED ROUTES REFUTED** | Phase feasibility and full-host degree-two feasibility both have exact width-three CNFs. The full selector repairs `2x3` and some `3x3` cases, but all tested `2x5` and `5x2` full hosts fail. |
| PC4 | **OPEN** | No infinite no-three multiplicative closure theorem is proved. |
| PC5 | **OPEN / FINITE CERTIFICATES** | Product searches give exact saturated configurations at sides 6, 8, and 9, but no generating family or arithmetic coverage. |
| PC6 | **SUBSTANTIAL PARTIAL** | All degree-two product states are connected by executable alternating-cycle trades. Lines, pair codegrees, and fixed nonzero carry levels have explicit multiplicity bounds; monotone hybrid-resonance repair remains open. |

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

Theorem PX9 enlarges the state space. The full factor-product host is a
four-regular bipartite graph on scalar rows and columns. Every spanning
degree-two subgraph is saturated and decomposes into two permutation layers by
alternating the edges on its even cycles. Thus cycle phases are a convenient
subfamily, not the complete factor-compatible state space.

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

### Enlarged full-host endpoint

Theorem PX10 gives a second width-three CNF with one variable for each of the
`4mn` host cells. Exact degree two at every row and column costs `16mn`
three-clauses, and every real-collinear host triple contributes one negative
three-clause.

This larger state space strictly improves on cycle phases. The exact `2x3`
phase counterexample has no phase solution in any orientation, but its crossed
product host contains the no-three layers

\[
(1,5,3,0,4,2),\qquad(3,1,5,2,0,4).
\]

It also produces side-nine configurations from selected `3x3` factor pairs.
However, exhaustive search over every ordered saturated no-three factor pair of
sizes `2` and `5`, in all four global orientations, finds no degree-two
no-three host state. Therefore the full four-orientation product host is still
not a universal PC3 theorem.

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

The full-host selector gives exact positive product instances at `2x2`, `2x3`,
`3x2`, `3x3`, `2x4`, and `4x2`, depending on factor pair and orientation. It
strictly contains the cycle-phase family and repairs the original `2x3`
obstruction.

The same exact search gives zero models for all 128 ordered `2x5` factor-pair
instances and all 128 ordered `5x2` instances in each of the four orientations.
Hence neither cycle phases nor arbitrary degree-two selection in the unmodified
factor-product host defines a multiplicatively closed class.

## PC5 — Arithmetic coverage

**Status: OPEN.**

### Target statement

Combine PC4 with base constructions to cover every sufficiently large integer. Possible routes:

- prove all prime powers are base cases and use multiplicative closure;
- prove a finite generating set of admissible factors;
- combine product closure with a bounded additive extension gadget;
- cover all smooth numbers by product and the remaining integers by a second base family.

State exactly which integers remain uncovered and provide finite constructions where possible.

The product searches give explicit saturated no-three configurations at side
lengths 6, 8, and 9. They are verified independently in
`docs/28-product-finite-witnesses.md` and
`scripts/verify_product_witnesses.py`.

No arithmetic coverage statement follows from these finite successes.

## PC6 — Product-compatible repair machinery

**Status: PARTIAL via Theorems PX5, PX6, PX11, and PX12.**

### Target statement

If the raw product is only a bounded-syndrome saturated seed, show that the current alternating-core or degree-constrained selection machinery respects the product decomposition. In particular:

- repair states remain row-column preserving in mixed-radix coordinates;
- cross-block carries have bounded signature multiplicity;
- the repair process cannot destroy the factor-level no-three property.

### Results

PX5 proves that each original phase-cycle toggle is an executable
row-column-preserving factor-protected trade in every global orientation.

For the full factor-product host

\[
\mathcal H^\theta_{m,n}
=
\{F_\theta(c,f):c\in S_m,\ f\in S_n\},
\]

PX6 proves:

- at most two points of a fixed coarse projection lie on one real line;
- at most two points of a fixed fine projection lie on one real line;
- every line contains at most `4 min(m,n)` host points;
- every fixed pair has at most `4 min(m,n)-2` third-point candidates.

PX11 proves that any two degree-two host states differ by edge-disjoint
alternating cycles. Toggling those cycles one at a time keeps every row and
column at degree two and never leaves the factor-product host. Thus the entire
factor-compatible saturation state space is connected by executable trades.

PX12 gives an arithmetic carry bound. For any no-three set of `s` points, the
number of ordered triples at one fixed nonzero signed determinant is at most
`2s(s-1)`. Consequently, for a fixed ordered coarse projected triple and a
fixed nonzero ordinary fine carry `kappa`, at most

\[
4n(2n-1)
\]

ordered fine projected triples satisfy `Delta_uv=n kappa`. The analogous
coarse bound is `4m(2m-1)`.

The unresolved PC6 work is simultaneous concentration of the two hybrid
determinants in PX2 and a monotone or resampling rule for choosing the
alternating-cycle trades.

## Candidate starting cases

- non-global digit bijections or block offsets that enlarge the host beyond the
  four global radix orientations and escape the exact `2x5` obstruction;
- a local-lemma, resampling, or entropy-compression theorem for the PX10
  exact-degree 3-CNF using PX6 and PX12;
- a monotone collinearity potential along the alternating-cycle state graph of
  PX11;
- joint concentration bounds for `(Delta_iv,Delta_uj,kappa)` rather than one
  determinant level at a time;
- product hosts built from subgroup-coset absorbers with additional offset
  states, not only the raw tensor cells.

The raw four-layer tensor host without degree-two selection is impossible: PX4
shows that common horizontal and vertical factor directions create immediate
type-`(2,2)` triples. The degree-two host is strictly stronger than cycle
phases, but the exhaustive `2x5` zero shows that it also needs enlargement.

## Mandatory falsification

- three points in distinct blocks aligned by coarse block centres;
- collinear triples created by base-`n` carries;
- duplicated rows or columns after flattening mixed-radix coordinates;
- products that work toroidally but fail after integer lifting;
- resonance when factor slopes are rationally related;
- apparent successes caused by incomplete phase enumeration.

The verification suite now checks all four global radix orientations,
row/column duplication, the exact determinant and carry identities, phase and
full-host CNF equivalence on base cases, exhaustive degree-two model counts,
explicit side-6/8/9 witnesses, and fixed signed-area multiplicity through side
five.

## Completion criterion

This branch is complete when PC1–PC6 give a rigorous closure operation and an arithmetic coverage theorem sufficient to derive `D(n)=2n` for all large `n`, followed by exact treatment of the remaining finite sizes.

**Current verdict:** not complete. PC1 is closed in the full product-host state
space. PC2 has exact resonance formulae. PC3 now has exact phase and
full-selector CNFs, but both unmodified global-host routes have finite
obstructions. PC6 has connected executable repair states and one-coordinate
carry concentration, while the joint hybrid-resonance termination theorem,
PC4 closure, and PC5 arithmetic coverage remain open.
