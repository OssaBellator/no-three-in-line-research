# Controller-entry deletion telescopes every future-dependency history

PP3aps--PP3apz compare a nonmonotone puncture package in its final candidate
universe and isolate credits whose entries are controlled by later-punctured
points.  Those records form a forward dependency graph.  Entrywise accounting
shows that this graph is not itself a negative contribution.

For one candidate entry, all insertion and removal events before its controller is
punctured telescope to its blocker-incidence count immediately before deletion.
Deleting the entry then removes that whole count.  The complete chronological
contribution of a later-deleted entry is therefore exactly the negative of its
initial blocker mass, independently of every intermediate oscillation.

Consequently future-controller credit dependencies need no separate payment.  They
are internal events on entries that disappear from the potential.  The only live
history cost is the net change on entries whose controllers survive the package,
with an additional favourable credit equal to the initial mass of all deleted
entries.

## 1. Incidence count of one candidate entry

Fix an initial candidate universe `V_0`.  For one entry `z in V_0` and one source
state `S`, let

```text
n_z(S)
```

be the number of source blocker pairs counted by `z`; equivalently, the contribution
of `z` to the controller-shadow potential.

Consider source states

```text
S_0,S_1,...,S_H
```

and nested puncture sets

```text
X_0 subseteq X_1 subseteq ... subseteq X_H=F.
```

The entry `z` remains active until the first stage at which its controller is
punctured.

### Proposition PP3aqu -- PROVED

Suppose the controller of `z` is punctured at stage `k`.  Let

```text
Delta_j(z)=n_z(S_j)-n_z(S_(j-1))
```

for every trade stage `j<k` while `z` is active.  Then the complete contribution of
`z` to the chronological potential change, including deletion of `z` at stage `k`,
is

```text
sum_(j<k) Delta_j(z) - n_z(S_(k-1))
=
-n_z(S_0).
```

In particular it is nonpositive and is independent of every intermediate creation,
removal, recreation, or designated-credit choice involving `z`.

#### Proof

The trade contributions telescope:

```text
sum_(j<k) Delta_j(z)
=
n_z(S_(k-1))-n_z(S_0).
```

Puncturing the controller deletes `z` from the active universe and therefore removes
its complete current contribution `n_z(S_(k-1))`.  Subtracting gives
`-n_z(S_0)`. ∎

The same identity holds when several controller values are punctured simultaneously.

## 2. Surviving entries and deleted entries

Write

```text
V_F={z in V_0 : controller(z) notin F}
```

for the final active universe and put

```text
D_0(F)=sum_(z in V_0\V_F) n_z(S_0).
```

Thus `D_0(F)` is the initial controller-shadow mass carried by entries deleted by
the final puncture set.

### Theorem PP3aqv -- PROVED

The complete chronological change of the nested potential satisfies the exact
entrywise identity

```text
Psi_F(S_H)-Psi_(X_0)(S_0)
=
sum_(z in V_F) [n_z(S_H)-n_z(S_0)]
-
D_0(F).
```

Equivalently, using the final-universe insertion and removal terms of PP3aps,

```text
Psi_F(S_H)-Psi_(X_0)(S_0)
=
sum_j (I_j^F-R_j^F)-D_0(F).
```

#### Proof

Partition `V_0` into final surviving entries and deleted entries.  A surviving
entry contributes `n_z(S_H)-n_z(S_0)`.  Proposition PP3aqu gives contribution
`-n_z(S_0)` for every deleted entry.  Sum.  The second formula is PP3aps applied to
`V_F`. ∎

This identity is stronger than comparing `Psi_F(S_H)` only with `Psi_F(S_0)`:
puncturing receives the full initial mass of every deleted entry as additional
chronological credit.

## 3. Deleted-entry histories are automatically favourable

### Corollary PP3aqw -- PROVED

Every insertion, removal, lost designated credit, repeated candidate dependency,
partner stack, future-controller stack, fixed-label stack, and forward dependency
matching supported entirely on entries whose controllers are punctured by the end
of the package has total chronological contribution

```text
-D_0(F)<=0.
```

No stability, disjointness, matching, or degree hypothesis is needed.

#### Proof

All such events are intermediate changes of the quantities `n_z` for deleted
entries.  Proposition PP3aqu cancels those changes entry by entry. ∎

Thus the target-scale dependency structures in PP3apy remain useful as diagnostics
of where final-universe credit disappeared, but they are not independent unpaid
objects in the chronological nested potential.

## 4. Strengthened aggregate payment criterion

Let

```text
I_F=sum_j I_j^F,
R_F=sum_j R_j^F.
```

### Theorem PP3aqx -- PROVED

The complete nested package strictly decreases the chronological potential whenever

```text
I_F < R_F + D_0(F).
```

More quantitatively,

```text
Psi_F(S_H)
<=
Psi_(X_0)(S_0)
-
[R_F+D_0(F)-I_F].
```

#### Proof

Substitute the final-universe dynamic identity into PP3aqv. ∎

The criterion permits final-universe insertion cost to exceed surviving removal
credit, provided the initial mass deleted with the punctured controllers supplies
the difference.

### Corollary PP3aqy -- PROVED

Fix `eta>0`.  If

```text
I_F <= R_F + D_0(F)-eta C
```

for a package credit scale `C`, then the package decreases the chronological
potential by at least `eta C`.

Failure of aggregate payment is therefore exactly the inequality

```text
I_F >= R_F + D_0(F),
```

not the existence of a future-controller dependency graph.

## 5. Current-universe upper bound

At stage `j`, evaluate the exact insertion and removal terms in the post-puncture
active universe `V_(X_j)` and denote them by `I_j^cur,R_j^cur`.

### Proposition PP3aqz -- PROVED

The nested chronological change always satisfies

```text
Psi_F(S_H)-Psi_(X_0)(S_0)
<=
sum_j (I_j^cur-R_j^cur).
```

Hence any package with aggregate current-universe inequality

```text
sum_j I_j^cur < sum_j R_j^cur
```

makes strict global progress, even if no individual stage is paid.

#### Proof

At stage `j`, shrinking the universe from `V_(X_(j-1))` to `V_(X_j)` cannot increase
the potential.  The subsequent trade changes the fixed new-universe potential by
`I_j^cur-R_j^cur`.  Sum the resulting stagewise upper bounds. ∎

This gives a second route that does not mention future dependencies or the final
universe.

## 6. Revised history frontier

### Corollary PP3ara -- PROVED

The future-controller dependency stacks and forward dependency matchings of
PP3apy are no longer independent frontiers.  For a nested puncture package:

1. every entry deleted by a later puncture contributes exactly its negative initial
   blocker mass;
2. all intermediate dynamics on deleted entries are automatically cancelled;
3. strict progress follows from either the final-universe criterion
   `I_F<R_F+D_0(F)` or the aggregate current-universe paid inequality;
4. the only internal numerical obstruction is excessive insertion cost on entries
   whose controllers survive the complete package.

The remaining alternatives are final-surviving insertion concentration or an
external source, pool, endpoint, Hall, alternating, matching, or controller-
preservation failure.

The no-three-in-line conjecture remains unproved.
