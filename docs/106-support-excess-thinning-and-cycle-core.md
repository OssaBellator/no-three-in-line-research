# Support-excess thinning and the short-cycle collateral core

The recursive rematching frontier after PX198--PX200 has a stable spread measure,
but still needs quantitative control of the rank-one, rank-two, and rank-three
certificate families created by a replacement matching. This chapter refines the
square-root thinning theorem PX189 at the exact level needed for that accounting.

The main point is that a rank-`r` certificate need not use only `r` endpoint
indices. If it uses `u>r`, endpoint thinning gives an additional factor

\[
q^{u-r}
\]

beyond the ordinary matching-cylinder scale. For square-root thinning this is a
power saving. The only sectors with no such saving are literal short cycles of
the rematching permutation.

Let the movable endpoints be

\[
A=\{(x_i,y_i):i\in[t]\}.
\]

Write

\[
e_{ij}=(x_i,y_j)
\]

for one candidate replacement cell. A compatible rank-`r` partial matching is a
set of `r` cells with distinct row indices and distinct column indices. Its
endpoint-index support is

\[
\operatorname{supp}(E)
=
\{i:e_{ij}\in E\}\cup\{j:e_{ij}\in E\}.
\]

Thus

\[
r\le |\operatorname{supp}(E)|\le2r.
\]

Certificate multiplicities are allowed. Equivalently, each partial matching may
carry a nonnegative weight recording the number of background completions of
that matching pattern.

## 1. Simultaneous support-sector thinning

For `1<=r<=3` and `r<=u<=2r`, let

\[
\mathcal C_{r,u}
\]

be a finite weighted family of compatible rank-`r` partial matchings having
support size exactly `u`. Let

\[
W_{r,u}
=
\sum_{E\in\mathcal C_{r,u}}w(E).
\]

For a set of endpoint indices `J`, let `W_(r,u)(J)` be the total weight of the
certificates whose complete support lies in `J`.

### Theorem PX201 -- PROVED

Let `0<q<=1` and suppose

\[
qt\ge32.
\]

There is a set `J subseteq [t]` such that

\[
\boxed{|J|\ge\frac{qt}{2}}
\]

and simultaneously for all nine support sectors

\[
\boxed{
W_{r,u}(J)
\le
16q^uW_{r,u}
}
\qquad
(1\le r\le3,\ r\le u\le2r).
\]

### Proof

Retain every endpoint index independently with probability `q`. A certificate
in `C_(r,u)` survives exactly when all its `u` support indices survive, so

\[
\mathbb E W_{r,u}(J)=q^uW_{r,u}.
\]

Markov's inequality gives

\[
\Pr\bigl(W_{r,u}(J)>16q^uW_{r,u}\bigr)
\le\frac1{16}.
\]

There are

\[
2+3+4=9
\]

possible sectors. Also the lower-tail Chernoff bound gives

\[
\Pr\left(|J|<\frac{qt}{2}\right)
\le e^{-qt/8}
\le e^{-4}.
\]

Therefore the probability that any required inequality fails is at most

\[
\frac9{16}+e^{-4}<1.
\]

A suitable realization exists. \(\square\)

The proof is weighted, so it applies without change when one geometric partial
matching represents many background certificates.

## 2. Conditioned certificate-load transfer

Let `F_J` be the forbidden-position graph on the selected rows and columns, with
maximum row and column degree at most `Delta`. Let `Omega_(F_J)` be the allowed
perfect matchings and put

\[
s=|J|.
\]

For `M` uniform on `Omega_(F_J)`, define

\[
\Phi_{r,u}(M)
=
\sum_{E\in\mathcal C_{r,u}(J)}w(E)\mathbf1_{E\subseteq M}.
\]

### Theorem PX202 -- PROVED

If

\[
s\ge8\Delta,
\]

then

\[
\boxed{
\mathbb E\Phi_{r,u}(M)
\le
\frac{e^{4\Delta}W_{r,u}(J)}{(s)_r}.
}
\]

More generally, condition on any extendable compatible partial matching `E_0`
of rank `a`. If `s-a>=8Delta`, then every residual weighted certificate family
satisfies

\[
\boxed{
\mathbb E\bigl(\Phi_{r,u}(M)\mid E_0\subseteq M\bigr)
\le
\frac{e^{4\Delta}W_{r,u}(J\mid E_0)}{(s-a)_r}.
}
\]

For a set `J` supplied by PX201, the unconditioned bound becomes

\[
\boxed{
\mathbb E\Phi_{r,u}(M)
\le
16\cdot4^r e^{4\Delta}
q^{u-r}\frac{W_{r,u}}{t^r}.
}
\]

### Proof

PX196 bounds the probability of every compatible rank-`r` cylinder by

\[
\frac{e^{4\Delta}}{(s)_r}.
\]

Multiply by the certificate weights and sum. Under conditioning, PX199 gives the
same estimate in the residual order `s-a`.

For the final display, PX201 gives

\[
W_{r,u}(J)\le16q^uW_{r,u}.
\]

Since `qt>=32`, one has `s>=16`. For `r<=3`, every factor of `(s)_r` is at least
`s/2`, and hence

\[
(s)_r\ge\left(\frac{s}{2}\right)^r
\ge
\left(\frac{qt}{4}\right)^r.
\]

Substitution gives the claim. \(\square\)

The conditioning statement is important: bounded-rank sequential exposure does
not multiply the spread constant. Only the residual falling factorial changes.

