# Regular-language constrained prefix-code dynamic programming

`docs/504` canonicalizes risk-decorated prefix trees.  A geometric marker word
may also have to obey a finite local legality rule, such as avoiding a forbidden
adjacent pattern.  This chapter incorporates any deterministic finite automaton
directly into the unequal-survival prefix-code recurrence.

Let `Q` be a deterministic automaton with transition `delta(q,b)` for
`b in {0,1}` and accepting states `F`.  Risk class `i` has risk `rho_i` and
multiplicity `m_i`.  Symbol survivals are `p_0,p_1`.

## 1. Product-state recurrence

### Theorem PP3cji -- PROVED / REGULAR-LANGUAGE PREFIX OPTIMUM

For an automaton state `q` and multiplicity vector `n`, let `V(q,n)` be the
minimum possible maximum realized risk among prefix codes whose continuation
words start from `q` and finish in accepting states.  For a unit vector `e_i`,

```text
V(q,e_i)=rho_i  if q in F,
V(q,e_i)=infinity otherwise.
```

For `|n|>1`,

```text
V(q,n)=min_(0<a<n) max(
    V(delta(q,0),a)/p_0,
    V(delta(q,1),n-a)/p_1).
```

#### Proof

Every nontrivial binary prefix tree has a unique nonempty partition of its leaves
between the zero and one children.  The automaton state updates by the chosen
symbol, and prefixing divides survival by that symbol's survival probability.
Conversely, any feasible pair of child codes combines to a feasible prefix code.
Induction on `|n|` proves the recurrence. ∎

## 2. Multiplicity quotient survives automaton constraints

### Theorem PP3cjj -- PROVED / AUTOMATON--MULTIPLICITY PRODUCT QUOTIENT

If banks in one risk class are interchangeable, `V(q,n)` depends only on the
automaton state and the class multiplicities, not on bank labels.  The exact
state space has at most

```text
|Q| product_i (m_i+1)
```

states, and labeled schedules lift from any optimal multiplicity split exactly
as in the unconstrained quotient recurrence.

#### Proof

The automaton reads only the common prefix word, while the objective reads only
risk class and survival.  Relabeling banks inside one class changes neither.
Thus the induction in `PP3cji` closes on multiplicity vectors. ∎

## 3. Reconstruction and obstruction

### Theorem PP3cjk -- PROVED / REGULAR-CODE FINITE CERTIFICATE

Storing one optimal split for every finite product state reconstructs an explicit
labeled legal prefix code.  If the root value is infinite, the exhausted finite
recurrence is an exact infeasibility certificate.  Verification checks automaton
acceptance, prefix-freeness, class multiplicities, and every leaf risk.

#### Proof

Recursive splitting constructs the tree and its labels.  The checks reproduce
the induction of `PP3cji`; absence of any feasible split at a state proves that
no legal subtree exists there. ∎

## 4. Stored exact fixture

The audit `scripts/check_regular_language_prefix_code_dp.py` forbids the pattern
`00`, uses survivals `(3/4,2/3)`, risks `(1/32,1/16,1/8)`, and multiplicities
`(3,2,1)`.  The unconstrained optimum is `3/16`; the regular-language optimum is
`243/1024`.  A canonical optimal code is

```text
c1: 0
b1: 10
b2: 110
a1: 1110
a2: 11110
a3: 11111.
```

The product recurrence has 26 feasible states in the stored range.

## 5. Prime-patching consequence

Marker-code optimization can now enforce finite geometric legality during the
search rather than filtering illegal words afterward.  Any support-local rule
recognized by a finite automaton adds only a finite state factor to the exact
multiplicity dynamic program.
