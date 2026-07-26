# Canonical reconstruction of unary blocker hosts

**Branch:** `research/alternating-core-chain`

AC3jd defines the unary blocker base host by testing every physical blocker cell
against the exact hard checks activated by its one-cell insertion.  AC3lv warns
that an arbitrary host subset can have exponential state entropy.  The host
constructed by AC3jd is not arbitrary: once its exact hard registry and current
builder context are fixed, the host and its least-reason map are deterministic.

This note removes that derived blocker host as an independent outer-profile
field.  It also quantifies how registry and context changes can affect the host.
The result applies only to the declared unary builder.  The active-layer base
host, nonunary feasibility conditions and any discretionary filtering remain
separate until they receive their own reconstruction theorem.

## Unary builder data

Let `Omega_B` be the physical blocker-cell universe, of size

\[
U_B=|\Omega_B|\le n^2.
\]

Let `omega` be the fixed binary blocker assignment used by the builder, and let
`H` be a finite exact hard-check registry.  A check is

\[
C=(S_C,f_C),
\]

with the activation relation from AC3jd: a currently absent cell `z` activates
`C` when

\[
z\in S_C,\qquad f_C(z)=1,
\qquad
f_C|_{S_C\setminus\{z\}}
=
\omega|_{S_C\setminus\{z\}}.
\]

Write `Act(C,omega,z)` for this predicate.  Fix global total orders on exact
checks and physical cells.  Define

\[
B_{\rm un}(\mathcal H,\omega)
=
\{z\in\Omega_B:
  \text{no }C\in\mathcal H\text{ satisfies }\operatorname{Act}(C,\omega,z)
\}.
\]

For every missing cell, define the canonical reason map

\[
r_{\mathcal H,\omega}(z)
=
\min\{C\in\mathcal H:
       \operatorname{Act}(C,\omega,z)\}.
\]

Current occupied cells activate no insertion check and therefore remain in the
base host.

## AC3lz -- exact host and reason reconstruction -- PROVED

The pair

\[
\boxed{
\bigl(B_{\rm un}(\mathcal H,\omega),
      r_{\mathcal H,\omega}\bigr)
}
\]

is a deterministic function of the exact registry `H`, the exact builder
assignment `omega` and the fixed global orders.

Consequently:

1. equal registry and context inputs give exactly equal hosts;
2. equal inputs give exactly equal least-reason maps;
3. while those inputs remain fixed, there is no independent blocker-host reset;
4. storing a separate arbitrary blocker-host subset would duplicate derived
   state and incorrectly introduce up to `2^(n^2)` apparent profiles.

### Proof

For each physical cell, the membership decision is the Boolean statement that
no check in the fixed registry activates at that cell.  The least-reason value,
when the membership decision is negative, is selected from the same fixed
activated set by the fixed order.  Both outputs are therefore determined
cell-by-cell by `(H,omega)`. QED.

The theorem does not claim that the registry or context themselves have
polynomially many states.  It removes only the additional Cartesian factor
which would store their derived host again.

## AC3ma -- registry symmetric-difference Lipschitz bound -- PROVED

Fix `omega` and two exact registries `H,H'`.  Then

