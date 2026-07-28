# Exact `m=9` single-support collateral words

`docs/332` isolates eight parity-clean signed states at macro distance four from
validity.  Each has one three-owner flaw support, exactly four atomic triples,
and no one-step decrease of either support count or atomic count.  This chapter
classifies those states and computes the least collateral required along a
shortest clean-macro path.

No uniform-in-`m` collateral word or asymptotic repair theorem is claimed.

## 1. Four complement-paired source types

Write a Hamilton cycle as its successor array

```text
rho=(rho(0),...,rho(8)).
```

Global sign complementation sends orientation mask `e` to `e xor 511` and
preserves all support and atomic counts.

### Theorem PP3bpd -- VERIFIED FINITELY / COMPLETE HARD-STATE CLASSIFICATION

The eight one-support distance-four states lie on exactly four Hamilton cycles
and form exactly four global-sign-complement pairs.  Representatives are:

| source orientation pair | successor array `rho` | unique flaw support |
|---|---|---|
| `(136,375)` | `(3,6,7,4,2,8,5,1,0)` | `(0,1,5)` |
| `(59,452)` | `(4,3,7,6,1,8,5,0,2)` | `(3,4,5)` |
| `(165,346)` | `(7,4,8,1,0,6,3,2,5)` | `(1,6,8)` |
| `(18,493)` | `(8,7,4,0,3,6,1,2,5)` | `(3,6,8)` |

Every state has atomic count four, support count one, and exact clean-macro
distance four.

#### Verification

Compile and run

```bash
g++ -O3 -std=c++17 -Wall -Wextra -pedantic \
  scripts/check_m9_single_support_collateral_words.cpp \
  -o /tmp/check_m9_single_support_collateral_words
/tmp/check_m9_single_support_collateral_words
```

The checker reconstructs all `6,727,728` parity-clean signed states, the exact
reverse macro distances, the eight hard states, and their complement pairing.
It compares the complete witness bank with
`experiments/m9-single-support-collateral-words-audit.json`. ∎

## 2. Sharp shortest-path collateral barrier

For a clean-macro path `x_0,...,x_4` to validity, define

```text
peak_a = max_i atomic_count(x_i),
peak_h = max_i support_count(x_i).
```

### Theorem PP3bpe -- VERIFIED FINITELY / SHARP FOUR-STEP BARRIER

For each of the eight hard states, among all shortest four-step paths to
validity,

```text
minimum peak_a = 8,
minimum peak_h = 2.
```

Both minima are attained simultaneously by an explicit path.

Thus every shortest repair must temporarily leave the one-support/four-atomic
level: at least one intermediate state has two flaw supports and at least eight
atomic triples.  Conversely, no shortest repair needs more than two supports or
eight atomic triples.

#### Verification

Dynamic programming is performed over the exact distance DAG.  For a state at
distance `d`, the minimum attainable peak is the minimum over legal target
cycles at distance `d-1` of the maximum of the source count and the already
computed target peak.  The same recursion is run independently for support and
atomic counts. ∎

## 3. Four canonical bounded-collateral words

A word records the four source triples rotated by successive macro moves.
Because each complement pair may freely choose the same target orientation in
the next clean fibre, one word serves both signs in the pair.

### Theorem PP3bpf -- VERIFIED FINITELY / CANONICAL WORD BANK

The four representative words and their count profiles are:

```text
(136,375):
  word     (0,1,2) (3,5,8) (0,2,6) (1,2,3)
  atomic   4,8,8,8,0
  supports 1,2,2,2,0

(59,452):
  word     (0,2,3) (0,2,5) (1,6,7) (3,4,5)
  atomic   4,8,8,8,0
  supports 1,2,2,2,0

(165,346):
  word     (4,6,7) (4,6,8) (0,3,5) (1,4,7)
  atomic   4,8,8,8,0
  supports 1,2,2,2,0

(18,493):
  word     (0,6,8) (3,5,6) (3,5,7) (3,4,5)
  atomic   4,4,8,8,0
  supports 1,1,2,2,0
```

Each word is a legal clean-macro path, each rotated triple meets a flaw support
present in its source state, and the final state is line-valid.

## 4. Revised sparse-collateral frontier

The eight-state obstruction is now quantitatively bounded.

1. It is not a dense terminal family: it consists of four complement-paired
   Hamilton-cycle types.
2. A monotone support or atomic potential is impossible, but the necessary
   excursion is only

   ```text
   one additional support,
   four additional atomic triples.
   ```

3. The exact four-step words provide a finite model for a compensated potential
   that budgets a bounded collateral excursion before a terminal drop.
4. The asymptotic task is to replace the four explicit words by a structural
   rule for an arbitrary isolated three-owner orbit, with predecessor charge
   controlled inside the owner light cone of `docs/338`.

The next theorem identifier after this chapter is `PP3bpg`.
