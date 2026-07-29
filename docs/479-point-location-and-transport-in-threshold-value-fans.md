# Point location and transport in threshold value fans

`docs/473` proves that the threshold optimum has a monodromy-free rational value
atlas.  This chapter gives exact point-location, segment traversal, and local
sensitivity certificates for using that atlas as an oracle.

Let

```text
V(theta)=max_(z in Z) (a_z dot theta+b_z)
```

for a finite rational set of dual vertices `Z`.

## 1. Exact point location

### Theorem PP3cft -- PROVED / ACTIVE-DUAL POINT-LOCATION CERTIFICATE

For rational `theta`, evaluating the finitely many affine pieces exactly returns

```text
A(theta)={z: a_z dot theta+b_z=V(theta)}.
```

The active set is a complete point-location certificate.  A unique active vertex
identifies the open value cell and its gradient; multiple active vertices identify
a rational wall or higher-codimension face.

#### Proof

The value is the maximum of the listed rational numbers.  Equality with that
maximum is exactly the definition of activity.  The cell inequalities are the
pairwise dominance inequalities against all other pieces. ∎

## 2. Exact segment walk

### Theorem PP3cfu -- PROVED / RATIONAL VALUE-FAN SEGMENT SUBDIVISION

Along a rational segment `theta(t)=theta_0+t d`, every affine piece becomes a
rational line in `t`.  Sorting the finitely many pairwise intersection parameters
in `[0,1]` and testing one rational midpoint in each interval gives the exact
ordered sequence of value cells.  Summing the active gradients over these
subsegments gives exactly

```text
V(theta(1))-V(theta(0)).
```

The procedure terminates after finitely many wall crossings and returns one
rational crossing witness for every cell change.

#### Proof

The upper envelope of finitely many lines can change only at pairwise
intersections.  Between consecutive intersections, their strict order is
constant, so one midpoint identifies the active line.  The value is affine on
each such interval, and the finite differences telescope. ∎

## 3. Directional and Lipschitz prices

### Theorem PP3cfv -- PROVED / ACTIVE-GRADIENT SENSITIVITY

For every direction `h`, the one-sided directional derivative is

```text
D V(theta;h)=max_(z in A(theta)) a_z dot h.
```

For any norm with dual norm `||.||_*`, the global bound

```text
|V(theta')-V(theta)|
 <= [max_z ||a_z||_*] ||theta'-theta||
```

holds.  Thus the finite gradient list is an exact local sensitivity certificate
and a global perturbation envelope.

#### Proof

Inactive affine pieces have a strictly smaller value and cannot overtake at
first order for sufficiently small positive step.  The active pieces therefore
determine the directional maximum.  For the Lipschitz bound, compare the same
affine piece at the two points and apply dual-norm Hölder inequality in both
directions. ∎

## 4. Stored exact fixture

The audit `scripts/check_threshold_value_fan_point_location.py` uses

```text
V(x,y)=max(x,y,-x+y,-x,-y,x-y).
```

It checks exact active sets on a `41 x 41` rational grid: 1,681 points, 13 distinct
active sets, and 121 wall or vertex points.  The segment

```text
(-2,-1)+t(4,5/2)
```

crosses walls at `t=2/5,1/2,2/3` and visits the cells `-x`, `-x+y`, `y`, `x`.
At the origin, direction `(2,-1)` has derivative three.  The exact global
`l_infinity` Lipschitz constant is two.

## 5. Prime-patching consequence

A threshold kernel can now be queried and transported through a precomputed dual
atlas without resolving the LP at every nearby geometry.  Active gradients give
both the exact next wall and a rigorous load-sensitivity reserve.
