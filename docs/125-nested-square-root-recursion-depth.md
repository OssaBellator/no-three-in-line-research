# Nested square-root recursion has logarithmic-logarithmic depth

PX195 returns a loaded line or a clean star whose selected endpoints lie in the
current rematching block. This allows the recursive decoder to be chosen
**nested**: every later endpoint block is a subset of the preceding block.
Combining this with exact-order weighted thinning gives square-root shrinkage at
every quantitatively nonterminal generation.

The result does not prove negative drift or absorb the final small core. It does
show that an absolute recursion depth is stronger than the probability theory
requires: `O(log log N)` nested generations have only subpower cumulative spread
loss.

## 1. Nested extraction from the PX195 shadow

Let `M` be the current matching block of order `t`. In the clean-star branch of
PX195a, the incidence graph has edges `(z,e)` with `z` a background anchor and
`e in M`, all collinear with one outside cell `f`.

### Theorem PX263 -- PROVED

Every clean-star or loaded-line output of PX195 can be converted to a movable
endpoint family contained in the current block `M`.

More precisely:

1. in the clean-star branch, if the incidence matching has `h` rays, choosing
   the `M`-endpoint of every ray gives `h` distinct matching cells of `M`;
2. in the loaded-line branch, the loaded selected cells are already a subset of
   `M`;
3. if the selected state lies in two permutation layers and `q_0` channels, one
   layer-channel type contains at least `h/(2q_0)` of these current-block cells.

The retained cells occupy distinct rows and columns.

### Proof

PX195a extracts a matching in the bipartite incidence graph `Z x M`, so its
`M`-endpoints are distinct. Since `M` is a matching, they occupy distinct rows
and columns. The loaded-line alternative is defined by many cells of `M` on one
line and has the same property.

There are at most `2q_0` layer-channel types. Pigeonholing the selected
current-block cells gives the last statement. \(\square\)

Thus later neutralization never has to enlarge the endpoint universe.

## 2. Exact-order simultaneous thinning

PX201 gives a retained set of size at least `qh/2` while controlling every
weighted rank-at-most-three support sector.

### Theorem PX264 -- PROVED

Assume `0<q<=1` and `qh>=32`. There is a retained set of **exact** order

\[
\boxed{s=\left\lfloor\frac{qh}{2}\right\rfloor}
\]

such that every PX201 sector `(r,u)` satisfies

\[
\boxed{W_{r,u}(J)\le16q^uW_{r,u}.}
\]

Every old clean-star or radial certificate assigned injectively to the retained
endpoints remains available as one unit of destruction or cancellation credit.

### Proof

PX201 supplies a set `J_0` with `|J_0|>=qh/2` and all displayed weight bounds.
Choose any subset `J subseteq J_0` of the required order. All certificate
weights are nonnegative, so passing to a subset cannot increase any sector.
Assigned endpoint certificates restrict injectively to `J`. \(\square\)

Exact order prevents uncontrolled slack from accumulating across generations.

## 3. Adaptive nested recurrence

At generation `j`, let the current nested block have order `t_j` and forbidden
degree at most

\[
\Delta_j\le\Delta_0+j.
\]

Let `h_j<=t_j` be the size of the nested obstruction extracted by PX263. Put

\[
b_j=\max\{32,16\Delta_j+4\}.
\]

If `h_j<b_j`, call the obstruction quantitatively terminal. Otherwise choose

\[
q_j=\max\left\{h_j^{-1/2},\frac{b_j}{h_j}\right\}
\]

and use PX264.

### Theorem PX265 -- PROVED

Every nonterminal generation admits a next nested block of order

\[
\boxed{
t_{j+1}=\left\lfloor\frac{q_jh_j}{2}\right\rfloor
}
\]

satisfying

\[
\boxed{t_{j+1}\ge8\Delta_j+2}
\]

and

\[
\boxed{
t_{j+1}
\le
\max\left\{\frac{\sqrt{t_j}}2,\frac{b_j}2\right\}.
}
\]

Consequently, after

\[
\boxed{d=O(\log\log t_0)}
\]

generations the chain reaches a block or extracted obstruction of order

\[
\boxed{O(\Delta_0+\log\log t_0).}
\]

### Proof

Since `h_j>=b_j`, one has `q_j<=1` and `q_jh_j>=b_j>=32`. PX264 applies and

\[
t_{j+1}\ge\left\lfloor\frac{b_j}{2}\right\rfloor
\ge8\Delta_j+2.
\]

The upper bound follows from `h_j<=t_j` and the definition of `q_j`.

If `h_j>=b_j^2`, then `h_j^{-1/2}>=b_j/h_j`, so
`t_(j+1)<=sqrt(t_j)/2`. If `b_j<=h_j<b_j^2`, then the next order is at most
`b_j/2`, already of terminal scale for the next generation up to an absolute
change in `b_j`.

Repeated square roots reduce `t_0` to a constant in at most
`ceil(log_2 log_2 max(t_0,4))+O(1)` steps. During that many steps,
`b_j=O(Delta_0+log log t_0)`, proving the terminal-order estimate. \(\square\)

## 4. Cumulative spread loss is subpower

Use the optimized cylinder factor of PX232--PX233 in every nonterminal block.

### Theorem PX266 -- PROVED

For a nested chain of length `d`, with `Delta_j<=Delta_0+j` and retained orders
at least `8Delta_j+2`, the product of all unconditioned or conditioned cylinder
losses is at most

\[
\boxed{
\prod_{j<d}e^{2\Delta_j}
\le
\exp\bigl(O(d\Delta_0+d^2)\bigr).
}
\]

With `d=O(log log t_0)` and fixed `Delta_0`, this is

\[
\boxed{
\exp(O((\log\log t_0)^2))=t_0^{o(1)}.
}
\]

The same conclusion holds when a fixed number of sequential matching blocks is
used per generation.

### Proof

PX232--PX233 give a factor at most `e^(2Delta_j)` for each matching block.
Summing `Delta_0+j` over `j<d` gives `O(dDelta_0+d^2)`. Finally
`(log log t)^2=o(log t)`. A fixed number of factors per generation changes only
the implicit constant. \(\square\)

Thus any polynomial support-excess saving survives the full nested recursive
probability loss.

## 5. What remains open

PX263--PX266 replace the former absolute-depth probability requirement by a
much weaker terminal-core problem.

They do **not** prove:

1. that every generation has strict negative drift;
2. that the terminal polylogarithmic block can always be absorbed;
3. that packet or coordinate-star branches always remain nested without a
   fixed-number two-block enlargement;
4. exact infinite product closure.

The immediate target is now a strict-sign-or-terminal theorem: every
nonterminal nested obstruction should either improve or produce the next nested
block, and every terminal block should admit a finite exact absorber.

## 6. Verification

Run

```bash
python scripts/verify_product_nested_recursion_depth.py
```

The verifier checks exact-order trimming, the adaptive recurrence, the
`O(log log t)` depth envelope, and the subpower cumulative spread exponent.
