# PFR coset absorbers and alternating anchor propagation

This chapter continues [`17-pfr-inverse-additive.md`](17-pfr-inverse-additive.md). The earlier chapter proves quotient-set and energy inverse theorems and extracts common-ratio rectangle banks. Here the structured output is converted into a larger subgroup-coset state space and then propagated to the opposite-colour anchor set.

Throughout,

\[
X=\{x_0,\ldots,x_{k-1}\}\subseteq\mathbb F_p^*
\]

is the parameter set of one carry-filtered Möbius cycle.

## 1. Density refinement below quotient doubling two

Put

\[
\kappa=\frac{|X/X|}{|X|}<2,
\]

let

\[
H=\operatorname{Stab}(X/X),
\]

and let `m` be the number of `H`-cosets met by `X`.

### Theorem I5 — PROVED

\[
\boxed{m\le\frac1{2-\kappa}.}
\]

Writing

\[
\alpha=\frac{|X|}{m|H|},
\]

one also has

\[
\boxed{\alpha\ge\frac{2m-1}{\kappa m}.}
\]

### Proof

Kneser's theorem applied to `XX^{-1}` gives

\[
|X/X|\ge |XH|+|X^{-1}H|-|H|=(2m-1)|H|.
\]

Since

\[
|X/X|=\kappa|X|\le\kappa m|H|,
\]

we obtain `(2-kappa)m<=1`. The density inequality follows from

\[
(2m-1)|H|\le\kappa|X|.
\]

`square`

### Consequences

1. If `kappa<3/2`, then `m=1`; the set lies in one multiplicative subgroup coset.
2. In that case `|X|>|H|/2`, hence
   \[
   X/X=H.
   \]
3. If `kappa=1`, then `X` is a full subgroup coset.
4. If `kappa=3/2` and `m=2`, then `alpha=1`; thus `X` is exactly a union of two full `H`-cosets.
5. If `kappa<2-1/(r+1)`, then `X` meets at most `r` subgroup cosets.

The second assertion follows because two subsets of one `H`-coset, each of size greater than `|H|/2`, must intersect after every translation by `H`.

## 2. Exact classification of the frozen p=11 cycle

For the frozen cycle

\[
p=11,
\qquad X=\{4,5,7,6\},
\]

one computes

\[
X/X=\{1,3,4,7,8,10\},
\qquad \kappa=\frac32.
\]

Its stabilizer is

\[
H=\{1,10\}=\{\pm1\},
\]

and Theorem I5 is sharp:

\[
\boxed{X=4H\cup5H.}
\]

The window supports are

\[
(q_0,q_1,q_2,q_3)=(1,2,1,2).
\]

Thus the first frozen cycle is not a pseudorandom exception. It is the extremal two-coset case of Kneser's inequality.

## 3. Full coset-union absorber bank

Let `H<=F_p^*` have order `h`, and suppose

\[
X=\bigcup_{\alpha=1}^m u_\alpha H
\]

is a disjoint union of full cosets. The row set used by the hyperbola layer `H_a` on these columns is

\[
aX^{-1}=\bigcup_{\beta=1}^m au_\beta^{-1}H.
\]

For `sigma in S_m` and `t=(t_1,...,t_m) in H^m`, define

\[
M_{\sigma,t}
=
\bigcup_{\alpha=1}^m
\left\{
\left(u_\alpha h,
\frac{a}{u_{\sigma(\alpha)}t_\alpha h}
\right):h\in H
\right\}.
\]

### Theorem I6 — PROVED

Every `M_{sigma,t}` is a perfect matching between the columns `X` and the rows `aX^{-1}`. The family has

\[
\boxed{m!h^m}
\]

states, contains the current hyperbola state, and each state is contained in a union of at most `m` modular hyperbolas.

Consequently every real line meets a state in at most

\[
\boxed{2m}
\]

points.

### Proof

For fixed `alpha`, multiplication by `t_alpha` permutes `H`, so the displayed orbit matches `u_alpha H` bijectively to `au_{sigma(alpha)}^{-1}H`. The quotient permutation `sigma` uses every row coset once.

Within that orbit,

\[
xy=\frac{au_\alpha}{u_{\sigma(\alpha)}t_\alpha}
\]

is constant. Hence it lies on one modular hyperbola, and a real line meets it at most twice. `square`

### Uniform orbit-bank probabilities

Choose `sigma` uniformly and the `t_alpha` independently and uniformly in `H`. Every individual block cell is selected with probability

