# Unrestricted one-layer obstruction at base sides six and seven

PX37 refutes the complete **affine** one-inner-layer family at base sides six
and seven.  PX43--PX44 make it possible to test the full arbitrary-permutation
family exactly: every normalized PX28 state is a perfect matching of rectangles,
and every bad triple is an explicit diagonal or transversal conflict.

The result is negative.  Even completely arbitrary blockwise permutations do
not produce a PX28 template at either base side.

## 1. Transpose equivalence of crossed orientations

Use the rectangle normal form

\[
Q_\theta(p,t,r).
\]

### Lemma PX47 -- PROVED

Template existence in orientation `cf` is equivalent to template existence in
orientation `fc`.

More explicitly, the scalar transpose of

\[
Q_{cf}(p,t,r)
\]

is

\[
Q_{fc}
\left(
 r\circ t^{-1},
 t^{-1},
 p\circ t^{-1}
\right).
\]

### Proof

In the `cf` orientation, the four rectangle coordinates indexed by `u` use

\[
x_0=u,
\qquad
x_1=n+p(u),
\]

and

\[
y_0=2t(u),
\qquad
y_1=2r(u)+1.
\]

After transposition reindex by `u'=t(u)`.  In the `fc` normal form the new first
row coordinate is `2u'`.  The second row coordinate is obtained from

\[
p'(u')=r(u),
\]

so `p'=r t^{-1}`.  The first column digit satisfies

\[
t'(u')=u,
\]

so `t'=t^{-1}`.  Finally

\[
r'(u')=p(u),
\]

so `r'=p t^{-1}`.  Transposition preserves real collinearity. \(\square\)

The same calculation maps `cc` to `cc` and `ff` to `ff`.

## 2. Exact conflict-aware search

For one side and orientation, construct all

\[
n^4
\]

candidate rectangle edges

\[
(u,p_0,t_0,r_0).
\]

The verifier uses the following exact data.

1. For every edge, a bitset of all compatible edges forming a diagonal conflict.
2. For every compatible selected pair, a cached bitset of all compatible edges
   whose rectangle has a corner on a line through one corner of each selected
   rectangle.  By PX44 this is exactly the transversal-completion set.
3. Four matching-coordinate masks enforcing that `u,p,t,r` are each used once.

A depth-first search chooses the uncovered `u` with the fewest currently legal
edges.  A branch is discarded only when it violates one matching constraint,
one PX44 diagonal conflict, or one PX44 transversal conflict.  Thus exhausting
the search tree is an exact infeasibility certificate for the rectangle
perfect-matching instance.

## Theorem PX48 -- PROVED FINITE

The unrestricted arbitrary-block PX28 family has no no-three normalized
template at base side six or base side seven, in any global orientation.

The complete search-node counts are:

| Base side | Orientation | Search nodes |
|---:|---|---:|
| 6 | `cc` | 236,651 |
| 6 | `cf` | 251,708 |
| 6 | `fc` | 260,521 |
| 6 | `ff` | 204,824 |
| 7 | `cc` | 3,185,100 |
| 7 | `cf` | 3,561,372 |
| 7 | `ff` | 2,761,350 |

At side seven, `fc` infeasibility follows from `cf` by PX47.

### Proof

Run the exact rectangle-matching search described above.  Every branch ends
before selecting `n` compatible conflict-free edges in each displayed case.
The search covers all triples of permutations `p,t,r`, and PX43 covers every
normalized arbitrary-block PX28 state.  PX39 then covers all unnormalized
four-block states.  PX47 supplies the remaining side-seven crossed orientation.
\(\square\)

## 3. Consequences

### Corollary PX48a -- PROVED FINITE

No saturated side-six or side-seven factor can be doubled by the PX28
one-inner-layer construction, even if all four block maps are arbitrary
permutations.

This is stronger than PX37, which only excludes affine maps.

The complete unrestricted one-layer template picture is now:

| Base side | Template existence |
|---:|---|
| 2 | yes |
| 3 | no |
| 4 | yes |
| 5 | yes |
| 6 | no |
| 7 | no |
| 8 | open |

Consequently the special closures

\[
2\times4\to8,
\qquad
2\times5\to10
\]

cannot be extended to an infinite doubling family merely by asserting that a
one-layer template exists at every side.  The next decisive finite target is
base side eight: a template there would allow the side-four closure to iterate
to side sixteen, while an exact obstruction would rule out that recursive
route inside PX28.

Other remaining routes are the full degree-two selector, two-inner-layer
explicit templates, larger outer factors, or a conflict-free matching theorem
using additional structure beyond the worst-case rectangle degrees PX45--PX46.

## Verification

Run

```bash
python scripts/verify_product_unrestricted_six_seven.py --side 6
python scripts/verify_product_unrestricted_six_seven.py --side 7
```

The side-six command checks all four orientations.  The side-seven command
checks `cc`, `cf`, and `ff`; `fc` follows from PX47.  The verifier uses only the
standard library.  The side-seven search is intentionally longer than the
small census scripts.
