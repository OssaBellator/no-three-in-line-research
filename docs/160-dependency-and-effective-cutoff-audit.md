# Dependency manifest and effective cutoff audit

PX450 reduces asymptotic exact doubling to a common cutoff and a dependency
audit.  This chapter makes both targets machine-readable.  The dependency graph
is stored in

`proofs/product-entry-invariant-dependencies.json`.

The graph confirms that the terminal path from PX397 to PX450 ends in rectangle
label moves.  The cutoff calculation, however, exposes three numerical witnesses
that are not yet instantiated in the theorem files:

1. an explicit absolute constant `A_3` in the Cartesian-product collinear-triple
   estimate used by PX333;
2. an effective divisor-bound witness for `mathfrak d(N)=N^(o(1))`;
3. one explicit nested-depth envelope replacing the `O(log log N)` constant in
   PX265.

Once those witnesses are supplied, every remaining asymptotic inequality is a
finite computable predicate.

## 1. The declared dependency graph

Let the seven theorem blocks be

\[
397\text{--}403,
404\text{--}410,
411\text{--}419,
420\text{--}427,
428\text{--}436,
437\text{--}444,
445\text{--}450.
\]

### Theorem PX451 -- PROVED

The declared dependency graph on these blocks is acyclic.  Every move-producing
block on a directed path to PX450 has move-space tag

\[
\boxed{\texttt{rectangle_label}}
\]

and every remaining block is tagged `arithmetic_only`.

No terminal dependency uses the deleted individual-point batching theorem or
the obsolete inaccessible-PX63 premise.

### Proof

Read the JSON manifest.  Its block order is topological: every continuation
block depends only on earlier continuation blocks and pre-PX397 theorems.  The
allowed move-space tags are listed in the manifest safety rules.  The duplicate
endpoint-type theorem was deleted before this manifest was created. \(\square\)

## 2. Theorem-ID and constant audit

### Theorem PX452 -- PROVED REDUCTION

A repository audit for the range PX397--PX450 must verify:

1. every theorem ID occurs in exactly one theorem heading;
2. the continuation index records exactly the same IDs;
3. the paired support-four denominator is `32768`, not `8192`;
4. the entry good-bank cylinder factor is nine;
5. the entry good-bank destruction denominator is eighteen;
6. the rectangle point-type and label-family counts are four and two.

The script in Section 6 performs these checks directly on repository text.

The uniqueness requirement is substantive: an earlier draft reused
PX356--PX361 and was removed because those IDs already belonged to the weighted
return theory.

## 3. Effective numerical witnesses

Fix a target square-root excess `epsilon>0` and margin `0<eta<1`.  An
**effective cutoff witness** consists of:

1. a rational constant `A_3>=1` such that
   
   \[
   W_{3,5}+W_{3,6}
   \le
   A_3t^4\log(2t)
   \]
   
   for every Cartesian candidate block;
2. rational `rho>0` and integer `N_div` such that
   
   \[
   \mathfrak d(N)\le N^\rho
   \quad(N\ge N_{\rm div});
   \]
3. an integer-valued depth envelope `d_*(N)` verified against the exact PX265
   recurrence;
4. the resulting label-degree envelope
   
   \[
   \Delta_*(N)=3+2d_*(N),
   \]
   
   where the extra two pays one line-avoidance graph in addition to the current
   diagonal and historical label restrictions.

Choose `rho<2epsilon`.  Put

\[
T(N)=\left\lceil N^{1/2+\epsilon}\right\rceil,
\]

\[
B(N)=
\max\left\{
32,
16\Delta_*(N)+4,
16e^{2\Delta_*(N)}
\right\},
\]

and

\[
C(N)=
\frac{32768e^{4\Delta_*(N)}}\eta.
\]

Finally define

\[
q(N)
=
\min\left\{
\frac\eta{128\log(2T(N))},
\frac{T(N)}{C(N)N^{1+\rho}}
\right\}.
\]

### Theorem PX453 -- PROVED

For a supplied effective witness, the following are finite decidable
inequalities in `N`:

\[
\boxed{q(N)T(N)\ge B(N),}
\]

\[
\boxed{N-1-2\Delta_*(N)>0,}
\]

and

\[
\boxed{
8\cdot512A_3e^{2\Delta_*(N)}
\bigl(q(N)\log(2T(N))+q(N)^2\log(2T(N))\bigr)
\le\frac18.
}
\]

If they hold for every `N>=N_0`, then `N_0` is a common paired spread,
divisor, internal-rank-three, and terminal-transposition cutoff for
PX445--PX449.

### Proof

The first inequality supplies every minimum retained-order and forbidden-degree
condition.  The second supplies an allowed partner for atomic terminal label
transpositions.  The third is the factor-eight version of PX333 with a fixed
`1/8` internal margin.  PX445 separately gives the paired support-four margin.
All expressions are explicit once the witness data are supplied. \(\square\)

## 4. Existence versus effectivity

### Theorem PX454 -- PROVED REDUCTION

For every fixed `epsilon>0`, an abstract finite cutoff exists from the currently
used asymptotic inputs:

- `mathfrak d(N)=N^(o(1))`;
- `d_*(N)=O(log log N)`;
- fixed absolute `A_3`.

But the repository does not yet contain enough numerical data to output a
certified integer `N_0`.

### Proof

Choose `rho<2epsilon`.  The divisor term contributes `N^rho`, while
`T(N)^2/N=N^(2epsilon)`.  Since `Delta_*(N)=O(log log N)`, both
`e^(4Delta_*)` and `B(N)` are polylogarithmic powers of `N`.  Thus the first
cutoff inequality eventually holds.  The terminal inequality is immediate.
The third inequality tends to zero because `q log T` does.

Effectivity fails only because `A_3`, the divisor threshold `N_div`, and the
constant in `d_*` are not instantiated. \(\square\)

This distinction prevents an asymptotic `o(1)` statement from being silently
converted into a finite census claim.

## 5. Exact remaining cutoff frontier

### Corollary PX455 -- PROVED REDUCTION

A certified common cutoff requires exactly the following next results.

1. **Explicit Cartesian incidence constant.**  Prove the PX189/PX333 estimate
   with a recorded rational `A_3`, using an explicit Szemeredi--Trotter or
   Cartesian-product incidence theorem.
2. **Effective divisor witness.**  Record an explicit pair `(rho,N_div)` with
   `rho<2epsilon`.
3. **Exact depth envelope.**  Replace the `O(1)` in PX265 by a verified formula
   `d_*(N)`.
4. **Cutoff search.**  Evaluate PX453 and output the first certified `N_0` or a
   conservative larger value.
5. **Finite range.**  Audit every base order below `N_0`, or construct a chain
   that enters the asymptotic range without requiring individual enumeration.

No additional geometric obstruction class is presently needed for the
asymptotic branch.

## 6. Verification

Run

```bash
python scripts/verify_product_entry_invariant_dependencies.py
```

The verifier reads the JSON manifest and theorem documents, checks DAG
acyclicity, theorem-ID uniqueness, safety tags, required constants, absence of
obsolete premises, and the arithmetic of the parameterized cutoff predicate.
