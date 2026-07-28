# Hall-core missing-rectangle cause router

**Branch:** `research/geometric-cleaning`

GC2go--GC2gs return one weighted alternating Hall core `(X,Y)` with `N(X)=Y` and exact deficiency. This note exposes the complete blocked donor rectangle behind that core. Every donor outside `Y` is unavailable to every target in `X`; therefore the Hall obstruction is either a global donor-count shortage or a weighted family of exact blocked target--donor incidences which must concentrate on one cause or spread across many distinct causes.

The result preserves exact physical cause labels. It does not itself pay a target-common or global cause.

## Hall core and donor universe

Let `T` be the target side and `A` the exact physical donor dictionary, with

\[
 |A|=K.
\]

Fix a maximum matching and let `(X,Y)` be the canonical all-unmatched alternating Hall core from GC2go. Thus

\[
 Y=N(X),
 \qquad
 d=|X|-|Y|>0.
\]

Give every target `x in X` a nonnegative weight `w_x`, and write

\[
 W_X=\sum_{x\in X}w_x.
\]

Every unavailable pair `(x,a)` retains its least exact blocker/cause address from a fixed finite dictionary `C` of size `L_cause`.

## GC2gt -- complete missing rectangle -- PROVED

If `Y!=A`, then

\[
 \boxed{X\times(A\setminus Y)}
\]

is a complete rectangle of nonedges. Its unweighted size is

\[
 \boxed{|X|(K-|Y|)}
\]

and its target-weighted incidence mass is

\[
 \boxed{(K-|Y|)W_X.}
\]

### Proof

Because `Y=N(X)`, no donor outside `Y` is adjacent to any target in `X`. The product counts follow by summing one unavailable incidence for every pair in the rectangle, with target weight `w_x` repeated once for each donor outside `Y`. QED.

## GC2gu -- global donor-count alternative -- PROVED

If `Y=A`, then the Hall deficit is a pure global donor-count overload:

\[
 \boxed{|X|-K=d>0.}
\]

No outside-donor rectangle exists, and the exact output is the target set `X`, total donor count `K`, deficiency `d` and retained unmatched weight.

### Proof

Substitute `Y=A` into `d=|X|-|Y|`. QED.

## GC2gv -- weighted cause concentration -- PROVED

Assume `Y!=A`. Partition the missing rectangle by least exact cause. One cause class carries target-weighted incidence mass at least

\[
 \boxed{
 \frac{(K-|Y|)W_X}{L_{\rm cause}}.
 }
\]

The selected output retains the exact cause atom together with all target, donor, blocker, column, lineage and context fields of its incidences.

### Proof

The cause classes partition the total weighted mass from GC2gt. Weighted pigeonhole over at most `L_cause` classes gives the bound. QED.

## GC2gw -- concentration-or-spread alternative -- PROVED

Suppose every exact cause atom occurs on at most `Gamma` unweighted pairs of the missing rectangle. Then the number of distinct active causes is at least

\[
 \boxed{
 \left\lceil\frac{|X|(K-|Y|)}{\Gamma}\right\rceil.
 }
\]

Thus a Hall core yields either one cause with incidence above `Gamma`, or a quantitatively large family of distinct exact causes.

### Proof

If `R` cause atoms are active and each covers at most `Gamma` rectangle pairs, then together they cover at most `R Gamma` pairs. GC2gt supplies `|X|(K-|Y|)` pairs. Rearranging gives the bound. QED.

## GC2gx -- Hall-core cause router -- PROVED UNDER THE LEAST-CAUSE CONTRACT

Every weighted Hall core has one continuation:

1. `Y=A`, giving the exact global donor-count overload of GC2gu;
2. one target-common, global, line, collision, context or generator cause carries the weighted concentration of GC2gv;
3. no cause is heavy, and GC2gw returns many distinct exact cause atoms for occurrence-faithful removal, created-collateral descent, finite tickets or bounded-denominator/alternating-core delegation;
4. a cause label, donor identity, target role, lineage, context or legality interpretation changes, giving an explicit reset.

Consequently a failed donor assignment is no longer only a deficient set. It contains either a global cardinality obstruction or a complete blocked rectangle with an exact weighted cause profile.

### Proof

Apply GC2gu when `Y=A`. Otherwise use GC2gt and then GC2gv or GC2gw according to whether a heavy cause exists at the declared threshold. QED.

## Updated GC frontier

The bounded-reservoir Hall failure now preserves all of the following simultaneously:

- exact deficiency and unmatched-target weight;
- the canonical alternating core `(X,Y)`;
- either global donor-count overload or the full outside-donor missing rectangle;
- one heavy exact cause or many distinct exact causes.

Remaining GC5 work is payment or neutralization of target-common/global causes, unbounded or replenishable donor dictionaries, untagged feedback, clean-height preservation and local superregular resampling.

## Finite check

`scripts/verify_gc_hall_core_missing_rectangle.py` enumerates small donor graphs, computes canonical maximum matchings and alternating Hall cores, verifies the global-shortage/rectangle dichotomy, and audits weighted cause concentration and cause-spread counting.