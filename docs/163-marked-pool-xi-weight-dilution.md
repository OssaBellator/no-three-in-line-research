# Marked pool dilution for dynamic Xi insertion weight

PP3yf--PP3yi close pool-local source validity for a large credited resource bank,
unless unary support already supplies another star/resource bank. The remaining
pool-compatible term is paid insertion weight for the dynamic excess potential
`Xi`.

A marked filler block gives an exact support-rank normalization for this weight.
Patterns containing the forced credited endpoint lose one thinning factor; all
other patterns retain the ordinary random-subbank factor. Summing the marked load
over every endpoint converts the remaining obstruction into explicit global
support-ranked weights or a set of credited endpoints with concentrated paid
load.

## 1. Support-ranked Xi weights

Let a full controller pool contain `N` tied endpoint indices. Decompose the unary
Xi-insertion weight as

```text
A=A_1+A_2,
```

where `A_h` is the total weight of unary patterns with endpoint-index support size
`h`. Decompose binary Xi-insertion weight as

```text
B=B_2+B_3+B_4.
```

For an endpoint `c`, let `D_A,h(c)` and `D_B,h(c)` be the total corresponding
pattern weight whose support contains `c`.

### Proposition PP3yj -- PROVED

```text
sum_c D_A,h(c)=h A_h,
sum_c D_B,h(c)=h B_h.
```

#### Proof

Double-count weighted pattern-index incidences. ∎

## 2. Marked filler expectation

Fix `c`, choose a uniform `(b-1)`-subset of the other pool endpoints, and assume
the prepared state law has one-edge and two-edge cylinder bounds `K/b` and
`K^2/b^2`.

Define the marked unary load

```text
M_A(c)
=
K [
  D_A,1(c)/b
  + D_A,2(c)/N
],
```

and the marked binary load

```text
M_B(c)
=
K^2 [
  D_B,2(c)/(bN)
  + D_B,3(c)/N^2
  + D_B,4(c)b/N^3
].
```

### Theorem PP3yk -- PROVED

The expected Xi-insertion cost on the marked block is at most a fixed constant
times

```text
M_A(c)+M_B(c)+U_A+U_B,
```

where the unmarked terms are

```text
U_A
=
K [A_1/N + A_2 b/N^2],
```

```text
U_B
=
K^2 [
  B_2/N^2
  + B_3 b/N^3
  + B_4 b^2/N^4
].
```

#### Proof

A unary support-rank-`h` pattern containing `c` needs `h-1` further selected
indices and one matching edge. Its contribution is

```text
O(D_A,h(c)(b/N)^(h-1)b^-1).
```

A pattern not containing `c` contributes

```text
O(A_h(b/N)^h b^-1).
```

These are exactly the displayed marked and unmarked unary terms for `h=1,2`.

A binary support-rank-`h` pattern specifies two matching edges. If it contains
`c`, its contribution is

```text
O(D_B,h(c)(b/N)^(h-1)b^-2);
```

otherwise it is

```text
O(B_h(b/N)^h b^-2).
```

Substitute `h=2,3,4`. ∎

## 3. Total marked paid load

### Corollary PP3yl -- PROVED

Summed over every possible marked endpoint,

```text
sum_c M_A(c)
=
K [A_1/b + 2A_2/N],
```

and

```text
sum_c M_B(c)
=
K^2 [
  2B_2/(bN)
  + 3B_3/N^2
  + 4B_4 b/N^3
].
```

#### Proof

Apply PP3yj to the definitions of `M_A,M_B`. ∎

These formulas identify which support ranks can concentrate on the forced
endpoint after filler dilution.

## 4. Almost-everywhere paid completion

Let `C` be a credited endpoint bank of size `H`, and suppose every endpoint in
`C` carries at least one distinct unit of Xi-removal credit.

### Theorem PP3ym -- PROVED

Assume

```text
U_A+U_B=o(1)
```

and

```text
A_1/b + A_2/N
+ B_2/(bN) + B_3/N^2 + B_4 b/N^3
=o(H).
```

Then all but `o(H)` endpoints `c in C` satisfy

```text
M_A(c)+M_B(c)=o(1).
```

For every endpoint that is also source-light under PP3yf, one common marked
filler block has expected Xi-insertion cost `o(1)` and source-invalid expectation
`o(1)`. Hence a pool-compatible state moves that endpoint and strictly decreases
`Xi`.

#### Proof

The second hypothesis and PP3yl make the summed marked load `o(H)`. Apply Markov
with a slowly vanishing threshold. Add the paid and source nonnegative objectives
before choosing the filler block. One state has zero source violations and cost
below the endpoint's unit credit. Apply PP3kx. ∎

For a star centre carrying larger credit, replace the unit threshold by its exact
credit; the same proof uses normalized marked load.

## 5. Exact paid failure alternatives

### Corollary PP3yn -- PROVED

If the resource-bank branch does not yield a paid marked trade, at least one of
the following persists.

1. **Unmarked pool weight:**

   ```text
   A_1/N + A_2 b/N^2
   + B_2/N^2+B_3 b/N^3+B_4 b^2/N^4
   ```

   is bounded away from zero.
2. **Marked endpoint-load core:**

   ```text
   A_1/b + A_2/N
   + B_2/(bN)+B_3/N^2+B_4 b/N^3
   ```

   is at least a fixed positive multiple of `H`, or a positive fraction of the
   credited endpoints individually have paid load comparable with their credit.
3. **Source/hard-unary obstruction:** the endpoint is not among the source-light
   endpoints of PP3yf, in which case PP3yi supplies a unary star/resource branch.
4. **Predetermined star concentration:** one fixed captive centre has exceptional
   marked source or Xi load even though almost every resource-bank endpoint is
   good.

#### Proof

Negate PP3ym and use the source dichotomy PP3yf--PP3yi. ∎

## 6. Relation to the chromatic Xi endpoint

PP3tk used aggregate pool-local quantities `A_Xi,B_Xi` after equitable colouring.
The marked formulas refine them by endpoint-index support rank and distinguish:

- weight unavoidable for every filler choice;
- weight caused by forcing one credited endpoint;
- weight diluted by the full pool reservoir.

### Corollary PP3yo -- PROVED

For a positive-density credited resource bank, diffuse support-ranked Xi weight is
closed by marked filler dilution. The remaining dynamic resource-bank obstruction
is a marked paid-load core or a hard-unary star/resource conversion.

A predetermined captive star centre remains a separate one-point concentration
problem.

## 7. Revised dynamic endpoint

### Corollary PP3yp -- PROVED

Combining PP3ya, PP3yi, and PP3ym, the pool-compatible resource-bank branch is
closed whenever the support-ranked marked and unmarked Xi expressions vanish.
Failure is reduced to:

1. a unary source-star/resource bank generated by marked unary concentration;
2. a marked endpoint set carrying Xi load at the removal-credit scale;
3. a global full-pool unary/binary Xi-weight threshold;
4. one predetermined captive star centre with exceptional source or paid load.

Pool-local source pairs, triples, transitions, and diffuse Xi weights are no
longer separate open cases for a large credited resource bank.
