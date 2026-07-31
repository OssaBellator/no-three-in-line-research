# Active mixed atoms delete monotonically or become forced certificates

This chapter records CMR2932--CMR2943. CMR2920--CMR2931 generate the exact
fixed-routing child product and prove the strict mixed-clean child handoff. The
present chapter installs the missing CMR677--CMR681 procedure which removes
active nonforced mixed atoms by literal child-edge deletion.

The executable checker is:

```text
scripts/check_prime_power_mixed_child_deletion_ancestry.py
```

## CMR2932 — exact active mixed-atom generation

Starting from a generated fixed-routing child product, the checker enumerates
every product state and every physically collinear labelled triple in original
parent-grid coordinates.

A triple is mixed exactly when its edges belong to more than one generated child
context. It is active exactly when it occurs in at least one generated product
state.

No external mixed-atom list is supplied.

## CMR2933 — exact Cartesian occurrence box

For an active mixed atom `T`, let `T_a` be its edges in child `a`. The checker
filters every child matching family by `T_a` and forms the Cartesian product of
those filtered families.

It proves exact equality with the directly enumerated product states containing
`T`:

\[
\boxed{
\{M\in\mathcal P:T\subseteq M\}
=
\prod_a\operatorname{PM}(H_a;T_a).
}
\]

The box is nonempty exactly for active atoms. This is the executable CMR677
criterion.

## CMR2934 — forced or nonessential split

For every edge of the selected active atom, the checker identifies its unique
routing child and tests whether the edge occurs in every feasible matching of
that child.

Exactly one of the following occurs.

1. Every atom edge is child-essential. Then the occurrence box is the complete
   product and the atom is a forced mixed certificate.
2. At least one atom edge is nonessential. The canonical action chooses the
   first such edge.

This is the literal CMR678 split.

## CMR2935 — exact nonessential-edge deletion transition

In the nonessential branch, the selected child context is replaced by the exact
single-edge deletion child. All other child contexts remain unchanged.

The step record contains:

```text
selected mixed atom
exact occurrence-state count
essential atom edges
selected nonessential edge
selected child index
parent child context
result child context
parent and result product-state counts
active mixed atoms before and after
```

Thus the CMR679 action is represented by an established deleted-edge context
transition inside one product coordinate.

## CMR2936 — matchability preservation and atom destruction

Because the selected edge is nonessential, the reduced child still has a
perfect matching. Since every other factor is unchanged, the complete child
product remains nonempty.

Every occurrence of the selected atom uses the deleted edge, so the atom is
absent from every result product state.

The checker verifies all three statements by complete family generation.

## CMR2937 — deletion cannot activate a mixed atom

Every result child matching was already a matching of the parent child host.
Consequently every result product state was already a parent product state.

The checker proves

\[
\mathcal A_{i+1}\subseteq\mathcal A_i,
\]

where `A_i` is the exact active mixed-atom set after `i` deletions.

No mixed atom is declared new merely because the product family became smaller.

## CMR2938 — strict active-set descent

The selected atom belongs to `A_i` and is destroyed by the selected deletion.
Together with CMR2937 this gives

\[
\boxed{
\mathcal A_{i+1}\subsetneq\mathcal A_i.
}
\]

The checker rejects any deletion step which fails this strict inclusion.

## CMR2939 — finite child-edge stock

The initial available edge stock is computed literally from the generated child
hosts:

\[
E_0=
\sum_a\bigl(d_a^2-|D_a|\bigr).
\]

Every nonterminal step adds one previously undeleted edge to one child mask and
never restores an edge. Hence the procedure has at most `E_0` deletion steps.

The implementation enforces this bound as a hard loop limit.

## CMR2940 — canonical terminal dichotomy

At every iteration choose the least active mixed atom. If it is forced, stop;
otherwise delete the least nonessential atom edge and continue.

The generated procedure terminates in exactly one of:

```text
mixed-clean-product
forced-mixed-certificate
```

In the mixed-clean branch the final active mixed-atom set is empty. In the
forced branch the recorded terminal atom occurs in every final product state.

This is the exact CMR681 terminal dichotomy.

## CMR2941 — forced-certificate scope

The checker proves that the forced terminal atom is active and present in every
final product state. It does not claim the later escape, contraction, routing or
entering-edge payment of CMR643--CMR648.

Therefore it records:

```text
forced_mixed_certificate_escape_proved = 0
```

The certificate itself is exact; its global continuation remains a separate
construction transition.

## CMR2942 — finite mixed-product regression

The checker runs the canonical procedure on every distinct fixed routing
skeleton of the complete binary side-four factor. It records:

```text
18 mixed-product scenarios
4 nonessential mixed-atom deletion steps
17 mixed-clean terminals
1 forced mixed-certificate terminal
7 rejected malformed or corrupted cases
```

Both terminal branches occur. Every deletion preserves a nonempty product,
destroys its selected atom and strictly decreases the active mixed-atom set.

The contract digest is:

```text
b49c1313b765fc63676aed96bfbb91adf52f17293feb47089cfc8129b42b7429
```

## CMR2943 — T02 consequence and honesty boundary

The complete fixed-routing child-product execution now has exact construction
ancestry through:

```text
fixed-routing-child-product-split
mixed-atom-nonessential-edge-deletion
mixed-clean-strict-child-handoff
forced-mixed-certificate terminal
```

The deletion branch has a literal finite child-edge stock. The mixed-clean dirty
branch has strict factor-side and prefix-envelope descent. The forced terminal
certificate is exact but its escape transition is not yet installed.

The permanent boundary is:

```text
factor_product_construction_ancestry_proved = 1
mixed_atom_deletion_ancestry_proved = 1
mixed_clean_child_handoff_ancestry_proved = 1
forced_mixed_certificate_escape_proved = 0
all_construction_ancestry_proved = 0
global_transition_kind_bank_exhaustive = 0
global_termination_proved = 0
actual_global_parent_rule_complete = 0
all_n_proved_by_checker = 0
```

Owner changes, closure-envelope transitions, restoration, returned-edge,
target-handoff, scheduler and forced-certificate escape operations remain open.
No all-`n` theorem or downstream population/chamber/final implication is claimed.
