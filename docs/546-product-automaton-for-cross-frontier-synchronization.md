# Product automaton for cross-frontier synchronization

Hall switching, threshold phase, and shell phase are each finite-state
constraints.  Treating them separately can select incompatible words.  This
chapter forms their synchronous product and extracts repeatable return cycles.

The stored Hall state records whether the previous letter was `B`, so `BB` is
forbidden.  The threshold phase lies in `Z/4Z`, and the shell phase lies in
`Z/3Z`.  Letter `A` adds `(1,1)` to the two phases; letter `B` adds `(2,0)`.

## 1. Product-cycle certificate

### Theorem PP3cnm -- PROVED / SYNCHRONOUS PRODUCT REDUCTION

For finitely many deterministic interface automata driven by a common alphabet,
a word satisfies all interface constraints and returns every phase to its start
if and only if it labels a directed return cycle in the synchronous product
automaton.

#### Proof

A product transition exists exactly when every component transition exists, and
its endpoint is the tuple of component endpoints.  Therefore a product path is
precisely a simultaneously legal word, and equality of its initial and final
product states is simultaneous phase return. ∎

## 2. Repeatability and multiplicative Hall decay

### Theorem PP3cnn -- PROVED / RETURN-CYCLE REPETITION

A return word may be concatenated arbitrarily many times without accumulating
threshold or shell phase drift.  If its Hall contraction certificate is `rho`,
then `q` repetitions have contraction at most `rho^q`.

#### Proof

Each copy begins in the same product state in which the preceding copy ended.
Thus all finite-state constraints remain legal and all phase coordinates reset.
The Hall contraction factors multiply under composition. ∎

## 3. Stored 24-state fixture

### Theorem PP3cno -- PROVED / SHORTEST MIXED SYNCHRONIZER

The product has `2*4*3=24` states and is strongly connected.  From the neutral
state `(0,0,0)`, the shortest return word containing both letters has length
seven.  There are exactly six such words:

```text
AAAAABA, AAAABAA, AAABAAA,
AABAAAA, ABAAAAA, BAAAAAA.
```

Each contains six `A` letters and one `B`, so with contractions

```text
A:1/2,
B:3/4,
```

one cycle contracts by `3/256`.  Two cycles contract by

```text
9/65536<1/100.
```

#### Proof

The phase equations for a mixed return require

```text
#A+2#B congruent 0 (mod 4),
#A congruent 0 (mod 3).
```

The smallest positive mixed solution compatible with a neutral final Hall state
is `#A=6,#B=1`, of length seven.  Placing the isolated `B` anywhere except the
last position gives the six listed words; direct transitions show all are legal.
Strong connectivity follows by the explicit finite reachability certificate in
the audit. ∎

## 4. Stored exact audit

The audit `scripts/check_product_synchronizer_automaton.py` builds all 24 states,
checks mutual reachability, exhausts all binary words until the first mixed
return length, and evaluates both contraction products using exact fractions.

## 5. Prime-patching consequence

Hall mixing can now be scheduled together with threshold and shell phases rather
than patched after the fact.  The product-cycle interface is finite and exact.
The remaining geometric task is to prove that the actual gadget alphabet induces
the certified component transitions.
