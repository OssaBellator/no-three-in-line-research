# Summing extension-free banks gives an exact line-composition kernel

CMR1358--CMR1365 sharpen one target-cell bank.  The target-incidence identity
sums over all selected cells, so the natural next step is to sum the extension-
free candidate counts over every target cell in one permutation layer.

The resulting formulas are exact and depend only on the composition of one real
line: opposite-layer cells, targeted-layer cells and unselected cells.  They give
a concrete sufficient inequality for strict improvement.  They also show why
pair moments and independent linewise envelopes alone are not enough: a sparse
three-cell target line with many unselected continuation cells can have a large
rank-three upper kernel even though a better response may exist globally.

Fix disjoint perfect matchings `O,M` on an `n x n` inherited board.  For every
nonaxis line `L`, put

\[
o=o_L=|O\cap L|,
\qquad
m=m_L=|M\cap L|,
\qquad
u=u_L=|L\cap[n]^2|-o-m.
\]

For each `e in M`, use the extension-free response graph

\[
H_e=K_{n,n}\setminus(O\cup\{e\}).
\]

## Rank-one sum over one layer

Let `V_1^e(L)` be the corrected rank-one candidate count on `L` for the bank
through `e`.

### Theorem CMR1366 -- PROVED

\[
\boxed{
\sum_{e\in M}V_1^e(L)
=
n\binom o2u.
}
\]

### Proof

If `e` is off `L`, the response graph has `o` fixed cells, `m` old response-layer
cells and `u` genuinely new available cells on `L`.  If `e` lies on `L`, both the
response-graph population and the surviving old population fall by one, so their
difference remains `u`.  Thus every one of the `n` choices of `e` contributes
`binom(o,2)u`. ∎

## Rank-two sum over one layer

### Theorem CMR1367 -- PROVED

\[
\boxed{
\sum_{e\in M}V_2^e(L)
=
o\left[(n-1)mu+n\binom u2\right].
}
\]

### Proof

For the `n-m` choices of `e` off `L`, the line contribution is

\[
o\left[\binom{m+u}{2}-\binom m2\right]
=o\left[mu+\binom u2\right].
\]

For the `m` choices on `L`, it is

\[
o\left[\binom{m+u-1}{2}-\binom{m-1}{2}\right]
=o\left[(m-1)u+\binom u2\right].
\]

Add the two classes. ∎

## Rank-three sum over one layer

### Theorem CMR1368 -- PROVED

\[
\boxed{
\sum_{e\in M}V_3^e(L)
=
(n-2)\binom m2u
+(n-1)m\binom u2
+n\binom u3.
}
\]

### Proof

For `e` off `L`, use

\[
\binom{m+u}{3}-\binom m3
=
\binom m2u+m\binom u2+\binom u3.
\]

For `e` on `L`, replace `m` by `m-1`.  Weight the two formulas by `n-m` and `m`.
The coefficients simplify to the displayed expression. ∎

All three sums vanish when `u=0`: a fully selected line creates no new
collateral on itself under any target-cell response.

## Layer target incidence

Let `D_S(e;L)` count old physical triples on `L` containing `e`.

### Theorem CMR1369 -- PROVED

\[
\boxed{
\sum_{e\in M}D_S(e;L)
=
m\binom{o+m-1}{2}.
}
\]

After summing both layers,

\[
\boxed{
m\binom{o+m-1}{2}
+o\binom{o+m-1}{2}
=3\binom{o+m}{3}.
}
\]

### Proof

Each selected `M` cell on `L` forms a target with every pair among the other
`o+m-1` selected cells.  The symmetric identity is
`(o+m)binom(o+m-1,2)=3binom(o+m,3)`. ∎

Summing over nonaxis lines recovers the global identity
`sum_e D_S(e)=3Phi(S)`.

## The one-layer upper kernel

Let

\[
\lambda_n=\frac{n!(n-1)}{D_n(n-2)}.
\]

