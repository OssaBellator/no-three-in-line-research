# Closed physical installation of an orbit-phase fixed edge

**Branch:** `research/orbit-phase-expansion`

OP4p--OP4s produce a paid coherent physical rational-inverse fixed-edge class. The paid roots are already current hyperbola cells, so they are not moved by the RI5 completion. The correct installation closes the entire physical completion debt once and substitutes every I6 state through the same closure.

## OP4t -- paid roots are completion-fixed -- PROVED

Let

\[
P_x=(x,a/x),\qquad P_u=(u,a/u)
\]

be the two same-channel cells of a current paid OP factor, and let `M_0` be the current active permutation. On the selected physical source block `X`, let

\[
T_X=\{(v,a/v):v\in X\}
\]

and define the RI5f relative completion map

\[
\sigma(v)=M_0^{-1}(a/v).
\]

Then

\[
\boxed{\sigma(x)=x,\qquad \sigma(u)=u.}
\]

### Proof

The factor is current, so `M_0(x)=a/x` and `M_0(u)=a/u`. The unique current column occupying row `a/x` is therefore `x`, and similarly for `u`. QED.

Thus OP4s payment is fixed-edge payment, not payment assigned to nontrivial completion components.

## Common completion closure

Decompose the partial map `sigma` on `X` into cycles and boundary paths. For each boundary path

\[
v_1\to v_2\to\cdots\to v_k\to y,
\qquad y\notin X,
\]

add the closure cell

\[
q_P=(y,M_0(v_1)).
\]

Let `Y` be the outside endpoint columns and `Q` the set of closure cells. Then `T_X union Q` is a matching on exactly the rows and columns used by `M_0` on `X union Y`.

## OP4u -- every I6 state uses the same closure -- PROVED

Write

\[
X=\bigcup_{\alpha=1}^{m}U_\alpha H,
\qquad 1\le m\le4,
\]

and let `J_{pi,t}` be any I6 state on `X`. Since every I6 state uses the column set `X` and row set `aX^{-1}`, define

\[
D_{\pi,t}=J_{\pi,t}\cup Q.
\]

Every `D_{pi,t}` is a permutation matching on exactly the same rows and columns as the current active matching on `X union Y`. Outside that set retain `M_0`.

### Proof

The closure `Q` supplies precisely the outside endpoint columns and the rows released at the starts of the boundary paths. Replacing `T_X` by any matching with the same columns and rows leaves the closed row and column sets unchanged. Every I6 state has those same local sets. QED.

## OP4v -- exact I6 source-coset cylinder law -- PROVED

For a compatible active collateral triple, let `r(T)` be the number of distinct source cosets whose I6 image and subgroup shift are prescribed. Several cells inside one source coset contribute rank one because they require one common image coset and shift. Then

\[
1\le r(T)\le3,
\qquad
\boxed{
\Pr(T)=\frac1{(m)_{r(T)}h^{r(T)}}.
}
\]

Incompatible prescriptions have probability zero.

### Proof

The I6 bank contains `m!h^m` states. Prescribing `r` distinct source-coset images and shifts leaves `(m-r)!h^{m-r}` states. Divide. QED.

## Opposite-layer repair

For each lifted state let `B_{pi,t}=D_{pi,t} intersect M_1`, where `M_1` is the current blocker permutation. Use the exact RI5h--RI5m menu: no move for zero blocked desired cells, an auxiliary transposition for one, and a derangement for at least two. Every joint state is legal.

## OP4w -- closed fixed-edge collateral criterion -- PROVED

Let `W` be the factor-conservative paid weight of one OP4s coherent fixed-edge class. Choose an I6 state uniformly and then choose its blocker repair uniformly from the conditional menu. Every paid fixed-edge object is neutralized with probability at least

\[
1-\frac1{mh}.
\]

Move state-independent collateral into `F`. For active collateral define

\[
C_r=\sum_{T:r(T)=r}\frac{w(T)}{(m)_rh^r},
\qquad 1\le r\le3,
\]

and let `B` be the exact conditional blocker collateral. If

\[
\boxed{
\left(1-\frac1{mh}\right)W>F+C_1+C_2+C_3+B,
}
\]

then one closed physical I6 state strictly lowers the paid potential.

### Proof

OP4u gives a valid active matching for every I6 state. OP4v gives the exact active cylinder probabilities, and RI5h--RI5m give legal blocker repair. The left side is the expected paid destruction and the right side is the complete expected collateral. A strict negative expected drift yields one improving state. QED.

## OP4x -- failed installation router -- PROVED

Assume

\[
G=\left(1-\frac1{mh}\right)W-F>0
\]

but the OP4w criterion fails. Then one of

\[
C_1,\ C_2,\ C_3,\ B
\]

is at least `G/4`. Thus a coherent OP4s class either installs and improves or returns one exact source-coset-rank-one, rank-two, rank-three or blocker-repair obstruction in the actual closed physical bank.

### Proof

The four nonnegative variable terms sum to at least `G`; apply pigeonhole. QED.

## Consequence for OP5

The first OP frontier is now closed at the installation level:

- physical roots and scales are reconstructed;
- paid roots are fixed by completion;
- every I6 state lifts through one common closure;
- every blocker occupancy is repairable;
- active collateral has exact source-coset-rank probabilities.

The remaining work is classification or absorption of the named `F,C_1,C_2,C_3,B` outputs, together with the incomplete-fibre, root-imbalance and scale-dispersion alternatives from OP4s.

## Finite check

`scripts/verify_phase_closed_fixed_edge.py` exhausts small current permutations, partial target matchings and completion closures, checks fixed roots and common closure preservation, enumerates small I6 banks and verifies the exact source-coset cylinder law.
