# Direct one-label insertion does not reach side seven

PX56--PX60 give three explicit side-six full-selector hosts, covering the
relative classes `(6)`, `(4,2)`, and `(3,3)`.  A natural structural bridge would
insert one new label into a relative cycle and extend the three normal-form
permutations `T,P,Q` by one label.  This chapter exhausts that complete local
neighbourhood.

The result is negative: none of the inherited one-label extensions contains a
spanning no-three selector.  Therefore a side-seven theorem cannot be obtained
by merely inserting one label into the recorded side-six hosts.

## 1. Permutation insertion family

Let `sigma` be a permutation of `[6]`.  Its seven elementary extensions to
`[7]` are:

1. the fixed extension `sigma^+` with `sigma^+(6)=6`;
2. for each source `a in [6]`, the arrow insertion
   
   \[
   a\to6\to\sigma(a),
   \]
   
   leaving every other arrow unchanged.

### Lemma PX496 -- PROVED

These are exactly the permutations on `[7]` obtained from `sigma` by deleting
source label six and target label six and recovering `sigma` without relabelling
the other six symbols.

### Proof

If the new source maps to the new target, deletion gives the fixed extension.
Otherwise exactly one old source maps to target six, while source six maps to
that source's former target.  This is the displayed arrow insertion. \(\square\)

The same insertion operation is applied independently to `T`, `P`, and `Q`.
For the relative permutation `H`, insert label six into one arrow of the cycle
whose length is to increase.

## 2. Inherited host census

For each extended quadruple `(T,P,Q,H)` and each of the four radix orientations,
construct the complete side-two outer host.  The selector search exposes the
fourteen scalar rows.  Each row chooses two of its four host cells.  Column
degree feasibility and exact integer collinearity tests prune the search, but
all spanning degree-two states are exhausted.

### Theorem PX497 -- PROVED FINITE

No inherited one-label extension of any recorded side-six canonical host has a
spanning no-three selector.

The exact census is:

| Side-seven target class | Side-six source class | `H` insertions | Host count | Selector nodes | Feasible hosts |
|---|---|---:|---:|---:|---:|
| `(7)` | `(6)` | 6 | 8,232 | 34,170,644 | 0 |
| `(5,2)` | `(4,2)` | 4 | 5,488 | 13,077,659 | 0 |
| `(4,3)` | `(3,3)` | 6 | 8,232 | 34,754,272 | 0 |

The host counts are

\[
6\cdot7^3\cdot4=8232,
\qquad
4\cdot7^3\cdot4=5488,
\qquad
6\cdot7^3\cdot4=8232.
\]

In total,

\[
\boxed{21,952}
\]

inherited hosts and

\[
\boxed{82,002,575}
\]

selector-search nodes are rejected exactly.

## 3. The missing `(3,2,2)` predecessor

The side-seven census PX493 contains the additional class `(3,2,2)`.  Its
obvious one-label predecessor is `(2,2,2)`, but that relative class does not
occur among saturated side-six factors and therefore was absent from PX56.

Let

\[
H_{2,2,2}=(0\ 1)(2\ 3)(4\ 5).
\]

Use the affine permutation group

\[
A_6=\{u\mapsto au+b\pmod6:a\in\{1,5\},\ b\in\mathbb Z/6\mathbb Z\}.
\]

### Theorem PX498 -- PROVED FINITE/REDUCTION

None of the

\[
4|A_6|^3=4\cdot12^3=6912
\]

affine full-selector hosts for `H_(2,2,2)` contains a spanning no-three state.
The exact search visits 14,345,445 selector nodes.

Consequently a recursive side-seven proof must do at least one of the following:

1. use a host outside the elementary one-label extension neighbourhood for one
   of `(7)`, `(5,2)`, or `(4,3)`;
2. use non-affine normal-form permutations for the auxiliary `(2,2,2)` class;
3. bypass cycle insertion entirely with a global full-selector or repair
   theorem.

This is an obstruction to one specific recursion mechanism, not a proof that
universal `2 x 7 -> 14` closure fails.

## Verification

Compile the exact verifier and run its cases independently:

```bash
g++ -O3 -std=c++17 scripts/verify_product_side_seven_insertion_barrier.cpp -o /tmp/side7_barrier
/tmp/side7_barrier cycle7
/tmp/side7_barrier cycle52
/tmp/side7_barrier cycle43
/tmp/side7_barrier affine222
```

Each case checks its recorded host count, search-node count, column-degree
completion, and every determinant using integer arithmetic.