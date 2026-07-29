# Singularity analysis of regular prefix-tree series

`docs/522` proves coefficientwise stabilization of automaton-constrained prefix
trees. For the basic legality rule forbidding `000`, the algebraic system can
be eliminated completely, giving an exact coefficient formula and exponential
schedule entropy.

A leaf is legal when its root-to-leaf word contains no `000`. Let `T_q(z)`
count ordered full binary trees whose current automaton state is `q`, with `z`
marking leaves.

## 1. Algebraic automaton system

### Theorem PP3clk -- PROVED / REGULAR-TREE ALGEBRAIC SYSTEM

For a deterministic binary automaton with accepting states `F`, the legal-tree
series satisfy

```text
T_q(z)=1_(q in F) z + T_delta(q,0)(z) T_delta(q,1)(z),
```

with a forbidden dead state assigned series zero. This finite polynomial
system uniquely determines all coefficients recursively from the zero constant
term.

#### Proof

A legal tree is either one accepted leaf or an ordered pair of legal child
trees reached by symbols zero and one. The decomposition is disjoint and
exhaustive. Since every product raises leaf degree, coefficient induction gives
uniqueness. ∎

## 2. Exact elimination and coefficients for avoiding `000`

### Theorem PP3cll -- PROVED / LEGAL-TREE LAGRANGE FORMULA

For the automaton recording the number of trailing zeroes, the root series
`T=T_0` satisfies

```text
T=z+zT+zT^2.
```

Consequently

```text
[z^n]T = (1/n) [u^(n-1)] (1+u+u^2)^n.
```

Equivalently, the coefficient is the finite integer sum over
`k+2j=n-1` of

```text
(1/n) n!/(j! k! (n-j-k)!).
```

#### Proof

The state with two trailing zeroes can only terminate or take a one-edge before
branching, which gives `T_2=z`; then `T_1=z+zT_0` and
`T_0=z+T_1T_0`. Elimination gives the displayed quadratic recurrence.
Lagrange inversion applied to `T=z(1+T+T^2)` gives the coefficient formula. ∎

## 3. Dominant singularity and schedule entropy

### Theorem PP3clm -- PROVED / LEGAL-TREE ASYMPTOTIC

The exact solution with zero constant term is

```text
T(z)=(1-z-sqrt((1-3z)(1+z)))/(2z).
```

Its dominant singularity is `z=1/3`, and

```text
[z^n]T ~ (sqrt(3)/(2 sqrt(pi))) 3^n n^(-3/2).
```

#### Proof

The other branch of the quadratic has a pole at the origin and is rejected.
The nearest radical zero is `1/3`; the second is `-1`. Near `1/3`,

```text
T(z)=1-sqrt(3) sqrt(1-3z)+O(1-3z).
```

The binomial expansion and Stirling's formula give
`[z^n](1-3z)^(1/2) ~ -3^n/(2 sqrt(pi)n^(3/2))`, yielding the stated constant. ∎

## 4. Stored exact fixture

The audit `scripts/check_regular_prefix_singularity.py` verifies the recurrence,
quadratic identity, and Lagrange formula through 100 leaves. The first ten
coefficients are

```text
1,1,2,4,9,21,51,127,323,835.
```

At `n=100`, the scaled coefficient
`a_n n^(3/2)/3^n` is approximately `0.48407`, approaching
`sqrt(3)/(2 sqrt(pi))`.

## 5. Prime-patching consequence

The legal support-chord schedule family is not merely finite-state enumerable:
its exact exponential growth constant is three, with the universal binary-tree
`n^(-3/2)` correction. This quantifies the entropy available after imposing a
local geometric word rule.
