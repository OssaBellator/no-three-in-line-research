# Multicritical faces for shell rates

`docs/451` treats a unique critical shell cycle. Ties are unavoidable at parameter boundaries. This chapter gives the exact directional derivative and stability face when several simple cycles attain the same optimal rate.

For a simple cycle `C`, let `g_C` be its normalized edge-incidence vector: `g_C(e)` is the multiplicity of edge `e` in `C` divided by `ell_C`. Under a multiplicative perturbation `p_e(t)=p_e exp(t h_e)`,

```text
log mu(t)=max_C [log mu_C(0)+t <g_C,h>].
```

## 1. Directional rate derivative

### Theorem PP3cdf -- PROVED / MULTICRITICAL DIRECTIONAL DERIVATIVE

Let `K` be the set of cycles critical at `t=0`. Then

```text
D_h log mu=max_(C in K) <g_C,h>.
```

#### Proof

Noncritical cycles have a strict intercept deficit and cannot maximize for sufficiently small positive `t`. Among the critical affine functions, the right derivative of their maximum is the largest slope. ∎

The formula is exact and requires no choice of a single critical cycle.

## 2. Subgradient certificate

### Theorem PP3cdg -- PROVED / CRITICAL-CYCLE SUBDIFFERENTIAL

The convex subdifferential of `log mu` in logarithmic edge coordinates is

```text
conv{g_C:C in K}.
```

#### Proof

`log mu` is a finite maximum of affine functions. The subdifferential of such a maximum is the convex hull of the gradients of its active functions. ∎

A rational convex combination of critical cycle incidences is therefore a finite exact sensitivity certificate at a tie.

## 3. Exact stability face

Let `Gamma_C` be the product of multiplicative edge factors around cycle `C`.

### Theorem PP3cdh -- PROVED / MULTICRITICAL STABILITY FACE

A proposed critical family `K` remains exactly tied and maximal precisely on the region defined by

```text
(P_C Gamma_C)^(ell_D)=(P_D Gamma_D)^(ell_C)
```

for `C,D in K`, together with

```text
(P_C Gamma_C)^(ell_E)>=(P_E Gamma_E)^(ell_C)
```

for `C in K` and every competitor `E`. In the relative interior, the critical family is unchanged.

#### Proof

The equalities are exactly equality of geometric cycle rates, written without radicals. The inequalities are exactly domination of every other cycle. Strict competitor inequalities characterize the relative interior. ∎

## 4. Exact audit

Run

```bash
python scripts/check_multicritical_shell_faces.py
```

The fixture has a critical loop and a critical two-cycle, both of rate `3/4`, plus one subcritical loop. It checks 625 integer perturbation directions. The subgradient extremes are `1` on the loop edge and `1/2,1/2` on the two-cycle edges.
