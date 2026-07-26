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

The proved chain has finite canonical forms for inherited banks, Hall walls,
closure envelopes, rollback, exchange-SCC and protected/free products,
minimum-core contraction, selected routing, target handoff, loaded-line and
star banks, blocker covers, small full-grid bases and owner-labelled
restoration ancestry.

Last-entering ownership makes the complete owner matrix block upper triangular:

\[
\rho(A)=\max_i\rho(A_{ii}).
\]

Only same-owner diagonal blocks require subcritical certificates.

## 3. Exact probability and assignment law

For response side `d`, target `e` and opposite matching `O`, use

\[
H_e=K_{d,d}\setminus(O\cup\{e\}).
\]

Every compatible prescription has an exact finite rook class, and every
candidate triple has one fixed entering owner before sampling.  Therefore

\[
\mathbb E N(R)=\sum_ap_e(a)g_e(a),
\]

where `p_e(x,y)` is doubly stochastic.  Expected collateral is one bipartite
assignment cost with an exact rational dual.  Every owner weight is a finite
geometric/rook dot product, so perfect-matching enumeration is unnecessary.

## 4. Inherited-coordinate capacity

Keep separate:

- response matching side `d`;
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

Then

\[
\gamma_e(a,R)
\le\frac12\sum_{b\in E_a(R)}c_\omega(h(a,b)).
\]

Exact pair rook probabilities yield a conditional eligible owner envelope.
Directions above `W_omega/2` have zero capacity.

## 5. Prime-power signature banks

Inside envelope `p^k`, every eligible pair has one signature

\[
(t_{\rm pair},s,\delta,H),
\]

where `s` is first-separation depth, `delta` projective direction and `H`
primitive-height band.  Put

\[
B_\omega=1+\lfloor\log_2\max\{1,W_\omega\}\rfloor.
\]

At most `2k(p+1)B_omega` classes occur for one owner.  A heavy owner class is
simultaneously realized and concentrates on one loaded line.

A global fractional obstruction contains an exact-displacement class of mass
at least

\[
M_0=
\frac{d-2}
{6k(p+1)B_\omega D_p(H)S_{\omega,p}(s,H)},
\]

with

\[
D_p(H)=(p-1)\left\lceil\frac{4H}{p}\right\rceil^2,
\qquad
S_{\omega,p}(s,H)=
\left\lfloor\frac{W_\omega}{p^sH}\right\rfloor.
\]

This class is a bank of parallel translated owner-partner pairs with one exact
lattice displacement.

## 6. Weighted carry routing

Every exact-displacement pair lies in one depth-`s` full prefix cell.  One of
the `p^{2s}` cells carries mass at least `M_0/p^{2s}`.  Routing the third cell
of each candidate gives:

1. an internal bank of mass at least
   \[
   M_0/(2p^{2s})
   \]
   which scales to a strict envelope `p^{k-s}` when `s>=1`;
2. a crossing bank with one common earlier exit depth and mass at least
   \[
   M_0/(2sp^{2s})
   \]
   when `s>=1`;
3. the depth-zero parent-scale exact-displacement branch.

For fixed owner stage, layer, depth, direction and displacement, there are
exactly `p^{2s}` full-cell tokens.  Repeated banks either consume fresh tokens
or concentrate on one exact absolute token.

## 7. Private path and blocker payment

For one fixed nonzero displacement, the translation support

\[
a\longmapsto a+\Delta
\]

is a finite path forest.  Alternating the path edges extracts at least half the
packed mass on endpoint-disjoint pairs.  Their residual supports are pairwise
disjoint, so any blocker meeting all extracted pairs must spend one distinct
response edge per pair.

Applied after CMR1470--CMR1477, the routed branches contain at least

\[
\left\lceil\frac{M_0}{4p^{2s}}\right\rceil,
\qquad
\left\lceil\frac{M_0}{4sp^{2s}}\right\rceil,
\qquad
\left\lceil\frac{M_0}{2}\right\rceil
\]

private translated pairs in the internal, earlier-exit and depth-zero branches,
respectively.  The middle count applies for `s>=1`.

At nonroot depth, these pairs partition exactly by full-prefix token.  They
therefore give either:

- one token carrying many private identical-displacement pairs; or
- many token-disjoint private witnesses.

This is a genuine protected-reserve currency: one common residual edge cannot
neutralize the whole translated bank.

## 8. Genuine remaining inequality

The remaining prime-power theorem must assign strict weighted payment to:

- internal envelope scaling;
- earlier-depth crossing transfer;
- private residual-edge or token consumption;
- depth-zero translated pairs;
- repeated absolute full-cell tokens;
- and the alternative one-owner loaded-line response.

The existing prefix-return, quotient/carry collision, protected-reserve,
loaded-line and token machinery supplies the structural actions.  What is
missing is a single weight assignment proving

\[
Av<v.
\]

## 9. Recommended next lemmas

1. **Private-reserve Lyapunov weight.**  Compare one unit of endpoint-disjoint
   residual blocker cost with destroyed parent credit and protected-reserve
   depletion.
2. **Depth-transfer Lyapunov weight.**  Choose weights decreasing under strict
   internal scaling and earlier exit depth.
3. **Depth-zero translation payment.**  Show the private parent-scale bank
   forces many quotient/carry cells, permanent mask depletion or one recurrent
   token-bearing edge.
4. **Repeated-token response.**  Convert repeated use of one absolute full-cell
   token into prefix return, contraction or target-load decrease.
5. **Packed-versus-loaded comparison.**  Combine the global private translated
   payment with the one-owner loaded-line gain without double counting.
6. **Exact diagonal certificate.**  Export the final inequalities as a
   rational/integer `Av<v` certificate.
7. **Prime-field, thin and CRT endpoints.**  Prove the remaining diagonal blocks
   and glue them through owner triangularity.

## 10. Computational priorities

- Enumerate exact depth-transfer and private-reserve offspring vectors.
- Search rational weights by depth, envelope side, partner type and token state.
- Measure depth-zero translation multiplicity in quotient/carry cells.
- Compare private blocker histories with stored protected-reserve and
  prefix-return ledgers.
- Test prime-field and thin diagonal blocks before CRT gluing.

## 11. Current proved endpoint

Through **CMR1485**:

- exact rook probabilities and owner weights are known;
- collateral is one shared-edge assignment cost;
- lattice capacity is valid for scattered inherited factors;
- one-owner and global packed signatures have quantitative lower bounds;
- exact-displacement banks route to strict scaling, earlier exit depth, depth
  zero or finite absolute-token reuse;
- every routed branch also contains an endpoint-disjoint private translated
  subbank with linear residual-blocker cost.

There is still no complete proof.  The next genuine advance is the Lyapunov
comparison of private reserve consumption and strict depth transfer with the
parent credit weight.
