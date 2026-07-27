# Impossible owner-pair ray classification and asymptotic rarity

`docs/316` and `docs/320` separate parity inconsistency into two mechanisms:
a pair-local obstruction, where one owner pair forbids both XOR values, and
signed-cycle frustration among individually consistent XOR edges.  The first
mechanism is now completely explicit and asymptotically negligible under the
uniform Hamilton-cycle measure.

No asymptotic parity-satisfiability or seed theorem is claimed.

## 1. Centered square normal form

For a pair assignment `s->t`, put

```text
u=2m-1-2s,
v=2m-1-2t.
```

These are positive odd integers.  After translating the board centre to the
origin and multiplying coordinates by two, orientation zero is the quarter-turn
orbit

```text
Q(u,v)={(u,v),(-v,u),(-u,-v),(v,-u)},
```

while orientation one is the reflected orbit `Q(u,-v)`.

### Proposition PP3bmn -- PROVED / CENTERED SECANT NORMAL FORM

The six secants of `Q(u,v)` consist of two diagonals through the origin and four
quarter-turn images of

```text
(u-v)X+(u+v)Y=u^2+v^2.
```

Consequently every two-owner flaw is either a diagonal incidence, in which the
two centered direction pairs are proportional up to coordinate swap, or a side
incidence satisfying one of the corresponding signed linear equations.

#### Proof

The four displayed points are the vertices of a square centred at the origin.
Its opposite-vertex lines are the two diagonals.  The side through `(u,v)` and
`(-v,u)` has normal `(u-v,u+v)` and the displayed constant; quarter-turning this
line gives the remaining sides.  A two-owner collinear triple uses two points
from one square and one from the other, so it is exactly a vertex-on-secant
incidence. ∎

## 2. Exact pair-local impossibility classification

Call a compatible pair of directed assignments **locally impossible** when both
relative orientation parities contain a two-owner flaw.  Compatibility means
distinct sources, distinct targets, and no fixed directed edge.

### Theorem PP3bmo -- PROVED / EXACT RAY--MULTIPLIER CLASSIFICATION

A compatible assignment pair with centered coordinates `(u,v)` and `(x,y)` is
locally impossible if and only if the following conditions hold.

First, the centered directions lie on the same ray up to coordinate swap.  Thus
there are coprime positive odd integers `a,b` and positive odd multipliers `k,l`
such that either

```text
(u,v)=k(a,b),  (x,y)=l(a,b),
```

or

```text
(u,v)=k(a,b),  (x,y)=l(b,a).
```

Second, writing

```text
R  = a^2+b^2,
D+ = |a^2+2ab-b^2|,
D- = |a^2-2ab-b^2|,
```

at least one multiplier equation holds:

```text
Rk=D+l,  Rl=D+k,
Rk=D-l,  Rl=D-k.
```

Here `D+l` and `D-l` mean `D_+ l` and `D_- l`, respectively, and similarly for
the equations with `k`.

#### Proof

Use PP3bmn for one equal-orientation incidence and one opposite-orientation
incidence.  If either incidence is diagonal, proportionality up to coordinate
swap is immediate.  If both are side incidences with the same host square,
comparing the two signed side equations after squaring forces `u=v` or `x=y`,
contrary to the derangement condition.  If the host squares differ, eliminating
the side constants in each of the finitely many sign choices gives one of

```text
uy-vx=0,
ux-vy=0.
```

Thus the ray representation follows.

Substitute `(u,v)=k(a,b)` and either aligned or swapped
`(x,y)=l(a,b)` into the opposite-orientation side equations.  After dividing by
the nonzero common scale, the four possible side incidences are exactly

```text
Rk=D_+l, Rl=D_+k, Rk=D_-l, Rl=D_-k.
```

Conversely, ray proportionality supplies the equal-orientation diagonal flaw,
and any one of the multiplier equations supplies an opposite-orientation side
flaw.  Coordinate swap interchanges `D_+` and `D_-` up to sign, so the same four
equations cover both ray forms. ∎

