# Cyclic marker automata and resolvent certificates

`docs/447` treats shared marker states when the state graph is acyclic. A local repair mechanism can also revisit a marked state, for example after a harmless normalization step. This chapter gives the exact replacement for the finite DAG path sum.

Let `Q` be a finite nonnegative transition-load matrix written in row orientation. Thus `Q_(uv)` is the load factor for a transition from state `u` to state `v`. Let `b` be the row vector of injected root loads.

## 1. Exact cyclic path sum

### Theorem PP3cct -- PROVED / MARKER-AUTOMATON RESOLVENT

If `rho(Q)<1`, the total state-load vector over all finite marker walks is

```text
B=b(I-Q)^(-1)=sum_(n>=0) bQ^n.
```

It is the unique nonnegative solution of

```text
B=b+BQ.
```

#### Proof

For a finite nonnegative matrix with spectral radius below one, the Neumann series converges entrywise and equals `(I-Q)^(-1)`. The term `bQ^n` is exactly the load of marker walks using `n` transitions. Summing and shifting the series gives `B=b+BQ`. Uniqueness follows because `I-Q` is invertible. ∎

A recoverable terminal label may be applied after this computation. Terminal classes with disjoint labels combine by a maximum, exactly as in the acyclic case.

## 2. Rational potential and truncation

### Theorem PP3ccu -- PROVED / WEIGHTED GEOMETRIC TAIL

Suppose `w>0` and `0<=q<1` satisfy

```text
Qw<=qw.
```

Then for every `n>=0`,

```text
bQ^n w<=q^n bw.
```

After retaining marker walks of length at most `m`, the omitted weighted load is at most

```text
bQ^(m+1)(I-Q)^(-1)w
 <=q^(m+1) bw/(1-q).
```

#### Proof

The first inequality follows by induction from positivity. Summing it for `n>=m+1` gives the tail estimate. ∎

This is an exact finite certificate whenever `Q`, `b`, `w`, and `q` are rational. It permits a cyclic marker search to be truncated without silently discarding repeated clean normalizations.

## 3. Recurrent obstruction

### Theorem PP3ccv -- PROVED / DUAL RECURRENCE WITNESS

Suppose there is a nonzero row vector `z>=0` with

```text
zQ>=z.
```

If for some `k` and `epsilon>0`,

```text
bQ^k>=epsilon z,
```

then the marker-walk path sum diverges entrywise in total mass on the support of `z`. In particular, no finite reverse-load certificate exists for that cyclic component.

#### Proof

By induction, `zQ^n>=z`. Hence

```text
bQ^(k+n)>=epsilon zQ^n>=epsilon z
```

for every `n`. Summing over `n` diverges on every positive coordinate of `z`. ∎

For an irreducible recurrent component with spectral radius at least one, Perron--Frobenius supplies such a witness. Thus cyclic marker failure localizes to a reachable recurrent state component rather than to an unstructured global loss.

## 4. Exact audit

Run

```bash
python scripts/check_cyclic_marker_automata.py
```

The stored rational automaton has potential rate `9/20`, exact resolvent load

```text
(8801/17850, 4447/10710, 2603/7140),
```

and a separate two-state dual recurrence witness whose depth-five mass is `7776/3125`.
