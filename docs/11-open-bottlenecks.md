# Open bottlenecks and research roadmap

## 1. Current proof status

The no-three-in-line conjecture remains open.  The branch has exact structural,
matching-bank and inherited-coordinate reductions, but no theorem yet proves
that every positive minimum of the real-triple potential becomes zero.

The decisive honesty correction remains:

> finite response and structural descent are not potential improvement.

A completion must exhibit an actual lower-potential response or an exact
weighted inequality guaranteeing one.

## 2. Structurally closed components

The proved chain contains finite canonical forms for inherited banks, Hall
walls, closure envelopes, rollback, exchange-SCC and protected/free products,
minimum-core contraction, selected routing, target handoff, loaded-line and
star banks, blocker covers, small full-grid bases and owner-labelled restoration
ancestry.

Last-entering ownership makes the complete owner matrix block upper triangular:

\[
\rho(A)=\max_i\rho(A_{ii}).
\]

Only same-owner diagonal blocks require subcritical certificates.

## 3. Exact same-owner probability and assignment law

For response side `d`, target `e` and opposite matching `O`, use

\[
H_e=K_{d,d}\setminus(O\cup\{e\}).
\]

After normalizing `O`, every compatible prescription has a finite exact rook
class.  Its completion count and probability are

\[
B_d(P)=
\sum_{j=0}^{d-r}(-1)^j
\left[\binom qj+\varepsilon\binom{q-d_0}{j-1}\right](d-r-j)!,
\]

\[
\Pr(P\subseteq R)=
\frac{B_d(P)}{D_d(d-2)/(d-1)}.
\]

Every candidate triple has a fixed entering owner before sampling.  Therefore

\[
\mathbb E N(R)=\sum_ap_e(a)g_e(a),
\]

where the marginal matrix `p_e(x,y)` is doubly stochastic.  Expected collateral
is one bipartite assignment cost with exact rational dual.  Every owner weight
is itself a finite geometric/rook dot product, so no perfect-matching
enumeration is needed.

## 4. Inherited-coordinate capacity

A residual matching factor may use scattered coordinates.  Keep separate:

- matching side `d`;
- prime-power envelope side `t=p^k`;
- coordinate span
  \[
  W_\omega=\max\{x_{\max}-x_{\min},y_{\max}-y_{\min}\}.
  \]

For primitive height `h`, define

\[
c_\omega(h)=
\max\left\{\left\lfloor\frac{W_\omega}{h}\right\rfloor-1,0\right\}.
\]

The exact owner-line reduction is

\[
\gamma_e(a,R)
\le\frac12\sum_{b\in E_a(R)}c_\omega(h(a,b)).
\]

Using exact pair rook probabilities gives a conditional eligible envelope
`Gamma_e^{elig}(a)` with `g_e(a)<=Gamma_e^{elig}(a)`.  Directions of height
above `W_omega/2` contribute zero.

## 5. One-owner prime-power signatures

Inside envelope `p^k`, every eligible pair has one signature

\[
(t_{\rm pair},s,\delta,H),
\]

where `s` is first-separation depth, `delta` projective direction modulo `p`,
and `H` a dyadic primitive-height band.  With

\[
B_\omega=1+\lfloor\log_2\max\{1,W_\omega\}\rfloor,
\]

there are at most

\[
2k(p+1)B_\omega
\]

classes for one owner.  A heavy eligible envelope forces one heavy class; some
actual response realizes at least its ceiling mean.  A direction stock bound
then concentrates that simultaneous class on one loaded real line through the
owner.

## 6. Global fractional exact-displacement bank

For a feasible candidate packing `z_T`, put `nu=sum_T z_T`.  The total packed
eligible partner incidence is exactly `2nu`.  At a positive minimum,
matching preclusion gives

\[
\nu\ge\frac{d-2}{3}.
\]

Hence one signature has packed mass at least

\[
\boxed{
\mu_\sigma\ge
\frac{d-2}{3k(p+1)B_\omega}.}
\]

This mass is dispersed over at least `ceil(mu_sigma)` ordered owner-partner
pairs and at least `ceil(mu_sigma/2)` owners.  In the response-partner branch,
it also uses at least `ceil(mu_sigma)` distinct response edges.

For

\[
D_p(H)=(p-1)\left\lceil\frac{4H}{p}\right\rceil^2,
\qquad
S_{\omega,p}(s,H)=
\left\lfloor\frac{W_\omega}{p^sH}\right\rfloor,
\]

one exact displacement class has mass at least

\[
\boxed{
\frac{d-2}
{6k(p+1)B_\omega D_p(H)S_{\omega,p}(s,H)}.}
\]

Thus the global obstruction contains a bank of parallel translated pairs with
one depth, projective direction, height band and exact lattice displacement.

## 7. Genuine remaining inequality

The remaining prime-power theorem must compare two canonical outputs:

1. the one-owner loaded-line/carry-cell class forced by CMR1458--CMR1461;
2. the many-owner exact-displacement translation bank forced by CMR1469.

The existing prefix-return, quotient/carry collision, protected-reserve,
loaded-line and token machinery supplies possible payments.  What is missing is
a weight assignment proving that at least one payment makes the same-owner
offspring row strictly subcritical:

\[
Av<v.
\]

## 8. Recommended next lemmas

1. **Exact-displacement prefix payment.**  Show that a bank of translated pairs
   with displacement `mq` either consumes many distinct prefix/carry cells or
   repeats one token-bearing cell beyond its finite capacity.
2. **Packed-versus-loaded comparison.**  Relate dispersed CMR1469 mass to the
   one-owner loaded-line gain, avoiding duplicate payment of one response edge.
3. **Carry-cell Lyapunov weights.**  Choose weights by first-separation depth,
   prefix occupancy, partner type and height band.
4. **Exact diagonal certificate.**  Prove a rational/integer `Av<v` system for
   the resulting finite rows.
5. **Prime-field and thin blocks.**  Replace missing nonroot depth with direct
   finite direction and line-distribution certificates.
6. **CRT assembly.**  Retain collision/local-line types and glue through owner
   triangularity.

## 9. Computational priorities

- Enumerate exact owner/rook/signature offspring vectors in inherited
  coordinates.
- Solve rational linear programs and export strict integer certificates.
- Measure prefix/carry-cell multiplicity for exact displacement banks.
- Compare packed translated-bank mass with protected-line absorption gain.
- Test prime-field and thin diagonal blocks independently before CRT gluing.

## 10. Current proved endpoint

Through **CMR1469**:

- prescription probabilities and host penalties are exact rook-class sums;
- collateral is one shared-edge assignment cost;
- owner weights have exact geometric/rook histograms;
- lattice capacity is valid for scattered inherited factors;
- one-owner heavy signatures concentrate on loaded lines;
- global fractional obstructions contain exact-displacement translation banks.

There is still no complete proof.  The next genuine advance is a quantitative
prefix/carry or protected-reserve payment for the CMR1469 bank and its
conversion into a subcritical same-owner certificate.
