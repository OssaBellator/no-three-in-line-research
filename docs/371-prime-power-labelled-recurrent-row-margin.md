# Exact labelled recurrent-row margin accounting

CMR2102--CMR2109 classify which labelled response vectors admit strictly positive
supporting child weights. CMR2062--CMR2069 provide a linked operation and exact destroyed
threshold. This chapter combines them into one responsewise recurrent-row accounting
surface.

## Theorem CMR2142 -- PROVED

A row-margin certificate requires one linked operation and one labelled weight-exposure
certificate over exactly the same geometric assignment bundle and source digest. Host,
fibre, source, response family and child-coordinate order are therefore common to both
surfaces.

## Theorem CMR2143 -- PROVED

The child weight vector

\[
w\in\mathbf Z_{>0}^{C}
\]

must equal one of the directly verified positive-support certificates in the exposure
manifest. The checker does not accept an arbitrary claimed positive normal.

Every uncredited minimizer under these weights is independently required to remain on
the exact componentwise Pareto frontier.

## Theorem CMR2144 -- PROVED

For each response `Q`, the certificate may declare a nonnegative child-indexed routed
credit vector

\[
r(Q)=(r_c(Q))_{c\in C}.
\]

Its total number of routed units must satisfy

\[
\boxed{\sum_c r_c(Q)\le T,}
\]

where `T` is the linked operation's exact destroyed-current-triple count. Routes are
response-local; no simultaneous reuse claim is inferred by summing them over different
responses.

## Theorem CMR2145 -- PROVED

For response-independent fixed load `a`, parent budget `W`, exact child vector `v(Q)` and
weights `w`, the row checker reconstructs

\[
\boxed{
L(Q)=a+w\cdot v(Q)-w\cdot r(Q),
\qquad
\operatorname{margin}(Q)=W-L(Q).
}
\]

Every coordinate product, routed weighted credit, row load and margin is stored and
recomputed exactly in integer arithmetic.

## Theorem CMR2146 -- PROVED

The deterministic row selector is the lexicographically first response minimizing
`L(Q)`, equivalently maximizing the row margin. If

\[
L_* = \min_Q L(Q),
\]

then the exact maximum margin is

\[
\boxed{W-L_*.}
\]

## Theorem CMR2147 -- PROVED

The row has the exact sign partition

\[
\begin{array}{ll}
W-L_*>0 & \text{strict},\\
W-L_*=0 & \text{critical},\\
W-L_*<0 & \text{excess}.
\end{array}
\]

No floating-point spectral or LP status is used for this row-level conclusion.

## Theorem CMR2148 -- PROVED

Positive support before credit and row selection after routed credit are different
surfaces. A response-local credit can change the selected response, and the checker
records whether the final response was already Pareto or carried the exact stored
support certificate before credit.

Passing the arithmetic check does not prove that a routed destroyed triple genuinely
belongs to the declared child state. That remains a rule-specific fate-semantic theorem.
Likewise, the supplied parent budget is not asserted to extend to one global SCC
Lyapunov vector.

## Corollary CMR2149 -- PROVED

`scripts/check_prime_power_labelled_recurrent_row_margin.py` validates arbitrary linked
row-margin certificates. Its deterministic suite exercises 100 linked operations with
strict, critical and excess rows, response-local routed credits and exact positive
weights; twelve independent corruptions are rejected.
