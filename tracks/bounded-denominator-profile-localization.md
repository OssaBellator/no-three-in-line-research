# Finite-profile localization of failed product banks

BDA3b reduces a compatible family of local chamber banks to one explicit
normalized collateral sum. This note makes the failure alternative
local: once the \(q\)-stripe arithmetic supplies finitely many profile
labels, one profile alone carries a quantified share of the obstruction.

Retain the notation of BDA3b and put

\[
K(T)=\prod_{i=1}^s\kappa_i(r_i(T)).
\]

Let

\[
\sigma:\mathcal T\longrightarrow\Sigma
\]

be any finite profile map, with \(1\leq|\Sigma|=L<\infty\). The profile
may record the \(q\)-strip residues, block-rank pattern, carry labels,
wrap-index type, and any bounded channel data. For \(\alpha\in\Sigma\)
define

\[
\mathcal C_\alpha
=
\sum_{\substack{T\in\mathcal T\\\sigma(T)=\alpha}}
w(T)K(T).
\]

## BDA3c -- failed-bank profile localization

### Lemma BDA3c -- PROVED

The profile sums satisfy

\[
\mathcal C=\sum_{\alpha\in\Sigma}\mathcal C_\alpha.
\]

If the BDA3b sufficient improvement inequality fails, so that

\[
W\leq F+\mathcal C,
\]

then some profile \(\alpha\) satisfies

\[
\boxed{
\mathcal C_\alpha
\geq
\frac{(W-F)_+}{L}.
}
\]

For that profile, set

\[
K_\alpha
=
\max_{\sigma(T)=\alpha}K(T).
\]

Whenever \(\mathcal C_\alpha>0\), the profile is nonempty,
\(K_\alpha>0\), and its unnormalized candidate weight obeys

\[
\boxed{
\sum_{\sigma(T)=\alpha}w(T)
\geq
\frac{\mathcal C_\alpha}{K_\alpha}
\geq
\frac{(W-F)_+}{L K_\alpha}.
}
\]

### Proof

The fibres of \(\sigma\) partition \(\mathcal T\), giving the first
identity. Failure of the improvement inequality gives

\[
\sum_{\alpha\in\Sigma}\mathcal C_\alpha
=\mathcal C\geq W-F.
\]

If \(W\leq F\), the first displayed lower bound is zero and is immediate.
Otherwise a largest one of the \(L\) nonnegative profile sums is at least
\((W-F)/L\).

Finally, \(K(T)\leq K_\alpha\) throughout the selected fibre, so

\[
\mathcal C_\alpha
\leq
K_\alpha\sum_{\sigma(T)=\alpha}w(T).
\]

Rearranging proves the raw-weight bound. \(\square\)

## BDA3d -- six rank-pattern alternatives

Move every certificate with \(r_i(T)=0\) for all selected blocks into the
fixed collateral \(F\). Every remaining triple has one of exactly six
positive block-rank patterns:

\[
\boxed{
(1),\ (2),\ (1,1),\ (3),\ (2,1),\ (1,1,1).
}
\]

### Corollary BDA3d -- PROVED

If \(W>F\) and the BDA3b improvement inequality fails, one of these six
patterns carries normalized collateral at least

\[
\boxed{\frac{W-F}{6}.}
\]

Within the six cases the normalized factors have, respectively, the
forms

\[
\frac{128}{t_i},\qquad
\frac{128}{(t_i)_2},\qquad
\frac{128^2}{t_it_j},\qquad
\frac{128}{(t_i)_3},\qquad
\frac{128^2}{(t_i)_2t_j},\qquad
\frac{128^3}{t_it_jt_k},
\]

with distinct block indices where more than one occurs.

### Proof

The positive entries among \((r_1(T),\ldots,r_s(T))\) form an integer
partition of a number in \(\{1,2,3\}\), giving exactly the displayed six
patterns. Apply BDA3c with this six-element profile map and substitute
the definition of \(\kappa_i(r)\). \(\square\)

Thus the unresolved \(q\)-arithmetic may be treated separately for
one-block, two-block, and three-block collateral; failure cannot require
a cancellation or mixture among all of them.

## Interface to the \(q\)-stripe classification

For fixed \(q\), suppose the remaining chamber arithmetic proves that all
possible collateral triples admit a profile map with
\(|\Sigma|\leq L_q\). Then every failed improving bank with \(W>F\)
returns one explicit profile carrying normalized collateral at least

\[
\frac{W-F}{L_q}.
\]

If the profile also fixes its block-rank factors, \(K_\alpha\) is
explicit, and the second boxed inequality converts this into a raw
candidate-weight lower bound. This is the exact input expected by BDA4:
the classification need only treat one heavy residue/carry/rank profile,
not a mixture of all collateral types.

BDA3c does not itself prove that \(L_q=O_q(1)\). Establishing that finite
\(q\)-profile theorem, and showing that each resulting heavy profile is
periodic or absorbable, remain the arithmetic parts of BDA3--BDA4.

`scripts/verify_bda_profile_localization.py` exhaustively checks the
partition, normalized pigeonhole bound, raw-weight conversion, and six
positive rank patterns for small rational instances.
