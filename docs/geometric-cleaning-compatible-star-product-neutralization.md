# Product neutralization of compatible paid current-star banks

**Branch:** `research/geometric-cleaning`

GC2cm--GC2cr convert surviving created-collateral cohorts into genuinely current paid star
incidence and then regularize them into a simultaneously compatible star family.  The remaining
execution question is whether several such stars can be neutralized at once without losing the
single-star spread calculation of AN1--AN4.

Under the declared block-disjoint compatibility contract, the answer is exact.  Independent
allowed matching banks form a product measure.  Every old star triple is destroyed
simultaneously, and every new rank-three certificate pays the product of its blockwise matching
probabilities.  Failure localizes to one interaction involving at most three star blocks.

## Compatible product-bank model

Fix a finite compatible current-star family indexed by `I={1,...,k}`.  Star `i` has:

- one current anchor and an endpoint-disjoint selected substar;
- a movable endpoint block of size `t_i>=7` in one fixed permutation layer/channel;
- row set `R_i` and column set `C_i`;
- a forbidden-position set `F_i subset C_i x R_i` of row and column degree at most two;
- the allowed matching family `Omega_i=Omega(F_i)` from AN1--AN3.

Assume the block-disjoint compatibility contract:

1. the moved cell blocks `C_i x R_i` are pairwise disjoint;
2. each local matching remains legal after all fixed rectangle switches;
3. choosing one matching from every `Omega_i` simultaneously preserves all row, column, layer and
   hard-context constraints;
4. every cross-star collateral certificate is represented explicitly in the global certificate
   list below.

Let `X` be the current configuration after removing every selected movable endpoint and every
fixed-switch removed cell.  Let `Z` be obtained from `X` by inserting all fixed-switch new cells.
For a product choice

`pi=(pi_i)_(i in I) in Omega_prod=prod_i Omega_i`,

write

`S_pi=Z union union_i M_(i,pi_i)`,

where `M_(i,pi_i)` is the replacement matching in block `i`.

For one prospective weighted rank-three certificate `Q`, let `r_i(Q)` be the number of required
matching cells from block `i`.  Then

`sum_i r_i(Q)<=3`.

Certificates containing incompatible positions have probability zero.  Put

`p_hat(Q)=prod_(i:r_i(Q)>0) 128/(t_i)_(r_i(Q))`.

Let `w_Q>=0` be its weight and define

`E_prod=sum_Q w_Q*p_hat(Q)`.

Finally put

`D_prod=Phi(S)-Phi(X)`,

`F_prod=Phi(Z)-Phi(X)`,

where `S` is the current pre-neutralization configuration.

## GC2cx -- exact product spread bound -- PROVED

For a uniformly random independent product choice `pi in Omega_prod`, every compatible
certificate `Q` satisfies

`Pr(Q subset S_pi)<=p_hat(Q)`.

### Proof

Inside block `i`, the certificate prescribes a compatible partial matching of size `r_i(Q)`.
AN1 gives probability at most `128/(t_i)_(r_i(Q))`.  The block choices are independent, so the
joint containment probability is the product of the blockwise probabilities.  A forbidden or
incompatible prescription has probability zero. QED.

The bound automatically handles certificates using one, two or three distinct star blocks.

## GC2cy -- simultaneous destruction of the paid star bank -- PROVED

Every product state `S_pi` destroys every selected old star triple in every block.

If the selected current-star weights are occurrence-faithful, their total weight `W_star` is
contained in `D_prod`:

`D_prod>=W_star`.

### Proof

AN3 destroys each old triple because the selected endpoint is forbidden from remaining in its
original cell.  The product compatibility contract guarantees that choices in other blocks do
not restore that exact occurrence.  Summing the current occurrence-faithful star weights gives
the second statement. QED.

Thus the product construction spends no selected star certificate twice.

## GC2cz -- product-bank collateral expectation -- PROVED

For uniform `pi in Omega_prod`,

`E[Phi(S_pi)-Phi(Z)]<=E_prod`.

Consequently,

