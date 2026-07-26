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

Every nonaxis line is a partial matching.  CMR1510--CMR1517 prove that deleting
its complete allowed trace from `H_e` leaves at least one perfect matching.
The resulting response still avoids the target and opposite layer, creates no
new line-local collateral, and gives zero same-owner/same-line offspring for a
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

## 5. Exact strong/weak line-clean factor signatures

CMR1534--CMR1541 give a universal spanning `(d-3)`-factor and coefficient

\[
\left(\frac d{d-3}\right)^d.
\]

CMR1542--CMR1549 sharpen this to an exact binary trace signature.  Put

\[
Y=X\cup\{e\}.
\]

The line-clean host contains a spanning `(d-2)`-factor exactly when:

1. `Y` is a partial matching, so the trace uses neither endpoint of `e`;
2. `Y` does not leave one unmatched source and target joined by `O`.

In the strong class,

\[
N_d(F)
\ge
 d!\left(\frac{d-2}{d}\right)^d,
\qquad
\Pr(P\subseteq R)
\le
\frac{(d/(d-2))^d}{(d)_r}.
\]

The strong class fails only through target-endpoint overlap or one singleton
opposite-edge remainder.  Weak traces retain

\[
N_d(F)
\ge
 d!\left(\frac{d-3}{d}\right)^d,
\qquad
\Pr(P\subseteq R)
\le
\frac{(d/(d-3))^d}{(d)_r}.
\]

Define

\[
q_X=
\begin{cases}
 d-2,&\text{strong trace},\\
 d-3,&\text{weak trace},
\end{cases}
\qquad
\kappa_d(X,e)=\left(\frac d{q_X}\right)^d.
\]

Then

\[
\mathbb E N_{off}(R)
\le
\kappa_d(X,e)
\left[
\frac{V_1^{off}}d
+
\frac{V_2^{off}}{(d)_2}
+
\frac{V_3^{off}}{(d)_3}
\right].
\]

With `b` unavailable allowed edges and current potential `m`, the inequality

\[
\kappa_d(X,e)
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

The line-clean numerical frontier is therefore a two-signature destroyed-credit
comparison.  Exact component rook ratios remain available when either uniform
coefficient is too weak.

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

1. **Strong line-clean row.**  Compare the `(d-2)` coefficient, or the exact
   component row, with destroyed target load.
2. **Weak line-clean row.**  Treat endpoint-overlap and singleton-remainder
   signatures with the `(d-3)` coefficient or exact component sharpening.
3. **Return row.**  New credits supported by one labelled edge return.
4. **Persistent selector row.**  The CMR531 paid-pair selector with surcharge
   two.
5. **Trace row.**  One fixed real trace line or row/column incidence slot.
6. **Root/fixed-interface row.**  Recurrence of one source residue, quotient
   carry and lifted low-rank prescription.
7. **Thin row.**  Small scattered residual factors not covered by nonroot depth
   transfer.

The broad labels “loaded line” and “repeated token” are no longer primitive
rows.

## 8. Recommended next lemmas

1. **Strong-trace credit comparison.**  Insert inherited line/height candidate
   counts into the `(d-2)` envelope and identify the geometric range where the
   strict inequality is automatic.
2. **Weak-trace component sharpening.**  Optimize exact path/cycle rook ratios
   for endpoint-overlap and singleton-remainder signatures.
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

- Evaluate the strong `(d-2)` criterion over inherited line/height classes.
- Enumerate extremal weak path/cycle signatures and their exact prescription
  ratios.
- Enumerate return-supported offspring with exact last-entering owner labels.
- Evaluate the CMR531 selector bound over exact residual rook classes and
  restoration thresholds.
- Enumerate fixed trace-line rows with row/column provenance retained.
- Enumerate recurrent root/fixed-interface rows and thin scattered factors.
- Search rational weights, clear denominators and verify strict integer row
  inequalities independently.

## 10. Current proved endpoint

Through **CMR1549**:

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
- every line-clean host has a universal `(d-3)` factor;
- every trace has an exact strong/weak factor signature, with a `(d-2)` factor
  outside the two explicit exception classes.

There is still no complete proof.  The next genuine advance is to close a
nontrivial geometric range of the strong-trace destroyed-credit inequality and
then isolate the truly exceptional weak signatures.
