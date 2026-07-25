# Global refill slack from defect mass

The bottleneck-slack theorem PP3mx compares the movement ownership bottleneck
with

\[
\Lambda_{\rm score}(B)
=
\sum_i(W-\chi_i(B))_+.
\]

This chapter lower-bounds that slack by global controller-defect mass. The result
is stronger than requiring every macro score to be small: a refill label may be
poor in several macros as long as its total capped loss remains controlled.

## 1. Elementary slack lower bound

### Proposition PP3nf -- PROVED

For every refill label \(B\),

\[
\boxed{
\Lambda_{\rm score}(B)
\ge
T-\sum_{i=1}^M\chi_i(B).
}
\]

#### Proof

For every real \(x\),

\[
(W-x)_+\ge W-x.
\]

Sum with \(x=\chi_i(B)\) and use \(MW=T\). ∎

The right side may be negative, in which case the statement is vacuous. Its
value is that large scores in a few macros cannot cost more than their actual
magnitude before the positive-part cap is applied.

## 2. Fixed refill-label margin

Fix \(\delta>0\). Say refill label \(B\) has margin \(\delta\) in every macro
when

\[
b_i(B)
\le
(1-\gamma-\delta)R
\qquad(i\in[M]).
\]

Then every denominator in the column score satisfies

\[
(1-\gamma)R-b_i(B)\ge\delta R.
\]

### Theorem PP3ng -- PROVED

If refill label \(B\) has margin \(\delta\) in every macro, then

\[
\boxed{
\Lambda_{\rm score}(B)
\ge
T-
\frac{
\sum_i A_i+\sum_iV_i(B)
}{\delta R}.
}
\]

#### Proof

The score definition and the margin give

\[
\chi_i(B)
\le
\frac{A_i+V_i(B)}{\delta R},
\]

where replacing the score by its truncation at \(T\) only decreases it. Sum and
apply PP3nf. ∎

Thus the refill side depends on the global movement-cell defect mass
\(\sum_iA_i\) and the global same-slot anchor column mass
\(\sum_iV_i(B)\), not their worst individual macro values.

## 3. Bottleneck completion from global mass

### Corollary PP3nh -- PROVED

Assume every refill label has margin \(\delta\) in every macro. If

\[
\boxed{
r_{\rm score}
+
\frac{
\sum_iA_i+\max_B\sum_iV_i(B)
}{\delta R}
\le
T,
}
\]

then the controller-aware global allocation and full patch exist.

#### Proof

PP3ng gives

\[
\Lambda_{\rm score,*}
\ge
T-
\frac{
\sum_iA_i+\max_B\sum_iV_i(B)
}{\delta R}.
\]

The displayed condition implies
\(r_{\rm score}\le\Lambda_{\rm score,*}\). Apply PP3mx. ∎

Using PP3mb,

\[
\sum_iA_i
\le
\sum_i\Xi_i.
\]

Hence the stronger but more intrinsic condition

\[
\boxed{
r_{\rm score}
+
\frac{
\sum_i\Xi_i+\max_B\sum_iV_i(B)
}{\delta R}
\le T
}
\]

also suffices.

## 4. Near-complete slack regime

### Corollary PP3ni -- PROVED

Under fixed refill-label margin \(\delta\), suppose

\[
\sum_i\Xi_i=o(RT)
\]

and

\[
\max_B\sum_iV_i(B)=o(RT).
\]

Then

\[
\Lambda_{\rm score,*}=T-o(T).
\]

Consequently direct allocation follows whenever

\[
r_{\rm score}\le T-o(T)
\]

with a dominating common error term.

#### Proof

Apply PP3ng, PP3mb, and PP3mx. ∎

This is substantially weaker on the movement side than PP3me: the balanced
movement ownership need only avoid rows whose nondegree score is asymptotically
all of \(T\). It need not achieve an \(o(T)\) bottleneck.

## 5. Revised global refill obstruction

### Corollary PP3nj -- PROVED

If the criterion PP3nh fails, then at least one of the following persists.

1. A refill label loses every fixed positive margin in some macro:
   \[
   b_i(B)>(1-\gamma-\delta)R
   \]
   for arbitrarily small fixed \(\delta>0\).
2. The movement ownership bottleneck is asymptotically close to \(T\).
3. The total excess-shadow mass satisfies
   \[
   \sum_i\Xi_i=\Omega(R(T-r_{\rm score})).
   \]
4. Some refill label has global same-slot anchor column mass
   \[
   \sum_iV_i(B)=\Omega(R(T-r_{\rm score})).
   \]

Thus a failure of one-sided direct allocation now requires either a nearly dead
refill macro-label pair, a nearly impossible movement routing problem, or global
controller/anchor mass at the exact scale of the remaining ownership slack.