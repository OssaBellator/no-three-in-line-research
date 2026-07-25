# Weighted line-clean averaging converts cheap availability into improvement, collateral mass, or unavailable-edge depletion

CMR497--CMR501 price the minimum restoration needed to execute one universal
line-clean cylinder.  The remaining issue is selection: a minimum-restoration
completion can be highly nonuniform inside the current restricted host, so the
full derangement spread from CMR332 cannot simply be conditioned on the minimum
face.

This chapter avoids that conditioning.  Average simultaneously over the full
line-clean derangement cylinder, charging every unavailable edge by weight
`1/q`.  The restoration term has an exact expectation because every allowed
residual edge has derangement marginal `1/(n-1)`.  If the weighted expectation
is below one, some completion creates no candidate-only triple and restores
fewer than `q` edges.  Failure therefore forces either the frozen collateral
mass of CMR334 or a large inventory of unavailable residual edges.

Use the notation of CMR330--CMR334 and CMR497.  Fix one paid line `L`, delete the
two source and two target vertices of its paid pair, and put

\[
n=t-2\ge5.
\]

After relabelling the forbidden perfect matching `F_L` as the identity, let

\[
\mathcal D_L
=
\{\delta\in S_n:\delta(i)\ne i\text{ for every }i\}
\]

be the line-clean residual derangements.  Let

\[
B_L
=
E(U_L)\setminus E(G_L)
\]

be the allowed residual edges which are currently unavailable.  For
`\delta\in\mathcal D_L`, define

\[
r_L(\delta)=|\delta\cap B_L|.
\]

Let `X_L(\delta)` denote the number of candidate-only triples created by the
completed paid-pair state.  As in CMR333, put

\[
S_L
=
\frac{V_0(L)}{(n)_3}
+
\frac{V_1(L)}{(n)_2},
\qquad
A_L=\frac{30}{11}S_L.
\]

Then CMR333 gives

\[
\mathbb E_{\delta\in\mathcal D_L}X_L(\delta)\le A_L.
\]

## 1. Exact restoration marginal

### Theorem CMR502 — PROVED

For every allowed residual edge `e\in U_L`,

\[
\boxed{
\Pr_{\delta\in\mathcal D_L}(e\in\delta)
=
\frac1{n-1}.
}
\]

Consequently,

\[
\boxed{
\mathbb E_{\delta\in\mathcal D_L}r_L(\delta)
=
\frac{|B_L|}{n-1}.
}
\]

### Proof

Fix a residual source vertex.  Under the uniform derangement law its image is
symmetric among the `n-1` nonidentity targets, and exactly one of those targets
is chosen.  Hence every allowed edge in that row has probability `1/(n-1)`.
Sum the indicators over `B_L`. ∎

This expectation is exact and requires no density or matchability property of
the current host `G_L`.

## 2. Weighted cheap-clean selection

### Theorem CMR503 — PROVED

Fix an integer threshold

\[
q\ge1.
\]

There is a line-clean completion `\delta\in\mathcal D_L` satisfying

\[
\boxed{
X_L(\delta)+\frac{r_L(\delta)}q
\le
A_L+
\frac{|B_L|}{q(n-1)}.
}
\]

In particular, if

\[
\boxed{
A_L+
\frac{|B_L|}{q(n-1)}
<1,
}
\]

then some line-clean completion has

\[
\boxed{X_L(\delta)=0,
\qquad
r_L(\delta)<q.}
\]

### Proof

Average the displayed weighted quantity over `\mathcal D_L`.  CMR333 bounds the
first expectation by `A_L`, and CMR502 evaluates the second one exactly.  Some
state is no larger than the average.

If the right side is below one, the nonnegative integer `X_L(\delta)` cannot be
positive.  Thus `X_L(\delta)=0`, and then `r_L(\delta)/q<1`; since restoration
cost is integral, `r_L(\delta)<q`. ∎

The theorem selects a cheap clean completion directly from the full cylinder;
it does not condition on a minimum-cost face.

## 3. Frozen-bank selection inequality

Assume the current parent state is globally minimal among positive-potential
saturated states, as in CMR334.  A completion with `X_L=0` destroys the chosen
old target and creates no candidate-only replacement triple.  If a required
replacement certificate uses an outside point, retain the anchored continuation
from CMR334.

### Corollary CMR504 — PROVED

If neither an anchored outside continuation nor a line-clean completion with

\[
X_L(\delta)=0,
\qquad
r_L(\delta)<q
\]

exists, then every paid line `L` satisfies

\[
\boxed{
\frac{30}{11}S_L
+
\frac{|B_L|}{q(n-1)}
\ge1.
}
\]

For an equal-size paid-line family `\mathcal R`, write

\[
\overline S
=
\frac1{|\mathcal R|}\sum_{L\in\mathcal R}S_L,
\qquad
\overline b
=
\frac1{|\mathcal R|}\sum_{L\in\mathcal R}|B_L|.
\]

Then

