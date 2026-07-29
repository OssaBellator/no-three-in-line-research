# Target hubs and dyadic codegree fans for direct-clean failure

`docs/401` shows that failure of fractional direct-clean expansion forces one
source with large total codegree load.  This chapter converts that load into
two concrete collision objects: a single highly reused target and a
single-scale fan of sources sharing comparable numbers of targets with the
root.

The statements are general.  They do not yet prove that either collision
object yields an additional clean repair action.

## 1. Codegree load as target multiplicity

For a source subset `A`, write

```text
m_A(y)=#{x in A:y in N(x)}
```

and, for `x in A`,

```text
L_A(x)=sum_(x' in A, x'!=x) codeg(x,x').
```

### Proposition PP3bxj -- PROVED / ROOTED CODEGREE-MULTIPLICITY IDENTITY

For every `x in A`,

```text
L_A(x)=sum_(y in N(x))(m_A(y)-1).
```

Consequently some target `y in N(x)` satisfies

```text
m_A(y)>=1+L_A(x)/d(x).
```

When the right side is not integral, the sharper integer form is

```text
m_A(y)>=1+ceil(L_A(x)/d(x)).
```

#### Proof

Expand each codegree and interchange sums:

```text
sum_(x'!=x)|N(x) intersect N(x')|
 =sum_(y in N(x))
   #{x' in A\{x}:y in N(x')}
 =sum_(y in N(x))(m_A(y)-1).
```

The average of `m_A(y)-1` over the `d(x)` targets in `N(x)` is
`L_A(x)/d(x)`, so one target is at least the ceiling of that average. ∎

Thus total pair overlap is exactly excess target multiplicity as seen from the
root source.

## 2. Expansion failure forces a target hub

### Theorem PP3bxk -- PROVED / DIRECT-CLEAN FAILURE TARGET HUB

Suppose a nonempty source set `A` violates the reverse-load bound `rho`.
Write

```text
bar_d_A=(1/|A|)sum_(x in A)d(x).
```

Then there are a source `x in A` and target `y in N(x)` such that

```text
m_A(y)
 >1+(rho bar_d_A^2-bar_d_A)/d(x).
```

If every degree in `A` lies in `[d,D]`, then

```text
m_A(y)>1+(rho d^2-d)/D.
```

In the `d`-regular case this simplifies to

```text
m_A(y)>rho d.
```

#### Proof

By `PP3bwr`, some root `x` satisfies

```text
L_A(x)>rho bar_d_A^2-bar_d_A.
```

Apply `PP3bxj` and divide by `d(x)`.  Under the degree window,
`bar_d_A>=d` and `d(x)<=D`; when `rho d^2-d` is negative the displayed
bound is automatic, while otherwise the function `rho z^2-z` is increasing
for the relevant range exactly as in `PP3bwr`.  The regular specialization is
immediate. ∎

A bad Hall subset therefore contains a literal reverse-column collision:
many sources reach one common clean target.

## 3. Dyadic common-target fans

Let the positive internal codegrees from a fixed root be

```text
c(x')=codeg(x,x')>0.
```

Put

```text
J=1+floor(log_2 d(x))
```

and for `0<=j<J` define

```text
F_j(x)
 ={x' in A\{x}:2^j<=c(x')<2^(j+1)}.
```

### Theorem PP3bxl -- PROVED / SINGLE-SCALE CODEGREE FAN

Some dyadic level `j` satisfies

```text
2^j |F_j(x)|>L_A(x)/(2J).
```

Equivalently,

```text
|F_j(x)|>L_A(x)/(2J 2^j),
```

and every source in this fan shares at least `2^j` targets with the root.

Combining with expansion failure, one root and one scale obey

```text
2^j |F_j(x)|
 >(rho bar_d_A^2-bar_d_A)/(2J).
```

#### Proof

Every positive codegree is at most `d(x)` and belongs to exactly one dyadic
class.  For `x' in F_j(x)`,

```text
c(x')<2^(j+1).
```

Hence

```text
L_A(x)
 =sum_j sum_(x' in F_j)c(x')
 <2 sum_j 2^j |F_j(x)|.
```

One of the `J` summands is therefore greater than `L_A(x)/(2J)`.  Insert the
load supplied by `PP3bwr` for the failure form. ∎

This removes the remaining multiscale ambiguity from the codegree core:
after a logarithmic loss, many sources share comparable numbers of targets
with one fixed source.

## 4. Revised fractional-layer frontier

Failure of the sparse-codegree criterion now has two simultaneous
localizations:

1. a target hub with high source multiplicity;
2. a root source with a dyadic fan of comparably overlapping neighbours.

The next repair-layer construction can attack either a highly reusable target
directly or use the common-target fan to manufacture additional
target-disjoint actions.

## 5. Finite diagnostic

The script

```bash
python scripts/check_direct_clean_target_hubs.py
```

exhausts every source subset of a stored action graph and checks the rooted
codegree identity, the strongest target hub, and all dyadic fan inequalities.

The next theorem identifier after this chapter is `PP3bxm`.
