# Threshold-local common-hole formulas for endpoint-flow deficiency

**Branch:** `research/superregular-resampling`

SRR2s--SRR2x use the uniform left-hole bound `|H(a)|<=Delta`.  That bound discards the main geometric information: a Hall cut is controlled by holes common to every source in the cut, not by the full hole set of one source.  This note gives the exact common-hole formula and a threshold-local endpoint-cost criterion.

Let `Gamma subseteq A x B` satisfy Hall's condition.  For `a in A`, put

\[
H(a)=B\setminus N_\Gamma(a).
\]

For `X subseteq A`, define the common-hole set

\[
H(X)=\bigcap_{a\in X}H(a),
\]

with `H(empty)=B`.  For `S subseteq B`, let `r(S)` be the maximum number of vertices of `A` matchable injectively into `S`.

## SRR2ac -- exact common-hole deficiency formula -- PROVED

For every endpoint set `S subseteq B`,

\[
\boxed{
|A|-r(S)
=
\max_{\varnothing\ne X\subseteq A}
\bigl(|X|-|S|+|S\cap H(X)|\bigr)_+.
}
\]

Equivalently, if

\[
\kappa_S(x)=
\max_{X\subseteq A,\ |X|=x}|S\cap H(X)|,
\]

then

\[
\boxed{
|A|-r(S)
=
\max_{1\le x\le |A|}
\bigl(x-|S|+\kappa_S(x)\bigr)_+.
}
\]

### Proof

For nonempty `X`, an endpoint belongs to no neighbour of `X` exactly when it is a hole for every member of `X`.  Hence

\[
B\setminus N_\Gamma(X)=H(X)
\]

and therefore

\[
|N_\Gamma(X)\cap S|
=|S|-|S\cap H(X)|.
\]

Substitute this identity into the deficiency form of Hall's theorem,

\[
|A|-r(S)=
\max_{X\subseteq A}
\bigl(|X|-|N_\Gamma(X)\cap S|\bigr)_+.
\]

The empty set contributes zero.  Grouping the remaining sets by cardinality gives the second display. QED.

## SRR2ad -- exact threshold-cost decomposition by common holes -- PROVED

Let `c:B->Z_{>=0}`, let

\[
B_{<k}=\{b:c(b)<k\},
\qquad 1\le k\le C:=\max_b c(b),
\]

and define

\[
\delta_k=|A|-r(B_{<k}).
\]

Then

\[
\boxed{
\delta_k
=
\max_{\varnothing\ne X\subseteq A}
\bigl(
|X|-|B_{<k}|+|B_{<k}\cap H(X)|
\bigr)_+,
}
\]

and the minimum endpoint-flow cost is exactly

\[
\boxed{
\operatorname{OPT}(c)=\sum_{k=1}^{C}\delta_k.
}
\]

### Proof

Apply SRR2ac to each sublevel set.  The cost identity is SRR2l. QED.

## SRR2ae -- threshold-intersection criterion -- PROVED

Suppose numbers `epsilon_k>=0` satisfy, for every nonempty `X subseteq A`,

\[
\boxed{
|B_{<k}\cap H(X)|
\le
|B_{<k}|-|X|+\epsilon_k.
}
\]

Then

\[
\boxed{
\delta_k\le\epsilon_k,
\qquad
\operatorname{OPT}(c)\le\sum_{k=1}^{C}\epsilon_k.
}
\]

The same conclusion holds after compatible endpoint conditioning `B'=B\setminus D` by replacing every sublevel with `B'_{<k}` and every common-hole intersection with `B'_{<k}\cap H(X)`.

### Proof

The displayed hypothesis makes every term in the maximum of SRR2ad at most `epsilon_k`.  Sum over thresholds.  Conditioning merely replaces the available endpoint set; the identity `B'\setminus N_{Gamma[A,B']}(X)=B'\cap H(X)` remains exact. QED.

## SRR2af -- corrected geometric frontier -- PROVED

The endpoint-flow problem no longer requires a uniform bound on every full hole set.  It is enough, and in the threshold formulation exact, to control intersections of low-event endpoints with common-hole sets `H(X)`.  A failed cost comparison returns one explicit threshold `k` and one source set `X` for which

\[
|B_{<k}\cap H(X)|
>
|B_{<k}|-|X|+\epsilon_k.
\]

Thus the remaining superregular task is a geometric common-hole intersection theorem for the actual bounded-cycle switching graph, including its conditioned versions.

## Finite check

`scripts/verify_superregular_common_hole_deficiency.py` exhausts small Hall-feasible bipartite graphs, compares maximum matching ranks with the exact common-hole formula, verifies the threshold-cost sum, and checks compatible endpoint conditioning.
