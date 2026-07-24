# PFR and inverse additive theory for multiplicative cycle cores

This chapter converts low window-product complexity and high multiplicative energy into explicit algebraic structure. It also shows how that structure propagates to the opposite-colour anchor set.

Throughout, `p` is prime and

\[
X=\{x_0,\ldots,x_{k-1}\}\subseteq \mathbb F_p^*
\]

is the distinct parameter set of a carry-filtered Möbius cycle, indexed cyclically by `i in Z_k`.

For `s in Z_k`, define

\[
W_s=\left\{\frac{x_{i+s}}{x_i}:i\in\mathbb Z_k\right\},
\qquad q_s=|W_s|,
\]

and

\[
\overline q=\frac1k\sum_{s\in\mathbb Z_k}q_s.
\]

## 1. Window quotient identity

### Theorem PF1 — PROVED

\[
\boxed{X/X=\bigcup_{s\in\mathbb Z_k}W_s.}
\]

Consequently,

\[
\boxed{|X/X|\le \sum_s q_s=k\overline q.}
\]

### Proof

Every ordered quotient `x_j/x_i` occurs in `W_s` for the unique cyclic difference `s=j-i`. The converse inclusion is immediate. `square`

Thus low average window complexity is exactly a small multiplicative-doubling hypothesis.

## 2. Window collision energy

For `g in F_p^*`, let

\[
r_s(g)=|\{i:x_{i+s}/x_i=g\}|,
\]

and let

\[
r(g)=|\{(i,j):x_j/x_i=g\}|=\sum_s r_s(g).
\]

The multiplicative energy is

\[
E^\times(X)=\sum_g r(g)^2.
\]

### Theorem PF2 — PROVED

\[
\boxed{
E^\times(X)
\ge k^2\sum_s\frac1{q_s}
\ge \frac{k^3}{\overline q}.
}
\]

### Proof

For each `s`, Cauchy--Schwarz gives

\[
\sum_g r_s(g)^2\ge \frac{k^2}{q_s}.
\]

Since all `r_s(g)` are nonnegative,

\[
r(g)^2\ge\sum_s r_s(g)^2.
\]

Sum first over `g`, then over `s`. Finally use

\[
\sum_s\frac1{q_s}\ge\frac{k^2}{\sum_s q_s}=\frac{k}{\overline q}.
\]

`square`

## 3. General Freiman--Ruzsa compression

Fix a generator `omega` of `F_p^*` and write

\[
A=\{\log_\omega x:x\in X\}\subseteq \mathbb Z/(p-1)\mathbb Z.
\]

Then

\[
|A-A|=|X/X|.
\]

A multiplicative coset progression is a set of the form

\[
P=x_0H\left\{g_1^{n_1}\cdots g_r^{n_r}:|n_j|\le L_j\right\},
\]

where `H <= F_p^*` is a subgroup.

### Theorem PF3 — PROVED FROM GREEN--RUZSA

For every `K>=1`, there exist functions `r(K)` and `C(K)` such that if

\[
|X/X|\le K|X|,
\]

then `X` is contained in a multiplicative coset progression `P` satisfying

\[
\operatorname{rank}(P)\le r(K),
\qquad
|P|\le C(K)|X|.
\]

In particular, if `overline q <= K`, then the same conclusion holds with parameter `K`.

### Justification

Standard Ruzsa sum--difference inequalities convert small difference into small doubling in the cyclic additive group. The Green--Ruzsa Freiman theorem in arbitrary abelian groups then contains `A` in an additive coset progression of rank and relative size depending only on `K`. Exponentiation by `omega` gives the displayed multiplicative progression.

The recent polynomial Freiman--Ruzsa theorem for bounded-torsion groups does not directly give polynomial constants here, because the exponent of `F_p^*` is `p-1` and is not bounded independently of `p`.

## 4. Energy inverse theorem

Low quotient support is sufficient but not necessary for structure. Energy gives a more robust hypothesis.

### Theorem PF4 — PROVED FROM BSG AND GREEN--RUZSA

Suppose

\[
E^\times(X)\ge \frac{|X|^3}{K}.
\]