\[
\boxed{
|B_{\rm un}(\mathcal H,\omega)
 \triangle
 B_{\rm un}(\mathcal H',\omega)|
\le
|\mathcal H\triangle\mathcal H'|.
}
\]

The support on which their canonical least-reason maps differ also has size at
most

\[
\boxed{|\mathcal H\triangle\mathcal H'|.}
\]

In particular, adding or removing one exact check changes the host at at most
one physical cell and changes the least-reason map at at most one cell.

### Proof

Suppose a cell has different host membership.  Some check activates there in
one registry and no check activates there in the other.  Any check common to
both registries has the same activation predicate in the fixed context, so at
least one activating check belongs to the registry symmetric difference.
AC3je proves that one exact check activates at most one inserted cell in a fixed
context.  Assign each changed host cell to one such changed check, giving the
first bound.

If the least reason changes at a cell, the activated-check sets cannot be
identical there; otherwise their least elements would agree.  Hence a changed
check activates at that cell, and the same uniqueness argument proves the
second bound. QED.

## AC3mb -- exact context-sensitivity bound -- PROVED

Fix one registry `H` and two hard-feasible builder assignments `omega,omega'`.
Let

\[
Y=\{y:\omega_y\ne\omega'_y\}
\]

and let

\[
\mathcal I_{\mathcal H}(Y)
=
\{C\in\mathcal H:S_C\cap Y\ne\varnothing\}.
\]

Then

\[
\boxed{
|B_{\rm un}(\mathcal H,\omega)
 \triangle
 B_{\rm un}(\mathcal H,\omega')|
\le
2|\mathcal I_{\mathcal H}(Y)|.
}
\]

The support on which the least-reason maps differ obeys the same bound.
If

\[
\Delta_{\mathcal H}
=
\max_y|\{C\in\mathcal H:y\in S_C\}|,
\]

then the coarser physical estimate is

\[
\boxed{
|B_{\rm un}(\mathcal H,\omega)
 \triangle
 B_{\rm un}(\mathcal H,\omega')|
\le
2\Delta_{\mathcal H}|Y|.
}
\]

### Proof

A check whose scope avoids `Y` sees identical assignments in both contexts, so
its activation status at every target is unchanged.  Therefore every changed
host or reason cell is witnessed by a check in `I_H(Y)`.  One such check can
activate at most one cell in the first context and at most one cell in the
second context, giving at most two affected cells per incident check.  The
maximum-incidence estimate follows from
`|I_H(Y)|<=Delta_H |Y|`. QED.

## AC3mc -- monotone registry evolution induces monotone host evolution -- PROVED

For fixed `omega`:

1. if `H subseteq H'`, then
   \[
   \boxed{
   B_{\rm un}(\mathcal H',\omega)
   \subseteq
   B_{\rm un}(\mathcal H,\omega);
   }
   \]
2. registry additions can only close host cells;
3. registry removals can only reopen host cells;
4. along any monotone registry history, the derived host changes strictly at
   most `U_B` times.

### Proof

Every check activated from the smaller registry is still present in the larger
registry, so a cell blocked before remains blocked.  This proves the inclusion
and the two directional statements.  A strictly decreasing or increasing
sequence of subsets of the `U_B` physical blocker cells has at most `U_B`
strict changes, as in AC3lx. QED.

The least-reason map may change while a cell remains blocked, but that change is
already caused and counted by the registry atom update; it is not a separate
host-state transition.

## Combined input changes

For two builder inputs `(H,omega)` and `(H',omega')`, put

\[
\mathcal R=\mathcal H\triangle\mathcal H',
\qquad
Y=\{y:\omega_y\ne\omega'_y\},
\]

and

\[
\mathcal I_{\cap}(Y)
=
\{C\in\mathcal H\cap\mathcal H':S_C\cap Y\ne\varnothing\}.
\]

## AC3md -- exact host-reset cause localization -- PROVED

The combined host difference satisfies

\[
\boxed{
|B_{\rm un}(\mathcal H,\omega)
 \triangle
 B_{\rm un}(\mathcal H',\omega')|
\le
|\mathcal R|+2|\mathcal I_{\cap}(Y)|.
}
\]

Every changed host cell has one canonical least cause of exactly one of the
following forms.

1. **Registry addition:** one exact check in `H'\H` activates the cell.
2. **Registry removal:** one exact check in `H\H'` activates the cell in the
   old context.
3. **Context sensitivity:** one common exact check meeting `Y` changes its
   activation status.

For a context cause retain the least changed literal
`y in S_C cap Y` and its direction.  If the exact hard-check atom stock is
`N_H` and the context-literal address stock is `U_ctx`, a safe cause-decoration
alphabet has size

\[
\boxed{
R_{\rm host}
\le
2U_BN_H(U_{\rm ctx}+1).
}
\]

A weighted family of derived-host changes of total weight `W` therefore has one
exact cell/check/cause class of weight at least

\[
\boxed{W/R_{\rm host}.}
\]

### Proof

A changed host cell is blocked by an activated check on one side and unblocked
on the other.  If that check is not common to the two registries, it belongs to
`R` and contributes at most one target on its side.  If it is common, its
activation can differ only because its scope meets `Y`; it contributes at most
one target in each context.  This gives the displayed bound.

Choose the least changed host cell, then the least applicable exact check and,
for a context cause, the least changed literal in its scope.  There are two
registry directions or two context-bit directions, giving the safe alphabet
bound.  Weighted pigeonhole proves the final statement. QED.

Equality of a cause decoration does not imply equality of the complete registry
or context states.  Repetition still needs the ticket, payment, descent or
reconstruction mechanisms of AC3kd.

## AC3me -- blocker-host outer-profile reduction -- PROVED UNDER THE UNARY BUILDER CONTRACT

When the blocker base host is constructed exactly by AC3jd, the global outer
profile need not retain a separate `blocker-base-host construction` subset.
Instead retain only the actual builder inputs used by the activation predicates:

- exact arithmetic and physical context data;
- the exact hard/protected/mask/envelope registry atoms or their canonical
  generators;
- the builder assignment `omega` or its already declared context identifier;
- the fixed global check and cell orders.

Then:

1. fixed inputs force a fixed blocker host by AC3lz;
2. registry changes route through AC3ma and AC3md;
3. context changes route through AC3mb and AC3md;
4. monotone registry evolution gives an opposite monotone host potential by
   AC3mc;
5. a host change with no changed input is impossible.

Thus the derived blocker host contributes no independent set-state multiplier
to the AC3ka profile count.  Its reset witness is inherited from the changed
registry or context field.

### Proof

AC3lz gives exact reconstruction.  AC3ma--AC3md classify every possible change
of the reconstructed output by a change of its inputs.  A deterministic output
cannot vary while all inputs are fixed, and adding it as an independent profile
coordinate would only duplicate information. QED.

This theorem does **not** remove:

- the active-layer base host `A` of AC3iu;
- nonunary constraints, which remain in the AC3v primal system;
- discretionary host filtering not represented by canonical exact hard checks;
- exponential entropy in the hard registry or builder context themselves.

Any implementation using extra discretionary filtering must expose that filter
as a separate outer field and cannot invoke AC3me for it.

## Consequence

One set-valued AC4 field has been reduced safely.  The canonical unary blocker
host and least-reason map are derived from exact builder inputs, registry atom
changes have a one-cell Lipschitz bound, context changes have an explicit
incidence bound, and monotone registry histories induce monotone host histories.

The remaining set-valued frontier is the active-layer host, canonicalization of
AC3v envelopes and protected/hard registries, together with nonmonotone changes
of their generating data.

## Finite check

`scripts/verify_ac_unary_host_reconstruction.py` exhausts exact binary hard
checks of rank at most three on four variables, verifies unique one-cell
activation, deterministic reconstruction, more than half a million registry
atom toggles, every feasible one-bit context transition for registries through
size three, combined registry/context changes, cause localization, monotone
host inclusion and the displayed decoration bounds.
