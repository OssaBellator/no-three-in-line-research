# Private payment and no-recycling for RI companion outputs

**Branch:** `research/alternating-core-chain`

AC3db--AC3df reduce every incomplete rational fibre and one-root scale imbalance to a carry defect, an off-family current companion factor, or a row-column-disjoint family of one-cell companion completions. This note proves the missing payment interface for the latter two outputs. After one exact orientation and fibre are fixed, every companion record has a private original current factor. The corresponding Hall problem is therefore exact, and the only root-reversal cycle is a two-state involution paid by one finite fibre ticket.

## Exact companion records

Fix one ordered channel pair and one nonfixed rational fibre

$$
\{c,c^\dagger\},
\qquad
c^\dagger=\tau_r(c),
\qquad
F_r(c)=F_r(c^\dagger)=g.
$$

For a represented base column `x`, write

$$
E_x=\{P_x,P_{gx}\}
$$

for the current fixed edge,

$$
T_x^c=E_x\cup\{B_{cx}\}
$$

for the paid original current factor, and

$$
T_x^{c^\dagger}=E_x\cup\{B_{c^\dagger x}\}
$$

for its same-base companion. A **companion record** is indexed by the exact base `x` after all duplicate occurrences with that base and profile have been aggregated. It retains its paid weight `w_x`, original factor `T_x^c`, desired companion anchor `B_{c^\dagger x}`, and all carry and quotient decorations.

## AC3dn -- private current-factor eligibility -- PROVED

For one exact oriented fibre, the map

$$
\boxed{
 j_x\longmapsto \pi_x=T_x^c
}
$$

from companion records to original current factors is injective. The map

$$
\boxed{
 j_x\longmapsto \widehat B_x=B_{c^\dagger x}
}
$$

from records to desired companion anchors is also injective.

Consequently every companion record has a private current-defect resource: its original factor `T_x^c`. No two distinct records in the exact oriented fibre use the same private resource or request the same companion cell.

### Proof

The column of `P_x` is exactly `x`, so the current factor `T_x^c` determines `x`. Hence equal original factors imply equal bases and equal aggregated records. Since `c^dagger` is nonzero, equality `c^dagger x=c^dagger y` also implies `x=y`, proving injectivity of the desired-anchor map. QED.

## AC3do -- exact capacitated Hall payment -- PROVED

Let `J` be any finite family of exact companion records. Let

$$
\mathcal P=\{\pi_x:x\in J\}
$$

be their private original-factor resources, each with capacity one, and give record `j_x` the eligibility set

$$
A_{j_x}=\{\pi_x\}.
$$

Then every subfamily `X subseteq J` satisfies the capacitated Hall identity

$$
\boxed{
|X|
=
\sum_{\pi\in\bigcup_{j\in X}A_j}c_\pi.
}
$$

Therefore AC3f gives a unique charge map, namely `j_x -> pi_x`, and the total number of companion reopenings paid by this exact record family is at most

$$
\boxed{|\mathcal P|=|J|.}
$$

The same conclusion holds with an integer multiplicity capacity attached to an aggregated current factor: split the capacity into distinguishable copies before applying AC3f.

### Proof

AC3dn makes the singleton eligibility sets pairwise disjoint. Their union over `X` therefore contains exactly `|X|` capacity-one resources. This is the displayed Hall identity, and AC3f supplies the charge map and total ticket bound. QED.

## AC3dp -- exact two-state companion involution -- PROVED

At one fixed base `x`, companion formation is an involution:

$$
\boxed{
(T_x^c)^\dagger=T_x^{c^\dagger},
\qquad
(T_x^{c^\dagger})^\dagger=T_x^c.
}
$$

If `c != c^dagger`, the root-choice transition graph at that base has exactly two vertices and two opposite directed edges. If `c=c^dagger`, it has one vertex and no genuine root-change transition.

Give every unordered nonfixed fibre/base pair

$$
\sigma_x=\{T_x^c,T_x^{c^\dagger}\}
$$

one reuse ticket of capacity one. Then a root-change transition may occur at most once at that base. In particular, the two-cycle cannot occur in the unticketed transition graph, and repeated off-family companion returns at one base are finite-ticket reopenings in the sense of AC3b--AC3e.

### Proof

The rational map `tau_r` is an involution, so applying it twice returns the original root. Thus the only possible root-choice graph is the stated one- or two-vertex graph. Traversing both directions of the nonfixed two-cycle requires two root-change transitions. A capacity-one ticket allows at most one, so no directed cycle remains after ticket accounting. QED.

## AC3dq -- scoped conflict and paid-bank router -- PROVED

Let an absent-anchor companion family have total paid weight

$$
W=\sum_x w_x.
$$

Build the scope-complete AC3v conflict graph on its one-cell completion objects. Every edge must include row/column or replacement overlap, private paid-set overlap, nonadditive potential terms, feasibility constraints, protected-bank conflicts, and opposite-layer conflicts.

Because the private resources from AC3dn are distinct, payment is additive on every independent set. For every real `K>=1`, AC2c gives one of:

1. **Paid scoped overload:** one object `j_x` has closed-neighbourhood paid load
   $$
   \boxed{L(j_x)>K w_x.}
   $$
   AC2d localizes this overload to one finite arithmetic conflict label.
2. **Paid compatible companion bank:** an independent family `I` has
   $$
   \boxed{
   \sum_{j_x\in I}w_x\ge W/K.
   }
   $$
   Its private original-factor resources are disjoint, its desired companion anchors are distinct, and AC3v makes all scoped collateral and payment additive.

Combining this with AC3de, if an unmatched exact fibre/root/profile class has weight `U` and the absent-anchor case is selected, then before any additional full-conflict loss there is a row-column-disjoint family of weight at least `U/51`; applying the scoped router gives either a labelled paid overload or a fully compatible privately paid bank of weight at least

$$
\boxed{
\frac{U}{51K}.
}
$$

### Proof

AC3dn--AC3do provide pairwise private payment. AC3v defines the complete conflict relation and proves exact additivity on independent sets. Apply AC2c to the weighted conflict graph. The final constant composes the `U/51` bound of AC3de with the `1/K` compatible extraction. QED.

## Consequence for the AC3 ticket ledger

The missing-companion route no longer has an abstract payment obligation.

- Carry-defect companions enter the finite carry-signature ledger.
- Off-family current companions use one capacity-one unordered-fibre ticket per base; their only raw root cycle is broken.
- Absent-anchor completions have a unique private current-factor charge and enter a scope-complete paid-bank-or-labelled-overload router.

What remains is the actual improvement/collateral comparison for a compatible one-cell completion bank and the arithmetic classification of any dense labelled overload. Neither payment eligibility nor companion-root recycling remains open.

## Finite check

`scripts/verify_ac_ri_companion_payment.py` enumerates rational fibres over small primes, checks companion involution, injectivity of original-factor and desired-anchor maps, every capacitated Hall subfamily, capacity-one cycle breaking, and the weighted AC2c compatible-bank constants on small conflict graphs.
