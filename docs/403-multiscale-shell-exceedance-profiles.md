# Multiscale shell exceedance profiles

`docs/390` controls shell products from total positive excess, while `docs/395`
controls them from one ceiling and the number of expansive boundaries.  This
chapter gives the common multiscale form: a complete exceedance-count profile
bounds the positive shell product.  Contractive shells remain available as an
exact multiplicative credit.

The statements do not establish any geometric exceedance profile for the clean-
macro shells.

## 1. Exact logarithmic layer cake

Let the nonterminal adjacent-shell norms be

```text
kappa_1,...,kappa_r>0.
```

Put

```text
p_j=max(kappa_j,1),
c_j=min(kappa_j,1),
Cprod=product_j c_j.
```

For `u>=1`, define the exceedance count

```text
q(u)=#{j:p_j>u}.
```

### Theorem PP3bwv -- PROVED / EXACT SHELL-TAIL LAYER CAKE

One has

```text
log(product_j p_j)
 = integral_(1)^infinity q(u) du/u.
```

Consequently the complete trajectory with terminal factor `tau<1` contracts
exactly when

```text
log(tau Cprod)
 + integral_(1)^infinity q(u) du/u
 <0.
```

#### Proof

For one factor `p>=1`,

```text
log p=integral_(1)^p du/u
     =integral_(1)^infinity 1_{p>u} du/u.
```

Sum over the finite set of shell factors and interchange the finite sum and
integral.  Since

```text
product_j kappa_j=Cprod product_j p_j,
```

the contraction criterion follows after taking logarithms. ∎

This is the exact continuous interpolation between total-excess and bad-shell
counting arguments.

## 2. Rational multiscale envelope

Choose thresholds

```text
1=B_0<B_1<...<B_s
```

and assume every positive shell factor satisfies `p_j<=B_s`.  Put

```text
q_i=#{j:p_j>B_i}
```

for `0<=i<s`.

### Theorem PP3bww -- PROVED / DISCRETE MULTISCALE SHELL PRODUCT

The positive shell product obeys

```text
product_j p_j
 <= product_(i=0)^(s-1)
    (B_(i+1)/B_i)^(q_i).
```

Hence the full trajectory contracts whenever

```text
tau Cprod
 product_(i=0)^(s-1)
 (B_(i+1)/B_i)^(q_i)
 <1.
```

#### Proof

For one factor `p_j`, let `h` be the largest index with `p_j>B_h`, taking
`h=-1` when `p_j=1`.  Since `p_j<=B_s`,

```text
p_j<=product_(i=0)^h B_(i+1)/B_i.
```

Multiply this inequality over `j`.  The ratio at level `i` appears once for each
factor exceeding `B_i`, namely `q_i` times.  Multiply by the exact contractive
credit and terminal factor. ∎

With only `B_0=1<B_1=B`, this is `PP3bvv`.  Refining the threshold list can only
improve the envelope and converges to the exact layer-cake value.

## 3. Strong-shell count plus mild excess

Fix `B>1`.  Split the expansive factors into

```text
S={j:kappa_j>B},
M={j:1<kappa_j<=B}.
```

Assume `|S|<=q`, every strong factor is at most `C`, and put

```text
E_M=sum_(j in M)(kappa_j-1),
r_M=|M|.
```

### Corollary PP3bwx -- PROVED / HYBRID STRONG-COUNT AND MILD-EXCESS BOUND

For `r_M>0`,

```text
product_j kappa_j
 <= Cprod C^q (1+E_M/r_M)^(r_M).
```

For `r_M=0`, omit the final factor.  Thus contraction follows when the right-hand
side, multiplied by `tau`, is below one.

#### Proof

Strong factors contribute at most `C^q`.  Apply AM--GM to the `r_M` mild factors,
whose total positive excess is `E_M`, exactly as in `PP3bvg`.  Multiply by the
contractive factors. ∎

This allows a few severe gates, a diffuse mild excess budget, and exact
compensation from contractive boundaries in one criterion.

## 4. Converting a decreasing invariant into a bad-shell bound

### Corollary PP3bwy -- PROVED / INVARIANT-DROP SHELL COUNT

Suppose a nonnegative shell invariant `J_i` never increases along a trajectory
and every boundary with

```text
kappa_i>B
```

forces

```text
J_i-J_(i+1)>=eta>0.
```

Then the number of such boundaries is at most

```text
floor(J_0/eta).
```

If all shell norms are at most `C`, the corresponding strong-boundary product is
at most

```text
C^(floor(J_0/eta)).
```

and may be inserted into `PP3bww` or `PP3bwx`.

#### Proof

Sum the invariant drops over all strong boundaries.  Their total is at least
`q eta` and at most `J_0`, because the invariant is nonnegative and never
increases.  Rearrangement gives the count. ∎

## 5. Revised shell frontier

The shell branch now admits four levels of information:

1. the exact compensated product;
2. the exact exceedance-tail integral;
3. a finite rational threshold profile;
4. a hybrid of a bounded number of severe gates and AM--GM control of mild
   expansion.

A geometric invariant need not bound every shell norm uniformly.  It is enough
to control how often each expansion scale occurs.

## 6. Finite diagnostic

The script

```bash
python scripts/check_multiscale_shell_exceedance.py
```

exhausts 1,296 rational four-boundary profiles and checks both the discrete
multiscale envelope and the hybrid strong-count/mild-excess bound exactly.

The next theorem identifier after this chapter is `PP3bwz`.
