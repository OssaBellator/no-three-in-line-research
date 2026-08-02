# Incidence-weighted joint packet release

PX217 measures a joint packet family by its number of packets.  That is wasteful
when many packets are small or nearly disjoint.  The canonical dependency graph
depends only on the maximum number of packets incident with one row or column,
while the density loss depends on the total number of packet-cross events.

This chapter replaces packet count by these two intrinsic parameters.

## 1. Packet incidence and event energy

Work on an `h x h` matching block.  Let `F` be an ordinary forbidden-position
graph of maximum row and column degree `Delta`.  Let

\[
\mathscr P=\{P_\alpha\}
\]

be a finite family of partial matchings.  Put

\[
B=
\max\left\{
\max_i|\{\alpha:i\in\operatorname{dom}P_\alpha\}|,
\max_j|\{\alpha:j\in\operatorname{im}P_\alpha\}|
\right\}.
\]

For every unordered pair of arcs in one packet, forbid the associated cross
two-cycle.  Let `Q` be the number of distinct such rank-two bad events.  Always

\[
Q\le\sum_\alpha\binom{|P_\alpha|}{2}.
\]

Let `Omega_(F,mathscr P)` be the permutations avoiding every ordinary forbidden
cell and every packet cross.

### Theorem PX307 -- PROVED

If

\[
\boxed{h\ge32\max(1,\Delta,B),}
\]

then `Omega_(F,mathscr P)` is nonempty and

\[
\boxed{
|\Omega_{F,\mathscr P}|
\ge
\exp\left(-4\Delta-\frac{8Q}{h^2}\right)h!.
}
\]

Consequently every compatible prescribed rank-`r` partial matching `E` satisfies

\[
\boxed{
\Pr(E\subseteq M)
\le
\frac{\exp(4\Delta+8Q/h^2)}{(h)_r}
}
\]

for uniform `M` on `Omega_(F,mathscr P)`.

### Proof

Use singleton bad events of probability `1/h` and packet-cross events of
probability `1/(h(h-1))`.  In the canonical negative-dependency graph:

- a singleton conflicts with at most `2Delta-2` other singletons and at most
  `2B(h-1)` packet events;
- a packet event conflicts with at most `4Delta` singletons and at most
  `4B(h-1)` packet events.

Use witnesses

\[
x_1=\frac2h,
\qquad
x_2=\frac4{h^2}.
\]

The size hypothesis and Bernoulli's inequality give

\[
(1-x_1)^{2\Delta}\ge\frac78,
\qquad
(1-x_2)^{2B(h-1)}\ge\frac34,
\]

so the singleton local-lemma inequality holds.  Similarly,

\[
(1-x_1)^{4\Delta}\ge\frac34,
\qquad
(1-x_2)^{4B(h-1)}\ge\frac12.
\]

Thus the packet-event right side is at least `3/(2h^2)`, which dominates
`1/(h(h-1))` for `h>=3`.

The local lemma gives density at least

\[
(1-2/h)^{|F|}(1-4/h^2)^Q.
\]

Use `|F|<=Delta h`, `(1-2/h)^(Delta h)>=e^(-4Delta)`, and

\[
(1-4/h^2)^Q\ge e^{-8Q/h^2}.
\]

The cylinder estimate follows by dividing the trivial numerator `(h-r)!` by
the family-size lower bound. \(\square\)

When `P_alpha` are full order-`h` packets, `B<=k` and
`Q<=k h(h-1)/2`; PX307 recovers the scale `e^(4Delta+4k)` of PX217.

## 2. Incidence automatically controls packet energy

### Corollary PX308 -- PROVED

If every packet has size at most `h`, then

\[
\boxed{Q\le\frac12Bh^2.}
\]

Therefore PX307 gives the simpler bounds

\[
\boxed{|\Omega_{F,\mathscr P}|\ge e^{-4\Delta-4B}h!}
\]

and

\[
\boxed{
\Pr(E\subseteq M)
\le
\frac{e^{4\Delta+4B}}{(h)_r}.
}
\]

### Proof

Since `binom(m,2)<=hm/2`,

\[
Q
\le
\frac h2\sum_\alpha|P_\alpha|.
\]

Counting packet arcs by their source rows gives

\[
\sum_\alpha|P_\alpha|\le Bh.
\]

Substitute into PX307. \(\square\)

Thus arbitrarily many packets may be released at constant cost when their
row/column incidence is bounded.

## 3. Conditioning

Condition on an extendable partial matching `E_0` and let the residual order be
`n`.  In one packet, every exposed edge creates at most one complementary cell
which would complete a forbidden packet cross.  These complementary cells form
a partial matching.  Across all packets their union has maximum row and column
degree at most `B`.

Let `Q_res` be the number of distinct packet events remaining wholly residual.

### Theorem PX309 -- PROVED

If

\[
\boxed{n\ge32\max(1,\Delta+B),}
\]

then the number of allowed extensions is at least

\[
\boxed{
\exp\left(-4(\Delta+B)-\frac{8Q_{\rm res}}{n^2}\right)n!.
}
\]

Every compatible residual rank-`r` cylinder satisfies

\[
\boxed{
\Pr(E_1\subseteq M\mid E_0\subseteq M)
\le
\frac{\exp(4(\Delta+B)+8Q_{\rm res}/n^2)}{(n)_r}.
}
\]

### Proof

Delete the exposed rows and columns.  The inherited ordinary forbidden graph
has degree at most `Delta`.  For each packet, the complementary cells created
by exposure form one partial matching.  A fixed residual row belongs to such a
complement matching only for packets containing that row, and similarly for a
fixed residual column.  Hence the union complement degree is at most `B`.

The residual packet incidence is still at most `B`.  Apply PX307 with ordinary
forbidden degree `Delta+B`, order `n`, and event count `Q_res`. \(\square\)

## 4. Verification

Run

```bash
python scripts/verify_product_incidence_weighted_packet_release.py
```

The verifier checks the dependency counts on random packet families, validates
the local-lemma inequalities over the full threshold range, verifies the energy
bound `Q<=Bh^2/2`, and tests the conditioned complement-degree statement.