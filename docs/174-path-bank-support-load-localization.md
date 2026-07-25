# Path-bank support-load localization

PP3aah--PP3aal extract two kinds of transition path banks through a captive centre:

1. a bank of paths `u_h->p_h->c` whose auxiliary pairs `{u_h,p_h}` are pairwise
   disjoint;
2. a fixed-predecessor star `u->p_h->c` with distinct variable middles `p_h`.

For either bank, any source-invalid or paid pattern has bounded endpoint-index
support. A pattern can therefore meet the variable auxiliary support of only
boundedly many local states. Averaging over the bank removes every diffuse
noncentral contribution.

The remaining concentrated object is exact:

- in the disjoint-auxiliary bank, a pattern supported on the fixed centre `c` and
  residual random indices;
- in the fixed-predecessor star, a pattern supported on the fixed pair `{u,c}` and
  residual random indices.

Thus path-bank failure is not an arbitrary average over `m^(19/40)` states. It is
a one-centre or two-centre support core plus globally averaged bounded-support
mass.

## 1. Abstract bounded-overlap bank

Let `H` be a finite state bank. Each state `h in H` has a fixed core `C` and a
variable auxiliary index set `A_h`, with

```text
A_h cap C = empty.
```

Assume the auxiliary sets are pairwise disjoint. Let `B` be a family of patterns,
each with endpoint-index support `supp(B)` of size at most `r_0`, and nonnegative
weight `w(B)`.

Call an incidence `(h,B)` **variable-touching** when

```text
supp(B) cap A_h != empty.
```

### Proposition PP3aau -- PROVED

One has

```text
sum_{h in H}
sum_{B: supp(B) cap A_h != empty} w(B)
<= r_0 sum_{B in B} w(B).
```

#### Proof

Fix one pattern `B`. Since the sets `A_h` are pairwise disjoint, every state
whose auxiliary support meets `supp(B)` consumes a distinct index of `supp(B)`.
There are at most `r_0` such states. Sum the weight of `B` over states and then sum
over patterns. ∎

This statement applies equally to integer event counts and exact insertion-cost
weights.

## 2. Core-only and variable-touching decomposition

For each state `h`, classify every remaining pattern after its local path is fixed
by:

1. the number `r` of additional random permutation arcs required;
2. whether its fixed support meets `A_h`.

Let:

```text
X_h,r = variable-touching total weight,
Y_h,r = core-only total weight.
```

Core-only means that the fixed part of the pattern is supported inside `C`; its
other support is supplied only by the residual random completion.

### Theorem PP3aav -- PROVED

For every rank `r`,

```text
(1/|H|) sum_h X_h,r
<= r_0 W_r/|H|,
```

where `W_r` is the total global weight of rank-`r` patterns in the relevant
support class.

Consequently the joint local-state and residual-permutation first moment is
bounded by

```text
sum_r K^r [
  (1/|H|) sum_h Y_h,r
  + r_0 W_r/|H|
]/n^r,
```

up to the fixed cylinder constant and the appropriate residual order `n`.

#### Proof

Apply PP3aau separately to each additional-arc rank. The residual cylinder law
then multiplies every rank-`r` pattern by at most `K^r/n^r`. ∎

All bank-size gain is therefore lost only on the core-only terms `Y_h,r`.

## 3. Disjoint-auxiliary transition bank

For the first alternative of PP3aaj, take

```text
C={c},
A_h={u_h,p_h}.
```

The sets `A_h` are pairwise disjoint and every source pattern considered in the
endpoint argument has endpoint support at most six.

### Corollary PP3aaw -- PROVED

For an `H`-state disjoint-auxiliary transition bank, every source or paid pattern
whose fixed support uses `u_h` or `p_h` receives an averaging gain `O(1/H)` after
summing global pattern weight.

Failure of the averaged paid single-cycle criterion PP3aak therefore forces one
of:

1. a core-only source or paid load supported at the captive centre `c`;
2. global bounded-support pattern weight large enough that its total divided by
   `H` reaches the path-credit scale;
3. residual single-cycle host failure.

The individual auxiliary resources cannot support scattered exceptional states.

## 4. Fixed-predecessor path star

For the star alternative of PP3aaj, take

```text
C={u,c},
A_h={p_h}.
```

The middles `p_h` are distinct, so the auxiliary singleton sets are disjoint.

### Corollary PP3aax -- PROVED

For an `H`-state fixed-predecessor star, every source or paid pattern that uses the
variable middle `p_h` receives the same `O(1/H)` averaged support gain.

Failure of PP3aak therefore forces one of:

1. a source or paid core supported on the fixed endpoint-index pair `{u,c}`;
2. global bounded-support weight divided by `H` at the path-credit scale;
3. residual single-cycle host failure.

Thus the fixed-predecessor star does not create `H` unrelated exceptional states.
Its whole obstruction is localized to one ordered pair of fixed endpoint indices.

## 5. Paid endpoint

Let `R_*>0` be the minimum removal credit over the path bank. Let `J_h^core` be the
expected insertion cost of patterns whose fixed support lies inside the relevant
core `C`, and let `W_var` be the global support-ranked weight of all
variable-touching patterns after their cylinder factors are included.

### Corollary PP3aay -- PROVED

A strict source-valid path trade exists whenever

```text
(1/|H|) sum_h J_h^core
+ O(W_var/|H|)
< R_*
```

and the corresponding expected source-invalid count is `o(1)`.

Negating this criterion gives an exact fixed-core alternative:

- one-centre concentration at `c` for a disjoint-auxiliary bank;
- two-centre concentration at `{u,c}` for a fixed-predecessor star;
- or global support-ranked weight of order `H R_*`.

#### Proof

Combine PP3aav with the conditional single-cycle first moment PP3aak and the exact
insertion-cost-minus-removal-credit identity. ∎

## 6. Revised transition path-bank frontier

The transition path banks of size

```text
H=m^(19/40+o(1))
```

now fail only through:

1. a one-centre support/weight core at the captive centre;
2. a two-centre support/weight core at a fixed predecessor/successor and the
   captive centre;
3. global support-ranked weight of order `H` times the removal credit;
4. residual source-host failure.

Diffuse auxiliary-state collateral is closed by bounded-support averaging.
