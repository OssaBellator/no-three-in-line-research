# Exact side-four residual host kernel

**Branch:** `research/exact-recurrent-lyapunov-audit`

**Status:** finite local theorem proved by exhaustive exact enumeration.

This chapter is the first physically grounded block in the exact recurrent
Lyapunov programme. It classifies the complete `4 x 4` response-host problem
obtained by forbidding the diagonal cells and the target cell `01`, then deleting
an arbitrary partial matching of the remaining cells.

It does **not** attach global owner, fate, collision, line, interface, CRT or
background provenance. A local reopening listed below is therefore a
combinatorial certificate, not yet a legal global repair.

## 1. Response spectrum

The six base response permutations are

```text
2031  2301  2310  3012  3201  3210.
```

Their exact intrinsic Euclidean collinear-triple counts are

```text
2031:0  2301:0  2310:0  3012:1  3201:0  3210:4.
```

Thus four responses are intrinsically triple-free and two are bad.

## 2. Complete host census

A deletion set is required to be a partial matching. A host is feasible when at
least one of the six response permutations remains.

Exact enumeration gives

```text
feasible hosts                 86
response incidences           206
good response incidences      137
bad response incidences        69
hosts with a good response     75
residual hosts                 11
```

The counts agree with the independently generated side-four raw-fibre lineage
census on the composite-modulus branch, but the checker in this branch rebuilds
them from first principles.

## 3. Minimal blocker basis

### Theorem ERL-S4.1 — PROVED

Among partial matchings, the inclusion-minimal deletion sets meeting all four
good response permutations are exactly

```text
B1 = {02,20}
B2 = {02,31}
B3 = {13,31}.
```

Consequently, a feasible side-four host is residual if and only if its deletion
set contains at least one of `B1`, `B2`, or `B3`.

### Proof

The checker enumerates every partial matching of the eleven base-allowed cells.
For each candidate it tests intersection with the cell set of all four good
responses and discards every nonminimal candidate. Exactly the three displayed
pairs remain. It then independently enumerates every feasible host and verifies
that the residual predicate is equivalent to containment of one of these three
pairs. All calculations use integer coordinates and ordinary Euclidean
collinearity. ∎

## 4. Exact residual worklist

The eleven residual deletion hosts are

```text
02,20
02,31
13,31
02,10,31
02,13,20
02,13,31
02,20,31
02,23,31
13,20,31
02,10,23,31
02,13,20,31
```

Every surviving response is `3012`, `3210`, or both.

### Theorem ERL-S4.2 — PROVED

Ten residual hosts need one deleted cell reopened before a good response becomes
available. The unique host with minimum reopening number two is

```text
{02,13,20,31}.
```

Its active blocker set is all of `{B1,B2,B3}`. Its exact minimum reopening
choices are

```text
restore {02,13} -> response 2310
restore {02,31} -> response 2031
restore {20,31} -> response 3201.
```

### Proof

For each residual host, enumerate deletion subsets in increasing cardinality,
restore that subset, and recompute the available good responses. The checker
records every first-cardinality success and verifies the depth distribution

```text
reopening depth 1: 10 hosts
reopening depth 2:  1 host.
```

∎

## 5. Interpretation

This result replaces an anonymous side-four geometric residual by an exact finite
kernel. The only genuinely overlapping local obstruction is the four-deletion
state `{02,13,20,31}`.

It does not yet prove descent in the full construction. A forbidden cell can be
reopened globally only after its physical reason, owner, reserve, protected-line
and ancestry contracts are discharged. Reclosing a blocker in a later host epoch
can also recreate the same local state.

The next compiler must therefore attach complete provenance to the eleven states,
enumerate only installed legal operations, and construct exact offspring rows.
The required outcome is either a positive rational strict Lyapunov certificate or
a realizable non-strict recurrent SCC demonstrating that the current repair
architecture is insufficient.

## 6. Executable audit

Run

```bash
python scripts/check_exact_recurrent_side_four_kernel.py \
  --check data/exact_recurrent_side_four_kernel.json
```

The checker regenerates the entire manifest, compares it byte-for-structure with
the committed worklist, and rejects mutation corruptions. Its global proof flags
remain zero.
