"""Illustrative FOREST-3 systems.

These records describe the demo scenario; they are not flight software,
executed test results, or evidence of compliance.
"""

RECORDS = [
    # ARC-FOREST3-SYS-001
    {
        'reference': 'SERVICE',
        'name': 'Wildfire information service',
        'description': 'Observation-to-customer chain',
    },

    # ARC-FOREST3-SYS-002
    {
        'reference': 'SPACECRAFT',
        'name': '8U reference spacecraft',
        'description': 'Reference spacecraft configuration',
    },

    # ARC-FOREST3-SYS-003
    {
        'reference': 'STR',
        'name': 'Structure',
        'description': 'Frames, mounts and mechanical supports',
    },

    # ARC-FOREST3-SYS-004
    {
        'reference': 'EPS',
        'name': 'Electrical power',
        'description': 'Panels, battery, control, conversion and power harness',
    },

    # ARC-FOREST3-SYS-005
    {
        'reference': 'OBD',
        'name': 'Onboard data handling',
        'description': 'Computing, retention, command receiver support and data harness',
    },

    # ARC-FOREST3-SYS-006
    {
        'reference': 'SW',
        'name': 'Flight software',
        'description': 'Versioned software unit; no separate hardware mass/power',
    },

    # ARC-FOREST3-SYS-007
    {
        'reference': 'PAY',
        'name': 'Thermal imaging payload',
        'description': 'MWIR/LWIR optical and acquisition assembly',
    },

    # ARC-FOREST3-SYS-008
    {
        'reference': 'COM',
        'name': 'Communications',
        'description': 'Shared S-band transceiver and antenna',
    },

    # ARC-FOREST3-SYS-009
    {
        'reference': 'ADCS',
        'name': 'Attitude determination and control',
        'description': 'Sensors, control and actuators',
    },

    # ARC-FOREST3-SYS-010
    {
        'reference': 'THM',
        'name': 'Thermal control',
        'description': 'Heaters, blankets and straps',
    },

    # ARC-FOREST3-SYS-011
    {
        'reference': 'GRD',
        'name': 'Ground operations and delivery',
        'description': 'Tasking, receive, quality control and publication',
    },

    # ARC-FOREST3-SYS-012
    {
        'reference': 'CUSTOMER',
        'name': 'Customer delivery interface',
        'description': 'Logical software endpoint, excluded from spacecraft budgets',
    },

    # ARC-FOREST3-SYS-013
    {
        'reference': 'DEPLOYER',
        'name': 'External integration fixture',
        'description': 'Ground/deployment boundary',
    },

]
