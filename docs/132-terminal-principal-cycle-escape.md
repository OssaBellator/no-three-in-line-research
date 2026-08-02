# Principal cycle escape below the Hall threshold

PX270--PX286 analyze perfect-matching failure in a terminal block. A full
rematching is stronger than the decoder actually needs: any nontrivial cyclic
permutation on a principal endpoint subset preserves row and column counts and
moves every endpoint on that cycle.

The historical forbidden graph always contains the current diagonal. Hence
the allowed cells define a loopless directed graph on endpoint labels. As soon
as the block order exceeds the forbidden row degree, every label has an allowed
out-neighbour and a directed cycle exists.

## 1. Allowed directed-cycle trade

Let `F subseteq [m] times [m]` have maximum row degree at most `Delta`, and
assume

\[
\boxed{(i,i)\in F\quad\text{for every }i.}
\]

Define a directed graph `A_F` on `[m]` by putting an arc `i to j` exactly when
`(i,j) notin F`.

### Theorem PX287 -- PROVED

If

\[
\boxed{m>\Delta,}
\]

then `A_F` contains a directed cycle of length at least two.

Consequently there is a nonempty principal label set

\[
J=\{i_1,\ldots,i_ell\},
\qquad \ell\ge2,
\]

and an allowed cyclic rematching

\[
\boxed{
i_1\mapsto i_2,
\ i_2\mapsto i_3,
\ \ldots,
\ i_\ell\mapsto i_1.
}
\]

Every endpoint of `J` moves.

### Proof

Every row has at least `m-Delta>=1` allowed cells, so every vertex of `A_F` has
outdegree at least one. Following successive outgoing arcs in a finite graph
must eventually repeat a vertex and hence contains a directed cycle. The
cycle cannot have length one because every diagonal cell is forbidden.
The corresponding cyclic assignment is a principal row-column-preserving
matching on its cycle labels. \(\square\)

This applies throughout the entire interval

\[
\Delta<m<2\Delta,
\]

where a full perfect matching may fail.

## 2. Designated-certificate decrease

### Corollary PX288 -- PROVED

Suppose every endpoint in the terminal block carries one injectively assigned
clean-star, loaded-line, radial, coordinate-field, or mixed-shadow certificate.
For `m>Delta`, an allowed cycle trade destroys at least

\[
\boxed{2}
\]

designated certificates and never recreates a paid ancestor certificate.

More generally, a cycle of length `ell` lowers the designated coordinate by at
least `ell`.

### Proof

PX287 moves every endpoint on the cycle away from its current diagonal cell.
PX278 gives one unique historical return position for each designated line
certificate and ancestor safety under the inherited forbidden graph. \(\square\)

Thus no terminal block with `m>Delta` is frozen at the designated level, even
when its allowed graph has positive Hall deficiency.

## 3. Exact cycle-core characterization

### Theorem PX289 -- PROVED

A principal endpoint subset `J` admits a fixed-point-free allowed rematching if
and only if the allowed digraph `A_F[J]` has a directed cycle cover. Every such
rematching decomposes uniquely into vertex-disjoint directed cycles of length
at least two.

In particular, the maximum number of endpoints which can be moved by a
principal allowed terminal trade is exactly the maximum size of a
vertex-disjoint directed-cycle packing in `A_F`.

### Proof

A principal rematching is a permutation of `J`. Its functional digraph is a
disjoint union of directed cycles. Diagonal avoidance excludes one-cycles.
Conversely, a directed cycle cover directly defines the permutation. \(\square\)

This identifies the exact principal terminal optimization problem when a full
matching fails.

## 4. Subpower cycle optimizer

### Corollary PX290 -- PROVED

For a terminal block of order `m=O(log log N)`, all allowed simple directed
cycles, all vertex-disjoint cycle packings, and their exact rank-at-most-three
collateral values can be enumerated in

\[
\boxed{\exp(O(m\log m))=N^{o(1)}}
\]

time.

The optimizer returns either:

1. a principal cycle trade with strict total improvement;
2. a largest designated decrease among all allowed cycle packings; or
3. an auditable terminal certificate that every allowed principal cycle
   packing is nonimproving.

### Proof

There are fewer than

\[
\sum_{\ell=2}^m\frac{(m)_\ell}{\ell}<e\,m!
\]

simple directed cycles. Enumerating subfamilies through permutation/cycle-
cover enumeration costs `exp(O(m log m))`; evaluating each state uses the
`O(m^6)` terminal certificate table of PX273. Apply PX275. \(\square\)

PX287--PX290 reduce the unresolved nonprincipal terminal range again. A block
can be genuinely immobile only after its order falls to `m<=Delta`, where some
rows may have no allowed nonhistorical position. Such trajectory-saturated
rows are the next terminal-core frontier.

## 5. Verification

Run

```bash
python scripts/verify_product_terminal_cycle_escape.py
```

The verifier exhausts all diagonal-forbidden graphs through order four,
checks cycle existence whenever `m>Delta`, compares principal rematchings with
directed cycle covers, and verifies the subpower cycle-count bound.
