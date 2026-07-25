# Midpoint exclusion for RI companion rectangles

**Branch:** `research/alternating-core-chain`

AC3et shows that the opposite diagonal of a companion-anchor rectangle can form an internal replacement triple with the fixed edge only if one fixed-edge point is the exact midpoint of the two anchors. The rational fibre equation rules out both midpoint possibilities for every nontrivial fixed edge. Thus the companion rectangle decoder destroys all four internal current triples and creates no internal triple on its four support cells.

## Fibre quadratic

For one rational fibre, the two roots `c,c^dagger` have common image `g` and satisfy

$$
rg=c(1+g-c),
$$

$$
rg=c^\dagger(1+g-c^\dagger).
$$

Equivalently, they are the two roots of

$$
X^2-(1+g)X+rg=0.
$$

## AC3ez -- fixed-edge midpoint exclusion -- PROVED

For a nontrivial fixed edge, `g!=1`. The fibre roots satisfy

$$
\boxed{c+c^\dagger=1+g.}
$$

Neither fixed-edge cell can be the exact midpoint of the two companion anchors:

$$
\boxed{2P_x\ne B_{cx}+B_{c^\dagger x},}
$$

$$
\boxed{2P_{gx}\ne B_{cx}+B_{c^\dagger x}.}
$$

Consequently, with `C,D` the opposite rectangle diagonal from AC3et,

$$
\boxed{
\{P_x,C,D\}
\text{ and }
\{P_{gx},C,D\}
\text{ are both noncollinear}.
}
$$

The final four-cell support

$$
\{P_x,P_{gx},C,D\}
$$

contains no collinear triple at all.

### Proof

Vieta's formula for the displayed quadratic gives `c+c^dagger=1+g` in `F_p`.

Suppose first that `P_x` were the exact physical midpoint of the two anchors. Reducing the column-coordinate equality modulo `p` gives

$$
2x=(c+c^\dagger)x.
$$

Since `x!=0`, this implies

$$
2=c+c^\dagger=1+g,
$$

hence `g=1`, contradiction.

If `P_{gx}` were the midpoint, reduction of the column equality gives

$$
2gx=(c+c^\dagger)x=(1+g)x.
$$

Again `x!=0`, so `2g=1+g` and `g=1`, contradiction.

AC3et proves that a point on the old companion line is collinear with `C,D` exactly when it is the rectangle midpoint. Therefore neither fixed-edge point forms a triple with `C,D`. The other two possible three-subsets contain both fixed-edge points and one of `C,D`; they are noncollinear because `C,D` do not lie on the old companion line. QED.

## Consequence for AC3ev--AC3ex

The midpoint label in the first formulation of AC3et is empty for actual rational companion fibres.

- A direct off-family rectangle switch destroys all four old internal triples and creates zero internal support triples.
- An absent-anchor install-and-decode transition has the same internal conclusion after the intermediate companion is installed.
- The two-cross collateral class is therefore an external exact secant profile only; its third cell lies outside the four-cell companion support.

The remaining rectangle collateral profiles are external context stars, external cross-pair secants, blocker-repair profiles, installation-closure profiles, and their mixed stage masks.

## Finite check

`scripts/verify_ac_ri_companion_midpoint_exclusion.py` enumerates odd primes, nonzero parameters `r,g,c`, all nonfixed two-root fibres, checks the fibre quadratic and Vieta identity, and verifies that neither midpoint congruence can occur when `g!=1`.