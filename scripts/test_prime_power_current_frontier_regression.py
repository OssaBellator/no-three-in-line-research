#!/usr/bin/env python3
"""Negative tests for the current-frontier regression contract.

These tests deliberately corrupt each source-level invariant and require the regression helpers to reject the
mutation. They validate the validator rather than any mathematical theorem.
"""
from __future__ import annotations

import copy
import tempfile
import unittest
from pathlib import Path

import run_prime_power_current_frontier_regression as regression


class CurrentFrontierRegressionMutationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.scripts_dir = Path(__file__).resolve().parent
        cls.atomic_path = cls.scripts_dir / "check_prime_power_atomic_frontier_execution.py"
        cls.target_rows = regression.literal_assignment(cls.atomic_path, "TARGET_ROWS")
        cls.frontiers = regression.literal_assignment(cls.atomic_path, "FRONTIERS")

    def assert_regression_rejects(self, callback) -> None:
        with self.assertRaises(regression.CurrentFrontierRegressionError):
            callback()

    def test_canonical_target_frontier_literals_pass(self) -> None:
        targets, frontiers = regression.validate_target_frontier_literals(
            copy.deepcopy(self.target_rows), copy.deepcopy(self.frontiers)
        )
        self.assertEqual(len(targets), 43)
        self.assertEqual(len(frontiers), 13)

    def test_missing_target_is_rejected(self) -> None:
        rows = copy.deepcopy(self.target_rows)
        rows.pop()
        self.assert_regression_rejects(
            lambda: regression.validate_target_frontier_literals(rows, self.frontiers)
        )

    def test_duplicate_or_nonsequential_target_is_rejected(self) -> None:
        rows = copy.deepcopy(self.target_rows)
        duplicate = list(rows[1])
        duplicate[0] = rows[0][0]
        rows[1] = tuple(duplicate)
        self.assert_regression_rejects(
            lambda: regression.validate_target_frontier_literals(rows, self.frontiers)
        )

    def test_unknown_frontier_is_rejected(self) -> None:
        rows = copy.deepcopy(self.target_rows)
        mutated = list(rows[0])
        mutated[1] = "F99_UNKNOWN"
        rows[0] = tuple(mutated)
        self.assert_regression_rejects(
            lambda: regression.validate_target_frontier_literals(rows, self.frontiers)
        )

    def test_empty_frontier_title_is_rejected(self) -> None:
        frontiers = copy.deepcopy(self.frontiers)
        first = next(iter(frontiers))
        frontiers[first] = ""
        self.assert_regression_rejects(
            lambda: regression.validate_target_frontier_literals(self.target_rows, frontiers)
        )

    def test_missing_endpoint_honesty_marker_is_rejected(self) -> None:
        self.assert_regression_rejects(
            lambda: regression.validate_endpoint_text("endpoint.py", "print('documentary')\n")
        )

    def test_endpoint_syntax_error_is_rejected(self) -> None:
        self.assertRaises(SyntaxError, regression.validate_endpoint_text, "endpoint.py", "all_n_proved_by_checker =")

    def test_missing_document_marker_is_rejected(self) -> None:
        self.assert_regression_rejects(
            lambda: regression.validate_document_markers(
                "STATUS.md", "the conjecture remains open", ("CMR2691",)
            )
        )

    def test_failing_self_test_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            scripts = root / "scripts"
            scripts.mkdir()
            (scripts / "fail.py").write_text("raise SystemExit(7)\n", encoding="utf-8")
            self.assert_regression_rejects(lambda: regression.run_self_test(root, "fail.py", "--x"))

    def test_silent_self_test_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            scripts = root / "scripts"
            scripts.mkdir()
            (scripts / "silent.py").write_text("pass\n", encoding="utf-8")
            self.assert_regression_rejects(lambda: regression.run_self_test(root, "silent.py", "--x"))

    def test_successful_self_test_is_recorded(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            scripts = root / "scripts"
            scripts.mkdir()
            (scripts / "ok.py").write_text("print('ok')\n", encoding="utf-8")
            result = regression.run_self_test(root, "ok.py", "--x")
            self.assertEqual(result["returncode"], 0)
            self.assertEqual(result["stdout"], "ok")

    def test_regression_honesty_value_is_fixed(self) -> None:
        self.assertIn("all_n_proved_by_checker", regression.__doc__ or "")
        self.assertEqual(regression.CANONICAL_ENDPOINTS[-1], "check_prime_power_final_support_handoff_frontiers_v2.py")
        self.assertIn(("check_prime_power_all_open_target_fixture.py", "--self-test"), regression.SELF_TESTS)


if __name__ == "__main__":
    unittest.main(verbosity=2)
