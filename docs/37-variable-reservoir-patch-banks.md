# Variable-reservoir patch banks

The fixed-reservoir endpoints PP2f--PP2k choose a completion after one deletion
set has already been fixed.  Some structured constructions, including translated
parabolic matching reservoirs, naturally offer a bank whose states delete
different old points.  This chapter gives the exact first-moment endpoint for
that situation.

## 1. Admissible variable-reservoir states

Let `S subseteq [m]^2` be saturated and no-three-in-line, and let `n=m+t`.
A state `omega` consists of:

- a deletion set `D_omega subseteq S`;
- an inserted set `Q_omega subseteq [n]^2`.

Assume every state satisfies:

1. `Q_omega` is disjoint from `S setminus D_omega`;
2. `(S setminus D_omega) union Q_omega` has exactly two points in every row and
   column of `[n]^2`;
3. `Q_omega` is internally no-three-in-line.

Let `Omega` be any probability distribution on such states.  No independence
between deletion and insertion is assumed.

For distinct points `x,y,z`, write `[x,y,z]` for the assertion that they are
collinear.

Define

\[
 \Gamma_1
 =
 \sum_{\substack{\{x,y\}\subseteq S,\ z\in[n]^2\\[x,y,z]}}
 \Pr(x,y\notin D_\omega,\ z\in Q_\omega),
\]

and

\[
 \Gamma_2
 =
 \sum_{\substack{x\in S,\ \{z,w\}\subseteq[n]^2\\[x,z,w]}}
 \Pr(x\notin D_\omega,\ z,w\in Q_\omega).
\]

Terms with repeated geometric points are omitted.

### Theorem PP2l -- PROVED

If

\[
 \boxed{\Gamma_1+\Gamma_2<1,}
\]

then some state `omega` gives a saturated no-three-in-line configuration on
`[n]^2`.

#### Proof

For one sampled state, let `Z_1` count final triples containing two retained
points of `S` and one point of `Q_omega`, and let `Z_2` count final triples
containing one retained point and two inserted points.  Linearity of expectation
gives

\[
 \mathbb E Z_1=\Gamma_1,
 \qquad
 \mathbb E Z_2=\Gamma_2.
\]

There are no triples wholly inside the retained set because it is a subset of
`S`, and none wholly inside `Q_omega` by hypothesis.  Thus `Z=Z_1+Z_2` is the
complete triple count of the final state.

If `E Z<1`, some state has `Z=0` because `Z` is a nonnegative integer.  Its
degree condition already gives saturation. ∎

The theorem is deletion-aware: a candidate point on an old secant is harmless
in states that delete an endpoint of that secant, and a candidate pair through
an old anchor is harmless in states that delete the anchor.

## 2. Uniform joint-incidence form

Let `U` be the union of all possible inserted points.  Define the geometric
certificate sets

\[
 \mathcal C_1
 =
 \{(\{x,y\},z):\{x,y\}\subseteq S,\ z\in U,\ [x,y,z]\},
\]

\[
 \mathcal C_2
 =
 \{(x,\{z,w\}):x\in S,\ z,w\in U,\ [x,z,w]\}.
\]

### Corollary PP2m -- PROVED

Suppose

\[
 \Pr(x,y\notin D_\omega,\ z\in Q_\omega)\le\eta_1
\]

for every certificate in `mathcal C_1`, and

\[
 \Pr(x\notin D_\omega,\ z,w\in Q_\omega)\le\eta_2
\]

for every certificate in `mathcal C_2`.  If

\[
 \boxed{
 \eta_1|\mathcal C_1|+\eta_2|\mathcal C_2|<1,
 }
\]

then a valid state exists.

#### Proof

Bound every term in `Gamma_1` and `Gamma_2` by the corresponding uniform joint
probability and apply PP2l. ∎

The joint probabilities are the correct quantities.  Separate deletion and
insertion marginals need not factor and should not be treated as independent.

## 3. Deletion-blind fallback

Sometimes only the inserted-state marginals are known.  Since survival events
can only lower probabilities,

\[
 \Pr(x,y\notin D_\omega,\ z\in Q_\omega)
 \le
 \Pr(z\in Q_\omega),
\]

and

\[
 \Pr(x\notin D_\omega,\ z,w\in Q_\omega)
 \le
 \Pr(z,w\in Q_\omega).
\]

### Corollary PP2n -- PROVED

It is sufficient that

\[
 \sum_{(e,z)\in\mathcal C_1}\Pr(z\in Q_\omega)
 +
 \sum_{(x,P)\in\mathcal C_2}\Pr(P\subseteq Q_\omega)
 <1.
\]

This is weaker than PP2l because it ignores certificates cleared by the chosen
deletion.  It is nevertheless useful when a variable-reservoir bank has strong
cell and pair spread but its deletion correlations have not yet been analyzed.

## 4. Failure localization

### Corollary PP2o -- PROVED

If every state in the support of `Omega` has a triple, then

\[
 \Gamma_1+\Gamma_2\ge1.
\]

In particular, if both certificate sets are finite and nonempty, some joint
certificate event has probability at least

\[
 \frac1{|\mathcal C_1|+|\mathcal C_2|}.
\]

#### Proof

Every state then has `Z>=1`, so `E Z>=1`.  The second assertion is the
pigeonhole principle applied to the summands of `Gamma_1+Gamma_2`. ∎

This is a weak but exact concentration certificate.  Stronger preparation
theorems should exploit the geometry of the concentrated old pair, old anchor,
or reservoir family.

## 5. Application to parabolic matching reservoirs

Every state from PP3ae satisfies the admissibility hypotheses:

- the matching deletion and parabolic insertion preserve saturation;
- the inserted patch is internally no-three.

A prepared seed may therefore offer many translated parabolic matching
reservoirs and sample among them.  PP2l says that the remaining task is exactly
to make the deletion-aware retained-pair and retained-anchor expectation below
one.  No candidate-only triple term remains.

The script

```bash
python scripts/analyze_parabolic_matching_reservoir.py \
  certificates/prime-patching-small.json --widths 2
```

records the exact two certificate counts for every finite state.  Its histogram
can be averaged directly to test PP2l for the uniform distribution on the
enumerated reservoir bank.
