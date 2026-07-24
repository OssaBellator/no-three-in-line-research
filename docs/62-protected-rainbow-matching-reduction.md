# Protected permutations as simultaneous rainbow matchings

PX95 shows that affine coset states stop gaining entropy after rank two.  This
chapter gives an exact reformulation of the required nonlinear local state space
as two sequential simultaneous-rainbow perfect-matching problems.

The reduction identifies the precise external theorem needed for a protected
rank-three spread distribution.

Work in one prime-order additive coset, identified with `F_ell`.  Assume every
protected primitive direction

\[
q=(a,b)
\]

has `a,b` nonzero modulo `ell`, and let `m` be nonzero modulo `ell`.

For every direction define an edge-colouring of the complete bipartite graph
with left vertex `x` and right vertex `y` by

\[
\chi_q(x,y)=bx-amy\pmod\ell.
\]

Because `b` and `am` are nonzero, every `chi_q` is a proper `ell`-edge-colouring:
each colour occurs exactly once at every left and right vertex.

## Theorem PX96 -- PROVED

A pair of permutations `(P,Phi)` protects all directions in `D` inside one
coset if and only if it can be chosen by the following two-stage rainbow
procedure.

1. The graph

   \[
   M_\Phi=\{(x,\Phi(x)):x\in\mathbb F_\ell\}
   \]

   is a perfect matching which is rainbow simultaneously in every colouring
   `chi_q`.
2. After fixing `Phi`, colour an edge `(x,w)` by

   \[
   \psi_q^\Phi(x,w)=bw-am\Phi(x).
   \]

   The graph of `P` is a perfect matching which is rainbow simultaneously in
   every colouring `psi_q^Phi`.

Every colouring in the second stage is also proper.

### Proof

The colours on the graph of `Phi` are

\[
\chi_q(x,\Phi(x))=bx-am\Phi(x).
\]

They are all distinct exactly when the top protected line-coordinate map is a
permutation.  This is the first local injectivity requirement in PX92, without
restricting `Phi` to be affine.

After fixing `Phi`, the colours on the graph of `P` are

\[
\psi_q^\Phi(x,P(x))=bP(x)-am\Phi(x).
\]

They are all distinct exactly when the bottom protected line-coordinate map is
a permutation.  This is the second PX92 requirement.

For fixed `x`, the map `w -> bw-amPhi(x)` is bijective because `b` is nonzero.
For fixed `w`, the map `x -> bw-amPhi(x)` is bijective because `Phi` is a
permutation and `am` is nonzero.  Hence every second-stage colouring is proper.
\(\square\)

Thus the protected local state problem is a pair of common-rainbow perfect
matchings in a fixed number of proper one-factorizations of `K_(ell,ell)`.

## Theorem PX97 -- PROVED CONDITIONALLY

Fix a constant `K`.  Suppose that for every protected direction set `D` and all
sufficiently large prime `ell`, the following distributions exist.

1. A distribution on perfect matchings simultaneously rainbow in every
   `chi_q`, such that for `1<=k<=3`, every prescribed `k`-edge matching cylinder
   has probability at most

   \[
   \frac K{(\ell)_k}.
   \]
2. For every first-stage matching `Phi`, a conditional distribution on perfect
   matchings simultaneously rainbow in every `psi_q^Phi`, with the same uniform
   cylinder bound.

Then there is a protected distribution on pairs `(P,Phi)` satisfying, for every
`k<=3` and every prescribed joint row/column image cylinder,

\[
\boxed{
\Pr\bigl(
\Phi(x_i)=y_i,
P(x_i)=w_i
\text{ for }i\in[k]
\bigr)
\le
\frac{K^2}{(\ell)_k^2}.
}
\]

Independent use in additive cosets gives a factor-compatible protected
rank-three spread distribution for the rectangle product family.

### Proof

Expose `Phi` first.  The first cylinder has probability at most `K/(ell)_k`.
Conditioned on every value of `Phi`, the prescribed `P` cylinder has probability
at most `K/(ell)_k`.  Multiply the two bounds and average over the first-stage
matching.  PX96 supplies protection, and independence across cosets multiplies
cylinder probabilities.  PX41 supplies factor transport. \(\square\)

The conditional statement isolates the missing theorem; it does not assert that
such distributions are currently available.

## 3. Relation to queens and rainbow matching theory

For the two diagonal directions, the first stage is the toroidal queens
condition: rows, columns, and both diagonal residues are all distinct.  More
general direction sets give simultaneous rainbow constraints from several
linear Latin-square colourings.

Known rainbow-matching and `n`-queens results establish existence, completion,
and asymptotic abundance in related settings.  They do not directly provide the
uniform simultaneous multi-colour rank-three cylinder bound assumed in PX97.
The needed result is therefore a spread refinement, not merely another
existence theorem.

## 4. Exact order-five census

For

\[
ell=5,
\qquad
m=2,
\qquad
D=\{(1,1),(1,-1)\},
\]

there are exactly ten first-stage common-rainbow permutations.  Across those
permutations there are exactly one hundred protected ordered pairs `(P,Phi)`.
They coincide in number with the 100 affine local states of PX92.

Thus the first protected example has no hidden nonlinear entropy; the rank-two
barrier is genuine at order five.  Larger prime orders are the first place where
a nonlinear spread theorem can add new states.

## 5. Revised general-proof target

PX97 turns the protected-spread problem into a precise rainbow-matching
statement:

> prove a rank-three spread distribution on perfect matchings simultaneously
> rainbow in a fixed number of proper linear edge-colourings of a complete
> bipartite graph, uniformly after conditioning on the first protected matching.

Possible routes include switching arguments, entropy plus completion, a
conflict-free matching process with absorption, or a direct spread refinement
of toroidal-queens constructions.

Once the cylinder bound is available, PX82 supplies the high-direction conflict
codegree saving and PX90 supplies a local-load endpoint.

## 6. Verification

Run

```bash
python scripts/verify_product_protected_rainbow_reduction.py
```

The verifier exhausts all permutation pairs at order five, checks the exact
rainbow/protection equivalence, reproduces the counts ten and one hundred, and
checks the proper-colouring identities at orders five and seven.