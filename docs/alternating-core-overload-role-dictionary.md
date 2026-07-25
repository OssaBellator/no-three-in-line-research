# Finite role dictionary for dense AC2d overloads

**Branch:** `research/alternating-core-chain`

AC2c returns either a compatible paid bank or one object whose full scoped conflict neighbourhood carries much more paid weight than the object itself. AC3x labels such edges by structural incidence words, but the current frontier still refers to “finite AC2d overload labels” without recording the local cell positions responsible for the conflict. The executable BDA and RI banks now have finite local envelope-role alphabets. Combining those roles with the AC3x incidence words gives an explicit core grid dictionary.

## Exact local envelope roles

Fix one exact arithmetic/profile class of local repair objects. Let `E` be a finite set of normalized roles for every cell which can occur in any local repair envelope, including old cells removed by the repair, new cells, auxiliary blocker cells and blocker replacements. Exact physical addresses remain attached to occurrences. Put

$$
e=|E|.
$$

Assume the candidate family has private paid buckets, so distinct objects do not share a paid certificate. This holds for the clean-pair, missing-support, scale and companion banks after their proved aggregation steps.

## Core grid conflicts

Ignore separately declared protected-bank constraints for the moment. Two disjoint local objects can still conflict for one of the following core geometric reasons.

1. **Envelope-cell overlap.** One physical cell has one role in each envelope.
2. **Row conflict.** A rank-two row scope meets both envelopes.
3. **Column conflict.** A rank-two column scope meets both envelopes.
4. **Cross-triple conflict.** One real-collinear triple scope meets both envelopes.

Replacement-cell overlap is envelope-cell overlap. Inter-layer cell disjointness is also detected by envelope-cell overlap; matching row and column constraints are cases 2 and 3.

## AC3fp -- explicit core overload dictionary -- PROVED

The core conflicts use at most

$$
\boxed{
T_{\rm core}(e)
=
18e^3+5e^2
}
$$

role-labelled edge types.

More precisely:

- envelope-cell overlap uses at most `e^2` ordered role pairs;
- row conflict has two cross-incidence words `JK,KJ` and at most `2e^2` role labels;
- column conflict has the same bound `2e^2`;
- a rank-three cross-triple witness has exactly eighteen `J,K,B,O` incidence words containing both `J` and `K`, and at most `18e^3` role-labelled words.

The private paid-overlap label is absent under the stated hypothesis.

### Proof

For an oriented object pair, a shared cell has one role in each envelope, giving `e^2` labels. A two-cell row or column scope meeting both disjoint envelopes has incidence word `JK` or `KJ`; assigning the two local roles gives at most `2e^2` labels per scope kind. AC3x counts

$$
4^3-2\cdot3^3+2^3=18
$$

rank-three incidence words containing both endpoint symbols. Assigning a role to every position is a safe upper bound of `e^3`, even though `B` and `O` positions do not require a local role. Summing gives `18e^3+(1+2+2)e^2`. QED.

## Protected constraints

Suppose there are `q` additional protected or feasibility kinds, each of rank at most `r`. Label every witness cell by its `J,K,B,O` incidence symbol and, when it lies in a private envelope, by its local role. A safe bound for the additional dictionary is

$$
q\sum_{s=1}^{r}(4e)^s.
$$

## AC3fq -- total finite overload label bound -- PROVED

With the protected constraints above, the canonical dense-return dictionary has size at most

$$
\boxed{
T(e,q,r)
\le
18e^3+5e^2
+
q\sum_{s=1}^{r}(4e)^s.
}
$$

If one nonprivate paid-overlap reason is allowed, add one label.

### Proof

AC3fp counts the core grid reasons. For a protected witness of rank `s`, each position has at most four incidence symbols and at most `e` local-role decorations, giving at most `(4e)^s` words. Sum over ranks and kinds. QED.

The bound is deliberately conservative: it counts noncrossing words and unnecessary roles at `B,O` positions. Its purpose is a uniform finite recursion dictionary, not constant optimization.

## Current local envelope bounds

The executable banks admit the following safe envelope-role inventories.

### Clean BDA pair: `e_clean <= 11`

- five radial support cells;
- four opposite-diagonal cross cells;
- two possible coupled blocker replacement positions.

Thus

$$
\boxed{e_{\rm clean}\le11,}
$$

and

$$
\boxed{T_{\rm core}(11)=24563.}
$$

### Missing BDA support: `e_miss <= 40`

A safe union over the complete install-and-decode menu contains:

- five radial support roles;
- four BDA cross roles;
- at most four old and four new active-completion roles;
- one generic auxiliary blocker role;
- twenty first-repair replacement roles;
- two coupled decoder-blocker replacement roles.

Hence

$$
\boxed{e_{\rm miss}\le40,}
$$

and

$$
\boxed{T_{\rm core}(40)=1160000.}
$$

### Direct RI companion rectangle: `e_dir <= 13`

The four-point line and opposite diagonal use six cell roles. One blocker repair contributes one generic auxiliary role and at most six replacement roles. Hence

$$
\boxed{e_{\rm dir}\le13,}
$$

and

$$
\boxed{T_{\rm core}(13)=40391.}
$$

### Absent-anchor companion composite: `e_abs <= 24`

Use six direct rectangle roles, at most four old/new one-cell completion roles, and at most seven roles for each of the two blocker repair stages. Thus

$$
\boxed{e_{\rm abs}\le24,}
$$

and

$$
\boxed{T_{\rm core}(24)=251712.}
$$

The role inventories retain stage and layer, so an identically positioned cell used in two stages may receive two labels. This only enlarges the safe bound.

## AC3fr -- quantitative labelled overload descent -- PROVED

Let an object `o` in one of these exact profile classes satisfy

$$
L(o)>K w(o),
\qquad K>1.
$$

With no additional protected kinds, one explicit core role label carries neighbouring paid weight greater than

$$
\boxed{
\frac{K-1}{T_{\rm core}(e)}w(o).
}
$$

With protected kinds, replace `T_core(e)` by `T(e,q,r)`.

Inside the selected label class, AC2d returns one of:

1. a deeper overload using the same exact reason/role word;
2. a compatible paid family of weight greater than
   $$
   \frac{K-1}{TQ}w(o);
   $$
3. one heavier neighbour;
4. a broad same-label star.

For core labels, the arithmetic object is now explicit:

- one shared physical cell with an ordered pair of local roles;
- one row or column collision with an ordered role pair;
- or one real-collinear cross-envelope witness with one of eighteen incidence words and a finite role tuple.

### Proof

AC3fp--AC3fq give a finite canonical edge partition. Apply AC2d with its dictionary size. QED.

## Consequence

Dense conflicts in the executable BDA and companion banks no longer return an unspecified “finite overload label.” They return one exact local role collision or one named external protected kind, with quantitative paid mass. The remaining work is arithmetic termination of those same-role stars or cross-triple witness families and proof that repeated descent consumes a finite ticket or exposes a new signature.

## Finite check

`scripts/verify_ac_overload_role_dictionary.py` enumerates the rank-three incidence words, verifies the eighteen cross words, checks the core formula, the four current envelope bounds and bounded weighted label pigeonholes.
