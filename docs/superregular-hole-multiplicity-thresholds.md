# Hole-multiplicity bounds for threshold endpoint flow

**Branch:** `research/superregular-resampling`

SRR2ac--SRR2af express every endpoint-cost deficiency through common hole intersections. This note bounds those intersections using source-side hole mass and endpoint hole multiplicity.

For a switching graph `Gamma subseteq A x B`, write

\[
H(a)=B\setminus N_\Gamma(a),
\qquad
\nu(b)=|\{a:b\in H(a)\}|.
\]

For a threshold set `S subseteq B`, put

\[
M_S=\sum_{a\in A}|S\cap H(a)|
=\sum_{b\in S}\nu(b),
\qquad
\mu_S=\max_{b\in S}\nu(b).
\]

## SRR2ag -- common-hole mass bound -- PROVED

For every nonempty `X subseteq A`, with `x=|X|`,

\[
\boxed{
|S\cap H(X)|
\le
\left\lfloor\frac{\sum_{a\in X}|S\cap H(a)|}{x}\right\rfloor
\le
\left\lfloor\frac{M_S}{x}\right\rfloor.
}
\]

Moreover,

\[
\boxed{x>\mu_S\implies S\cap H(X)=\varnothing.}
\]

### Proof

Every endpoint in `S cap H(X)` is a hole for all `x` sources of `X`, so it contributes `x` incidences to the sum over `a in X`. This proves the first two inequalities. If such an endpoint existed for `x>mu_S`, its multiplicity would be at least `x`, contradicting the definition of `mu_S`. QED.

## SRR2ah -- computable threshold deficiency bound -- PROVED

Let `S=B_{<k}` be one endpoint-cost sublevel. Its Hall deficiency satisfies

\[
\boxed{
\delta_k
\le
\max_{1\le x\le \min\{|A|,\mu_S\}}
\left(
 x-|S|+\left\lfloor\frac{M_S}{x}\right\rfloor
\right)_+.
}
\]

If the maximum is zero, `S` supports a matching saturating `A`.

### Proof

Insert SRR2ag into the exact common-hole formula SRR2ac. Terms with `x>mu_S` have zero common-hole contribution, and are already nonpositive whenever `|S|>=|A|`; retaining only `x<=mu_S` gives the displayed safe bound. If it is zero, every Hall deficiency term vanishes. QED.

## SRR2ai -- uniform endpoint-multiplicity criterion -- PROVED

Suppose every endpoint is excluded by at most `mu` sources and the threshold hole mass is at most `M_k`. Then

\[
\boxed{
\delta_k
\le
\epsilon_k:=
\max_{1\le x\le \min\{|A|,\mu\}}
\left(
 x-|B_{<k}|+\left\lfloor\frac{M_k}{x}\right\rfloor
\right)_+.
}
\]

Consequently,

\[
\boxed{
\operatorname{OPT}(c)
\le
\sum_k\epsilon_k.
}
\]

The same statement survives compatible endpoint conditioning after recomputing `M_k` and `mu` on the surviving endpoint set.

### Proof

Apply SRR2ah at each threshold and sum using SRR2ad. Conditioning only deletes endpoints and therefore preserves the incidence double count. QED.

## SRR2aj -- exact overload witnesses -- PROVED

Failure of a proposed small `epsilon_k` has one explicit cause:

1. a threshold sublevel is too small;
2. its total source-hole mass `M_k` is too large;
3. one endpoint has hole multiplicity exceeding the declared `mu`;
4. or one source cut `X`, with `|X|<=mu`, realizes a larger common-hole intersection than the proposed bound.

Thus the geometric frontier can be attacked through endpoint multiplicity and total low-cost hole mass, without enumerating all source cuts unless a bound fails.

## Finite check

`scripts/verify_srr_hole_multiplicity.py` exhausts small hole systems, compares the exact Hall deficiency with the multiplicity bound, and checks the conditioned version.