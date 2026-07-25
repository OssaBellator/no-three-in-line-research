# Rectangle clause-core regularization

PP3pb leaves heavy geometric-clause variables as one possible obstruction to paid
rectangle selection. The common-line bank has additional structure: its variable
supports are pairwise resource-disjoint, and the adaptive source-validity
preparation gives vanishing density for triples using three distinct variables.

This chapter removes all diffuse ternary clauses. The remaining geometric CSP
obstruction is a dense binary interaction graph or a hard local-state
restriction.

## 1. Unit-clause preprocessing

For one rectangle variable \(s\), let \(A_s\subseteq\{0,1\}\) be the states not
forbidden by unit clauses after the residual source-valid matching is fixed.

### Proposition PP3pc -- PROVED

Exactly one of the following holds for each variable.

1. \(A_s=\varnothing\): the rectangle block is locally impossible.
2. \(|A_s|=1\): the variable may be fixed to its unique allowed state and removed
   from the CSP; its shadow contribution is absorbed into the fixed cost
   \(C_0\) and into unary tables of the remaining variables.
3. \(A_s=\{0,1\}\): the variable remains flexible and has no unit clause.

Fixing variables cannot increase the rank of any remaining clause.

#### Proof

This is direct Boolean restriction. A clause containing a fixed variable is
either satisfied and deleted or loses that literal requirement. Cost tables are
restricted to the fixed state, producing constant or lower-rank tables. ∎

Thus only locally impossible blocks and the cost accumulated by forced blocks are
new obstructions at rank one.

## 2. Binary clause graph

Let \(K\) be the number of flexible rectangle variables. Form a graph \(G_2\) on
these variables, joining \(s,t\) when the restricted formula has at least one
rank-two bad box on \(\{s,t\}\). Duplicate state boxes are ignored.

Let \(N_3\) be the number of distinct rank-three bad boxes on three flexible
variables.

### Proposition PP3pd -- PROVED

For the adaptively prepared common-line bank,

\[
\boxed{N_3=o(K^3)}
\]

whenever \(K=\Omega(q)\).

#### Proof

A rank-three bad box selects a collinear triple containing cells from three
distinct rectangle supports. Such a triple is a support-rank-at-least-four
inserted triple in the endpoint bank. The PP3nr high-support normalized expression
gives \(o(q^3)\) such triples after resource deletion. Every geometric triple
produces at most one distinct bad box after the local state intersections are
formed. Since \(K=\Omega(q)\), the bound is \(o(K^3)\). ∎

No analogous conclusion is asserted for \(G_2\): two-variable clauses may use
two cells of one rectangle and therefore can have quadratic density.

## 3. Adaptive clause-free subbank

### Theorem PP3pe -- PROVED

Assume

\[
K\longrightarrow\infty,
\qquad
|E(G_2)|=o(K^2),
\qquad
N_3=o(K^3).
\]

Then there is a subset \(I\) of flexible variables such that

\[
|I|\longrightarrow\infty
\]

and the formula induced on \(I\) has no clause of any rank.

#### Proof

Put

\[
\eta_2=\dfrac{|E(G_2)|}{K^2}=o(1),
\qquad
\eta_3=\dfrac{N_3}{K^3}=o(1).
\]

Choose an integer \(s\to\infty\) with

\[
s\le K,
\qquad
\eta_2s^2=o(1),
\qquad
\eta_3s^3=o(1).
\]

A uniform \(s\)-subset of variables contains expected binary-clause edges

\[
\dfrac{(s)_2}{(K)_2}|E(G_2)|=o(1)
\]

and expected ternary bad boxes

\[
\dfrac{(s)_3}{(K)_3}N_3=o(1).
\]

Some subset contains neither. Unit clauses were removed in PP3pc, so the induced
formula is clause-free. ∎

Every state assignment on this subbank is source-admissible relative to the fixed
residual matching. The only remaining selection issue is paid shadow cost.

## 4. Dense binary alternative

### Corollary PP3pf -- PROVED

If no growing clause-free flexible subbank exists, at least one of the following
holds.

1. A linear number of rectangle blocks are locally impossible or forced by unit
   clauses.
2. The binary clause graph satisfies
   \[
   |E(G_2)|=\Omega(K^2).
   \]
3. The adaptive high-support triple estimate fails, contrary to PP3nr.

In alternative 2, the binary clause graph contains either:

- one rectangle variable with \(\Omega(K)\) binary-clause neighbors; or
- a matching of \(\Omega(K)\) pairwise variable-disjoint binary conflicts.

#### Proof

If a positive fraction of the original linear rectangle bank is not flexible,
alternative 1 holds. Otherwise \(K=\Omega(q)\), and PP3pd supplies
\(N_3=o(K^3)\). If the binary graph is sparse, PP3pe gives a growing clause-free
subbank. Hence failure forces alternative 2.

For the final dichotomy, greedily take a maximal matching. If its size is
\(\Omega(K)\), use it. Otherwise its endpoints form a sublinear vertex cover of
a graph with \(\Omega(K^2)\) edges, so one cover vertex has
\(\Omega(K)\) neighbors. ∎

The geometric CSP branch is therefore reduced from arbitrary rank-three
satisfiability to a local-state core or a dense binary rectangle-interaction
star/matching. Diffuse ternary interactions are no longer a separate
obstruction.