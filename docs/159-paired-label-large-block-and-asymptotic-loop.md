# Paired-label large-block margin and the repaired PX63 loop

PX397--PX444 provide an invariant-preserving repair language for rectangle
states.  PX397--PX403 give an entry block from every nonzero bad-triple set;
PX411--PX419 remove channel dependence; PX420--PX427 lift clean-star, radial,
and loaded-line banks; PX428--PX436 lift packet corrections; and PX437--PX444
lift mixed shadows and packet recurrence.

Pairing introduces at most `2^r<=8` geometric copy patterns in rank `r`.  The
adaptive thinning constants below pay that factor explicitly.  In particular,
internal rank-three creation is bounded by a fixed fraction of the old
destruction supplied by a large label block.

This chapter states the resulting asymptotic repair loop.  The later effective
audit PX451--PX470 supplies the explicit incidence constant, recursion depth,
and divisor witness needed to turn the asymptotic threshold into a computable
one.

## 1. Explicit paired thinning margins

Let a label block have original order `t`, ambient grid order `N`, inherited
label forbidden degree `Delta`, and saturated background size at most `2N`.
Let `mathfrak d(N)` be the divisor cap and use the explicit Cartesian constant

\[
A_3=320
\]

from PX460.  Put

\[
L_\Delta
=
8\cdot512A_3e^{2\Delta}
=
1{,}310{,}720e^{2\Delta}.
\]

Fix

\[
0<\eta\le\frac1{12}.
\]

Define

\[
C_{\Delta,\eta}
=
\frac{32768e^{4\Delta}}{\eta}
\]

and

\[
\boxed{
q_\eta
=
\min\left\{
\frac{\eta}{16L_\Delta\log(2t)},
\frac{t}{C_{\Delta,\eta}N\mathfrak d(N)}
\right\}.
}
\]

Finally put

\[
\boxed{
B_{\Delta}
=
\max\left\{
32,
16\Delta+4,
256e^{2\Delta}
\right\}.
}
\]

### Theorem PX445 -- PROVED, CONSTANTS CORRECTED

Assume

\[
q_\eta t\ge B_\Delta.
\]

Then there is a retained paired label block of order

\[
s\ge q_\eta t/2
\]

for which:

1. paired rank-two support-four expected creation is at most
   
   \[
   \boxed{\eta s/8;}
   \]
2. paired internal rank-three support five and six have expected load at most
   
   \[
   \boxed{\eta s/8;}
   \]
3. paired internal rank-three support three and four have expected load at most
   
   \[
   \boxed{\frac{11}{96}s;}
   \]
4. every fixed-rank external cylinder retains the optimized bounded-forbidden
   denominator, with only its copy-pattern multiplicity.

Consequently

\[
\boxed{
\mathbb E T_3^{\rm internal}
\le
\frac{s}{8}.
}
\]

For fixed `Delta,eta` and every fixed `epsilon>0`, the hypotheses hold for all
large `N` whenever

\[
t\ge N^{1/2+\epsilon}.
\]

### Proof

PX225 gives the one-copy relative support-four bound

\[
512e^{4\Delta}\frac{qN\mathfrak d(N)}t.
\]

Multiplying by eight and using the second term in `q_eta` gives

\[
4096e^{4\Delta}
\frac{q_\eta N\mathfrak d(N)}t
\le
\frac\eta8.
\]

PX333 with `A_3=320`, followed by the factor-eight copy split, gives

\[
\frac{\mathbb E(T_{3,5}+T_{3,6})}{s}
\le
L_\Delta
\left(q_\eta\log(2t)+q_\eta^2\log(2t)\right).
\]

Since `q_eta<=1`, the parenthesis is at most
`2q_eta log(2t)`.  The first term in `q_eta` therefore makes this ratio at most
`eta/8`.

PX332 contributes at most

\[
8\cdot\frac{11}{6}e^{2\Delta}
=
\frac{44}{3}e^{2\Delta}
\]

in support three and four.  The retained-order condition gives

\[
s\ge128e^{2\Delta},
\]

so this is at most `11s/96`.  Finally `eta<=1/12` implies

\[
\frac{11}{96}+\frac{\eta}{8}
\le
\frac18.
\]

The asymptotic threshold follows from `mathfrak d(N)=N^(o(1))`; PX468 later
makes it effective at exponent `3/5`. \(\square\)

The paired support-four term is external rank two and may alternatively be sent
to the packet decoder PX435.

