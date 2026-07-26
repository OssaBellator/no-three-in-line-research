# Final-universe telescoping and future-controller credit dependencies

PP3apm--PP3apr prove global termination when every puncture stage is already a
strict paid move for its new active universe.  A multi-step package may be known
to have credit at each intermediate stage without yet having a stagewise strict
inequality after all later punctures are imposed.

The correct common comparison is the **final candidate universe**.  Re-evaluate
every trade in the package using only entries whose controllers survive the whole
package.  The dynamic identities telescope exactly.  Designated removal credit
survives unless its candidate entry is controlled by a point punctured later.

Consequently failure of final-universe payment has one precise cause: a large
fraction of the recorded credit points forward to future puncture centres.  Those
lost-credit records form a directed chronological dependency table.  A
matching-versus-degree argument localizes it to a repeated candidate dependency,
a future-controller star, or a target-size full dependency matching.

## 1. Fixed final-universe telescoping

Consider source states

```text
S_0,S_1,...,S_H
```

and nested puncture sets

```text
X_0 subseteq X_1 subseteq ... subseteq X_H=F.
```

Let

```text
V_F
```

be the final active candidate universe.  For stage `j`, let

```text
I_j^F
```

be the complete insertion-shadow increase counted in `V_F`, and let

```text
R_j^F
```

be the complete removal credit counted in `V_F`.

### Proposition PP3aps -- PROVED

The complete package satisfies the exact identity

```text
Psi_F(S_H)-Psi_F(S_0)
=
sum_(j=1)^H (I_j^F-R_j^F).
```

In particular all intermediate creation and destruction cancel without any
coexistence or stability hypothesis on the blocker endpoints.

#### Proof

For the fixed universe `V_F`, the dynamic potential identity applies to every
source-admissible transition:

```text
Psi_F(S_j)-Psi_F(S_(j-1))=I_j^F-R_j^F.
```

Sum over `j`. ∎

This is potential path independence.  It is distinct from final blocker-support
path independence: the present identity retains insertion and removal
multiplicity but cancels it algebraically.

## 2. Which designated star credits survive

At stage `j`, let

```text
D_j
```

be a chosen multiset of designated removal incidences.  Each incidence consists
of a blocker pair destroyed by the stage and a candidate entry `z` belonging to
`V_(X_j)`.  Define

```text
D_j^F={d in D_j: controller(z_d) notin F}.
```

### Proposition PP3apt -- PROVED

Every incidence in `D_j^F` contributes one unit to `R_j^F`.  Therefore

```text
R_j^F >= |D_j^F|
```

and

```text
Psi_F(S_H)-Psi_F(S_0)
<=
sum_j I_j^F - sum_j |D_j^F|.
```

#### Proof

The blocker pair of a designated incidence is present immediately before stage
`j` and is destroyed by that stage.  If its entry controller is not punctured in
the final set `F`, the entry belongs to `V_F`; hence the same incidence is counted
as removal credit in the fixed final-universe identity.  Sum and use PP3aps. ∎

Later deletion of the blocker partner does not erase this historical removal
term.  Only deletion of the candidate entry from the final universe can erase it.

## 3. Global slack versus lost credit

Put

```text
C=sum_j |D_j|,
L=sum_j |D_j\D_j^F|,
I=sum_j I_j^F.
```

Thus `C-L` designated credits survive in the final universe.

### Theorem PP3apu -- PROVED

If

```text
I < C-L,
```

then

```text
Psi_F(S_H)<Psi_F(S_0)<=Psi_(X_0)(S_0).
```

Hence the complete nested puncture package makes strict global progress.

More generally, if for some `eta>0`

```text
I <= (1-eta)C,
```

then failure of strict final-universe payment forces

```text
L >= eta C.
```

#### Proof

The first statement is PP3apt followed by PP3apm.  For the second, if
`L<eta C`, then

```text
C-L>(1-eta)C>=I,
```

so the first statement applies. ∎

Thus a package with uniform paid slack can fail only by losing a comparable
fraction of its designated entries to later controller punctures.

## 4. Future-controller dependency records

Suppose the puncture centres are ordered

```text
p_1,...,p_H.
```

For every lost designated credit at stage `j`, record

```text
(p_j,z,e,k),
```

where `z` is the complete candidate entry, `e` is its controller point, and `k>j`
is the unique later stage at which `e=p_k` is punctured.

