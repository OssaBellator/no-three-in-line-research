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

## 4. Extension-free line cleaning

CMR1510--CMR1517 show that every Hall-cut blocker of `H_e` has more edges than a
partial matching can place in the same cut rectangle.  Hence

\[
\operatorname{PM}(H_e\setminus X)\ne\varnothing
\]

for every partial matching `X` of allowed response edges.

Every nonaxis line is a partial matching.  Its complete allowed response trace
may therefore be forbidden while the response continues to avoid both `O` and
`e`.  The resulting state creates no new line-local collateral.  For a CMR1461
owner-labelled loaded line, the same-owner, same-line offspring coordinate has
policy coefficient zero.

## 5. Exact and uniform line-clean coefficients

Put

\[
F=O\cup X\cup\{e\},
\qquad
D=O\cup X.
\]

CMR1526--CMR1533 show that `D` has maximum degree two, decomposes into alternating
paths and even cycles, and has a component-factorized rook polynomial.  If
`e=uv`,

\[
\mathcal R_F(z)
=
\mathcal R_D(z)+z\mathcal R_{D-u-v}(z).
\]

Therefore

\[
N_d(F)=\sum_j(-1)^jr_j(F)(d-j)!,
\qquad
\Pr(P\subseteq R)=\frac{N_{d-r}(F/P)}{N_d(F)}.
\]

CMR1534--CMR1541 add a host-uniform denominator.  Every such allowed graph
contains a spanning `(d-3)`-regular subgraph, so

\[
\boxed{
N_d(F)
\ge
 d!\left(\frac{d-3}{d}\right)^d.
}
\]

Write

\[
\kappa_d^{line}
=
\left(\frac d{d-3}\right)^d.
\]

Every rank-one through rank-three allowed prescription satisfies

\[
\boxed{
\Pr(P\subseteq R)
\le
\frac{\kappa_d^{line}}{(d)_r}.
}
\]

Consequently the exact off-line rook row is bounded by

\[
\boxed{
\mathbb E N_{off}(R)
\le
\kappa_d^{line}
\left[
\frac{V_1^{off}}d
+
\frac{V_2^{off}}{(d)_2}
+
\frac{V_3^{off}}{(d)_3}
\right].
}
\]

With `b` unavailable allowed edges and current potential `m`, the strict test

\[
\kappa_d^{line}
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

forces one feasible lower-potential line-clean response.

The line-clean coefficient is now defined both exactly and uniformly.  The
remaining issue is whether the uniform envelope is strong enough in every
recurrent geometric class; where it is not, the exact component signature must
be used.

## 6. Atomic repeated-token quotient

For one nonroot full token in an envelope `t=p^h`, repeated heavy episodes first
pay finite token-edge stock or identify one recurrent central edge.  Once that
edge is fixed, the pair and trace signature stocks are

\[
(t-1)^2
\qquad\text{and}\qquad
2(t-1).
\]

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

1. **Line-clean credit row.**  Compare the explicit uniform envelope, or the
   sharper exact component row, with destroyed target load.
2. **Return row.**  New credits supported by one labelled edge return.
3. **Persistent selector row.**  The CMR531 paid-pair selector with surcharge
   two.
4. **Trace row.**  One fixed real trace line or row/column incidence slot.
5. **Root/fixed-interface row.**  Recurrence of one source residue, quotient
   carry and lifted low-rank prescription.
6. **Thin row.**  Small scattered residual factors not covered by nonroot depth
   transfer.

The broad labels “loaded line” and “repeated token” are no longer primitive
rows.

## 8. Recommended next lemmas

1. **Line-clean destroyed-credit comparison.**  Insert inherited line/height
   candidate counts into the CMR1539 envelope and identify the classes where
   the CMR1540 inequality is automatic.
2. **Component-signature sharpening.**  For the remaining classes, optimize the
   exact CMR1533 rook ratios over path/cycle signatures.
3. **Return coefficient.**  Combine entering-edge recreation support with
   `(p+1)(h-1)` labelled incidence per returned edge.
4. **Selector coefficient.**  Evaluate
   \[
   A_L+\frac2Q+\frac{|B_L|}{Q(n-1)}
   \]
   over exact residual rook classes and optimize `Q`.
5. **Trace coefficient.**  Convert one fixed trace incidence into a loaded-line,
   secant-star, prefix/carry, or fixed-interface row without losing provenance.
6. **Root/fixed-interface coefficient.**  Enumerate exact offspring by partner
   type, source residue, quotient carry and local rank.
7. **Core matrix and CRT rows.**  Assemble surviving rows into an integer
   certificate `Av<v`, then retain collision and local-line labels during CRT
   gluing.

## 9. Computational priorities

The next finite calculations should target coefficients rather than new
structural alternatives.

- Evaluate the CMR1540 line-clean criterion over exact inherited line/height
  classes.
- Enumerate extremal path/cycle signatures for the exact CMR1533 ratios.
- Enumerate return-supported offspring with exact last-entering owner labels.
- Evaluate the CMR531 selector bound over exact residual rook classes and
  restoration thresholds.
- Enumerate fixed trace-line rows with row/column provenance retained.
- Enumerate recurrent root/fixed-interface rows and thin scattered factors.
- Search rational weights, clear denominators and verify strict integer row
  inequalities independently.

## 10. Current proved endpoint

Through **CMR1541**:

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
- every line-clean host contains a spanning `(d-3)`-factor and obeys the
  explicit uniform permanent and collateral bounds above.

There is still no complete proof.  The next genuine advance is to certify the
CMR1540 inequality on a nontrivial uniform geometric range, or sharpen the
exact component rows until such a range closes.