`E[Phi(S_pi)-Phi(S)]<=F_prod-D_prod+E_prod`.

### Proof

Every new triple in `S_pi` has a unique exact certificate `Q` in the declared complete list.
Its indicator expectation is at most `p_hat(Q)` by GC2cx.  Sum with weights and use linearity of
expectation.  The second identity follows from

`Phi(S_pi)-Phi(S)`

`=[Phi(Z)-Phi(X)]-[Phi(S)-Phi(X)]+[Phi(S_pi)-Phi(Z)]`.

QED.

## GC2da -- improvement or low-order cross-star concentration -- PROVED

If

`D_prod>F_prod+E_prod`,

some product state strictly lowers `Phi`.

Otherwise put

`H=(D_prod-F_prod)_+`.

If `H>0`, then `E_prod>=H`.  Partition the prospective certificates by the number

`s(Q)=|{i:r_i(Q)>0}| in {1,2,3}`

of touched star blocks.  One value `s` carries normalized expected mass at least `H/3`.
Moreover, with

`M_k=sum_(s=1)^3 binom(k,s)`,

one exact block subset `J subset I`, `1<=|J|<=3`, carries normalized expected certificate mass at
least

`H/M_k`.

### Proof

The strict inequality makes the expectation in GC2cz negative, so one state improves.  If it
fails and `H>0`, rearrange to obtain `E_prod>=H`.  Every rank-three certificate touches at most
three moved blocks.  Weighted pigeonhole over the three support sizes gives `H/3`; weighted
pigeonhole over all nonempty block subsets of size at most three gives `H/M_k`. QED.

The failure witness is therefore never a diffuse interaction over an unbounded number of stars:
it is one one-star, two-star or three-star product-collateral profile.

## GC2db -- paid current-star product router -- PROVED UNDER THE PRODUCT-COMPATIBILITY CONTRACT

Suppose GC2cp returns a compatible current paid star family of total surviving weight `W_cur`.
Choose occurrence-faithful substars and AN3 blocks so that

`W_star>=rho*W_cur`

for some declared extraction fraction `rho>0`.  Then the product neutralization has one exact
continuation:

1. **strict cleaning descent:** if `rho W_cur>F_prod+E_prod`, one product state lowers `Phi`;
2. **fixed-switch collateral:** `F_prod` itself is at least a declared fraction of `rho W_cur`;
3. **one-star product obstruction:** one exact star block carries large normalized collateral;
4. **two-star interaction:** one exact compatible star pair carries large normalized collateral;
5. **three-star interaction:** one exact compatible star triple carries large normalized
   collateral;
6. **contract failure:** block disjointness, certificate completeness or occurrence-faithful
   payment fails and returns its exact physical cause.

Quantitatively, outside the descent branch the sum `F_prod+E_prod` is at least `rho W_cur`; after
separating `F_prod`, GC2da localizes the residual normalized collateral to one subset of at most
three star blocks.

### Proof

GC2cy gives `D_prod>=W_star>=rho W_cur`.  Apply GC2cz--GC2da.  If the product hypotheses fail,
record the least failed contract field rather than treating the star weight as executable. QED.

This is the exact execution interface missing from GC2cr.  It reduces a compatible current-star
bank either to a genuine cleaning move or to bounded-order cross-star collateral geometry.

## Corrected GC frontier

Compatible paid current-star banks are now executable under a complete product-certificate
contract.  Their failure is one fixed-switch collateral term or one exact interaction among at
most three stars.  The live geometric tasks are therefore:

- classify the one-, two- and three-star normalized collateral profiles;
- resolve labelled paid-overload recursion against the endpoint theorem;
- handle high created-pair multiplicity;
- treat identity-sensitive or unbounded tagged recycling;
- and continue the isolated-cell, pool-depletion, global-context and local-resampling branches.

## Finite check

`scripts/verify_geometric_compatible_star_product_neutralization.py` exhausts small independent
matching families and weighted rank-three certificate lists.  It checks product containment
probabilities, simultaneous old-star destruction, the exact expectation decomposition and the
one/two/three-block failure localization.