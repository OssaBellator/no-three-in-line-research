# Exact single-cut terminal normalizer envelopes through `m=10`

`docs/374` optimizes contiguous coarsenings of the fixed dyadic normalizer bins.
At `m=9`, three such segments are needed for contraction.  This chapter removes
the fixed dyadic boundaries and optimizes one cut over the complete observed
normalizer support.

No asymptotic single-cut theorem is claimed.

## 1. One exact normalizer cut

Fix a target cycle `eta`.  Write its incoming labelled terminal moves as `i`,
with capacity normalizers `Z_i`.  Let

```text
z_1 < z_2 < ... < z_r
```

be the complete normalizer values observed anywhere in the terminal gate, so
`z_1=z_min`.  For `2<=k<=r`, define

```text
L_eta(k) = #{i into eta : Z_i < z_k},
H_eta(k) = #{i into eta : Z_i >= z_k}.
```

### Proposition PP3btn -- PROVED / EXACT SINGLE-CUT ENVELOPE

For every target and every cut index `k`,

```text
kappa_F(eta)
  <= E_k(eta)
   := L_eta(k)/z_1 + H_eta(k)/z_k.
```

Consequently

```text
sup_eta kappa_F(eta)
 <= min_{2<=k<=r} max_eta E_k(eta).
```

#### Proof

Every low-segment label has normalizer at least `z_1`, and every high-segment
label has normalizer at least `z_k`.  Replacing each reciprocal by the
corresponding segment lower edge gives the first inequality.  Taking the target
maximum and then minimizing over the common cut preserves it. ∎

The cut is recorded by the consecutive observed pair `(z_{k-1},z_k)`.  Values
strictly between them do not occur, so the low segment ends at `z_{k-1}` and the
high segment starts at `z_k`.

## 2. Complete exact optimization

### Theorem PP3bto -- VERIFIED FINITELY / BEST OBSERVED SINGLE CUTS

The complete terminal-gate census gives:

| `m` | distinct normalizers | best consecutive cut | low/high labels on a maximizing target | exact worst-target envelope | decimal | components | ties |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 8 | 166 | `3152 | 3168` | `160 / 1536` | `2852/4521` | `0.630833886308...` | 6 | 2 |
| 9 | 704 | `9648 | 9664` | `1024 / 6144` | `13760/14043` | `0.979847610909...` | 8 | 2 |
| 10 | 684 | `39584 | 39824` | `896 / 7168` | `415800/1535713` | `0.270753715050...` | 9 | 2 |

For example, the `m=9` certificate is exactly

```text
1024/2976 + 6144/9664
  = 13760/14043.
```

The clean rational bounds and margins are

```text
m=8:
  2852/4521 < 2/3,
  2/3 - 2852/4521 = 54/1507;

m=9:
  13760/14043 < 49/50,
  49/50 - 13760/14043 = 107/702150;

m=10:
  415800/1535713 < 3/10,
  3/10 - 415800/1535713 = 449139/15357130.
```

#### Verification

The regeneration checker instruments the already committed exact terminal
implementation.  It performs the complete shell and closing-gate census,
records every observed normalizer, and builds the exact target-by-normalizer
population matrix.  It then tests every cut between consecutive observed
normalizers, computes every target envelope by integer arithmetic, and minimizes
the exact worst-target ratio.  Compilation uses
`-Wall -Wextra -pedantic -fopenmp`; all displayed values are hard-coded Python
regressions. ∎

## 3. One adaptive cut resolves the finite `m=9` obstruction

### Corollary PP3btp -- PROVED / VERIFIED FINITELY / AT-MOST-ONE-CUT CONTRACTION

An optimally placed single normalizer cut certifies terminal contraction at all
three audited sizes.

The fixed dyadic coarsening of `docs/374` required three segments at `m=9`, but
one exact cut between `9648` and `9664` gives a two-segment envelope below
`49/50`.  Thus the dyadic three-scale requirement was a boundary-placement
artifact, not an intrinsic need for three scales.

At `m=10`, even the zero-cut one-segment ratio `560/617` already contracts; the
optimized cut merely strengthens it to `415800/1535713`.

The asymptotic target can therefore be stated with one balancing threshold.  It
is enough to find a normalizer level `z_*` such that, uniformly over targets,

```text
C_eta(z_*^-)/z_min
 + (N_eta-C_eta(z_*^-))/z_* < 1,
```

where `N_eta` is the total incoming labelled multiplicity.  This combines the
low-normalizer tail and the high-normalizer reverse multiplicity without
requiring control of every dyadic scale separately.

Reproduce or verify with

```bash
python scripts/check_terminal_normalizer_exact_single_cut.py .

python scripts/check_terminal_normalizer_exact_single_cut.py . \
  --regenerate --threads 8 \
  --output /tmp/terminal-normalizer-exact-single-cut.json
```

The next theorem identifier after this chapter is `PP3btq`.
