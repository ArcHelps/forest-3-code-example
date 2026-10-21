"""Illustrative FOREST-3 test plans.

These records describe the demo scenario; they are not flight software,
executed test results, or evidence of compliance.
"""

RECORDS = [
    # ARC-FOREST3-TPL-001
    {
        'reference': 'PLAN-SUBSYSTEM',
        'name': 'Spacecraft subsystem verification',
        'objective': 'Spacecraft subsystem verification for the defined mission scenario.',
        'entry_criteria': 'Pin the selected configuration, procedure and inputs. Establish the prerequisites and evidence for each selected case.',
        'exit_criteria': 'Record selected-case outcomes and evidence; retain failures, coverage gaps, the STR-007 gap and unresolved constraint or qualification findings. Mission acceptance remains open.',
    },

    # ARC-FOREST3-TPL-002
    {
        'reference': 'PLAN-INTEGRATED',
        'name': 'Integrated mission and ground verification',
        'objective': 'Integrated mission and ground verification for the defined mission scenario.',
        'entry_criteria': 'Pin the selected configuration, procedure and inputs. Establish the prerequisites and evidence for each selected case.',
        'exit_criteria': 'Record selected-case outcomes and evidence; retain failures, coverage gaps, the STR-007 gap and unresolved constraint or qualification findings. Mission acceptance remains open.',
    },

    # ARC-FOREST3-TPL-003
    {
        'reference': 'PLAN-ACCEPTANCE',
        'name': 'Customer acceptance and verification control',
        'objective': 'Customer acceptance and verification control for the defined mission scenario.',
        'entry_criteria': 'Pin the selected configuration, procedure and inputs. Establish the prerequisites and evidence for each selected case.',
        'exit_criteria': 'Record selected-case outcomes and evidence; retain failures, coverage gaps, the STR-007 gap and unresolved constraint or qualification findings. Mission acceptance remains open.',
    },

]
