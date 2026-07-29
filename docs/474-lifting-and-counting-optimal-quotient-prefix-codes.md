# Lifting and counting optimal quotient prefix codes

`docs/468` reduces equal-risk banks to multiplicity-vector states.  This chapter
shows how an optimal quotient state is converted back into an explicit labeled
prefix code and how all labeled optimal codes can be counted exactly.

There are risk classes `i=1,...,r`, with `m_i` distinctly labeled banks in class
`i`, class risk `rho_i`, and symbol survivals `p_0,p_1`.  Let `V(m)` be the exact
multiplicity-state recurrence from `docs/450` and `docs/468`.

## 1. Constructive lifting

### Theorem PP3cfe -- PROVED / QUOTIENT-TO-LABELED CODE LIFT

Choose any optimal oriented split `a,m-a` at each nontrivial quotient state.
At that node, choose any `a_i` of the currently available labels from class `i`
for the zero child and send the rest to the one child.  Recursing produces a
labeled binary prefix code whose maximum realized risk is exactly `V(m)`.

#### Proof

The two child label sets are disjoint and have the prescribed multiplicity
vectors.  By induction, each child realizes its quotient value.  Prefixing by
zero or one divides the child risks by `p_0` or `p_1`, and optimality of the split
makes the larger value exactly `V(m)`.  Distinct branches are prefix separated. ∎

## 2. Exact optimizer count

### Theorem PP3cff -- PROVED / LABELED OPTIMUM COUNT RECURRENCE

Let `N(m)` be the number of optimal labeled codes with ordered zero and one
edges.  For a unit vector `e_i`, set `N(e_i)=1`.  Otherwise,

```text
N(m)=sum_(a optimal oriented split)
     [product_i binom(m_i,a_i)] N(a) N(m-a).
```

This recurrence counts every labeled optimum exactly once.

#### Proof

Every labeled ordered prefix tree has a unique set of labels entering its zero
child, hence a unique root count split and a unique choice among the
`product_i binom(m_i,a_i)` concrete subsets.  Its two optimal labeled subtrees
are then counted independently.  Conversely, every term constructs a distinct
labeled optimum. ∎

## 3. Canonical reconstruction certificate

### Theorem PP3cfg -- PROVED / FINITE LIFTING CERTIFICATE

Storing `V(m)`, one optimal split per state, and the resulting labeled leaf words
is a complete finite certificate.  Verification checks the quotient Bellman
inequalities, the recursive label partition, prefix-freeness, and every leaf risk.
Any failure identifies one state, split, duplicate label, prefix collision, or
overloaded leaf.

#### Proof

The checks exactly reproduce the inductive proof of `PP3cfe`; each is finite and
rational. ∎

## 4. Stored exact fixture

The audit `scripts/check_quotient_code_reconstruction.py` has multiplicities
`(3,3,2)`, survivals `(3/4,2/3)`, and risks `(1/32,1/16,1/8)`.  Its 47 quotient
states give exact optimum `1/4`.  The counting recurrence finds 2,304 optimal
labeled codes, and the script reconstructs and verifies one explicit eight-word
prefix code.

## 5. Prime-patching consequence

Symmetry reduction no longer ends with an abstract optimum.  It returns an
actual bank-by-bank marker schedule, and the optimizer count quantifies how much
combinatorial freedom remains for later geometric constraints.
