# Conflict-colored cancellation bundles expose exact reuse gains

CMR1934--CMR1941 replace global injective deletion payment by a proper coloring of
the exact deleted-witness conflict graph.  CMR1910--CMR1917 identify the surviving
owner/fate export with the downstream coefficient table.

This chapter composes the two surfaces and records exactly how many integer units of
average and uniform slack are gained by static credit reuse.

## 1. Common geometric source

### Theorem CMR1942 -- PROVED

An accepted conflict-colored cancellation bundle uses one identical owner/fate
source in:

1. the conflict-colored cancellation manifest; and
2. the geometric coefficient bundle.

### Proof

The checker validates both inner objects and requires direct JSON-value equality of
their inline source manifests. ∎

The coefficient fingerprint remains an additional reproducibility check.

## 2. Gain over global injection

Let

\[
D=\#W_{\rm del},
\qquad
k=\#\{\text{used colors}\},
\qquad
T=|\mathcal D(P,R)|.
\]

The injective and colored unused credits are

\[
U_{\rm inj}=T-D,
\qquad
U_{\rm col}=T-k.
\]

### Theorem CMR1943 -- PROVED

The colored certificate gains exactly

\[
\boxed{s=D-k\ge0}
\]

unused destroyed-triple credits over global injection:

\[
\boxed{U_{\rm col}=U_{\rm inj}+s.}
\]

### Proof

Subtract the two definitions.  Proper coloring never uses more than one color per
vertex, so `k<=D`. ∎

## 3. Average slack gain

Let `Z=|PM(G)|` and let `A_B` be the exact exported numerator.  Define

\[
\Sigma_{\rm inj}^{\rm avg}=ZU_{\rm inj}-A_B,
\qquad
\Sigma_{\rm col}^{\rm avg}=ZU_{\rm col}-A_B.
\]

### Theorem CMR1944 -- PROVED

\[
\boxed{
\Sigma_{\rm col}^{\rm avg}
=
\Sigma_{\rm inj}^{\rm avg}+Zs.
}
\]

### Proof

Insert CMR1943 and expand. ∎

Thus every safely reused credit contributes one full denominator unit of average
slack.

## 4. Uniform slack gain

Let `M_B=max_Q B(Q)` and define

\[
\Sigma_{\rm inj}^{\rm all}=U_{\rm inj}-M_B,
\qquad
\Sigma_{\rm col}^{\rm all}=U_{\rm col}-M_B.
\]

### Theorem CMR1945 -- PROVED

\[
\boxed{
\Sigma_{\rm col}^{\rm all}
=
\Sigma_{\rm inj}^{\rm all}+s.
}
\]

### Proof

Again substitute `U_col=U_inj+s`. ∎

## 5. Reuse-only strictness

### Theorem CMR1946 -- PROVED

If

\[
\Sigma_{\rm col}^{\rm avg}>0
\quad\text{and}\quad
\Sigma_{\rm inj}^{\rm avg}\le0,
\]

then static conflict-compatible reuse, and not global injective payment, certifies an
improving response.  The analogous statement holds for uniform slack.

### Proof

The positive colored slack gives the corresponding strict certificate by CMR1940.
The nonpositive injective slack fails that same sufficient inequality. ∎

This is a comparison of certificate strength, not a claim that injective failure
proves the exact row non-improving.

## 6. Certified optimal static slack

### Theorem CMR1947 -- PROVED

When the colored manifest supplies a clique lower bound whose size equals `k`, the
recorded static unused credit

\[
U_{\rm col}=T-k
\]

is maximal among all fixed witness-to-credit assignments.

### Proof

CMR1938 gives `k=chi(Gamma_del)`, and CMR1937 identifies the chromatic number with
the minimum static reservation. ∎

## 7. Integration with exact and nested assignments

### Theorem CMR1948 -- PROVED

Any proved denominator-cleared upper bound `L` on `A_B` gives a strict average
certificate when

\[
\boxed{L<ZU_{\rm col}.}
\]

In the existing nested rank currency, it is sufficient that

\[
\boxed{6l_1+3l_2+l_3<6ZU_{\rm col}.}
\]

If one outer assignment maximum `M` bounds every response score, then

\[
\boxed{M<U_{\rm col}}
\]

proves uniform improvement.

### Proof

Apply CMR1940 after replacing the exact numerator or maximum by a proved upper
bound.  The sixfold inequality clears the existing factors `1`, `1/2`, and `1/6`.
∎

## 8. Executable endpoint

### Corollary CMR1949 -- PROVED

`scripts/check_conflict_colored_cancellation_bundle.py` implements the complete
source, coloring, coefficient and slack composition.

Its deterministic self-test validates 300 systems containing:

- 2,734 primitive witnesses;
- 1,180 deleted witnesses;
- 624 used destroyed credits;
- 556 safely reused credits;
- 300 unused destroyed credits;
- 1,550 exact coefficient bins;
- 2,012 units of coefficient mass;
- 3,391 exported numerator units;
- 6,816 units of average-slack gain;
- 556 units of uniform-slack gain;
- 124 average-strict systems;
- 107 uniform-strict systems;
- 100 reuse-only average-strict systems;
- 100 reuse-only uniform-strict systems; and
- 233 clique-matched optimal static colorings.

It rejects ten independently corrupted bundles.

The deliberately constructed reuse-strict systems prove completeness of the
certificate surface.  They do not claim that the actual 740 host fibres already
have these slacks.
