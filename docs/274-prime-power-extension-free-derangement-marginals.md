# Exact derangement counts sharpen the extension-free bank

CMR1350--CMR1357 give the extension-free response graph

\[
H_e=K_{n,n}\setminus(O\cup\{e\})
\]

the same permanent lower bound as a fixed-extension bank.  Because only one
nonidentity edge is removed from the derangement graph, the bank size and its
rank-one marginals can be counted exactly.

Relabel `O` as the identity and write `e=(0,1)`.  Let `D_n` be the number of
derangements of `n` objects.

## Exact bank size

### Theorem CMR1358 -- PROVED

\[
\boxed{
|\operatorname{PM}(H_e)|
=D_n\frac{n-2}{n-1}.
}
\]

### Proof

The perfect matchings avoiding `O` are the `D_n` derangements.  The symmetric
group acts transitively on the `n(n-1)` nonidentity cells.  Counting incidences
between derangements and their `n` selected cells shows that every nonidentity
cell belongs to

\[
\frac{nD_n}{n(n-1)}=\frac{D_n}{n-1}
\]

derangements.  Delete those containing `e`. ∎

The formula also proves the required divisibility.

## Improved universal constant

Define

\[
\boxed{
\lambda_n
=
\frac{n!(n-1)}{D_n(n-2)}.
}
\]

### Theorem CMR1359 -- PROVED

For every `n>=4`,

\[
\boxed{
\lambda_n\le4.
}
\]

Moreover `lambda_4=4` and `lambda_n` tends to `e`.

### Proof

The exact value at four uses `D_4=9`.  For `n>=5`, the alternating derangement
series gives

\[
D_n/n!\ge1/3.
\]

Hence

\[
\lambda_n
\le
3\frac{n-1}{n-2}
\le4.
\]

The limit follows from `D_n/n!` tending to `e^{-1}`. ∎

This replaces the earlier bound `kappa_n<=16` for higher-rank prescriptions in
the extension-free bank.

## Exact rank-one marginal bound

Let `R` be uniform on `PM(H_e)` and let `a` be any allowed edge of `H_e`.

### Theorem CMR1360 -- PROVED

\[
\boxed{
\Pr(a\in R)\le\frac1{n-2}.
}
\]

Equality holds when `a` shares the source row or target column of `e`.

### Proof

Among all derangements, the edge `a` occurs `D_n/(n-1)` times.  Restricting to
those which avoid `e` can only reduce this numerator.  Divide by the exact bank
size from CMR1358.  If `a` shares the source row or target column of `e`, no
perfect matching can contain both, so no numerator is lost and equality holds. ∎

Thus rank-one collateral and unavailable-edge use need no constant larger than
one.

## Rank-two and rank-three prescriptions

### Theorem CMR1361 -- PROVED

For every compatible rank-`r` prescription `P subseteq E(H_e)`, with `r=2` or
`3`,

\[
\boxed{
\Pr(P\subseteq R)
\le
\frac{\lambda_n}{(n)_r}
\le
\frac4{(n)_r}.
}
\]

### Proof

At most `(n-r)!` permutations contain `P`.  Divide by the exact bank size of
CMR1358 and simplify. ∎

The same formula is valid for rank one, but CMR1360 is stronger there.

## Sharpened collateral expectation

Let `V_r^e` be the corrected extension-free candidate counts of CMR1354.

### Theorem CMR1362 -- PROVED

For uniform `R in PM(H_e)`,

\[
\boxed{
\mathbb E N(R)
\le
\frac{V_1^e}{n-2}
+
\lambda_n
\left[
\frac{V_2^e}{(n)_2}
+
\frac{V_3^e}{(n)_3}
\right].
}
\]

Therefore an ambient strict improvement exists whenever the right side is below
`D_S(e)`.

### Proof

Apply CMR1360 to every rank-one prescription and CMR1361 to ranks two and three,
then sum.  Every response omits `e`. ∎

This is the strongest general one-bank expectation currently proved in the
branch.

## Sharpened restricted-host penalty

Let `b_e` be the number of extension-free allowed edges unavailable in the
current host, and let `m=Phi(S)`.

### Theorem CMR1363 -- PROVED

If

\[
\boxed{
\frac{V_1^e+(m+1)b_e}{n-2}
+
\lambda_n
\left[
\frac{V_2^e}{(n)_2}
+
\frac{V_3^e}{(n)_3}
\right]
<
D_S(e),
}
\]

then some extension-free response is feasible and has potential below `m`.

### Proof

CMR1360 gives expected unavailable-edge use at most `b_e/(n-2)`.  Add the
feasibility penalty `(m+1)` and combine it with CMR1362 exactly as in CMR1207. ∎

Complete blockage still gives the minimal unit-wall descent.

## Sharpened line-profile quotient

Let the corrected extension-free line profiles be those of CMR1334--CMR1349,
with `G=H_e`.

### Theorem CMR1364 -- PROVED

The rank/profile upper quotient may use coefficients

\[
\boxed{
\frac1{n-2}
}

for rank one and unavailable-edge incidences, and

\[
\boxed{
\frac{\lambda_n}{(n)_2},
\qquad
\frac{\lambda_n}{(n)_3}
}

for rank two and rank three.  These coefficients dominate every exact
extension-free response row and preserve the upper-quotient lifting of CMR1329.

### Proof

The probability bounds CMR1360--CMR1361 are uniform over all exact
prescriptions of the stated ranks.  Multiply the exact class counts and group by
profile fibres. ∎

## Exact-derangement endpoint

### Corollary CMR1365 -- PROVED

Using one extension-free bank per target cell:

1. the response-bank denominator is exact;
2. the higher-rank loss factor is at most four and tends to `e`;
3. rank-one collateral has edge probability at most `1/(n-2)`;
4. the unavailable-edge penalty has the same sharp coefficient;
5. the fixed-extension optimization is absent;
6. line-profile upper quotients inherit the sharper constants;
7. blocked banks retain exact unit-wall descent and every response has a
   canonical realizing forbidden extension.

The remaining diagonal-block task is to combine these constants with the
pair-moment and arithmetic line-distribution bounds strongly enough to obtain a
subcritical same-owner quotient.  No all-`n` theorem is claimed.

Exact derangement bank sizes, constants, marginals, prescription ratios and
restricted-host arithmetic are checked in
[`scripts/verify_prime_power_extension_free_derangement_marginals.py`](../scripts/verify_prime_power_extension_free_derangement_marginals.py).
