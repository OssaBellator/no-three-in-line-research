# Primitive-direction carry windows and secant energy

This chapter complements the product-carry and coordinate-carry classifications by describing the Euclidean lift along primitive integer directions. It gives an exact root-window model for the carry filter and a scale-sensitive decomposition of secant-star load.

Throughout, `p` is an odd prime and grid coordinates lie in `{1,...,p-1}`.

## 1. Primitive-direction channel words

Every grid cell `Z=(z,w)` belongs to the unique channel

\[
d\equiv zw\pmod p.
\]

Let `nu=(r,s)` be a primitive integer direction, normalized by `r>0`, or `r=0` and `s>0`. Define its feasible step interval

\[
I_Z(\nu)=\{t\in\mathbb Z:1\le z+tr\le p-1,\ 1\le w+ts\le p-1\}.
\]

Define the quadratic channel word

\[
\gamma_{Z,\nu}(t)=d+(zs+wr)t+rs\,t^2\pmod p.
\]

### Theorem G5 — PROVED

For every primitive direction `nu`:

1. reduction modulo `p` is injective on `I_Z(nu)`;
2. `Z+t nu` lies on `H_c` exactly when `gamma_{Z,nu}(t)=c`;
3. the real points of `H_c` on `Z+R nu` are exactly the feasible integer representatives of the roots of
   \[
   rsT^2+(zs+wr)T+(d-c)=0\pmod p.
   \]

Thus a modular secant survives the standard integer lift precisely when both modular step roots lie in the same feasible interval.

If `Z in H_b`, `a != b`, and `rs != 0`, the two real step roots `m,n` for `H_a` satisfy

\[
m+n\equiv-\frac{zs+wr}{rs},\qquad mn\equiv\frac{b-a}{rs}\pmod p.
\]

### Proof

If `t_1,t_2 in I_Z(nu)`, then

\[
|t_1-t_2|\max(|r|,|s|)\le p-2,
\]

so congruent feasible steps are equal. Expanding gives

\[
(z+tr)(w+ts)=zw+(zs+wr)t+rs\,t^2.
\]

Reduction modulo `p` proves the channel criterion; injectivity gives the exact real-root correspondence. The final identities are Vieta's relations. `square`

## 2. Secant-star collision energy

Let

\[
Y\subseteq\bigcup_{c\in\mathcal B}H_c,\qquad |\mathcal B|=q,
\]

and let `Z notin Y`. For each primitive direction define

\[
n_{\nu,c}(Y)=|\{t\in I_Z(\nu)\setminus\{0\}:Z+t\nu\in Y\cap H_c\}|,
\]

and `N_nu(Y)=sum_c n_{nu,c}(Y)`.

### Theorem G6 — PROVED

The weighted secant load has the exact decomposition

\[
\boxed{A_Y(Z)=\sum_\nu\binom{N_\nu(Y)}2.}
\]

Equivalently,

\[
A_Y(Z)=
\sum_c\sum_\nu\binom{n_{\nu,c}(Y)}2+
\sum_{\{b,c\}}\sum_\nu n_{\nu,b}(Y)n_{\nu,c}(Y).
\]

Moreover,

\[
n_{\nu,c}(Y)\le2,\qquad N_\nu(Y)\le2q,
\]

and hence

\[
\boxed{A_Y(Z)\le\frac{2q-1}{2}|Y|\le\frac{q(2q-1)(p-1)}2.}
\]

### Proof

Primitive directions partition the real lines through `Z`; a line containing `N_nu(Y)` outside points contributes `binom(N_nu(Y),2)`. Theorem G5 gives at most two roots per channel. Thus

\[
\binom{N_\nu(Y)}2\le\frac{2q-1}{2}N_\nu(Y),
\]

and summing uses `sum_nu N_nu(Y)=|Y|`. `square`

## 3. High-direction tail

Put `h(nu)=max(|r|,|s|)` and

\[
A_Y^{\ge H}(Z)=\sum_{h(\nu)\ge H}\binom{N_\nu(Y)}2.
\]

### Theorem G7 — PROVED

Let

\[
M_H=\min\left(2q,\left\lfloor\frac{p-2}{H}\right\rfloor\right).
\]

Then

\[
\boxed{A_Y^{\ge H}(Z)\le\frac{\max(M_H-1,0)}2|Y|}
\]

and in particular

\[
\boxed{A_Y^{\ge H}(Z)\le\frac{p-2}{2H}|Y|.}
\]

No real secant through `Z` has primitive height greater than `(p-2)/2`.

### Proof

The feasible interval contains zero and has at most

\[
\left\lfloor\frac{p-2}{h(\nu)}\right\rfloor
\]

nonzero steps. Hence `N_nu(Y)<=M_H` for `h(nu)>=H`. Apply

\[
\binom{N_\nu(Y)}2\le\frac{\max(M_H-1,0)}2N_\nu(Y)
\]

and sum over directions. `square`

## 4. Low/high decomposition

Write

\[
A_Y^{<H}(Z)=\sum_{h(\nu)<H}\binom{N_\nu(Y)}2.
\]

### Corollary G8 — PROVED

For every integer `H>=1`,

\[
\boxed{A_Y^{<H}(Z)\le2H(H-1)\binom{2q}{2}.}
\]

Consequently,

\[
\boxed{A_Y(Z)\le2H(H-1)\binom{2q}{2}+\frac{p-2}{2H}|Y|.}
\]

If `T=A_Y(Z)>0` and

\[
H>\frac{(p-2)|Y|}{T},
\]

then `A_Y^{<H}(Z)>T/2`.

### Proof

There are `4H(H-1)` nonzero integer vectors of height below `H`, and at most `2H(H-1)` normalized directions after identifying opposites. Each contributes at most `binom(2q,2)`. Add Theorem G7. The final assertion follows because the high-height tail is then less than `T/2`. `square`

## 5. Relation to the carry-signature pathway

The existing carry-signature theorems classify large obstruction classes arithmetically. G5--G8 add a geometric coordinate:

- every signature incidence occupies a primitive direction and finite root window;
- high primitive directions have a decaying `O(p|Y|/H)` energy tail;
- persistent load must concentrate in only `O(H^2)` low directions;
- an alternating-closure potential can charge both new carry signatures and new low-height direction classes.

This does not prove termination. It narrows the remaining target to showing that a bounded family of low primitive directions cannot remain carry-feasible along a long multiplicative or bounded-denominator anchor orbit, except inside the already isolated perfect-alignment chambers.

The checker

```bash
python scripts/verify_carry_windows.py --prime 17 --all-pairs
```

verifies the root-window model and height estimate for every ordered channel pair at a chosen prime. It is a finite sanity check, not a proof for arbitrary `p`.
