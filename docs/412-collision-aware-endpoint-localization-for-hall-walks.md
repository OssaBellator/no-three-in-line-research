# Collision-aware endpoint localization for Hall walks

`docs/406` represents every finite-depth Hall ratio as the expectation of the
raw congestion ratio at the endpoint of an inhomogeneous backward overlap walk.
It also gives a lower bound on the endpoint mass carried by raw-high sources.
This chapter converts that mass into a lower bound on the number of distinct
high endpoints, using either endpoint collision probability or path
multiplicity.

The statements are general.  They do not prove anti-concentration for the
prime-patching overlap walk.

## 1. Endpoint collision energy

Fix a root `x` and depth `t`.  Let

```text
mu(z)=P_x(Z_0=z)
```

be the endpoint distribution from `PP3bxi`, and define its collision energy

```text
chi=sum_z mu(z)^2
   =P_x(Z_0=Z'_0),
```

where `Z_0,Z'_0` are independent endpoints of two backward walks from the same
root.

Let

```text
M=max_z r_0(z),
H_theta={z:r_0(z)>theta}.
```

### Theorem PP3bxz -- PROVED / COLLISION-AWARE HIGH-ENDPOINT COUNT

Fix `theta<C<=M`.  If

```text
r_t(x)>=C,
```

then

```text
|H_theta intersect supp(mu)|
 >= [(C-theta)/(M-theta)]^2 / chi.
```

Equivalently, the integer cardinality is at least the ceiling of the right-hand
side.

#### Proof

By `PP3bxi`, the endpoint mass

```text
p=mu(H_theta)
```

satisfies

```text
p>=(C-theta)/(M-theta).
```

Cauchy--Schwarz on the high endpoint set gives

```text
p^2
 =(sum_(z in H_theta) mu(z))^2
 <=|H_theta intersect supp(mu)|
   sum_(z in H_theta) mu(z)^2
 <=|H_theta intersect supp(mu)| chi.
```

Rearrange and insert the lower bound for `p`. ∎

Thus a failed Hall certificate cannot concentrate on only a few raw-congestion
sources unless two independent backward walks have a substantial collision
probability.

## 2. Maximum endpoint atom

Put

```text
beta=max_z mu(z).
```

### Corollary PP3bya -- PROVED / ATOM-CAPPED ENDPOINT MULTIPLICITY

Under the hypotheses of `PP3bxz`,

```text
|H_theta intersect supp(mu)|
 >=(C-theta)/[beta(M-theta)].
```

Also

```text
chi<=beta,
```

so the collision-energy theorem gives the weaker but sometimes more directly
auditable bound

```text
|H_theta intersect supp(mu)|
 >=[(C-theta)/(M-theta)]^2/beta.
```

#### Proof

The high endpoint mass is at least

```text
p=(C-theta)/(M-theta).
```

Each high endpoint carries mass at most `beta`, so at least `p/beta` endpoints
are needed.  Finally

```text
chi=sum_z mu(z)^2<=beta sum_z mu(z)=beta.
```

∎

The first estimate is strongest when a direct bound on the largest endpoint
atom is available.

## 3. From path multiplicity to endpoint atoms

For each positive-probability backward path

```text
omega=(x_t,x_(t-1),...,x_0),
```

write `p(omega)` for its probability.  Assume

```text
p(omega)<=q_path
```

for every path and that at most `N_path` positive-probability paths end at one
fixed source.

### Theorem PP3byb -- PROVED / BOUNDED-PATH-MULTIPLICITY LOCALIZATION

One has

```text
beta<=N_path q_path.
```

Consequently a depth-`t` ratio at least `C` forces at least

```text
(C-theta)
/[N_path q_path (M-theta)]
```

distinct raw endpoints with ratio greater than `theta`.

If every backward transition atom is at most `b_i` at level `i`, then one may
take

```text
q_path<=product_(i=1)^t b_i.
```

#### Proof

The endpoint mass at `z` is the sum of the probabilities of all paths ending at
`z`.  There are at most `N_path` such paths, each of mass at most `q_path`, so
`mu(z)<=N_path q_path`.  Apply `PP3bya`.  The final assertion follows by
multiplying the transition probabilities along a path. ∎

This gives a concrete new Hall frontier: either the backward overlap walk
spreads onto many raw-congestion sources, or many bounded-depth paths merge at
the same endpoint.  The latter is itself a finite collision pattern suitable
for geometric classification.

## 4. Finite diagnostic

Run

```bash
python scripts/check_hall_endpoint_collision_localization.py
```

The checker uses exact rational arithmetic on the stored three-source overlap
system, enumerates all backward paths through depth six, and verifies the
collision-energy, maximum-atom, and path-multiplicity bounds at every nontrivial
threshold.

The next theorem identifier after this chapter is `PP3byc`.
