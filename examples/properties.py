"""Illustrative FOREST-3 properties.

These records describe the demo scenario; they are not flight software,
executed test results, or evidence of compliance.
"""

RECORDS = [
    # ARC-FOREST3-PROP-001
    {
        'reference': 'STR_mass',
        'name': 'STR mass',
        'expression': '2.4 kg',
        'unit': 'kg',
    },

    # ARC-FOREST3-PROP-002
    {
        'reference': 'STR_mass_limit',
        'name': 'STR mass limit',
        'expression': '2.5 kg',
        'unit': 'kg',
    },

    # ARC-FOREST3-PROP-003
    {
        'reference': 'EPS_mass',
        'name': 'EPS mass',
        'expression': '3.6 kg',
        'unit': 'kg',
    },

    # ARC-FOREST3-PROP-004
    {
        'reference': 'EPS_mass_limit',
        'name': 'EPS mass limit',
        'expression': '4 kg',
        'unit': 'kg',
    },

    # ARC-FOREST3-PROP-005
    {
        'reference': 'OBD_mass',
        'name': 'OBD mass',
        'expression': '1.2 kg',
        'unit': 'kg',
    },

    # ARC-FOREST3-PROP-006
    {
        'reference': 'OBD_mass_limit',
        'name': 'OBD mass limit',
        'expression': '1.25 kg',
        'unit': 'kg',
    },

    # ARC-FOREST3-PROP-007
    {
        'reference': 'PAY_mass',
        'name': 'PAY mass',
        'expression': '3.6 kg',
        'unit': 'kg',
    },

    # ARC-FOREST3-PROP-008
    {
        'reference': 'PAY_mass_limit',
        'name': 'PAY mass limit',
        'expression': '4 kg',
        'unit': 'kg',
    },

    # ARC-FOREST3-PROP-009
    {
        'reference': 'COM_mass',
        'name': 'COM mass',
        'expression': '1.2 kg',
        'unit': 'kg',
    },

    # ARC-FOREST3-PROP-010
    {
        'reference': 'COM_mass_limit',
        'name': 'COM mass limit',
        'expression': '1.25 kg',
        'unit': 'kg',
    },

    # ARC-FOREST3-PROP-011
    {
        'reference': 'ADCS_mass',
        'name': 'ADCS mass',
        'expression': '2.3 kg',
        'unit': 'kg',
    },

    # ARC-FOREST3-PROP-012
    {
        'reference': 'ADCS_mass_limit',
        'name': 'ADCS mass limit',
        'expression': '2.5 kg',
        'unit': 'kg',
    },

    # ARC-FOREST3-PROP-013
    {
        'reference': 'THM_mass',
        'name': 'THM mass',
        'expression': '1.2 kg',
        'unit': 'kg',
    },

    # ARC-FOREST3-PROP-014
    {
        'reference': 'THM_mass_limit',
        'name': 'THM mass limit',
        'expression': '1.25 kg',
        'unit': 'kg',
    },

    # ARC-FOREST3-PROP-015
    {
        'reference': 'vehicle_mass',
        'name': 'Vehicle mass',
        'expression': '@{ref:STR_mass}+@{ref:EPS_mass}+@{ref:OBD_mass}+@{ref:PAY_mass}+@{ref:COM_mass}+@{ref:ADCS_mass}+@{ref:THM_mass}',
        'unit': 'kg',
    },

    # ARC-FOREST3-PROP-016
    {
        'reference': 'vehicle_mass_limit',
        'name': 'Vehicle mass limit',
        'expression': '16 kg',
        'unit': 'kg',
    },

]
