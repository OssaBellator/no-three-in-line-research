# Shell collateral-cost budget

`docs/631` shows that six uses of a hypothetical `(1,1,1)` macro reduce the
unweighted active-control count from fifteen to twelve.  This chapter converts
that saving into an exact allowance for geometric repairs and collateral effects.

## 1. Exact overhead region

### Theorem PP3cxz -- PROVED / COLLATERAL BUDGET HALF-SPACE

Let `delta >= 0` be the active-equivalent overhead paid per use beyond unit cost,
and let `C >= 0` be fixed collateral cost per twenty-slot period.  The six-use
schedule has total active-equivalent cost

```text
12 + 6*delta + C.
```

It strictly improves the recorded baseline exactly when

```text
6*delta + C < 3.
```

#### Proof

The frontier point with six macro uses contains six recorded controls and six
new controls.  Replace each new control's unit cost by `1+delta` and add `C`, then
compare with fifteen.  ∎

## 2. Integer repair allowance

### Theorem PP3cya -- PROVED / TWO-CONTROL COLLATERAL LIMIT

At unit macro cost, at most two additional integer active controls may be spent
per period while retaining a strict improvement.  Three additional controls tie
the baseline.

With no fixed collateral cost, the sharp per-use overhead threshold is
`delta=1/2`.

#### Proof

Substitute `delta=0` or `C=0` into `PP3cxz`.  ∎

## 3. Repair-frequency consequence

### Theorem PP3cyb -- PROVED / SUB-HALF REPAIR RATE REQUIREMENT

Across six macro uses, unit repair controls must occur at average rate strictly
below one repair per two uses.  Two repairs per period remain beneficial; three
only tie.

This is a cost condition, not a geometric construction.  A useful clean macro
must still realize incidence `(1,1,1)`, preserve exposed legality, and fit its
startup and collateral corrections inside the displayed strict budget.
