# LLL-distribution spread for square-root macro patches

PP3dn proves that the product slot model has internally clean assignments, but
raw avoidance density may be small.  The conditional LLL-distribution theorem
still gives fixed-rank spread because a cylinder event meets only `O(qn^2)`
internal conflict events while each LLL activity is `Theta(1/n^2)`.

We use the standard LLL-distribution bound of Haeupler, Saha, and Srinivasan:
under asymmetric LLL activities `x(A)`, any event `B` satisfies

\[
 \Pr(B\mid\text{all conflicts avoided})
 \le
 \Pr(B)
 \prod_{A\in\Gamma(B)}(1-x(A))^{-1}.
\]

## 1. Uniform activities with slack

Use the slot model and conflict events of PP3dl--PP3dn.  Recall that

\[
 n=2W,
 \qquad
 p\le\frac8R,
 \qquad
 D\le2n^2.
\]

Put

\[
 x=\frac1{2n^2+1}.
\]

### Proposition PP3dp -- PROVED FROM THE PUBLISHED LLL-DISTRIBUTION THEOREM

If

\[
 \boxed{24(2n^2+1)\le R,}
\]

then the symmetric asymmetric-LLL inequalities hold with activity `x`.

#### Proof

For every conflict event,

\[
 x(1-x)^D
 \ge
 \frac1{2n^2+1}
 \left(1-\frac1{2n^2+1}\right)^{2n^2}.
\]

The final power is greater than `1/e`, and hence greater than `1/3`.  Therefore

\[
 x(1-x)^D
 >
 \frac1{3(2n^2+1)}
 \ge
 \frac8R
 \ge
 \Pr(A).
\]

Thus the LLL hypotheses hold. ∎

## 2. Cylinder inflation

Let `D_int` be the product distribution conditioned on avoiding all internal
pair and triple conflicts.  Because the original slot variables are independent
and uniform, `D_int` is the uniform distribution on all internally clean slot
assignments.

### Theorem PP3dq -- PROVED FROM THE PUBLISHED LLL-DISTRIBUTION THEOREM

Let `B` specify values for any `q` distinct slot variables.  Then

\[
 \boxed{
 \Pr_{D_{\rm int}}(B)
 \le
 \frac{e^{q/2}}{R^q}.
 }
\]

#### Proof

An event depending on `q` slots is adjacent only to conflict events containing
at least one of those slots.  The number of pair conflicts meeting them is at
most

\[
 \binom n2-\binom{n-q}2\le qn,
\]

and the number of triple conflicts is at most

\[
 \binom n3-\binom{n-q}3
 \le
 q\binom{n-1}2.
\]

For `n>=2`, their sum is at most `qn^2`.  The unconditional cylinder probability
is `R^{-q}`.  The LLL-distribution theorem gives

\[
 \Pr_{D_{\rm int}}(B)
 \le
 R^{-q}(1-x)^{-qn^2}.
\]

Since

\[
 -\log(1-x)
 \le
 \frac{x}{1-x}
 =
 \frac1{2n^2},
\]

one has `(1-x)^(-qn^2)<=e^(q/2)`. ∎

## 3. Grid-cell and pair spread

### Corollary PP3dr -- PROVED

Under `D_int`:

1. every prescribed movement or refill cell has probability at most

\[
 \boxed{
 \frac{2\sqrt e}{R};
 }
\]

2. every prescribed pair controlled by two distinct source edges has probability
at most

\[
 \boxed{
 \frac{4e}{R^2};
 }
\]

3. every fixed-rank pattern on `q` distinct controlling edges has probability
`O_q(R^{-q})`;
4. a movement/refill pair controlled by the same source edge has probability at
most `2 sqrt(e)/R`.

#### Proof

A prescribed cell can be realized by at most the two slots in one fibre of
`alpha` or `beta`.  A pair on distinct controlling edges has at most four slot
realizations.  Apply PP3dq and a union bound.  A same-edge pair is one-slot data
and has at most two compatible slots. ∎

The rank-one same-edge pair is the only local patch-pair class that does not gain
an additional power of `R`.  This agrees with the earlier width-two and
matching-block analyses.

## 4. Prime-gap-scale consequence

For

\[
 W=\lfloor\sqrt R/16\rfloor,
\]

one has `n^2<=R/64`; hence `24(2n^2+1)<=R` for all sufficiently large `R`.
Therefore every matching pool carries a uniform internally clean macro-state
distribution with:

\[
 W=Theta(\sqrt R),
 \qquad
 \Pr(\text{cell})=O(1/R),
 \qquad
 \Pr(\text{ordinary pair})=O(1/R^2).
\]

This closes the positive fixed-rank spread requirement in PP3dh.  The remaining
issues are no longer internal geometry or conditional-density loss; they are:

- opposite-layer cell and pair patterns;
- the rank-one same-source-edge movement/refill pair class;
- support-compressed cross-macro incidences.

The conditional distribution may have exponentially small total mass in the
raw product space, but this does not affect its fixed-rank marginals.