## 2. Paired internal gap

### Theorem PX446 -- PROVED REDUCTION, EXPLICIT MARGIN

Under PX445, some allowed paired label-bank state satisfies

\[
\boxed{c_3\le s/8<s.}
\]

Every clean-star or radial label block destroys at least `s` injectively
assigned old certificates.  Every loaded-line block has the stronger exact
line destruction of PX422.  Therefore

\[
\boxed{d_\sigma>c_3}
\]

for the chosen state, and the corrected external blocker forest PX324--PX329
applies.  Every child of that forest is implementable by the rectangle label
moves PX420--PX444.

### Proof

Choose a state whose internal rank-three load is at most the expectation in
PX445.  Insert the exact old-destruction bounds PX421--PX423 and use the causal
ledger PX235--PX243. \(\square\)

## 3. Host-compatible large-block strict-sign interface

### Theorem PX447 -- PROVED REDUCTION

For ambient `N` satisfying the paired thinning conditions, every
factor-compatible rectangle label block above the chosen ambient threshold has
one of:

1. a strict decrease of the full bad-triple potential;
2. a deeper clean-star, radial, loaded-line, packet, or mixed-shadow label child;
3. a smaller nested label block;
4. a bounded high-source terminal label child.

Every transition preserves the PX43 rectangle normal form and all factor
projections.

### Proof

PX446 supplies the internal gap.  PX324--PX329 convert all external support-one
and support-two debt into deeper children.  PX427 handles first-generation
children, PX436 handles selected packet corrections, and PX444 handles mixed
and packet-recurrence children.  PX263--PX266 give nested shrinkage; PX417--PX419
handle bounded high-source returns. \(\square\)

## 4. Every nonzero rectangle state enters large or high-source repair

Let `Q` be any factor-compatible rectangle state with `D(Q)>0`.  Apply the
one-hit construction PX397--PX398, obtaining one label family with assigned
weight `W>=2D/9` on a source set `C`.

### Theorem PX448 -- PROVED

For every threshold `T>=1`, one of the following holds.

1. `|C|>=T`, giving a factor-compatible label block of order at least `T` with
   assigned old destruction at least `2D/9` and a constant-density derangement
   subbank.
2. One source label carries assigned old weight greater than
   
   \[
   \boxed{\frac{2D}{9T}.}
   \]

Thus every positive rectangle state enters either the large-block interface
PX447 or the one-source terminal-return interface PX416--PX419.

### Proof

The source weights sum to at least `2D/9`.  If fewer than `T` sources are
positive, one exceeds the average.  Host compatibility and derangement spread
are PX399--PX401 and PX412. \(\square\)

## 5. Conditional asymptotic repair loop

### Theorem PX449 -- PROVED UNDER LABEL-INTERFACE REDUCTIONS

For every sufficiently large ambient order `N`, every factor-compatible
rectangle state with positive bad-triple potential admits a finite causal
subtree ending in a strict potential decrease.

No independent channel-count or selected-line hypothesis is required.

### Proof

Use PX448.  A large entry enters PX447.  A high-source entry enters the
channel-free amplification PX417--PX419.  PX418 and the actual PX64 line cap
return it in bounded depth to a large clean star, loaded line, or label block,
unless an improvement occurs earlier.  PX394 gives lexicographic descent inside
the causal subtree.  All leaves preserve rectangle form. \(\square\)

### Corollary PX450 -- PROVED REDUCTION, ASYMPTOTIC

Under the label-interface reductions of PX449, every sufficiently large
saturated no-three side-`n` factor has a factor-compatible side-`2n` rectangle
state with zero bad triples.

PX63 supplies a state with finite integer potential `O(n log n)`.  Apply PX449
repeatedly.  Each completed repair subtree lowers the potential by at least one
and remains in the same factor-compatible rectangle state space, so after
finitely many iterations the potential reaches zero.

PX450 is not yet unconditional exact all-side closure.  The remaining audit
items are:

1. compute one common cutoff from PX453 using PX460, PX465, and PX468;
2. verify all below-cutoff base orders or provide an independent route into the
   asymptotic range;
3. complete the mechanical dependency audit of PX397--PX449;
4. update the global theorem index only after those checks pass.

## 6. Verification

Run

```bash
python scripts/verify_product_paired_large_block_margin.py
```

The verifier checks both explicit `eta/8` margins, the support-three/four
retained-order constant, the ambient threshold exponent, and integer-potential
termination.
