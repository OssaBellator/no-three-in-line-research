# Associative SCC elimination for type-load matrices

`docs/422` eliminates one contractive transient block by a nonnegative Schur
complement.  Large type systems naturally contain several transient blocks.
This chapter proves that elimination is associative, monotone under entrywise
upper envelopes, and localizable to strongly connected components of the
transient type graph.

The statements are general.  They do not construct the final prime-patching
type matrix.

## 1. Associativity of transient elimination

Let `M` be a nonnegative matrix whose index set is partitioned into

```text
E_1 disjoint_union E_2 disjoint_union C.
```

Assume the full transient principal block on `E_1 union E_2` has spectral
radius below one.  Let `Schur_E(M)` denote the effective matrix on the
complement after eliminating `E`:

```text
D+C(I-A)^(-1)B.
```

### Theorem PP3bzw -- PROVED / ASSOCIATIVE TYPE ELIMINATION

Eliminating `E_1` and then the resulting `E_2` block gives exactly the same
effective core matrix as eliminating `E_1 union E_2` in one step:

```text
Schur_(E_2)(Schur_(E_1)(M))
 =Schur_(E_1 union E_2)(M).
```

The same holds for any finite sequence of transient blocks.

#### Proof

Both sides sum the weights of all walks that start and end in the retained
indices while all internal vertices lie in the eliminated set.  Sequential
elimination first resums excursions through `E_1` and then through `E_2`;
direct elimination resums the same walks at once.  Equivalently, this is the
standard quotient identity for block Gaussian elimination applied to `I-M`.
The transient spectral-radius hypothesis makes every inverse a convergent
nonnegative Neumann series. ∎

Thus a large transient system may be reduced in whichever block order is most
convenient.

## 2. Monotone upper envelopes

Consider two block matrices with the same partition,

```text
M=[A B; C D],
Mhat=[Ahat Bhat; Chat Dhat],
```

such that every block of `M` is entrywise at most the corresponding block of
`Mhat` and `rho(Ahat)<1`.

### Theorem PP3bzx -- PROVED / MONOTONE SCHUR LOAD ENVELOPE

Their effective core matrices satisfy

```text
D+C(I-A)^(-1)B
 <=Dhat+Chat(I-Ahat)^(-1)Bhat
```

entrywise.

#### Proof

The Neumann series is entrywise monotone:

```text
(I-A)^(-1)=sum_(t>=0)A^t
 <=sum_(t>=0)Ahat^t=(I-Ahat)^(-1).
```

Multiply by the ordered nonnegative entrance and exit blocks and add the core
blocks. ∎

Local coarse upper bounds can therefore be substituted before elimination
without invalidating the final contraction certificate.

## 3. Strongly connected transient blocks

Let the directed graph of the transient block `A` be decomposed into strongly
connected components.  Its condensation graph is acyclic.

### Theorem PP3bzy -- PROVED / SCC-LOCAL TRANSIENT ELIMINATION

If every transient strongly connected principal block has spectral radius
below one, then eliminating the components in reverse topological order gives
the exact global effective core matrix.

All infinite resummation occurs inside individual strongly connected
components.  Movement between components is acyclic and is accounted for by a
finite sequence of block multiplications.

#### Proof

Order the strongly connected components topologically, making `A` block
triangular.  Each diagonal block is contractive by hypothesis.  Apply
`PP3bzw` successively in reverse topological order.  Because the condensation
has no directed cycles, no eliminated component can be revisited after moving
downstream; the only geometric series are the local diagonal resolvents. ∎

This converts one large inverse into small recurrent inverses plus finite
acyclic propagation.

## 4. Revised integration frontier

A machine-generated type certificate may now proceed hierarchically.

1. Decompose transient types into strongly connected components.
2. Replace each component by a rigorous local upper envelope.
3. Eliminate components in any convenient order.
4. Test the much smaller effective recurrent core with a rational positive
   potential.

Associativity guarantees that independent audit modules compose exactly.

## 5. Exact diagnostic

Run

```bash
python scripts/check_associative_type_elimination.py
```

The checker performs exact rational direct and sequential eliminations,
verifies monotonicity under an inflated envelope, and reproduces the same core
matrix by reverse-topological SCC elimination.

The next theorem identifier after this chapter is `PP3bzz`.
