# Scale-filtered alternating-core menus

**Branch:** `research/alternating-core-chain`

AC5b--AC5f reduce reverse-scale compatibility at dyadic height `H` to two
quantities for a certified multicover batch `B`:

\[
N_{2H}(S,S')=0,
\qquad
N_H(S\setminus B,S')<|B|.
\]

Existing alternating-core banks already produce finite menus with exact
physical states and complete created-triple ledgers.  This note gives the
canonical way to apply the scale audit to any such menu.  First delete every
state creating a protected-band triple.  On the surviving menu, only the
current-threshold count remains.  If no state survives, retain one exact
high-line triple from a polynomial witness dictionary rather than discarding
the failed menu.

The note also records the intermediate-state condition required by multistep
BDA, RI, phase and petal installations.  Final cleanliness alone does not
justify an intermediate transition which temporarily violates a protected
line.

## Complete finite menus

Let `S` be the current two-layer grid state and suppose

\[
\Psi_{2H}(S)=0.
\]

Let `B` be a certified multicover batch at threshold `H`, and put

\[
S^-=S\setminus B.
\]

Let

\[
\mathcal M=\{S_\theta:\theta\in\Theta\}
\]

be one finite alternating-core menu.  Every state is assumed to have:

- complete physical row-column realization;
- a complete AC3v feasibility envelope;
- exact changed-cell and owner records;
- exact created collinear triples, including their supporting lines.

The alternatives need not be mutually compatible because exactly one state is
selected.

Define the protected-band survivor set

\[
\Theta_{<2H}
=
\{\theta\in\Theta:
  N_{2H}(S,S_\theta)=0\}.
\]

## AC5g -- exact protected-band menu filter -- PROVED

For every menu state,

\[
\boxed{
\theta\in\Theta_{<2H}
\iff
\Psi_{2H}(S_\theta)=0.
}
\]

Consequently the survivor set is obtained exactly by adding to the menu's hard
feasibility system every potential newly created triple of height at least
`2H` which meets the changed-cell envelope.

### Proof

If the new high-triple count is zero, AC5c and the upper-`2H` cleanliness of
`S` give `Psi_{2H}(S_theta)=0`.  Conversely, a state with zero protected-band
excess contains no collinear triple on a line of height at least `2H`, so its
new high-triple count is zero.  The hard-filter statement follows because a
new triple necessarily meets the changed-cell envelope, and forbidding every
such triple removes exactly the nonsurviving states. QED.

This filter does not assign payment to the excluded high-line geometry.  It is
a hard feasibility restriction.

## AC5h -- filtered expectation gives a reverse-scale state -- PROVED

Assume `Theta_<2H` is nonempty.  Let `mu` be any probability law supported on
the survivor set.  If

\[
\boxed{
\mathbb E_{\theta\sim\mu}
N_H(S^-,S_\theta)
<|B|,
}
\]

then some survivor state satisfies the complete AC5 audit:

\[
N_{2H}(S,S_\theta)=0,
\qquad
N_H(S^-,S_\theta)\le |B|-1.
\]

Hence

\[
\Psi_H(S_\theta)<\Psi_H(S)
\]

while all previously settled bands remain clean.

### Proof

Every state in the law passes the protected-band filter.  Since the expected
integer current-threshold count is below `|B|`, one state has count at most
`|B|-1`.  Apply AC5e and AC5c. QED.

The probability law may be uniform, product-derived, rank-conditioned or any
other exact finite menu law.  It must be renormalized after filtering unless
the original law already assigns zero probability to excluded states.

## Failed protected-band filters

Suppose the survivor set is empty.  Every menu state then contains at least one
new triple supported on a line of height at least `2H`.  Fix orders on physical
cells and triples and assign each state its least such witness.

Let `Z` be the union of all cells which can be inserted by any menu state, and
put `z=|Z|`.  The grid has `n^2` physical cells.  Every new triple contains at
least one cell of `Z`, so the ambient witness stock has size at most

\[
W_{\rm high}
\le
z\binom{n^2}{2}.
\]

The coarser board-only bound is

\[
W_{\rm high}
\le
\binom{n^2}{3}
=O(n^6).
\]

## AC5i -- failed-filter high-line concentration -- PROVED

Give the failed menu states nonnegative weights of total `W`.  One exact new
protected-band triple is the least witness for states of total weight at least

\[
\boxed{
\frac{W}{W_{\rm high}}.
}
\]

That witness retains:

- its three physical cells;
- its unique supporting real line and primitive height;
- the subset of new cells;
- the menu/owner/transition records of every incident state.

It enters the geometric-cleaning high-line blocker or a dedicated arithmetic
line router.  It receives no destroyed-payment credit merely from blocking all
menu states.

### Proof

Every failed state chooses one witness from a stock of size at most
`W_high`.  Weighted pigeonhole gives the displayed class.  The remaining data
are deterministic functions or retained transition records.  The payment
warning follows from the same prospective-geometry rule as AC3ln. QED.

Thus a failed AC5 filter is not an unspecified loss of the menu.  It is one
polynomially indexed exact protected-line obstruction.

## Rank and height refinement

For every new triple `T subset S_theta`, define its created-cell rank relative
to `S^-` by

\[
r(T)=|T\setminus S^-|\in\{1,2,3\}.
\]

Split its supporting line into two scale classes:

- current band: `H <= h(T) < 2H`;
- protected band: `h(T) >= 2H`.

Write

\[
C_{r,\mathrm{cur}}(\theta),
\qquad
C_{r,\mathrm{high}}(\theta)
\]

for the six exact counts.

## AC5j -- exact rank-height ledger -- PROVED

Every menu state has the exact partition

\[
\boxed{
N_H(S^-,S_\theta)
=
\sum_{r=1}^{3}
\bigl(
C_{r,\mathrm{cur}}(\theta)
+
C_{r,\mathrm{high}}(\theta)
\bigr).
}
\]

Moreover,

\[
\boxed{
N_{2H}(S,S_\theta)
=
\sum_{r=1}^{3}C_{r,\mathrm{high}}(\theta)
}
\]

when the rank ledger uses the same physical baseline for the protected-band
triples.  On the filtered menu all three high-band counts vanish, so the AC5h
expectation reduces to

\[
\mathbb E
\sum_{r=1}^{3}C_{r,\mathrm{cur}}<|B|.
\]

### Proof

Every new triple has one created-cell rank and one unique supporting line.  The
line lies in exactly one of the two scale classes.  Partition the triple set by
these six labels. QED.

This is the required refinement of AC3fa.  Rank-only created mass is not a
reverse-scale certificate; rank plus supporting-line height is exact.

## Intermediate-state stability

Some installed banks are executed by a sequence

\[
S_0=S,
S_1,
\ldots,
S_t=S_\theta
\]

rather than one atomic state replacement.  Protected banks and later local
repairs may need every `S_j` to remain upper-`2H`-clean.

## AC5k -- stepwise high-line exclusion preserves every intermediate state -- PROVED

Assume

\[
\Psi_{2H}(S_0)=0
\]

and, for every step `j=1,...,t`,

\[
\boxed{
N_{2H}(S_{j-1},S_j)=0.
}
\]

Then

\[
\boxed{
\Psi_{2H}(S_j)=0
\quad(0\le j\le t).
}
\]

Therefore a multistep AC menu is intermediate-state safe whenever every local
step has a complete high-line hard envelope.  Checking only the final state is
not sufficient for contracts which require protected cleanliness during the
installation.

### Proof

Apply AC5c inductively.  The initial state is clean.  If `S_{j-1}` is clean and
the step creates no new protected-band triple, then `S_j` is clean. QED.

Current-band excess may rise temporarily unless the particular bank requires a
stronger invariant.  AC5k addresses protected-band persistence; the final
`Psi_H` drift is supplied by AC5h.

## Interface to installed AC menus

For each pivot, BDA, RI, target, common-host cycle or petal menu:

1. form the exact protected-band survivor set using AC5g;
2. if it is empty, retain the AC5i exact high-line obstruction;
3. otherwise refine created triples by AC5j;
4. prove an expected survivor count below `|B|` and apply AC5h;
5. for a multistep realization, prove AC5k at every intermediate step.

The high-line filter can be included directly in the AC3v hard registry.  Any
change to the declared protected-line registry or its physical occurrence data
is an outer-profile reset and must remain visible to AC3ka--AC3lc.

## Consequence

The AC5 frontier is now menu-local and exact.  For every installed finite bank,
only three outputs remain:

1. a scale-audited state with strict `Psi_H` descent;
2. one exact protected-band triple from a polynomial witness stock;
3. a protected-registry or physical-realization reset.

The unresolved geometric work is to prove that enough states survive the high
filter and that their rank-height current-band expectation is below the
certified batch size, uniformly after earlier switches.

## Finite check

`scripts/verify_ac_scale_filtered_menus.py` exhausts all state pairs on the
`3 x 3` grid at two thresholds, verifies the exact protected-band filter,
checks stepwise high-line preservation on all one-point paths of length two,
exhausts abstract filtered expectation ledgers, verifies weighted failed-filter
concentration, checks every small rank-height partition and audits the
polynomial high-triple witness bounds.