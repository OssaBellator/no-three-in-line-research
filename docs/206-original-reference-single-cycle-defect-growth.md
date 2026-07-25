# Original-reference defect growth under fresh-helper single-cycle moves

The adaptive cascade theorems PP3aih--PP3air control every *planned* sequence of
marked source-star moves of depth `o(W)`, but they do not explain why a sequence
cannot continue indefinitely. A fixed original permutation layer supplies an
additional exact invariant.

Keep one original matching layer `M_0` as a reference. At each generation choose
one marked centre from the current defect and choose every other endpoint from
rows on which the current layer still agrees with `M_0`. Use a single-cycle
endpoint state on this selected block. The move then inserts the untouched
helpers into the one relative-permutation cycle containing the centre. It
increases the defect size by exactly `q-1`, does not create another defect cycle,
and cannot reinsert an original selected edge.

Thus a canonical marked cascade is monotone relative to `M_0`. Starting from one
single-cycle seed, the entire defect remains one growing alternating cycle.

## 1. Relative permutation and defect cycles

Let

```text
M_0={(i,pi_0(i)):i in [m]}
```

be the fixed original permutation layer and let

```text
M={(i,pi(i)):i in [m]}
```

be a current permutation layer on the same row and column resources. Define

```text
sigma=pi_0^{-1} o pi
```

and

```text
D(M)={i:pi(i) != pi_0(i)}.
```

### Proposition PP3ais -- PROVED

The fixed points of `sigma` are exactly the rows outside `D(M)`. The nontrivial
cycles of `sigma` are exactly the alternating cycles of `M_0 triangle M`, with a
cycle of length `ell` in `sigma` corresponding to an alternating cycle of length
`2ell` in the union of the two matchings.

#### Proof

Row `i` is fixed by `sigma` exactly when

```text
pi_0^{-1}(pi(i))=i,
```

which is equivalent to `pi(i)=pi_0(i)`. On a nontrivial cycle

```text
i_1 -> i_2 -> ... -> i_ell -> i_1
```

of `sigma`, the current edge from row `i_j` ends in the original column of
`i_(j+1)`. Alternating current and original edges gives the corresponding even
cycle in `M_0 union M`. The construction is reversible. ∎

In particular

```text
|D(M)|
```

is the total row-length of the nontrivial relative cycles.

## 2. A single-cycle seed creates one defect cycle

Choose a set `I` of `q>=3` rows on which `M=M_0`, and let `tau` be one directed
`q`-cycle on `I`. Replace the selected current columns according to

```text
pi'(i)=pi(tau(i))  for i in I,
pi'(i)=pi(i)       for i outside I.
```

### Proposition PP3ait -- PROVED

The new relative permutation is

```text
sigma'=sigma o tau.
```

If every row of `I` was fixed by `sigma`, then `sigma'` has exactly one new
nontrivial cycle, namely `tau`, and

```text
|D(M')|=|D(M)|+q.
```

Every selected current edge is moved and every selected new edge is outside
`M_0`.

#### Proof

The composition formula follows from

```text
pi_0^{-1} o pi'=(pi_0^{-1} o pi) o tau.
```

On `I`, `sigma` is the identity, so the restriction of `sigma'` is `tau`. Outside
`I` nothing changes. Because `tau` has no fixed point, no selected row retains
its original selected column. ∎

This is the original-reference form of the universal single-cycle state
PP3yx--PP3za.

## 3. Fresh-helper growth is exact

Now suppose `c in D(M)` lies in a nontrivial cycle `C` of `sigma`. Choose

```text
H={h_1,...,h_(q-1)} subseteq [m]\D(M)
```

and put `I={c} union H`. Let `tau` be any directed `q`-cycle on `I`, and again set
`pi'=pi o tau` on the selected rows.

### Theorem PP3aiu -- PROVED

The move has all of the following properties.

1. Every row in `I` is defective after the move.
2. No selected new edge belongs to `M_0`.
3. The relative cycle `C` is replaced by one cycle of length

   ```text
   |C|+q-1.
   ```

