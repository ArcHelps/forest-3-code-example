"""Illustrative FOREST-3 thermal processing; not actual flight software."""

import math

# ARC-FOREST3-SYS-006
REQUIRED_INTERFACES = ("power", "payload", "storage", "attitude", "telemetry")


# ARC-FOREST3-REQ-048
def initialize_observation(readiness: dict[str, bool]) -> bool:
    """Allow acquisition only when all example interfaces are ready."""
    return all(readiness.get(name) is True for name in REQUIRED_INTERFACES)


# ARC-FOREST3-REQ-050
# ARC-FOREST3-RSK-005
def process_observation(
    mwir_kelvin: float,
    lwir_kelvin: float,
    *,
    calibration: str,
    attitude_valid: bool,
) -> bool:
    """Classify one example scene using the A1 temperature thresholds."""
    if not calibration or not attitude_valid:
        raise ValueError("A calibrated scene and valid attitude are required.")
    if not all(math.isfinite(value) for value in (mwir_kelvin, lwir_kelvin)):
        raise ValueError("Temperatures must be finite values in kelvin.")
    return mwir_kelvin >= 330 and mwir_kelvin - lwir_kelvin >= 10
