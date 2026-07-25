# Closed-completion fixed-edge bank for canonical RI payment

**Branch:** `research/alternating-core-chain`

The canonical OP-to-RI records in AC3ay carry paid current factors whose two same-channel cells are actual hyperbola cells. This exposes a correction to the first formulation of completion faithfulness: those paid factors cannot be charged to completion components, because their root cells are already equal to the proposed hyperbola target. The correct construction closes the physical completion debt and then replaces the completed hyperbola block by the full I6 fixed-edge bank in one joint state.

## AC3bf -- canonical paid roots are completion-fixed -- PROVED

Let

$$
P_x=(x,a/x),
\qquad
P_u=(u,a/u)
$$

be the two same-channel cells of one current paid OP4g factor, and let `M_0` be the current active permutation matching. Since the factor is current,

$$
M_0(x)=a/x,
\qquad
M_0(u)=a/u.
$$

Let `X` be the physical source block selected by the coherent RI scale class and let

$$
T_X=\{(v,a/v):v\in X\}
$$

be its target hyperbola matching. For the RI5f completion map

$$
\sigma(v)=M_0^{-1}(a/v),
$$

we have

$$
\boxed{\sigma(x)=x,\qquad \sigma(u)=u.}
$$

Thus both paid root cells are fixed one-cycles of the relative completion map. No nontrivial completion component can certify destruction of the paid factor by moving either root cell.

### Proof

The target row at column `x` is `a/x=M_0(x)`. The unique current column occupying that row is therefore `x`, so `σ(x)=x`. The same argument applies to `u`. QED.

This does not invalidate the coherent-scale payment. It identifies its correct role: the paid factors are fixed-edge payment for the I6 bank, not payment for installing the missing columns of the physical block.

## Closed physical completion

Apply RI5f to the entire physical block `X`. Every internal component is retained. For every boundary path

$$
v_1\to v_2\to\cdots\to v_k\to y,
\qquad y\notin X,
$$

adjoin the RI5h closure cell

$$
q_P=(y,M_0(v_1)).
$$

Let `Y` be the set of distinct outside endpoint columns and let `Q` be the set of closure cells. The completed hyperbola state

$$
D_0=T_X\cup Q
$$

is a matching on the same rows and columns as `M_0` restricted to `X∪Y`.

The paid fixed roots from AC3bf lie in `T_X`; they need not be assigned to the nontrivial completion components.

## AC3bg -- every I6 state lifts through the same completion closure -- PROVED

Let

$$
X=\bigcup_{\alpha=1}^m U_\alpha H,
\qquad 1\le m\le4,
$$

and let `J_{π,t}` be any I6 state on `X` from RI5a. Every `J_{π,t}` uses exactly the column set `X` and exactly the row set

$$
aX^{-1}.
$$

Define

$$
D_{\pi,t}=J_{\pi,t}\cup Q.
$$

Then every `D_{π,t}` is a permutation matching on exactly the same rows and columns as the current active matching on `X∪Y`. Outside `X∪Y`, retain `M_0`.

### Proof

RI5a gives the same columns and rows for every I6 state as for `T_X`. The closure set `Q` is disjoint from `X`, and `T_X∪Q` already has the current row and column sets on `X∪Y`. Replacing `T_X` by `J_{π,t}` therefore preserves those sets. QED.

Hence physical completion and the fixed-edge absorber do not need two sequential active-layer moves. The I6 state is installed directly through the common closure.

## Opposite-layer repair

Let `M_1` be the blocker permutation. For each lifted state `D_{π,t}`, put

$$
B_{\pi,t}=D_{\pi,t}\cap M_1.
$$

Use the exact RI5h--RI5m occupancy menu:

1. no blocked desired cell: leave `M_1` unchanged;
2. at least two blocked desired cells: use a fixed-point-free blocker replacement;
3. exactly one blocked desired cell: use one auxiliary blocker transposition.

Every resulting pair of active and blocker layers is legal. Thus blocker occupancy is not an additional hypothesis of the closed fixed-edge bank.

