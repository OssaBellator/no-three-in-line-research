# Created-cell rank router for executable AC banks

**Branch:** `research/alternating-core-chain`

The executable clean-pair, missing-support, companion-rectangle and coherent multiscale banks currently return collateral through stage masks or source-specific expectation terms. Those labels are useful for bookkeeping but are not the smallest invariant. Relative to the fixed pre-transition two-layer configuration, every genuinely created triple contains exactly one, two or three cells which were absent before the transition. This note introduces that exact rank, proves a universal three-term failed-bank router, and localizes each rank to one finite literal-role word for every bounded local decoder used in the current AC chain.

## Pre-transition new-cell rank

Let `M` be the union of the two permutation layers before a legal local or product transition. For any cell triple `C`, define

$$
\operatorname{nrk}_M(C)=|C\setminus M|.
$$

A triple is **created** when it is present after the transition but was not present before it.

## AC3fa -- exact created-cell rank split -- PROVED

Every created triple has

$$
\boxed{
\operatorname{nrk}_M(C)\in\{1,2,3\}.
}
$$

For a finite transition bank with any probability distribution on legal states, let `N_k` be the exact expected total weight of created triples with new-cell rank `k`. Then

$$
\boxed{
\mathbb E[\text{created collateral}]=N_1+N_2+N_3.
}
$$

If the expected destroyed certified payment is `D` and no bank state improves the paid triple potential, then

$$
N_1+N_2+N_3\ge D,
$$

so one exact rank satisfies

$$
\boxed{N_k\ge D/3.}
$$

### Proof

A created triple is not a subset of `M`, so it contains at least one cell outside `M`; it has only three cells, so the rank is at most three. The three rank classes are disjoint and exhaustive, giving the expectation identity. If expected created collateral were smaller than expected destroyed payment, some legal state would have negative potential drift. Failure of improvement therefore gives the sum bound, and weighted pigeonhole gives `D/3`. QED.

The rank is independent of which local menu state creates the triple: membership in the fixed initial set `M` is fixed once the triple address is fixed.

## Geometric meaning of the three ranks

The rank classes retain exact current context.

1. `k=1`: one new cell and two cells already in `M`. This is one exact current-pair completion literal.
2. `k=2`: two new cells and one cell already in `M`. This is one exact current-centred secant or two-arm context.
3. `k=3`: all three cells are new. This is one exact rank-three new-cell tuple.

Thus the three classes enter the existing AC literal-star, pair/secant and rank-three routers without inventing another terminal object. Layer, stage, anchor, denominator, scale, blocker and carry fields remain attached to every occurrence.

## Finite literal roles

Fix one exact local transition profile. Give every cell which can be new in some local menu state a **literal role** containing its layer, stage and position inside the normalized local envelope. Auxiliary blocker cells retain their exact physical address but use one generic auxiliary-source or auxiliary-target role.

Let `Lambda` be the finite role alphabet and put

$$
\ell=|\Lambda|.
$$

For a created triple of rank `k`, forget the exact physical addresses temporarily and retain only the multiset of its `k` new-cell roles. Repetition is allowed because the same role may occur in different disjoint envelopes.

## AC3fb -- finite role-word localization -- PROVED

For rank `k`, the number of possible role multisets is at most

$$
\boxed{
M(\ell,k)=\binom{\ell+k-1}{k}.
}
$$

Consequently, if a rank-`k` class has expected weight `N_k`, one exact role multiset has expected weight at least

$$
\boxed{
\frac{N_k}{\binom{\ell+k-1}{k}}.
}
$$

Combined with AC3fa, a failed bank returns one exact created-cell rank and one exact literal-role multiset of weight at least

$$
\boxed{
\frac{D}{3\binom{\ell+k-1}{k}}.
}
$$

The selected profile still retains the exact addresses of all represented envelopes; only the finite local position word has been pigeonholed.

### Proof

A rank-`k` triple contributes a multiset of size `k` from `ell` role labels. The standard stars-and-bars count is `binom(ell+k-1,k)`. Weighted pigeonhole proves the bounds. QED.

## AC3fc -- current decoder role alphabets -- PROVED

The executable banks already constructed in the AC chain admit the following uniform alphabets.

### Clean BDA pair: `ell_clean <= 10`

The union of all BDA5e menu states uses at most:

- four active opposite-diagonal roles `C_u,D_u,C_v,D_v`;
- four blocker roles at old active endpoints in full phase flips;
- two blocker replacement roles in the coupled two-single-blocker derangement.

Hence

$$
\boxed{\ell_{\rm clean}\le10.}
$$

### Missing BDA support: `ell_miss <= 34`

The install-then-decode composite uses at most:

- four active completion roles: two partner targets and two closure cells;
- twenty first blocker-repair roles: twelve ordered nonfixed replacements among four selected roles and eight singleton-auxiliary roles;
- ten BDA decoder roles from the clean-pair alphabet.

Hence

$$
\boxed{\ell_{\rm miss}\le34.}
$$

