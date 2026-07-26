# Canonical reconstruction of active hosts and protected registries

**Branch:** `research/alternating-core-chain`

AC3lv warns that a physical atom dictionary does not by itself make a
set-valued outer field polynomial. AC3lz--AC3me remove the unary blocker host by
reconstructing it from exact hard checks and the current builder assignment.
This note gives the corresponding contract for the active-layer host and for a
maximal protected registry.

The result is conditional on canonical builders. An active host obtained by
extra discretionary filtering, or a protected bank chosen as an arbitrary
subset of the currently realised protected atoms, remains genuine generator
data. The theorems below remove only the deterministic set-valued outputs of
declared predicates.

## Canonical active-cell exclusions

Let `Omega_A` be the physical active-layer cell universe, with

\[
U_A=|\Omega_A|\le n^2.
\]

An exact active-support generator produces a base support

\[
G(\chi)\subseteq\Omega_A
\]

from arithmetic and physical context `chi`. Retain this generator and its
context as genuine input data.

Let `V_ctx` be a finite context-literal universe and let `omega` be the current
context assignment. An exact one-cell exclusion atom is a tuple

\[
E=(z,D_E,g_E),
\]

where `z in Omega_A` is its unique target cell, `D_E subseteq V_ctx` is its
dependency scope and `g_E` is one forbidden exact assignment on that scope. The
atom is active in context `omega` when

\[
\omega|_{D_E}=g_E.
\]

For an exact exclusion registry `E`, define the canonical active host

\[
\boxed{
A_{\rm can}(G,\mathcal E,\omega)
=
G\setminus
\{z:\text{some }E\in\mathcal E
\text{ targets }z\text{ and is active at }\omega\}.
}
\]

Soft collateral, constraints involving two or more newly inserted active cells,
and protected high-line events are not one-cell exclusions. They remain in the
AC3v primal system and AC5 scale filter.

## AC3ml -- exact active-host reconstruction -- PROVED UNDER THE DECLARED BUILDER CONTRACT

The active host `A_can` is a deterministic function of:

- the exact base-support generator output `G(chi)`;
- the exact one-cell exclusion registry `E`;
- the exact context assignment `omega`; and
- the fixed orders used for canonical cause selection.

Consequently fixed inputs force one fixed active host. There is no independent
active-host reset while those inputs remain fixed, and storing an additional
arbitrary host subset would duplicate derived data.

### Proof

For each cell `z`, membership is the Boolean conjunction that `z` belongs to
`G` and no exact exclusion atom targeting `z` is active. All predicates and
inputs are fixed, so the decision is fixed cell by cell. QED.

The theorem does not bound the number of possible base-support generators,
registries or contexts.

## AC3mm -- exact active-host cause localization -- PROVED

Compare inputs `(G,E,omega)` and `(G',E',omega')`. Put

