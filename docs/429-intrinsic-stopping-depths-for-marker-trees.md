# Intrinsic stopping depths for sequential marker trees

`docs/423` gives a sequential marker-prefix tree and localizes failure to one
low-branching prefix.  A repair procedure need not force every source through
the same depth.  This chapter allows different sources to stop at different
marker depths, provided the final target intrinsically records the stopping
level.

The statements are general interfaces.  They do not construct the required
prime-patching marker words.

## 1. Level kernels

Let `X` be a finite source set.  For levels `i=1,...,k`, let

```text
P_i:X_i -> Y_i
```

be row-stochastic kernels on pairwise disjoint source classes

```text
X=X_1 disjoint_union ... disjoint_union X_k.
```

The class `X_i` consists of the sources whose sequential repair stops after
level `i`.  Assume that the target itself determines `i`, so the supports
`Y_i` are pairwise disjoint.

### Theorem PP3bzz -- PROVED / INTRINSIC STOPPING-DEPTH COMBINATION

Let `P` be the kernel obtained by using `P_i` on `X_i`.  Then

```text
lambda(P)=max_i lambda(P_i).
```

#### Proof

For `y in Y_i`, only sources in `X_i` can reach `y`.  Its column load under
`P` is therefore exactly its column load under `P_i`.  Maximizing over the
disjoint target supports gives the identity. ∎

Thus adaptive stopping does not pay for the number of allowed depths.

## 2. Prefix reservoirs and conditioning

Suppose level `i` offers at least

```text
Q_i=product_(j=1)^i q_j
```

prefix targets per source, and every level-`i` target has at most `h_i`
predecessors within `X_i`.  Uniform choice gives

```text
lambda(P_i)<=h_i/Q_i.
```

More generally, suppose a safety condition retains row mass at least `p_i>0`
before renormalization.

### Corollary PP3caa -- PROVED / CONDITIONED ADAPTIVE PREFIX LOAD

The adaptive stopping kernel satisfies

```text
lambda(P)
 <= max_i h_i/(p_i Q_i).
```

In particular, every source may stop immediately before its first poorly
branching continuation, and the global load is controlled by the worst level
actually used rather than by the deepest attempted word.

#### Proof

Before conditioning, uniform choice has load at most `h_i/Q_i`.  Conditioning
amplifies it by at most `1/p_i`, by `PP3bxa`.  Apply `PP3bzz`. ∎

## 3. Failure localization

### Proposition PP3cab -- PROVED / BAD STOPPING-LEVEL TARGET

Fix proposed level budgets `rho_i`.  If the combined adaptive kernel violates

```text
lambda(P)<=max_i rho_i,
```

then some used level `i` has a target `y in Y_i` with column load exceeding
`rho_i`.

For a uniform unconditioned level with exactly `Q_i` choices per source, this
implies that more than

```text
rho_i Q_i
```

sources in `X_i` reach the same level-`i` target.

#### Proof

The first statement is the exact identity `PP3bzz`.  In the uniform case each
predecessor contributes `1/Q_i`, so a column load larger than `rho_i` requires
more than `rho_i Q_i` predecessors. ∎

The remaining geometric audit may therefore choose a source-dependent stopping
depth.  Failure returns one concrete depth and one overmerged prefix target.

## 4. Finite diagnostic

The script

```bash
python scripts/check_intrinsic_marker_stopping.py
```

checks exact level separation, conditioned bounds, and failure localization on
a rational three-depth marker system.

The next theorem identifier after this chapter is `PP3cac`.
