# Alternative-target menus and exact owner accounting

**Branch:** `research/alternating-core-chain`

AC3ji--AC3jm return many missing alternatives of one blocker row or inverse
blocker column.  Their residual hard-check scopes may be disjoint, share one
current literal, or have one owner token.  Those alternatives are not
simultaneous values of the permutation variable.  They form a finite menu: one
target value and its complete correction are selected at a time.

This note gives the exact installation and payment contract.  It prevents two
opposite errors:

- requiring different target alternatives to be mutually compatible even
  though only one is chosen;
- summing common or private owner payment across alternatives as though all
  were installed simultaneously.

## Per-target complete states

Fix one current two-layer state `S`, one blocker permutation variable `v`, and a
finite target set `A`.  For each `a in A`, a **complete target state** `S_a`
consists of:

1. the centre assignment `v=a`;
2. every auxiliary residual change needed to discharge the selected hard
   reason;
3. a complete active and blocker permutation state;
4. all opposite-layer repairs;
5. an AC3v envelope containing every touched hard scope, soft factor,
   replacement cell, protected contract and paid set;
6. exact reverse-ticket and owner-status records.

Different states `S_a` may overlap arbitrarily.  They are alternatives, not
factors of one product state.

Let `D_0` be a common set of current paid tokens destroyed by every `S_a`.  Let
`D_a` be a private paid set destroyed only in state `S_a`, with

\[
D_0\cap D_a=\varnothing.
\]

No disjointness between `D_a` and `D_b` is needed for menu legality because
`S_a` and `S_b` are never selected together.  Exact payment in one state is
always the weight of the set union `D_0 union D_a`, so duplicate token names
inside that state are counted once.

## AC3ki -- complete alternatives form a legal finite menu -- PROVED

If every `S_a` is a complete target state, then

\[
\mathcal M=\{S_a:a\in A\}
\]

is one legal finite menu.  No pairwise compatibility assumption between
`S_a` and `S_b` is required.

Every target which lacks a complete state is not a menu state.  A residual
scope, owner name, prospective BDA/RI formula, or reopened Hall edge is not
promoted to a legal transition until all six completion conditions above are
proved.

### Proof

A menu selects one index `a` and installs only `S_a`.  Its legality is exactly
the per-target legality in the definition.  Interactions between two distinct
alternatives never occur in one selected state.  The final statement is the
scope-complete legality requirement of AC3v together with AC3jw's owner-payment
criterion. QED.

## AC3kj -- exact common/private menu payment -- PROVED

Let `mu` be any probability law on `A`.  Write

\[
D_0=w(D_0),
\qquad
D_a=w(D_a\setminus D_0).
\]

Then

\[
\boxed{
\mathbb E_\mu[\text{destroyed certified payment}]
=
D_0+\sum_{a\in A}\mu(a)D_a.
}
\]

In particular:

1. one common pivot or same-owner token is counted once in every selected
   state, not `|A|` times;
2. private owners belonging to different alternatives contribute their
   probability-weighted average, not their total sum;
3. under the uniform law on `m=|A|` targets,
   \[
   \boxed{
   \mathbb E[\text{payment}]
   =D_0+\frac1m\sum_aD_a;
   }
   \]
4. some one target has private payment at least
   \[
   \boxed{
   \max_a D_a
   \ge
   \frac1m\sum_aD_a.
   }
   \]

### Proof

For one selected state the exact paid token set is `D_0 union D_a`.  The common
and private sets are disjoint after removing common tokens from `D_a`, so its
weight is `D_0+D_a`.  Average over `mu`.  The uniform identity and maximum-at-
least-average inequality follow immediately. QED.

## Created collateral

For state `S_a`, let `C_{a,r}` be the exact created union-collateral weight of
new-cell rank `r=1,2,3`, measured relative to the common parent state `S`.
AC3fa partitions all genuinely new triples into these three ranks.

## AC3kk -- alternative-menu comparison and rank return -- PROVED

Under any law `mu`, put

\[
D_\mu
=
D_0+\sum_a\mu(a)D_a,
\qquad
C_{\mu,r}
=
\sum_a\mu(a)C_{a,r}.
\]