\[
\boxed{
\frac{30}{11}\overline S
+
\frac{\overline b}{q(n-1)}
\ge1.
}
\]

For every real `0<\alpha<1`, at least one of the following holds:

1. **Frozen collateral mass.**
   \[
   \boxed{
   \overline S
   \ge
   \frac{11}{30}(1-\alpha).
   }
   \]
2. **Unavailable-edge depletion.**
   \[
   \boxed{
   \overline b
   \ge
   \alpha q(n-1).
   }
   \]

### Proof

If the one-line inequality failed, CMR503 would supply a cheap clean completion.
Average the resulting inequalities over the equal-size cylinders.  If the first
alternative fails, the first term in the averaged inequality is below
`1-\alpha`, so the second term is greater than `\alpha`. ∎

CMR334 is recovered when all residual edges are available, so `B_L` is empty.
The new term measures exactly how much restricted-host availability can replace
frozen collateral concentration.

## 4. Concentrated or dispersed unavailable inventory

Put

\[
I_B
=
\sum_{L\in\mathcal R}|B_L|,
\qquad
U_B
=
\bigcup_{L\in\mathcal R}B_L.
\]

For an edge `e\in U_B`, let

\[
\mu(e)
=
|\{L\in\mathcal R:e\in B_L\}|.
\]

### Theorem CMR505 — PROVED

For every integer `\lambda\ge2`, at least one of the following holds.

1. **Cylinder concentration.** Some unavailable edge satisfies
   \[
   \boxed{\mu(e)\ge\lambda.}
   \]
2. **Dispersed unavailable inventory.**
   \[
   \boxed{
   |U_B|
   \ge
   \frac{I_B}{\lambda-1}.
   }
   \]

In the second branch, when `t=p^h`, the distinct unavailable edges carry exact
labelled full-token incidence

\[
\boxed{
\mathcal I(U_B)
=
(p+1)(h-1)|U_B|
\ge
(p+1)(h-1)
\frac{I_B}{\lambda-1}.
}
\]

If the unavailable-depletion branch of CMR504 holds, then

\[
I_B
\ge
\alpha q(n-1)|\mathcal R|,
\]

and hence the dispersed branch gives

\[
\boxed{
\mathcal I(U_B)
\ge
(p+1)(h-1)
\frac{\alpha q(n-1)|\mathcal R|}{\lambda-1}.
}
\]

### Proof

If the concentration branch fails, every edge belongs to at most
`\lambda-1` of the sets `B_L`.  Double-counting the incidences `(L,e)` gives

\[
I_B
=
\sum_{e\in U_B}\mu(e)
\le
(\lambda-1)|U_B|.
\]

The token identity is CMR413 applied to the distinct edge set `U_B`.  Substitute
the CMR504 lower bound for `I_B`. ∎

The concentrated branch isolates one previously unavailable cell which blocks
many line-clean cylinders.  The dispersed branch is a genuine protected-reserve
or host-depletion certificate with exact token mass.

## 5. Combined cheap-availability endpoint

### Corollary CMR506 — PROVED

Apply the line-clean cylinders to the rooted secant-star arms of CMR494 or the
bottleneck pairs of CMR496.  Fix `q\ge1`, `0<\alpha<1`, and
`\lambda\ge2`.  At least one of the following endpoints is available.

1. an anchored outside continuation;
2. a line-clean completion which destroys the selected inherited target, creates
   no candidate-only replacement triple, and restores fewer than `q` residual
   edges;
3. a minimum line-clean restoration footprint of size at least `q`, giving the
   strict forced-core factorization of CMR499;
4. frozen normalized rank-zero/rank-one collateral mass
   \[
   \overline S\ge\frac{11}{30}(1-\alpha);
   \]
5. one unavailable residual edge lies in at least `\lambda` cylinder inventories;
6. a dispersed set of distinct unavailable residual edges has the labelled
   full-token mass in CMR505.

### Proof

If a selected cylinder has minimum restoration cost at least `q`, use CMR499.
Otherwise apply CMR503--CMR504 to the cheap-availability cylinders.  The
unavailable branch is split by CMR505.  CMR494 and CMR496 provide the rooted-arm
and bottleneck paid pairs to which these cylinders are attached. ∎

This closes the purely numerical selection step.  Failure to find a cheap clean
completion is no longer an unstructured event: it produces the already-known
CMR334 collateral mass, exact host factorization, one repeated unavailable cell,
or a large distinct unavailable-edge inventory.

The remaining geometric task is to convert the repeated-cell branch into a
prefix, primitive-height, quotient, carry, Hall, reserve, or envelope
certificate, and to feed the dispersed unavailable inventory into the protected
reserve and ancestor-return budgets without double counting across parent
epochs.

No all-`n` theorem is claimed.  Derangement marginals, weighted selection, the
tunable arithmetic alternative, and unavailable-incidence counting are checked
in [`scripts/verify_prime_power_line_clean_weighted_selection.py`](../scripts/verify_prime_power_line_clean_weighted_selection.py).
