# Open bottlenecks and research roadmap

## 1. Current proof status

The no-three-in-line conjecture remains open. The branch now has exact
structural reductions, response laws, return and line-clean certificate forms,
selector capacity compilers, prime-field support normal forms, a complete
matching-level thin census through residual rank three on sides four and five,
multiplicity-aware rank-mass bounds, owner-support closures and a label-
preserving auxiliary/CRT assembly protocol.

No theorem yet proves that every positive minimum of the real-triple potential
becomes zero.

The honesty condition is unchanged:

> finite response, finite resource use and structural descent are not by
> themselves potential improvement.

A completion must exhibit a lower-potential response or an exact weighted
inequality guaranteeing one.

## 2. Closed structural components

Last-entering ownership makes the complete offspring matrix block upper
triangular after retaining all labels needed to determine future rows:

\[
\rho(A)=\max_i\rho(A_{ii}).
\]

Strict child descent, earlier-depth transfer, first private-edge/token/
restoration/support/signature use and ordinary later-owner exits are off-diagonal
only when the selected policy executes them. All finite transfer collateral
glues after the genuinely recurrent labelled blocks are certified.

The broad labels “loaded line”, “repeated token”, “diffuse selector”, “root
translation”, “fixed trace” and “return churn” are no longer primitive undefined
rows in the regimes already reduced.

## 3. Exact response and line-clean rows

For response side `d`, opposite matching `O` and target `e`, use

\[
H_e=K_{d,d}\setminus(O\cup\{e\}).
\]

Every compatible prescription has an exact rook probability and every genuinely
new candidate has one canonical last-entering owner. Deleting the complete
allowed trace of a nonaxis line preserves a target-avoiding response for `d>=4`
and creates no new collateral on that line.

For deleted trace `X`,

\[
F=O\cup X\cup\{e\},
\qquad
D_0=O\cup X,
\]

and

\[
\mathcal R_F(z)
=
\mathcal R_{D_0}(z)+z\mathcal R_{D_0-u-v}(z).
\]

Every response denominator and contracted prescription probability is therefore
an exact integer rook computation.

## 4. Exact, universal and classwise line-clean budgets

Define

\[
W_d
=(d-1)(d-2)V_1+(d-2)V_2+V_3+(m+1)b(d-1)(d-2).
\]

For line-clean fractional factor `q=u/v` and destroyed target load `D`, strict
improvement is exactly

\[
(dv)^dW_d<D u^d d(d-1)(d-2).
\]

The three permanent ratios are increasing for `d>=4`, giving universal floors

\[
1/16,
\qquad
81/4096,
\qquad
1/256.
\]

Hence the universal automatic budgets are

\[
\lceil D(d)_3/16\rceil-1,
\qquad
\lceil 81D(d)_3/4096\rceil-1,
\qquad
\lceil D(d)_3/256\rceil-1.
\]

Exact rank/profile/geometric capacities compile into

\[
\widehat W
=
\sum_\chi c_{r(\chi)}C_\chi
+(m+1)B(d-1)(d-2),
\]

with

\[
c_1=(d-1)(d-2),
\qquad c_2=d-2,
\qquad c_3=1.
\]

If `widehat W` fits an exact or universal budget, the whole class family has one
positive integer slack. Failure forces one candidate or unavailable-edge class
above an explicit overflow threshold. Rooted-target traces require only the
strong and singleton budgets.

## 5. Multiplicity-aware rank mass

For every response law and rank `r`, the total probability mass of **distinct**
rank-`r` prescriptions is

\[
\sum_{P:\operatorname{rank}P=r}\Pr(P\subseteq Q)=C(d,r).
\]

A geometric row may contain several candidate triples sharing one response
prescription. Let `m(P)` be that multiplicity and let `m_r` be the maximum
multiplicity in rank `r`. Then

\[
\mathbb E N_{\mathrm{off}}
\le
\sum_{r=1}^3m_r C(d,r).
\]

After removing `F_r` forced common prescriptions,

\[
\mathbb E N_{\mathrm{off}}
\le
\sum_{r=1}^3m_r\bigl(C(d,r)-F_r\bigr).
\]

