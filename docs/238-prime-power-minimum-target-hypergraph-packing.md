# A dirty minimum has disjoint target contraction or one rooted concentration

The robust-surplus chapters analyse target-destroying escape states. There is
also a static structure inside the chosen minimum itself. Its physical collinear
triples form a 3-uniform hypergraph on the `2n` selected cells.

A matching/cover dichotomy gives either many vertex-disjoint target triples or a
small cell cover. The disjoint bank is one compatible labelled prescription and
contracts host-representably. A small cover concentrates many targets on one
selected cell; exact line decomposition then gives a loaded target line or a
simultaneous secant-star bank, which enters CMR1046--CMR1069.

Let `S` be a saturated side-`n` state with

\[
m=\Phi(S)>0.
\]

Let `\mathcal H(S)` be the 3-uniform hypergraph whose vertices are the physical
cells of `S` and whose edges are the physical collinear triples of `S`.

## 1. Disjoint target bank or small cell cover

### Theorem CMR1070 -- PROVED

Fix an integer `q>=2`. At least one of the following holds.

1. **Disjoint target bank.** `\mathcal H(S)` contains `q` pairwise
   vertex-disjoint target triples.
2. **Small target cover.** There is a selected-cell set `C\subseteq |S|` with
   \[
   \boxed{|C|\le3(q-1)}
   \]
   meeting every target triple.

In the second branch, one selected cell belongs to at least

\[
\boxed{
\left\lceil\frac{m}{3(q-1)}\right\rceil
}
\]

target triples.

### Proof

Take a maximal vertex-disjoint target family. If it has size at least `q`, use the
first branch. Otherwise the union of its at most `q-1` triples has size at most
`3(q-1)` and meets every target, by maximality. Assign each of the `m` targets to
one cover cell it contains and average. ∎

## 2. A disjoint target bank is one compatible joint prescription

### Theorem CMR1071 -- PROVED

Let `T_1,\ldots,T_q` be pairwise physically disjoint targets of `S`, and let `P`
be their exact labelled realization in `S`. Then

\[
\boxed{|P|=3q,}
\]

and `P` is a compatible partial joint state.

Restricting the complete current family to states containing `P` preserves `S`
and its minimum value. The conditioned family is host-representable, and exact
contraction of `P` lowers residual labelled state cardinality by `3q` while
preserving minimality for the induced objective.

### Proof

The targets use disjoint physical cells. Their labelled edges form a subset of
the feasible joint state `S`, so they are compatible. The restriction contains
the known minimum `S`; apply CMR902. Host representability and induced contraction
are CMR974--CMR981. ∎

Thus a large target matching produces strict structural descent in one step.

## 3. Exact rooted target-line decomposition

Assume the concentrated branch of CMR1070 and let `z` be a selected cell contained
in `d` target triples. For every real line `L` through `z`, put

\[
r_L=|(|S|\setminus\{z\})\cap L|.
\]

### Theorem CMR1072 -- PROVED

\[
\boxed{
d=\sum_{L\ni z}\binom{r_L}{2}.}
\]

### Proof

Every target through `z` is determined by its other two selected cells, which lie
on one line through `z`. Conversely every two selected cells on one such line
form a target with `z`. Distinct lines through `z` partition the other selected
cells. ∎

## 4. Loaded line or simultaneous rooted star

### Theorem CMR1073 -- PROVED

Fix an integer `R>=3`. At least one of the following holds.

1. **Loaded target line.** Some line through `z` has `r_L>=R`. The minimum state
   contains at least
   \[
   \boxed{\binom{R+1}{3}}
   \]
   target triples on that line.
2. **Simultaneous geometric star.** There are at least
   \[
   \boxed{
   M_z
   \ge
   \left\lceil
   \frac{d}{\binom{R-1}{2}}
   \right\rceil
   }
   \]
   distinct lines through `z`. Choosing one outside pair from each line gives a
   cell-disjoint geometric secant-star bank, all occurring simultaneously in `S`.

### Proof

If the first branch fails, every line contributes at most
`\binom{R-1}{2}` to CMR1072. Choose one pair on every line with positive
contribution. Distinct line groups are disjoint away from `z`. In the first
branch the line contains `z` and at least `R` other selected cells, hence at least
`\binom{R+1}{3}` triples. ∎

## 5. Layer-polarized execution of the rooted star

### Theorem CMR1074 -- PROVED

The simultaneous star branch of CMR1073 reaches at least one of:

1. a common-layer outside-pair subbank of size at least `ceil(M_z/4)` and direct
   protected growth
   \[
   \boxed{2\max\{0,M_0-2k\};}
   \]
2. a cross-layer subbank of size at least `ceil(M_z/2)` and one-side protected
   growth
   \[
   \boxed{\max\{0,M_\times-2\min(k_c,k_o)\};}
   \]
3. large protected cores, finite protected-capacity expenditure, degree-two Hall
   rematching, rollback, contraction, structural exit, or strict potential
   improvement.

### Proof

Apply the simultaneous common-layer and cross-layer executions
CMR1054--CMR1069. ∎

No generic matching-vertex wall loss is needed because all arms occur in `S`.

## 6. Loaded target lines also execute

### Theorem CMR1075 -- PROVED

The loaded-line branch of CMR1073 reaches old-profile target destruction,
majority-layer protected absorption, a large protected core, finite protected
capacity, exact product descent, host transition, envelope exit, or strict
potential improvement.

### Proof

Apply CMR1046--CMR1053 and CMR1038--CMR1045. ∎

## 7. Total disjoint-target contraction is finite

Consider a sequence of disjoint-target contractions along one selected minimum
lineage. Let `q_i` be the number of disjoint target triples contracted at step
`i`, and let the initial labelled state cardinality be `K_0`.

### Theorem CMR1076 -- PROVED

\[
\boxed{
3\sum_iq_i\le K_0.
}
\]

For an initial saturated side-`n` state, `K_0=2n`, so

\[
\boxed{
\sum_iq_i\le\left\lfloor\frac{2n}{3}\right\rfloor.
}
\]

### Proof

Every contraction removes `3q_i` fixed labelled edges, and residual cardinality
never increases along the conditioned lineage. ∎

## 8. Minimum-target hypergraph endpoint

### Corollary CMR1077 -- PROVED

For every threshold pair `q>=2,R>=3`, a dirty minimum state reaches at least one
of:

1. host-representable contraction of `q` disjoint targets and rank decrease `3q`;
2. one selected cell in at least `ceil(m/(3(q-1)))` targets;
3. a line with at least `binom(R+1,3)` old targets;
4. a simultaneous common-layer or cross-layer secant-star execution;
5. protected growth, large-core product descent, Hall rematching, rollback,
   restoration/ancestry payment, factor/envelope exit, or strict potential
   improvement.

Thus the minimum's own target hypergraph has an exact packing/concentration
normal form. The remaining obstruction is a sequence of fixed-core target
contractions and structural exits which preserves a positive induced minimum.

### Proof

Combine CMR1070--CMR1076. ∎

No all-`n` theorem is claimed. Hypergraph packing/cover, compatible joint
contraction, rooted line decomposition, star extraction, and contraction budgets
are checked in
[`scripts/verify_prime_power_minimum_target_hypergraph.py`](../scripts/verify_prime_power_minimum_target_hypergraph.py).
