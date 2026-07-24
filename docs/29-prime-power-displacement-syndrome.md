# Prime-power displacement signatures and companion carries

This chapter develops exact secant equations for valuation-completed reciprocal
channels. The original coarse syndrome estimate CMR8 is retained for the
historical progression; CMR39 and CMR42 later improve the one- and two-layer
bounds to quadratic polylogarithmic order for fixed prime base.

Let

\[
N=p^k
\]

and let `R_c` be the completed reciprocal permutation. For a nonzero integer
`z`, write `v_p(z)` for its `p`-adic valuation.

## 1. Every secant is p-adically diagonal

Take two distinct channel points

\[
P=(x,R_c(x)),
\qquad
P'=(x',R_c(x')),
\]

and write their exact lifted displacement as

\[
(a,b)=(x'-x,R_c(x')-R_c(x)).
\]

### Theorem CMR6 — PROVED

Every completed-reciprocal secant satisfies

\[
v_p(a)=v_p(b).
\]

Consequently a displacement whose two coordinates have unequal `p`-adic
valuation has multiplicity zero. After the common power of `p` is removed, both
coordinates of every primitive secant direction are units modulo `p`.

### Proof

Let `r=v_p(x)` and `s=v_p(x')`, with the origin assigned valuation `k`. If
`r!=s`, both coordinate differences have valuation `min(r,s)` because the
channel preserves valuation pointwise.

If `r=s<k`, write

\[
x=p^ru,
\qquad
x'=p^rv.
\]

On this stratum,