Define

\[
\begin{aligned}
K_n(o,m,u)
={}&
\frac{n\binom o2u}{n-2}\\
&+\frac{\lambda_n}{n(n-1)}
 o\left[(n-1)mu+n\binom u2\right]\\
&+\frac{\lambda_n}{n(n-1)(n-2)}
\left[(n-2)\binom m2u+(n-1)m\binom u2+n\binom u3\right].
\end{aligned}
\]

### Theorem CMR1370 -- PROVED

The sum, over all `e in M`, of the CMR1362 expected-new-credit upper bounds is
exactly

\[
\boxed{
\sum_LK_n(o_L,m_L,u_L).
}
\]

### Proof

Insert CMR1366--CMR1368 into the rank-one coefficient `1/(n-2)` and the
rank-two/rank-three coefficients `lambda_n/(n)_r`, then interchange the finite
sums over cells and lines. ∎

This is an upper bound on expected collateral, not necessarily the exact
expectation.

## Symmetric target-cell criterion

Define the symmetric line kernel

\[
\mathcal K_n(o,m,u)
=K_n(o,m,u)+K_n(m,o,u).
\]

### Theorem CMR1371 -- PROVED

If

\[
\boxed{
\sum_L\mathcal K_n(o_L,m_L,u_L)
<
3\Phi(S),
}
\]

then some selected target cell in one of the two layers has an extension-free
response state of strictly smaller potential.

At a positive minimum, the reverse weak inequality is necessary.

### Proof

The left side bounds the sum of expected new collateral over all `2n` selected
cell banks.  The exact sum of destroyed target incidences is `3Phi(S)` by
CMR1369.  If the total new upper bound is smaller, at least one cell has expected
new collateral below its destroyed load.  Some response in that bank improves.
The minimum statement is the contrapositive. ∎

This is the first complete linewise target-versus-collateral inequality for all
extension-free target cells simultaneously.

## Independent linewise domination is false

### Theorem CMR1372 -- PROVED BY EXPLICIT STANDARD-GRID EXAMPLE

The inequality

\[
\mathcal K_n(o,m,u)<3\binom{o+m}{3}
\]

does not hold for every realizable line composition.

At `n=5`, take

\[
M=(0,1,2,4,3),
\qquad
O=(1,3,4,0,2).
\]

The main diagonal has composition

\[
(o,m,u)=(0,3,2).
\]

For this line,

\[
\boxed{
\mathcal K_5(0,3,2)=\frac{160}{11}>3.
}
\]

The complete state has one further selected target line of composition `(1,2,0)`;
its kernel is zero.  Hence the total independent-line upper kernel is `160/11`,
while

\[
3\Phi(S)=6.
\]

### Proof

The two displayed permutations are disjoint.  Direct determinant enumeration
gives exactly the two stated target lines.  Substitute `D_5=44` and
`lambda_5=40/11` into CMR1370. ∎

This does not show that the state lacks an improving response.  It shows that
the present independent-line upper relaxation is too coarse to prove one.

## Line-composition endpoint

### Corollary CMR1373 -- PROVED

The global target-versus-collateral problem for extension-free banks now has an
exact composition-level form:

1. all candidate counts summed over target cells have closed line formulas;
2. destroyed target incidence is the exact symmetric cubic line count;
3. a strict global kernel inequality gives an improving response;
4. a positive minimum must violate that strict inequality;
5. pointwise line domination fails even on a realizable `5 x 5` state.

Therefore the next genuine improvement must exploit correlation between lines,
primitive-height distribution, shared response edges, row/column assignment, or
carry/prefix structure.  Pair moments and independent band maxima alone cannot
close the diagonal block.  No all-`n` theorem is claimed.

The line sums, target incidences, symmetric criterion and explicit obstruction
are checked in
[`scripts/verify_prime_power_extension_free_line_kernel.py`](../scripts/verify_prime_power_extension_free_line_kernel.py).
