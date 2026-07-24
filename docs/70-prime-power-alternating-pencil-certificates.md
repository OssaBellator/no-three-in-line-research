# Quantitative alternating certificates from child pencils

CMR107--CMR109 prove a diffuse-or-alternating dichotomy. This chapter sharpens
the alternating side in two ways:

1. the degree-two forbidden matching bank has a better universal constant than
   the original `128` bound;
2. the pencil mass controls the size of the extracted endpoint-disjoint star,
   and failure of its matching bank forces an explicit rank concentration.

## 1. Optimized degree-two matching spread

Let `F` be a set of forbidden cells in a `t` by `t` matching board, with at most
two forbidden cells in every row and column. Put

\[
\Omega(F)=\{\pi\in S_t:(i,\pi(i))\notin F\text{ for all }i\}.
\]

### Theorem CMR110 — PROVED

For every `t>=7`,

\[
|\Omega(F)|\ge\frac{t!}{72}.
\]

If `Q` is a compatible partial matching of `r` nonforbidden cells and `pi` is
uniform on `Omega(F)`, then

\[
\Pr(Q\subseteq\pi)
\le
\frac{72}{(t)_r}.
\]

### Proof

For every forbidden cell `(i,j)`, let `A_{ij}` be the canonical event
`pi(i)=j` under a uniformly random permutation. Each event has probability
`1/t`, and its lopsided dependency degree is at most two.

For `t=7`, choose

\[
x=\frac5{19}.
\]

Then

\[
\frac17
\le
\frac5{19}\left(\frac{14}{19}\right)^2
\]

because `7*5*14^2=6860>=6859=19^3`. The lopsided local lemma gives

\[
\Pr(\pi\in\Omega(F))
\ge
\left(\frac{14}{19}\right)^{|F|}
\ge
\left(\frac{14}{19}\right)^{14}
>
\frac1{72}.
\]

For `t>=8`, choose

\[
x=\frac2{t+1}.
\]

The local-lemma condition is

\[
\frac1t
\le
\frac{2(t-1)^2}{(t+1)^3},
\]

which is equivalent to

\[
t^3-7t^2-t-1\ge0.
\]

It holds at `t=8`, where the left side is `55`, and is increasing thereafter.
Thus

\[
\Pr(\pi\in\Omega(F))
\ge
\left(\frac{t-1}{t+1}\right)^{2t}.
\]

The final expression is increasing for real `t>1`: writing `u=1/t`, its
logarithmic derivative is positive because

\[
\frac{u}{1-u^2}
>
\operatorname{artanh}(u).
\]

At `t=8` it is `(7/9)^16>1/56>1/72`. This proves the state count.
At most `(t-r)!` permutations contain `Q`, so division by `t!/72` proves the
cylinder bound. ∎

The constant `72` may replace `128` in every prefix or alternating matching bank
whose forbidden-position graph has row and column degree at most two.

## 2. Quantitative star extraction

Retain the supported child-pencil notation from CMR106--CMR109.

### Theorem CMR111 — PROVED

If `V_{1,Omega}(A)>0`, there is a supported pencil cell whose outside-pair graph
contains an alternating star bank with

\[
t_1
\ge
\left\lfloor
\frac{\mathcal V_{1,\Omega}(A)}
{4p^2L(|Z|-1)}
\right\rfloor
\]

selected endpoints in one permutation layer, whenever the right side is at
least seven.

If `V_{2,Omega}(A)>0`, there are a supported child profile and an outside point
whose translated-child secant graph contains a nested matching bank with

\[
t_2
\ge
\left\lfloor
\frac{\mathcal V_{2,\Omega}(A)}
{2p^2|Z|(L-1)}
\right\rfloor
\]

selected endpoints, whenever the right side is at least seven.

Both banks contain at least `t_i!/72` states and have cylinder probability at
most `72/(t_i)_r`.

### Proof

For the one-point pencil, some supported cell `z` has degree at least

\[
\frac{\mathcal V_{1,\Omega}(A)}{p^2L}.
\]

If a maximal matching in its outside-pair graph has `nu` edges, maximality gives

\[
\deg(z)\le2\nu(|Z|-1).
\]

At least half of the matching edges have an endpoint in one fixed permutation
layer. Choosing one such endpoint from each gives

\[
t_1\ge\frac{\deg(z)}{4(|Z|-1)}.
\]

The first formula follows.

For the two-point pencil, average over at most `p^2|Z|` translated-child graphs.
If one has `d` edges and a maximal matching of size `nu`, then

\[
d\le2\nu(L-1).
\]

All matching endpoints already lie in one permutation layer, so `t_2=nu` and
the second formula follows. CMR110 supplies the state count and cylinder law. ∎

## 3. Frozen-bank concentration certificate

Fix either extracted star in one parent-node state containing its supported
profile. Let `B` be the selected endpoint set of size `t>=7`, let

\[
X=S_*\setminus B,
\]

and let `T_r` count real-collinear certificates consisting of exactly `r`
compatible candidate cells from the endpoint matching board and `3-r` points
of `X`.

The current fixed state contains at least the `t` extracted star triples, each
of which touches `B`. Hence

\[
D_*:=\Phi(S_*)-\Phi(X)\ge t.
\]

### Theorem CMR112 — PROVED

For a uniform optimized endpoint bank,

\[
\mathbb E\bigl[\Phi(S_\pi)-\Phi(X)\bigr]
\le
72\left(
\frac{T_1}{t}
+
\frac{T_2}{(t)_2}
+
\frac{T_3}{(t)_3}
\right).
\]

If no endpoint-bank state lowers the triple potential relative to the fixed
parent-node state `S_*`, then at least one rank `r in {1,2,3}` satisfies

\[
\boxed{
\frac{T_r}{(t)_r}
\ge
\frac{t}{216}.
}
\]

### Proof

The first inequality is the AN4 certificate calculation with CMR110 in place of
the original constant. If every state has potential at least `Phi(S_*)`, then
the expectation on the left is at least

\[
\Phi(S_*)-\Phi(X)=D_*\ge t.
\]

Therefore the sum of the three normalized certificate counts is at least
`t/72`. One of them is at least one third of this value. ∎

## 4. Revised termination target

A concentrated child pencil no longer yields only a constant-size repair bank.
Its mass quantitatively produces a large endpoint-disjoint alternating bank.
If that bank is frozen, it produces one of three explicit density certificates:

1. a one-cell outside secant shadow;
2. a two-cell anchored pair shadow;
3. a candidate-only triple core.

These are exactly the three concentration alternatives in the main branch's
alternating star-neutralization program, now embedded at a definite node and
p-adic depth. The remaining theorem is to show that repeated expansion of these
certificates either finds a decreasing joint state or consumes a scale-summable
carry or quotient budget.

The local-lemma constants and quantitative matching extraction are checked in
[`scripts/verify_prime_power_alternating_pencil_certificates.py`](../scripts/verify_prime_power_alternating_pencil_certificates.py).
