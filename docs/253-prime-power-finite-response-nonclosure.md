# Finite response does not by itself force minimum zero

CMR1134--CMR1189 make the selected minimum response system finite: routing,
rollbacks, protected growth, blocker covers, unit walls, small factors, and lifted
interface targets all have canonical responses.  This is substantial structural
progress, but it is not yet a contradiction to a positive minimum.

A finite response tree can end with a dirty conditioned anchor even when every
escape state has strictly larger potential.  Exact contraction preserves the
induced minimum; it does not lower it.  Unit-wall and child descent reduce matching
side; they do not automatically remove triples already stored in the fixed
interface.  The missing theorem must compare destroyed target load with created
collateral across a complete response bank and force one state below the current
minimum.

This chapter records the nonclosure explicitly to prevent a finite termination
statement from being mistaken for the no-three-in-line theorem.

## 1. Abstract positive-minimum response model

Let

\[
\mathcal F=\{S,Q_1,Q_2\}
\]

with objective

\[
\Phi(S)=1,
\qquad
\Phi(Q_1)=\Phi(Q_2)=2.
\]

Assume `S` contains one designated target and each `Q_i` destroys it while creating
two replacement targets.

### Theorem CMR1190 -- PROVED

The family has a strict positive minimum at `S`.  Every target-destroying response
is nonimproving, even though the response family is finite and all target
transitions are explicitly classified.

### Proof

The displayed objective values give

\[
\min_{R\in\mathcal F}\Phi(R)=1>0,
\]

and both response values equal two. ∎

This model satisfies the robust-surplus inequality with destroyed load one and gap
one.

## 2. Conditioning can terminate at a dirty singleton

### Theorem CMR1191 -- PROVED

Restricting the abstract family to the anchor prescription which uniquely selects
`S` produces the singleton family `{S}`.  Exact contraction of that prescription
preserves induced minimum value one.

### Proof

The anchor survives the restriction and remains the only state.  By definition of
the induced objective, its residual lift still has value `Phi(S)=1`. ∎

Thus host-representable contraction is compatible with a positive induced
minimum.

## 3. Finite currency exhaustion is not a potential inequality

### Theorem CMR1192 -- PROVED

A proof that every canonical episode consumes one member of a finite stock implies
termination of that scheduler, but does not imply that the terminal minimum value
is zero.

### Proof

The model of CMR1190 can be assigned any finite episode stock.  After inspecting
both response states and conditioning on `S`, the stock is exhausted and the
terminal minimum remains one. ∎

Therefore CMR1140--CMR1189 are finite-response and descent theorems, not a complete
minimum-zero theorem.

## 4. Exact averaging criterion for improvement

Let `S` have current minimum value `m`, and let `B` be any nonempty finite bank of
feasible response states.  Let `mu` be any probability distribution on `B`.

### Theorem CMR1193 -- PROVED

If

\[
\boxed{
\mathbb E_{Q\sim\mu}\Phi(Q)<m,
}
\]

then some bank state satisfies

\[
\boxed{
\Phi(Q)<m.
}
\]

Conversely, if every bank state has value at least `m`, then every distribution on
that bank has expectation at least `m`.

### Proof

An average cannot be smaller than all of its summands.  The converse is immediate
from nonnegative averaging weights. ∎

This is the exact logical bridge still required.

## 5. Destroyed-load versus collateral form

For a transition from `S` to `Q`, write

\[
L(Q)=|\mathcal T(S)\setminus\mathcal T(Q)|,
\qquad
N(Q)=|\mathcal T(Q)\setminus\mathcal T(S)|.
\]

Then

\[
\Phi(Q)-\Phi(S)=N(Q)-L(Q).
\]

### Theorem CMR1194 -- PROVED

A response bank forces strict improvement whenever it has a distribution `mu`
satisfying

\[
\boxed{
\mathbb E_\mu N(Q)
<
\mathbb E_\mu L(Q).
}
\]

If every response is minimum-robust, then every distribution satisfies the reverse
weak inequality.

### Proof

Average the exact new-minus-lost identity and apply CMR1193. ∎

Hence the final target is a quantitative target-versus-collateral inequality.

## 6. What the finite-response machinery contributes

### Theorem CMR1195 -- PROVED

The existing finite-response normal forms reduce the averaging problem to finitely
many canonical certificate classes:

1. active residual targets and their degree-two banks;
2. fixed-core targets at canonical lifted owners;
3. loaded-line and simultaneous secant-star banks;
4. minimal blocker unit-wall factors;
5. side-three singleton response banks;
6. rigid side-one/two induced interfaces.

Within each class, exact duplicate states, routing relabellings, same-value
rollbacks, and redundant blocker edges may be removed without changing the
minimum-zero question.

### Proof

Use CMR1094--CMR1189.  Every listed normalization preserves one selected minimum
or gives strict descent/improvement; the removed operations are idempotent or
redundant. ∎

Thus the remaining inequality is finite and structured, not an uncontrolled
history problem.

## 7. Required global inequality

### Theorem CMR1196 -- OPEN TARGET

A sufficient final prime-power theorem would assign nonnegative weights to the
canonical response banks of every dirty selected minimum `S` such that the weighted
average satisfies

\[
\sum_B w_B
\mathbb E_{Q\in B}N(Q)
<
\sum_B w_B
\mathbb E_{Q\in B}L(Q),
\qquad
\sum_Bw_B>0.
\]

By CMR1194, one response state would then have smaller potential.

The weights must respect:

- host availability and blocker-wall factorisation;
- fixed-interface lifting;
- rank-zero/rank-one/rank-two collateral;
- prime-field and thin quotient/carry cases;
- CRT assembly for arbitrary side lengths.

This statement is recorded as an open target, not as proved.

## 8. Revised frontier

### Corollary CMR1197 -- PROVED

The current frontier is the **global target-versus-collateral inequality**.  Finite
scheduler response, unit-wall descent, small-factor classification, and lifted
interface ancestry are supporting reductions.  They do not by themselves imply
that a positive minimum is impossible.

Any claimed completion must exhibit an actual lower-potential state, or an
averaging inequality which guarantees one, before asserting the no-three-in-line
conjecture.

### Proof

Combine CMR1190--CMR1196. ∎

No all-`n` theorem is claimed.  The abstract countermodel, induced contraction,
finite-stock nonimplication, and averaging identities are checked in
[`scripts/verify_prime_power_finite_response_nonclosure.py`](../scripts/verify_prime_power_finite_response_nonclosure.py).
