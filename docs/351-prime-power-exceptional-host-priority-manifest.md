# Exact priority manifest for the 89 critical and excess rank-three hosts

The canonical raw-host catalogue gives every side-four/five host a stable primary
key and exact values

\[
Z,\qquad A_3,\qquad S_3=Z-A_3.
\]

This chapter extracts the exact non-strict worklist and records the minimum integer
rank-three reduction needed to make each raw rank-three row strict.

The manifest is a priority and linkage surface. It does not assert that hosts with
the same response signature have equivalent backgrounds, owners, collision states,
interfaces or CRT semantics.

## 1. Minimum rank-three correction

Let `c` be an integer number of rank-three numerator units removed, cancelled or
routed away from the scalar self-row.

### Theorem CMR1982 -- PROVED

For a critical or excess host, the minimum integer correction making the rank-three
row strict is

\[
\boxed{
c_{\min}=A_3-Z+1=1-S_3.
}
\]

### Proof

Strictness after correction is

\[
A_3-c<Z.
\]

Because all terms are integers, this is equivalent to `c>=A_3-Z+1`. Equality gives
the minimum. Substituting `S_3=Z-A_3` yields `1-S_3`. ∎

Thus a critical host requires one unit, while an excess host requires at least two.

## 2. Exact exceptional extraction

### Theorem CMR1983 -- PROVED

The canonical catalogue contains exactly

\[
\boxed{89}
\]

hosts with `S_3<=0`, split as

\[
\boxed{
44\text{ critical},\qquad
45\text{ excess}.
}
\]

By side, the split is

\[
\boxed{
33\text{ side-four exceptional hosts},\qquad
56\text{ side-five exceptional hosts}.
}
\]

### Proof

Filter the accepted 740-host catalogue by the exact stored slack and count. ∎

Every priority record retains its source host ID and full catalogue-record digest.

## 3. Exact correction distribution

### Theorem CMR1984 -- PROVED

The minimum required rank-three corrections have distribution

| `c_min` | 1 | 2 | 3 | 4 | 5 |
|---:|---:|---:|---:|---:|---:|
| hosts | 44 | 14 | 18 | 12 | 1 |

The total required correction mass, if every exceptional host were treated
independently by scalar rank-three deletion, is

\[
\boxed{179},
\]

and the largest individual requirement is five.

### Proof

Apply CMR1982 hostwise and tabulate the exact slacks. The weighted total is

\[
44+2(14)+3(18)+4(12)+5=179.
\]

∎

The unique five-unit host is
`\texttt{s5-190649dd48641a44}`. It has `Z=10`, `A_3=14`, `S_3=-4`, and response
histogram

\[
\{0^1,1^6,2^2,4^1\}.
\]

In particular, its unfavorable uniform numerator does not prevent a zero-rank-three
individual response.

## 4. Exact response-profile fields

### Theorem CMR1985 -- PROVED

Each exceptional record stores, and the checker independently verifies:

1. the complete response-triple histogram;
2. the minimum and maximum response triple counts;
3. the number of responses with positive rank-three load;
4. `Z`, `A_3`, `S_3`; and
5. `c_min=1-S_3`.

### Proof

All fields are deterministic functions of the linked canonical host response list.
The validator rebuilds them from that list and requires direct equality. ∎

This exposes the difference between a poor uniform average and the existence of a
good deterministic response.

## 5. Exact signature classes

Define the exceptional response signature

\[
\sigma(H)
=
\left(
s,Z,S_3,|D|,
\operatorname{hist}(\psi_3)
\right).
\]

### Theorem CMR1986 -- PROVED

The 89 exceptional hosts occupy exactly

\[
\boxed{49}
\]

distinct signatures `sigma(H)`.

The class ID is a canonical digest of the complete signature, and every class lists
all member host IDs.

### Proof

Compute the displayed tuple for every exceptional canonical record and group by
exact tuple equality. The checker verifies complete member coverage and the fixed
class count. ∎

## 6. Signature classes are not geometric quotients

### Theorem CMR1987 -- PROVED

Equality of `sigma(H)` proves equality only of the five stored response-summary
components. It does not prove Euclidean equivalence of deletion geometry, equality of
future backgrounds, owner/fate equivalence or equality of labelled offspring rows.

### Proof

The signature omits those data. Therefore they cannot be inferred from signature
equality without a separate theorem. ∎

The classes are valid batching and regression keys: a proof template may be tested
once per class and then must still be instantiated and checked on every member.

## 7. Deterministic priority order

### Theorem CMR1988 -- PROVED

The priority manifest orders hosts deterministically by:

1. decreasing `c_min`;
2. increasing side;
3. increasing denominator; and
4. increasing canonical host ID.

This order is a reproducible worklist and does not assert that a larger `c_min` is
always mathematically harder after exact response selection or labelled routing.

### Proof

All ordering fields are exact canonical-record functions, so the sort is
deterministic. The final disclaimer follows because alternative corrections can
depend on omitted state data. ∎

The complete priority-manifest digest is

\[
\boxed{\texttt{730d06e8fab61c302b565ad09fc63bd625c886ec521a7fc71d8b6914fe769444}.}
\]

## 8. Executable endpoint

### Corollary CMR1989 -- PROVED

`scripts/check_prime_power_exceptional_host_priority_manifest.py` implements the
complete exceptional worklist.

It:

1. validates and links the canonical 740-host catalogue;
2. extracts every and only critical/excess host;
3. computes exact correction requirements;
4. records exact response extrema and histograms;
5. constructs all 49 exact signature classes;
6. verifies the fixed priority digest and all census totals;
7. writes and reloads deterministic JSON manifests; and
8. rejects ten independently corrupted manifests.

This closes the raw-host identification and prioritization problem. Actual operation
backgrounds, destroyed triples, owner/fate semantics and labelled correction proofs
remain separate required inputs.
