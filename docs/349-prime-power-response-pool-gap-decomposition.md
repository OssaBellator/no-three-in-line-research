# Exact decomposition of response-pool upper-bound slack

CMR1958--CMR1965 compute the literal potential change `Delta Psi(Q)` for every
response. CMR1950--CMR1957 compute the response-pool upper bound

\[
B(Q)-U_{\rm pool}.
\]

This chapter identifies their difference exactly. The only losses are unused
simultaneous deletion capacity and explicit dominated-coefficient inflation.

## 1. Unit nondeleted export

For a response `Q`, let `E_1(Q)` count every occurring nondeleted primitive witness
with multiplicity one, irrespective of its child label. Let `E_+(Q)` be the total
extra multiplicity contributed by dominated witnesses:

\[
E_+(Q)
=
\sum_{\substack{w\text{ dominated}\\P(w)\subseteq Q}}
(m_w-1).
\]

### Theorem CMR1966 -- PROVED

The accepted scalar coefficient score decomposes exactly as

\[
\boxed{B(Q)=E_1(Q)+E_+(Q).}
\]

### Proof

Retained and transferred witnesses export one unit. Dominated witnesses export
their declared multiplicity `m_w`, equal to one unit plus `m_w-1`. Deleted
witnesses export zero. Summing the exact source-to-table equality over the
prescriptions contained in `Q` gives the formula. ∎

## 2. Pointwise gap identity

Let

\[
d(Q)=\#\{w\in W_{\rm del}:P(w)\subseteq Q\},
\qquad
K=\max_Qd(Q).
\]

### Theorem CMR1967 -- PROVED

For every response,

\[
\boxed{
\bigl(B(Q)-U_{\rm pool}\bigr)-\Delta\Psi(Q)
=
\bigl(K-d(Q)\bigr)+E_+(Q).
}
\]

### Proof

The exact direct identity is

\[
\Delta\Psi(Q)=E_1(Q)+d(Q)-T.
\]

The pool remainder is `U_pool=T-K`, and CMR1966 gives
`B(Q)=E_1(Q)+E_+(Q)`. Substitute and cancel `E_1(Q)` and `T`. ∎

Both terms on the right are nonnegative. Hence this identity reproves the pool
upper inequality and states exactly when it is tight.

### Corollary CMR1968 -- PROVED

The pool bound is exact on a response if and only if

\[
\boxed{d(Q)=K\quad\text{and}\quad E_+(Q)=0.}
\]

Thus tightness requires both maximum simultaneous deleted load and no occurring
domination inflation.

## 3. Global average decomposition

Let

\[
G_{\rm cap}=\sum_Q(K-d(Q)),
\qquad
G_{\rm dom}=\sum_QE_+(Q),
\qquad
G=G_{\rm cap}+G_{\rm dom}.
\]

### Theorem CMR1969 -- PROVED

The total response-pool bound gap satisfies

\[
\boxed{
\sum_Q\left[(B(Q)-U_{\rm pool})-\Delta\Psi(Q)\right]
=G.
}
\]

Equivalently,

\[
\boxed{
-\sum_Q\Delta\Psi(Q)
=
\bigl(ZU_{\rm pool}-A_B\bigr)+G.
}
\]

### Proof

Sum CMR1967 over all responses and use `A_B=sum_Q B(Q)`. ∎

## 4. Exact corrected average criterion

Define

\[
\Sigma_{\rm pool}=ZU_{\rm pool}-A_B,
\qquad
\Sigma_{\rm exact}= -\sum_Q\Delta\Psi(Q).
\]

### Theorem CMR1970 -- PROVED

The exact average slack is

\[
\boxed{
\Sigma_{\rm exact}
=
\Sigma_{\rm pool}+G_{\rm cap}+G_{\rm dom}.
}
\]

Consequently

\[
\boxed{
A_B<ZU_{\rm pool}+G
}
\]

is necessary and sufficient for the exact average of the literal triple changes to
be negative.

### Proof

The identity is CMR1969. Strict positivity of `Sigma_exact` is equivalent to a
negative sum of the finite integer response deltas. ∎

The original pool condition `A_B<ZU_pool` is recovered by discarding the two exact
nonnegative corrections.

## 5. Exact-only improvement

### Corollary CMR1971 -- PROVED

If

\[
\Sigma_{\rm pool}\le0<\Sigma_{\rm exact},
\]

then the response-pool sufficient condition fails while the literal response census
still proves that at least one response strictly improves.

The checker records this case explicitly as `exact_only_average_strict`.

This distinction is especially important for honest dominated tables: coefficient
inflation may be necessary for labelled closure but need not describe the literal
unlabelled triple change sharply.

## 6. Domination-free and full-load special cases

### Theorem CMR1972 -- PROVED

1. If no dominated witness occurs in any response, then `G_dom=0`; all pool loss is
   caused by responses with deleted load below `K`.
2. If every response has `d(Q)=K`, then `G_cap=0`; all pool loss is explicit
   domination surplus.
3. If both conditions hold, the response-pool bound equals the literal direct delta
   for every response.

### Proof

Each statement follows directly from the two nonnegative summands in CMR1967. ∎

This theorem gives a precise refinement target: sharpen `K` only through the actual
response-load distribution, and remove domination loss only through a tighter
labelled coefficient table.

## 7. Executable endpoint

### Corollary CMR1973 -- PROVED

`scripts/check_response_pool_gap_decomposition.py` implements the exact decomposition.
It:

1. validates the direct before/after response certificate;
2. revalidates the response-pool and coefficient bundles;
3. reconstructs deleted loads response-by-response;
4. separates unit export from dominated multiplicity surplus;
5. verifies the pointwise identity of CMR1967;
6. verifies both global identities of CMR1969--CMR1970;
7. records exact-only average-improvement cases; and
8. hashes the complete response gap table canonically.

Its deterministic suite runs 300 systems and rejects ten corrupted certificates.
One hundred regression systems deliberately inflate recurrent upper multiplicities:
the literal geometry is unchanged, and the suite confirms exact average improvement
in cases where the inflated pool sufficient condition does not certify it.

The deliberately inflated systems test the decomposition and honesty boundary. They
do not assert that the real 740 host fibres require those multiplicities or already
have negative exact average delta.
