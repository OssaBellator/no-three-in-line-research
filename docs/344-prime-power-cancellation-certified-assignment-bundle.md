# Cancellation-certified coefficient bundles expose exact improvement slack

CMR1918--CMR1925 certify a one-for-one cancellation of every deleted primitive
geometric witness against a distinct current triple destroyed by the same removal.
CMR1910--CMR1917 certify exact equality between the remaining owner/fate export and
the downstream labelled coefficient table.

This chapter composes those two surfaces. The resulting certificate contains:

- one destroyed-triple cancellation manifest;
- one exact geometric-to-assignment coefficient bundle built from the same source;
- the exact unused destruction credit;
- the exact total exported response numerator; and
- average and response-uniform strictness slacks.

No optimization claim is hidden in the certificate: all response scores are
enumerated exactly for the finite side-three/four/five checker surface.

## 1. Common source identity

### Theorem CMR1926 -- PROVED

An accepted cancellation-certified bundle uses exactly one owner/fate source:

\[
\boxed{
M_{\mathrm{cancel}}=M_{\mathrm{coeff}}.
}
\]

### Proof

The checker validates both inner objects and then requires direct JSON-value
equality between their inline source manifests. ∎

The source fingerprint in the coefficient bundle remains an additional
reproducibility check.

## 2. Exact exported response score

Let the accepted coefficient table be

\[
c^{(r)}_j(P).
\]

For a response matching `Q`, define the unweighted scalar export score

\[
B(Q)
=
\sum_{r=1}^3
\sum_j
\sum_{\substack{P\subseteq Q\\|P|=r}}
c^{(r)}_j(P).
\]

### Theorem CMR1927 -- PROVED

The checker computes `B(Q)` exactly from the accepted downstream coefficient table,
and

\[
\boxed{
A_B=\sum_{Q\in\operatorname{PM}(G)}B(Q)
}
\]

is the exact denominator-cleared exported scalar numerator.

### Proof

CMR1912 identifies the downstream table with the source export. The checker tests
prescription containment in every enumerated perfect matching and sums integer
coefficients. ∎

This scalar score ignores child-state weights. It is used for direct real-triple
potential improvement; the weighted recurrent analysis remains separate.

## 3. Average improvement slack

Let `U` be the unused destroyed-triple credit from CMR1923 and let
`Z=|PM(G)|`.

Define

\[
\Sigma_{\mathrm{avg}}
=
ZU-A_B.
\]

### Theorem CMR1928 -- PROVED

The exact average net-triple numerator satisfies

\[
\boxed{
\sum_Q\Delta\Psi(Q)
\le
-\Sigma_{\mathrm{avg}}.
}
\]

### Proof

Sum the responsewise inequality

\[
\Delta\Psi(Q)\le B(Q)-U
\]

from CMR1923 over all `Z` responses. ∎

A positive `Sigma_avg` is an exact integer certificate that at least one response
strictly improves the potential.

## 4. Uniform response slack

Define

\[
\Sigma_{\mathrm{all}}
=
U-\max_Q B(Q).
\]

### Theorem CMR1929 -- PROVED

Every response satisfies

\[
\boxed{
\Delta\Psi(Q)\le-\Sigma_{\mathrm{all}}.
}
\]

### Proof

CMR1923 gives `Delta Psi(Q)<=B(Q)-U`; replace `B(Q)` by its exact maximum. ∎

Thus `Sigma_all>0` proves every response improves, not merely that a favorable
response exists.

## 5. Strict average and uniform criteria

### Corollary CMR1930 -- PROVED

If

\[
\boxed{\Sigma_{\mathrm{avg}}>0,}
\]

then some response has strictly smaller real-triple potential.

### Proof

A positive average slack makes the sum of all integer potential changes negative,
so at least one summand is negative. ∎

### Corollary CMR1931 -- PROVED

If

\[
\boxed{\Sigma_{\mathrm{all}}>0,}
\]

then every response has strictly smaller real-triple potential.

### Proof

Apply CMR1929 responsewise. ∎

The uniform certificate may be useful for eliminating a state without any selector.

## 6. Integration with existing exact and nested assignments

The exact response enumeration in the checker is a validation surface, not the only
way to prove strictness on a populated quotient.

### Theorem CMR1932 -- PROVED

Let `L` be any proved denominator-cleared upper bound on the exported numerator
`A_B`. Then

\[
\boxed{L<ZU}
\]

is sufficient for a strict average-improvement certificate.

In particular:

1. an exact rook-marginal numerator may be compared directly with `ZU`;
2. if rank-one, rank-two and rank-three nested assignment numerators are
   `l_1,l_2,l_3`, then
   \[
   \boxed{
   6l_1+3l_2+l_3<6ZU
   }
   \]
   is sufficient; and
3. if one outer assignment maximum `M` bounds `B(Q)` for every response, then
   \[
   \boxed{M<U}
   \]
   proves every response improves.

### Proof

The first statement follows from `A_B<=L` and CMR1928. The sixfold inequality is
the denominator clearing of the proved peeling factors. The final statement
combines the responsewise upper bound with CMR1929. ∎

This places destroyed-triple credits in the same exact integer currency as the
existing line-clean, nested-assignment and unified-outer-score compilers.

## 7. Executable endpoint

### Corollary CMR1933 -- PROVED

`scripts/check_cancellation_certified_assignment_bundle.py` implements the composed
certificate.

It:

1. validates the destroyed-triple cancellation manifest;
2. validates the exact geometric coefficient bundle;
3. requires common source identity;
4. enumerates every response score `B(Q)`;
5. checks the claimed unused credit, exact numerator and maximum score;
6. computes `Sigma_avg` and `Sigma_all`; and
7. rejects any altered source, denominator, coefficient or slack claim.

Its deterministic self-test validates 300 systems containing:

- 3,717 primitive witnesses;
- 1,766 deleted witnesses;
- 1,881 unused destroyed-triple credits; and
- 4,557 exported numerator units.

Among these systems:

- 129 have positive exact average slack; and
- 105 have positive response-uniform slack.

It rejects ten independently corrupted certificates.

The deliberately strict test systems demonstrate certificate completeness, not that
the actual 740 research hosts already satisfy these inequalities. The next
frontier is to populate their real pre-response point sets, removal sets and fate
maps, then measure the resulting credits against the exact exported rows.
