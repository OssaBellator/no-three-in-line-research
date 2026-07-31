# Profile-sliced existence for prefix risk

The prefix row in `docs/543--548` needs one legal support-chord object satisfying
several support and risk restrictions simultaneously.  `docs/534` and `docs/540`
count the legal objects by profile.  This chapter turns those counts into a
deterministic existence certificate from aggregate bad-incidence data.

Let `F` be one finite profile slice of legal prefix trees, and let
`r_1,...,r_s:F->Z_>=0` be nonnegative integer risk scores.

## 1. Exact simultaneous-risk certificate

### Theorem PP3coe -- PROVED / PROFILE-SLICED RISK UNION BOUND

Fix positive integer thresholds `T_k` and total risk budgets

```text
R_k=sum_(x in F) r_k(x).
```

The number of objects with `r_k(x)>=T_k` is at most `floor(R_k/T_k)`.  Therefore,
if

```text
sum_k floor(R_k/T_k)<|F|,
```

there exists an object satisfying `r_k(x)<T_k` for every `k`.  Moreover, at least

```text
|F|-sum_k floor(R_k/T_k)
```

objects satisfy all restrictions.

#### Proof

Each violating object contributes at least `T_k` to `R_k`, giving the individual
count bound.  The union bound over the violating sets gives the simultaneous
statement. ∎

## 2. Entropy reserve against sparse bad families

### Theorem PP3cof -- PROVED / CENTRAL-PROFILE ABUNDANCE RESERVE

For the legal prefix-tree family of `docs/534`, every central profile
`j=n/3+O(sqrt(n))` has size

```text
exp(n log 3-O(log n)).
```

Consequently, any fixed number of bad families whose total sizes are
`exp((log 3-delta)n)` for some `delta>0` leave a legal central-profile object for
all sufficiently large `n`.  The same conclusion holds for polynomially many
bad families of polynomial size.

#### Proof

`PP3cmv` gives a local Gaussian probability of order `n^(-1/2)` in the central
window, while the total family has exponential growth constant three.  Hence a
central profile has the displayed size.  The proposed bad-family totals are
exponentially smaller, so their union cannot cover the profile. ∎

## 3. Weighted ledger consequence

### Theorem PP3cog -- PROVED / PREFIX RISK-ROW ADAPTER

Suppose an object accepted by `PP3coe` has `r_k<T_k`, and nonnegative rational
prices `a_k` convert risk coordinates to ledger loss.  Then its prefix-row loss
is strictly less than

```text
sum_k a_k T_k.
```

Thus exact profile counts, aggregate risk sums, integer thresholds, and a price
vector form a finite certificate for the prefix ledger row.

#### Proof

For the accepted object, multiply each strict coordinate bound by `a_k` and sum. ∎

## 4. Stored exact fixture

The audit `scripts/check_prefix_profile_risk_adapter.py` uses the profile

```text
n=30, j=9,
|F|=168212023980.
```

For four risk coordinates it stores thresholds `(10,10,8,16)` and aggregate
risk totals `(3|F|,2|F|,|F|,|F|)`.  The union certificate leaves at least

```text
52566257495
```

simultaneously acceptable objects.  Every accepted integer risk vector has total
score at most forty; normalizing by 1600 gives the derived prefix row

```text
1/40<1/32.
```

The audit also verifies the exact profile-ratio identity through 100 leaves.

## 5. Prime-patching consequence

The prefix frontier is reduced to an incidence census rather than an explicit
search through an exponential family.  One must bound, over a central legal
profile, the aggregate support, branching, and geometric risk scores required by
the patch.  If those totals satisfy `PP3coe`, existence follows.  The stored risk
census is synthetic and does not yet supply the actual geometric incidence
bounds.
