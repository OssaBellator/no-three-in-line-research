# Recurrent trace incidences batch to rooted line-clean rows

CMR1523 leaves one fixed trace signature

\[
(e,w,\varepsilon)
\]

inside one envelope epoch.  When the rooted centre is already fixed, that
signature determines one real trace line.  The remaining ambiguity is the
rooted centre itself.

The ambiguity has finite exact stock.  An envelope of side `t` contains at most
`t^2` physical centre cells.  Therefore excess recurrence fixes one centre and
one nonaxis trace line.  If that rooted centre is used as the fixed target, the
line contains the target cell and its complete allowed trace is automatically
target-disjoint.  Hence the endpoint-overlap line-clean coefficient can never
occur in this rooted trace splice: only the strong or singleton coefficient is
needed.

The argument does not add historical trace loads.  Recurrence is used only to
identify one repeated exact policy class; the line-clean response is executed
when one occurrence of that class is current.

Fix one inherited envelope epoch of side

\[
t=p^h,
\]

one layer, and one CMR1523 trace signature `(e,w,epsilon)`.  For every occurrence
`j`, let

\[
a_j
\]

be the rooted centre of its rooted-arm cylinder.  The trace witness `w` is
distinct from `a_j` and lies on the corresponding paid real line.

## 1. Finite rooted-centre stock

### Theorem CMR1566 -- PROVED

The number of possible physical rooted centres in one side-`t` envelope is at
most

\[
\boxed{t^2.}
\]

If additional layer, owner or prefix labels are retained, fixing those labels
can only decrease this stock.

### Proof

A physical centre is one cell of the `t by t` envelope.  There are exactly
`t^2` physical cells. ∎

## 2. Exact centre batching

Suppose the fixed trace signature occurs `J` times in the epoch.  For a centre
`a`, let `m(a)` be its occurrence multiplicity.

### Theorem CMR1567 -- PROVED

One centre satisfies

\[
\boxed{
m(a)\ge
\left\lceil\frac{J}{t^2}\right\rceil.
}
\]

Equivalently, for every integer `lambda>=2`, at least one of the following holds.

1. **Finite centre ancestry.**
   \[
   \boxed{J\le(\lambda-1)t^2.}
   \]
2. **Fixed rooted centre.**  One exact centre occurs in at least `lambda`
   episodes.

### Proof

Distribute the `J` occurrences among at most `t^2` centres and apply
pigeonhole.  If every multiplicity is at most `lambda-1`, sum those bounds. ∎

This stock is polynomial, unlike the complete selected-state stock.

## 3. A fixed centre gives one nonaxis line

Assume one centre `a` has been fixed by CMR1567.

### Theorem CMR1568 -- PROVED

The pair of distinct cells `(a,w)` determines one unique real line

\[
\boxed{K(a,w).}
\]

For every rooted-arm occurrence with centre `a` and trace witness `w`, the paid
trace line is exactly `K(a,w)`.  This line is nonhorizontal and nonvertical.

### Proof

Two distinct real grid cells determine one unique real line.  The trace witness
is chosen on the paid rooted-arm line, so that line must be `K(a,w)`.

A paid rooted-arm line supports a candidate collinear triple in the union of two
permutation layers.  CMR1334 excludes horizontal and vertical triple lines.
Therefore `K(a,w)` is nonaxis. ∎

Thus centre batching fixes the complete geometric line, not just one
row/column incidence slot.

## 4. Root-target traces are automatically target-disjoint

Use the rooted centre `a` as the selected fixed target.  Let `O` be the opposite
perfect matching and put

\[
H_a=K_{d,d}\setminus(O\cup\{a\}).
\]

Let

\[
X_K=E(H_a)\cap K(a,w)
\]

be the complete allowed response trace of the fixed line.

### Theorem CMR1569 -- PROVED

`X_K` is a partial matching and no edge of `X_K` uses the source endpoint or the
target endpoint of `a`.  Hence

\[
\boxed{X_K\cup\{a\}}
\]

is a partial matching disjoint from `O`.

In particular, the target-endpoint-overlap coefficient

\[
\left(\frac d{d-3}\right)^d
\]

never occurs for a rooted trace line cleaned at its rooted target.

### Proof

Every nonaxis line meets each source row and each target column in at most one
cell, so `X_K` is a partial matching.  Since the line contains `a`, any other
cell on it has a different source coordinate and a different target coordinate;
otherwise the line through the two cells would be horizontal or vertical.
The allowed trace omits `a` and all opposite-matching cells.  Therefore adjoining
`a` preserves the matching property and remains disjoint from `O`. ∎

This is stronger than the general ternary line-clean classification.

## 5. Exact rooted trace coefficient class

