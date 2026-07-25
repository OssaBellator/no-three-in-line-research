# Finite interaction words in the shadow-free terminal core

**Branch:** `research/rational-inverse-expansion`

RI5ab produces a terminal component core with no uncharged active rank-one collateral. Every surviving uncharged active triple has filtered rank two or three. This note classifies the finite component words and then uses the target hyperbola to reduce all of them to two geometric incidence types.

## Canonical component word

Order the prescribed components of a triple by their least active column. For each prescribed component record:

- its required bit, current `0` or target `1`;
- the number of triple cells lying in that component.

For rank two, a third cell may lie outside the two prescribed components or in an unprescribed common state. Record this as a neutral cell `N`.

Every new compatible word contains at least one target bit `1`. A word with only current bits would already be present in the original current matching.

## RI5ac -- thirteen terminal interaction words -- PROVED

There are at most thirteen realizable canonical component words.

### Rank two

The required bit word is one of

$$
10,\qquad 01,\qquad 11.
$$

The local-size word is one of

$$
(1,1;N),\qquad (2,1),\qquad (1,2).
$$

The two combinations

$$
11\text{ with }(2,1),\qquad 11\text{ with }(1,2)
$$

are impossible because they would place all three cells on the target hyperbola. Therefore rank two has at most

$$
3+2+2=7
$$

realizable words.

### Rank three

Each of the three prescribed components contributes exactly one cell. The bit word is any nonzero binary word except `111`:

$$
100,010,001,110,101,011.
$$

Thus rank three has at most six realizable words.

### Proof

A prescribed component contributes at least one exclusive cell, so rank two uses either two prescribed cells plus one neutral cell or all three cells across the two components. Rank three uses exactly one cell in each component.

Newness excludes the all-current words. Every cell in a target-state component belongs to the target hyperbola. The nondegenerate hyperbola contains no collinear triple, so any word forcing three target-state cells is impossible. This removes the two rank-two `11` size-two cases and the rank-three word `111`. The remaining enumeration is exhaustive. QED.

## RI5ad -- two hyperbola interaction geometries -- PROVED

Every terminal-core active interaction contains exactly one or exactly two target-hyperbola cells.

### One-target geometry

The other two cells form a context pair. Their affine line contains at most two target-hyperbola points. Therefore one fixed context pair can support at most two possible target columns across all terminal interactions.

### Two-target geometry

The two target cells are

$$
(x,a/x),\qquad (y,a/y),\qquad x\ne y.
$$

They determine the exact secant

$$
xy R+aX=a(x+y).
$$

The secant determines the unordered pair `{x,y}` uniquely, and the third cell is a current or neutral context cell on that line.

### Proof

Every new word contains a target prescription, so at least one target cell occurs. RI5w proves that an affine line meets the target hyperbola in at most two points. The one-target multiplicity and two-target secant claims are the same line-intersection and quadratic-root identities used in RI5w. QED.

## RI5ae -- finite terminal profile router -- PROVED

Let `L` be the size of any finite arithmetic profile alphabet recording the component types, quotient labels, physical scales, carry words, blocker states, and desired incidence decorations.

Let `C_2` and `C_3` be the raw candidate weights of the terminal rank-two and rank-three active triples. Their expected contributions are

$$
H_2^*=C_2/4,\qquad H_3^*=C_3/8.
$$

After splitting by the thirteen canonical words and the `L` profile values:

- one rank-two word/profile class has raw weight at least `C_2/(7L)`;
- one rank-three word/profile class has raw weight at least `C_3/(6L)`.

Consequently, if either expected active term is at least `Q`, one exact interaction/profile class has raw weight at least

$$
4Q/(7L).
$$

Under the RI5ab failed-bank output, if an active term rather than blocker repair is selected, one exact terminal interaction class has raw weight at least

$$
4(G_*/2-F)/(21L).
$$

Every selected class is then either a bounded-multiplicity one-target incidence family or an exact two-target secant family.

### Proof

RI5ac gives at most seven rank-two words and six rank-three words. Pigeonhole after the finite profile split gives the first two bounds. If `H_2^*>=Q`, then `C_2>=4Q`, yielding `4Q/(7L)`. If `H_3^*>=Q`, then `C_3>=8Q`, yielding the stronger `4Q/(3L)`. The conservative common bound is `4Q/(7L)`.

RI5ab gives `Q=(G_*/2-F)/3` for a selected active term. Substitute this value. RI5ad supplies the two geometric alternatives. QED.

## Interface to RI6

The shadow-free active obstruction is no longer an arbitrary two- or three-component interaction.

- It has one of thirteen finite component words.
- It contains one or two target-hyperbola cells.
- One-target classes have context-pair multiplicity at most two.
- Two-target classes have exact sum/product secant addresses.

The remaining arithmetic task is to classify the component quotient/scale/carry labels inside one selected word and one selected incidence geometry. This is the direct input needed for the fixed-edge bank audit.

## Finite check

`scripts/verify_rational_terminal_interactions.py` enumerates the canonical rank-two and rank-three words, rejects exactly the three-target cases, and checks the two hyperbola geometries over small finite fields. It also verifies the word/profile pigeonhole constants and the conversion from expected to raw weight.