\[
\frac1{mh}=\frac1{|X|}.
\]

For prescribed compatible cells lying in `r` distinct source cosets and `r` distinct target cosets, with consistent orbit shifts,

\[
\Pr(\text{all selected})
=
\frac1{(m)_r h^r}.
\]

Cells belonging to the same orbit state are intentionally correlated. This is the block structure that a later conflict theorem must use rather than treating the cells as independent.

## 4. Möbius anchor compression

Consider a red-red-blue real collinearity

\[
R_x=(x,a/x),
\qquad R_u=(u,a/u),
\qquad B_z=(z,b/z),
\]

and set

\[
r=b/a,
\qquad g=u/x,
\qquad c=z/x.
\]

Real collinearity implies the modular identity

\[
r xu=z(x+u-z).
\]

After division by `x^2`,

\[
\boxed{c^2-(1+g)c+rg=0.}
\]

### Theorem I7 — PROVED

Let

\[
R=\{x_{i+1}/x_i:i\in\mathbb Z_k\},
\qquad |R|=L,
\]

and let `Z` be the set of chosen opposite-colour anchors labelling the cycle edges. Then there is a set `C` with

\[
|C|\le2L
\]

such that

\[
\boxed{Z\subseteq CX.}
\]

Consequently,

\[
\boxed{|Z/Z|\le4L^2|X/X|.}
\]

### Proof

For each fixed `g`, the displayed monic quadratic has at most two possible values of `c`. Therefore the normalized ratios `z_i/x_i` use at most `2L` values. Finally,

\[
Z/Z\subseteq(C/C)(X/X),
\]

and `|C/C|<=|C|^2`. `square`

## 5. Alternating inverse-propagation dichotomy

### Theorem I8 — PROVED

Assume

\[
|X/X|\le K|X|,
\qquad |R|\le L,
\]

and fix `0<eta<=1`. Then one of the following holds.

1. **Anchor concentration:**
   \[
   |Z|<\eta|X|,
   \]
   and some opposite-colour anchor labels more than `1/eta` cycle edges.
2. **Structure propagation:**
   \[
   |Z|\ge\eta|X|
   \]
   and
   \[
   \boxed{
   |Z/Z|\le\frac{4L^2K}{\eta}|Z|.
   }
   \]
   Therefore `Z` is controlled by a multiplicative coset progression with parameters depending only on `K,L,eta`.

### Proof

The first alternative is the pigeonhole principle. In the second, Theorem I7 gives

\[
|Z/Z|\le4L^2K|X|\le\frac{4L^2K}{\eta}|Z|.
\]

Apply the Green--Ruzsa inverse theorem in the cyclic logarithm group. `square`

This is the first exact inverse statement that propagates across the alternating red/blue closure:

\[
\boxed{
\text{low-complexity cycle}
\Longrightarrow
\text{high-load anchor or low-complexity opposite colour}.
}
\]

## 6. What the inverse theorem does and does not solve

The inverse theory now compresses a frozen obstruction into one of two forms:

- a bounded quotient/coset system supporting the explicit bank in Theorem I6;
- a small family of high-load opposite-colour anchors.

It does not by itself prove that the structured core is repairable. The frozen `p=11` example already has quotient doubling `3/2` and is a full union of two subgroup cosets, yet no one-colour cycle-block permutation improves its triple potential.

Thus PFR is a classification engine, not the decoder.

## 7. Rational-expander target

The normalized Möbius transition is

\[
F_r(c)=\frac{c(1-c)}{r-c}.
\]

A persistently low-complexity alternating core would require both `C` and `F_r(C)` to have small multiplicative doubling.

### Target I9 — OPEN

For fixed `r notin {0,1}`, classify finite sets

\[
C\subseteq\mathbb F_p\setminus\{0,r\}
\]

for which both

\[
|C/C|\le K|C|
\]

and

\[
|F_r(C)/F_r(C)|\le K|F_r(C)|.
\]

The desired conclusion is that `C` is bounded in size or lies in one of finitely many explicitly describable exceptional Möbius orbits.

Finite-field sum-product estimates for rational functions suggest expansion outside special algebraic forms, but the precise simultaneous multiplicative-doubling statement above remains open in this notebook.

## External inputs

- Green and Ruzsa, *Freiman's theorem in an arbitrary abelian group*.
- Bukh and Tsimerman, *Sum-product estimates for rational functions*.
