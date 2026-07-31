# Automaton support-leaf risk decoder

`docs/570` reconciles the original leaf grading with the size-preserving
unary-binary encoding.  This chapter decodes the encoded constructors back into
the terminal states of the original three-state automaton and gives the
previous unary-run statistic a source-level meaning.

## 1. Constructor-to-terminal decoder

The eliminated equations are

```text
T_2=z,
T_1=z+zT_0,
T_0=z+zT_0+zT_0^2.
```

Interpret the three encoded constructors as follows:

```text
L: one state-0 terminal,
U(T): one auxiliary state-1 terminal plus T,
B(T_1,T_2): one auxiliary state-2 terminal plus T_1,T_2.
```

### Theorem PP3cqy -- PROVED / SIZE-PRESERVING SUPPORT INVENTORY

For encoded size `n`, binary count `j`, and unary count `a=n-1-2j`, the decoded
original tree has

```text
j+1 state-0 terminals,
a   state-1 terminals,
j   state-2 terminals.
```

Their sum is `n`, the original leaf count.

#### Proof

The constructor rules contribute the displayed terminal type once per encoded
node of the corresponding kind.  The unary-binary degree identities give
`j+1+a+j=n`. ∎

## 2. Support-nesting risk

### Theorem PP3cqz -- PROVED / AUTOMATON-DECODED RISK

An encoded edge from a unary parent to a unary child is exactly a pair of
consecutively nested state-1 auxiliary terminals along the continuation spine.
Thus the unary-to-unary risk of `docs/564` is an exact incidence statistic of
the original automaton decomposition, not merely an arbitrary Motzkin-tree
mark.

#### Proof

Every unary constructor introduces one state-1 terminal and continues through
its unique encoded child.  A unary child immediately repeats the same
construction before any binary split or state-0 terminal intervenes. ∎

## 3. Exact profile census

### Theorem PP3cra -- PROVED / SUPPORT-NESTING MOMENT

At original leaf count and encoded size thirty with nine encoded binary nodes,
the decoded terminal inventory is

```text
state 0: 10,
state 1: 11,
state 2:  9.
```

The exact support-nesting risk distribution remains the eleven-entry
distribution of `docs/564`; its aggregate is `638045608200` and mean `110/29`.

#### Proof

Apply `PP3cqy` and the exact risk dynamic program.  `PP3cqz` identifies every
marked edge with the decoded support-terminal incidence. ∎

## 4. Exact diagnostic

Run

```bash
python scripts/check_prefix_support_leaf_risk_decoder.py
```

## 5. Prime-patching consequence

One prefix risk now has a machine-checkable path back to the original automaton.
It is still not a coordinate-level support-chord collision count.  The remaining
decoder must identify these automaton terminals with actual support cells and
then determine which nesting incidences are geometrically dangerous.
