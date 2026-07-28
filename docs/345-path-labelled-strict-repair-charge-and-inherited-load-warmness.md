# Path-labelled strict-repair charge and inherited-load warmness

`docs/341` compresses an arbitrary strict-repair phase into the inherited
terminal cycle load `a_F` and shows that the subsequent clean action has density

```text
h_F(rho)=a_F(rho)/v(rho).
```

This chapter identifies the exact source of concentration inside `h_F`.
A fixed labelled locally coupled repair path is injective, so all predecessor
merging comes from collisions between distinct path words.

No asymptotic warmness, mixing, or termination theorem is claimed.

## 1. Reversible local step labels

A locally coupled successor step is specified by:

1. its source-owner triple `T`;
2. the successor reassignment of the three outgoing targets;
3. the sign-change mask `z subseteq T`.

The step is defined only on signed Hamilton states for which the resulting
cycle and orientation satisfy the policy's admissibility conditions.

### Proposition PP3bpz -- PROVED / LABELLED STEP INJECTIVITY

Every fixed locally coupled step label is a partial bijection on signed
Hamilton states.

#### Proof

The successor reassignment permutes three distinct outgoing targets among the
three labelled sources.  That permutation is invertible, and the inverse
reconstructs the unique source Hamilton cycle from the target cycle and the
step label.  The sign update is XOR with the recorded mask `z`, hence is also
invertible.  Therefore two distinct source signed states cannot produce the
same target signed state under one fixed label. ∎

The same statement holds if the step label includes additional deterministic
acceptance data, since restricting the domain of a partial bijection preserves
injectivity.

## 2. Repair words have unique labelled predecessors

A repair word

```text
w=(ell_1,...,ell_k)
```

is a sequence of locally coupled step labels.  Write `Phi_w` for its partial
state transformation.

### Corollary PP3bqa -- PROVED / PATH-WORD INJECTIVITY

For every fixed repair word `w`, `Phi_w` is a partial bijection.  Consequently,
for any terminal signed state `y`, there is at most one source signed state

```text
x=Phi_w^(-1)(y)
```

that reaches `y` using `w`.

#### Proof

A composition of partial bijections is a partial bijection. ∎

Thus a single word never creates predecessor multiplicity.  Any large terminal
column must be assembled from many different words.

## 3. Exact path-collision formula

Fix a family `F` of source signed states.  Let a strict policy assign to each
`x in F` a probability `Q_x(w)` of using repair word `w`; the value is zero
when the word is inadmissible from `x`.  Words may have different lengths and
may terminate on different parity-clean states.

For a parity-clean signed terminal state `y`, let

```text
L_F(y)
```

be its total incoming strict-repair mass.

### Theorem PP3bqb -- PROVED / EXACT WORD-COLLISION COLUMN FORMULA

For every terminal state `y`,

```text
L_F(y)
 = sum_w 1[Phi_w^(-1)(y) exists in F]
         Q_(Phi_w^(-1)(y))(w).
```

In particular, each word contributes at most one predecessor term.

#### Proof

Expand the strict kernel by path word:

```text
L_F(y)
 = sum_(x in F) sum_w Q_x(w) 1[Phi_w(x)=y].
```

For a fixed `w`, PP3bqa implies that at most one `x` satisfies
`Phi_w(x)=y`.  Replacing the inner source sum by that unique inverse
predecessor gives the formula. ∎

This is an exact decomposition, not a union bound.  It includes collisions
between different lengths, different source triples, and different local sign
updates.

## 4. Warmness after terminal fibre regeneration

For a clean cycle `rho`, let `Omega(rho)` be its clean orientation fibre and

```text
v(rho)=|Omega(rho)|.
```

The inherited load from `docs/341` is

```text
a_F(rho)=sum_(y in Omega(rho)) L_F(y).
```

### Theorem PP3bqc -- PROVED / COLLISION-TO-WARMNESS REDUCTION

The inherited density is the average strict column mass in the terminal fibre:

```text
h_F(rho)
 = a_F(rho)/v(rho)
 = [1/v(rho)] sum_(y in Omega(rho)) L_F(y).
```

Consequently,

```text
||h_F||_infinity <= ||L_F||_infinity.
```

If `K` is any stochastic clean-cycle kernel, then for every `t>=0`,

```text
||K^t h_F||_infinity <= ||h_F||_infinity
                      <= ||L_F||_infinity.
```

#### Proof

The first identity is the definition of `a_F`, divided by the fibre size.
An average cannot exceed the maximum summand, proving the first norm bound.
A stochastic kernel maps each value to a convex combination of previous
values, so it is an `L^infinity` contraction. ∎

Thus the strict-to-clean action switch cannot increase an already controlled
signed-state column charge.  Fibre regeneration can strictly improve it by
averaging uneven terminal columns over one cycle.

## 5. A usable word-weight bound

For every word `w`, put

```text
q(w)=sup_(x in F) Q_x(w).
```

### Corollary PP3bqd -- PROVED / PATH-WORD MERGING BOUND

The strict column charge and inherited warmness obey

```text
||L_F||_infinity
 <= sum_w q(w),

||h_F||_infinity
 <= sum_w q(w),

gamma_F(t)
 <= sum_w q(w)
```

for every subsequent clean heat time `t`.

More sharply, for a terminal state `y`, only words for which
`Phi_w^(-1)(y)` exists contribute.

#### Proof

Apply PP3bqb and bound each contributing predecessor probability by `q(w)`.
Then use PP3bqc and the exact switch heat-kernel formula PP3bpl. ∎

This bound is useful when path probabilities decay faster than the number of
words that can collide at one endpoint.  Counting all syntactically possible
words is generally too crude; the remaining problem is endpoint-specific word
merging.

## 6. Interaction with the owner light cone

Let `R(w)` be the union of owners touched by a word.  By PP3bpc, a predecessor
and terminal state connected by `w` agree on every owner outside `R(w)` and
have identical atomic supports disjoint from `R(w)`.

### Corollary PP3bqe -- PROVED / LIGHT-CONE COLLISION FILTER

For a fixed terminal state `y` and word `w`, the unique possible predecessor
is obtained by changing only assignments of owners in `R(w)`.  Therefore the
indicator in PP3bqb vanishes unless the source-family conditions defining `F`
are compatible with `y` outside `R(w)`.

In particular, a selected source flaw whose owner assignments are disjoint
from `R(w)` must already be present with the same assignments in `y`.

#### Proof

Reverse PP3boz along the word.  Every owner outside the union of rotated
triples retains its signed assignment at every step. ∎

This filter links charge to geometric locality: most words cannot contribute
to most terminal columns when their owner light cones are incompatible with
the defining source flaw.

## 7. Revised inherited-load frontier

The action-switch charge problem now has three separated layers.

1. **Within one word:** there is no predecessor multiplicity.
2. **Across words:** exact concentration is the endpoint collision sum in
   PP3bqb.
3. **After parity cleaning:** fibre regeneration averages signed terminal
   columns, and the clean heat kernel contracts the resulting density.

The remaining asymptotic task is to design or analyze a strict policy whose
different repair words have small endpoint collision sums.  The useful inputs
are:

- many covering rotations from the cycle coordinate;
- low-cost boundary solutions from `docs/343` and `docs/344`;
- owner-light-cone incompatibility from `docs/338`;
- and clean-cycle mixing after the switch.

The next theorem identifier after this chapter is `PP3bqf`.