## 3. The exact short-cycle core

Every recursive endpoint bank forbids the current endpoint positions. In the
index notation above, all diagonal cells `e_(ii)` are therefore forbidden.

### Theorem PX203 -- PROVED

Assume every diagonal cell `e_(ii)` is forbidden.

1. A rank-one allowed certificate has support size two.
2. A rank-two compatible certificate has support size two if and only if it is
   the transposition pair

   \[
   \boxed{\{e_{ij},e_{ji}\}}
   \qquad(i\ne j).
   \]

3. A rank-three compatible certificate has support size three if and only if it
   is one of the two directed three-cycles on three endpoint indices:

   \[
   \boxed{\{e_{ij},e_{jk},e_{ki}\}}
   \]

   or its reverse.

Consequently, under square-root thinning `q=t^(-1/2)`:

- every rank-one certificate gains at least `t^(-1/2)`;
- every rank-two certificate except a transposition pair gains at least
  `t^(-1/2)`;
- every rank-three certificate except a directed three-cycle gains at least
  `t^(-1/2)`.

### Proof

Support size one for one cell means `i=j`, which is forbidden.

For rank two and support size two, the two distinct source rows and two distinct
target columns use the same two indices. Since fixed points are forbidden, the
only bijection between them is the transposition.

For rank three and support size three, the source and target index sets are the
same three-element set. The partial matching is therefore a permutation of that
set. It has no fixed points, so it must be one of the two three-cycles.
\(\square\)

This is an exact structural reduction, not only an asymptotic estimate.

## 4. Explicit consequence for the `T_2` sector

Give every compatible rank-two pair the weight equal to the number of background
anchors completing it to a collinear triple. Write

\[
W_{2,2},\qquad W_{2,3},\qquad W_{2,4}
\]

for the three support sectors before thinning.

### Corollary PX203a -- PROVED

For square-root thinning, a set `J` can be chosen so that its uniform allowed
matching satisfies

\[
\boxed{
\mathbb E T_2
\le
256e^{4\Delta}
\left(
\frac{W_{2,2}}{t^2}
+
\frac{W_{2,3}}{t^{5/2}}
+
\frac{W_{2,4}}{t^3}
\right).
}
\]

If every candidate secant line contains at most `L_Z` background anchors, then

\[
W_{2,2}
\le
L_Z\binom t2,
\]

and therefore the undamped transposition core contributes at most

\[
\boxed{128e^{4\Delta}L_Z}
\]

to the displayed expectation.

### Proof

Apply PX202 with `r=2` and `q=t^(-1/2)`. The common constant is

\[
16\cdot4^2=256.
\]

For support size two, PX203 gives at most one candidate transposition pair for
each unordered pair of endpoint indices. Its weight is at most `L_Z`. Hence

\[
W_{2,2}\le L_Z\binom t2.
\]

Substitute. \(\square\)

Thus the only rank-two sector untouched by square-root thinning is already
bounded by the selected-line occupancy parameter. The genuinely unresolved
rank-two quantities are now the support-three and support-four weighted counts.

## 5. Improvement criterion

Let `D_*` be a number of old certificates destroyed by every matching in the
allowed bank. In the clean-star, loaded-line, and radial-core applications after
PX189, one has at least

\[
D_*\ge s.
\]

### Corollary PX204 -- PROVED

If

\[
\boxed{
D_*
>
e^{4\Delta}
\sum_{r=1}^3\sum_{u=r}^{2r}
\frac{W_{r,u}(J)}{(s)_r},
}
\]

then some allowed replacement matching strictly lowers the total certificate
potential.

The same conclusion holds after compatible bounded-rank conditioning, with
`(s)_r` replaced by the residual falling factorial and with only residual
certificate weights included.

### Proof

PX202 bounds the expected total created certificate weight by the right-hand
side. Every bank state destroys at least `D_*` old weight. If the expected
created weight is smaller than `D_*`, at least one state has negative net
potential change. The conditional statement is identical using PX199. \(\square\)

## 6. Updated termination frontier

PX201--PX204 do not prove an absolute recursion depth. They do remove a large
part of the accounting ambiguity.

After square-root thinning:

1. all rank-one collateral is support-excess and receives a power saving;
2. the only undamped rank-two sector is the transposition core, whose contribution
   is `O(L_Z)`;
3. the only undamped rank-three sector is the directed three-cycle core;
4. every other sector receives at least one factor `t^(-1/2)`;
5. all of these estimates survive bounded-rank conditioning without multiplying
   the spread constant.

The next quantitative task is therefore to bound

\[
\frac{W_{1,2}}{t^{3/2}},
\qquad
\frac{W_{2,3}}{t^{5/2}},
\qquad
\frac{W_{2,4}}{t^3},
\]

and the support-excess rank-three analogues along the decoder output. A successful
depth-two theorem no longer needs to control arbitrary certificate families at
full strength; it only needs these normalized support sectors plus the bounded
short-cycle core.

## 7. Verification

Run

```bash
python scripts/verify_product_support_excess_thinning.py
```

The verifier exhausts all compatible rank-at-most-three partial matchings on
seven endpoint indices, checks the short-cycle classification, verifies the
Bernoulli support identity exactly, checks the simultaneous-thinning probability
budget, tests the allowed-bank load transfer by exact permutation enumeration,
and verifies the transposition-core line-load bound.