Then there is `X' subseteq X` with

\[
|X'|\ge cK^{-1/2}|X|
\]

and

\[
|X'/X'|\le CK^4|X'|,
\]

for absolute constants `c,C`. Consequently `X'` is contained in a multiplicative coset progression whose rank and relative size depend only on `K`.

### Justification

Apply the quantitative Balog--Szemeredi--Gowers theorem to the logarithmic image of `X`, then apply PF3.

Combining with PF2, bounded average window complexity yields a large progression-controlled subcycle vertex set even if one does not use the direct quotient identity.

## 5. Explicit structure below doubling two

The general Freiman theorem is qualitative. Below doubling two, Kneser's theorem gives an explicit classification.

Put

\[
\kappa=\frac{|X/X|}{|X|}<2,
\]

and let

\[
H=\operatorname{Stab}(X/X)
=\{h\in\mathbb F_p^*:h(X/X)=X/X\}.
\]

Let `m` be the number of `H`-cosets met by `X`, so

\[
|XH|=m|H|.
\]

### Theorem PF5 — PROVED

\[
\boxed{m\le \frac1{2-\kappa}.}
\]

Moreover, writing

\[
\alpha=\frac{|X|}{m|H|},
\]

we have

\[
\boxed{
\alpha\ge\frac{2m-1}{\kappa m}.
}
\]

### Proof

Kneser's theorem applied to `XX^{-1}` gives

\[
|X/X|\ge |XH|+|X^{-1}H|-|H|=(2m-1)|H|.
\]

On the other hand,

\[
|X/X|=\kappa|X|\le\kappa m|H|.
\]

Thus

\[
(2-\kappa)m\le1.
\]

The density estimate follows from

\[
(2m-1)|H|\le\kappa|X|.
\]

`square`

### Consequences

1. If `kappa<3/2`, then `m=1`: `X` lies in one subgroup coset.
2. In this case `|X|>|H|/2`, so
   \[
   X/X=H.
   \]
3. If `kappa=1`, then `X` is a full subgroup coset.
4. If `kappa=3/2` and `m=2`, then `alpha=1`, so `X` is exactly a union of two full `H`-cosets.
5. More generally, if `kappa<2-1/(r+1)`, then `X` meets at most `r` subgroup cosets.

The same statements hold with `overline q` in place of `kappa`, since `kappa<=overline q`.

## 6. Frozen p=11 cycle classification

For the frozen cycle

\[
p=11,
\qquad X=\{4,5,7,6\},
\]

one has

\[
X/X=\{1,3,4,7,8,10\},
\qquad \kappa=\frac64=\frac32.
\]

Its stabilizer is

\[
H=\{1,-1\}=\{1,10\},
\]

and

\[
\boxed{X=4H\cup5H.}
\]

Thus the smallest known frozen cycle is not pseudorandom: it is the extremal two-coset case of PF5.

Its window supports are

\[
(q_0,q_1,q_2,q_3)=(1,2,1,2).
\]

## 7. Coset-union absorber bank

The explicit small-doubling classification can be converted into executable row--column trades.

Let `H <= F_p^*` have order `h`, and suppose

\[
X=\bigcup_{\alpha=1}^m u_\alpha H
\]

is a disjoint union of full cosets. The associated row set in the hyperbola layer `H_a` is

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

### Theorem PF6 — PROVED

Each `M_{sigma,t}` is a perfect matching between the columns `X` and rows `aX^{-1}`. The bank contains

\[
\boxed{m!h^m}
\]

states, includes the current hyperbola state, and every state is contained in a union of at most `m` modular hyperbolas.

Consequently every real line meets a state in at most

\[
\boxed{2m}
\]

points.

### Proof

For fixed `alpha`, multiplication by `t_alpha` permutes `H`; hence the displayed set matches `u_alpha H` bijectively to `au_{sigma(alpha)}^{-1}H`. Since `sigma` permutes the quotient cosets, all rows and columns are used exactly once.

Within the `alpha`-th orbit block,

\[
xy=\frac{au_\alpha}{u_{\sigma(\alpha)}t_\alpha}
\]

