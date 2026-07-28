#!/usr/bin/env python3
"""Compatibility entrypoint for the canonical obligation artifact-support DAG checker.

The stronger checker requires every proved obligation bundle to reach every artifact in each
immediate prerequisite bundle. This module preserves the earlier import and command name while
delegating all validation and construction to that canonical implementation.
"""
from check_prime_power_obligation_artifact_support_dag import (
    ObligationArtifactSupportError,
    build_certificate,
    exact_certificate,
    main,
    require,
    validate_certificate,
)

ArtifactSupportDagError = ObligationArtifactSupportError


if __name__ == "__main__":
    main()
