# Superregular atom-budget perturbation stability

This note records SRR2ca--SRR2ce. It controls how the exact witness-atom budget changes under local conflict and capacity perturbations.

## Contract

For each retained exact witness atom `a`, let reference weighted conflict burden be `B_a` and reference capacity be `C_a`. The actual system has

`B'_a = B_a + I_a - R_a`,

`C'_a = C_a + D_a - L_a`,

where `I_a,R_a,D_a,L_a` are nonnegative exact burden additions, burden removals, capacity deposits and capacity losses. All values are retained per atom.

## Theorem block

### SRR2ca — coordinatewise perturbation identity

The actual overload at atom `a` is exactly `(B'_a-C'_a)_+`. Added capacity and removed burden are monotone improvements.

### SRR2cb — total shortfall stability

Writing `Psi=sum_a(B_a-C_a)_+` and `Psi'=sum_a(B'_a-C'_a)_+`,

`Psi' <= Psi + sum_a I_a + sum_a L_a`.

The sharper coordinatewise envelope retains `R_a` and `D_a` as improvements.

### SRR2cc — robust paid criterion

A reference-paid atom remains paid whenever its retained slack plus deposit and burden removal covers burden addition plus capacity loss.

### SRR2cd — exact overloaded-atom return

If the actual atom budgets are not all paid, the least atom with `B'_a>C'_a` is an exact local obstruction carrying its full overload.

### SRR2ce — composition with executable weight

When all actual atom burdens are paid, the existing threshold atom-budget theorem applies with the actual total capacity. Omitted conflicts, witness changes or unrecorded capacity changes return reset.

## Proof

The coordinate identity is definitional. The positive-part inequality `(x+y)_+ <= x_+ + y_+` applied with `y=I_a+L_a-R_a-D_a` gives SRR2cb. The remaining claims are coordinatewise.

## Finite audit

Run `python scripts/verify_srr_atom_budget_perturbation.py`.

The deterministic audit checks 7,000 systems, 31,574 exact atoms, 189,016 reference burden units, 189,200 reference capacity units, 62,861 burden additions, 50,803 removals, 63,204 capacity deposits, 58,073 capacity losses, 73,948 actual shortfall units, and 6,060 exact overloaded-atom witnesses.

## Scope

This theorem does not construct the geometric witness atoms or prove their reference burdens, capacities or perturbation terms. SRR2, SRR4 and the no-three-in-line conjecture are not proved.