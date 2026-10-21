"""Illustrative FOREST-3 requirements.

These records describe the demo scenario; they are not flight software,
executed test results, or evidence of compliance.
"""

RECORDS = [
    # ARC-FOREST3-REQ-001
    {
        'reference': 'CUST-001',
        'name': 'Customer wildfire information',
        'statement': 'The wildfire monitoring service shall deliver time-stamped, geolocated wildfire information and supporting thermal observations for the customer areas defined in the agreed service acceptance specification.',
    },

    # ARC-FOREST3-REQ-002
    {
        'reference': 'MIS-001',
        'name': 'Observation-to-customer mission chain',
        'statement': 'The mission shall deliver wildfire-relevant information derived from spacecraft thermal observations to a ground user through a documented observation, processing, downlink, and ground-delivery chain.',
    },

    # ARC-FOREST3-REQ-003
    {
        'reference': 'MIS-002',
        'name': '8U spacecraft integration',
        'statement': 'The spacecraft shall use an 8U CubeSat platform with its mechanical envelope and integration constraints defined in the controlled configuration.',
    },

    # ARC-FOREST3-REQ-004
    {
        'reference': 'MIS-003',
        'name': 'Spacecraft and ground architecture',
        'statement': 'The mission architecture shall identify the spacecraft Structures, EPS, OBD, Software, Thermal Payload, Communications, ADCS, and Thermal Control subsystems and the ground segment, with their responsibilities and interfaces.',
    },

    # ARC-FOREST3-REQ-005
    {
        'reference': 'MIS-004',
        'name': 'Thermal observation and processing',
        'statement': 'The spacecraft shall acquire thermal observations in the mid-wave and long-wave infrared bands and process the acquired data onboard to support wildfire-information generation.',
    },

    # ARC-FOREST3-REQ-006
    {
        'reference': 'MIS-005',
        'name': 'Telemetry and command',
        'statement': 'The mission shall exchange spacecraft commands and operational telemetry with the ground segment through defined communication interfaces.',
    },

    # ARC-FOREST3-REQ-007
    {
        'reference': 'MIS-006',
        'name': 'Operating modes and fault management',
        'statement': 'The spacecraft shall implement documented operating modes and fault responses that control mission operations and place the spacecraft in the defined safe condition when required.',
    },

    # ARC-FOREST3-REQ-008
    {
        'reference': 'MIS-007',
        'name': 'Power, thermal and pointing capability',
        'statement': 'The spacecraft shall provide the electrical power, thermal conditions, and pointing capability required to execute the documented observation and communication mission sequence.',
    },

    # ARC-FOREST3-REQ-009
    {
        'reference': 'MIS-008',
        'name': 'Controlled engineering information',
        'statement': 'The mission shall maintain controlled configuration records, engineering drawings, interface definitions, software documentation, a concept of operations, integration procedures, and a verification control document.',
    },

    # ARC-FOREST3-REQ-010
    {
        'reference': 'MIS-009',
        'name': 'Verification and acceptance',
        'statement': 'The mission shall assess every applicable requirement against its planned verification activity and record the evidence, outcome, and acceptance disposition in the verification control document.',
    },

    # ARC-FOREST3-REQ-011
    {
        'reference': 'MIS-BUD-DATA',
        'name': 'Spacecraft data allocation',
        'statement': 'The spacecraft generated data rate shall not exceed 5,025,000 bit/s, and its reference pass volume shall not exceed 750,000,000 bit.',
    },

    # ARC-FOREST3-REQ-012
    {
        'reference': 'MIS-BUD-MASS',
        'name': 'Spacecraft mass allocation',
        'statement': 'The spacecraft mass total of {{property:ref:vehicle_mass}}, obtained from its distinct physical contributors, shall not exceed {{property:ref:vehicle_mass_limit}}.',
    },

    # ARC-FOREST3-REQ-013
    {
        'reference': 'MIS-BUD-POWER',
        'name': 'Spacecraft power allocation',
        'statement': 'The spacecraft demand for the defined mission scenario shall not exceed 100 W of available power on the defined comparison basis.',
    },

    # ARC-FOREST3-REQ-014
    {
        'reference': 'STR-001',
        'name': 'Equipment integration',
        'statement': 'The spacecraft structure shall support and integrate the spacecraft equipment in the controlled mechanical configuration.',
    },

    # ARC-FOREST3-REQ-015
    {
        'reference': 'STR-002',
        'name': '8U mechanical envelope',
        'statement': 'The spacecraft structure shall comply with the controlled mechanical envelope and interface definition for the selected 8U platform.',
    },

    # ARC-FOREST3-REQ-016
    {
        'reference': 'STR-003',
        'name': 'Environmental compatibility',
        'statement': 'The spacecraft primary structural materials and joints shall have documented suitability for the defined mechanical and thermal environments.',
    },

    # ARC-FOREST3-REQ-017
    {
        'reference': 'STR-004',
        'name': 'Equipment mounting interfaces',
        'statement': 'The spacecraft structure shall provide documented mounting interfaces for the payload and all spacecraft subsystem equipment.',
    },

    # ARC-FOREST3-REQ-018
    {
        'reference': 'STR-005',
        'name': 'Electrical and mechanical clearances',
        'statement': 'The spacecraft structural arrangement shall maintain the defined clearances needed to prevent unintended electrical contact and mechanical interference.',
    },

    # ARC-FOREST3-REQ-019
    {
        'reference': 'STR-006',
        'name': 'Controlled CAD model',
        'statement': 'The spacecraft structural configuration shall be defined in a controlled three-dimensional CAD model.',
    },

    # ARC-FOREST3-REQ-020
    {
        'reference': 'STR-007',
        'name': 'Inspection and integration access',
        'statement': 'The spacecraft ground assembly configuration shall provide documented access for the inspections, integration tasks, and verification connections identified in the assembly and verification procedures.',
    },

    # ARC-FOREST3-REQ-021
    {
        'reference': 'STR-008',
        'name': 'Solar hardware interfaces',
        'statement': 'The spacecraft structure shall provide controlled mechanical interfaces for the selected solar power-generation hardware.',
    },

    # ARC-FOREST3-REQ-022
    {
        'reference': 'STR-009',
        'name': 'Structural handling hazards',
        'statement': 'The spacecraft structure and ground handling provisions shall control the structural handling hazards identified in the ground integration risk assessment.',
    },

    # ARC-FOREST3-REQ-023
    {
        'reference': 'STR-BUD-MASS',
        'name': 'STR mass allocation',
        'statement': 'The STR mass contribution of {{property:ref:STR_mass}} shall not exceed its allocated limit of {{property:ref:STR_mass_limit}}.',
    },

    # ARC-FOREST3-REQ-024
    {
        'reference': 'EPS-001',
        'name': 'Operating-mode power supply',
        'statement': 'The Electrical Power System shall supply the electrical loads required by each defined spacecraft operating mode.',
    },

    # ARC-FOREST3-REQ-025
    {
        'reference': 'EPS-002',
        'name': 'Solar power generation',
        'statement': 'The Electrical Power System shall provide solar electrical generation for the mission phases in which solar generation is specified.',
    },

    # ARC-FOREST3-REQ-026
    {
        'reference': 'EPS-003',
        'name': 'Stored energy capacity',
        'statement': 'The Electrical Power System shall provide stored electrical energy for mission phases in which generation alone does not supply the required loads.',
    },

    # ARC-FOREST3-REQ-027
    {
        'reference': 'EPS-004',
        'name': 'Energy-storage limits and interfaces',
        'statement': 'The energy-storage configuration shall document its rated capacity, allowable operating limits, and compatibility with the spacecraft electrical interfaces.',
    },

    # ARC-FOREST3-REQ-028
    {
        'reference': 'EPS-005',
        'name': 'Power-system status telemetry',
        'statement': 'The Electrical Power System shall provide power-system status information to the spacecraft telemetry function.',
    },

    # ARC-FOREST3-REQ-029
    {
        'reference': 'EPS-006',
        'name': 'Load switching and power inhibits',
        'statement': 'The Electrical Power System shall control electrical load switching and power inhibits according to the approved spacecraft mode and fault-response definitions.',
    },

    # ARC-FOREST3-REQ-030
    {
        'reference': 'EPS-007',
        'name': 'Regulated power limits',
        'statement': 'The Electrical Power System shall regulate supplied power where required to meet the controlled electrical limits of connected spacecraft equipment.',
    },

    # ARC-FOREST3-REQ-031
    {
        'reference': 'EPS-008',
        'name': 'Electrical protection functions',
        'statement': 'The Electrical Power System shall implement the electrical protection functions specified for connected loads and fault conditions.',
    },

    # ARC-FOREST3-REQ-032
    {
        'reference': 'EPS-009',
        'name': 'Controlled electrical interfaces',
        'statement': 'Electrical connections between the EPS and other spacecraft subsystems shall use controlled, identifiable interface definitions.',
    },

    # ARC-FOREST3-REQ-033
    {
        'reference': 'EPS-010',
        'name': 'Prevent prohibited short-circuit paths',
        'statement': 'The EPS assembly and harness configuration shall prevent prohibited short-circuit paths identified by the electrical design and integration risk assessment.',
    },

    # ARC-FOREST3-REQ-034
    {
        'reference': 'EPS-BUD-MASS',
        'name': 'EPS mass allocation',
        'statement': 'The EPS mass contribution of {{property:ref:EPS_mass}} shall not exceed its allocated limit of {{property:ref:EPS_mass_limit}}.',
    },

    # ARC-FOREST3-REQ-035
    {
        'reference': 'EPS-BUD-POWER',
        'name': 'EPS power allocation',
        'statement': 'The EPS power demand in the reference operating scenario shall not exceed 6.25 W.',
    },

    # ARC-FOREST3-REQ-036
    {
        'reference': 'OBD-001',
        'name': 'Payload data path',
        'statement': 'The OBD subsystem shall acquire, manage, and process thermal payload data through the documented onboard data path.',
    },

    # ARC-FOREST3-REQ-037
    {
        'reference': 'OBD-002',
        'name': 'Onboard computing platform',
        'statement': 'The OBD subsystem shall provide a programmable onboard computing platform for the allocated spacecraft control and payload-data functions.',
    },

    # ARC-FOREST3-REQ-038
    {
        'reference': 'OBD-003',
        'name': 'Payload data and metadata intake',
        'statement': 'The OBD subsystem shall receive thermal observation data and associated identification metadata from the payload.',
    },

    # ARC-FOREST3-REQ-039
    {
        'reference': 'OBD-004',
        'name': 'Onboard processing chain',
        'statement': 'The OBD subsystem shall execute the controlled onboard processing chain used to derive wildfire-relevant information from acquired thermal observations.',
    },

    # ARC-FOREST3-REQ-040
    {
        'reference': 'OBD-005',
        'name': 'Telemetry state and health data',
        'statement': 'The OBD subsystem shall collect and expose the operational state and health information allocated to spacecraft telemetry.',
    },

    # ARC-FOREST3-REQ-041
    {
        'reference': 'OBD-008',
        'name': 'Payload electrical and data interfaces',
        'statement': 'The OBD subsystem shall provide the controlled electrical and data interfaces required to connect and operate the thermal payload.',
    },

    # ARC-FOREST3-REQ-042
    {
        'reference': 'OBD-009',
        'name': 'Controlled software loading',
        'statement': 'The OBD subsystem shall support controlled loading and updating of onboard software through the defined ground integration or mission command interface.',
    },

    # ARC-FOREST3-REQ-043
    {
        'reference': 'OBD-010',
        'name': 'Ground access and verification connections',
        'statement': 'The OBD installation shall provide the ground access and verification connections required by its integration and test procedures.',
    },

    # ARC-FOREST3-REQ-044
    {
        'reference': 'OBD-011',
        'name': 'Observation product retention',
        'statement': 'The OBD subsystem shall retain observation products and their required metadata until confirmed delivery or an approved disposition under the defined observation and contact scenario.',
    },

    # ARC-FOREST3-REQ-045
    {
        'reference': 'OBD-BUD-DATA',
        'name': 'OBD data allocation',
        'statement': 'The spacecraft housekeeping stream generated by OBD shall not exceed 25,000 bit/s on the agreed scenario basis.',
    },

    # ARC-FOREST3-REQ-046
    {
        'reference': 'OBD-BUD-MASS',
        'name': 'OBD mass allocation',
        'statement': 'The OBD mass contribution of {{property:ref:OBD_mass}} shall not exceed its allocated limit of {{property:ref:OBD_mass_limit}}.',
    },

    # ARC-FOREST3-REQ-047
    {
        'reference': 'OBD-BUD-POWER',
        'name': 'OBD power allocation',
        'statement': 'The OBD power demand in the reference operating scenario shall not exceed 12.5 W.',
    },

    # ARC-FOREST3-REQ-048
    {
        'reference': 'SW-001',
        'name': 'Thermal observation initialization',
        'statement': 'The onboard software shall initialise the hardware and data interfaces required for the selected thermal-observation and processing sequence.',
    },

    # ARC-FOREST3-REQ-049
    {
        'reference': 'SW-002',
        'name': 'Thermal observation acquisition',
        'statement': 'The onboard software shall acquire thermal observations and their required metadata according to the commanded observation sequence.',
    },

    # ARC-FOREST3-REQ-050
    {
        'reference': 'SW-003',
        'name': 'Processing outputs',
        'statement': 'The onboard software shall produce wildfire-relevant processing outputs from thermal observations according to a controlled processing specification.',
    },

    # ARC-FOREST3-REQ-051
    {
        'reference': 'SW-004',
        'name': 'Payload-derived information delivery',
        'statement': 'The onboard software shall prepare the required payload-derived information and its identification metadata for delivery through the spacecraft communication interface.',
    },

    # ARC-FOREST3-REQ-052
    {
        'reference': 'SW-005',
        'name': 'Telemetry encoding',
        'statement': 'The onboard software shall encode operational state and health information according to the controlled telemetry dictionary.',
    },

    # ARC-FOREST3-REQ-053
    {
        'reference': 'SW-006',
        'name': 'Mode and fault management',
        'statement': 'The onboard software shall implement the approved mode transitions, fault responses, and recovery rules allocated to software.',
    },

    # ARC-FOREST3-REQ-054
    {
        'reference': 'SW-007',
        'name': 'Controlled software storage',
        'statement': 'The onboard software source and build configuration shall be maintained in controlled versioned storage.',
    },

    # ARC-FOREST3-REQ-055
    {
        'reference': 'SW-008',
        'name': 'Software version traceability',
        'statement': 'Each released version of the onboard software shall have a unique version identifier linked to its controlled source, build, and verification records.',
    },

    # ARC-FOREST3-REQ-056
    {
        'reference': 'SW-009',
        'name': 'Software architecture and interfaces',
        'statement': 'The software documentation shall define the architecture, principal functions, data flows, and allocated mission interfaces of the onboard software.',
    },

    # ARC-FOREST3-REQ-057
    {
        'reference': 'SW-010',
        'name': 'Target configuration verification',
        'statement': 'The onboard software shall be verified on the representative target computing configuration before its applicable requirements are declared accepted.',
    },

    # ARC-FOREST3-REQ-058
    {
        'reference': 'PAY-001',
        'name': 'Thermal imagery acquisition',
        'statement': 'The payload shall acquire thermal-infrared Earth-observation imagery for the mission wildfire-information processing chain.',
    },

    # ARC-FOREST3-REQ-059
    {
        'reference': 'PAY-002',
        'name': 'MWIR and LWIR channels',
        'statement': 'The thermal payload shall provide observation channels in both the mid-wave infrared and long-wave infrared spectral regions.',
    },

    # ARC-FOREST3-REQ-060
    {
        'reference': 'PAY-003',
        'name': 'Thermal data and metadata delivery',
        'statement': 'The payload shall provide thermal observation data and the required observation metadata to the OBD subsystem through the controlled payload interface.',
    },

    # ARC-FOREST3-REQ-061
    {
        'reference': 'PAY-004',
        'name': 'Payload platform interfaces',
        'statement': 'The thermal payload shall use controlled power, command, and observation-data interfaces with the spacecraft platform.',
    },

    # ARC-FOREST3-REQ-062
    {
        'reference': 'PAY-005',
        'name': 'MWIR image quality and calibration',
        'statement': 'The payload shall acquire MWIR observation data meeting the agreed channel image-quality and calibration criteria.',
    },

    # ARC-FOREST3-REQ-063
    {
        'reference': 'PAY-009',
        'name': 'LWIR image quality and calibration',
        'statement': 'The payload shall acquire LWIR observation data meeting the agreed channel image-quality and calibration criteria.',
    },

    # ARC-FOREST3-REQ-064
    {
        'reference': 'PAY-BUD-DATA',
        'name': 'PAY data allocation',
        'statement': 'The thermal observation and payload metadata stream shall not exceed 5,000,000 bit/s on the agreed scenario basis.',
    },

    # ARC-FOREST3-REQ-065
    {
        'reference': 'PAY-BUD-MASS',
        'name': 'PAY mass allocation',
        'statement': 'The PAY mass contribution of {{property:ref:PAY_mass}} shall not exceed its allocated limit of {{property:ref:PAY_mass_limit}}.',
    },

    # ARC-FOREST3-REQ-066
    {
        'reference': 'PAY-BUD-POWER',
        'name': 'PAY power allocation',
        'statement': 'The PAY power demand in the reference operating scenario shall not exceed 60 W.',
    },

    # ARC-FOREST3-REQ-067
    {
        'reference': 'COM-001',
        'name': 'Command and telemetry path',
        'statement': 'The communications subsystem shall provide a defined path for spacecraft commands and housekeeping telemetry between the spacecraft and ground operations.',
    },

    # ARC-FOREST3-REQ-068
    {
        'reference': 'COM-002',
        'name': 'Link margin',
        'statement': 'Each mission radio path shall achieve a link margin of at least 3 dB under the approved link-budget reference conditions.',
    },

    # ARC-FOREST3-REQ-069
    {
        'reference': 'COM-003',
        'name': 'Observation product delivery',
        'statement': 'The communications subsystem shall deliver the agreed observation products and priority messages within its allocated transmission windows.',
    },

    # ARC-FOREST3-REQ-070
    {
        'reference': 'COM-004',
        'name': 'Transfer recovery reporting',
        'statement': 'The communications subsystem shall report interrupted or incomplete transfers so that the approved recovery policy can preserve and subsequently deliver the affected observation products.',
    },

    # ARC-FOREST3-REQ-071
    {
        'reference': 'COM-BUD-MASS',
        'name': 'COM mass allocation',
        'statement': 'The COM mass contribution of {{property:ref:COM_mass}} shall not exceed its allocated limit of {{property:ref:COM_mass_limit}}.',
    },

    # ARC-FOREST3-REQ-072
    {
        'reference': 'COM-BUD-POWER',
        'name': 'COM power allocation',
        'statement': 'The COM power demand in the reference operating scenario shall not exceed 50 W.',
    },

    # ARC-FOREST3-REQ-073
    {
        'reference': 'ADCS-001',
        'name': 'Mission-mode pointing support',
        'statement': 'The attitude-control subsystem shall support the observation, power-generation and communications pointing conditions defined for each authorised mission mode.',
    },

    # ARC-FOREST3-REQ-074
    {
        'reference': 'ADCS-002',
        'name': 'Pointing accuracy and stability',
        'statement': 'The attitude-control subsystem shall maintain observation pointing error at or below 0.1 degree and stability drift at or below 0.01 degree per 10 ms exposure, using the units and time basis specified in the payload interface definition.',
    },

    # ARC-FOREST3-REQ-075
    {
        'reference': 'ADCS-003',
        'name': 'Pointing-loss response',
        'statement': 'The attitude-control subsystem shall report loss of required pointing performance and support the approved spacecraft safe-mode response.',
    },

    # ARC-FOREST3-REQ-076
    {
        'reference': 'ADCS-004',
        'name': 'Attitude and time metadata',
        'statement': 'The attitude-control subsystem shall provide observation-associated attitude, time and validity information in the reference frames defined by the geolocation interface.',
    },

    # ARC-FOREST3-REQ-077
    {
        'reference': 'ADCS-BUD-MASS',
        'name': 'ADCS mass allocation',
        'statement': 'The ADCS mass contribution of {{property:ref:ADCS_mass}} shall not exceed its allocated limit of {{property:ref:ADCS_mass_limit}}.',
    },

    # ARC-FOREST3-REQ-078
    {
        'reference': 'ADCS-BUD-POWER',
        'name': 'ADCS power allocation',
        'statement': 'The ADCS power demand in the reference operating scenario shall not exceed 20 W.',
    },

    # ARC-FOREST3-REQ-079
    {
        'reference': 'THM-001',
        'name': 'Operating temperature control',
        'statement': 'The thermal-control subsystem shall keep the payload and spacecraft equipment within their approved operating-temperature ranges for each scheduled operating mode.',
    },

    # ARC-FOREST3-REQ-080
    {
        'reference': 'THM-002',
        'name': 'Calibration and image-quality temperatures',
        'statement': 'The payload thermal interface shall maintain the thermal conditions required by the approved calibration and image-quality acceptance criteria.',
    },

    # ARC-FOREST3-REQ-081
    {
        'reference': 'THM-003',
        'name': 'Thermal protection response',
        'statement': 'The thermal-control function shall report limit excursions and execute the approved protective response through the spacecraft mode-control interface.',
    },

    # ARC-FOREST3-REQ-082
    {
        'reference': 'THM-004',
        'name': 'Survival temperature control',
        'statement': 'The spacecraft shall remain within the approved equipment survival-temperature ranges during the defined non-operating and safe-mode environmental cases.',
    },

    # ARC-FOREST3-REQ-083
    {
        'reference': 'THM-BUD-MASS',
        'name': 'THM mass allocation',
        'statement': 'The THM mass contribution of {{property:ref:THM_mass}} shall not exceed its allocated limit of {{property:ref:THM_mass_limit}}.',
    },

    # ARC-FOREST3-REQ-084
    {
        'reference': 'THM-BUD-POWER',
        'name': 'THM power allocation',
        'statement': 'The THM power demand in the reference operating scenario shall not exceed 6.25 W.',
    },

    # ARC-FOREST3-REQ-085
    {
        'reference': 'GRD-001',
        'name': 'Command and telemetry records',
        'statement': 'Ground operations shall issue controlled observation and operating-mode commands and record their acknowledgement, execution status and spacecraft telemetry context.',
    },

    # ARC-FOREST3-REQ-086
    {
        'reference': 'GRD-002',
        'name': 'Observation product receipt',
        'statement': 'The ground segment shall receive observation products and preserve their observation time, location, acquisition configuration and processing-version references through delivery to the customer-facing service.',
    },

    # ARC-FOREST3-REQ-087
    {
        'reference': 'GRD-003',
        'name': 'Observation quality classification',
        'statement': 'The ground service shall distinguish accepted detections, rejected data and incomplete products according to the approved quality and confidence rules.',
    },

    # ARC-FOREST3-REQ-088
    {
        'reference': 'GRD-004',
        'name': 'Customer delivery latency',
        'statement': 'The mission delivery chain shall make each accepted observation product available at the agreed customer interface within 900 s of the defined observation reference time for the approved service scenario.',
    },

    # ARC-FOREST3-REQ-089
    {
        'reference': 'INT-001',
        'name': 'Integration activity control',
        'statement': 'All mission interfaces between spacecraft subsystems and the ground segment shall be identified and controlled before the affected integration activity.',
    },

    # ARC-FOREST3-REQ-090
    {
        'reference': 'INT-002',
        'name': 'Electrical interface definition',
        'statement': 'Each electrical interface shall define its endpoints, power or signal function, connection assignments, and applicable electrical operating limits.',
    },

    # ARC-FOREST3-REQ-091
    {
        'reference': 'INT-003',
        'name': 'Integration interface constraints',
        'statement': 'Each mechanical interface shall define its connected items, attachment arrangement, and applicable envelope and interface constraints.',
    },

    # ARC-FOREST3-REQ-092
    {
        'reference': 'INT-004',
        'name': 'Data interface definition',
        'statement': 'Each data interface shall define its source, destination, content, units where applicable, format, and required timing and integrity behaviour.',
    },

    # ARC-FOREST3-REQ-093
    {
        'reference': 'INT-005',
        'name': 'Integration readiness',
        'statement': 'The mission shall complete the planned subsystem verification entry criteria before the affected system-level integration activity.',
    },

    # ARC-FOREST3-REQ-094
    {
        'reference': 'INT-006',
        'name': 'Assembly and integration procedures',
        'statement': 'Spacecraft and ground-chain integration shall be performed using controlled assembly and integration procedures applicable to the reviewed configuration.',
    },

    # ARC-FOREST3-REQ-095
    {
        'reference': 'INT-007',
        'name': 'Engineering record updates',
        'statement': 'Changes to an integrated mission configuration shall be recorded and reflected in the affected design, interface, software, and verification records.',
    },

    # ARC-FOREST3-REQ-096
    {
        'reference': 'VRF-001',
        'name': 'Verification method identification',
        'statement': 'Each applicable mission requirement shall have an identified verification method.',
    },

    # ARC-FOREST3-REQ-097
    {
        'reference': 'VRF-002',
        'name': 'Verification compliance assessment',
        'statement': 'Each applicable mission requirement shall receive a recorded compliance assessment after completion of its planned verification activity.',
    },

    # ARC-FOREST3-REQ-098
    {
        'reference': 'VRF-003',
        'name': 'Test evidence traceability',
        'statement': 'Requirements verified by test shall have objective evidence linked to the applicable test record and tested configuration.',
    },

    # ARC-FOREST3-REQ-099
    {
        'reference': 'VRF-004',
        'name': 'Inspection evidence traceability',
        'statement': 'Requirements verified by inspection shall have objective evidence linked to the inspected configuration and acceptance criterion.',
    },

    # ARC-FOREST3-REQ-100
    {
        'reference': 'VRF-005',
        'name': 'Verification method and results',
        'statement': 'Requirements verified by analysis shall have a documented method, controlled inputs and assumptions, and supporting results.',
    },

    # ARC-FOREST3-REQ-101
    {
        'reference': 'VRF-006',
        'name': 'Acceptance disposition control',
        'statement': 'The mission shall not be declared accepted until every applicable requirement has an assessment and every open noncompliance has a recorded acceptance disposition.',
    },

    # ARC-FOREST3-REQ-102
    {
        'reference': 'OPS-001',
        'name': 'Concurrent imaging and downlink',
        'statement': 'The spacecraft shall support concurrent thermal-image acquisition and communications downlink in its nominal operating profile.',
    },

]
