# Candidate packet energy needs linearly many levels in the worst case

PX215--PX218 show that every residual support-four mass extracts another product
level and that any fixed packet family can be released jointly. The natural next
hope is that an absolute number of packet extractions always suffices.

That statement is false for candidate support-four energy alone. A geometric-
progression packet grid has linearly many product levels, each with quadratic
energy, and total energy cubic in the packet order. Any fixed number of released
levels removes only a vanishing fraction.

The same calculation identifies a viable intermediate regime. PX217 allows a
logarithmic number of packets with only polynomial loss in the cylinder constant.
Such a loss can still be paid by sufficiently large endpoint-support excess.

## 1. Exact geometric-progression packet spectrum

Take packet order `h` and coordinates

\[
x_i=2^i,
\qquad
y_j=2^j,
\qquad 0\le i,j<h,
\]

with anchor `z=(0,0)`. The product level indexed by `s=i+j` is

\[
\mathcal P_s
=
\{i\to j:i+j=s\}.
\]

Its size is

\[
m_s
=
\begin{cases}
s+1,&0\le s<h,\\
2h-1-s,&h\le s\le2h-2.
\end{cases}
\]

Every two arcs in one level certify one support-four cross.

### Theorem PX221 -- PROVED

The total support-four packet energy at the anchor `z=(0,0)` is exactly

\[
\boxed{
\sum_{s=0}^{2h-2}\binom{m_s}{2}
=
2\binom h3+\binom h2
=
\frac{h(h-1)(2h-1)}6.
}
\]

Every one product level has energy at most

\[
\boxed{\binom h2.}
\]

Consequently, releasing any `k` product levels leaves residual candidate energy
at least

\[
\boxed{
\frac{h(h-1)(2h-1)}6
-k\binom h2.
}
\]

In particular:

1. every fixed `k` leaves `Theta(h^3)` residual energy;
2. reducing the total energy by one half requires at least

   \[
   \boxed{
   k\ge\frac{2h-1}{6}.
   }
   \]

Thus no absolute packet-count theorem follows from candidate support-four mass,
product-level overlap, and packet release alone.

### Proof

The level sizes are

\[
1,2,\ldots,h-1,h,h-1,\ldots,2,1.
\]

Using

\[
\sum_{m=1}^{h-1}\binom m2=\binom h3,
\]

one obtains the exact total. The largest level has size `h`, so every level has
energy at most `binom(h,2)`. Removing `k` levels can therefore remove at most
`k binom(h,2)` energy.

To remove at least half the total, one needs

\[
k\binom h2
\ge
\frac12\cdot\frac{h(h-1)(2h-1)}6,
\]

which simplifies to the displayed lower bound. \(\square\)

The obstruction is compatible with PX215: distinct levels for one anchor are
disjoint, yet there are linearly many large levels.

## 2. Consequence for the termination strategy

PX221 separates candidate energy from old selected defect mass. Packet release
can eliminate every candidate cross from a chosen level, but the current selected
matching contains only a small subset of those crosses. Therefore a terminating
potential must use at least one of:

1. weights induced by old selected defects rather than all candidate pairs;
2. simultaneous release of a growing packet family;
3. aggregation of many product levels into a different structured bank;
4. a potential charging each new packet to a decreasing anchor or endpoint
   resource.

Pure greedy removal of the largest candidate product level cannot prove bounded
termination.

## 3. Logarithmic packet families retain polynomial spread

The negative result does not rule out a slowly growing packet family. Let

\[
k\le\kappa\log h.
\]

### Theorem PX222 -- PROVED

For fixed forbidden degree `Delta` and all sufficiently large `h` satisfying the
PX217 threshold, the joint release family has density at least

\[
\boxed{
e^{-4\Delta}h^{-4\kappa}}
\]

and every rank-`r` cylinder satisfies

\[
\boxed{
\Pr(E\subseteq M)
\le
\frac{e^{4\Delta}h^{4\kappa}}{(h)_r}.
}
\]

After compatible exposure, the corresponding PX218 polynomial loss is at most
`h^(8 kappa)` up to an absolute factor depending on `Delta`, provided the
residual order is comparable to `h`.

### Proof

Substitute `k<=kappa log h` into the PX217 factors

\[
e^{-4\Delta-4k}
\quad\text{and}\quad
e^{4\Delta+4k}.
\]

Since `e^(4k)<=h^(4kappa)`, the unconditioned conclusions follow. PX218 has
factor `e^(4Delta+8k)`, giving the conditioned statement. \(\square\)

### Corollary PX222a -- PROVED

Under square-root endpoint thinning, a support-`u`, rank-`r` sector receives the
factor

\[
h^{-(u-r)/2}.
\]

The unconditioned logarithmic-packet spread still gives a power saving whenever

\[
\boxed{
\kappa<\frac{u-r}{8}.
}
\]

After arbitrary compatible exposure, the conditioned power saving remains when

\[
\boxed{
\kappa<\frac{u-r}{16}.
}
\]

Thus logarithmically many packet rounds are compatible with support-excess
accounting in sectors having enough excess. The minimal-excess sectors and the
short-cycle cores still require sharper treatment.

## 4. Updated frontier

The candidate-energy route now has a sharp boundary.

- `O(1)` packet levels do not suffice in general.
- `Theta(h)` levels can be necessary to remove a fixed fraction of unrestricted
  candidate energy.
- `O(log h)` levels retain polynomial cylinder spread and may be compatible with
  endpoint-support power savings.

The next viable termination theorem must therefore be **defect weighted** or
**scale sensitive**. A promising target is to prove that old selected defects
occupy only `O(log h)` heavy product levels, even though the unrestricted
candidate grid may occupy `Theta(h)` such levels.

## 5. Verification

Run

```bash
python scripts/verify_product_packet_count_barrier.py
```

The verifier checks the exact geometric-progression level spectrum, the cubic
energy identity, the half-energy packet lower bound, the fixed-packet
counterexample, and the logarithmic packet spread exponents.
