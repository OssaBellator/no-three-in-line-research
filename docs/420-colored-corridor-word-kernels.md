# Colored corridor word kernels

`docs/414` decomposes every dyadic support-chord type into vertex-disjoint
corridor banks. This chapter records the exact analytic target for local repair
words on those banks. Bank coloring itself need not cost the number of colors:
only actual overlap between the final target reservoirs matters.

The statements are general. They do not construct the required corridor-local
prime-patching words.

## 1. Word kernels inside one bank

Let the source family be partitioned into corridor banks

```text
S=S_1 disjoint_union ... disjoint_union S_K.
```

For each source `x in S_i`, let `W_i(x)` be its valid local repair words, and let
`t(w)` be the final clean target of word `w`.

Assume

```text
|W_i(x)|>=q
```

and that, inside each fixed bank, every target is produced by words from at most
`h` sources.

### Theorem PP3byy -- PROVED / WITHIN-BANK WORD LOAD

Choosing uniformly among valid words gives every bank kernel reverse load at
most

```text
h/q.
```

#### Proof

Each word has probability at most `1/q`. At most `h` source rows in the bank
can contribute to one target column. ∎

Vertex-disjoint corridors are intended to make both `q` large and `h` small,
because local words can be supported independently.

## 2. Combining all colored banks

Let `Y_i` be the target support of bank `i`, and assume every target belongs to
at most `g` of the supports `Y_i`.

### Theorem PP3byz -- PROVED / COLOR-OVERLAP WORD KERNEL

The combined kernel on all corridor states has reverse load at most

```text
gh/q.
```

In particular, the complete colored family contracts whenever

```text
q>gh.
```

If the final target intrinsically determines the bank color, then `g=1`, so the
number `K` of corridor colors causes no load loss.

#### Proof

Each bank contributes column load at most `h/q` by `PP3byy`. A fixed target
receives contributions from at most `g` bank supports. Sum those contributions,
which is the type-overlap bound `PP3bxb` specialized to word kernels. ∎

## 3. Pair-safety conditioning

Suppose only a fraction of the candidate words survive a safety condition, but
every source retains at least

```text
alpha q
```

valid words.

### Theorem PP3bza -- PROVED / CONDITIONED CORRIDOR-WORD CRITERION

If the within-bank source multiplicity remains at most `h` and bank-support
overlap remains at most `g`, then the conditioned combined kernel has load at
most

```text
gh/(alpha q).
```

Strict contraction follows from

```text
alpha q>gh.
```

Failure of this finite audit exposes one of three concrete obstructions:

1. low safe-word count in one corridor;
2. high predecessor collision inside one bank;
3. high target-support overlap across bank colors.

#### Proof

Apply the uniform retained-word bound inside each bank and then the bank-support
overlap bound. ∎

## 4. Revised support-chord frontier

The geometric and analytic tasks are now cleanly separated. The corridor
coloring supplies vertex-disjoint source banks. For each bank one must build
several safe local words and bound predecessor collisions. Across banks one
must show that the final target recovers the bank color, or at least that only a
bounded number of colors can reach one target.

No union bound over the number of dyadic types or corridor colors is necessary.

## 5. Exact diagnostic

Run

```bash
python scripts/check_colored_corridor_word_kernels.py
```

The checker constructs rational bank kernels, verifies within-bank loads,
combines overlapping target supports, and checks a conditioned subfamily.

The next theorem identifier after this chapter is `PP3bzb`.