4. Every other nontrivial relative cycle is unchanged.
5. Consequently

   ```text
   |D(M')|=|D(M)|+q-1,
   ```

   and the number of nontrivial defect cycles is invariant.

#### Proof

For a helper `h`, the unique selected column equal to `pi_0(h)` is its current
column `pi(h)`, and the single cycle `tau` does not fix `h`. Thus no helper row
receives its original column.

The original column `pi_0(c)` is not among the selected current columns. Indeed,
its current preimage is another defective row: it cannot be `c`, and it cannot be
a fixed helper because `pi_0` is injective. Hence the centre row also cannot
receive its original column.

The support of `tau` meets the nontrivial cycles of `sigma` in exactly the one
vertex `c`; all helpers are singleton cycles. Multiplying `sigma` on the right by
the `q`-cycle splices those `q-1` singleton cycles into `C`. Written from `c`, the
new cycle follows the helper order prescribed by `tau` and then resumes the old
cycle at `sigma(c)`. No other cycle is touched. The length and defect-count
formulas follow. ∎

The result is independent of the cyclic ordering of the helpers.

## 4. New cascade centres are automatically free

Assume every fixed controller edge belongs to `M_0` and is preserved throughout
the cascade.

### Proposition PP3aiv -- PROVED

Every point corresponding to a row in `D(M)` is outside the fixed controller
infrastructure. Hence every source-star centre created by the defect cascade is
a free centre in the sense of PP3ki.

#### Proof

A controller point in row `i` is the fixed original edge `(i,pi_0(i))`. A defect
point in that row is `(i,pi(i))` with `pi(i)!=pi_0(i)`, so it is not the controller
point. It cannot equal a controller point in another row because the row
coordinates differ. ∎

This removes the captive-centre alternative after the initial seed.

## 5. The untouched-original helper reservoir remains linear

Let the selected controller pools occupy at most `(rho+o(1))m` rows of the
reference layer for some fixed `rho<1`. Suppose the current defect size is
`S=o(m)`.

### Proposition PP3aiw -- PROVED

Outside the controller pools there are

```text
(1-rho-o(1))m-S=Theta(m)
```

current edges that still agree with `M_0`. They form an ambient fresh-helper
reservoir for every defect centre.

Choosing `q-1` helpers uniformly from this reservoir and then a uniform directed
single cycle on the selected block has the same fixed-rank cylinder orders as
PP3yy, with the ambient pool size replaced by `Theta(m)`. Thus the marked source
and support first-moment arguments transfer whenever their normalized lightness
hypotheses hold uniformly on this fresh reservoir.

#### Proof

At most the controller rows and the `S` defect rows are unavailable. The count is
therefore the displayed quantity. Uniform subset probabilities are ordinary
hypergeometric ratios on a linear-sized ground set, and conditional single-cycle
arc probabilities are exactly those of PP3yy. ∎

This is a host interface, not an unconditional assertion that every generation
is source-valid. Failure is still an explicit marked source, transition,
anchor, Hall, alternating-host, or distinguished endpoint-host certificate.

## 6. Canonical one-cycle cascade

### Corollary PP3aix -- PROVED / CONDITIONAL FRESH-HELPER MARKED INTERFACE

Suppose:

1. the first free-centre move uses `q` untouched original rows and one
   source-valid single-cycle state;
2. every later move uses one centre in the current defect and `q-1` untouched
   original helpers;
3. the corresponding source-valid single-cycle marked host exists at each step.

After `t>=1` moves, the relative permutation has exactly one nontrivial cycle and

```text
|D(M_t)|=q+(t-1)(q-1).
```

Every post-seed centre is free, the fixed controller universe is unchanged, and
the defect cycle grows monotonically by `q-1` rows per generation.

No abstract recurrence or repeated-state phenomenon is possible inside this
canonical cascade. The only ways it can stop are direct completion, failure of a
required marked host, or arrival at a prescribed defect-size boundary.