### Theorem CMR1570 -- PROVED

The rooted-target trace belongs to exactly one of two line-clean classes.

1. **Strong rooted trace.**  `X_K union {a}` extends to a perfect matching
   disjoint from `O`.  The host contains a spanning `(d-2)`-factor and has
   coefficient
   \[
   \boxed{
   \kappa_d^{\rm root,strong}
   =
   \left(\frac d{d-2}\right)^d.
   }
   \]
2. **Singleton rooted trace.**  `X_K union {a}` has size `d-1` and leaves one
   unmatched source and target joined by the sole residual opposite edge.  Its
   optimal fractional factor is
   \[
   q_{\rm sing}=d-2-\frac1{d-2}
   \]
   and its coefficient is
   \[
   \boxed{
   \kappa_d^{\rm root,sing}
   =
   \left(
   \frac{d(d-2)}{(d-1)(d-3)}
   \right)^d.
   }
   \]

No third class occurs.

### Proof

CMR1569 places the trace in the target-disjoint case of CMR1542.  CMR1543 says
such a partial matching has a derangement extension except for exactly the
singleton opposite-edge remainder.  Apply CMR1545 in the extendable case and
CMR1553 in the singleton case. ∎

The exact CMR1531 component-rook ratio remains available in both classes.

## 6. Rooted trace execution row

Let

\[
\mathcal C_{\rm off}^{K}
=
\frac{V_1^{\rm off}}d
+
\frac{V_2^{\rm off}}{(d)_2}
+
\frac{V_3^{\rm off}}{(d)_3}
\]

for the corrected off-line candidate counts after deleting `X_K`.  Let `kappa`
be the strong or singleton coefficient from CMR1570.

### Theorem CMR1571 -- PROVED

There is a target-safe line-clean response law satisfying

\[
\boxed{
\mathbb E N_{\rm off}(R)
\le
\kappa\mathcal C_{\rm off}^{K},
}
\]

and creating no new line-local collateral on `K(a,w)`.

If `b` line-clean allowed edges are unavailable and the current potential is
`m`, then

\[
\boxed{
\kappa
\left[
\mathcal C_{\rm off}^{K}
+
\frac{(m+1)b}{d}
\right]
<
D_S(a)
}
\]

forces a feasible strict-improvement response.

### Proof

CMR1513--CMR1515 give a target-safe response after deleting the complete
nonaxis trace and zero line-local collateral.  CMR1547 gives the strong bound
and CMR1554--CMR1555 give the singleton bound, including the unavailable-edge
penalty. ∎

The target load is the load of the rooted centre `a`; no historical occurrence
is counted as additional destruction.

## 7. Master trace alternative

### Theorem CMR1572 -- PROVED

For every integer `lambda>=2`, `J` occurrences of one fixed CMR1523 trace
signature in a side-`t` envelope reach at least one of:

1. the finite ancestry bound
   \[
   \boxed{J\le(\lambda-1)t^2;}
   \]
2. at least `lambda` occurrences of one exact rooted line-clean policy class
   \[
   (a,K(a,w),\kappa),
   \]
   where `kappa` is strong or singleton and never endpoint-overlap.

At every occurrence in branch 2, the response law and strict-improvement test of
CMR1571 are available with the same rooted centre and real line.

### Proof

Apply CMR1567.  In the recurrent-centre branch, CMR1568 fixes the line,
CMR1569 excludes endpoint overlap, and CMR1570 fixes one of the two remaining
coefficient classes.  CMR1571 supplies the policy. ∎

The theorem does not assert that the `lambda` historical lines are simultaneous.
They identify repeated access to one exact response row.

## 8. Trace-row endpoint

### Corollary CMR1573 -- PROVED

The fixed trace incidence from CMR1523 need not remain an independent broad
recurrent row.

1. Variation of the rooted centre has finite stock at most `t^2` per fixed trace
   signature and envelope epoch.
2. Excess recurrence fixes one rooted centre and one nonaxis real line.
3. Cleaning at the rooted target excludes the worst endpoint-overlap
   coefficient.
4. The recurrent row is one exact strong or singleton line-clean row, with the
   exact component-rook ratio available for sharpening.

Thus the repeated-token quotient may replace the broad trace row by finite
centre ancestry plus the already explicit rooted line-clean coefficient rows.
The remaining work is numerical comparison with `D_S(a)` and treatment of trace
incidences whose execution cannot choose the rooted centre as the fixed target.
No all-`n` theorem is claimed.

Centre batching, rooted-line uniqueness, target-disjoint traces and the exact
strong/singleton classification are checked in
[`scripts/verify_prime_power_trace_centre_line_clean_splice.py`](../scripts/verify_prime_power_trace_centre_line_clean_splice.py).
