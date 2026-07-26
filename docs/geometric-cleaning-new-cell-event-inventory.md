# New-cell pair-shadow inventory and intermediate-state margins

**Branch:** `research/geometric-cleaning`

GC2a shows that pure target or partner restriction cannot increase the
possible-cell pair-shadow.  GC3c identifies every increase caused by a genuinely
new possible-cell set `Y`.  The remaining elementary geometry is that a line of
primitive height at least `H` contains only

\[
\ell_H=1+\left\lfloor\frac{n-1}{H}\right\rfloor
\]

grid cells.  Consequently one new cell can form only `O(ell_H)` anchored pairs
at any fixed unchanged anchor.

The estimates below are deterministic.  They do not yet prove that the number
of newly possible target--partner assignments is small after every installed
bank state; that is the remaining geometric stability obligation.

## Pair-shadow conventions

Let `a` be one unchanged selected anchor.  Let `Z` be the old possible-cell set
and let `Y` be a disjoint set of genuinely new possible cells.  All cells in an
anchored pair are distinct from each other and from `a`.  Write

\[
m_H=(\ell_H-2)_+.
\]

The subtraction by two accounts for the anchor and one prescribed possible
cell already occupying the unique line through them.

Retain the GC3c notation

\[
e_H(a;Z,Y)
=
|\{(z,y)\in Z\times Y:
 a,z,y\text{ are compatible and collinear on a height-}\ge H\text{ line}\}|.
\]

## GC2b -- one-anchor new-cell pair bound -- PROVED

For every unchanged anchor `a`,

\[
\boxed{
e_H(a;Z,Y)\le |Y|m_H
}
\]

and

\[
\boxed{
\lambda_H(a;Y)\le \frac{|Y|m_H}{2}.
}
\]

Therefore GC3c's exact increment satisfies

\[
\boxed{
\lambda_H(a;Z\cup Y)-\lambda_H(a;Z)
\le
\frac{3}{2}|Y|m_H.
}
\]

### Proof

Fix `y in Y`.  The anchor and `y` determine one line.  If its primitive height
is at least `H`, that line has at most `ell_H` grid cells, so at most `m_H`
other cells can serve as `z`.  Summing over `y` gives the cross-pair bound.

For pairs contained in `Y`, orient every unordered pair in both directions.
For each first endpoint `y`, at most `m_H` second endpoints lie on the same
eligible line through `a`.  The oriented count is therefore at most
`|Y|m_H`, and division by two gives the second display.  Add the two bounds and
use GC3c's increment identity. QED.

The estimate intentionally ignores compatibility restrictions beyond
distinctness, so those restrictions can only lower the actual increment.

## Newly possible assignments

Suppose an intermediate state change makes `k` target--partner assignments
newly possible.  Each rectangle assignment inserts at most two cross-cells.
Let `Y` be the set of genuinely new possible cells contributed by those
assignments after duplicates are removed.  Then

\[
\boxed{|Y|\le 2k.}
\]

This statement does not require the new assignments to be mutually compatible
or simultaneously selectable.

## GC3e -- assignment-event pair-shadow inventory -- PROVED

Under the preceding hypotheses, every unchanged anchor satisfies

\[
\boxed{
\lambda_H(a;Z\cup Y)-\lambda_H(a;Z)
\le 3k m_H.
}
\]

If before the state change

\[
\lambda_H(a;Z)\le \Theta-\eta
\]

and

\[
\boxed{3k m_H\le\eta,}
\]

then the anchor remains nonexceptional after the change:

\[
\lambda_H(a;Z\cup Y)\le\Theta.
\]

For a sequence of intermediate states exposing `k_i` new assignments at step
`i`, the cumulative increase at one anchor is at most

\[
\boxed{3m_H\sum_i k_i.}
\]

Thus an initial pair-shadow reserve of that size protects the anchor throughout
the complete installation path, not only in the final state.

### Proof

The cell bound gives `|Y|<=2k`.  Substitute it into GC2b.  The margin and
multistep conclusions follow by addition. QED.

The cumulative statement inventories newly possible assignments, not the
number of assignments actually selected by one bank state.  A complete GC3
proof must control the former quantity or use a sharper structured overlap
bound.

## GC3f -- explicit threshold-crossing count -- PROVED

Let `A` be the current selected-anchor set, so `|A|<=2n`.  At one intermediate
state change exposing `k` newly possible assignments, let `E` be the anchors
whose pre-change load is at most `Theta-eta` and whose post-change load exceeds
`Theta`, for one `eta>0`.  Then

\[
\boxed{
|E|
<
\frac{6n k m_H}{\eta}.
}
\]

Across a sequence of steps, counting declarations with multiplicity,

\[
\boxed{
\sum_i |E_i|
<
\frac{6n m_H}{\eta}
\sum_i k_i.
}
\]

For integer loads, `eta` may be replaced in the denominator by
`floor(eta)+1` with a weak inequality.

### Proof

GC3c says every crossing in `E` requires more than `eta` units of pair-shadow
increment.  GC3e bounds the increment at each of at most `2n` anchors by
`3k m_H`, so the total increment over all anchors is at most
`6n k m_H`.  Comparing the required and available increments gives the first
bound.  Sum the same argument over steps for the second. QED.

This is a raw geometric inventory and may be much weaker than GC3d's paid
`RW/eta` bound.  Its value is that it reduces the missing paid comparison to a
concrete quantity: the number of newly possible target--partner assignments.

## Combined stability interface

Inside one scale-`H` installation path, suppose:

1. pure restrictions are handled by GC2a;
2. step `i` exposes at most `k_i` genuinely new assignments;
3. every initially nonexceptional anchor has reserve at least
   `3m_H sum_i k_i` below the threshold;
4. partner-pool depletion is controlled by GC1b and GC3a.

Then no unchanged anchor becomes pair-shadow exceptional at any intermediate
state.  Without item 3, GC3f gives the exact fallback count of possible new
exceptions.  A paid incidence theorem may replace the raw assignment count by
GC3d whenever each new-pair event has a bounded-reuse current owner.

## Corrected GC frontier

The GC1--GC3 interface now separates four tasks cleanly:

- initial blocker density;
- pool depletion;
- the number `k_i` of newly possible assignments at each intermediate state;
- paid ownership or bounded reuse of the resulting new-pair events.

The first two are independent of pair-shadow creation.  The third has the
explicit `3m_H` conversion proved here.  The fourth is the remaining route to a
scale-uniform exceptional-anchor budget when the raw `k_i` bound is too large.

## Finite check

`scripts/verify_geometric_new_cell_inventory.py` enumerates small grids, every
anchor, every height threshold and every disjoint pair of old/new possible-cell
sets.  It checks the line-length cap, both GC2b inequalities, the exact GC3c
increment decomposition and the `3k m_H` assignment bound for arbitrary lists
of new two-cell assignment outputs.