Then

\[
\boxed{
\mathbb E_\mu[\Phi(S_a)-\Phi(S)]
=
(C_{\mu,1}+C_{\mu,2}+C_{\mu,3})-D_\mu.
}
\]

If

\[
D_\mu>C_{\mu,1}+C_{\mu,2}+C_{\mu,3},
\]

one menu state improves.  If no menu state improves, one rank satisfies

\[
\boxed{C_{\mu,r}\ge D_\mu/3.}
\]

After selecting a state realizing that rank expectation, AC3gg--AC3gm orient it
to a union-safe pivot bucket.  For every pivot extraction parameter `K>=1`, the
usual alternatives give payment at least

\[
\boxed{D_\mu/(3K)}
\]

or a next-rank return at least

\[
\boxed{D_\mu/(9K)},
\]

unless an explicit overload or improving state occurs.

### Proof

Apply the exact created-minus-destroyed identity separately to each complete
state and average.  If the average is negative, one summand is negative.  If
no summand is negative, total expected creation is at least `D_mu`; one of
three ranks carries at least one third.  The final statement is the established
expectation-realization and all-rank pivot interface. QED.

## AC3kl -- centred fan accounting guardrails -- PROVED

Apply AC3ki--AC3kk to the five AC3jl records.

1. **Unconditional target stock.**  An unconditional hard exclusion is not a
   legal target state and has zero payment.  It is a finite forbidden-target
   stock unless another transition changes the hard context.
2. **Common residual literal.**  Sharing a residual literal does not create a
   paid menu.  Each target still needs one complete correction state; a current
   charging token attached to the common literal is counted once per selected
   state.
3. **Support-disjoint residual arms.**  Disjointness across different target
   alternatives is a dispersion certificate, not a simultaneous product.
   Once each arm is completed separately, the resulting states form a menu.
4. **Same-owner fan.**  One shared current owner contributes its weight once in
   each state.  The fan size does not multiply that payment.
5. **Many-owner star.**  Different owners on different alternatives contribute
   through `sum mu(a)D_a`; under a uniform menu this is their average.  A
   deterministic selection may retain the heaviest owner, at least the average.

Prospective target-containing BDA/RI/carry geometry contributes zero destroyed
payment in every case by AC3jv--AC3jz.

### Proof

The first three statements are the distinction between hard feasibility,
per-target completion and alternative-state menus.  The last two are the exact
identity AC3kj.  AC3jv excludes prospective payment. QED.

## AC3km -- exact installation frontier for centred target fans -- PROVED

For one centred AC3jl target fan, partition target values into:

- `A_exec`: targets with complete states satisfying AC3ki;
- `A_forbid`: unconditional hard exclusions in the fixed context;
- `A_reset`: targets whose attempted completion changes an outer profile field;
- `A_open`: targets still lacking a complete correction theorem.

Then:

1. `A_exec` forms the paid or unowned menu of AC3ki--AC3kk;
2. `A_forbid` is a finite forbidden-target stock and has no payment;
3. every member of `A_reset` is a decorated outer edge for AC3ka--AC3kd;
4. `A_open` is the exact remaining local installation obligation.

No other unstructured target-fan output remains.  In particular, residual-arm
or owner-star cardinality alone is not an installation theorem.

### Proof

The four classes are defined by exhaustive tests in the displayed order:
complete state, unconditional exclusion, outer-profile change, or unresolved
completion.  The preceding theorems give the route for each class. QED.

## Consequence

The centred literal/owner frontier is now payment-safe.  Executable alternatives
form one finite common-parent menu and feed the universal rank fallback.
Unconditional exclusions remain unowned hard constraints.  Outer changes enter
the finite macro quotient.  The unresolved local work is exactly to construct
complete states for `A_open`, not to reinterpret fan size as simultaneous
payment.

## Finite check

`scripts/verify_ac_alternative_target_menu.py` exhausts finite menus with shared
and private owner sets, arbitrary probability laws, duplicate-token removal,
created-rank ledgers, no-improvement rank returns and every AC3jl guardrail.
