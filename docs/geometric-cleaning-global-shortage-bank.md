# Global donor-shortage potential and adverse bank

**Branch:** `research/geometric-cleaning`

GC2gt--GC2hc route every bounded-reservoir Hall failure to a blocked rectangle, a cause-capacity overload, or the pure global case in which every donor already lies in the Hall neighbourhood. This note gives the pure global case an exact one-dimensional potential.

## Signed shortage

For target set `T` and donor set `A`, define

\[
s=|T|-|A|.
\]

A progress operation removes `r` targets and adds `a` donors. An adverse operation recreates `c` targets and destroys `z` donors. The exact update is

\[
s'=s-(r+a)+(c+z).
\]

The actual Hall shortage is `s_+=max(s,0)`.

## GC2hd -- exact global-shortage update -- PROVED

The signed shortage changes by progress mass `r+a` minus adverse mass `c+z`, exactly as displayed.

### Proof

Substitute `|T'|=|T|-r+c` and `|A'|=|A|+a-z`. QED.

## GC2he -- monotone global repair -- PROVED

If no target is recreated and no donor is destroyed, every nontrivial repair strictly lowers `s`. Therefore a positive global shortage cannot recur under target removal and donor addition alone.

## GC2hf -- closed count cycles require exact adverse compensation -- PROVED

On every closed count cycle returning to the same pair `(|T|,|A|)`,

\[
\sum(r+a)=\sum(c+z).
\]

### Proof

Sum GC2hd around the cycle. The total signed-shortage change is zero. QED.

## GC2hg -- finite adverse bank -- PROVED UNDER THE NONREPLENISHING CONTRACT

Suppose target recreations and donor destructions consume an exact nonnegative bank of total capacity `B_adv`. Then the cumulative progress mass occurring inside recurrent global-shortage episodes is at most `B_adv`.

In particular, every unit of repeated target removal or donor addition must be matched by one paid adverse unit before the count state can return.

### Proof

GC2hf equates progress and adverse mass on each closed episode. Nonreplenishing adverse capacity bounds the latter. QED.

## GC2hh -- pure global-shortage router -- PROVED UNDER COMPLETE COUNT LINEAGE

A pure global Hall shortage has one continuation:

1. strict decrease of `s` by target removal or donor addition;
2. current payment by an adverse recreation/destruction source;
3. finite debit from the adverse bank;
4. capacity-one target-recreation or donor-destruction tickets;
5. physical impossibility of the selected adverse edge;
6. or an explicit reset in target/donor dictionary, multiplicity, lineage, clean-height or context interpretation.

Thus the `Y=A` Hall-core case is no longer an unstructured global obstruction. Remaining work is to pay or exclude the exact adverse source, or handle genuinely replenishable global target/donor creation.

## Finite check

`scripts/verify_gc_global_shortage_bank.py` generates exact target/donor count histories, checks the signed update, verifies closed-cycle progress/adverse equality and audits the nonreplenishing adverse bank.