The formula explains the sparse threshold behaviour observed computationally.
For example, the first family has primitive direction `(3,1)` and reduced
multiplier pairs `(5,1)` and `(7,5)`.

## 3. Only `O(m log m)` impossible compatible pairs

Let `H_m` be the number of compatible directed-assignment pairs that are locally
impossible.

### Theorem PP3bmp -- PROVED / SPARSE PAIR-LOCAL OBSTRUCTION

```text
H_m=O(m log m).
```

#### Proof

Fix a primitive odd direction `(a,b)` and one of `D_+,D_-`; put
`g=gcd(R,D)`.  The multiplier equation forces `(k,l)`, up to reversal and a
common positive factor `q`, to be

```text
(k,l)=q(D/g,R/g).
```

Let `A=max(a,b)`.  For `D_+`, the gcd divides

```text
R-(a^2+2ab-b^2)=2b(b-a),
```

and `gcd(R,b)=1`, so `g<=2|a-b|<=2A`.  For `D_-`, the analogous difference is
`2b(a+b)`, hence `g<=2(a+b)<=4A`.  Therefore

```text
max(R,D)/g >= A/4.
```

The largest centered coordinate in the minimal parameter pair is at least
`A^2/4`.  Since every centered coordinate is at most `2m-1`, only directions
with `A=O(sqrt(m))` occur, and for one direction the common factor has at most
`O(m/A^2)` choices.

There are `O(A)` ordered primitive pairs with maximum coordinate `A`.  Summing
and allowing the constant number of choices of `D`, multiplier reversal,
coordinate swap, and source ordering gives

```text
H_m
 = O(sum_(A<=C sqrt(m)) A*m/A^2)
 = O(m log m).
```

∎

## 4. A uniform Hamilton cycle is pair-locally safe with high probability

### Corollary PP3bmq -- PROVED / PAIR-LOCAL OBSTRUCTION VANISHES

Let `rho` be a uniform directed Hamilton cycle on `m` pair vertices.  Then

```text
Pr(rho contains a locally impossible owner pair)
 = O(log m/m).
```

In particular, asymptotically almost every Hamilton cycle avoids every owner
pair that forbids both XOR values.

#### Proof

A fixed compatible pair of directed edges either cannot belong to a Hamilton
cycle or forms a two-edge directed path forest.  In the latter case the exact
Hamilton cylinder formula gives

```text
Pr(both edges occur)=1/[(m-1)(m-2)].
```

Apply the union bound over `H_m=O(m log m)` pairs from PP3bmp. ∎

This removes the pair-local mechanism from the asymptotic clean-cycle frontier.
The remaining parity obstruction is signed-cycle frustration among individually
consistent XOR edges.

## 5. Exact finite audit through `m=80`

The geometric predicate and PP3bmo were compared for every compatible assignment
pair for `4<=m<=80`.  The number of impossible pairs grows from zero through
`m=7` to only `52` at `m=80`.

Compile and run

```bash
g++ -O3 -std=c++17 \
  scripts/check_hamilton_impossible_owner_pair_classification.cpp \
  -o /tmp/check_hamilton_impossible_owner_pair_classification
/tmp/check_hamilton_impossible_owner_pair_classification
```

The stored ledger is

```text
experiments/hamilton-impossible-owner-pair-classification-audit.json.
```

## 6. Revised parity frontier

The next parity results should address the signed-cycle mechanism rather than
pair-local impossibility:

1. bound the expected number and length distribution of signed parity cycles in
a uniform pair-safe Hamilton cycle;
2. prove a switching or local-repair theorem that destroys a frustrated signed
cycle while preserving pair safety;
3. combine pair-safe abundance with owner-intersecting clean mobility;
4. determine whether a sparse biased cycle measure makes the parity graph
subcritical;
5. control merged rotation-label charge on the pair-safe clean manifold.