\[
R_c(x)=p^rc_ru^{-1},
\qquad
R_c(x')=p^rc_rv^{-1}
\pmod {p^k}.
\]

Therefore

\[
R_c(x')-R_c(x)
\equiv
-p^rc_r\frac{v-u}{uv}
\pmod {p^k}.
\]

The unit factors do not change the valuation of `v-u`. Since the exact lifted
differences are nonzero and have magnitude below `p^k`, adding a multiple of
`p^k` cannot change their valuation. ∎

## 2. Exact same-stratum displacement quadratic

Suppose the endpoints have common valuation `r`. Put

\[
t=v_p(a)=v_p(b),
\qquad
\alpha=a/p^t,
\qquad
\beta=b/p^t.
\]

Then `r<=t<k`, and `alpha,beta` are units modulo `p`.

### Theorem CMR7 — PROVED

With `x=p^ru` and `x'=p^rv`, one has

\[
uv\equiv-c_r\alpha\beta^{-1}
\pmod {p^{k-t}},
\]

and hence

\[
u\bigl(u+p^{t-r}\alpha\bigr)
\equiv-c_r\alpha\beta^{-1}
\pmod {p^{k-t}}.
\]

For odd `p`, define the corrected discriminant

\[
D_{r,t}
=
\bigl(p^{t-r}\alpha\bigr)^2
-4c_r\alpha\beta^{-1}.
\]

The candidate residue classes for `u` modulo `p^(k-t)` are in bijection with
the square roots of `D_{r,t}` modulo that modulus. Their number is at most

\[
2p^{\lfloor(k-t)/2\rfloor}.
\]

### Proof

The reciprocal difference identity is

\[
\frac b{p^r}
\equiv
-c_r\frac{a/p^r}{uv}
\pmod {p^{k-r}}.
\]

Both sides contain the factor `p^(t-r)`. Dividing it out and cancelling the
remaining unit gives

\[
\beta\equiv-c_r\alpha(uv)^{-1}
\pmod {p^{k-t}},
\]

which is the first identity. Since

\[
v-u=p^{t-r}\alpha,
\]

substitution gives the quadratic. Moving its right-hand side to the left and
completing the square yields

\[
\bigl(2u+p^{t-r}\alpha\bigr)^2
\equiv
\bigl(p^{t-r}\alpha\bigr)^2
-4c_r\alpha\beta^{-1}
\pmod {p^{k-t}}.
\]

The square-root count is the odd-prime classification from CMR3. ∎

The minus sign in this discriminant is essential. Earlier branch revisions
printed a plus sign even though the preceding product identity had the correct
sign; this consolidated version repairs that transcription error.

## 3. Historical coarse one-channel syndrome bound

Let

\[
L_{p,k}=2k+2p^{\lfloor k/2\rfloor}+1.
\]

### Theorem CMR8 — PROVED

For every odd prime power,

\[
T(R_c)
\le
\frac{L_{p,k}-2}{3}\binom N2
=
O\bigl(N^{5/2}+N^2\log N\bigr).
\]

### Proof

If `s_L` is the occupancy of a real line `L`, then

\[
\sum_L\binom{s_L}{2}=\binom N2.
\]

For `s_L<=L_{p,k}`,

\[
\binom{s_L}{3}
=
\frac{s_L-2}{3}\binom{s_L}{2}
\le
\frac{L_{p,k}-2}{3}\binom{s_L}{2}.
\]

Summation proves the claim. ∎

For the uniform parameter choice, exact data are:

| `N` | maximum real line | real triples |
|---:|---:|---:|
| 9 | 5 | 10 |
| 27 | 7 | 93 |
| 81 | 9 | 580 |
| 243 | 12 | 3303 |
| 25 | 5 | 30 |
| 125 | 8 | 809 |

CMR39 supersedes the asymptotic estimate above by `O(N^2 log N)`.

## 4. Exact companion cross-displacement quadratic

Let

\[
\sigma_p(y)=[(1+e_p)y+1]_N,
\qquad
e_p=
\begin{cases}
p,&p\text{ odd},\\
4,&p=2,
\end{cases}
\]

and put `G=sigma_p o R_c`. Consider

\[
P=(x,R_c(x)),
\qquad
P'=(x+a,G(x+a)),
\]

with exact displacement `(a,b)`. Suppose both columns are nonzero and lie in
the same valuation stratum `r`. Write

\[
x=p^ru,
\qquad
a=p^r\alpha,
\qquad
m=k-r.
\]

### Theorem CMR9 — PROVED

Every such cross-layer pair satisfies

\[
b\equiv1\pmod {p^r}.
\]

Putting `B=(b-1)/p^r`, the first endpoint parameter obeys

\[
Bu^2+(B\alpha-c_re_p)u+c_r\alpha
\equiv0\pmod {p^m}.
\]

For odd `p`, if `p` does not divide `B`, the candidate classes are controlled by
square roots of

\[
\mathcal D=(B\alpha-c_rp)^2-4Bc_r\alpha
\pmod {p^m},
\]

and their number is at most `2p^(floor(m/2))`.

### Proof

Modulo `N`, the row displacement equation is

\[
p^rc_r\bigl((1+e_p)(u+\alpha)^{-1}-u^{-1}\bigr)+1
\equiv b.
\]

The first term is divisible by `p^r`. Subtract one, divide by `p^r`, and
multiply by `u(u+alpha)` to obtain

\[
Bu(u+\alpha)\equiv c_r(e_pu-\alpha)\pmod {p^m}.
\]

This is the stated quadratic. Completing the square with leading coefficient
`B` gives the discriminant. ∎

The remaining fixed-displacement cases are cross-stratum pairs and the singular
regime `p|B`.

## 5. Universal mixed-layer determinant carry identity

Let `f` be any permutation of `[N]`. Put

\[
q(y)=\left\lfloor\frac{(1+e_p)y+1}{N}\right\rfloor,
\qquad
d(y)=e_py+1-Nq(y),
\]

so that `sigma_p(y)=y+d(y)` as standard integers. For columns `x_i`, write
`y_i=f(x_i)`, choose layer indicators `epsilon_i` in `{0,1}`, and set

\[
z_i=y_i+\epsilon_i d(y_i).
\]

### Theorem CMR10 — PROVED

The exact determinant is

\[
\begin{aligned}
\Delta((x_i,z_i)_{i=1}^3)
={}&\Delta((x_i,y_i)_{i=1}^3)\\
&+(x_2-x_1)(\epsilon_3d(y_3)-\epsilon_1d(y_1))\\
&-(x_3-x_1)(\epsilon_2d(y_2)-\epsilon_1d(y_1)).
\end{aligned}
\]

For three companion-layer points,

\[
\Delta_G
=(1+e_p)\Delta_f
-N\Bigl((x_2-x_1)(q(y_3)-q(y_1))
-(x_3-x_1)(q(y_2)-q(y_1))\Bigr).
\]

### Proof

Substitute the definition of `z_i` and use linearity in the row coordinates.
When all layer indicators equal one, the constant terms in `d(y)` cancel, the
`e_py` terms contribute `e_p Delta_f`, and the remaining terms give the stated
multiple of `N`. ∎

The finite checks are implemented in
[`scripts/verify_prime_power_displacement.py`](../scripts/verify_prime_power_displacement.py).