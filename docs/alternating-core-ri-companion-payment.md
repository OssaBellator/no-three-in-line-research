# Private payment and no-recycling for RI companion outputs

**Branch:** `research/alternating-core-chain`

AC3db--AC3df reduce every incomplete rational fibre and one-root scale imbalance to a carry defect, an off-family current companion factor, or a row-column-disjoint family of one-cell companion completions. This note proves the missing payment interface for the latter two outputs. After one exact orientation and fibre are fixed, every companion record has a private original current factor. The corresponding Hall problem is therefore exact, the only root-reversal cycle is a two-state involution paid by one finite fibre ticket, and an off-family current companion produces a bounded-ratio bank of four-point current defect lines.

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

The factor retains its channel labels. Its unique `H_b` anchor is `B_{cx}`, whose column is `cx`; because `c` is nonzero, this determines `x`. Hence equal labelled original factors imply equal bases and equal aggregated records. Since `c^dagger` is nonzero, equality `c^dagger x=c^dagger y` also implies `x=y`, proving injectivity of the desired-anchor map. QED.

## AC3do -- exact capacitated Hall payment -- PROVED

Let `J` be any finite family of distinct exact companion records. Let

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

Therefore AC3f gives a unique charge map, namely `j_x -> pi_x`. Under the capacity-one ticket policy, each exact base/profile record can pay at most one reopening. A second event with the same base is immediately an explicit repeated-resource obstruction rather than another silently payable event.

The same conclusion holds with an integer multiplicity capacity attached to an aggregated current factor: split the capacity into distinguishable copies before applying AC3f.

### Proof

AC3dn makes the singleton eligibility sets pairwise disjoint. Their union over `X` therefore contains exactly `|X|` capacity-one resources. This is the displayed Hall identity, and AC3f supplies the charge map. QED.

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

## AC3dr -- off-family companions form four-point current lines -- PROVED

Assume the off-family current-companion case of AC3dc, so both `T_x^c` and `T_x^{c^dagger}` are current factors. Then

$$
\boxed{
L_x=\{P_x,P_{gx},B_{cx},B_{c^\dagger x}\}
}
$$

consists of four distinct current cells on one real affine line. Consequently all four three-element subsets of `L_x` are current collinear certificates.

### Proof

The two current factors share the two distinct points `P_x,P_{gx}`. Hence their third points lie on the same unique real line through that edge. The source points are distinct because `g!=1`; the anchors are distinct because the fibre is nonfixed; and no `H_a` cell equals an `H_b` cell because `a!=b`. Thus the four points are distinct. Every three-element subset of four points on one line is collinear. QED.

## AC3ds -- bounded support conflict of four-point lines -- PROVED

For one exact oriented fibre, the four columns of `L_x` have multipliers

$$
\mathcal M=\{1,g,c,c^\dagger\}
$$

relative to `x`. Relative to the source row `a/x`, their row multipliers are

$$
\mathcal N=\{1,g^{-1},c/g,c^\dagger/g\}.
$$

Join two distinct bases `x,y` when `L_x` and `L_y` share a row or column. Then a conflict requires

$$
\boxed{
y/x\in
\mathcal M\mathcal M^{-1}
\cup
\mathcal N\mathcal N^{-1}.
}
$$

The union has at most thirty-one elements including the identity. Therefore the support-conflict graph has maximum degree at most

$$
\boxed{30,}
$$

and contains a row-column-disjoint subfamily carrying at least `1/31` of the total weight.

### Proof

A column equality has the form `mu x=nu y`, with `mu,nu in M`, and a row equality has the same quotient form with multipliers in `N`. Each quotient set has at most sixteen elements and both contain the identity, so their union has at most thirty-one. Every nonidentity ratio determines at most one conflicting base `y` for a fixed `x`. Greedy weighted colouring gives the `1/31` class. QED.

## AC3dt -- paid off-family line-bank router -- PROVED

Let one exact off-family current-companion class have total paid weight `V`. Then AC3ds gives a row-column-disjoint family of four-point current lines carrying at least

$$
\boxed{V/31.}
$$

Complete its full conflict relation with AC3v. For every `K>=1`, either one four-point line has scoped closed-neighbourhood paid load greater than `K` times its own weight, and AC2d returns one finite conflict label, or a fully support-compatible family carries at least

$$
\boxed{V/(31K).}
$$

Every selected object retains four explicit current collinear certificates, its common fixed edge, both rational roots, base scale, and all carry data. If the off-family branch came from an unmatched class of weight `U`, then `V>=U/3`, so the compatible-bank lower bound is

$$
\boxed{U/(93K).}
$$

unless a labelled overload occurs.

### Proof

Apply AC3ds and then AC2c to the scope-complete graph. AC3v supplies exact additivity on the independent family. The final constant uses the three-way split in AC3de. QED.

## Consequence for the AC3 ticket ledger

The missing-companion route no longer has an abstract payment obligation.

- Carry-defect companions enter the finite carry-signature ledger.
- Off-family current companions use one capacity-one unordered-fibre ticket per base; their only raw root cycle is broken, and their current support amplifies to a four-point-line bank or a labelled scoped overload.
- Absent-anchor completions have a unique private current-factor charge and enter a scope-complete paid-bank-or-labelled-overload router.

What remains is the actual improvement/collateral comparison for compatible one-cell-completion and four-point-line banks, together with arithmetic classification of any dense labelled overload. Neither payment eligibility nor companion-root recycling remains open.

## Finite check

`scripts/verify_ac_ri_companion_payment.py` enumerates rational fibres over small primes, checks companion involution, injectivity of original-factor and desired-anchor maps, every capacitated Hall subfamily, four-point-line certificates, the thirty-ratio support bound, capacity-one cycle breaking, and the weighted AC2c compatible-bank constants on small conflict graphs.
