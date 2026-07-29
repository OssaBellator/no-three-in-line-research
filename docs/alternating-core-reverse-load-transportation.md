# Alternating core: restricted-menu reverse-load transportation

## Scope

This note records AC5be--AC5bi. It is a deterministic transportation lemma for a fixed restricted-menu installation stage. It does not estimate the geometric forward degrees or reverse loads; those remain menu-specific inputs.

Fix a finite set `L` of current menu states and a finite set `R` of legal installation endpoints. Each endpoint `r` has an integer cost `c(r)>=0`. Let `G_t` be the bipartite graph containing precisely the legal incidences to endpoints of cost at most `t`.

Assume the full graph admits a matching saturating `L`. Write `n=|L|`, `nu_t` for the maximum matching size in `G_t`, and

`delta_t=n-nu_t`.

## AC5be: exact threshold layer cake

The minimum total endpoint cost of a matching saturating `L` is exactly

`sum_{t>=0} delta_t`.

Only finitely many terms are nonzero. This is the integral layer-cake form of minimum-cost bipartite matching: every unit of endpoint cost contributes one unit at every lower threshold, and the threshold matching deficit is the exact number of left states forced above that level.

## AC5bf: Hall-deficiency form

For every threshold,

`delta_t=max_{X subseteq L} (|X|-|N_t(X)|)`.

Thus failure at a particular cost level retains a canonical Hall-deficient restricted-menu subset rather than only a scalar cost excess.

## AC5bg: degree/reverse-load bound

Suppose that after all retained conditioning losses, every left state has at least `d_t` neighbours in `G_t`, and every right endpoint has reverse load at most `D_t>0`. Then

`delta_t <= floor(n (1-d_t/D_t)_+)`.

More generally, if conditioning deletes at most `b_t` legal incidences from each left state, replace `d_t` by `d_t-b_t`.

## AC5bh: endpoint-cost consequence

Combining AC5be and AC5bg gives

`minimum installation cost <= sum_t floor(n (1-(d_t-b_t)/D_t)_+)`.

This is the exact interface needed to import restricted-menu forward-degree estimates and reverse-load estimates into one pathwise AC5 installation bound.

## AC5bi: retained failure object

If the desired AC5 cost budget fails, then at least one threshold has positive degree/load imbalance. At that threshold the canonical Hall-deficient set, its exact endpoint neighbourhood, `d_t`, `b_t`, and `D_t` are retained. Omitted higher-order legality or a changing endpoint-cost dictionary is a model reset, not a hidden successful installation.

## Remaining frontier

The theorem reduces the reverse-flow/min-cost step to menu-specific estimates of `d_t`, `b_t`, and `D_t`, together with payment of any returned Hall core or exact obstruction class. It does not prove AC5, AC6, or the no-three-in-line conjecture.