\[
\mathcal R=\mathcal E\triangle\mathcal E',
\qquad
Y=\{y:\omega_y\ne\omega'_y\},
\]

and

\[
\mathcal I_\cap(Y)
=
\{E\in\mathcal E\cap\mathcal E':D_E\cap Y\ne\varnothing\}.
\]

Writing `t(F)` for the set of target cells of an atom family `F`,

\[
\boxed{
A_{\rm can}(G,\mathcal E,\omega)
\triangle
A_{\rm can}(G',\mathcal E',\omega')
\subseteq
(G\triangle G')
\cup t(\mathcal R)
\cup t(\mathcal I_\cap(Y)).
}
\]

Therefore

\[
\boxed{
|A_{\rm can}\triangle A'_{\rm can}|
\le
|G\triangle G'|
+|t(\mathcal R)|
+|t(\mathcal I_\cap(Y))|
}
\]

and safely

\[
|A_{\rm can}\triangle A'_{\rm can}|
\le
|G\triangle G'|+|\mathcal R|+|\mathcal I_\cap(Y)|.
\]

Every changed active-host cell has one canonical least cause of exactly one
kind:

1. base-support addition or removal;
2. exclusion-registry addition or removal;
3. context sensitivity of a common exclusion atom.

If the exact exclusion-atom stock is `N_E` and the context-literal stock is
`U_ctx`, a safe cell/cause decoration alphabet has size

\[
\boxed{
R_A\le 2U_A\bigl(1+N_E(U_{\rm ctx}+1)\bigr).
}
\]

A weighted family of derived active-host changes of total weight `W` therefore
has one exact cause class of weight at least `W/R_A`.

### Proof

A cell whose membership changes must either change membership in the base
support or change blocked/unblocked status. In the latter case some active
exclusion atom appears on only one side. If it is not common to the registries,
it lies in `R`. If it is common, its truth value can change only because its
dependency scope meets `Y`. This proves the set inclusion and cardinality
bounds. Fixed orders select the least changed cell and least applicable cause.
The displayed alphabet is a safe product bound, and weighted pigeonhole gives
the final statement. QED.

Equality of the cause decoration does not identify the full generator,
registry or context state and is not by itself progress.

## AC3mn -- compatible monotone inputs induce a monotone active host -- PROVED

For fixed context `omega`:

1. enlarging the base support can only enlarge `A_can`;
2. shrinking the base support can only shrink `A_can`;
3. adding exclusion atoms can only shrink `A_can`;
4. removing exclusion atoms can only enlarge `A_can`.

Hence either of the following compatible histories is monotone:

- base support only enlarges while the exclusion registry only loses atoms;
- base support only shrinks while the exclusion registry only gains atoms.

Along such a history the derived active host changes strictly at most `U_A`
times.

### Proof

The active host is the base support minus the cells blocked by active exclusion
atoms. Each of the four operations has the stated inclusion direction. In the
two compatible combinations both inputs move the output in the same direction.
A strictly monotone sequence of subsets of `Omega_A` changes at most `U_A`
times. QED.

Opposing changes, such as simultaneous support enlargement and exclusion
addition, need not make the host monotone and remain in the reset router.

## AC3mo -- active-host outer-profile reduction -- PROVED UNDER THE CANONICAL ACTIVE BUILDER

Assume every active-layer transition family declares:

- one exact arithmetic/physical base-support generator `G(chi)`;
- one exact one-cell exclusion registry;
- the context assignment used by those exclusion predicates;
- all nonunary hard constraints, soft factors and protected events separately in
  AC3v and AC5.

Require the active base host to equal `A_can`. Then the active-host subset is a
derived field and need not appear as an independent coordinate in the AC3ka
outer profile.

A changed active host is inherited from exactly one of:

- a base-support generator or arithmetic-context change;
- an exclusion-registry atom change;
- a context-literal change.

Compatible monotone input histories enter AC3mn's linear cell potential;
nonmonotone input histories retain AC3mm's exact cause decoration and still need
payment, descent, impossibility or a capacity-one ticket.

### Proof

AC3ml gives deterministic reconstruction. AC3mm classifies every possible
change by an input cause, and AC3mn handles compatible monotone histories. A
deterministic output cannot change while its inputs remain fixed, so storing the
host again would only duplicate its generators. QED.

This theorem does not apply to discretionary pruning, heuristic partner
filters, or constraints whose truth requires two or more newly inserted cells.
Those must remain explicit generator or AC3v data.

## Canonical maximal protected registry

Let `U_prot` be a finite universe of exact protected atoms. Each atom `p` has:

- a finite physical support `Q_p`;
- a protection-context predicate `rho_p(kappa)` depending on scale, bank type or
  another declared protection context `kappa`.

For a current physical state `S`, define the maximal realised protected registry

\[
\boxed{
\mathcal P_{\max}(S,\kappa)
=
\{p\in\mathcal U_{\rm prot}:
Q_p\subseteq S,
\ \rho_p(\kappa)=1\}.
}
\]

Owner identities, capacities and payment rights are not inferred from
membership in this registry. They remain separate AC3kf owner records.

## AC3mp -- protected-registry reconstruction and incidence bound -- PROVED

The maximal registry `P_max(S,kappa)` is a deterministic function of the exact
physical state, protected-atom dictionary and protection context.

For fixed `kappa` and two states `S,S'`, put `D=S triangle S'`. Then

\[
\boxed{
\mathcal P_{\max}(S,\kappa)
\triangle
\mathcal P_{\max}(S',\kappa)
\subseteq
\{p:Q_p\cap D\ne\varnothing\}.
}
\]

If

\[
\Delta_{\rm prot}
=
\max_x|\{p:x\in Q_p\}|,
\]

then

\[
\boxed{
|\mathcal P_{\max}(S,\kappa)
\triangle
\mathcal P_{\max}(S',\kappa)|
\le
\Delta_{\rm prot}|S\triangle S'|.
}
\]

For a context change `kappa -> kappa'`, only atoms whose protection predicate
changes can enter the registry difference. Every changed protected atom can
therefore retain either one changed physical support cell or one exact changed
protection-context field as its canonical cause.

### Proof

If a protected atom changes realised status while `kappa` is fixed, its support
is contained in exactly one of `S,S'`. Therefore some support cell belongs to
the state symmetric difference. Counting incidences gives the degree bound.
For a context change with fixed state, physical realisation is unchanged, so
only the predicate value can change. Determinism is immediate from the
definition. QED.

## AC3mq -- corrected protected-field and residual set-state interface -- PROVED

If an installed bank declares its protected registry to be exactly
`P_max(S,kappa)`, that registry is a derived field and is removed as an
independent outer-profile coordinate. Its changes are inherited from physical
state changes or protection-context changes through AC3mp.

The following data are **not** removed:

1. an arbitrary selected subbank of `P_max`;
2. independent owner, capacity or payment assignments on protected atoms;
3. a protection predicate or atom dictionary with unbounded generator entropy;
4. global or unbounded-scope protected conditions;
5. discretionary active-host filters excluded by AC3mo;
6. the arithmetic base-support generator and exact exclusion registry.

Consequently AC3me, AC3mk, AC3mo and AC3mq remove four duplicated set-valued
outputs from the outer profile:

- the canonical unary blocker host;
- its least-reason map;
- canonical AC3v private/common envelopes;
- the canonical active host and maximal protected registry.

The live set-state frontier is now concentrated on the actual hard/protected
atom generators, selected-subbank or owner assignments, arithmetic support
generators and transition-state families. These generators still require a
polynomial quotient, monotonicity, payment, descent, impossibility or
capacity-one tickets.

### Proof

The first statement is AC3mp's deterministic reconstruction. The exclusions
list data not determined by `(S,kappa)` and the fixed atom dictionary, so none
can be deleted without an additional theorem. The final inventory combines the
four reconstruction interfaces and AC3lv's set-entropy guardrail. QED.

## Consequence

The active host and the maximal realised protected set are no longer legitimate
unlabelled AC4 reset fields under their canonical contracts. Any recurrence must
now expose the input that actually changed: arithmetic support, one-cell
exclusion atom, context literal, physical state, protection context, selected
subbank, owner assignment or transition generator.

## Finite check

`scripts/verify_ac_active_host_protected_reconstruction.py` exhausts canonical
one-cell active-host systems on three cells and two context bits, checks every
single registry toggle, all context pairs, compatible monotone directions and
combined cause bounds, and exhausts maximal protected registries on four cells
with support rank at most three, verifying state-incidence localization and all
displayed degree bounds.
