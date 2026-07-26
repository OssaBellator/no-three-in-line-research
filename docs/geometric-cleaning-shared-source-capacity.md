# Aggregate private capacity and shared target-link payment

**Branch:** `research/geometric-cleaning`

GC2o--GC2r pay a latent partner when one partner-private destroyed factor is
large enough.  Two natural residuals remain: several smaller private factors may
jointly have enough capacity, and target-common factors must be shared across
all partners rather than charged independently.

This note installs both fractional source maps.  Aggregate partner-private
capacity pays with the same rank loss as the single-factor theorem.  The common
target link pays with no rank loss because every factor containing the removed
target is destroyed by every correction in the fixed-target family.

## Fixed-target source pools

Fix a current target cell `b`, distinct partners `u in U`, and rectangle
corrections `T_u` removing `b,u`.  Partner `u` has latent weight `lambda_u`.
Every current destroyed factor contains `b` or `u`.

Let `P_u` be the set of partner-private factors for `u`:

- `u in Q`;
- `b notin Q`.

Let

`C_u=sum_(Q in P_u) omega_Q`.

Let `F_b` be the current factors containing `b`, with shared target-link
capacity

`C_b=sum_(Q in F_b) omega_Q`.

All factors have rank at most `r`.

## GC2s -- aggregate partner-private transfer -- PROVED

Fix `kappa>=1`.  Suppose every retained partner satisfies

`lambda_u <= kappa*C_u`.

For `Q in P_u`, define the fractional payment

`a_(u,Q) = lambda_u*omega_Q/(r*kappa*C_u)`.

Then:

1. partner `u` sends total payment `lambda_u/(r*kappa)`;
2. every current factor `Q` receives total payment at most `omega_Q`;
3. the total paid mass is `sum_u lambda_u/(r*kappa)`.

### Proof

Summing the displayed allocation over `Q in P_u` gives the partner total.
If `Q in P_u`, then `u` is a cell of `Q`.  Distinct partners are distinct cells,
so at most `r` partners have `Q in P_u`.  For each such partner,

`a_(u,Q) <= omega_Q/r`

by `lambda_u<=kappa*C_u`.  Therefore the total load on `Q` is at most
`omega_Q`. QED.

Thus the previous requirement for one individually dominant private factor can
be replaced by dominance by the full private source pool.

## GC2t -- the target-common pool is shared by every correction -- PROVED

Every factor `Q in F_b` is destroyed by every correction `T_u` in the
fixed-target family.

If a retained target-common partner family has total latent weight

`W_b=sum_u lambda_u <= kappa*C_b`,

define

`a_(u,Q)=lambda_u*omega_Q/(kappa*C_b)`.

Then partner `u` sends `lambda_u/kappa`, every target-common factor receives at
most its capacity, and the total paid mass is `W_b/kappa`.

### Proof

Every correction deletes `b`, so every current factor containing `b` is
destroyed by every correction.  For one factor `Q`, its total received load is

`omega_Q*W_b/(kappa*C_b) <= omega_Q`.

Summing over factors gives each partner and global total. QED.

The common target link must be treated as one shared pool.  This proportional
allocation is exactly the capacity-safe replacement for independent per-partner
charges.

## Aggregate eligibility roles

Fix `kappa>=1`.  Classify every partner canonically:

1. **source-free:** no current factor is destroyed;
2. **target-only:** destroyed factors exist but `P_u` is empty;
3. **aggregate-private eligible:** `P_u` is nonempty and
   `lambda_u<=kappa*C_u`;
4. **aggregate-private underweight:** `P_u` is nonempty and
   `lambda_u>kappa*C_u`.

These four roles partition the partner family.

## GC2u -- shared-capacity source router -- PROVED

Let total latent weight be `W`.  One of the following occurs.

1. Aggregate-private eligible partners carry at least `W/4` and give
   factor-conservative payment at least `W/(4r*kappa)` by GC2s.
2. Source-free partners carry at least `W/4`.
3. Aggregate-private underweight partners carry at least `W/4`.
4. Target-only partners carry weight `W_b>=W/4`; then either
   `W_b<=kappa*C_b` and GC2t pays `W_b/kappa>=W/(4kappa)`, or
   `W_b>kappa*C_b` and the exact target-link overload ratio exceeds `kappa`.

### Proof

The four role weights sum to `W`, so one is at least `W/4`.  Apply GC2s or
GC2t in the payable roles.  In the final target-only case, failure of the
aggregate dominance inequality is exactly the displayed overload. QED.

## GC2v -- corrected latent-source frontier -- PROVED

The current source-transfer residuals are now exact.

- Individual or aggregate partner-private capacity pays with rank loss `r` and
  local dominance loss `kappa`.
- Target-common capacity is one shared pool and pays with loss `kappa` whenever
  its aggregate dominance inequality holds.
- Failure is either genuinely source-free, aggregate-private underweight, or an
  explicit target-link overload `W_b/C_b>kappa`.

The next theorem should turn these two quantitative overloads into geometric
structure or show that their total mass is small.  No additional source-map
problem remains when either aggregate dominance condition holds.

## Finite check

`scripts/verify_geometric_shared_source_capacity.py` exhausts small abstract
rank-bounded partner-factor incidence systems.  It checks proportional private
allocation, rank reuse, shared target-link allocation, the four-way router and
the exact overload alternatives.
