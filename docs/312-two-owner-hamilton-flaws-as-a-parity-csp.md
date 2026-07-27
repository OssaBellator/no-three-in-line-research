# Two-owner Hamilton flaws as a signed-graph parity CSP

The complete flaw kernel in `docs/307` repairs a two-owner bad triple by flipping
one orientation bit. This chapter identifies the entire fixed-cycle two-owner
subsystem exactly. It is not a generic 2-SAT instance: a board reflection shows
that every owner-pair predicate depends only on the XOR of its two orientation
bits.

Consequently all two-owner defects for a fixed Hamilton cycle form a signed
graph parity CSP. It can be solved, counted, or certified inconsistent by one
linear-time parity propagation before any three-edge successor rotations are
used.

## 1. Simultaneous sign complementation is a reflection

Write `J(x)=n-1-x`, and let `O_e(i,j)` be the four-cell orbit block selected by
pair edge `i->j` with orientation `e`.

### Proposition PP3bkv -- PROVED

Let

```text
H(x,y)=(x,J(y))
```

be horizontal board reflection. For every nonloop pair edge,

```text
H(O_e(i,j)) = O_(e xor 1)(i,j).
```

Hence for any two pair edges `i->j` and `k->l`, the existence and multiplicity
of collinear triples in

```text
O_e(i,j) union O_f(k,l)
```

is unchanged when `(e,f)` is replaced by `(e xor 1,f xor 1)`.

#### Proof

The two signed orbit blocks are

```text
O_0(i,j) = {(i,j),(Ji,Jj),(Jj,i),(j,Ji)},
O_1(i,j) = {(i,Jj),(Ji,j),(j,i),(Jj,Ji)}.
```

Applying `H` to the first set gives the second set, and applying `H` again
returns the first. Euclidean reflection preserves collinearity and maps the
union of two blocks bijectively to the simultaneously complemented union. ∎

## 2. Exact parity constraints

Fix a Hamilton pair cycle `rho` on vertices `{0,...,m-1}`. For an owner pair
`{i,k}`, define `F_(i,k)` to be the set of parity values `r in {0,1}` for which
some selected collinear triple occurs in

```text
O_(e_i)(i,rho(i)) union O_(e_k)(k,rho(k))
```

when `e_i xor e_k=r`.

### Theorem PP3bkw -- PROVED / EXACT REDUCTION

An orientation vector `e` has no two-owner bad triple if and only if

```text
e_i xor e_k notin F_(i,k)
```

for every owner pair `{i,k}`.

Each pair therefore has exactly one of four forms:

1. `F_(i,k)=emptyset`: no constraint;
2. `F_(i,k)={0}`: require `e_i xor e_k=1`;
3. `F_(i,k)={1}`: require `e_i xor e_k=0`;
4. `F_(i,k)={0,1}`: the fixed Hamilton cycle admits no two-owner-clean
   orientation vector.

#### Proof

A two-owner triple uses cells from exactly two orbit blocks. For fixed owner
edges, whether such a triple exists is a predicate of the two orientation bits.
PP3bkv makes that predicate invariant under simultaneous complementation, so it
depends only on their XOR. Excluding every forbidden XOR value is therefore
necessary and sufficient. ∎

Thus the two-owner subsystem is a binary parity CSP, not an arbitrary collection
of four possible clauses on each variable pair.

## 3. Signed-graph solution and exact count

When no owner pair forbids both parity values, place an edge labelled `r` between
`i` and `k` whenever the system requires

```text
e_i xor e_k=r.
```

### Proposition PP3bkx -- PROVED

The two-owner parity system is satisfiable if and only if the XOR of edge labels
around every cycle of the signed constraint graph is zero. If it is satisfiable
and the graph has `c` connected components, then it has exactly

```text
2^c
```

orientation solutions.

The system, a satisfying orientation, and its exact solution count can all be
computed in linear time in the signed graph size.

#### Proof

Choose one root value in each connected component and propagate values along
labelled edges. A contradiction occurs exactly when two paths to one vertex
prescribe different values, equivalently when some graph cycle has nonzero
label XOR. If propagation is consistent, each component root is free and all
other values in that component are forced, giving two choices per component. ∎

Every satisfying vector removes all support-one flaws simultaneously. Any
remaining collinear triple then has three owners and is targetable by a
successor rotation.

## 4. Exhaustive finite parity census

### Proposition PP3bky -- VERIFIED FINITELY

For every Hamilton cycle with `4<=m<=7`, exact orbit geometry was tested under
all four sign assignments on every owner pair. The results are:

| `m` | Hamilton cycles | parity edges | satisfiable cycles | inconsistent cycles | clean sign vectors |
|---:|---:|---:|---:|---:|---:|
| 4 | 6 | 2 | 6 | 0 | 80 |
| 5 | 24 | 32 | 22 | 2 | 376 |
| 6 | 120 | 180 | 112 | 8 | 3,576 |
| 7 | 720 | 1,296 | 664 | 56 | 36,736 |

No owner pair forbids both XOR values in this range. The parity-edge labels
split as follows:

| `m` | require XOR 0 | require XOR 1 |
|---:|---:|---:|
| 4 | 0 | 2 |
| 5 | 12 | 20 |
| 6 | 84 | 96 |
| 7 | 624 | 672 |

For each satisfiable cycle, the observed number of clean sign vectors is the
power of two predicted by PP3bkx.

#### Verification

Run

```bash
python scripts/check_hamilton_two_owner_parity_csp.py \
  experiments/hamilton-two-owner-parity-csp-audit.json
```

The checker constructs the two four-cell orbit blocks directly, tests every
cell triple with exact integer determinants, verifies simultaneous-complement
invariance, builds the signed parity graph, and compares parity propagation
with the stored exact ledger. ∎

## 5. Revised orientation frontier

### Corollary PP3bkz -- PROVED / FRONTIER REFINED

For a fixed Hamilton cycle, orientation selection can be separated into two
stages:

1. solve the signed parity CSP and eliminate every two-owner flaw;
2. control the remaining three-owner flaws, either by choosing among the parity
   solutions or by applying successor rotations that change the Hamilton cycle.

The first stage is exact and polynomial. The remaining asymptotic questions are
whether one can choose Hamilton cycles whose parity systems are consistently
sparse and satisfiable, and whether the residual three-owner event family has a
smaller causal or dependency structure after this preprocessing.

The finite census does not prove that all large `m` admit a satisfiable parity
system, nor does it establish the asymptotic seed theorem.
