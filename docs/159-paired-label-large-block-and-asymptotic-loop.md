# Paired-label large-block margin and the repaired PX63 loop

PX397--PX444 now provide an invariant-preserving repair language for rectangle
states.  PX397--PX403 give an entry block from every nonzero bad-triple set;
PX411--PX419 remove channel dependence; PX420--PX427 lift clean-star, radial,
and loaded-line banks; PX428--PX436 lift packet corrections; and PX437--PX444
lift mixed shadows and packet recurrence.

The only quantitative concern introduced by pairing is an absolute increase in
candidate copy patterns.  A rank-`r` certificate has at most `2^r<=8` copy
patterns.  Adaptive thinning has a free constant factor, so this increase can
be paid while retaining the same square-root ambient exponent.  Internal
rank-three creation remains strictly below the old destruction supplied by a
large label block.

This chapter states the resulting asymptotic repair loop carefully.  It proves
an invariant-preserving strict-decrease interface for all sufficiently large
ambient orders.  The final exact all-side closure still requires a finite-order
cutoff audit and a formal dependency check that every invoked reduction uses
only the displayed label-level hypotheses.

## 1. Adjustable paired support-four margin

Let a label block have original order `t`, ambient grid order `N`, inherited
label forbidden degree `Delta`, and saturated background size at most `2N`.
Let `mathfrak d(N)` be the divisor cap.  Pairing increases the one-copy
support-four candidate weight by at most a factor eight, using the slack bound
of PX430.

Fix `0<eta<1`.  Put

\[
C_{\Delta,\eta}
=
\frac{8192e^{4\Delta}}{\eta}
\]

and choose

\[
\boxed{
q_\eta
=
\min\left\{
\frac{\eta}{128\log(2t)},
\frac{t}{C_{\Delta,\eta}N\mathfrak d(N)}
\right\}.
}
\]

### Theorem PX445 -- PROVED

Assume

\[
q_\eta t\ge\max(32,16\Delta+4).
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
   `O_Delta(eta s)`;
3. paired internal rank-three support three and four have expected load
   `O_Delta(1)`;
4. every fixed-rank external cylinder retains the optimized bounded-forbidden
   denominator, with only its copy-pattern multiplicity.

For fixed `Delta,eta` and every fixed `epsilon>0`, the hypotheses hold for all
large `N` whenever

\[
\boxed{t\ge N^{1/2+\epsilon}.}
\]

### Proof

PX225 gives the one-copy relative support-four bound

\[
512e^{4\Delta}\frac{qN\mathfrak d(N)}t.
\]

Multiply by eight and use the second term in `q_eta`; the chosen constant leaves
more than the displayed margin.  PX227 and PX333 bound internal support-five
and six relative to `s` by constant multiples of
`q log(2t)+q^2 log(2t)`.  Multiplication by eight is paid by the first term in
`q_eta`.  PX332 makes support three/four constant-scale, again stable under an
absolute factor.

The threshold calculation is unchanged: `mathfrak d(N)=N^(o(1))`, and changing
constants or the logarithmic cap does not alter the exponent one half.
\(\square\)

The support-four term is external rank two and may also be sent to the paired
packet decoder PX435; the expectation margin is recorded because it gives an
independent direct payment route.

## 2. Paired internal gap

Choose `eta` sufficiently small in terms of the fixed absolute constants in the
support-five/six estimates.  Let `c_3` be the total internal rank-three creation
of one retained label-bank state.

### Theorem PX446 -- PROVED REDUCTION

For every sufficiently large retained label block of order `s`, some allowed
bank state satisfies

\[
\boxed{c_3<s/2.}
\]

Every clean-star or radial label block destroys at least `s` injectively
assigned old certificates.  Every loaded-line block has the stronger exact
line destruction of PX422.  Therefore

\[
\boxed{d_\sigma>c_3}
\]

for the chosen state, and the corrected external blocker forest PX324--PX329
applies.

All children of that forest can be implemented by rectangle label moves from
PX420--PX444.

### Proof

Apply PX445 with a small fixed `eta`.  The support-five/six contribution is a
small fixed fraction of `s`; support three/four is `O_Delta(1)` and is below the
remaining margin for sufficiently large `s`.  Average over the allowed bank and
choose one state below the expectation.

The destruction statements are PX421--PX423 and the exact causal ledger
PX235--PX243.  The child invariant is PX444. \(\square\)

## 3. Host-compatible large-block strict-sign interface

### Theorem PX447 -- PROVED REDUCTION

For ambient `N` sufficiently large, every factor-compatible rectangle label
block above the square-root ambient threshold satisfies one of:

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

Let `Q` be any factor-compatible rectangle state with `D(Q)>0`, not necessarily
the original random PX63 realization.  Apply the one-hit construction
PX397--PX398, obtaining one label family with assigned weight `W>=2D/9` on a
source set `C`.

### Theorem PX448 -- PROVED

For every threshold `T>=1`, one of the following holds.

1. `|C|>=T`, giving a factor-compatible label block of order at least `T` with
   assigned old destruction at least `2D/9` and a constant-density derangement
   subbank.
2. One source label carries assigned old weight greater than
   
   \[
   \boxed{\frac{2D}{9T}.}
   \]

In particular, if `T` is the square-root ambient threshold, every nonzero state
enters either the large-block interface PX447 or the one-source terminal-return
interface PX416--PX419.

### Proof

The source weights sum to at least `2D/9`.  If fewer than `T` sources are
positive, one exceeds the average.  Host compatibility and derangement spread
are PX399--PX401 and PX412. \(\square\)

This replaces the earlier `c in {1,2}` terminal split by a direct
large-source/high-source dichotomy valid for every entry order.

## 5. Conditional asymptotic repair loop

Start from the PX63 state, whose potential is `O(N log N)`.  Every strict repair
move preserves rectangle form by PX444, so PX448 may be reapplied after each
decrease.

### Theorem PX449 -- PROVED UNDER LABEL-INTERFACE REDUCTIONS

For every sufficiently large ambient order `N`, assume the exact causal child
interfaces cited in PX447 and their inherited label-degree bounds.  Then every
factor-compatible rectangle state with positive bad-triple potential admits a
finite causal subtree ending in a strict potential decrease.

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

Indeed, PX63 supplies a state with finite integer potential `O(n log n)`.  Apply
PX449 repeatedly.  Each completed repair subtree lowers the potential by at
least one and remains in the same factor-compatible rectangle state space, so
after finitely many iterations the potential reaches zero.

PX450 is the first asymptotic exact-doubling reduction on this branch.  It is
not yet recorded as unconditional exact closure because the following audit
items remain:

1. instantiate one common finite cutoff satisfying every paired spread,
   divisor, and terminal-transposition inequality;
2. verify all below-cutoff base orders or provide an independent route into the
   asymptotic range;
3. mechanically audit the dependency chain PX397--PX449 for hidden use of an
   individual-point move rather than its paired label lift;
4. update the global theorem index and construction statement only after that
   audit.

The classical no-three-in-line conjecture and exact all-side closure remain
open.

## 6. Verification

Run

```bash
python scripts/verify_product_paired_large_block_margin.py
```

The verifier checks the adjustable support-four constant, the logarithmic
paired rank-three cap, the square-root threshold exponent, the internal-gap
margin, and the integer-potential termination implication.
