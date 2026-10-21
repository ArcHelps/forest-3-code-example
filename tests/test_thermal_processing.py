"""Illustrative checks for the FOREST-3 code-link example, not flight qualification."""

import unittest

from src.fault_handling import recover_mode
from src.thermal_processing import initialize_observation, process_observation


class ThermalProcessingTests(unittest.TestCase):
    # ARC-FOREST3-TST-047 ARC-FOREST3-REQ-048
    def test_missing_prerequisite_prevents_acquisition(self):
        ready = {
            name: True
            for name in ("power", "payload", "storage", "attitude", "telemetry")
        }
        self.assertTrue(initialize_observation(ready))
        for missing in ready:
            with self.subTest(missing=missing):
                self.assertFalse(initialize_observation({**ready, missing: False}))

    # ARC-FOREST3-TST-049 ARC-FOREST3-REQ-050
    def test_scene_thresholds_and_invalid_inputs(self):
        self.assertTrue(
            process_observation(340, 320, calibration="A1", attitude_valid=True)
        )
        self.assertTrue(
            process_observation(330, 320, calibration="A1", attitude_valid=True)
        )
        self.assertFalse(
            process_observation(329, 310, calibration="A1", attitude_valid=True)
        )
        self.assertFalse(
            process_observation(340, 331, calibration="A1", attitude_valid=True)
        )
        for calibration, attitude, temperature in (
            ("", True, 340),
            ("A1", False, 340),
            ("A1", True, float("nan")),
        ):
            with self.subTest(
                calibration=calibration, attitude=attitude, temperature=temperature
            ):
                with self.assertRaises(ValueError):
                    process_observation(
                        temperature,
                        320,
                        calibration=calibration,
                        attitude_valid=attitude,
                    )

    # ARC-FOREST3-TST-052 ARC-FOREST3-REQ-053
    def test_recovery_requires_dwell_and_authorized_reset(self):
        self.assertEqual(
            recover_mode(
                thermal_ok=False,
                pointing_ok=True,
                stable_seconds=90,
                authorized_reset=True,
            ),
            "safe",
        )
        self.assertEqual(
            recover_mode(
                thermal_ok=True,
                pointing_ok=False,
                stable_seconds=90,
                authorized_reset=True,
            ),
            "safe",
        )
        self.assertEqual(
            recover_mode(
                thermal_ok=True,
                pointing_ok=True,
                stable_seconds=59,
                authorized_reset=True,
            ),
            "safe",
        )
        self.assertEqual(
            recover_mode(
                thermal_ok=True,
                pointing_ok=True,
                stable_seconds=60,
                authorized_reset=False,
            ),
            "safe",
        )
        self.assertEqual(
            recover_mode(
                thermal_ok=True,
                pointing_ok=True,
                stable_seconds=60,
                authorized_reset=True,
            ),
            "idle",
        )


if __name__ == "__main__":
    unittest.main()
