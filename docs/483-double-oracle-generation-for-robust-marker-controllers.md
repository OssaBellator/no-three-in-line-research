# Double-oracle generation for robust marker controllers

`docs/477` generates missing marker actions from exact reduced costs while keeping
the adversarial scenario list fixed.  A geometric controller may have both a
large action catalogue and a large family of local obstruction scenarios.  This
chapter generates whichever side is currently missing.

Let `U` be a finite marker-state set.  State `u` has finite action set `A_u`.
For scenario `s` and protected observable `j`, action `(u,a)` has rational gap
`G_(s,j,u,a)`.  A feasible controller must satisfy all scenario inequalities,
all state simplex equations, and any rational shared-resource budgets.  A
rational linear objective measures resource use.

## 1. Restricted row-and-column master

### Theorem PP3cgf -- PROVED / FINITE RESTRICTED MASTER

Choose action subsets `A'_u subseteq A_u` and a scenario subset `S'`.  The
controller restricted to those actions and scenarios is a finite rational linear
program.  Its primal solution, dual scenario prices, resource prices, and free
state-simplex prices are exact rational certificates for the restricted problem.

#### Proof

Restriction deletes finitely many primal variables and finitely many robust
inequalities from the full rational controller LP.  Standard rational LP
primal--dual theory applies.  A basic optimum and a dual optimum may both be
chosen rational. ∎

## 2. Two exact oracles

### Theorem PP3cgg -- PROVED / ACTION PRICING AND SCENARIO SEPARATION

For a restricted dual solution, the reduced cost of a missing action is its
objective cost minus its priced scenario, resource, and state-simplex
contributions.  A negative reduced cost is an exact improving-column witness.

For a restricted primal controller, evaluating every omitted scenario gives its
actual averaged gaps.  A negative gap is an exact violated-row witness.

If neither oracle returns a witness, the restricted primal controller and dual
prices are feasible for the full primal and full dual and have equal objective.
They therefore certify a global optimum.

#### Proof

The reduced-cost statement is the dual feasibility condition for each omitted
column.  The separation statement is direct evaluation of each omitted primal
inequality.  When all omitted dual inequalities and all omitted primal
inequalities hold, the restricted primal and dual extend by zeros to feasible
solutions of the full pair.  Their restricted objectives already agree, so weak
duality forces global optimality. ∎

## 3. Finite double-oracle termination

### Theorem PP3cgh -- PROVED / EXACT DOUBLE-ORACLE TERMINATION

Start from a feasible restricted master, or use standard rational Phase-I artificial
columns until one is obtained.  Repeatedly solve the current restricted master,
add one violated scenario if one exists, otherwise add one negative-reduced-cost
action if one exists.  The procedure terminates after finitely many additions.
At termination it returns a globally optimal rational controller and dual
certificate.  Any earlier stop is accompanied by the explicit missing action or
scenario that invalidates it.

#### Proof

Every unsuccessful iteration adds an action or scenario not previously present.
Both full sets are finite, so only finitely many additions are possible.  The
preceding theorem proves global optimality when both oracles are silent. ∎

## 4. Stored exact fixture

The audit `scripts/check_double_oracle_marker_controllers.py` starts with actions
`{0,1}` and scenario `{0}`.  Its exact trace is

```text
scenario 1 at value 5 with gap -1,
action 2 at value 17/3 with reduced cost -4/3,
action 4 at value 5 with reduced cost -3,
scenario 2 at value 19/4 with gap -3.
```

The final policy on actions `(0,1,2,4)` is `(0,1/2,1/2,0)`, with global value
`5`.  Scenario prices `(1/3,1/2,1/6)` make every remaining action reduced cost
nonnegative, while every scenario gap is nonnegative.

## 5. Prime-patching consequence

Boundary-recleaning synthesis no longer needs either the complete repair-action
catalogue or the complete local-obstruction catalogue in advance.  The finite
certificate contains only the actions and scenarios actually needed, plus exact
oracles proving that no omitted item changes the result.
