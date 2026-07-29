# Corridor hubs and disjoint banks for dyadic support-chord types

`docs/402` localizes hard two-support states to one alternation pattern and two
dyadic chord scales.  This chapter associates a short cycle corridor with each
state of that type and applies a weighted hub-or-disjoint argument.  The result
is a cycle-vertex hub or a bank whose chord corridors are vertex-disjoint.

The statements do not construct the repair word inside a corridor.

## 1. Canonical short-arc corridors

Fix a Hamilton cycle and, for every unordered pair of cycle vertices, choose
one shortest connecting arc.  When the two shortest arcs tie, use any fixed
deterministic tie-break.

For a support pair

```text
A={c,a_1,a_2},
B={c,b_1,b_2},
```

let `I_A` and `I_B` be the chosen short arcs between the two leaves of each
support, and define the corridor

```text
C(A,B)=V(I_A) union V(I_B).
```

### Proposition PP3bxm -- PROVED / DYADIC CORRIDOR SIZE

If the dyadic chord indices are `j_A,j_B`, then

```text
|C(A,B)|
 <=ell(j_A,j_B)
 :=2^(j_A+1)+2^(j_B+1).
```

The corridor contains all four noncentral support vertices.  The estimate is
independent of the alternation bit.

#### Proof

A shortest arc joining a pair at cyclic distance `delta` has `delta+1`
vertices.  In dyadic class `j`,

```text
delta<2^(j+1),
```

so integrality gives `delta+1<=2^(j+1)`.  Add the two arc sizes; overlap can
only reduce their union. ∎

Thus a fixed dyadic type comes with a uniformly bounded local cycle region at
its own two scales.

## 2. Weighted corridor packing

Let `Omega_tau` be a weighted family of states of one fixed dyadic type, with
weights `w(omega)>=0` and total weight `W`.  For a cycle vertex `v`, put

```text
H(v)=sum_(omega:v in C(omega)) w(omega).
```

### Theorem PP3bxn -- PROVED / CORRIDOR HUB-OR-DISJOINT BANK

For every threshold `H_0>0`, one of the following holds:

1. some cycle vertex has corridor load

   ```text
   H(v)>H_0;
   ```

2. there are at least

   ```text
   ceil(W/(ell H_0))
   ```

   states whose corridors are pairwise vertex-disjoint, where
   `ell=ell(j_A,j_B)`.

#### Proof

Assume every vertex load is at most `H_0`.  Greedily select a remaining
positive-weight state and delete every remaining state whose corridor meets
its corridor.  A selected corridor contains at most `ell` vertices, so the
total deleted weight is at most

```text
sum_(v in C(omega))H(v)<=ell H_0.
```

If `s` states are selected, all weight has been deleted and

```text
W<=s ell H_0.
```

The selected corridors are pairwise disjoint by construction. ∎

This is the cycle-geometric analogue of `PP3bwj`.

## 3. Scale-balanced square-root form

### Corollary PP3bxo -- PROVED / DYADIC CORRIDOR SQUARE-ROOT DICHOTOMY

Assume every individual state weight is at most `M>0`.  Put

```text
q=sqrt(W/(M ell))
```

and choose

```text
H_0=M q=sqrt(MW/ell).
```

Then either some cycle vertex has normalized load

```text
H(v)/M>q,
```

or there is a pairwise vertex-disjoint corridor bank of size at least

```text
ceil(q).
```

If the original family has total weight `W_total`, then after the dyadic
localization of `PP3bwu` one type has

```text
W>=W_total/[L(L+1)],
```

and hence

```text
q>=sqrt(
 W_total/
 [M ell L(L+1)]
).
```

#### Proof

Insert the chosen threshold into `PP3bxn`:

```text
W/(ell H_0)
 =W/[ell sqrt(MW/ell)]
 =sqrt(W/(Mell))
 =q.
```

The normalized hub inequality is the same threshold divided by `M`.
The localized-family form follows from `PP3bwu`. ∎

The conclusion is scale-sensitive: wide chord classes pay through their
corridor length, while short chords can produce much larger disjoint banks.

## 4. Revised support-chord frontier

After only the `O(log^2 m)` dyadic type loss, every large hard-state family
has one of two geometric shapes:

1. many weighted states route through one cycle vertex;
2. many states occupy pairwise disjoint two-arc corridors.

A repair-word theorem can now be proved separately for a fixed corridor hub
and for independent local words on disjoint corridors.  The target-reservoir
calculus of `docs/404` can combine the resulting type kernels without paying
the raw number of types.

## 5. Finite diagnostic

The script

```bash
python scripts/check_support_chord_corridor_banks.py
```

enumerates support pairs through cycle length twelve, verifies every corridor
size bound, and checks the weighted greedy bank inequality on stored rational
families.

The next theorem identifier after this chapter is `PP3bxp`.
