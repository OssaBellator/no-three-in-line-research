# Closed-completion fixed-edge bank for canonical RI payment

**Branch:** `research/alternating-core-chain`

The canonical OP-to-RI records in AC3ay carry paid current factors whose two same-channel cells are actual hyperbola cells. This exposes a correction to the first formulation of completion faithfulness: those paid factors cannot be charged to completion components, because their root cells already equal the proposed hyperbola target. The correct construction closes the physical completion debt and replaces the completed hyperbola block by the full I6 fixed-edge bank in one joint state.

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

The target row at column `x` is `a/x=M_0(x)`. The unique current column occupying that row is `x`, so `σ(x)=x`. The same argument applies to `u`. QED.

The coherent-scale payment remains useful as fixed-edge payment for I6; it is not completion-debt payment.

## Closed physical completion

Apply RI5f to the entire physical block `X`. For every boundary path

$$
v_1\to v_2\to\cdots\to v_k\to y,
\qquad y\notin X,
$$

adjoin the RI5h closure cell

$$
q_P=(y,M_0(v_1)).
$$

Let `Y` be the set of distinct outside endpoint columns and let `Q` be the set of closure cells. Then

$$
D_0=T_X\cup Q
$$

is a matching on the same rows and columns as `M_0` restricted to `X∪Y`.

## AC3bg -- every I6 state lifts through the same completion closure -- PROVED

Let

$$
X=\bigcup_{\alpha=1}^m U_\alpha H,
\qquad 1\le m\le4,
$$

and let `J_{π,t}` be any I6 state on `X`. Every `J_{π,t}` uses the column set `X` and row set `aX^{-1}`. Define

$$
D_{\pi,t}=J_{\pi,t}\cup Q.
$$

Every `D_{π,t}` is a permutation matching on exactly the same rows and columns as the current active matching on `X∪Y`. Outside `X∪Y`, retain `M_0`.

### Proof

Every I6 state has the same columns and rows as `T_X`. Replacing `T_X` by `J_{π,t}` in the closed matching `T_X∪Q` preserves the complete row and column sets. QED.

Hence physical completion and the fixed-edge absorber do not require sequential active-layer moves. Each I6 state is installed directly through the common closure.

## Opposite-layer repair

Let `M_1` be the blocker permutation. For each lifted state, put

$$
B_{\pi,t}=D_{\pi,t}\cap M_1.
$$

Use the exact RI5h--RI5m occupancy menu:

1. no blocked desired cell: leave `M_1` unchanged;
2. at least two: use a fixed-point-free blocker replacement;
3. exactly one: use one auxiliary blocker transposition.

Every resulting pair of active and blocker layers is legal.

## I6 prescription rank

A compatible active triple may use more than one moving cell from the same source coset. All such cells must prescribe the same target coset and the same subgroup shift; otherwise the triple is incompatible and has probability zero.

For a compatible triple `T`, let `r(T)` be the number of distinct prescribed source cosets. Their target cosets are automatically distinct because the I6 coset map is a permutation. Then

$$
1\le r(T)\le3,
$$

and the exact occurrence probability is

$$
\boxed{
\Pr(T)=\frac1{(m)_{r(T)}h^{r(T)}}.
}
$$

This includes several cells in one source coset: they impose one coset image and one common shift, so they contribute rank one.

## AC3bh -- exact closed fixed-edge collateral criterion -- PROVED FROM RI5a--RI5m

Let `W` be the factor-conservative paid weight on one coherent physical fixed edge. Choose an I6 state uniformly and then choose uniformly from its conditional blocker-repair menu.

Every paid fixed-edge object is neutralized with probability at least

$$
1-\frac1{mh}.
$$

Move every state-independent contribution into `F`. For active-layer collateral define

$$
C_r=
\sum_{T:\,r(T)=r}
\frac{w(T)}{(m)_r h^r},
\qquad 1\le r\le3,
$$

where the sum includes every compatible triple of source-coset rank `r`, including repeated cells inside one source coset. Incompatible local prescriptions contribute zero.

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

AC3bg gives the active matching. I6 prescriptions on `r` distinct source cosets fix `r` distinct coset images and `r` shifts, leaving `(m-r)!h^{m-r}` states out of `m!h^m`. RI5h--RI5m give a legal conditional blocker repair. The displayed inequality makes expected net drift negative. QED.

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

Thus failure returns one named source-coset-rank-one, rank-two, rank-three, or blocker-repair profile in the actual closed physical bank.

### Proof

Pigeonhole the four nonnegative variable terms. QED.

## AC3bj -- corrected canonical OP-to-RI composition -- PROVED UNDER HYPOTHESES

Retain the AC3be notation. Unless incomplete fibres, one-root imbalance, or scale dispersion occur, one coherent decorated fixed-edge class has paid weight

$$
W_{edge}
\ge
\frac{W_x}{16R_0\rho P K L}.
$$

Assume only that the selected physical block is closed by its actual RI5f paths and every active and blocker event is retained in the exact AC3bh audit. No completion-payment assignment is required.

AC3bg--AC3bi give either an improving closed I6 state or a named active/blocker profile at gain scale

$$
\left(1-\frac1{mh}\right)
\frac{W_x}{16R_0\rho P K L}.
$$

The remaining geometry is classification of `F,C_1,C_2,C_3,B` and the explicit scale/fibre escape outputs.

## Corrected frontier

For canonical OP quotient roles:

- normalized RI arithmetic and common-scale paid pairing are complete;
- physical completion closes every I6 state;
- blocker occupancy is always repairable;
- all compatible active prescriptions have exact source-coset-rank probabilities.

The remaining RI obstruction is the arithmetic structure of `F,C_1,C_2,C_3,B`, together with incomplete fibres, root imbalance, and scale dispersion.

## Finite check

`scripts/verify_ac_ri_closed_fixed_edge.py` exhausts small completion systems and cyclic I6 models, checks fixed roots, common closure preservation, single- and multi-cell source-coset cylinder counts, blocker repair, and the four-way failed-bank router.
