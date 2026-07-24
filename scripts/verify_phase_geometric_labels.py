#!/usr/bin/env python3
"""Verify OP4g--OP4h geometric factor labels and bicycle compatibility."""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations, product


Point = tuple[int, int]


@dataclass(frozen=True)
class OrientedSecantRecord:
    """One orientation of a two-channel secant factor."""

    prime: int
    endpoint: Point
    partner: Point
    anchor: Point
    endpoint_channel: int
    anchor_channel: int
    root: int
    parameter: int
    transition: int
    collision_partner: int
    cross_at_endpoint: int
    cross_at_partner: int


@dataclass(frozen=True)
class CarryStarRoute:
    """Product-carry data after choosing one point as the star centre."""

    anchor: Point
    endpoints: tuple[Point, Point]
    signature: tuple[tuple[int, int], tuple[int, int]]
    cross_levels: tuple[int, int] | None


@dataclass(frozen=True)
class FactorCertificate:
    """Lossless channel-profile certificate for one modular factor."""

    prime: int
    points: tuple[Point, Point, Point]
    channels: tuple[int, int, int]
    determinant: int
    kind: str
    rational_records: tuple[OrientedSecantRecord, ...]
    carry_routes: tuple[CarryStarRoute, CarryStarRoute, CarryStarRoute]


@dataclass(frozen=True)
class QuotientTransition:
    """An unordered rational collision edge in an additive quotient."""

    source_factor: int
    normalization: int
    root: int
    left: int
    right: int
    colour: int
    certificate: FactorCertificate | None = None


@dataclass(frozen=True)
class CarryOnlyEdge:
    """An implication source factor with no same-channel endpoint pair."""

    source_factor: int
    certificate: FactorCertificate


def inverse(value: int, prime: int) -> int:
    assert value % prime
    return pow(value, prime - 2, prime)


def determinant(left: Point, middle: Point, right: Point) -> int:
    return (
        (middle[0] - left[0]) * (right[1] - left[1])
        - (right[0] - left[0]) * (middle[1] - left[1])
    )


def channel(point: Point, prime: int) -> int:
    value = point[0] * point[1] % prime
    assert value
    return value


def product_carry(point: Point, prime: int) -> tuple[int, int]:
    residue = channel(point, prime)
    numerator = point[0] * point[1] - residue
    assert numerator % prime == 0
    carry = numerator // prime
    assert 0 <= carry <= prime - 2
    return residue, carry


def rational_map(value: int, root: int, prime: int) -> int:
    assert value % prime not in (0, root % prime)
    return (
        value
        * (1 - value)
        * inverse(root - value, prime)
    ) % prime


def collision_involution(value: int, root: int, prime: int) -> int:
    assert value % prime not in (0, root % prime)
    return (
        root
        * (value - 1)
        * inverse(value - root, prime)
    ) % prime


