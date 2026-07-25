# Exact preprocessing of canonical phase cores

Every OP1 check is a canonical **nogood**: on its scope \(N(C)\) it
forbids exactly one partial assignment \(f_C\).  Before applying the
topological solvers OP2a--OP2f or asking for arithmetic Tanner
expansion, these nogoods admit an exact subsumption and unit-propagation
reduction.

Let each variable \(v\) have a nonempty current domain
\(\mathcal A_v\).  An assignment satisfies a check \(C\) exactly when
some \(v\in N(C)\) has \(a_v\ne f_C(v)\).

## OP2g -- canonical antichain/unit core

Apply the following rules to a fixed point.

1. **Satisfied literal.**  If \(f_C(v)\notin\mathcal A_v\) for some
   \(v\in N(C)\), delete \(C\): every current assignment already
   mismatches its forbidden tuple.
2. **Forced matching literal.**  If
   \(\mathcal A_v=\{f_C(v)\}\), delete \(v\) from the scope of \(C\).
   If the scope becomes empty, return unsatisfiable.
3. **Unit nogood.**  If the remaining scope is \(\{v\}\), delete
   \(f_C(v)\) from \(\mathcal A_v\), delete the check, and return
   unsatisfiable if the domain becomes empty.
4. **Subsumption.**  Merge duplicate checks.  If checks \(A,B\) satisfy
   \[
   N(A)\subseteq N(B),
   \qquad
   f_B|_{N(A)}=f_A,
   \]
   delete \(B\).

### Theorem OP2g -- PROVED

The fixed-point procedure terminates and preserves exactly the set of
satisfying assignments.  It either returns a variable with empty domain
as an explicit unsatisfiability certificate, or returns an equivalent
canonical instance with all of the following properties:

- every surviving check has arity at least two;
- every forbidden label of a surviving check remains in its variable
  domain;
- every variable occurrence in a surviving check has domain size at
  least two; and
- the surviving forbidden partial assignments form an antichain under
  extension.

Consequently every residual core passed to OP2a--OP2f or to arithmetic
expansion may be assumed to satisfy these four irreducibility
conditions.

### Proof

Rule 1 deletes a tautologically satisfied check.  Under rule 2 the
removed variable is forced to agree with the forbidden tuple, so it
cannot supply the mismatch that satisfies the check; deleting that
literal is exact.  An empty residual scope says that every forbidden
literal is forced and is therefore an unsatisfiability certificate.

A unary nogood is satisfied exactly when its variable avoids its one
forbidden label, proving rule 3.  For rule 4, every assignment violating
\(B\) also agrees with \(f_A\) on \(N(A)\) and therefore violates
\(A\).  Once \(A\) is retained, \(B\) imposes no additional
restriction.

Every nonterminal application strictly decreases the finite measure

\[
\sum_v|\mathcal A_v|
+\sum_C|N(C)|
+|\mathcal C|.
\]

The process terminates.  Since every rule preserves the satisfying
assignments, induction over the reduction trace proves exact
equivalence.

At a fixed point rule 1 gives the second property.  Rule 2 then gives
the third.  Rule 3 gives the first, and rule 4 gives the antichain
property. \(\square\)

## Consequence for expansion

OP2g removes topological density caused only by repeated or extended
copies of a smaller forbidden pattern.  In particular, high check
degree in the residual Tanner graph must come from genuinely
incomparable canonical tuples, not from redundant supersets.  It also
turns every forced-label cascade into either a smaller exact instance or
an explicit empty-domain obstruction before any treewidth, cactus, or
feedback computation is attempted.

This preprocessing does not prove arithmetic expansion of the
irreducible core.  It sharpens that remaining target to antichain checks
of arity at least two on genuinely nontrivial domains.

`scripts/verify_phase_core_preprocessing.py` compares the complete
satisfying-assignment set before and after reduction for every binary
three-variable check family of size at most three and every nonempty
domain choice.
