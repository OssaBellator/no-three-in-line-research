# Open bottlenecks and research roadmap

## 1. Current proof status

The no-three-in-line conjecture remains open.  The branch has exact structural,
matching-bank, inherited-coordinate, displacement, temporal and line-clean
reductions, but no theorem yet proves that every positive minimum of the real-
triple potential becomes zero.

The honesty condition is unchanged:

> finite response, finite resource use and structural descent are not by
> themselves potential improvement.

A completion must exhibit a lower-potential response or an exact weighted
inequality guaranteeing one.

## 2. Closed structural components

The selected execution has finite canonical forms for inherited banks, Hall
walls, unit-wall products, rollback, exchange-SCC and protected/free products,
selected routing, strict children, fixed-interface lifting, restoration
ancestry, loaded-line/star banks and small-side factors.

Last-entering ownership makes the complete offspring matrix block upper
triangular:

\[
\rho(A)=\max_i\rho(A_{ii}).
\]

Only genuinely recurrent same-owner diagonal blocks need numerical
certificates.  Strict internal scaling, earlier-depth transfer, first use of a
private edge, first use of an absolute token and ordinary structural exits are
off-diagonal and glue after recurrent cores are certified.

## 3. Exact response and packed-displacement law

For response side `d`, opposite matching `O` and target `e`, use

\[
H_e=K_{d,d}\setminus(O\cup\{e\}).
\]

Every compatible prescription has an exact finite rook class and every
candidate has one canonical owner before sampling.  Expected collateral is one
exact bipartite assignment cost with a rational dual.

A positive-minimum fractional obstruction contains one exact-displacement class
of mass at least

\[
M_0=
\frac{d-2}
{6k(p+1)B_\omega D_p(H)S_{\omega,p}(s,H)}.
\]

That bank routes to strict scaling, earlier depth, an absolute token, or a root-
residue channel.  Its translation support contains a large endpoint-disjoint
private subbank.  Loaded-owner and private translated currencies have disjoint
canonical owner support.

## 4. Extension-free line cleaning and exact rook rows

Every nonaxis line is a partial matching.  CMR1510--CMR1517 prove that deleting
its complete allowed trace from `H_e` leaves at least one perfect matching.  The
resulting response still avoids the target and opposite layer, creates no new
line-local collateral, and gives zero same-owner/same-line offspring for a
CMR1461 loaded owner line.

CMR1526--CMR1533 make the remaining off-line response row exact.  If

\[
F=O\cup X\cup\{e\},
\qquad
D=O\cup X,
\]

then `D` decomposes into alternating paths and even cycles, and

\[
\mathcal R_F(z)
=
\mathcal R_D(z)+z\mathcal R_{D-u-v}(z).
\]

Thus

\[
N_d(F)=\sum_j(-1)^jr_j(F)(d-j)!,
\qquad
\Pr(P\subseteq R)=\frac{N_{d-r}(F/P)}{N_d(F)}.
\]

## 5. Three exact line-clean coefficient classes

CMR1534--CMR1557 give a complete uniform coefficient classification.

### Strong derangement-extendable trace

The target-plus-trace partial matching extends to a perfect matching disjoint
from the opposite layer.  The host contains a spanning `(d-2)`-factor and

\[
\kappa_d^{strong}
=
\left(\frac d{d-2}\right)^d.
\]

### Target-disjoint singleton remainder

The target-plus-trace matching leaves one unmatched source and target joined by
the sole residual opposite edge.  The exact optimal fractional factor is

\[
q_{sing}
=d-2-\frac1{d-2}
=
\frac{(d-1)(d-3)}{d-2},
\]

with coefficient

\[
\kappa_d^{sing}
=
\left(
\frac{d(d-2)}{(d-1)(d-3)}
\right)^d.
\]

### Target-endpoint overlap

One trace edge uses an endpoint of the target, giving a vertex of degree `d-3`.
The coefficient is

\[
\kappa_d^{overlap}
=
\left(\frac d{d-3}\right)^d.
\]

These satisfy

\[
\kappa_d^{strong}
<
\kappa_d^{sing}
<
\kappa_d^{overlap}.
\]

For the appropriate coefficient `kappa`,

\[
\mathbb E N_{off}(R)
\le
\kappa
\left[
\frac{V_1^{off}}d
+
\frac{V_2^{off}}{(d)_2}
+
\frac{V_3^{off}}{(d)_3}
\right].
\]

With `b` unavailable allowed edges and current potential `m`,

\[
\kappa
\left[
\frac{V_1^{off}}d
+
\frac{V_2^{off}}{(d)_2}
+
\frac{V_3^{off}}{(d)_3}
+
\frac{(m+1)b}{d}
\right]
<
D_S(e)
\]