def oriented_secant_record(
    prime: int,
    endpoint: Point,
    partner: Point,
    anchor: Point,
) -> OrientedSecantRecord:
    """Derive the exact F_r record of an affine two-channel secant."""

    endpoint_channel = channel(endpoint, prime)
    assert channel(partner, prime) == endpoint_channel
    anchor_channel = channel(anchor, prime)
    assert anchor_channel != endpoint_channel
    assert endpoint != partner
    assert determinant(anchor, endpoint, partner) % prime == 0

    x, y_x = endpoint
    u, y_u = partner
    z, w = anchor
    root = anchor_channel * inverse(endpoint_channel, prime) % prime
    parameter = z * inverse(x, prime) % prime
    transition = u * inverse(x, prime) % prime

    assert root not in (0, 1)
    assert parameter not in (0, 1, root)
    assert transition not in (0, 1)
    assert (
        (root - parameter) * transition
        - parameter * (1 - parameter)
    ) % prime == 0
    assert rational_map(parameter, root, prime) == transition

    collision_partner = collision_involution(
        parameter,
        root,
        prime,
    )
    assert collision_partner not in (0, 1, root)
    assert collision_involution(
        collision_partner,
        root,
        prime,
    ) == parameter
    assert rational_map(
        collision_partner,
        root,
        prime,
    ) == transition
    assert (
        parameter * collision_partner
        - root * transition
    ) % prime == 0
    assert (
        parameter + collision_partner
        - 1 - transition
    ) % prime == 0

    offset = anchor_channel - endpoint_channel
    first_numerator = (x - z) * (y_u - w) - offset
    second_numerator = (u - z) * (y_x - w) - offset
    assert first_numerator % prime == 0
    assert second_numerator % prime == 0
    cross_at_endpoint = first_numerator // prime
    cross_at_partner = second_numerator // prime
    assert (
        prime * (cross_at_endpoint - cross_at_partner)
        == determinant(anchor, endpoint, partner)
    )

    return OrientedSecantRecord(
        prime=prime,
        endpoint=endpoint,
        partner=partner,
        anchor=anchor,
        endpoint_channel=endpoint_channel,
        anchor_channel=anchor_channel,
        root=root,
        parameter=parameter,
        transition=transition,
        collision_partner=collision_partner,
        cross_at_endpoint=cross_at_endpoint,
        cross_at_partner=cross_at_partner,
    )


def carry_star_route(
    prime: int,
    anchor: Point,
    endpoints: tuple[Point, Point],
) -> CarryStarRoute:
    endpoint_data = tuple(
        sorted(
            (product_carry(point, prime), point)
            for point in endpoints
        )
    )
    ordered_endpoints = tuple(item[1] for item in endpoint_data)
    signature = tuple(item[0] for item in endpoint_data)
    assert len(ordered_endpoints) == 2
    assert len(signature) == 2

    cross_levels: tuple[int, int] | None = None
    if signature[0][0] == signature[1][0]:
        assert channel(anchor, prime) != signature[0][0]
        record = oriented_secant_record(
            prime,
            ordered_endpoints[0],
            ordered_endpoints[1],
            anchor,
        )
        cross_levels = (
            record.cross_at_endpoint,
            record.cross_at_partner,
        )

    return CarryStarRoute(
        anchor=anchor,
        endpoints=ordered_endpoints,
        signature=signature,
        cross_levels=cross_levels,
    )


def classify_factor(
    prime: int,
    points: tuple[Point, Point, Point],
) -> FactorCertificate:
    """Classify a distinct modularly collinear triple by channel profile."""

    assert len(set(points)) == 3
    assert all(
        1 <= coordinate < prime
        for point in points
        for coordinate in point
    )
    det = determinant(*points)
    assert det % prime == 0
    channels = tuple(channel(point, prime) for point in points)
    multiplicities = {
        value: channels.count(value)
        for value in set(channels)
    }

    # A line meets one nondegenerate modular hyperbola in at most two
    # affine points.
    assert len(multiplicities) != 1

    carry_routes = tuple(
        carry_star_route(
            prime,
            points[anchor_index],
            tuple(
                points[index]
                for index in range(3)
                if index != anchor_index
            ),
        )
        for anchor_index in range(3)
    )
    assert len(carry_routes) == 3

    if len(multiplicities) == 3:
        assert all(
            route.signature[0][0] != route.signature[1][0]
            and route.cross_levels is None
            for route in carry_routes
        )
        rational_records: tuple[OrientedSecantRecord, ...] = ()
        kind = "three_channel_carry"
    else:
        repeated_channel = next(
            value
            for value, count in multiplicities.items()
            if count == 2
        )
        endpoint_indices = tuple(
            index
            for index, value in enumerate(channels)
            if value == repeated_channel
        )
        anchor_index = next(
            index
            for index, value in enumerate(channels)
            if value != repeated_channel
        )
        first = oriented_secant_record(
            prime,
            points[endpoint_indices[0]],
            points[endpoint_indices[1]],
            points[anchor_index],
        )
        reverse = oriented_secant_record(
            prime,
            points[endpoint_indices[1]],
            points[endpoint_indices[0]],
            points[anchor_index],
        )
        assert reverse.root == first.root
        assert (
            reverse.parameter
            == first.parameter * inverse(first.transition, prime) % prime
        )
        assert reverse.transition == inverse(first.transition, prime)
        assert {
            reverse.parameter,
            reverse.collision_partner,
        } == {
            first.parameter * inverse(first.transition, prime) % prime,
            first.collision_partner
            * inverse(first.transition, prime)
            % prime,
        }
        assert (
            first.cross_at_endpoint,
            first.cross_at_partner,
        ) == (
            reverse.cross_at_partner,
            reverse.cross_at_endpoint,
        )
        rational_records = (first, reverse)
        kind = "two_channel_rational"

        same_channel_routes = tuple(
            route
            for route in carry_routes
            if route.signature[0][0] == route.signature[1][0]
        )
        assert len(same_channel_routes) == 1
        assert same_channel_routes[0].cross_levels == (
            first.cross_at_endpoint,
            first.cross_at_partner,
        ) or same_channel_routes[0].cross_levels == (
            first.cross_at_partner,
            first.cross_at_endpoint,
        )

    if det == 0:
        assert all(
            route.cross_levels is None
            or route.cross_levels[0] == route.cross_levels[1]
            for route in carry_routes
        )

    return FactorCertificate(
        prime=prime,
        points=points,
        channels=channels,
        determinant=det,
        kind=kind,
        rational_records=rational_records,
        carry_routes=carry_routes,
    )