is constant, so the block state lies on one modular hyperbola. A real line intersects each modular hyperbola in at most two points. `square`

PF6 turns a PFR conclusion into an installed absorber family whenever the controlling progression has rank zero and the occupied cosets are full.

## 8. Möbius anchor compression

Consider a red-red-blue real collinearity with

\[
R_x=(x,a/x),
\qquad R_u=(u,a/u),
\qquad B_z=(z,b/z),
\]

and put

\[
r=b/a,
\qquad g=u/x,
\qquad c=z/x.
\]

Reduction modulo `p` gives

\[
r xu=z(x+u-z).
\]

Therefore

\[
\boxed{c^2-(1+g)c+rg=0.}
\]

### Theorem PF7 — PROVED

Let a carry-filtered cycle have consecutive ratio set

\[
R=\{x_{i+1}/x_i:i\in\mathbb Z_k\},
\qquad |R|=L,
\]

and let `Z` be the set of chosen opposite-colour anchors on its cycle edges. Then there is a set `C` with

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

For each fixed `g`, the displayed quadratic has at most two roots `c`. Thus the set of normalized anchor ratios `z_i/x_i` has size at most `2L`. The quotient-set bound follows from

\[
Z/Z\subseteq(C/C)(X/X).
\]

`square`

## 9. Alternating inverse-propagation dichotomy

### Corollary PF8 — PROVED

Assume

\[
|X/X|\le K|X|,
\qquad |R|\le L,
\]

and fix `0<eta<=1`. Then either:

1. **anchor concentration:**
   \[
   |Z|<\eta|X|,
   \]
   and some opposite-colour anchor supports more than `1/eta` cycle edges; or
2. **structure propagation:**
   \[
   |Z|\ge\eta|X|
   \]
   and
   \[
   \boxed{
   |Z/Z|\le\frac{4L^2K}{\eta}|Z|.
   }
   \]
   Hence `Z` is controlled by a multiplicative coset progression with parameters depending only on `K,L,eta`.

### Proof

The first alternative is pigeonhole. In the second, apply PF7 and divide by `|Z|>=eta|X|`. Then apply PF3. `square`

This is the first rigorous inverse theorem that propagates through the alternating red/blue closure:

\[
\boxed{
\text{low-complexity cycle}
\Longrightarrow
\text{high-load anchor or low-complexity opposite colour}.
}
\]

## 10. Limit of PFR alone

PFR classification does not itself prove that a structured core is repairable. The frozen `p=11` cycle already has quotient doubling `3/2` and is a full union of two subgroup cosets, yet no one-colour permutation of its cycle block improves the triple potential.

The role of inverse theory is therefore to compress an obstruction into one of two objects:

- a bounded quotient/coset system supporting an explicit absorber bank;
- a small set of high-load anchors.

The next step must prove that alternating expansion of these compressed objects terminates or enters the superregular selection endpoint.

## 11. Rational-expander target

The Möbius transition is governed by

\[
F_r(c)=\frac{c(1-c)}{r-c}.
\]

A persistently low-complexity alternating core would require both a set `C` and its image `F_r(C)` to have small multiplicative doubling. This suggests the following targeted sum-product statement.

### Target PF9 — OPEN

For fixed `r notin {0,1}`, classify finite sets `C subset F_p\setminus{0,r}` for which both

\[
|C/C|\le K|C|
\]

and

\[
|F_r(C)/F_r(C)|\le K|F_r(C)|.
\]

The desired conclusion is that `C` is bounded in size or lies in one of finitely many explicitly describable exceptional Möbius orbits.

Finite-field sum-product estimates for rational functions indicate that nonlinear rational maps should expand multiplicatively structured sets unless they have a special algebraic form, but the precise simultaneous-doubling statement above is not currently established here.

## References used as external inputs

- Green and Ruzsa, *Freiman's theorem in an arbitrary abelian group*.
- Reiher and Schoen, *Note on the Theorem of Balog, Szemeredi, and Gowers*.
- Gowers, Green, Manners and Tao, *Marton's Conjecture in abelian groups with bounded torsion*.
- Bukh and Tsimerman, *Sum-product estimates for rational functions*.