forces one feasible lower-potential response.

The line-clean numerical frontier is therefore a three-signature destroyed-
credit comparison.  Exact component rook ratios remain available when a
uniform coefficient is too weak.

## 6. Atomic repeated-token quotient

For one nonroot full token in an envelope `t=p^h`, repeated heavy episodes first
pay finite token-edge stock or identify one recurrent central edge.  Once that
edge is fixed, the pair and trace signature stocks are `(t-1)^2` and `2(t-1)`.

Choose recurrence multiplicity `q` and return threshold `R`, and set

\[
\lambda=2Rq(t-1)^2.
\]

CMR1518--CMR1525 give an explicit five-way alternative:

1. a finite episode bound;
2. at least `R` edge reintroductions with exact full-token incidence
   `R(p+1)(h-1)`;
3. adaptive absorption of the persistent edge;
4. `q` occurrences of one jointly persistent paid-pair selector with surcharge
   two;
5. `q` occurrences of one fixed trace-line or trace-incidence slot.

Repeated-token/reused-support recurrence therefore has only three atomic
numerical rows:

- edge return;
- persistent paid-pair selector;
- fixed trace incidence.

Fresh stock and successful absorption are not independent recurrent classes.

## 7. Genuine recurrent rows

After all closed reductions, the host-uniform diagonal quotient needs
coefficients for:

1. **Strong line-clean row.**  Compare the `(d-2)` coefficient, or the exact
   component row, with destroyed target load.
2. **Singleton line-clean row.**  Use the optimal fractional coefficient and
   sharpen the near-perfect two-matching component when necessary.
3. **Endpoint-overlap line-clean row.**  Treat the true degree-`d-3` local
   obstruction.
4. **Return row.**  New credits supported by one labelled edge return.
5. **Persistent selector row.**  The CMR531 paid-pair selector with surcharge
   two.
6. **Trace row.**  One fixed real trace line or row/column incidence slot.
7. **Root/fixed-interface row.**  Recurrence of one source residue, quotient
   carry and lifted low-rank prescription.
8. **Thin row.**  Small scattered residual factors not covered by nonroot depth
   transfer.

The broad labels “loaded line” and “repeated token” are no longer primitive
rows.

## 8. Recommended next lemmas

1. **Strong-trace credit comparison.**  Insert inherited line/height candidate
   counts into the strong envelope and identify a uniform geometric range where
   strict improvement is automatic.
2. **Singleton exact-component sharpening.**  Exploit the isolated opposite
   edge plus alternating-cycle decomposition of the near-perfect trace.
3. **Endpoint-overlap local sharpening.**  Separate one-endpoint and two-endpoint
   overlap and compute their exact component rook ratios.
4. **Return coefficient.**  Combine entering-edge recreation support with
   `(p+1)(h-1)` labelled incidence per returned edge.
5. **Selector coefficient.**  Evaluate
   \[
   A_L+\frac2Q+\frac{|B_L|}{Q(n-1)}
   \]
   over exact residual rook classes and optimize `Q`.
6. **Trace and root coefficients.**  Enumerate fixed trace and root/fixed-
   interface rows with provenance retained.
7. **Core matrix and CRT rows.**  Assemble surviving rows into an integer
   certificate `Av<v`, then retain collision and local-line labels during CRT
   gluing.

## 9. Computational priorities

- Evaluate all three line-clean criteria over inherited line/height classes.
- Enumerate extremal singleton and endpoint-overlap component signatures.
- Enumerate return-supported offspring with exact last-entering owner labels.
- Evaluate the CMR531 selector bound over exact residual rook classes and
  restoration thresholds.
- Enumerate fixed trace-line and root/fixed-interface rows.
- Search rational weights, clear denominators and verify strict integer row
  inequalities independently.

## 10. Current proved endpoint

Through **CMR1557**:

- exact response probabilities and owner weights are known;
- inherited-coordinate capacity is valid for scattered residual factors;
- packed displacement banks have quantitative lower bounds;
- strict transfers and fresh resources are off-diagonal;
- depth-zero banks split into deterministic root child channels;
- packed and loaded-owner currencies are owner-disjoint;
- arbitrary partial matchings, including complete nonaxis line traces, can be
  deleted from the extension-free host;
- repeated-token histories compress to return, persistent-selector or fixed-
  trace rows;
- the complete off-line line-clean response row is an exact rational rook-
  component dot product;
- line-clean traces have exact strong, singleton and endpoint-overlap uniform
  coefficients.

There is still no complete proof.  The next genuine advance is to close a
nontrivial geometric range of the strong-trace destroyed-credit inequality,
then isolate and sharpen the singleton and endpoint-overlap exceptions.
