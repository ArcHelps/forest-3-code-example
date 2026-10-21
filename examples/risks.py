"""Illustrative FOREST-3 risks.

These records describe the demo scenario; they are not flight software,
executed test results, or evidence of compliance.
"""

RECORDS = [
    # ARC-FOREST3-RSK-001
    {
        'reference': 'R01',
        'name': 'Concurrent demand',
        'cause': 'Imaging and transmitter are enabled together',
        'event': '100 W allocation exceeded',
        'consequence': 'Observation or delivery is interrupted',
    },

    # ARC-FOREST3-RSK-002
    {
        'reference': 'R02',
        'name': 'Invalid geolocation',
        'cause': 'Attitude/time/orbit input is invalid',
        'event': 'Incorrect location is accepted',
        'consequence': 'Customer acts on an incorrect detection',
    },

    # ARC-FOREST3-RSK-003
    {
        'reference': 'R03',
        'name': 'Unusable thermal data',
        'cause': 'Calibration or temperature is out of bounds',
        'event': 'Invalid thermal observation is accepted',
        'consequence': 'Customer receives misleading information',
    },

    # ARC-FOREST3-RSK-004
    {
        'reference': 'R04',
        'name': 'Delivery shortfall',
        'cause': 'Contact is unavailable or backlog is excessive',
        'event': 'Delivery deadline is missed',
        'consequence': 'Wildfire product arrives too late',
    },

    # ARC-FOREST3-RSK-005
    {
        'reference': 'R05',
        'name': 'Interface mismatch',
        'cause': 'Versions, units or timing differ',
        'event': 'Command or product is misinterpreted',
        'consequence': 'Integration fails or output is invalid',
    },

    # ARC-FOREST3-RSK-006
    {
        'reference': 'R06',
        'name': 'Operational permission unresolved',
        'cause': 'Spectrum or deployment approvals are not assessed',
        'event': 'Operational authorization is unavailable',
        'consequence': 'Mission entry is delayed',
    },

    # ARC-FOREST3-RSK-007
    {
        'reference': 'R07',
        'name': 'Vehicle mass growth',
        'cause': 'The 15.5 kg design has limited margin below the 16 kg ceiling',
        'event': 'Added hardware consumes the remaining allowance',
        'consequence': 'The vehicle mass limit or integration margin is exceeded',
    },

    # ARC-FOREST3-RSK-008
    {
        'reference': 'R08',
        'name': 'Structural access gap',
        'cause': 'STR-007 access provisions are not fully verified',
        'event': 'Inspection or harness access is unavailable',
        'consequence': 'Integration rework or verification delay occurs',
    },

    # ARC-FOREST3-RSK-009
    {
        'reference': 'R09',
        'name': 'Thermal excursion',
        'cause': 'Thermal control margin is consumed',
        'event': 'Payload or electronics exceed operating range',
        'consequence': 'Observation quality or hardware availability is lost',
    },

    # ARC-FOREST3-RSK-010
    {
        'reference': 'R10',
        'name': 'Pointing loss',
        'cause': 'Attitude validity is lost during exposure',
        'event': 'Invalid pointing is accepted',
        'consequence': 'Geolocation or detection quality is degraded',
    },

    # ARC-FOREST3-RSK-011
    {
        'reference': 'R11',
        'name': 'Command replay or spoofing',
        'cause': 'Command authentication or sequence checks fail',
        'event': 'Replay or unauthorized command is accepted',
        'consequence': 'Mode or payload state changes without authorization',
    },

    # ARC-FOREST3-RSK-012
    {
        'reference': 'R12',
        'name': 'Product integrity loss',
        'cause': 'Product hash or metadata is altered in transit',
        'event': 'Corrupted data is published',
        'consequence': 'Customer receives an incorrect observation',
    },

    # ARC-FOREST3-RSK-013
    {
        'reference': 'R13',
        'name': 'Configuration drift',
        'cause': 'Software and configuration identifiers diverge',
        'event': 'A run uses an unreviewed configuration',
        'consequence': 'Results cannot be reproduced or trusted',
    },

    # ARC-FOREST3-RSK-014
    {
        'reference': 'R14',
        'name': 'Software rollback failure',
        'cause': 'The inactive image or rollback path is invalid',
        'event': 'A failed update cannot restore the active image',
        'consequence': 'Safe operations are delayed',
    },

    # ARC-FOREST3-RSK-015
    {
        'reference': 'R15',
        'name': 'Storage exhaustion',
        'cause': 'Product retention outpaces downlink',
        'event': 'Onboard storage fills before acknowledgement',
        'consequence': 'Observation data is dropped or acquisition stops',
    },

    # ARC-FOREST3-RSK-016
    {
        'reference': 'R16',
        'name': 'Contact outage',
        'cause': 'Ground contact is unavailable',
        'event': 'Queued product misses its delivery window',
        'consequence': 'Wildfire information arrives late',
    },

    # ARC-FOREST3-RSK-017
    {
        'reference': 'R17',
        'name': 'Supply component delay',
        'cause': 'A critical component or material is unavailable',
        'event': 'Integration schedule slips',
        'consequence': 'Mission delivery date is delayed',
    },

    # ARC-FOREST3-RSK-018
    {
        'reference': 'R18',
        'name': 'Parts compatibility variance',
        'cause': 'A supplied part differs from the controlled interface',
        'event': 'Mount, electrical or data integration fails',
        'consequence': 'Rework or unsafe energization occurs',
    },

    # ARC-FOREST3-RSK-019
    {
        'reference': 'R19',
        'name': 'Ground integration damage',
        'cause': 'Handling or harness work damages hardware',
        'event': 'A latent integration fault escapes inspection',
        'consequence': 'Test failure or hardware loss occurs',
    },

    # ARC-FOREST3-RSK-020
    {
        'reference': 'R20',
        'name': 'Verification evidence gap',
        'cause': 'Planned verification has no execution evidence',
        'event': 'A requirement is treated as verified',
        'consequence': 'Acceptance decision is unsupported',
    },

    # ARC-FOREST3-RSK-021
    {
        'reference': 'R21',
        'name': 'Uncovered requirement',
        'cause': 'STR-007 has no linked verification test',
        'event': 'Access compliance is not checked',
        'consequence': 'Integration obstruction remains undiscovered',
    },

    # ARC-FOREST3-RSK-022
    {
        'reference': 'R22',
        'name': 'Regulatory qualification gap',
        'cause': 'Launch, spectrum or environmental obligations are not assessed',
        'event': 'External approval is assumed',
        'consequence': 'Operations cannot be authorized',
    },

    # ARC-FOREST3-RSK-023
    {
        'reference': 'R23',
        'name': 'Calibration drift',
        'cause': 'Calibration or bad-pixel behavior drifts',
        'event': 'Hotspot classification changes',
        'consequence': 'False or missed detection reaches the customer',
    },

    # ARC-FOREST3-RSK-024
    {
        'reference': 'R24',
        'name': 'Interface timing mismatch',
        'cause': 'Endpoint timing or units differ',
        'event': 'Telemetry, commands or products are misinterpreted',
        'consequence': 'Integration or operations fail',
    },

    # ARC-FOREST3-RSK-025
    {
        'reference': 'R25',
        'name': 'Unauthorized product release',
        'cause': 'Access controls on delivered products are misconfigured',
        'event': 'Observation data is released to an unauthorized customer',
        'consequence': 'Confidentiality or trust is lost',
    },

]