### Direct RI companion rectangle: `ell_dir <= 8`

There are two new active rectangle roles `C,D` and at most six blocker-repair roles on those two targets: two mutual replacements and four singleton-auxiliary roles. Thus

$$
\boxed{\ell_{\rm dir}\le8.}
$$

### Absent-anchor RI companion composite: `ell_abs <= 16`

There are two installation roles `Z,Q`, six first blocker-repair roles, two final rectangle roles `C,D`, and six second blocker-repair roles. The two repair stages are distinguished. Thus

$$
\boxed{\ell_{\rm abs}\le16.}
$$

### Proof

Each list is the union of normalized cell positions over the finite local menus proved in AC3eq--AC3er, BDA5a--BDA5e and AC3eu--AC3ew. A fixed-point-free repair among at most four selected completion cells has at most `4*3=12` ordered selected-to-selected roles. A singleton auxiliary transposition has two orientations for each selected role, giving at most eight. On a two-cell repair set the corresponding bounds are two mutual roles and four auxiliary roles. QED.

For reference, the rank-one, rank-two and rank-three multiset counts are:

| Bank | `ell` | `M(ell,1)` | `M(ell,2)` | `M(ell,3)` |
|---|---:|---:|---:|---:|
| Direct companion rectangle | 8 | 8 | 36 | 120 |
| Clean BDA pair | 10 | 10 | 55 | 220 |
| Absent companion composite | 16 | 16 | 136 | 816 |
| Missing BDA support | 34 | 34 | 595 | 7140 |

## AC3fd -- improved failed-bank returns -- PROVED

The universal rank split sharpens the current stage-mask constants before optional role-word localization.

### Clean BDA pairs

AC3em and AC3eg give executable paid weight at least

$$
\frac{W_x}{32KR\rho L}
$$

from an endpoint-origin clean class and

$$
\frac{W_x}{64KR\rho L}
$$

from an oriented-variation clean class. If no product state improves, AC3fa returns one created-cell rank of weight at least

$$
\boxed{
\frac{W_x}{96KR\rho L}
}
$$

or

$$
\boxed{
\frac{W_x}{192KR\rho L},
}
$$

respectively. These supersede the coarser four-term constants `1/128` and `1/256` when only a finite executable collateral output is required.

### Missing BDA supports

The same source and conflict bounds apply to AC3ee--AC3es. A failed install-then-decode bank returns one created-cell rank of weight at least

$$
\boxed{
\frac{W_x}{96KR\rho L}
}
$$

from an endpoint front or

$$
\boxed{
\frac{W_x}{192KR\rho L}
}
$$

from an oriented variation front. These supersede the seven-mask constants `1/224` and `1/448` for coarse rank routing. The seven masks remain available as additional stage decorations.

### RI companion rectangles

A direct off-family decoder bank of paid class weight `V` returns one created-cell rank of weight at least

$$
\boxed{\frac{V}{93K}.}
$$

If it came from unmatched weight `U` with `V>=U/3`, this is

$$
\boxed{\frac{U}{279K}.}
$$

For an absent-anchor class extracted from unmatched weight `U`, AC3dq and AC3ew give executable payment at least `U/(51K)`. A failed composite therefore returns one created-cell rank of weight at least

$$
\boxed{\frac{U}{153K},}
$$

improving the seven-mask constant `U/(357K)`.

### Coherent multiscale RI banks

AC3dz retains paid scale weight at least `W/(31K)`, and every nontrivial closed I6 bank destroys expected certified weight at least half of its scale weight. Hence a failed multiscale product has one created-cell rank of expected weight at least

$$
\boxed{\frac{W}{186K}.}
$$

This is an alternative coarse return to the finer five-way `F,C1,C2,C3,B` split of AC3eb. The latter remains available when source-layer or blocker-layer geometry is needed.

### Proof

Apply AC3fa to the executable-bank lower bounds already proved in AC3em, AC3ee, AC3ev, AC3ex and AC3dz. For the multiscale case, expected destroyed payment is at least half of `W/(31K)`. All constants are direct multiplication by `1/3`. QED.

## Consequence

The new finite collateral outputs are no longer merely seven stage masks or four/five source terms.

- Every failed executable bank returns rank one, two or three relative to the fixed pre-transition configuration.
- Rank one is a current-pair completion literal.
- Rank two is a current-centred secant/two-arm record.
- Rank three is an exact all-new tuple.
- Every bounded local decoder further localizes to one finite role multiset with explicit alphabet size.
- Stage masks and source/blocker labels remain attached as refinements, not terminal states.

The remaining work is termination of the resulting rank-one contexts, rank-two secants and rank-three literal tuples through the existing AC resource and arithmetic routers, together with classification of dense AC2d overload labels.

## Finite check

`scripts/verify_ac_created_cell_rank_router.py` exhausts initial subsets and triples on small universes, checks the exact rank partition, all integer failed-bank ledgers in a bounded range, the role-multiset counts, the four decoder role-alphabet bounds and every composed constant in AC3fd.
