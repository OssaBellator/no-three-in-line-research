# Coded schedules for corridor repair banks

`docs/420` shows that a recoverable bank marker removes the analytic cost of
combining vertex-disjoint corridor banks.  This chapter quantifies how much
marker information is needed.  A short fixed-length code can distinguish all
bank colours, while a shorter code gives a controlled ambiguity factor.

The statements are general.  They do not construct geometric marker bits for
prime-patching repair words.

## 1. Labelled bank kernels

Partition the sources into repair banks

```text
X=X_1 disjoint_union ... disjoint_union X_K.
```

For bank `i`, let `P_i:X_i->Y` be row-stochastic with

```text
lambda(P_i)<=rho.
```

Assign a code label `c(i)` to each bank and augment the final target to

```text
(c(i),y).
```

Let

```text
a=max_z #{i:c(i)=z}
```

be the maximum code ambiguity.

### Theorem PP3bzq -- PROVED / CODE-LABELLED BANK LOAD

The combined augmented kernel has reverse load at most

```text
a rho.
```

In particular, injective bank codes give load at most `rho`, independent of
the number of banks.

#### Proof

A fixed augmented target `(z,y)` receives contributions only from banks with
code `z`.  At most `a` such banks occur, and each contributes column load at
most `rho`. ∎

For corridor word banks with `q` words per source and predecessor multiplicity
at most `h`, this becomes

```text
lambda<=a h/q.
```

## 2. Fixed-length code compression

Let the code alphabet have size `b>=2` and use words of length `ell`.

### Theorem PP3bzr -- PROVED / OPTIMAL BALANCED BANK CODING

There is an assignment of `K` banks to `b^ell` codewords with ambiguity

```text
a=ceil(K/b^ell).
```

No assignment can have smaller maximum ambiguity.  Therefore corridor banks
admit the bound

```text
lambda
 <=ceil(K/b^ell) h/q.
```

An injective marker schedule requires only

```text
ell=ceil(log_b K)
```

symbols.

#### Proof

Distribute the `K` banks as evenly as possible among the `b^ell` codewords.
Pigeonholing gives the matching lower bound on the largest code class. ∎

Thus the marker overhead is logarithmic in the number of corridor colours and
dyadic types, not linear.

## 3. Safety-conditioned coded schedules

Suppose bank `i` is first restricted to safe words retaining row mass at least
`p_i>0`, and let `rho_i` be its unconditioned load.

### Theorem PP3bzs -- PROVED / CONDITIONED CODE-SCHEDULE ENVELOPE

For every codeword `z`, the augmented target columns have load at most

```text
sum_(i:c(i)=z) rho_i/p_i.
```

Consequently

```text
lambda
 <=max_z sum_(i:c(i)=z) rho_i/p_i.
```

Under common bounds `rho_i<=h/q` and `p_i>=p`, this reduces to

```text
lambda<=a h/(pq).
```

#### Proof

Conditioning amplifies bank `i` by at most `1/p_i` by `PP3bxa`.
Sum only over banks sharing the visible code label. ∎

A short schedule code can therefore absorb corridor colouring, dyadic type,
and safety conditioning in one explicit load ledger.

## 4. Revised support-chord frontier

The remaining geometric task is now information-theoretic and local:

1. construct `q` valid words inside each vertex-disjoint corridor bank;
2. encode the bank and type using `O(log K)` recoverable marker symbols;
3. ensure the safety density is large enough that `a h<pq`.

No global union bound over all word types is required.

## 5. Exact diagnostic

Run

```bash
python scripts/check_coded_corridor_bank_schedules.py
```

The checker constructs seven sharp banks, verifies balanced binary codes at
lengths two and three, and checks the exact conditioned column-load ledger.

The next theorem identifier after this chapter is `PP3bzt`.
