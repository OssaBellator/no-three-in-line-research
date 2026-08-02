# Constant spread with any fixed forbidden degree

The first-generation neutralization banks PX73, PX76, and PX79 avoid the union
of two forbidden partial matchings: the original positions and the opposite
permutation layer. A recursive second-generation bank may also need to avoid
one or more earlier replacement positions.

This chapter extends AN1 from forbidden degree two to every fixed forbidden
degree. The constants grow exponentially in that degree, but remain absolute at
every bounded recursion depth.

Let \(F\subseteq [t]\times[t]\) be a forbidden-position graph with maximum row
and column degree at most

\[
\Delta.
\]

Let \(\Omega_F\) be the set of permutations \(\pi\in S_t\) satisfying

\[
(i,\pi(i))\notin F
\qquad(i\in[t]).
\]

## 1. Uniform allowed-matchings spread

### Theorem PX196 -- PROVED

If

\[
\boxed{t\ge8\Delta,}
\]

then

\[
\boxed{|\Omega_F|\ge e^{-4\Delta}t!.}
\]

Moreover, under the uniform distribution on \(\Omega_F\), every compatible
prescribed partial matching \(E\) of rank \(r\) satisfies

\[
\boxed{
\Pr(E\subseteq M)
\le
\frac{e^{4\Delta}}{(t)_r}.
}
\]

Thus the uniform allowed family is fixed-rank

\[
\frac{e^{4\Delta}}t
\]

spread.

### Proof

Choose a uniformly random permutation. For every forbidden cell
\(e=(i,j)\in F\), let

\[
A_e=\{\pi(i)=j\}.
\]

Then

\[
\Pr(A_e)=\frac1t.
\]

The canonical conflict graph joins events whose cells share a source row or
target column. It is a negative dependency graph for the permutation space.
Every event has at most

\[
2\Delta-2
\]

neighbors.

Set

\[
x_e=\frac2t.
\]

Since \(t\ge8\Delta\),

\[
\left(1-\frac2t\right)^{2\Delta-2}
\ge
1-\frac{4\Delta}{t}
\ge\frac12.
\]

Hence

\[
x_e\prod_{A_f\sim A_e}(1-x_f)
\ge
\frac2t\cdot\frac12
=
\Pr(A_e).
\]

The lopsided local lemma therefore gives

\[
\Pr\left(\bigcap_{e\in F}\overline{A_e}\right)
\ge
\prod_{e\in F}(1-x_e).
\]

There are at most \(\Delta t\) forbidden cells. For \(t\ge4\),

\[
\log\left(1-\frac2t\right)
\ge-
\frac4t,
\]

so

\[
\prod_{e\in F}(1-x_e)
\ge
\left(1-\frac2t\right)^{\Delta t}
\ge e^{-4\Delta}.
\]

Multiplying by \(t!\) proves the count.

For a compatible partial matching \(E\) of rank \(r\), at most
\((t-r)!\) permutations contain \(E\). Dividing by the lower bound on
\(|\Omega_F|\) gives

\[
\Pr(E\subseteq M)
\le
\frac{(t-r)!}{e^{-4\Delta}t!}
=
\frac{e^{4\Delta}}{(t)_r}.
\]

\(\square\)

The bound is intentionally simple. For \(\Delta=2\), AN1 gives the much better
constant \(128\), while PX196 gives \(e^8\). The advantage is that PX196 scales
uniformly with every fixed \(\Delta\).

## 2. Residual cylinders and conditioning stability

The same argument applies after fixing part of the replacement matching. This
is useful in a recursive decoder because earlier generations become conditions,
not merely additional forbidden positions.

### Theorem PX198 -- PROVED

Let \(E\) be a compatible partial matching of rank \(r\). If

\[
\boxed{t-r\ge8\Delta,}
\]

then the number of allowed extensions of \(E\) satisfies

\[
\boxed{
|\{\pi\in\Omega_F:E\subseteq\pi\}|
\ge e^{-4\Delta}(t-r)!.
}
\]

Consequently, for the uniform measure on \(\Omega_F\),

\[
\boxed{
\frac{e^{-4\Delta}}{(t)_r}
\le
\Pr(E\subseteq M)
\le
\frac{e^{4\Delta}}{(t)_r}.
}
\]

### Proof

Delete the \(r\) rows and \(r\) columns used by \(E\). The remaining forbidden
position graph has order \(t-r\) and maximum row and column degree at most
\(\Delta\). PX196 gives at least

\[
e^{-4\Delta}(t-r)!
\]

allowed residual permutations, each extending \(E\).

For the lower probability bound, divide this extension count by the trivial
upper bound \(|\Omega_F|\le t!\). The upper probability bound is PX196.
\(\square\)

### Corollary PX199 -- PROVED

Let \(E_0\) be an extendable compatible partial matching of rank \(q\), and
condition the uniform measure on \(\Omega_F\) on \(E_0\subseteq M\). If

\[
t-q\ge8\Delta,
\]

then every further compatible residual partial matching \(E_1\) of rank \(r\)
satisfies

\[
\boxed{
\Pr(E_1\subseteq M\mid E_0\subseteq M)
\le
\frac{e^{4\Delta}}{(t-q)_r}.
}
\]

If also \(t-q-r\ge8\Delta\), then

\[
\boxed{
\Pr(E_1\subseteq M\mid E_0\subseteq M)
\ge
\frac{e^{-4\Delta}}{(t-q)_r}.
}
\]

### Proof

After deleting the rows and columns fixed by \(E_0\), the conditional measure is
exactly the uniform allowed-permutation measure for the residual forbidden graph.
Its maximum degree is still at most \(\Delta\). Apply PX196 for the upper bound
and PX198 for the lower bound. \(\square\)

