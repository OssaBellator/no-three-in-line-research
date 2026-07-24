# Full width-two matching-block banks

The canonical adjacent state is only one of the 36 degree-preserving width-two
patches on four old columns and four old rows.  This chapter retains all 36
states for every four-edge deletion.  Equal margins are preserved, cell and pair
spread improve, and the finite clean-state hypergraph becomes substantially
less concentrated.

## 1. The complete local state family

Let `E` be an `r`-edge matching block and reserve new coordinates `a,b`.  For a
four-edge subset `D`, sort its four column endpoints and choose an ordered
partition into two unordered pairs.  Put the first pair in new row `a` and the
second in row `b`.  Independently choose an ordered pair partition of the four
row endpoints and put the two pairs in new columns `a,b`.

There are six ordered pair partitions on four labelled coordinates, hence 36
patch geometries `Q(D,sigma,tau)`.

Define

\[
 A^{D,\sigma,\tau}
 =
 (E\setminus D)\cup Q(D,\sigma,\tau).
\]

### Proposition PP3cf -- PROVED

The complete block bank has

\[
 \boxed{36\binom r4}
\]

states, and every state has the same row-incidence and column-incidence vectors:
one point on every old coordinate incident with `E` and two points on each
reserved new row and column.

#### Proof

The four deleted matching edges create deficit one on their old endpoint
coordinates.  Every width-two degree state restores each of those old columns
and rows once and gives two points to each new coordinate.  Undeleted edges
supply incidence one on all other block coordinates.  The partition choices do
not change any line sum. ∎

Any geometrically clean subfamily remains an equal-margin multistate domain.

## 2. Uniform spread before pruning

Choose `D` uniformly from `binom(E,4)` and choose the two ordered pair partitions
independently and uniformly.

### Proposition PP3cg -- PROVED

1. Every source edge is deleted with probability `4/r`.
2. Every prescribed movement or refill cell has probability at most

\[
 \boxed{\frac2r}.
\]

3. Every prescribed same-component patch pair has probability at most

\[
 \boxed{\frac4{r(r-1)}}.
\]

   If both cells lie on the same specified new line, the sharper bound is
   `2/(r(r-1))`.
4. A prescribed movement/refill pair controlled by the same source edge has
   probability at most `1/r`; requiring that source edge to remain makes the
   event impossible.
5. A prescribed movement/refill pair controlled by distinct source edges has
   probability at most

\[
 \boxed{\frac3{r(r-1)}}.
\]

#### Proof

A selected edge is assigned to either new movement row with probability `1/2`,
and independently to either new refill column with probability `1/2`.  This
gives the cell and same-edge cross-pair formulas.

Two specified edges are selected with probability `12/(r(r-1))`.  Conditional
on selection, an ordered pair partition puts both on one specified line with
probability `1/6`, and puts them on two specified different lines with
probability `1/3`.  The movement and refill partition choices are independent,
giving the remaining bounds. ∎

Compared with the canonical bank, prescribed cell probability falls from `4/r`
to `2/r`, while ordinary pair probabilities improve by another constant factor.

## 3. Clean-domain restriction

Let

\[
 \Omega_{36}(E)
 =
 \{(D,\sigma,\tau):A^{D,\sigma,\tau}
   \text{ is no-three-in-line}\}.
\]

### Proposition PP3ch -- PROVED

If `Omega_36(E)` has density `delta` inside the complete bank, then uniform
sampling from the clean domain preserves the PP3cg bounds with an additional
factor `1/delta`.

#### Proof

Every event count in the clean domain is at most its count in the full state
space.  Divide the full-space probability upper bounds by the surviving state
fraction `delta`. ∎

Thus a polynomially large clean fraction gives a polynomially spread multistate
variable.  Unlike the canonical family, the full bank may also repair a unary
anchor obstruction by changing the pair partitions without changing which four
source edges are deleted.

## 4. Clean deletion hypergraph with geometry multiplicity

Define a four-edge deletion `D` to be **36-clean** if at least one of its 36
patch geometries lies in `Omega_36(E)`.  The 36-clean deletions form a 4-uniform
hypergraph on `E`, and each hyperedge carries a multiplicity equal to the number
of clean geometries.

The packing theorems PP3cc--PP3ce apply to this enlarged deletion hypergraph.
The multiplicities provide additional local state entropy after disjoint
reservoirs have been selected.

## 5. Finite results

The script

```bash
python scripts/analyze_full_width_two_block_bank.py \
  certificates/prime-patching-small.json
```

computes clean geometry counts, clean deletion sets, exact maximum matchings, and
minimum transversals.

For complete stored matching layers:

| Side | Layer 0 clean states / total | Layer 1 clean states / total |
|---:|---:|---:|
| 4 | `5/36` | `5/36` |
| 5 | `11/180` | `14/180` |
| 6 | `27/540` | `43/540` |
| 7 | `29/1260` | `53/1260` |
| 8 | `92/2520` | `83/2520` |
| 9 | `47/4536` | `59/4536` |
| 10 | `63/7560` | `83/7560` |

The corresponding numbers of 36-clean deletion sets and their packing data are:

| Side | Layer 0 deletions / matching / transversal | Layer 1 deletions / matching / transversal |
|---:|---:|---:|
| 4 | `1 / 1 / 1` | `1 / 1 / 1` |
| 5 | `4 / 1 / 1` | `4 / 1 / 1` |
| 6 | `13 / 1 / 2` | `11 / 1 / 2` |
| 7 | `15 / 1 / 2` | `22 / 1 / 3` |
| 8 | `34 / 2 / 3` | `34 / 2 / 3` |
| 9 | `29 / 2 / 3` | `30 / 2 / 2` |
| 10 | `33 / 2 / 3` | `47 / 2 / 3` |

Retaining all width-two geometries therefore breaks the canonical
matching-number-one obstruction at sides eight through ten.  It still does not
produce a large packing on the stored seeds, but it demonstrates that endpoint
geometry multiplicity can diffuse the clean deletion domain.

## 6. Revised target

A scalable constant-width block construction should prove simultaneously:

1. a clean-state density `delta>=r^{-O(1)}` or preferably `delta=Omega(1)`;
2. a diffuse 36-clean deletion hypergraph with matching number proportional to
   the required number of rungs;
3. external and cross-block bad-box probabilities that remain small after the
   `1/delta` conditioning loss;
4. protected trades for the residual low-transversal core.

The full 36-state bank is the natural finite-state replacement for the rigid
canonical block whenever unary local concentration is the main failure.