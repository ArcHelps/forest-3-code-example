"""Illustrative FOREST-3 test cases.

These records describe the demo scenario; they are not flight software,
executed test results, or evidence of compliance.
"""

RECORDS = [
    # ARC-FOREST3-TST-001
    {
        'reference': 'V-CUST-001',
        'name': 'Customer wildfire information',
        'method': 'test',
        'objective': 'Verify wildfire classification, product metadata, and delivery timing across the ten acceptance cases.',
        'procedure': 'Run the ten labelled scene fixtures through acquisition, processing, contact and publication; compare labels and metadata with expected labels; subtract t=0 from publication times and record each result separately.',
        'acceptance_criteria': 'For the single 20 km × 20 km scene centred at 38.0° N, 23.0° E, all six valid hot cases are detected, both valid cold cases yield no detection, and both invalid cases are rejected; accepted products have UTC error ≤0.1 s, WGS84 location error ≤250 m, both band IDs, calibration ID, attitude/orbit validity and software/configuration version; publication occurs by t=900 s from first acquisition.',
    },

    # ARC-FOREST3-TST-002
    {
        'reference': 'V-MIS-001',
        'name': 'Observation-to-customer mission chain',
        'method': 'test',
        'objective': 'Confirm nominal and outage product delivery preserves IDs, hashes, queue timing, and publication deadline.',
        'procedure': 'Follow one product through the nominal chain and the t=360–420 s outage chain; reconcile IDs, hashes and stage timestamps with the queue calculation.',
        'acceptance_criteria': 'Each accepted product retains its product ID and SHA-256 through acquisition, processing, durable ground receipt and publication; nominal queue receipt is t=495.967742 s and publication ≤555.967742 s; the prescribed outage case publishes ≤616.451613 s.',
    },

    # ARC-FOREST3-TST-003
    {
        'reference': 'V-MIS-002',
        'name': '8U spacecraft integration',
        'method': 'inspection',
        'objective': 'Confirm the spacecraft envelope, attachment geometry, and keep-out volume match the mechanical design.',
        'procedure': 'Measure the three CAD bounding extents and attachment centres; compare with the dimensioned design and inspect the keep-out volume.',
        'acceptance_criteria': 'The stowed representation fits within 226×226×227 mm, has four M4 ground-fixture attachments on a 180×180 mm square and ≥5 mm keep-out. Deployer interfaces remain to be confirmed.',
    },

    # ARC-FOREST3-TST-004
    {
        'reference': 'V-MIS-003',
        'name': 'Spacecraft and ground architecture',
        'method': 'review',
        'objective': 'Confirm the architecture traces acquisition, power, storage, downlink, and publication with single ownership.',
        'procedure': 'Trace acquisition, power, storage, downlink and publication across the architecture and interface register; check ownership once per physical contributor.',
        'acceptance_criteria': 'The architecture names STR, EPS, OBD, SW, PAY, COM, ADCS, THM and ground; every power, data and mechanical interface has two named endpoints and an owner; SW and ground have no spacecraft mass contribution.',
    },

    # ARC-FOREST3-TST-005
    {
        'reference': 'V-MIS-004',
        'name': 'Thermal observation and processing',
        'method': 'test',
        'objective': 'Confirm thermal observations preserve dimensions, timing, processing completion, and expected classifications.',
        'procedure': 'Feed ten labelled MWIR/LWIR pairs and record dimensions, acquisition bounds, processing completion and classifications; compare against independent expected labels.',
        'acceptance_criteria': 'Both 128×128 bands are acquired in the 120 s observation interval and processing finishes by t=180 s; thresholds are MWIR ≥330 K and MWIR−LWIR ≥10 K; the labelled set gives six hot, two cold and two invalid outcomes exactly.',
    },

    # ARC-FOREST3-TST-006
    {
        'reference': 'V-MIS-005',
        'name': 'Telemetry and command',
        'method': 'test',
        'objective': 'Confirm telemetry and command exchange accepts valid records and rejects duplicate, invalid, and unauthorized requests.',
        'procedure': 'Exchange each dictionary command and telemetry record through the simulated link; inject duplicate IDs, invalid integrity and unauthorized requests and inspect execution and rejection records.',
        'acceptance_criteria': 'The shared simulated transceiver carries command acknowledgements and 20,000 bit/s housekeeping during the prescribed contact; duplicate command IDs do not execute twice; corrupted or unauthorized commands do not change mode.',
    },

    # ARC-FOREST3-TST-007
    {
        'reference': 'V-MIS-006',
        'name': 'Operating modes and fault management',
        'method': 'test',
        'objective': 'Confirm permitted mode transitions execute and rejected or faulted transitions enforce safe reset controls.',
        'procedure': 'Exercise each permitted transition, rejected transition and fault; record mode and load states at boundaries and attempt premature and unauthorized resets.',
        'acceptance_criteria': 'The documented modes cover imaging, processing/slew, downlink and safe/idle; thermal or pointing excursions enter safe within 2 s; recovery needs 60 s continuously in range plus authorized reset; CFG-B prevents PAY/COM main-load overlap.',
    },

    # ARC-FOREST3-TST-008
    {
        'reference': 'V-MIS-007',
        'name': 'Power, thermal and pointing capability',
        'method': 'test',
        'objective': 'Confirm the corrected profile meets load, pointing, and temperature limits while retaining the CFG-A concurrency failure.',
        'procedure': 'Replay the 900 s mode profile and sample load, pointing and temperatures at each transition; compare CFG-A concurrency separately and retain failures.',
        'acceptance_criteria': 'CFG-B imaging uses 80 W, downlink 70 W and safe/idle 20 W against 100 W; imaging pointing error ≤0.1° and drift ≤0.01° per 10 ms exposure; operating temperatures remain payload/battery 0–40 °C and electronics −10–50 °C. CFG-A concurrent 120 W is an explicit starting failure.',
    },

    # ARC-FOREST3-TST-009
    {
        'reference': 'V-MIS-008',
        'name': 'Controlled engineering information',
        'method': 'review',
        'objective': 'Confirm controlled engineering documents have consistent titles, revisions, owners, configuration, and references.',
        'procedure': 'Reconcile the package file register with each document title, revision, named owner and configuration; follow every internal document reference.',
        'acceptance_criteria': 'The controlled document register contains requirements, CONOPS, architecture/design, mechanical/electrical/data interfaces, software design/release records, integration procedure and verification plan; each identifies owner, revision and CFG-A/CFG-B applicability.',
    },

    # ARC-FOREST3-TST-010
    {
        'reference': 'V-MIS-009',
        'name': 'Verification and acceptance',
        'method': 'review',
        'objective': 'Confirm every active requirement has an accurate verification record, evidence, and disposition.',
        'procedure': 'Compare the active requirement ID set to the verification register; count active, retired and unlinked records, then inspect evidence and disposition fields for each completed activity.',
        'acceptance_criteria': 'All 102 active requirements appear in the verification control record; eight retired records are excluded from active coverage; STR-007 remains the sole unlinked case; each requirement has a distinct verification outcome.',
    },

    # ARC-FOREST3-TST-011
    {
        'reference': 'V-MIS-BUD-DATA',
        'name': 'Spacecraft data allocation',
        'method': 'test',
        'objective': 'Confirm payload and housekeeping generation fit pass capacity and both data reserve targets.',
        'procedure': 'Add PAY 4,000,000 and OBD 20,000 bit/s for peak generation; integrate PAY over 120 s and OBD over 600 s, then compare with effective 300 s×2.5 Mbit/s pass capacity and the two reserve targets.',
        'acceptance_criteria': 'Peak generation <= 5025000 bit/s; peak-generation reserve >= 0.2 ratio; pass reserve >= 0.2 ratio.',
    },

    # ARC-FOREST3-TST-012
    {
        'reference': 'V-MIS-BUD-MASS',
        'name': 'Spacecraft mass allocation',
        'method': 'analysis',
        'objective': 'Confirm that the seven subsystem masses remain within the 16 kg spacecraft limit.',
        'procedure': 'Sum STR 2.4, EPS 3.6, OBD 1.2, PAY 3.6, COM 1.2, ADCS 2.3 and THM 1.2 kg once; compare the result with the 16 kg vehicle limit.',
        'acceptance_criteria': 'The calculated vehicle mass is <= 16 kg in the defined mission scenario.',
    },

    # ARC-FOREST3-TST-013
    {
        'reference': 'V-MIS-BUD-POWER',
        'name': 'Spacecraft power allocation',
        'method': 'test',
        'objective': 'Confirm CFG-A power failures and CFG-B mode loads are calculated separately against the reserve basis.',
        'procedure': 'Sum each concurrent bus-input row and calculate reserve; repeat for CFG-B imaging 80 W, processing/slew 30 W, downlink 70 W and idle 20 W; keep the two baseline numerical failures separate.',
        'acceptance_criteria': 'Vehicle power <= 100 W; vehicle-power reserve >= 0.2 ratio; mode power difference >= 0 W.',
    },

    # ARC-FOREST3-TST-014
    {
        'reference': 'V-STR-001',
        'name': 'Equipment integration',
        'method': 'inspection',
        'objective': 'Confirm each equipment installation has one owned location and no assembly interference.',
        'procedure': 'Inspect the assembly model and equipment placement table; compare component ownership with the mass ledger and check interference.',
        'acceptance_criteria': "The represented structure locates EPS, OBD, PAY, COM, ADCS and THM without overlap inside the 226×226×227 mm envelope; mounts and harness mechanical support are counted within STR's 2 kg.",
    },

    # ARC-FOREST3-TST-015
    {
        'reference': 'V-STR-002',
        'name': '8U mechanical envelope',
        'method': 'test',
        'objective': 'Confirm CAD envelope and ground attachments meet the 8U mechanical limits without interference.',
        'procedure': 'Extract CAD bounding box and attachment centre distances and inspect interference at the four ground attachment points.',
        'acceptance_criteria': 'Stowed X/Y/Z bounds do not exceed 226/226/227 mm; the four M4 ground-fixture centres form a 180×180 mm square and ≥5 mm keep-out is clear.',
    },

    # ARC-FOREST3-TST-016
    {
        'reference': 'V-STR-003',
        'name': 'Environmental compatibility',
        'method': 'review',
        'objective': 'Confirm each joint has identified material and interface coverage distinct from qualification evidence.',
        'procedure': 'Inspect the materials/joint schedule and supporting fixture design rationale; verify each joint has an identified material/interface and distinguish documentary review from qualification evidence.',
        'acceptance_criteria': 'The design identifies structural materials, joint type, 2 N·m ground attachment torque and applicability over the represented −20–60 °C non-operating range. Materials are 6061-T6 aluminium with bolted joints. The bench fixture covers static 1g along each principal axis with ≤0.5 mm joint slip and no visible damage; launch loads and physical qualification remain open.',
    },

    # ARC-FOREST3-TST-017
    {
        'reference': 'V-STR-004',
        'name': 'Equipment mounting interfaces',
        'method': 'inspection',
        'objective': 'Confirm equipment and ground fixture attachments match the controlled mechanical drawings.',
        'procedure': 'Cross-check the equipment inventory against mechanical drawings; inspect each equipment-to-structure attachment and ground fixture interface.',
        'acceptance_criteria': 'Each EPS, OBD, PAY, COM, ADCS and THM installation has a named mount, dimensioned location, fastener and accessible assembly direction; ground mounting uses four M4 points on the 180×180 mm square. Internal trays are centred at X/Y=113/113 mm at Z=20/80/140/200 mm, using M3 centres on 40×40 mm squares and 1 N·m torque; shared carriers follow D1 nonoverlap limits.',
    },

    # ARC-FOREST3-TST-018
    {
        'reference': 'V-STR-005',
        'name': 'Electrical and mechanical clearances',
        'method': 'inspection',
        'objective': 'Confirm harness clearances and intentional electrical contacts match the interface register.',
        'procedure': 'Measure minimum separation in the CAD/connection drawings, including harness routes; inspect intentional electrical contacts against the interface register.',
        'acceptance_criteria': 'The model maintains ≥5 mm clearance between reserved equipment/harness keep-out volumes and unrelated structure, with no conductor-to-chassis contact outside intentional bonded/return points.',
    },

    # ARC-FOREST3-TST-019
    {
        'reference': 'V-STR-006',
        'name': 'Controlled CAD model',
        'method': 'review',
        'objective': 'Confirm the controlled CAD model units, revision, extents, mounts, and hardware configuration match the drawings.',
        'procedure': 'Open the declared model data, inspect units and revision, compare bounding extents and mount coordinates with drawings and compare hardware revision across configurations.',
        'acceptance_criteria': 'The controlled CAD representation identifies CFG-A and CFG-B as identical hardware, uses mm, shows the complete envelope, mount coordinates and equipment blocks, and matches the drawing register revision.',
    },

    # ARC-FOREST3-TST-020
    {
        'reference': 'V-STR-008',
        'name': 'Solar hardware interfaces',
        'method': 'inspection',
        'objective': 'Confirm solar hardware attachment and electrical routing match the generation allocation.',
        'procedure': 'Inspect the solar hardware arrangement and attachment drawing, then trace its electrical route to EPS and compare its generation label with A3.',
        'acceptance_criteria': 'Solar-generation hardware has identified attachment points, envelope, routing and EPS endpoint in the design; its defined reference generation is 120 W in sunlight and deployable mechanism qualification remains open. The solar fixture mount and harness route must be explicitly identified before this planned inspection can pass; reference generation alone is not mounting evidence.',
    },

    # ARC-FOREST3-TST-021
    {
        'reference': 'V-STR-009',
        'name': 'Structural handling hazards',
        'method': 'inspection',
        'objective': 'Confirm assembly hazards have assigned controls in procedures and verification records.',
        'procedure': 'Walk the assembly procedure against each hazard and confirm its control is assigned to a step and verification record; record any missing control as open.',
        'acceptance_criteria': 'The ground handling assessment addresses sharp edges, loose fasteners, tipping/drop, harness snagging and energized assembly; controls specify de-energized assembly, supported fixture, retained fasteners and inspected routes before power-up.',
    },

    # ARC-FOREST3-TST-022
    {
        'reference': 'V-STR-BUD-MASS',
        'name': 'STR mass allocation',
        'method': 'inspection',
        'objective': 'Confirm the STR mass allocation includes each physical contributor once and remains within 2.5 kg.',
        'procedure': 'Reconcile the STR parts within its A2 ownership boundary; sum their controlled estimated masses and compare with the 2.5 kg STR mass limit; inspect for duplicate contributors.',
        'acceptance_criteria': 'The calculated STR mass is <= 2.5 kg in the defined mission scenario.',
    },

    # ARC-FOREST3-TST-023
    {
        'reference': 'V-EPS-001',
        'name': 'Operating-mode power supply',
        'method': 'test',
        'objective': 'Confirm each operating mode meets its simulated EPS demand and isolates the CFG-A power failure.',
        'procedure': 'Apply the four mode loads to the simulated EPS and inspect bus voltage and demand; run CFG-A concurrency separately as an expected power-budget failure.',
        'acceptance_criteria': 'The 12 V bus stays within 11.4–12.6 V under corrected 80 W imaging, 30 W processing/slew, 70 W downlink and 20 W safe/idle demand; the 120 W concurrent stress case is explicitly outside the 100 W limit.',
    },

    # ARC-FOREST3-TST-024
    {
        'reference': 'V-EPS-002',
        'name': 'Solar power generation',
        'method': 'test',
        'objective': 'Confirm solar charging stays within storage capacity and restores the required energy.',
        'procedure': 'Recalculate (120−20)×3300/3600×0.90; test charge at empty and full storage and verify capacity is never exceeded.',
        'acceptance_criteria': 'Reference delivered solar generation is 120 W for 3300 s; after a 20 W sunlight load and 90% charging efficiency the available charge energy is 82.5 Wh, capped by battery headroom.',
    },

    # ARC-FOREST3-TST-025
    {
        'reference': 'V-EPS-003',
        'name': 'Stored energy capacity',
        'method': 'test',
        'objective': 'Confirm the operating and eclipse energy profiles fit usable storage with the required reserve.',
        'procedure': 'Integrate the 900 s 11.666667 Wh profile plus 1200 s at 20 W; compare against usable energy and calculate reserve using usable capacity.',
        'acceptance_criteria': 'Eclipse energy <= 40 Wh; energy reserve >= 0.2 ratio.',
    },

    # ARC-FOREST3-TST-026
    {
        'reference': 'V-EPS-004',
        'name': 'Energy-storage limits and interfaces',
        'method': 'review',
        'objective': 'Confirm storage limits use usable energy and preserve the defined interface margins.',
        'procedure': 'Inspect storage specification and interface limits; verify no analysis substitutes nominal energy for usable energy or double-counts derating.',
        'acceptance_criteria': 'Storage records distinguish 80 Wh nominal from 40 Wh assessed usable, 12 V ±5% bus compatibility, 0–40 °C operating and −10–50 °C survival limits; derating/depth-of-discharge policy is included in the usable figure.',
    },

    # ARC-FOREST3-TST-027
    {
        'reference': 'V-EPS-005',
        'name': 'Power-system status telemetry',
        'method': 'test',
        'objective': 'Confirm power telemetry reports normal, charging, depleted, inhibited, and fault states with valid units and time.',
        'procedure': 'Generate normal, charging, depleted, inhibited and temperature-fault states; decode telemetry and compare units, values, validity and timestamps against input states.',
        'acceptance_criteria': 'EPS telemetry includes bus voltage V, bus demand W, battery usable energy Wh, charge/discharge state, battery temperature °C, branch switch/inhibit state and fault reason, with UTC, sequence and validity on each sample.',
    },

    # ARC-FOREST3-TST-028
    {
        'reference': 'V-EPS-006',
        'name': 'Load switching and power inhibits',
        'method': 'test',
        'objective': 'Confirm load switching prevents conflicting main loads and preserves inhibits after a fault.',
        'procedure': 'Issue permitted and conflicting enable commands in every mode and after a fault; inspect switch telemetry and verify no simultaneous main-load enable in CFG-B.',
        'acceptance_criteria': 'CFG-B enables PAY main power only in imaging and COM main power only in downlink; safe mode inhibits both, retaining command/retention services in OBD; unauthorized or fault-latched enables are rejected.',
    },

    # ARC-FOREST3-TST-029
    {
        'reference': 'V-EPS-007',
        'name': 'Regulated power limits',
        'method': 'test',
        'objective': 'Confirm regulated voltage stays within continuous and transient limits across the bounded load profile.',
        'procedure': "Sweep steady loads and execute the design's bounded transient profile; capture minimum and maximum voltage and distinguish transient limits from continuous demand.",
        'acceptance_criteria': 'Regulated output remains 11.4–12.6 V at corrected scheduled loads 20/30/70/80 W. Corrected startup enables one main load at a time, holding its initial current <=2 A for 20 ms before ramping without overshoot; total startup demand <=80 W, preserving 20% reserve against 100 W. Capture millisecond startup behavior separately from the ten-second power trace.',
    },

    # ARC-FOREST3-TST-030
    {
        'reference': 'V-EPS-008',
        'name': 'Electrical protection functions',
        'method': 'test',
        'objective': 'Confirm protection thresholds trigger safe response and reject unauthorized reset.',
        'procedure': 'Inject simulated overload, voltage and thermal faults at their defined interface thresholds; measure response time against the protection specification and try unauthorized reset.',
        'acceptance_criteria': 'Overload, supply excursion and thermal-protection fixtures invoke the interface-defined inhibit/latch response; PAY and COM are de-energized in safe mode and restoration requires authorized reset after 60 s in range; the fixture uses current limiting instead of an injected short. D2 thresholds are <11.4 V or >12.6 V continuously for 100 ms followed by safe entry within 2 s; the simulated bench-source current limit is 8.77 A. Current limiting does not substitute for the separate 100 W power criterion.',
    },

    # ARC-FOREST3-TST-031
    {
        'reference': 'V-EPS-009',
        'name': 'Controlled electrical interfaces',
        'method': 'inspection',
        'objective': 'Confirm electrical pins, polarity, returns, and limits are consistent across connected equipment.',
        'procedure': 'Check the electrical interface register against harness and equipment endpoints; test reversed polarity and unmatched pin declarations as rejected configurations.',
        'acceptance_criteria': 'Each power route identifies source EPS output, receiving equipment, connector/pins, polarity, return, 12 V nominal range and load limit; no two pins carry contradictory functions in the same configuration. J-PWR pins 1/2/3/4 are +12 V/return/chassis bond/3.3 V enable; return is PCDU star-connected and chassis carries no normal return current.',
    },

    # ARC-FOREST3-TST-032
    {
        'reference': 'V-EPS-010',
        'name': 'Short-circuit prevention',
        'method': 'inspection',
        'objective': 'Check harness continuity and isolation against the connection table and reject prohibited paths before power-up.',
        'procedure': 'Inspect every harness net against the connection table; inject each prohibited continuity in a non-energized fixture and verify the pre-power gate rejects it.',
        'acceptance_criteria': 'The design prohibits supply-to-return and supply-to-chassis shorts outside the intentional return/bond scheme; pre-power inspection verifies polarity, isolation and protection coverage using the simulated continuity matrix. Disconnected-fixture continuity is <0.1 Ω per intended path and isolation >10 MΩ at 24 V; power conductors are insulated 20 AWG with strain relief.',
    },

    # ARC-FOREST3-TST-033
    {
        'reference': 'V-EPS-BUD-MASS',
        'name': 'EPS mass allocation',
        'method': 'inspection',
        'objective': 'Confirm the EPS mass allocation includes each physical contributor once and remains within 4 kg.',
        'procedure': 'Reconcile the EPS parts within its A2 ownership boundary; sum their controlled estimated masses and compare with the 4 kg EPS mass limit; inspect for duplicate contributors.',
        'acceptance_criteria': 'The calculated EPS mass is <= 4 kg in the defined mission scenario.',
    },

    # ARC-FOREST3-TST-034
    {
        'reference': 'V-EPS-BUD-POWER',
        'name': 'EPS power allocation',
        'method': 'test',
        'objective': 'Confirm EPS mode demands stay within the 6.25 W allocation without double-counting bus input.',
        'procedure': 'Read the EPS concurrent, imaging, downlink and safe/idle demand from A3; compare each with 6.25 W, calculate reserve at maximum demand and reconcile bus-input ownership with the system total.',
        'acceptance_criteria': 'EPS power <= 6.25 W; EPS power reserve >= 0.2 ratio.',
    },

    # ARC-FOREST3-TST-035
    {
        'reference': 'V-OBD-001',
        'name': 'Payload data path',
        'method': 'test',
        'objective': 'Confirm the payload path preserves bits through ingest, processing, storage, and acknowledged deletion.',
        'procedure': 'Run the reference acquisition through ingest, processing, storage and ACK; reconcile bit counts, stage completion and deletion time.',
        'acceptance_criteria': 'OBD accepts both thermal bands, produces the 480 Mbit observation product including metadata/framing, completes processing by t=180 s and retains the product until durable hash-matching ACK.',
    },

    # ARC-FOREST3-TST-036
    {
        'reference': 'V-OBD-002',
        'name': 'Onboard computing platform',
        'method': 'test',
        'objective': 'Confirm the onboard computing platform executes the reference workload within storage and timing limits.',
        'procedure': 'Review the target/runtime manifest and function allocation; run the reference workload and inspect storage occupancy and processing completion.',
        'acceptance_criteria': 'The named representative computing target executes initialization, acquisition, processing, mode control, telemetry and transfer functions; usable observation storage is 2,000,000,000 bit and processing finishes by t=180 s in the fixture.',
    },

    # ARC-FOREST3-TST-037
    {
        'reference': 'V-OBD-003',
        'name': 'Payload data and metadata intake',
        'method': 'test',
        'objective': 'Confirm complete product metadata is preserved and incomplete or corrupt products are rejected.',
        'procedure': 'Exchange one complete product and variants missing each mandatory field or with a corrupt hash; verify exact metadata preservation or explicit rejection.',
        'acceptance_criteria': 'Received payload data carries product ID, observation UTC, WGS84 position, both band identifiers, calibration ID, attitude/orbit validity, software/configuration version and integrity hash; missing or mismatched fields reject the product.',
    },

    # ARC-FOREST3-TST-038
    {
        'reference': 'V-OBD-004',
        'name': 'Onboard processing chain',
        'method': 'test',
        'objective': 'Confirm the pinned processing chain classifies all scene cases and handles threshold boundaries.',
        'procedure': 'Run the ten named scene cases through the pinned processing version; compare outcomes with labels and inspect threshold-boundary behaviour.',
        'acceptance_criteria': 'The controlled processing algorithm detects exactly the six valid hot fixtures, returns no detection for two cold fixtures and rejects two invalid fixtures using MWIR ≥330 K and MWIR−LWIR ≥10 K.',
    },

    # ARC-FOREST3-TST-039
    {
        'reference': 'V-OBD-005',
        'name': 'Telemetry state and health data',
        'method': 'test',
        'objective': 'Confirm OBD telemetry reflects normal and fault truth for every health group.',
        'procedure': 'Drive one normal and one fault state for each telemetry group; decode the record and compare it with the simulated subsystem truth.',
        'acceptance_criteria': 'Telemetry exposes mode, fault latch/reason, EPS values, payload readiness, storage occupancy, processing state, transfer offsets, pointing/thermal validity and software/configuration IDs with UTC and sequence numbers.',
    },

    # ARC-FOREST3-TST-040
    {
        'reference': 'V-OBD-008',
        'name': 'Payload electrical and data interfaces',
        'method': 'test',
        'objective': 'Confirm payload electrical and data interfaces enforce readiness and preserve transferred bytes and hash.',
        'procedure': 'Review pin assignment and protocol endpoints; attempt acquisition before readiness, then transfer a complete valid product and compare received bytes/hash.',
        'acceptance_criteria': 'The PAY interface supplies 12 V ±5%, a switched 45 W main load and the defined command/data connection; 4 Mbit/s including metadata/framing reaches OBD only after payload and receiver readiness. OBD–PAY uses 100BASE-TX with ≥5.025 Mbit/s sustained application service; J-DATA pins 1/2/3/6 are TX+/TX−/RX+/RX−.',
    },

    # ARC-FOREST3-TST-041
    {
        'reference': 'V-OBD-009',
        'name': 'Controlled software loading',
        'method': 'demonstration',
        'objective': 'Confirm software loading activates only valid authorized images and records rollback for failed updates.',
        'procedure': 'Attempt valid, corrupted, interrupted and unauthorized update fixtures; restart after each and inspect active image/configuration and rollback record.',
        'acceptance_criteria': 'Only an authorized update may activate FSW-1.1/CFG-B after integrity and target compatibility checks; corrupt, interrupted or unauthorized loads preserve the last working FSW-1.0/CFG-A image and report a reason. The D6 inactive-slot protocol verifies signature/hash before authorized restart; missing health ACK within 30 s rolls back into safe mode, while interrupted staging never activates an incomplete image.',
    },

    # ARC-FOREST3-TST-042
    {
        'reference': 'V-OBD-010',
        'name': 'Ground access and verification connections',
        'method': 'inspection',
        'objective': 'Confirm OBD installation and verification connectors are accessible without unsafe powered disconnection.',
        'procedure': 'Trace OBD installation/test steps to labelled connectors in the mechanical and electrical drawings; inspect whether access requires an unsafe powered disconnection.',
        'acceptance_criteria': 'The ground access plan exposes power isolation, software loading, diagnostic telemetry and PAY data-loopback connections with equipment de-energized for connector changes; each test task names a reachable connection.',
    },

    # ARC-FOREST3-TST-043
    {
        'reference': 'V-OBD-011',
        'name': 'Observation product retention',
        'method': 'test',
        'objective': 'Verify product retention, capacity, and recovery across ACK and contact interruptions.',
        'procedure': 'Compute retained occupancy at each event; withhold, corrupt, and duplicate ACKs and interrupt t=360–420 s; verify no premature deletion, duplicate publication, or capacity breach.',
        'acceptance_criteria': 'Retained occupancy <= 2000000000 bit.',
    },

    # ARC-FOREST3-TST-044
    {
        'reference': 'V-OBD-BUD-DATA',
        'name': 'OBD data allocation',
        'method': 'test',
        'objective': 'Confirm OBD housekeeping generation stays within its rate allocation and reserve target.',
        'procedure': 'Count encoded housekeeping bits over the 600 s reference interval; divide by interval and compare with rate limit and reserve target.',
        'acceptance_criteria': 'OBD data rate <= 25000 bit/s; OBD data reserve >= 0.2 ratio.',
    },

    # ARC-FOREST3-TST-045
    {
        'reference': 'V-OBD-BUD-MASS',
        'name': 'OBD mass allocation',
        'method': 'inspection',
        'objective': 'Confirm the OBD mass allocation includes each physical contributor once and remains within 1.25 kg.',
        'procedure': 'Reconcile the OBD parts within its A2 ownership boundary; sum their controlled estimated masses and compare with the 1.25 kg OBD mass limit; inspect for duplicate contributors.',
        'acceptance_criteria': 'The calculated OBD mass is <= 1.25 kg in the defined mission scenario.',
    },

    # ARC-FOREST3-TST-046
    {
        'reference': 'V-OBD-BUD-POWER',
        'name': 'OBD power allocation',
        'method': 'test',
        'objective': 'Confirm OBD mode demands stay within the 12.5 W allocation without double-counting bus input.',
        'procedure': 'Read the OBD concurrent, imaging, downlink and safe/idle demand from A3; compare each with 12.5 W, calculate reserve at maximum demand and reconcile bus-input ownership with the system total.',
        'acceptance_criteria': 'OBD power <= 12.5 W; OBD power reserve >= 0.1 ratio.',
    },

    # ARC-FOREST3-TST-047
    {
        'reference': 'V-SW-001',
        'name': 'Thermal observation initialization',
        'method': 'test',
        'objective': 'Confirm software starts only with required prerequisites and records readiness before acquisition.',
        'procedure': 'Boot the representative target with all prerequisites then repeat with each prerequisite unavailable; compare readiness, mode and acquisition-start records.',
        'acceptance_criteria': 'Before imaging starts, power, PAY acquisition, OBD storage, attitude/orbit validity and telemetry interfaces report ready; failure of any prerequisite prevents acquisition and records the failed prerequisite.',
    },

    # ARC-FOREST3-TST-048
    {
        'reference': 'V-SW-002',
        'name': 'Thermal observation acquisition',
        'method': 'test',
        'objective': 'Confirm acquisition preserves duration, data volume, band identity, and validity when metadata or attitude is invalid.',
        'procedure': 'Execute the reference observation and inject invalid metadata/attitude during acquisition; compare duration, bit count, band identity and validity flags.',
        'acceptance_criteria': 'The commanded observation occupies t=0–120 s, includes both 128×128 bands and all required metadata, and generates 480,000,000 bit including framing; invalid attitude/orbit/time prevents accepted output.',
    },

    # ARC-FOREST3-TST-049
    {
        'reference': 'V-SW-003',
        'name': 'Processing outputs',
        'method': 'test',
        'objective': 'Confirm processing classification and rejection follow the defined scene thresholds and input validity rules.',
        'procedure': 'Apply the feature-level thresholds to the controlled A1 scene cases; reject invalid attitude or incomplete input first.',
        'acceptance_criteria': 'Processing uses MWIR ≥330 K and MWIR−LWIR ≥10 K with declared calibration/version; six hot cases detect, two cold cases do not and two invalid cases reject explicitly; completion ≤t=180 s.',
    },

    # ARC-FOREST3-TST-050
    {
        'reference': 'V-SW-004',
        'name': 'Payload-derived information delivery',
        'method': 'test',
        'objective': 'Confirm interrupted product transfers resume with identical bytes, metadata, and hash and reject malformed data.',
        'procedure': 'Serialize a valid product, interrupt transfer and resume; compare complete bytes, metadata and hash before/after and reject malformed serialization.',
        'acceptance_criteria': 'Every queued delivery product has a stable product ID, SHA-256, observation UTC/location, band and calibration identifiers, validity and configuration/version; retransmission preserves identical content and resumes acknowledged offsets.',
    },

    # ARC-FOREST3-TST-051
    {
        'reference': 'V-SW-005',
        'name': 'Telemetry encoding',
        'method': 'test',
        'objective': 'Confirm telemetry encoding and decoding preserves normal and fault fields and marks missing sensors invalid.',
        'procedure': 'Encode known normal/fault telemetry vectors, decode them independently and compare all fields; inject missing sensors and inspect validity indicators.',
        'acceptance_criteria': 'Software encodes all defined mode, power, storage, processing, transfer, pointing and thermal values with documented units, UTC, sequence and validity; invalid sensors are not encoded as valid zero measurements.',
    },

    # ARC-FOREST3-TST-052
    {
        'reference': 'V-SW-006',
        'name': 'Mode and fault management',
        'method': 'test',
        'objective': 'Confirm software mode and fault recovery enforce corrected sequencing, thermal and pointing guards, and reset dwell.',
        'procedure': 'Replay the corrected schedule and inject thermal and pointing faults around transitions; inspect mode/load traces and test 60 s in-range plus authorized-reset recovery.',
        'acceptance_criteria': 'CFG-B uses imaging t=0–120 s, processing/slew t=120–300 s, transition complete by t=240 s, contact t=300–600 s and safe/idle to t=900 s; PAY/COM do not overlap and protective response is ≤2 s.',
    },

    # ARC-FOREST3-TST-053
    {
        'reference': 'V-SW-007',
        'name': 'Controlled software storage',
        'method': 'review',
        'objective': 'Confirm release manifests reproduce the controlled software configuration.',
        'procedure': 'Compare release manifests and rebuild the documented software configuration.',
        'acceptance_criteria': 'Source manifest, build recipe, dependency versions and configuration identify FSW-1.0/CFG-A and FSW-1.1/CFG-B reproducibly; the change is software scheduling only and hardware inputs remain identical.',
    },

    # ARC-FOREST3-TST-054
    {
        'reference': 'V-SW-008',
        'name': 'Software version traceability',
        'method': 'review',
        'objective': 'Confirm software versions trace unambiguously through source, build, change, and verification records.',
        'procedure': 'Resolve both release identifiers through source, build, change and verification records; reject ambiguous or mismatched version/configuration pairs.',
        'acceptance_criteria': 'Each of the two software IDs links to one source/build manifest, configuration and applicable planned or completed verification records; corrected scheduling is assigned only to FSW-1.1/CFG-B.',
    },

    # ARC-FOREST3-TST-055
    {
        'reference': 'V-SW-009',
        'name': 'Software architecture and interfaces',
        'method': 'review',
        'objective': 'Confirm software functions, interfaces, states, and update procedures match the architecture.',
        'procedure': 'Trace each software function to its inputs, outputs, state transition and interface; compare the architecture with the reference sequence and update procedure.',
        'acceptance_criteria': 'Software design defines initialization, acquisition, processing, storage, transfer, telemetry and mode/fault control, including data ownership and the CFG-A→CFG-B scheduling delta.',
    },

    # ARC-FOREST3-TST-056
    {
        'reference': 'V-SW-010',
        'name': 'Target configuration verification',
        'method': 'test',
        'objective': 'Confirm each software verification result names the executed target and build before acceptance.',
        'procedure': 'Review target identity, build, and run evidence for every software verification case; require target execution evidence before acceptance.',
        'acceptance_criteria': 'Each software verification case identifies its representative target manifest, configuration, and execution result.',
    },

    # ARC-FOREST3-TST-057
    {
        'reference': 'V-PAY-001',
        'name': 'Thermal imagery acquisition',
        'method': 'test',
        'objective': 'Confirm payload acquisition meets band accuracy, bad-pixel, dimension, volume, and metadata limits.',
        'procedure': 'Acquire the three temperature fixtures and labelled scene set; measure per-band error, bad pixels, dimensions, bit volume and metadata integrity.',
        'acceptance_criteria': 'The fixture produces both 128×128 thermal bands over 120 s, 480 Mbit including metadata/framing; brightness-temperature error ≤2 K at 290/310/330 K and bad-pixel fraction ≤1%.',
    },

    # ARC-FOREST3-TST-058
    {
        'reference': 'V-PAY-002',
        'name': 'MWIR and LWIR channels',
        'method': 'review',
        'objective': 'Confirm MWIR and LWIR spectral response samples meet the controlled in-band and out-of-band limits.',
        'procedure': "Compare each channel's normalized spectral fixture samples against the spectral table in the payload design; record wavelength, response and limit per sample.",
        'acceptance_criteria': 'MWIR spans 3.5–4.1 μm and LWIR 8–12 μm; normalized response ≥0.5 at defined in-band samples and ≤0.05 at defined out-of-band samples for each channel. In-band sample wavelengths are MWIR 3.5/3.8/4.1 μm and LWIR 8/10/12 μm; out-of-band samples are MWIR 3.0/4.6 μm and LWIR 7/13 μm.',
    },

    # ARC-FOREST3-TST-059
    {
        'reference': 'V-PAY-003',
        'name': 'Thermal data and metadata delivery',
        'method': 'test',
        'objective': 'Confirm payload data delivery preserves complete product bytes and fields and rejects corrupted or incomplete variants.',
        'procedure': 'Exchange a complete 120 s product and a corrupted/missing-field variant with OBD; verify byte totals, field preservation and rejection reasons.',
        'acceptance_criteria': 'PAY transmits both band IDs, product ID, UTC, WGS84 position, calibration and validity/configuration references with the framed observation at 4,000,000 bit/s; received bytes/hash match the source.',
    },

    # ARC-FOREST3-TST-060
    {
        'reference': 'V-PAY-004',
        'name': 'Payload platform interfaces',
        'method': 'test',
        'objective': 'Confirm payload connectors, commands, data, readiness, and switched power states agree.',
        'procedure': 'Cross-check connector/pin and command/data tables; exercise ready/not-ready acquisition and switched states and inspect power and data traces.',
        'acceptance_criteria': 'PAY power is 12 V ±5% at 45 W main demand during imaging, zero switched main demand otherwise; commands require readiness and the controlled data interface carries 4 Mbit/s including metadata/framing.',
    },

    # ARC-FOREST3-TST-061
    {
        'reference': 'V-PAY-005',
        'name': 'MWIR image quality and calibration',
        'method': 'test',
        'objective': 'Confirm MWIR calibration meets temperature accuracy, bad-pixel, and drift limits.',
        'procedure': 'Apply the three MWIR temperature fixtures at calibration limits; compare calibrated pixels to truth, count bad pixels and record thermal drift.',
        'acceptance_criteria': 'MWIR 3.5–4.1 μm calibration at 20±2 °C with drift ≤0.5 °C/min yields absolute brightness-temperature error ≤2 K at 290/310/330 K truth, ≤1% bad pixels and 128×128 samples. CAL-A maps input kelvin with gain 1 and offset 0 and excludes marked bad pixels.',
    },

    # ARC-FOREST3-TST-062
    {
        'reference': 'V-PAY-009',
        'name': 'LWIR image quality and calibration',
        'method': 'test',
        'objective': 'Confirm LWIR calibration meets temperature accuracy, bad-pixel, and drift limits.',
        'procedure': 'Apply the three LWIR temperature fixtures at calibration limits; compare calibrated pixels to truth, count bad pixels and record thermal drift.',
        'acceptance_criteria': 'LWIR 8–12 μm calibration at 20±2 °C with drift ≤0.5 °C/min yields absolute brightness-temperature error ≤2 K at 290/310/330 K truth, ≤1% bad pixels and 128×128 samples. CAL-A maps input kelvin with gain 1 and offset 0 and excludes marked bad pixels.',
    },

    # ARC-FOREST3-TST-063
    {
        'reference': 'V-PAY-BUD-DATA',
        'name': 'PAY data allocation',
        'method': 'test',
        'objective': 'Confirm payload data generation stays within rate, volume, and reserve allocations without double-counting framing.',
        'procedure': 'Count all encoded payload bits over 120 s and recompute average rate, volume and reserve without adding framing a second time.',
        'acceptance_criteria': 'PAY data rate <= 5000000 bit/s; PAY data reserve >= 0.2 ratio.',
    },

    # ARC-FOREST3-TST-064
    {
        'reference': 'V-PAY-BUD-MASS',
        'name': 'PAY mass allocation',
        'method': 'inspection',
        'objective': 'Confirm the PAY mass allocation includes each physical contributor once and remains within 4 kg.',
        'procedure': 'Reconcile the PAY parts within its A2 ownership boundary; sum their controlled estimated masses and compare with the 4 kg PAY mass limit; inspect for duplicate contributors.',
        'acceptance_criteria': 'The calculated PAY mass is <= 4 kg in the defined mission scenario.',
    },

    # ARC-FOREST3-TST-065
    {
        'reference': 'V-PAY-BUD-POWER',
        'name': 'PAY power allocation',
        'method': 'test',
        'objective': 'Confirm PAY mode demand stays within the 60 W allocation without double-counting bus input.',
        'procedure': 'Read the PAY concurrent, imaging, downlink and safe/idle demand from A3; compare each with 60 W, calculate reserve at maximum demand and reconcile bus-input ownership with the system total.',
        'acceptance_criteria': 'PAY power <= 60 W; PAY power reserve >= 0.25 ratio.',
    },

    # ARC-FOREST3-TST-066
    {
        'reference': 'V-COM-001',
        'name': 'Command and telemetry path',
        'method': 'test',
        'objective': 'Confirm the shared communications path carries commands, acknowledgements, housekeeping, and products in contact and safe mode.',
        'procedure': 'Inspect the single-path architecture and exercise commands, acknowledgements, housekeeping and product transfer in contact and safe-mode fixtures.',
        'acceptance_criteria': 'One shared simulated S-band transceiver supports command, telemetry and observation data; command reverse service is 10 kbit/s and error-corrected application downlink is 2.5 Mbit/s; essential command reception remains in the OBD safe-load allowance.',
    },

    # ARC-FOREST3-TST-067
    {
        'reference': 'V-COM-002',
        'name': 'Link margin',
        'method': 'analysis',
        'objective': 'Confirm forward and reverse RF link margins meet the 3 dB requirement.',
        'procedure': 'Recalculate free-space loss as 32.44+20log10(2200)+20log10(1000), received power and margin for forward/reverse paths; do not subtract FEC or Eb/N0 again.',
        'acceptance_criteria': 'RF link margin >= 3 dB.',
    },

    # ARC-FOREST3-TST-068
    {
        'reference': 'V-COM-003',
        'name': 'Observation product delivery',
        'method': 'test',
        'objective': 'Confirm the downlink queue drains within contact capacity while preserving distinct rate and volume allocations.',
        'procedure': 'Build the t=300 queue of 486 Mbit, drain at net 2.48 Mbit/s while generating housekeeping, and compare completion and full-pass volume with their distinct allocations.',
        'acceptance_criteria': 'Pass volume <= 750000000 bit.',
    },

    # ARC-FOREST3-TST-069
    {
        'reference': 'V-COM-004',
        'name': 'Transfer recovery reporting',
        'method': 'test',
        'objective': 'Confirm outage recovery reports durable ACK, resume offset, storage retention, and customer status.',
        'procedure': 'Inject the 60 s outage and whole-contact outage separately; inspect resume offsets, durable ACK/hash, retained storage and customer status.',
        'acceptance_criteria': 'Outage acknowledgement <= 600 s.',
    },

    # ARC-FOREST3-TST-070
    {
        'reference': 'V-COM-BUD-MASS',
        'name': 'COM mass allocation',
        'method': 'inspection',
        'objective': 'Confirm the COM mass allocation includes each physical contributor once and remains within 1.25 kg.',
        'procedure': 'Reconcile the COM parts within its A2 ownership boundary; sum their controlled estimated masses and compare with the 1.25 kg COM mass limit; inspect for duplicate contributors.',
        'acceptance_criteria': 'The calculated COM mass is <= 1.25 kg in the defined mission scenario.',
    },

    # ARC-FOREST3-TST-071
    {
        'reference': 'V-COM-BUD-POWER',
        'name': 'COM power allocation',
        'method': 'test',
        'objective': 'Confirm COM mode demand stays within the 50 W allocation without double-counting bus input.',
        'procedure': 'Read the COM concurrent, imaging, downlink and safe/idle demand from A3; compare each with 50 W, calculate reserve at maximum demand and reconcile bus-input ownership with the system total.',
        'acceptance_criteria': 'COM power <= 50 W; COM power reserve >= 0.15 ratio.',
    },

    # ARC-FOREST3-TST-072
    {
        'reference': 'V-ADCS-001',
        'name': 'Mission-mode pointing support',
        'method': 'test',
        'objective': 'Confirm pointing support follows the reference orbit timeline through observation and contact preparation.',
        'procedure': 'Replay the 500 km reference-orbit attitude fixture through observation and contact preparation; compare mode targets and transition completion with the timeline.',
        'acceptance_criteria': 'The mode table associates imaging with scene pointing, downlink with the prescribed ground direction, and safe/idle with the reference power-generation attitude; transition is complete by t=240 s before t=300 s contact.',
    },

    # ARC-FOREST3-TST-073
    {
        'reference': 'V-ADCS-002',
        'name': 'Pointing accuracy and stability',
        'method': 'test',
        'objective': 'Confirm commanded and measured attitude meet exposure error and drift limits.',
        'procedure': 'Compare commanded and actual attitude for each exposure; calculate maximum angular error and start-to-end drift, including exact-limit and over-limit cases.',
        'acceptance_criteria': '[pointing error limit]=0.1° and [stability limit]=0.01° drift per 10 ms exposure; every accepted observation meets both in the disturbance fixture.',
    },

    # ARC-FOREST3-TST-074
    {
        'reference': 'V-ADCS-003',
        'name': 'Pointing-loss response',
        'method': 'test',
        'objective': 'Confirm pointing faults invalidate affected products and enforce the defined recovery dwell and reset.',
        'procedure': 'Inject error and drift excursions independently; check invalid product flags and response timestamps; attempt reset before and after the recovery dwell.',
        'acceptance_criteria': 'Exceeding 0.1° error or 0.01° drift per 10 ms marks affected observations invalid and invokes safe mode within 2 s; recovery requires 60 s valid conditions and authorized reset.',
    },

    # ARC-FOREST3-TST-075
    {
        'reference': 'V-ADCS-004',
        'name': 'Attitude and time metadata',
        'method': 'test',
        'objective': 'Confirm attitude, time, orbit, and geolocation metadata meet validity and ground-truth limits.',
        'procedure': 'Compare attitude/time/orbit metadata with the controlled reference-frame fixture, then independently calculate ground-location error; invalidate missing orbit or frame data.',
        'acceptance_criteria': 'Attitude knowledge error ≤0.01°, observation UTC error ≤0.1 s and declared frame/orbit validity accompany each observation; independent WGS84 ground-truth comparison yields ≤250 m position error. D4 uses ECEF orbit positions in metres and normalized scalar-first body-to-ECEF quaternions with +Z boresight; geolocation selects the nearest positive WGS84 ellipsoid ray intersection and rejects absent intersections.',
    },

    # ARC-FOREST3-TST-076
    {
        'reference': 'V-ADCS-BUD-MASS',
        'name': 'ADCS mass allocation',
        'method': 'inspection',
        'objective': 'Confirm the ADCS mass allocation includes each physical contributor once and remains within 2.5 kg.',
        'procedure': 'Reconcile the ADCS parts within its A2 ownership boundary; sum their controlled estimated masses and compare with the 2.5 kg ADCS mass limit; inspect for duplicate contributors.',
        'acceptance_criteria': 'The calculated ADCS mass is <= 2.5 kg in the defined mission scenario.',
    },

    # ARC-FOREST3-TST-077
    {
        'reference': 'V-ADCS-BUD-POWER',
        'name': 'ADCS power allocation',
        'method': 'test',
        'objective': 'Confirm ADCS mode demand stays within the 20 W allocation without double-counting bus input.',
        'procedure': 'Read the ADCS concurrent, imaging, downlink and safe/idle demand from A3; compare each with 20 W, calculate reserve at maximum demand and reconcile bus-input ownership with the system total.',
        'acceptance_criteria': 'ADCS power <= 20 W; ADCS power reserve >= 0.2 ratio.',
    },

    # ARC-FOREST3-TST-078
    {
        'reference': 'V-THM-001',
        'name': 'Operating temperature control',
        'method': 'test',
        'objective': 'Confirm equipment temperatures remain within operating limits across mode boundaries and heater allowances.',
        'procedure': 'Inspect reference thermal time histories at mode boundaries and extrema; compare each equipment temperature to its own limits and reconcile heater allowance.',
        'acceptance_criteria': 'Throughout the 900 s nominal mode profile, payload and battery remain 0–40 °C and electronics −10–50 °C; the 5 W THM mode allowance is included once in system demand.',
    },

    # ARC-FOREST3-TST-079
    {
        'reference': 'V-THM-002',
        'name': 'Calibration and image-quality temperatures',
        'method': 'test',
        'objective': 'Confirm calibration temperature and drift stay within limits for both thermal channels.',
        'procedure': 'Evaluate payload temperature and drift during calibration, then correlate each channel result with calibration ID and reject out-of-window calibration.',
        'acceptance_criteria': 'Payload calibration occurs at 20±2 °C with drift ≤0.5 °C/min; both channel calibration fixtures meet ≤2 K absolute error at 290/310/330 K truth and ≤1% bad pixels.',
    },

    # ARC-FOREST3-TST-080
    {
        'reference': 'V-THM-003',
        'name': 'Thermal protection response',
        'method': 'test',
        'objective': 'Confirm thermal excursions trigger safe response and restart recovery dwell after renewed faults.',
        'procedure': 'Inject payload, electronics and battery excursions independently; inspect trip timestamps and recovery dwell, including a renewed excursion that restarts the dwell.',
        'acceptance_criteria': 'Any operating-range excursion triggers safe mode within 2 s and explicit equipment/limit telemetry; restart is inhibited until 60 s continuously in range plus authorized reset.',
    },

    # ARC-FOREST3-TST-081
    {
        'reference': 'V-THM-004',
        'name': 'Survival temperature control',
        'method': 'analysis',
        'objective': 'Confirm non-operating survival temperatures permit powered recovery only after the defined dwell and reset.',
        'procedure': 'Evaluate minimum/maximum non-operating profiles for the full 2100 s duration, then verify powered recovery begins only inside operating limits after the defined dwell/reset.',
        'acceptance_criteria': 'For 2100 s non-operating boundary fixtures, payload/electronics remain −20–60 °C and battery −10–50 °C; safe-mode powered equipment additionally respects operating limits; TVAC qualification remains open.',
    },

    # ARC-FOREST3-TST-082
    {
        'reference': 'V-THM-BUD-MASS',
        'name': 'THM mass allocation',
        'method': 'inspection',
        'objective': 'Confirm the THM mass allocation includes each physical contributor once and remains within 1.25 kg.',
        'procedure': 'Reconcile the THM parts within its A2 ownership boundary; sum their controlled estimated masses and compare with the 1.25 kg THM mass limit; inspect for duplicate contributors.',
        'acceptance_criteria': 'The calculated THM mass is <= 1.25 kg in the defined mission scenario.',
    },

    # ARC-FOREST3-TST-083
    {
        'reference': 'V-THM-BUD-POWER',
        'name': 'THM power allocation',
        'method': 'test',
        'objective': 'Confirm THM mode demand stays within the 6.25 W allocation without double-counting bus input.',
        'procedure': 'Read the THM concurrent, imaging, downlink and safe/idle demand from A3; compare each with 6.25 W, calculate reserve at maximum demand and reconcile bus-input ownership with the system total.',
        'acceptance_criteria': 'THM power <= 6.25 W; THM power reserve >= 0.1 ratio.',
    },

    # ARC-FOREST3-TST-084
    {
        'reference': 'V-GRD-001',
        'name': 'Command and telemetry records',
        'method': 'demonstration',
        'objective': 'Confirm ground command and telemetry records preserve IDs, acknowledgements, outcomes, and rejection states.',
        'procedure': 'Issue a valid command, duplicate ID, unauthorized command and invalid transition; reconcile request, ACK, telemetry and outcome records with the reference timeline.',
        'acceptance_criteria': 'Each authorized observation/mode command has an ID, issuer, configuration, requested time, ACK and execution/rejection status; duplicate IDs execute once and unauthorized commands are rejected. Reference role labels do not substitute for actual Arc identities.',
    },

    # ARC-FOREST3-TST-085
    {
        'reference': 'V-GRD-002',
        'name': 'Observation product receipt',
        'method': 'test',
        'objective': 'Confirm durable receipt and publication require complete product data and do not acknowledge interrupted commits.',
        'procedure': 'Compare source, durable receipt and published product field-by-field; interrupt before durable commit and verify no ACK or accepted publication occurs.',
        'acceptance_criteria': 'Ground publication preserves product ID/hash, both band IDs, calibration ID, observation UTC within 0.1 s, WGS84 location within 250 m, validity and software/configuration version; ACK is emitted only after durable hash-matching receipt.',
    },

    # ARC-FOREST3-TST-086
    {
        'reference': 'V-GRD-003',
        'name': 'Observation quality classification',
        'method': 'test',
        'objective': 'Confirm customer status and metadata match labelled products and explain each invalid rejection.',
        'procedure': 'Submit the ten labelled products plus a partial transfer; compare customer-facing status and metadata with expected labels and inspect the rejection reason for each invalid case.',
        'acceptance_criteria': 'Exactly six valid hot fixtures are accepted detections, two valid cold fixtures are accepted no-detection products, and two invalid fixtures have explicit rejection reasons; incomplete products never become accepted detections and operators see incomplete/rejected status.',
    },

    # ARC-FOREST3-TST-087
    {
        'reference': 'V-GRD-004',
        'name': 'Customer delivery latency',
        'method': 'test',
        'objective': 'Confirm delivery latency uses acquisition time and reports nominal, outage, and whole-contact-loss outcomes against the deadline.',
        'procedure': 'Read the nominal and outage rows in the controlled A4 delivery/recovery table; identify ACK and add 60 s publication processing.',
        'acceptance_criteria': 'Delivery latency <= 900 s; outage latency <= 900 s.',
    },

    # ARC-FOREST3-TST-088
    {
        'reference': 'V-INT-001',
        'name': 'Integration activity control',
        'method': 'review',
        'objective': 'Confirm integration activities use the applicable interface revision for each architecture edge.',
        'procedure': 'Reconcile architecture edges against the interface register and assembly sequence; flag any integration step whose applicable interface revision is absent.',
        'acceptance_criteria': 'Before integration, the register covers equipment/structure mounts, EPS power, PAY–OBD data/commands, OBD–COM transfer, ADCS/THM telemetry and COM–ground delivery, with endpoint, owner and configuration revision for every entry.',
    },

    # ARC-FOREST3-TST-089
    {
        'reference': 'V-INT-002',
        'name': 'Electrical interface definition',
        'method': 'review',
        'objective': 'Confirm every electrical pin, return, limit, and role is defined without conflict.',
        'procedure': 'Check every pin and limit against harness and equipment tables; inject conflicting roles or omitted returns into the review checklist and record rejection.',
        'acceptance_criteria': 'Each electrical entry names both endpoints, connector/pins, power/signal/return role, polarity, voltage range and continuous/transient limits; power routes use 12 V ±5% and mode loads from A3. Power pin assignments, Ethernet TX/RX pairs and CAN H/L/return/shield are fixed by D2/D3; CAN is 500 kbit/s with 120 Ω termination at each end.',
    },

    # ARC-FOREST3-TST-090
    {
        'reference': 'V-INT-003',
        'name': 'Integration interface constraints',
        'method': 'review',
        'objective': 'Confirm mechanical interface entries match assembly geometry, attachment, envelope, and torque limits.',
        'procedure': 'Compare mechanical register entries with the dimensioned assembly/CAD representation and inspect attachment, envelope and torque callouts.',
        'acceptance_criteria': 'Mechanical entries identify equipment pair, dimensions, mounting coordinates/fasteners, ≥5 mm keep-out and assembly direction; ground interface is four M4 points, 180×180 mm square, 2 N·m torque within 226×226×227 mm stowed bounds.',
    },

    # ARC-FOREST3-TST-091
    {
        'reference': 'V-INT-004',
        'name': 'Data interface definition',
        'method': 'test',
        'objective': 'Confirm data interfaces preserve valid products and reject corrupt, missing, duplicate, and unsafe resumes.',
        'procedure': 'Exchange valid, corrupt, missing-field, duplicate and resumed products at each data endpoint; verify decoding, rejection and durable ACK semantics.',
        'acceptance_criteria': 'Data entries define source/destination, schema, units, UTC, IDs, validity, rate, integrity hash and ACK/resume rules; payload is 4 Mbit/s, housekeeping 20 kbit/s and application downlink 2.5 Mbit/s, with no double-counted framing. Ground commands carry an authenticated signature, monotonic counter and command ID; CAN messages carry CRC/counter; invalid signature, stale counter, malformed content and unauthorized role cause explicit rejection.',
    },

    # ARC-FOREST3-TST-092
    {
        'reference': 'V-INT-005',
        'name': 'Integration readiness',
        'method': 'review',
        'objective': 'Confirm integration readiness distinguishes missing evidence and limited proceeding decisions from acceptance.',
        'procedure': 'Apply the entry checklist to the planned integration package; enumerate absent evidence and distinguish a documented limited proceeding decision from full subsystem acceptance.',
        'acceptance_criteria': 'System integration entry requires reviewed applicable interface revisions, isolated power/harness checks, matching software/configuration, and disposition of relevant blocking faults.',
    },

    # ARC-FOREST3-TST-093
    {
        'reference': 'V-INT-006',
        'name': 'Assembly and integration procedures',
        'method': 'review',
        'objective': 'Confirm executed integration procedures record configuration, measured results, dispositions, and operator.',
        'procedure': 'Review the controlled ordered procedure and, when executed, record each measured result or authorized disposition against the actual configuration and operator identity.',
        'acceptance_criteria': 'Integration records identify procedure revision/configuration and steps for fixture mounting at 2 N·m, harness inspection, power isolation, software load, interface checkout and end-to-end execution; unexecuted steps remain planned.',
    },

    # ARC-FOREST3-TST-094
    {
        'reference': 'V-INT-007',
        'name': 'Engineering record updates',
        'method': 'review',
        'objective': 'Confirm configuration changes trace affected records and regression cases while preserving mass accounting.',
        'procedure': 'Compare configuration manifests, load tables and change impact list; trace every affected record and regression case, then confirm the 15.5 kg vehicle mass remains within its 16 kg limit.',
        'acceptance_criteria': 'The CFG-A→CFG-B change records FSW-1.0→1.1 scheduling only, unchanged equipment ratings/mass and updated power, sequence, impact and regression records; the vehicle mass remains 15.5 kg against its 16 kg limit.',
    },

    # ARC-FOREST3-TST-095
    {
        'reference': 'V-VRF-001',
        'name': 'Verification method identification',
        'method': 'review',
        'objective': 'Identify verification methods and open coverage for STR-007.',
        'procedure': 'Count active IDs, candidate methods, and case links; review the Requirement→Test mapping and record STR-007 as open verification coverage.',
        'acceptance_criteria': 'The planning register identifies a candidate method for all 102 active requirements; 101 link to existing case IDs and STR-007 alone has no case. In Arc, methods and verification Relationships belong to Tests; candidate source columns are not imported as Requirement fields.',
    },

    # ARC-FOREST3-TST-096
    {
        'reference': 'V-VRF-002',
        'name': 'Verification compliance assessment',
        'method': 'review',
        'objective': 'Confirm verification records have supported results, evidence, and requirement assessments.',
        'procedure': 'Compare each test run to its result, evidence, and requirement assessment; audit every verification record for unsupported acceptance claims.',
        'acceptance_criteria': 'Each verification activity receives an evidence-supported pass/fail/not-assessed disposition for its pinned configuration; an available procedure alone does not constitute a pass.',
    },

    # ARC-FOREST3-TST-097
    {
        'reference': 'V-VRF-003',
        'name': 'Test evidence traceability',
        'method': 'review',
        'objective': 'Confirm each test result links to exact evidence files and configuration.',
        'procedure': 'Inspect each test result and follow its evidence references to the applicable files and configuration.',
        'acceptance_criteria': 'Every test-based verification result links to the exact case/run, procedure revision, article/configuration, actual result, and objective evidence.',
    },

    # ARC-FOREST3-TST-098
    {
        'reference': 'V-VRF-004',
        'name': 'Inspection evidence traceability',
        'method': 'inspection',
        'objective': 'Confirm inspection evidence identifies the observed feature, criterion, and configuration.',
        'procedure': 'Sample each inspection record, open its referenced feature, and compare the observation with the requirement criterion and inspected configuration.',
        'acceptance_criteria': 'Every inspection record identifies the reviewed drawing/model/document revision, exact feature or checklist item, and observed comparison to its stated criterion.',
    },

    # ARC-FOREST3-TST-099
    {
        'reference': 'V-VRF-005',
        'name': 'Verification method and results',
        'method': 'analysis',
        'objective': 'Confirm independent mass, power, energy, data, and RF calculations use controlled units and inputs.',
        'procedure': 'Independently recompute mass, power, energy, data and RF calculations from A2–A5; compare each constraint separately and reject double-counting or an unsupported qualification conclusion.',
        'acceptance_criteria': 'Analysis claims include equation, units, controlled inputs and outputs; additive reserve is (limit−demand)/limit; RF uses dB and thermal uses ranges. Mass is assessed as 15.5 kg against the 16 kg vehicle limit.',
    },

    # ARC-FOREST3-TST-100
    {
        'reference': 'V-VRF-006',
        'name': 'Acceptance disposition control',
        'method': 'review',
        'objective': 'Confirm active requirements receive evidence-backed dispositions before acceptance.',
        'procedure': 'Assess all 102 active requirements and their evidence and dispositions before declaring mission acceptance.',
        'acceptance_criteria': 'Mission acceptance is withheld while any applicable requirement lacks assessment or an open noncompliance lacks authorized disposition; STR-007 and unassessed external qualifications are visibly open, regardless of corrected power and mass results.',
    },

    # ARC-FOREST3-TST-101
    {
        'reference': 'V-OPS-001',
        'name': 'Concurrent imaging and downlink',
        'method': 'test',
        'objective': 'Confirm CFG-A concurrency failure and CFG-B sequential correction remain separately evidenced through delivery.',
        'procedure': 'Read the CFG-A concurrency and CFG-B corrected rows in the controlled A3 power/load table; check maximum power and minimum reserve. Corrected profile: check no concurrent mode, peak demand, reserve, and integrated energy.',
        'acceptance_criteria': 'CFG-A must support simultaneous PAY imaging and COM downlink for the 120 s reference concurrency case, with total demand <=100 W and reserve>=20%. A result exceeding either bound fails. This requirement revision does not accept the separate-mode correction; that requires revision B.',
    },

    # ARC-FOREST3-TST-102
    {
        'reference': 'AN-POWER',
        'name': 'Power scenario analysis',
        'method': 'analysis',
        'objective': 'Check concurrent and corrected power profiles against OPS-001 and MIS-BUD-POWER.',
        'procedure': 'Read the CFG-A concurrency and CFG-B corrected rows in the controlled A3 power/load table; check maximum power and minimum reserve. Corrected profile: check no concurrent mode, peak demand, reserve, and integrated energy.',
        'acceptance_criteria': 'Every interval <=100 W and reserve >=20%; CFG-B has separate imaging and downlink modes.',
    },

    # ARC-FOREST3-TST-103
    {
        'reference': 'AN-MASS',
        'name': 'Mass scenario analysis',
        'method': 'analysis',
        'objective': 'Calculate the seven subsystem masses and compare the 15.5 kg vehicle total with its 16 kg limit.',
        'procedure': 'Use the controlled A2 mass table and the mass Properties (STR_mass, EPS_mass, OBD_mass, PAY_mass, COM_mass, ADCS_mass, THM_mass); compare vehicle_mass with vehicle_mass_limit (16 kg).',
        'acceptance_criteria': 'The calculated vehicle mass is 15.5 kg and <= 16 kg. Physical qualification remains open.',
    },

    # ARC-FOREST3-TST-104
    {
        'reference': 'AN-DATA',
        'name': 'Data scenario analysis',
        'method': 'analysis',
        'objective': 'Check spacecraft, payload, OBD, and communications data allocations and reserves.',
        'procedure': 'Calculate PAY4Mbit/s*120s plus HK20kbit/s*600s. Compare peak-generation allocation and contact capacity separately.',
        'acceptance_criteria': 'Peak<=5.025Mbit/s and peak reserve>=20%; generated volume<=750Mbit and pass reserve>=20%. Payload and HK rate reserves>=20%.',
    },

    # ARC-FOREST3-TST-105
    {
        'reference': 'AN-DELIVERY',
        'name': 'Delivery scenario analysis',
        'method': 'analysis',
        'objective': 'Check nominal and outage delivery latency against the 900 s requirement.',
        'procedure': 'Read nominal and outage-60s delivery-trace rows; identify ACK and add60s publication processing.',
        'acceptance_criteria': 'Both publication times<=900s from earliest acquisition. Contact-lost is explicitly unavailable; it is outside the guaranteed reference cases.',
    },

    # ARC-FOREST3-TST-106
    {
        'reference': 'AN-STORAGE',
        'name': 'Storage scenario analysis',
        'method': 'analysis',
        'objective': 'Check retained occupancy and acknowledgement behavior against the storage requirement.',
        'procedure': 'For nominal/outage/contact-lost queue models retain full observation volume until ACK and bound housekeeping conservatively.',
        'acceptance_criteria': 'Retained occupancy <=2 Gbit; product not released before ACK; contact-lost products remain through 900 s; flash integrity qualification remains open.',
    },

    # ARC-FOREST3-TST-107
    {
        'reference': 'AN-RECOVERY',
        'name': 'Recovery scenario analysis',
        'method': 'analysis',
        'objective': 'Check outage recovery timing, resume offsets, and customer status.',
        'procedure': 'Compare nominal service with outage360–420s; compute remaining service and queue completion; inspect full-contact-loss case.',
        'acceptance_criteria': '60s outage completes before600s; full loss shows noACK/no customer availability. Transfer resumes from the last acknowledged offset without duplicate publication.',
    },

    # ARC-FOREST3-TST-108
    {
        'reference': 'AN-ENERGY',
        'name': 'Energy scenario analysis',
        'method': 'analysis',
        'objective': 'Check corrected mission energy and reserve against the stored-energy requirement.',
        'procedure': 'Calculate corrected900s sequence energy then add1200s idle at20W for eclipse.',
        'acceptance_criteria': 'Eclipse energy<=40Wh and reserve>=20%; generated18.333333Wh passes. This does not test battery hardware or lifetime.',
    },

    # ARC-FOREST3-TST-109
    {
        'reference': 'AN-RF',
        'name': 'RF link analysis',
        'method': 'analysis',
        'objective': 'Calculate reciprocal RF link margins against the 3 dB requirement.',
        'procedure': 'Recompute FSPL from2200MHz and1000km; combine2W transmitter,6/37dBi gains,1+3dB losses and-125dBW receiver thresholds for each direction.',
        'acceptance_criteria': 'Each reciprocal path margin>=3dB; 7.721846dB passes. Radio transmission, licensing and receiver sensitivity remain open.',
    },

    # ARC-FOREST3-TST-110
    {
        'reference': 'AN-QUALITY',
        'name': 'Quality scenario analysis',
        'method': 'analysis',
        'objective': 'Classify valid and invalid scene inputs against the wildfire quality thresholds.',
        'procedure': 'Apply MWIR ≥330 K and MWIR−LWIR ≥10 K only to valid complete A1 scene cases; reject invalid attitude or incomplete input first.',
        'acceptance_criteria': 'Six valid hot detections, two valid cold negatives, two explicit rejections, 10/10 expected outcomes. These checks cover scene-level thresholds; image-processing, calibration and geolocation remain open.',
    },

]