Thus bounded-rank exposure does not destroy the bank's fixed-rank spread. It
only reduces the available order by the number of exposed rows.

## 3. Recursive neutralization banks

At first generation, a moved endpoint set must avoid:

1. its original positions;
2. the opposite permutation layer.

At the next generation, to preserve the first neutralization while destroying
a newly extracted star, also forbid the current positions of the second-star
endpoints. This is a union of at most three partial matchings.

After \(d\) nested generations, the natural endpoint bank has forbidden degree
at most

\[
\boxed{\Delta_d\le d+1.}
\]

## Corollary PX197 -- PROVED

For every fixed recursion depth \(d\), every endpoint block of order

\[
\boxed{t\ge8(d+1)}
\]

admits a nonempty joint replacement family preserving all earlier forbidden
positions. Its uniform distribution satisfies

\[
\boxed{
\Pr(E\subseteq M)
\le
\frac{e^{4(d+1)}}{(t)_{|E|}}.
}
\]

### Proof

The original positions, opposite layer, and at most \(d-1\) earlier replacement
positions are each partial matchings on the same row and column sets. Their
union has maximum degree at most \(d+1\). Apply PX196. \(\square\)

PX199 also shows that this spread conclusion remains valid after any bounded
compatible exposure, provided the residual order is still at least
\(8(d+1)\).

## 4. Sharp nonemptiness threshold

Spread needs slack, but mere executability has a much smaller and sharp
threshold.

### Theorem PX200 -- PROVED

If

\[
\boxed{t\ge2\Delta,}
\]

then \(\Omega_F\ne\varnothing\).

The threshold is sharp for general degree-\(\Delta\) forbidden graphs, even when
\(F\) is a union of \(\Delta\) partial matchings: at
\(t=2\Delta-1\) there is such an \(F\) with no allowed permutation.

### Proof

Let \(G\) be the allowed-position bipartite graph. Every vertex of \(G\) has
degree at least

\[
t-\Delta\ge\frac t2.
\]

To verify Hall's condition, take a set \(S\) of left vertices. If
\(|S|\le t/2\), then one vertex of \(S\) already has at least \(t/2\) neighbours,
so \(|N(S)|\ge t/2\ge|S|\). If \(|S|>t/2\) and \(|N(S)|<|S|\), then any right
vertex outside \(N(S)\) has all its neighbours outside \(S\), hence degree at
most \(t-|S|<t/2\), a contradiction. Thus \(G\) has a perfect matching.

For sharpness, take \(t=2\Delta-1\), choose \(\Delta\) left vertices and
\(\Delta\) right vertices, and let \(F\) be the complete bipartite graph between
them. Its maximum degree is \(\Delta\), it decomposes into \(\Delta\) partial
matchings, and those \(\Delta\) left vertices have only \(\Delta-1\) allowed
neighbours. Hall's condition fails. \(\square\)

Therefore a depth-\(d\) recursive endpoint bank is guaranteed to be nonempty
already when

\[
\boxed{t\ge2(d+1),}
\]

although the present uniform spread theorem still requires
\(t\ge8(d+1)\).

## 5. Consequence for the rainbow decoder recursion

PX195a converts a large second-generation \(T_2\) mass into a loaded line or
clean star through a new outside cell. PX197 shows that a bounded number of such
recursive neutralizations can be performed without undoing the earlier ones.
PX199 adds the stronger fact that bounded-rank conditioning during the decoder
does not degrade the cylinder constant, and PX200 separates the threshold for
mere executability from the threshold for quantitative spread.

This removes a combinatorial obstruction which was implicit in the earlier
roadmap: the third forbidden matching does not destroy the replacement bank.
It merely changes the spread constant from \(128\) to an absolute
\(e^{12}\) at depth two.

A bounded-depth proof can now proceed as follows.

1. Neutralize the first clean star, line, or radial core.
2. Square-root thin the endpoint set using PX189.
3. Minimize the background-rainbow collision potential using PX194.
4. If PX195a extracts another star or line, apply a depth-two bank avoiding all
   three relevant position matchings.
5. Expose bounded-rank certificates using PX199 without losing the residual
   spread estimate.
6. Repeat a fixed number of times if necessary, paying the explicit
   \(e^{4(d+1)}\) spread constants.

What remains is a **depth bound**: prove that some absolute number of recursive
generations destroys more old mass than the accumulated fixed-rank collateral,
or construct a monotone generational potential.

PX156 shows that arbitrary lattice absorption can require unbounded support,
but that negative result does not contradict PX197 or PX200: the recursion here
uses a growing endpoint block and only a fixed number of forbidden partial
matchings.

## 6. Quantitative boundary

PX197 does not support recursion depth growing with \(t\) at no cost. The spread
constant is exponential in \(d\), and the spread-capable minimum block size is
linear in \(d\). Thus a successful termination theorem should keep

\[
d=O(1)
\]

or at worst \(d=o(\log t)\) with additional quantitative savings.

PX200 shows that bank nonemptiness itself survives to four times greater depth
than the present spread proof: \(d+1\le t/2\) rather than \(d+1\le t/8\). The
immediate target remains depth two or three, where PX199 gives conditioning
stability with an absolute cylinder constant. The rainbow decoder already
returns exactly the same star/line geometry, so there is no evidence yet that
new geometric types appear at later bounded depth.

## 7. Verification

Run

```bash
python scripts/verify_product_bounded_forbidden_spread.py
```

The verifier exactly counts allowed permutations for random unions of up to
three forbidden permutations through order fourteen, checks conditioned
cylinder estimates at the first nontrivial LLL thresholds, verifies the sharp
Hall obstruction through degree seven, checks the symbolic lopsided-LLL
inequalities for \(t\ge8\Delta\), and records both recursive-depth thresholds.
