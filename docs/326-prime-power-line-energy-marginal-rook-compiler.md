# Line-energy coefficients compile into exact response marginals

CMR1766--CMR1773 give the exact line-energy profile of one response set, while
CMR1774--CMR1781 require that geometry be computed in each exact geometric fibre.
This chapter converts that profile into a finite response-law row.

The rank-one part is an ordinary bipartite assignment score. The rank-two and
rank-three parts are exact joint prescription marginals and are computed by the
same rook contractions already used for line-clean responses. Thus one geometric
fibre has a fully explicit rational or integer strict-improvement certificate.

Let `B` be a fixed background point set and let `G` be a bipartite response host
of side `d` embedded in the standard grid. Let `nu` be any probability law on a
nonempty family of perfect matchings of `G`.

For a compatible response prescription `P`, write

\[
p(P)=\Pr_{Q\sim\nu}(P\subseteq Q).
\]

## 1. Exact geometric prescription coefficients

For one allowed response point `x`, define

\[
a_1(x)
=
\sum_{\ell\ni x}C(|B\cap\ell|,2).
\]

For a compatible response pair `P={x,y}`, define

\[
a_2(P)=|B\cap\ell(x,y)|.
\]

For a compatible response triple `P`, define

\[
a_3(P)=
\begin{cases}
1,&P\text{ is collinear},\\
0,&P\text{ is not collinear}.
\end{cases}
\]

### Theorem CMR1782 -- PROVED

For every response perfect matching `Q`,

\[
\boxed{
\Psi(B\cup Q)-\Psi(B)
=
\sum_{x\in Q}a_1(x)
+
\sum_{P\in C(Q,2)}a_2(P)
+
\sum_{P\in C(Q,3)}a_3(P).
}
\]

### Proof

The first coefficient counts background pairs collinear with one selected
response point, the second counts background points collinear with one selected
response pair, and the third detects a collinear response triple. These are the
three terms of the linewise identity CMR1766, regrouped by response
prescription. Every collinear triple has one unique response prescription. ∎

This is the prescription form of the exact line-energy census.

## 2. Exact response-law expectation

### Theorem CMR1783 -- PROVED

\[
\boxed{
\mathbb E_{Q\sim\nu}
\bigl[\Psi(B\cup Q)-\Psi(B)\bigr]
=
\sum_x a_1(x)p(\{x\})
+
\sum_{|P|=2}a_2(P)p(P)
+
\sum_{|P|=3}a_3(P)p(P).
}
\]

### Proof

Take expectation in CMR1782 and interchange each finite sum with expectation.
The expected indicator of `P subseteq Q` is `p(P)`. ∎

No independence between response edges is used.

## 3. Corrected genuinely-new domination

Let `N_new(B,Q)` be any corrected family of genuinely new recurrent triples
created by the response.

### Theorem CMR1784 -- PROVED

\[
\boxed{
\mathbb E N_{\mathrm{new}}(B,Q)
\le
\sum_x a_1(x)p(\{x\})
+
\sum_{|P|=2}a_2(P)p(P)
+
\sum_{|P|=3}a_3(P)p(P).
}
\]

Equality holds when every triple containing a response point is genuinely new and
retained.

### Proof

CMR1768 gives response-wise domination by the complete line energy. Take
expectation and apply CMR1783. ∎

Thus the displayed rational row is always an honest upper row.

## 4. Rank-one assignment certificate

Put

\[
A_1(\nu)=\sum_xa_1(x)p(\{x\}).
\]

The rank-one marginal matrix `p(x)` is doubly stochastic on the response host.

### Theorem CMR1785 -- PROVED

\[
\boxed{
A_1(\nu)
\le
\max_{Q\in\operatorname{PM}(G)}\sum_{x\in Q}a_1(x).
}
\]

Equivalently, every assignment dual satisfying

\[
u_i+v_j\ge a_1(i,j)
\]

on allowed cells certifies

\[
\boxed{A_1(\nu)\le\sum_i u_i+\sum_j v_j.}
\]

The superlevel cover compilers of CMR1630--CMR1637 and CMR1670--CMR1677 apply
directly to the score `a_1`.

### Proof

The marginal matrix is a convex combination of perfect-matching incidence
matrices. A linear score is at most its maximum on an extreme response matching.
The dual statement is ordinary bipartite assignment duality. ∎

Pair-only and background-triple-shadow components of `a_1` may be covered
separately before their vertex weights are combined.

