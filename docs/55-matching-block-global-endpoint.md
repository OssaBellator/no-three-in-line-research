# Global completion endpoint for full width-two matching blocks

The full 36-state block bank closes local degree bookkeeping and supplies explicit
cell and pair spread.  This chapter converts those estimates into one global
first-moment inequality covering retained-core, cross-block, and three-block
triples.

## 1. Prepared clean block variables

Let `E_1,...,E_K` be pairwise disjoint matching blocks, each of size `r>=4`, and
reserve one disjoint width-two new-coordinate interval for each block.  For block
`i`, let `Omega_i` be a nonempty locally no-three subfamily of the full 36-state
bank from PP3cf.  Assume

\[
 |\Omega_i|
 \ge
 \delta\,36\binom r4
\]

for one common `0<delta<=1`.  Choose the block states independently and uniformly.
All row and column sums are preserved by PP3cf.

For one block, PP3cg and conditioning give the following convenient bounds:

- one prescribed patch cell:

\[
 q_1=\frac{2}{\delta r};
\]

- one movement/refill pair controlled by the same source edge:

\[
 q_h=\frac{1}{\delta r};
\]

- any other prescribed patch pair in that block:

\[
 q_2=\frac{8}{\delta r^2}.
\]

The last estimate uses
`4/[r(r-1)]<=8/r^2`.  A triple wholly inside one block has probability zero by
the definition of `Omega_i`.

## 2. Certificate profiles

Every remaining possible collinear triple has exactly one of the following
profiles.  Fixed points mean selected points outside all block supports.

- `N_1`: two fixed points and one patch cell from one block.
- `N_h`: one fixed point and a same-edge movement/refill pair from one block.
- `N_2`: one fixed point and an ordinary patch pair from one block.
- `N_11`: one fixed point and one patch cell from each of two blocks.
- `N_h1`: a same-edge pair from one block and one cell from another block.
- `N_21`: an ordinary pair from one block and one cell from another block.
- `N_111`: one patch cell from each of three distinct blocks.

Duplicate geometric triples are counted once.  Profiles involving three patch
points from one block are absent because every local state is clean.

## 3. Explicit first-moment theorem

### Theorem PP3ci -- PROVED

A valid saturated no-three assignment exists whenever

\[
\boxed{
 \frac{2N_1+N_h}{\delta r}
 +\frac{8N_2}{\delta r^2}
 +\frac{4N_{11}+2N_{h1}}{\delta^2r^2}
 +\frac{16N_{21}}{\delta^2r^3}
 +\frac{8N_{111}}{\delta^3r^3}
 <1.
}
\]

#### Proof

For each candidate triple, expose only the block variables meeting it.

- A profile-`N_1` triple requires one prescribed cell, with probability at most
  `q_1`.
- A profile-`N_h` triple requires one same-edge pair, with probability at most
  `q_h`.
- A profile-`N_2` triple requires one ordinary pair, with probability at most
  `q_2`.
- A profile-`N_11` triple requires one prescribed cell in each of two independent
  blocks, with probability at most `q_1^2`.
- A profile-`N_h1` triple has probability at most `q_h q_1`.
- A profile-`N_21` triple has probability at most `q_2 q_1`.
- A profile-`N_111` triple has probability at most `q_1^3`.

Substituting the displayed values of `q_1,q_h,q_2` gives the seven terms in the
boxed inequality.  Their sum bounds the expected number of selected collinear
triples.  If it is below one, some assignment selects none.  Equal margins give
saturation. ∎

The theorem is deletion-aware through the clean local state domains.  In
particular, the high raw probability of a same-edge movement/refill pair is paid
only in the `N_h` and `N_h1` profiles; when its source edge is the proposed
retained anchor, the event is impossible and should not be counted.

## 4. Asymptotic corollary

### Corollary PP3cj -- PROVED

Suppose `delta` is bounded below by a positive constant and, as `r` tends to
infinity,

\[
 N_1+N_h=o(r),
\]

\[
 N_2+N_{11}+N_{h1}=o(r^2),
\]

and

\[
 N_{21}+N_{111}=o(r^3).
\]

Then the block bank contains a valid saturated no-three assignment.

#### Proof

Each group of terms in PP3ci tends to zero under the stated assumptions. ∎

More generally, polynomially small clean density can be accommodated by inserting
the corresponding powers of `delta` in the three displayed requirements.

## 5. Bounded-occurrence alternative

Let `p` be the largest exact bad-box probability after local cleaning and let
each block variable occur in at most `Delta` distinct remaining bad boxes.
PP3bl gives a valid assignment whenever

\[
 3p(3\Delta-2)\le1.
\]

The crude spread bounds above give `p<=2/(delta r)` for every nonempty profile.
Therefore the directly checkable sufficient condition

\[
\boxed{
 \Delta
 \le
 \frac{\delta r+12}{18}
}
\]

implies completion.

Indeed, this inequality gives
`3(2/(delta r))(3Delta-2)<=1`.  Exact profile probabilities can improve the
constant substantially, especially for rank-two and rank-three boxes.

## 6. Remaining geometric theorem

The constant-width matching-first route is now reduced to constructing blocks
with three simultaneous properties:

1. clean-domain density `delta` large enough for PP3ci or PP3bl;
2. a diffuse clean-deletion hypergraph large enough to pack the required
   `K=T/2` disjoint rungs;
3. certificate profile counts `N_1,N_h,N_2,N_11,N_h1,N_21,N_111` satisfying the
   boxed first-moment inequality, or block occurrence at most `O(delta r)`.

For the published transfer width `T=m^0.525`, the natural block scale is
`r=m^0.475`.  The unresolved work is therefore a quantitative secant-shadow and
cross-block incidence theorem at this block scale, not matching availability or
row-column completion.