# Rank-one active collateral in the completion-toggle bank

**Branch:** `research/rational-inverse-expansion`

RI5s toggles closed completion components independently. RI5u returns a rank-one active term when the global comparison fails. This note shows that such a term is one-sided and component-local, and then uses the target hyperbola to reduce its geometric rank from three to at most two.

## Toggle notation

Let `C` be the current active matching. For each selected completion component `K_i`, let `C_i` and `D_i` be its current and target states. A toggle vector `ε` chooses `D_i` when `ε_i=1` and `C_i` when `ε_i=0`.

A compatible active collateral triple has rank `r(T)` equal to the number of component bits it prescribes. A triple is called new when it is not already contained in the global current matching `C`.

## RI5v -- one-sided rank-one decomposition -- PROVED

Let `T` be a new compatible active triple with `r(T)=1`. Then its unique prescribed component bit is the target value `1`, never the current value `0`.

Consequently every new rank-one triple has one unique controlling component. Let `R_i` denote the total weight of the new rank-one triples controlled by component `i`. Then

$$
A_1 = (1/2) sum_i R_i.
$$

More strongly, for every deterministic subset `S` of components toggled to their target states, the total rank-one active collateral is exactly

$$
sum_{i in S} R_i.
$$

Suppose the paid certificates assigned to component `i` have total weight `W_i`, and each is absent whenever component `i` is in its target state. Toggling `S` therefore destroys paid weight at least

$$
sum_{i in S} W_i,
$$

so its guaranteed paid-minus-rank-one margin is at least

$$
sum_{i in S} (W_i-R_i).
$$

### Proof

If the unique prescribed bit were `0`, every cell of `T` in that component would belong to its current state. Every other component is unprescribed, so all cells of `T` there belong to both its current and target states. Cells outside the selected components are fixed current cells. Hence all three cells of `T` would already belong to `C`, contradicting newness.

Thus every new rank-one triple occurs exactly when its unique controlling component is toggled to `1`. The triples partition by that component, proving the exact subset formula and the uniform identity for `A_1`. The paid bound follows from the assignment rule. QED.

## RI5w -- hyperbola rank at most two -- PROVED

In the RI5 application, the target cells lie on the nondegenerate affine hyperbola

$$
H_a = {(x,a/x): x in F_p^*},
$$

with `a` nonzero. Every affine line contains at most two points of `H_a`.

Therefore a new rank-one collateral triple contains at most two target-hyperbola cells. In particular, it contains at most two target-exclusive cells of its controlling component. There is no rank-three local target channel.

### Proof

A vertical line meets `H_a` in at most one point. A nonvertical line has equation `R=mX+b`. Its intersections with `H_a` satisfy

$$
mX^2+bX-a=0.
$$

This polynomial has degree at most two and is not identically zero because `a` is nonzero. Hence there are at most two intersections. QED.

## Exact one-target and two-target channels

Split the component-local rank-one triples according to the number `s` of target-exclusive cells in the controlling component. By RI5w, `s` is `1` or `2`.

### One-target channel

A triple consists of one controlling target cell and two context cells. The context pair determines one affine line, and that line contains at most two target-hyperbola points. Thus one fixed context pair can charge at most two target columns across the entire completion family.

### Two-target channel

Let the two controlling target cells be

$$
Q_x=(x,a/x),\qquad Q_y=(y,a/y),\qquad x\ne y.
$$

Their secant line has the exact equation

$$
xy R + a X = a(x+y).
$$

The line determines the unordered pair `{x,y}` uniquely: its intersections with `H_a` are the roots of

$$
Z^2-(x+y)Z+xy=0.
$$

Hence an exact two-target secant identifies the target pair and therefore its controlling completion component.

## RI5x -- rank-one profile router -- PROVED

Let

$$
R = sum_i R_i = 2A_1.
$$

Let `σ` be any finite profile map on the component-local rank-one triples, with `L` profile values. Include in the profile the component type, quotient label, physical scale, carry word, and any desired finite incidence decoration.

After splitting by local target rank `s in {1,2}` and by `σ`, one class has raw weight at least

$$
R/(2L)=A_1/L.
$$

If the RI5u rank-one outcome satisfies

$$
A_1 >= (W/2-F)/4,
$$

then one exact rank/profile class has weight at least

$$
(W/2-F)/(4L).
$$

The selected class has one of two rigid forms.

1. A one-target class with context-pair multiplicity at most two.
2. A two-target class of exact hyperbola secants, each encoded by `(x+y,xy)` and attached to one controlling component.

There is also a component-ratio router. For any real `ρ>0`, let `B_ρ` be the components with `R_i>ρW_i`. Then

$$
sum_{i in B_ρ} R_i >= R-ρW.
$$

If every bad component carries collateral at most `β`, at least

$$
ceil((R-ρW)/β)
$$

bad components are present whenever `R>ρW`.

### Proof

The local target-rank and finite profile values partition the rank-one triples into at most `2L` classes, proving the first bounds.

For the ratio router, components outside `B_ρ` contribute at most `ρW_i` each. Their total collateral is at most `ρW`. Removing them from `R` leaves at least `R-ρW` collateral on `B_ρ`. The cardinality conclusion is averaging under the cap `β`. QED.

## Interface to RI6

The RI5u rank-one alternative is no longer an arbitrary active-layer profile.

- It is one-sided: every certificate is switched on by one target component.
- Its cost is exactly additive over deterministic component subsets.
- Hyperbola geometry eliminates local target rank three.
- One-target certificates have context-pair multiplicity at most two.
- Two-target certificates are exact secants determined by their sum/product address.
- Failure either concentrates on one poor paid/collateral component ratio or spreads over quantitatively many components.

The next active-layer work is to compare these component-local costs with their paid weights using quotient and scale labels, then pass only rank-two and rank-three interactions to the general finite-profile machinery.

## Finite check

`scripts/verify_rational_rank_one_active.py` exhausts small finite fields, target hyperbolas, row-preserving cycle switches, and nontrivial fixed outside matching states. It verifies one-sided rank-one newness, exact subset additivity, the two-intersection bound, one-context-pair multiplicity, the secant equation and uniqueness, and the profile/component routers.