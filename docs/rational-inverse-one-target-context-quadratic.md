# Exact one-target context-line quadratic

**Branch:** `research/rational-inverse-expansion`

RI5bh--RI5bl close the two-target terminal geometry by fixing its secant. This note closes the purely geometric ambiguity in the complementary one-target geometry. A fixed context pair determines one projective affine line, and its possible target-hyperbola cells are exactly the nonzero roots of one quadratic. Hence there are at most two physical target lifts and fixed-line recurrence has period at most two.

This is a geometric classification only. It does not pay the selected target occurrence, prove owner coherence or invoke the fixed-edge bank.

## Prime-field target hyperbola

Fix an odd prime `p` and `a in F_p^*`. The target hyperbola is

\[
 H_a=\{(x,a/x):x\in\mathbb F_p^*\}.
\]

Let two distinct context cells determine the affine line

\[
 \ell: AX+BY=C,
\]

where `(A,B)` is not `(0,0)` and the coefficient triple is normalized projectively by the branch's fixed least-scalar convention.

A target point `(x,a/x)` lies on `ell` exactly when

\[
 \boxed{A x^2-Cx+Ba=0.}
\]

## RI5bm -- exact context-line intersection equation -- PROVED

The map

\[
 x\longmapsto(x,a/x)
\]

is a bijection between the nonzero roots of

\[
 q_\ell(X)=AX^2-CX+Ba
\]

and the target-hyperbola points on `ell`.

### Proof

Substitute `Y=a/X` into `AX+BY=C` and multiply by the nonzero coordinate `X`. This gives the displayed quadratic. Reversing the calculation proves that every nonzero root gives a point of `H_a cap ell`. QED.

## RI5bn -- at most two exact target candidates -- PROVED

Every fixed context line contains at most two target-hyperbola cells. More precisely:

1. if `A!=0`, the candidates are the roots of the normalized quadratic

   \[
   X^2-sX+r,
   \qquad
   s=C/A,
   \qquad
   r=Ba/A;
   \]

2. if `A=0`, the equation is linear or inconsistent and therefore has at most one nonzero root.

### Proof

A nonzero quadratic over a field has at most two roots. When `A=0`, the polynomial has degree at most one. The impossible zero polynomial cannot occur because `A=B=0` is excluded and `a!=0`. QED.

## RI5bo -- exact two-root address -- PROVED

When `A!=0` and the line has two distinct target roots `x,y`, they satisfy

\[
 \boxed{x+y=s,\qquad xy=r.}
\]

Conversely the normalized line data `(a,s,r)` determine the unordered root pair `{x,y}` uniquely. The only ordered lifts are `(x,y)` and `(y,x)`.

### Proof

Vieta's formulas give the sum and product. The unordered pair is the root multiset of the monic polynomial `X^2-sX+r`, hence is unique. Distinct roots have exactly two orderings. QED.

The discriminant

\[
 \Delta=s^2-4r
\]

classifies the zero-, one- and two-candidate cases in the usual way, but no choice of square root is retained as an independent terminal-state field.

## RI5bp -- fixed-context recurrence has period at most two -- PROVED

Fix the physical context pair, projective line address, target hyperbola parameter `a`, finite terminal word and all owner/completion/blocker fields. Any recurrent change of the selected target occurrence is either:

1. a stutter at one root;
2. a transposition between the two roots of `q_ell`, with exact period two;
3. or a change of context pair, line, field, owner, completion, blocker, legality or physical occurrence interpretation, giving an explicit reset.

### Proof

RI5bn leaves at most two target candidates. A deterministic recurrence on a one- or two-element exact candidate set is a stutter or a two-cycle unless another retained field changes. QED.

## RI5bq -- updated RI6 geometric frontier -- PROVED AS A REDUCTION

Both terminal active geometries now have exact finite physical lifts:

- two-target classes have one unordered secant pair and at most the swap orientation;
- one-target classes have one context-line quadratic and at most two target roots.

The remaining RI6 work is arithmetic and payment specific: pay or absorb the selected exact root/secant occurrence, establish owner and scale coherence, close the blocker profiles and verify the final bank-ready collateral inequality.

## Finite check

`scripts/verify_ri_one_target_context_quadratic.py` enumerates normalized projective lines over small odd prime fields, compares direct line--hyperbola intersections with the quadratic roots, and checks the exact zero/one/two-root classification and Vieta reconstruction.