Thus every actual nonempty line-clean host closes whenever destroyed load exceeds
this multiplicity-corrected mass. The explicit threshold

\[
(d^3+5d)/6+1
\]

is valid only for injective candidate families. The next geometric line-clean
work must therefore bound prescription multiplicities, not merely distinct
prescription counts.

## 6. Shared return-selector assignment and class covers

For selector restoration cap `T`, use one score

\[
h_T=g_{\mathrm{ret}}+Tg_{\mathrm{sel}}.
\]

A rational assignment dual below one certifies the complete return-selector
block. For positive levels `tau_j`, put

\[
E_j=\{a:h_T(a)\ge\tau_j\}.
\]

Then

\[
\max_Q\sum_{a\in Q}h_T(a)
\le
\sum_j(\tau_j-\tau_{j-1})\nu(E_j).
\]

Every matching number has an equal-size source/target vertex cover by Konig's
theorem. If class `s` has score cap `H_s` and cover `C_s`, nested threshold
covers give the feasible dual objective

\[
\sum_{z\in L\cup R}\max\{H_s:z\in C_s\}.
\]

An objective below one, or its denominator-cleared integer form, certifies the
coupled block. Alternative source-row and target-column covers may be optimized
jointly as a finite set-cover problem.

## 7. Owner-support capacities and strict closures

Let `A` be an exact possible-owner edge support and let `mu(A)` be its matching
number. Distinct rank-`r` prescriptions canonically owned in `A` have total mass
at most

\[
\mu(A)C(d-1,r-1).
\]

A source/target cover of size `k` may replace `mu(A)` by `k`. With rankwise
prescription multiplicity caps `m_r`, expected new owned collateral is at most

\[
\mu(A)\sum_{r=1}^3m_r C(d-1,r-1).
\]

If every retained child owner lies in `A`, destruction above this quantity gives
a strict response. If the certificate fails, one rankwise multiplicity is at
least the explicit CMR1732 overflow threshold.

Prime-field reused-support states have support size one or two. They enter this
closure when every retained child owner lies in the fixed terminal support;
response reintroductions already routed through the return kernel are not counted
again.

## 8. Critical-selector capacity compiler

For one exact selector host, write

\[
A_L=\sum_\chi a_\chi/D
\]

and prove class capacities `a_chi<=C_chi`. Put `C=sum C_chi`. If `C<D`,
criticality is impossible and the selector has gap

\[
\eta=(D-C)/D
\]

with exact restoration cap

\[
T_C
=
\left\lfloor
D[2(n-1)+B]/((n-1)(D-C))
\right\rfloor.
\]

The resulting selector feeds the shared score `h_{T_C}`. If `C>=D`, only exact
classes meeting the necessary capacity threshold require sharper enumeration.
Exact rook numerators, side-four/five caps, distinct rank mass, owner support and
candidate multiplicities are simultaneous constraints.

## 9. Prime-field, fixed-interface and auxiliary endpoint

For exponent `k>=2`, root-channel normalization enters a strict child factor. At
`k=1`, every root channel is one ordered pair with support size one or two. First
support use is finite resource; recurrence is reused support, returned-edge
currency or one exact fixed-interface prescription.

Every fixed-interface response row is rational with exact contracted rook
probabilities. For every fixed thin-side cap, the complete table is finite and
integer-certifiable.

If an auxiliary recurrent table `D` has already been certified, then

\[
R_D=(I-D)^{-1}\ge0
\]

and

\[
\rho\begin{pmatrix}A&B\\C&D\end{pmatrix}<1
\quad\Longleftrightarrow\quad
\rho\bigl(A+B(I-D)^{-1}C\bigr)<1.
\]

The lift is constructive and rational. Certified thin, fixed-interface or
support modules may therefore be removed from the final search through exact
resolvents. Uncertified reused-support modules remain explicit.

## 10. Symmetry-normalized thin response census

Normalize every opposite matching and forbidden target to

\[
(O,e)=(I_d,(0,1)).
\]

The remaining exact stabilizer is `S_{d-2}`. Canonicalize deleted traces,
interface prescriptions and every retained provenance label under this action.
One exact row is computed per orbit and every orbit certificate lifts to the
fully labelled table.

The exhaustive matching-level census is:

