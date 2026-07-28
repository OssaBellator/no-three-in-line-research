# `m=10` sparse-core support-chord signature

`docs/354` classifies the sixteen-state distance-five minimum core into four
owner-cover Pareto types and supplies canonical five-step words for every
nondominated profile. This chapter identifies a simple Hamilton-cycle
coordinate that predicts those four finite types exactly.

No general bounded-collateral word theorem is claimed.

## 1. The support-chord signature

Each minimum-core state has two flaw supports

```text
A={c,a_1,a_2},
B={c,b_1,b_2}
```

with one common owner `c`. Place the five owners on the Hamilton cycle of
`rho`. For the two noncentral owners in one support, let

```text
delta_A = min cyclic distance between a_1 and a_2,
delta_B = min cyclic distance between b_1 and b_2.
```

Let `chi` be `alternating` when the four leaves occur in alternating
`A,B,A,B` order around the cycle, and `nested` otherwise. Define

```text
sigma(rho;A,B)
 = (chi, sorted{delta_A,delta_B}).
```

### Proposition PP3brq -- PROVED / SIGNATURE INVARIANCE

The support-chord signature is unchanged by:

1. changing the starting owner used to write the Hamilton cycle;
2. reversing the cyclic order;
3. swapping the two flaw supports;
4. global sign complementation of the signed state.

#### Proof

Cyclic distance and endpoint alternation are invariant under rotation and
reflection of the cycle. Swapping `A` and `B` preserves the unordered distance
pair and merely exchanges the two endpoint colours. Global sign
complementation changes no owner support and no Hamilton-cycle edge. ∎

Thus `sigma` is a genuine cycle/support coordinate on every complement pair.

## 2. Exact prediction of the four Pareto types

### Theorem PP3brr -- VERIFIED FINITELY / COMPLETE SIGNATURE CLASSIFICATION

The eight canonical complement-pair representatives from `docs/348` and
`docs/354` have exactly four support-chord signatures:

| support-chord signature | representatives | shortest-path Pareto profile |
|---|---|---|
| alternating, `{4,4}` | orientations `209`, `402` | `{(2,8,2)}` |
| alternating, `{2,2}` | orientations `382`, `25` | `{(3,12,1)}` |
| alternating, `{3,5}` | orientations `293`, `311` | `{(3,12,2),(4,16,1)}` |
| nested, `{2,3}` | orientations `478`, `42` | `{(3,12,2)}` |

Each row contains two global-sign-complement pairs, hence four signed states.
No two rows share a signature and no row splits into different Pareto types.

#### Verification

The checker hard-codes the exact Hamilton successor arrays and support masks
from the complete terminal-layer ledger. It reconstructs cyclic positions,
computes the two leaf distances and alternation flag, and compares the resulting
signature with the independently verified Pareto profile from `docs/354`. ∎

## 3. Structural consequences for the word bank

The signature separates all observed behaviours:

1. **Wide alternating chords `{4,4}`.** The initial `(2,8)` collateral can be
   preserved, but every shortest path reaches owner-cover two.
2. **Tight alternating chords `{2,2}`.** A star-local shortest path exists with
   the sharp excursion `(3,12)`.
3. **Asymmetric alternating chords `{3,5}`.** The shortest-path frontier has a
   genuine tradeoff: `(3,12,2)` or the star-local `(4,16,1)`.
4. **Nested chords `{2,3}`.** The sharp `(3,12)` excursion still requires
   owner-cover two.

This replaces an unstructured eight-representative list by a four-value
cycle/support invariant. The next task is to prove that the same signature, or
a local refinement of it, selects a bounded-collateral repair template beyond
the finite minimum core and to bound collisions between the resulting words.

Compile and run the exact classifier with

```bash
g++ -O3 -std=c++17 -Wall -Wextra -pedantic \
  scripts/check_m10_sparse_core_support_chord_signature.cpp \
  -o /tmp/check_m10_sparse_core_support_chord_signature

/tmp/check_m10_sparse_core_support_chord_signature
```

The next theorem identifier after this chapter is `PP3brs`.