## 5. Rank-two and rank-three marginal rows

Define

\[
A_2(\nu)=\sum_{|P|=2}a_2(P)p(P),
\qquad
A_3(\nu)=\sum_{|P|=3}a_3(P)p(P).
\]

### Theorem CMR1786 -- PROVED

1. `A_2(nu)` is the expected number of triples with two response points and one
   background point.
2. `A_3(nu)=E Psi(Q)` is the expected number of collinear response triples.
3. The coarse rank-mass bounds are
   \[
   \boxed{
   A_2(\nu)
   \le
   \left(\max_{|P|=2}a_2(P)\right)C(d,2),
   }
   \]
   and
   \[
   \boxed{A_3(\nu)\le C(d,3).}
   \]
4. Exact classwise or rook-marginal sums may replace these maxima.

### Proof

The first two statements are the corresponding terms of CMR1783. For part three,
use the exact distinct-prescription rank masses of CMR1702 and the nonnegative
coefficient maxima. Part four is immediate from the exact definitions. ∎

When every supported response is triple-free, `A_3(nu)=0` exactly.

## 6. Charged coefficient alternative

For an allowed response point `x`, let

\[
c_1(x)=S_2(x)+3T_3(x),
\]

using CMR1751. For a response pair on a line containing `h` background points,
put

\[
c_2(P)=2+C(h,3).
\]

Put `c_3=a_3`.

### Theorem CMR1787 -- PROVED

\[
\boxed{
a_1(x)\le c_1(x),
\qquad
a_2(P)\le c_2(P),
\qquad
a_3(P)=c_3(P).}
\]

Consequently the expectation in CMR1784 is bounded by the same marginal formula
with `a_r` replaced by `c_r`.

### Proof

The first two inequalities are CMR1751--CMR1752, and the third is the definition.
Multiply by nonnegative prescription probabilities and sum. ∎

The charged version exposes current background-triple currency and pair-only or
low-slot residuals explicitly.

## 7. Exact uniform rook numerator

Assume the response law is uniform on the perfect matchings of

\[
G=K_{d,d}\setminus F,
\qquad
Z=N_d(F)>0.
\]

For a compatible rank-`r` prescription `P`, put

\[
z(P)=N_{d-r}(F/P).
\]

### Theorem CMR1788 -- PROVED

The exact uncorrected line-energy numerator is

\[
\boxed{
A_{\mathrm{line}}
=
\sum_x a_1(x)z(\{x\})
+
\sum_{|P|=2}a_2(P)z(P)
+
\sum_{|P|=3}a_3(P)z(P).
}
\]

Moreover

\[
\boxed{
\mathbb E[\Psi(B\cup Q)-\Psi(B)]
=
A_{\mathrm{line}}/Z.
}
\]

Every term is an integer computable by the component-rook contractions of
CMR1526--CMR1533.

### Proof

CMR1531 gives `p(P)=z(P)/Z`. Substitute these exact probabilities into
CMR1783 and clear the common denominator. ∎

The numerator must be computed separately in every exact geometric fibre of
CMR1778.

## 8. Hybrid strict-improvement certificate

Let `D` be the destroyed current load. Let `U_1` be any proved upper bound for
the rank-one assignment term, and let `U_2,U_3` be exact or upper bounds for the
rank-two and rank-three marginal terms.

### Corollary CMR1789 -- PROVED

If

\[
\boxed{U_1+U_2+U_3<D,}
\]

then at least one response has strictly smaller potential.

For the uniform law, the exact integer condition

\[
\boxed{A_{\mathrm{line}}<ZD}
\]

is sufficient. The same conclusion holds with corrected-row numerators in place
of the complete line-energy numerator.

### Proof

CMR1784 bounds expected genuinely new collateral by `U_1+U_2+U_3`. If this is
below the destroyed load, the expected post-response potential is below the
current potential, so some finite response is strictly better. The integer form
is CMR1788 after denominator clearing. ∎

The current numerical frontier is now explicit: certify the rank-one assignment
score and compute or bound the exact rank-two/rank-three rook marginals in each
geometric fibre. No all-`n` theorem is claimed.

Exact coefficient identities, response-law marginals, assignment bounds,
charged coefficients and integer rook numerators are checked in
[`scripts/verify_prime_power_line_energy_marginal_rook_compiler.py`](../scripts/verify_prime_power_line_energy_marginal_rook_compiler.py).