| side | canonical executable hosts | result |
|---:|---:|---|
| 2 | 0 | no extension-free response |
| 3 | 4 | every positive rank-at-most-three prescription is forced and contractible |
| 4 | 45 | nonforced caps `3/4`, `2/3`, `1/2` in ranks one, two, three |
| 5 | 124 | caps `2/3`, `2/5`, `1/4`; no forced positive rank-at-most-three prescriptions |

The side-four rank-three census has 448 extendable instances, 28 forced. The
side-five census has 15,017 rank-three instances, none forced.

The next thin-table work is no longer host or matching-probability discovery. It
is exact geometric offspring enumeration, including multiplicity and absolute
owner data, on the 169 canonical side-four/five hosts.

## 11. Genuine recurrent modules

The labelled diagonal quotient now needs certificates only for:

1. **Return-selector assignment blocks.** One shared score `h_T`, preferably
   certified by class-supported owner covers.
2. **Line-clean low-load/high-multiplicity blocks.** Rows not closed by exact,
   universal or multiplicity-aware mass bounds.
3. **Critical-selector survivors.** Exact classes whose combined capacities do
   not yet fall below the response denominator.
4. **Reused-support survivors.** Small-support states not closed because of high
   multiplicity or child owners outside the claimed support.
5. **Canonical fixed-interface/thin blocks.** Geometric offspring rows on
   normalized hosts, until certified and eliminated by the resolvent.
6. **Residual collision/local-line blocks.** States which genuinely recur with
   every owner, factor and CRT label unchanged.

## 12. Recommended next lemmas and computations

1. **Multiplicity lemma for line-clean triples.** Bound the number of off-line
   candidate triples sharing one rank-one, rank-two or rank-three response
   prescription, first by owner/height/token classes and then globally.
2. **Owner-cover lemma for `h_T`.** Prove small source-row/target-column covers and
   classwise multiplicity caps for heavy return/selector score classes.
3. **Selector multiplicity-capacity table.** Combine exact rook numerators,
   side-four/five pointwise caps, distinct rank mass and owner-support bounds, then
   test `D-C`.
4. **Side-four/five geometric offspring census.** Enumerate genuinely new rank-
   one/two/three credits, shared-prescription multiplicities and absolute owners,
   including non-targetable trace incidences.
5. **Auxiliary orbit certificates.** Search strict rational/integer vectors for
   normalized thin and fixed-interface orbit matrices, then replace each certified
   table by `B(I-D)^{-1}C`.
6. **Reused-support survivor kernel.** Apply the one/two-edge closure and retain
   only high-multiplicity or out-of-support states with exact provenance.
7. **Final labelled SCC certificate.** Assemble exact rational rows, publish a
   strict integer Lyapunov vector for every surviving SCC and then apply CRT
   gluing.

## 13. Computational priorities

- Enumerate candidate-to-prescription multiplicities in canonical side-four/five
  hosts.
- Generate exact owner supports, matching numbers and source/target covers.
- Evaluate multiplicity-aware line-clean and small-support integer slacks.
- Compute selector numerator capacities using all simultaneous bounds.
- Certify and eliminate auxiliary orbit tables by exact rational resolvents.
- Retain collision, local-line, owner and CRT labels until honest domination is
  proved.
- Clear all denominators and independently verify every final strict integer row.

## 14. Current proved endpoint

Through **CMR1733**:

- strict transfers and first-use resources are off-diagonal;
- return and subunit-selector recurrence share one assignment score;
- score superlevels compile from geometric class supports into assignment duals;
- line-clean rows have exact/universal budgets and multiplicity-aware large-load
  closure;
- owner-support matching numbers give exact local mass capacities and strict
  small-support closures;
- critical selectors have exact denominator-capacity gap tests;
- prime-field root channels reduce to singleton supports and fixed interfaces;
- matching-level ranks one through three are completely censused through side
  five;
- certified auxiliary modules eliminate by an exact nonnegative resolvent;
- collision and local-line labels have a proved SCC/CRT gluing protocol.

There is still no complete proof. The next genuine advance is to prove geometric
multiplicity and owner-support bounds, fill the canonical offspring tables, and
publish the first complete strict integer recurrent-core certificate.
