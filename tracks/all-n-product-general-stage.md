# All-n product track: general repair and protected-spread stage

**Branch:** `research/all-n-product-construction`

The finite full-selector stage proves exact factor-independent products

\[
2\times n\longrightarrow2n
\qquad(n=3,4,5,6),
\]

but no recursive or all-side exact closure.  This stage replaces larger
factorial template searches by two all-side structural routes:

1. low-syndrome descent and shadow decoding;
2. low-direction protection and protected spread.

The routes now meet at one explicit missing theorem.

## Current ledger

| Item | Status |
|---|---|
| General seed | **PROVED.** Every saturated side-`n` factor has a factor-compatible saturated side-`2n` rectangle state with `O(n log n)` bad triples (PX63). |
| Elementary repair | **PROVED.** Repeated column transpositions either reach no-three or end at logarithmic one-point or inserted-pair shadow concentration (PX67--PX69). |
| Conflict geometry | **PROVED.** High primitive height gives polynomial transversal-codegree saving, while height-one pairs have full-order codegree (PX70--PX73). |
| Structured recursion | **NEGATIVE IN TWO GROUPS.** The side-eight all-transposition class has no template with ordinary affine column maps (PX66) or with the 48-element bit-affine group (PX74), even with arbitrary `P` and the full selector. |
| Low-direction removal | **PROVED.** On rough moduli, an affine factor-compatible rectangle state protects every direction through height `H`; for primes one may take `H=Theta(sqrt(n))` (PX75--PX77). |
| Protected local states | **PROVED.** Additive cosets install `n/h` independent `h`-state absorbers preserving every protected line capacity (PX78). |
| Direct coset LLL | **CRITERION PROVED, SIMPLE BANK INSUFFICIENT.** Constant normalized certificate load implies exact closure (PX79), but the first `Z_25` bank has maximum load `1341.504`, versus threshold `1/12` (PX80). |
| Infinite closure | **OPEN.** No all-side exact doubling or multiplicatively closed infinite class is proved. |
| Arithmetic coverage | **OPEN.** The finite closures and approximate theorem do not cover all side lengths. |

## 1. Low-syndrome decoder route

Start with the PX63 state `Q` having

\[
D(Q)=O(n\log n).
\]

PX67--PX69 average every transposition in the two column labelings.  Either one
move lowers `D`, or a transposition-local minimum has a point-pair or pair-point
line shadow of order comparable to `D/n`.

Thus repeated descent terminates at:

1. an exact no-three product; or
2. an explicit logarithmic shadow concentration.

The remaining theorem on this route is a conversion or absorption result for
that concentrated shadow.  Generic monotone descent is already known to be
false, so the conversion must use the line geometry or a bounded composite
batch.

## 2. Direction-stratified matching route

The complete rectangle hypergraph has base degree

\[
d=n^3.
\]

For compatible rectangle edges `e,f`, PX71 gives

\[
\operatorname{codeg}_{\rm trans}(e,f)
\le
64n^2\left(1+\frac{2n}{h(e,f)}\right).
\]

At height `h>=n^delta`, this is `O(d^(1-delta/3))`, which has the polynomial
saving expected in conflict-free matching arguments.  PX72 proves that no
uniform saving is possible: height-one pairs have `Theta(d)` completions.

Therefore the low-height sector is the exact obstruction to a black-box
conflict-free matching theorem.

## 3. Protected affine and coset states

PX75 gives the affine rectangle family

\[
p(u)=u+s,
\qquad
t(u)=r(u)=mu+c\pmod n.
\]

If every protected direction `(a,b)` satisfies

\[
\gcd(b-am,n)=1,
\]

then each protected line contains at most one top and one bottom point.  PX76
chooses such a slope on rough moduli, and PX77 protects every primitive direction
through height `H` when the least prime factor exceeds `2H(H+1)+1`.

PX78 then replaces `u` by an independent translation inside each additive coset.
This supplies `h^(n/h)` states while preserving all protected capacities.

The construction solves the geometric codegree obstruction, but not the spread
problem.  PX80 shows that plain coset translations have enormous accumulated
certificate load even though every event depends on at most three variables.

## 4. Exact missing bridge

The next general theorem should construct a **protected spread distribution** on
the three independent labelings `(R,A,B)` from PX61 with all of the following.

1. **Protected capacity:** every primitive line through height `H` contains at
   most two selected points.
2. **Permutation spread:** every fixed-rank cylinder in each exposed labeling has
   probability `O((n)_k^{-1})`, or an equivalent power-saving bound.
3. **High-direction codegree:** after protection, PX71 supplies
   `O(n^2(1+2n/H))` transversal completions per compatible pair.
4. **Constant local certificate mass:** the normalized one-, two-, and
   three-variable loads satisfy a local-lemma or resampling threshold.
5. **Factor transport:** the distribution remains inside the normalized
   rectangle/full-host family, so PX41 transports it to every input factor.

For prime `n`, choosing `H=Theta(sqrt(n))` already gives high-direction codegree

\[
O(n^{5/2})=O(d^{5/6}).
\]

The missing content is entropy conditioned on the protected line injections.
For composite rough moduli, PX78 supplies local variables but not enough spread;
for primes, a different local entropy source is required.

## 5. Concrete next subproblems

1. **Shadow-to-direction conversion.** Prove that the logarithmic shadow
   concentration from PX69a either lies mostly in low-height directions or pays
   many bounded-support improving transpositions/batches.
2. **Two-coordinate coset bank.** Randomize the row labeling and the two column
   labelings independently inside compatible coset systems while retaining
   protected line-coordinate injectivity.
3. **Conditioned permutation spread.** Establish fixed-rank spread for
   permutations satisfying all protected line-capacity constraints.
4. **High-direction resampling.** Apply a conflict-free matching or local-lemma
   argument after the low directions have been removed.
5. **Prime entropy source.** Replace additive cosets by a switching distribution
   or a large protected permutation family on prime moduli.

## 6. Verification

```bash
python scripts/verify_product_low_syndrome_doubling.py
python scripts/verify_product_transposition_decoder.py
python scripts/verify_product_direction_stratification.py
python scripts/verify_product_bit_affine_transposition_eight.py
python scripts/verify_product_affine_rectangle_protection.py
python scripts/verify_product_protected_coset_absorbers.py
python scripts/verify_product_protected_coset_local_load.py
```

The overall no-three-in-line conjecture remains open.  None of PX63--PX80 is an
exact all-side closure theorem.