## AC3bh -- exact closed fixed-edge collateral criterion -- PROVED FROM RI5a--RI5m

Let `W` be the factor-conservative paid weight on one coherent physical fixed edge. Choose an I6 state uniformly and then choose uniformly from its conditional blocker-repair menu.

Every paid fixed-edge object is neutralized with probability at least

$$
1-\frac1{mh}.
$$

Move every state-independent contribution into `F`. For active-layer collateral, let `C_r` be the total expected weight of compatible prescriptions using exactly `r` distinct I6 source cosets and `r` distinct target row cosets, where

$$
C_r=
\sum_{T:\,r(T)=r}
\frac{w(T)}{(m)_r h^r},
\qquad 1\le r\le3.
$$

Repeated-coset prescriptions are evaluated with their actual I6 correlation and placed in `F` or in an exact separate profile; they are not assigned the distinct-coset formula.

Let `B` be the exact conditional expected blocker collateral over the zero, singleton, and multiple-blocker menus. If

$$
\boxed{
\left(1-\frac1{mh}\right)W
>
F+C_1+C_2+C_3+B,
}
$$

then one closed-completion I6 state strictly lowers the paid potential.

### Proof

AC3bg makes every I6 state an active matching with the correct global row and column sets. RI5a gives the paid survival and compatible-cylinder probabilities. RI5h--RI5m give a legal blocker repair for every active state and define the exact conditional blocker expectation. The displayed strict inequality makes the expected net drift negative, so one joint state improves. QED.

## AC3bi -- failed closed fixed-edge router -- PROVED

Assume

$$
\left(1-\frac1{mh}\right)W>F
$$

but the AC3bh criterion fails. Then at least one of

$$
C_1,\quad C_2,\quad C_3,\quad B
$$

is at least

$$
\boxed{
\frac{(1-1/(mh))W-F}{4}.
}
$$

Thus failure returns one named active rank-one, rank-two, rank-three, or blocker-repair profile in the actual closed physical bank.

### Proof

Failure gives

$$
C_1+C_2+C_3+B
\ge
\left(1-\frac1{mh}\right)W-F.
$$

Pigeonhole among the four nonnegative terms. QED.

## AC3bj -- corrected canonical OP-to-RI composition -- PROVED UNDER HYPOTHESES

Retain the AC3be notation. Unless the incomplete-fibre, one-root imbalance, or scale-dispersion outputs occur, one coherent decorated fixed-edge class has paid weight at least

$$
W_{edge}
\ge
\frac{W_x}{16R_0\rho P K L}.
$$

Assume only that:

1. the selected physical source block is closed using its actual RI5f boundary paths;
2. all active and blocker collateral events are retained in the exact AC3bh audit.

No completion-faithful assignment of `W_edge` to target columns is required. AC3bf shows such an assignment would be conceptually wrong for canonical paid roots. Instead AC3bg--AC3bi give either an improving closed I6 state or a named active/blocker profile with gain scale

$$
\left(1-\frac1{mh}\right)
\frac{W_x}{16R_0\rho P K L}.
$$

The remaining geometry is classification of the four failed-bank terms and payment of any state-independent closure collateral in `F`.

## Corrected frontier

For canonical OP quotient roles:

- normalized RI arithmetic is complete;
- common-scale paid pairing is complete;
- physical completion can be closed for every I6 state;
- blocker occupancy is always repairable;
- support is exact when the full active and blocker candidate families are retained.

The remaining RI obstruction is now the size and arithmetic structure of `F`, `C_1`, `C_2`, `C_3`, or `B`, together with the explicit incomplete-fibre, root-imbalance, and scale-dispersion outputs. It is not a target-column payment matching problem.

## Finite check

`scripts/verify_ac_ri_closed_fixed_edge.py` exhausts small cyclic quotient models, current/target completion systems, lifted I6 states, fixed-root identities, common closure preservation, compatible cylinder counts, and the four-way failed-bank router.
