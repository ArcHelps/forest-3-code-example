"""Illustrative FOREST-3 safe-mode recovery; not actual flight software."""


# ARC-FOREST3-REQ-053
def recover_mode(
    *,
    thermal_ok: bool,
    pointing_ok: bool,
    stable_seconds: float,
    authorized_reset: bool,
) -> str:
    """Remain safe until guards, dwell and an authorized reset permit idle."""
    if thermal_ok and pointing_ok and stable_seconds >= 60 and authorized_reset:
        return "idle"
    return "safe"