def prime_divisors(value: int) -> tuple[int, ...]:
    divisors: list[int] = []
    candidate = 2
    residual = value
    while candidate * candidate <= residual:
        if residual % candidate == 0:
            divisors.append(candidate)
            while residual % candidate == 0:
                residual //= candidate
        candidate += 1
    if residual > 1:
        divisors.append(residual)
    return tuple(divisors)


def primitive_root(prime: int) -> int:
    factors = prime_divisors(prime - 1)
    for candidate in range(2, prime):
        if all(
            pow(candidate, (prime - 1) // factor, prime) != 1
            for factor in factors
        ):
            return candidate
    raise AssertionError("prime field has no primitive root")


def logarithm_table(prime: int) -> dict[int, int]:
    generator = primitive_root(prime)
    table: dict[int, int] = {}
    value = 1
    for exponent in range(prime - 1):
        assert value not in table
        table[value] = exponent
        value = value * generator % prime
    assert value == 1
    return table


def quotient_transition(
    source_factor: int,
    normalization: int,
    record: OrientedSecantRecord,
    quotient_order: int,
    logs: dict[int, int],
    certificate: FactorCertificate | None = None,
) -> QuotientTransition:
    assert (record.prime - 1) % quotient_order == 0
    transition = QuotientTransition(
        source_factor=source_factor,
        normalization=normalization,
        root=logs[record.root] % quotient_order,
        left=logs[record.parameter] % quotient_order,
        right=logs[record.collision_partner] % quotient_order,
        colour=logs[record.transition] % quotient_order,
        certificate=certificate,
    )
    assert (
        transition.left + transition.right
        - transition.root - transition.colour
    ) % quotient_order == 0
    return transition


def factor_quotient_options(
    source_factor: int,
    certificate: FactorCertificate,
    quotient_order: int,
    logs: dict[int, int],
) -> tuple[QuotientTransition, ...] | CarryOnlyEdge:
    if not certificate.rational_records:
        return CarryOnlyEdge(source_factor, certificate)
    options = tuple(
        quotient_transition(
            source_factor,
            normalization,
            record,
            quotient_order,
            logs,
            certificate,
        )
        for normalization, record in enumerate(
            certificate.rational_records
        )
    )
    assert len(options) == 2
    forward, reverse = options
    assert reverse.root == forward.root
    assert reverse.colour == -forward.colour % quotient_order
    assert {
        reverse.left,
        reverse.right,
    } == {
        (forward.left - forward.colour) % quotient_order,
        (forward.right - forward.colour) % quotient_order,
    }
    return options


def transition(
    source_factor: int,
    normalization: int,
    root: int,
    left: int,
    right: int,
    order: int,
) -> QuotientTransition:
    return QuotientTransition(
        source_factor=source_factor,
        normalization=normalization,
        root=root % order,
        left=left % order,
        right=right % order,
        colour=(left + right - root) % order,
    )


def fixed_transition_labels(
    walk_nodes: tuple[int, ...],
    selected: tuple[QuotientTransition, ...],
    quotient_order: int,
) -> dict[str, object]:
    """Orient fixed unordered edge pairs, or return a local conflict."""

    assert len(selected) == len(walk_nodes) - 1
    assert walk_nodes[0] == walk_nodes[-1]
    adjacency: dict[int, list[tuple[int, int]]] = {}
    for edge_index, (left_node, right_node) in enumerate(
        zip(walk_nodes, walk_nodes[1:])
    ):
        adjacency.setdefault(left_node, []).append(
            (edge_index, right_node)
        )
        if right_node != left_node:
            adjacency.setdefault(right_node, []).append(
                (edge_index, left_node)
            )

    def propagate(
        seed_labels: dict[int, int],
    ) -> dict[str, object]:
        labels = {
            node: value % quotient_order
            for node, value in seed_labels.items()
        }
        queue = list(labels)
        queued = set(queue)
        while queue:
            node = queue.pop()
            queued.discard(node)
            value = labels[node]
            for edge_index, neighbour in adjacency[node]:
                record = selected[edge_index]
                pair = (record.left, record.right)
                if neighbour == node:
                    if record.left != record.right or value != record.left:
                        return {
                            "status": "conflict",
                            "edge_index": edge_index,
                            "node": node,
                            "actual": value,
                            "required_pair": pair,
                            "source_factor": record.source_factor,
                        }
                    continue
                if value == record.left:
                    required = record.right
                elif value == record.right:
                    required = record.left
                else:
                    return {
                        "status": "conflict",
                        "edge_index": edge_index,
                        "node": node,
                        "actual": value,
                        "required_pair": pair,
                        "source_factor": record.source_factor,
                    }
                if neighbour in labels:
                    if labels[neighbour] != required:
                        return {
                            "status": "conflict",
                            "edge_index": edge_index,
                            "node": neighbour,
                            "actual": labels[neighbour],
                            "required": required,
                            "source_factor": record.source_factor,
                        }
                else:
                    labels[neighbour] = required
                    if neighbour not in queued:
                        queue.append(neighbour)
                        queued.add(neighbour)
        return {"status": "compatible", "literal_labels": labels}

    first = selected[0]
    first_left_node = walk_nodes[0]
    first_right_node = walk_nodes[1]
    if first_left_node == first_right_node:
        if first.left != first.right:
            return {
                "status": "incompatible",
                "conflicts": (
                    {
                        "status": "conflict",
                        "edge_index": 0,
                        "node": first_left_node,
                        "required_pair": (first.left, first.right),
                        "source_factor": first.source_factor,
                    },
                ),
            }
        attempts = ({first_left_node: first.left},)
    elif first.left == first.right:
        attempts = (
            {
                first_left_node: first.left,
                first_right_node: first.right,
            },
        )
    else:
        attempts = (
            {
                first_left_node: first.left,
                first_right_node: first.right,
            },
            {
                first_left_node: first.right,
                first_right_node: first.left,
            },
        )

    conflicts: list[dict[str, object]] = []
    for seed in attempts:
        result = propagate(seed)
        if result["status"] == "compatible":
            labels = result["literal_labels"]
            assert set(walk_nodes[:-1]) <= set(labels)
            for edge_index, (left_node, right_node) in enumerate(
                zip(walk_nodes, walk_nodes[1:])
            ):
                record = selected[edge_index]
                assert {
                    labels[left_node],
                    labels[right_node],
                } == {record.left, record.right}
                assert (
                    labels[right_node]
                    - record.root
                    - record.colour
                    + labels[left_node]
                ) % quotient_order == 0
            return result
        conflicts.append(result)
    return {
        "status": "incompatible",
        "conflicts": tuple(conflicts),
    }


def orient_rational_bicycle(
    walk_nodes: tuple[int, ...],
    edge_options: tuple[
        tuple[QuotientTransition, ...] | CarryOnlyEdge,
        ...,
    ],
    quotient_order: int,
) -> dict[str, object]:
    """Choose secant orientations and globally consistent literal labels."""

    assert quotient_order >= 1
    assert len(edge_options) == len(walk_nodes) - 1
    assert len(edge_options) >= 1
    assert walk_nodes[0] == walk_nodes[-1]

    for edge_index, options in enumerate(edge_options):
        if isinstance(options, CarryOnlyEdge):
            return {
                "status": "carry_output",
                "edge_index": edge_index,
                "source_factor": options.source_factor,
                "certificate": options.certificate,
            }
        assert options
        edge_roots = {
            option.root % quotient_order
            for option in options
        }
        if len(edge_roots) != 1:
            return {
                "status": "invalid_edge",
                "edge_index": edge_index,
                "source_factor": options[0].source_factor,
                "roots": frozenset(edge_roots),
            }
        for option in options:
            if (
                option.left + option.right
                - option.root - option.colour
            ) % quotient_order:
                return {
                    "status": "invalid_edge",
                    "edge_index": edge_index,
                    "source_factor": option.source_factor,
                    "normalization": option.normalization,
                }

    rational_options = tuple(
        options
        for options in edge_options
        if not isinstance(options, CarryOnlyEdge)
    )
    roots = tuple(options[0].root % quotient_order for options in rational_options)
    if len(set(roots)) != 1:
        first_root = roots[0]
        mismatch = next(
            index
            for index, root in enumerate(roots)
            if root != first_root
        )
        return {
            "status": "root_mismatch",
            "edge_index": mismatch,
            "expected_root": first_root,
            "actual_root": roots[mismatch],
            "source_factor": rational_options[mismatch][0].source_factor,
            "certificate": rational_options[mismatch][0].certificate,
        }

    trial_count = 0
    conflict_table: list[dict[str, object]] = []
    option_ranges = tuple(
        range(len(options))
        for options in rational_options
    )
    for choices in product(*option_ranges):
        selected = tuple(
            options[choice]
            for options, choice in zip(rational_options, choices)
        )
        result = fixed_transition_labels(
            walk_nodes,
            selected,
            quotient_order,
        )
        trial_count += 1
        if result["status"] == "compatible":
            labels = result["literal_labels"]
            colours = tuple(item.colour for item in selected)
            for index, (left_node, right_node) in enumerate(
                zip(walk_nodes, walk_nodes[1:])
            ):
                assert (
                    labels[right_node]
                    - selected[index].root
                    - colours[index]
                    + labels[left_node]
                ) % quotient_order == 0
            return {
                "status": "rational_admissible",
                "root": roots[0],
                "literal_labels": labels,
                "edge_colours": colours,
                "normalizations": choices,
                "selected": selected,
                "normalization_trials": trial_count,
            }
        conflict_table.append(
            {
                "normalizations": choices,
                "conflicts": result["conflicts"],
            }
        )

    return {
        "status": "literal_root_mismatch",
        "normalization_trials": trial_count,
        "conflict_table": tuple(conflict_table),
        "source_certificates": tuple(
            options[0].certificate
            for options in rational_options
        ),
    }


def brute_fixed_compatible(
    walk_nodes: tuple[int, ...],
    selected: tuple[QuotientTransition, ...],
    quotient_order: int,
) -> bool:
    nodes = tuple(sorted(set(walk_nodes[:-1])))
    for values in product(range(quotient_order), repeat=len(nodes)):
        labels = dict(zip(nodes, values))
        if all(
            {
                labels[left_node],
                labels[right_node],
            } == {record.left, record.right}
            for left_node, right_node, record in zip(
                walk_nodes,
                walk_nodes[1:],
                selected,
            )
        ):
            return True
    return False


def divisors(value: int) -> tuple[int, ...]:
    return tuple(
        candidate
        for candidate in range(1, value + 1)
        if value % candidate == 0
    )


def verify_factor_classification() -> tuple[int, int, int, FactorCertificate]:
    modular_factors = 0
    real_factors = 0
    quotient_records = 0
    example: FactorCertificate | None = None

    for prime in (5, 7, 11, 13):
        points = tuple(
            (x, y)
            for x in range(1, prime)
            for y in range(1, prime)
        )
        logs = logarithm_table(prime)
        for triple in combinations(points, 3):
            det = determinant(*triple)
            if det % prime:
                continue
            certificate = classify_factor(prime, triple)
            modular_factors += 1
            if det == 0:
                real_factors += 1

            for route in certificate.carry_routes:
                for (residue, carry), point in zip(
                    route.signature,
                    route.endpoints,
                ):
                    assert point[0] * point[1] == residue + prime * carry
                if det == 0 and route.cross_levels is not None:
                    assert route.cross_levels[0] == route.cross_levels[1]

            if certificate.rational_records:
                forward, reverse = certificate.rational_records
                if (
                    example is None
                    and forward.parameter != forward.collision_partner
                ):
                    example = certificate
                assert (
                    forward.cross_at_endpoint
                    == forward.cross_at_partner
                ) == (det == 0)
                for quotient_order in divisors(prime - 1):
                    options = factor_quotient_options(
                        modular_factors,
                        certificate,
                        quotient_order,
                        logs,
                    )
                    assert not isinstance(options, CarryOnlyEdge)
                    quotient_records += len(options)
            else:
                carry_only = factor_quotient_options(
                    modular_factors,
                    certificate,
                    prime - 1,
                    logs,
                )
                assert isinstance(carry_only, CarryOnlyEdge)

    assert example is not None
    return modular_factors, real_factors, quotient_records, example


def verify_fixed_compatibility() -> int:
    checked = 0
    for order in range(1, 5):
        root = 0
        edge_pool = tuple(
            transition(0, 0, root, left, right, order)
            for left in range(order)
            for right in range(left, order)
        )
        for cycle_length in (2, 3):
            walk = tuple(range(cycle_length)) + (0,)
            for selected in product(edge_pool, repeat=cycle_length):
                indexed = tuple(
                    QuotientTransition(
                        source_factor=index,
                        normalization=record.normalization,
                        root=record.root,
                        left=record.left,
                        right=record.right,
                        colour=record.colour,
                    )
                    for index, record in enumerate(selected)
                )
                result = fixed_transition_labels(walk, indexed, order)
                assert (
                    result["status"] == "compatible"
                ) == brute_fixed_compatible(walk, indexed, order)
                checked += 1

        loop = (0, 0)
        for record in edge_pool:
            indexed = (
                QuotientTransition(
                    source_factor=0,
                    normalization=record.normalization,
                    root=record.root,
                    left=record.left,
                    right=record.right,
                    colour=record.colour,
                ),
            )
            result = fixed_transition_labels(loop, indexed, order)
            assert (
                result["status"] == "compatible"
            ) == brute_fixed_compatible(loop, indexed, order)
            checked += 1

        if order <= 3:
            for walk in (
                (0, 1, 0, 2, 0),
                (0, 1, 2, 1, 0),
            ):
                for selected in product(edge_pool, repeat=4):
                    indexed = tuple(
                        QuotientTransition(
                            source_factor=index,
                            normalization=record.normalization,
                            root=record.root,
                            left=record.left,
                            right=record.right,
                            colour=record.colour,
                        )
                        for index, record in enumerate(selected)
                    )
                    result = fixed_transition_labels(
                        walk,
                        indexed,
                        order,
                    )
                    assert (
                        result["status"] == "compatible"
                    ) == brute_fixed_compatible(
                        walk,
                        indexed,
                        order,
                    )
                    checked += 1
    return checked


def verify_bicycle_gate(example: FactorCertificate) -> int:
    prime = example.prime
    logs = logarithm_table(prime)
    order = prime - 1
    geometric_options = factor_quotient_options(
        0,
        example,
        order,
        logs,
    )
    assert not isinstance(geometric_options, CarryOnlyEdge)
    geometric = orient_rational_bicycle(
        (0, 1, 0),
        (geometric_options, geometric_options),
        order,
    )
    assert geometric["status"] == "rational_admissible"
    assert all(
        record.certificate == example
        for record in geometric["selected"]
    )

    consistent = (
        (transition(0, 0, 2, 1, 3, 7),),
        (
            transition(1, 0, 2, 0, 6, 7),
            transition(1, 1, 2, 3, 4, 7),
        ),
        (transition(2, 0, 2, 1, 4, 7),),
    )
    # The first normalization at edge 1 fails; the second gives
    # labels 1,3,4 around the triangle.
    choice = orient_rational_bicycle(
        (0, 1, 2, 0),
        consistent,
        7,
    )
    assert choice["status"] == "rational_admissible"
    assert choice["normalizations"] == (0, 1, 0)
    assert choice["normalization_trials"] == 2

    incompatible = (
        (transition(0, 0, 0, 0, 1, 5),),
        (transition(1, 0, 0, 1, 2, 5),),
        (transition(2, 0, 0, 3, 0, 5),),
    )
    failure = orient_rational_bicycle(
        (0, 1, 2, 0),
        incompatible,
        5,
    )
    assert failure["status"] == "literal_root_mismatch"
    assert failure["normalization_trials"] == 1

    geometric_loop = orient_rational_bicycle(
        (0, 0),
        (geometric_options,),
        order,
    )
    assert geometric_loop["status"] == "literal_root_mismatch"
    assert geometric_loop["source_certificates"] == (example,)

    points = tuple(
        (x, y)
        for x in range(1, prime)
        for y in range(1, prime)
    )
    other_certificate = next(
        certificate
        for triple in combinations(points, 3)
        if determinant(*triple) % prime == 0
        for certificate in (classify_factor(prime, triple),)
        if certificate.rational_records
        and (
            logs[certificate.rational_records[0].root] % order
            != geometric_options[0].root
        )
    )
    other_options = factor_quotient_options(
        1,
        other_certificate,
        order,
        logs,
    )
    assert not isinstance(other_options, CarryOnlyEdge)
    mismatch = orient_rational_bicycle(
        (0, 1, 0),
        (geometric_options, other_options),
        order,
    )
    assert mismatch["status"] == "root_mismatch"
    assert mismatch["certificate"] == other_certificate

    carry_points = next(
        triple
        for triple in combinations(
            tuple(
                (x, y)
                for x in range(1, prime)
                for y in range(1, prime)
            ),
            3,
        )
        if determinant(*triple) % prime == 0
        and len({channel(point, prime) for point in triple}) == 3
    )
    carry_certificate = classify_factor(prime, carry_points)
    carry_edge = factor_quotient_options(
        1,
        carry_certificate,
        order,
        logs,
    )
    assert isinstance(carry_edge, CarryOnlyEdge)
    carry_result = orient_rational_bicycle(
        (0, 1, 0),
        (geometric_options, carry_edge),
        order,
    )
    assert carry_result["status"] == "carry_output"
    return 6


def main() -> None:
    (
        modular_factors,
        real_factors,
        quotient_records,
        example,
    ) = verify_factor_classification()
    fixed_instances = verify_fixed_compatibility()
    gate_cases = verify_bicycle_gate(example)
    print(
        "phase geometric labels verified:",
        f"{modular_factors} modular factors,",
        f"{real_factors} real factors,",
        f"{quotient_records} quotient records,",
        f"{fixed_instances} compatibility instances,",
        f"{gate_cases} routed gate cases",
    )


if __name__ == "__main__":
    main()