The inequality `k>j` is forced: if `e` had already been punctured, `z` would not
belong to the active universe at stage `j`.

For one centre `p_j`, the designated candidate entries are distinct by PP3apf.
Let

```text
G_dep subseteq {p_1,...,p_H} x Z_lost
```

be the simple bipartite graph joining a centre to each complete lost candidate
entry used by that centre.

### Proposition PP3apv -- PROVED

If every stage chooses at most `W` designated credits, then

```text
Delta_left(G_dep)<=W,
|E(G_dep)|=L.
```

Every right vertex is controlled by a strictly later puncture centre.

#### Proof

The left-degree bound is the chosen credit cap.  Distinctness of candidate entries
for one source-star centre is PP3apf.  The chronological controller statement is
the preceding observation. ∎

## 5. Dependency localization

Let

```text
Delta_Z=max_z degree_G_dep(z).
```

### Theorem PP3apw -- PROVED

For every integer `D>=1`, at least one of the following holds.

1. One exact candidate entry is used as lost credit by at least `D` earlier
   puncture centres.
2. There is a centre--lost-entry matching of size at least

   ```text
   L/(W+D).
   ```

#### Proof

Assume every right degree is below `D` and take a maximal matching of size `s`.
Every dependency edge meets a matched left centre or matched right entry.  The
matched centres cover at most `sW` edges and the matched entries cover fewer than
`sD` edges.  Hence

```text
L<s(W+D),
```

which gives the result. ∎

Retain one movement/refill type from the matching.  Split the complete entry
coordinate into its future controller and final label, and retain the chronological
blocker partner as an additional resource.

### Corollary PP3apx -- PROVED

For every `D>=1`, a one-type centre--lost-entry matching of size `K` gives one of:

1. one chronological blocker partner in at least `D` records;
2. one later puncture centre controlling at least `D` lost entries;
3. one final label occurring in at least `D` lost entries;
4. a chronological dependency matching of size at least

   ```text
   K/(6D)
   ```

   with distinct earlier centres, partners, later controller centres, labels, and
   complete candidate entries.

#### Proof

This is the greedy resource deletion in PP3aph, with the controller coordinate now
identified as a strictly later puncture centre. ∎

The second alternative is a directed many-to-one dependency stack, while the
fourth is a family of disjoint forward dependencies.

## 6. Slab-scale consequence

Assume every one of `H>=beta R` puncture stages selects exactly `W=sqrt(R)`
designated credits and the final-universe insertion total satisfies

```text
I <= (1-eta)HW
```

for fixed `beta,eta>0`.

### Corollary PP3apy -- PROVED

Either the complete package strictly decreases the final-universe potential, or
there is one of the following target-scale future-controller structures.

1. One exact lost candidate entry used by at least `W` earlier centres.
2. One chronological partner used by at least `W` earlier centres.
3. One later puncture centre controlling at least `W` lost credit entries.
4. One final label supporting at least `W` lost credit entries.
5. A full forward dependency matching of size at least

   ```text
   (eta beta/12+o(1))W.
   ```

#### Proof

Failure of strict payment gives `L>=eta HW` by PP3apu.  Apply PP3apw with `D=W`.
The matching branch has size at least

```text
L/(2W)>=eta beta R/2.
```

Retain one type and apply PP3apx with `D=W`.  The full dependency matching has
size at least

```text
(eta beta R/2)/(6W)
=
(eta beta/12)W.
```

The high-degree alternatives give items 1--4. ∎

## 7. Revised temporal frontier

### Corollary PP3apz -- PROVED

Temporal instability of blocker endpoints is not the primary obstruction to
multi-step puncture payment.  In the fixed final universe, historical removals
telescope whether or not their blocker endpoints coexist later.

A nonmonotone puncture package now has the exact alternatives:

1. enough designated entries survive the final puncture set, and the package
   strictly decreases the final-universe potential;
2. a positive fraction of credit points to controllers punctured later, producing
   an exact candidate dependency, partner stack, future-controller stack,
   fixed-label stack, or full forward dependency matching of target order;
3. the claimed aggregate paid slack fails because final-universe insertion cost is
   already at the total removal-credit scale;
4. source, marked-host, controller-pool, Hall, alternating, or distinguished
   endpoint preparation fails.

Thus the live puncture-history problem has been reduced from arbitrary transient
blocker witnesses to **future-controller credit dependencies** and residual
final-universe insertion cost.

The no-three-in-line conjecture remains unproved.
