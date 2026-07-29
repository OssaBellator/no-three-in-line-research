# Telescoping potentials for shell expansion

`docs/409` bounds shell products by charging each expansion scale against a
decreasing invariant.  Its exceedance-tail estimate may reuse the same initial
invariant budget at several thresholds.  This chapter gives a complementary
per-boundary certificate: compare every expansive factor directly with a
multiplicative potential drop.  The product then telescopes exactly.

The statements are general.  They do not identify the required shell invariant
for prime patching.

## 1. Exact multiplicative telescoping

Let

```text
J_0>=J_1>=...>=J_r>=0
```

be a nonincreasing shell invariant and put

```text
p_i=max(kappa_i,1),
c_i=min(kappa_i,1),
Cprod=product_i c_i.
```

Let `Phi` be a positive function on the range of the invariant.

### Theorem PP3byi -- PROVED / TELESCOPING SHELL POTENTIAL

Suppose every nonterminal boundary satisfies

```text
p_i Phi(J_(i+1))<=Phi(J_i).
```

Then

```text
product_i p_i<=Phi(J_0)/Phi(J_r),
```

and the complete trajectory with terminal factor `tau` obeys

```text
tau product_i kappa_i
 <=tau Cprod Phi(J_0)/Phi(J_r).
```

It therefore contracts whenever the right-hand side is below one.

#### Proof

Multiply the boundary inequalities.  Every intermediate potential cancels:

```text
product_i p_i
 <=product_i Phi(J_i)/Phi(J_(i+1))
 =Phi(J_0)/Phi(J_r).
```

Then use

```text
product_i kappa_i=Cprod product_i p_i.
```

∎

This certificate spends each invariant drop once, at the boundary where it
occurs.

## 2. Additive logarithmic charge

### Theorem PP3byj -- PROVED / LOG-DROP SHELL BUDGET

Assume that for some `A>0`, every boundary satisfies

```text
log p_i<=A(J_i-J_(i+1)).
```

Then

```text
product_i p_i<=exp(A(J_0-J_r))<=exp(AJ_0),
```

and

```text
tau product_i kappa_i
 <=tau Cprod exp(A(J_0-J_r)).
```

#### Proof

Apply `PP3byi` with

```text
Phi(J)=exp(AJ).
```

Equivalently, sum the displayed log-drop inequalities and exponentiate. ∎

A useful sufficient condition is: if an actual expansive factor `u` forces a
drop at least `eta(u)>0`, then one may take

```text
A=sup_(1<u<=B) log(u)/eta(u)
```

whenever all factors are at most `B`.

## 3. Exact rational-base specialization

### Corollary PP3byk -- PROVED / INTEGER-DROP RATIONAL SHELL CERTIFICATE

Suppose every `J_i` is a nonnegative integer and `B>=1` is rational.  If

```text
p_i<=B^(J_i-J_(i+1))
```

for every boundary, then

```text
product_i p_i<=B^(J_0-J_r)<=B^J_0.
```

Thus exact rational arithmetic certifies contraction from

```text
tau Cprod B^(J_0-J_r)<1.
```

In particular, if an expansive boundary in scale band

```text
B^(q-1)<p_i<=B^q
```

always consumes at least `q` integer units of invariant, the hypothesis holds.

#### Proof

Use `Phi(J)=B^J` in `PP3byi`.  The scale-band assertion gives

```text
p_i<=B^q<=B^(J_i-J_(i+1)).
```

∎

This rational form is well suited to finite shell ledgers and avoids numerical
logarithms.  It also gives a sharper alternative to threshold-tail charging
when the same invariant controls each boundary separately.

## 4. Finite diagnostic

Run

```bash
python scripts/check_telescoping_shell_potentials.py
```

The script exhausts rational four-boundary shell profiles together with all
compatible integer drop allocations, verifies the per-boundary potential
inequalities, and checks the exact telescoped product and terminal contraction
comparisons.

The next theorem identifier after this chapter is `PP3byl`.
