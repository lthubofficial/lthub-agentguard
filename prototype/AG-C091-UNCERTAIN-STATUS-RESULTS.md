Test 91 — Fail Closed on Uncertain Request Status

Project: LT Hub™ AgentGuard
Test ID: AG-C091
Status: PASS — 6/6 checks
Total trials: 500
Trials per status: 100
Test type: Local in-memory status simulation

1. Objective

Evaluate whether the retry logic distinguishes confirmed commitment, known non-commitment, and uncertain request states.

The intended behaviour is to recognize an already committed request, permit a retry for a known "NOT_COMMITTED" request, and reject uncertain statuses without creating another simulated effect.

2. Test configuration

Each trial used request ID "REQ-091" and transaction "TX-091-A", amount 1000 ZAR, recipient "SUPPLIER-A".

Five initial statuses were evaluated:

- "COMMITTED"
- "PENDING"
- "UNKNOWN"
- "PARTIAL"
- "NOT_COMMITTED"

The retry function operated on an in-memory request registry and effect list.

3. Observed results [V]

Initial status| Observed response| Trials
"COMMITTED"| "ALREADY_COMMITTED"| 100/100
"PENDING"| "STATUS_UNCERTAIN"| 100/100
"UNKNOWN"| "STATUS_UNCERTAIN"| 100/100
"PARTIAL"| "STATUS_UNCERTAIN"| 100/100
"NOT_COMMITTED"| "COMMITTED"| 100/100

Additional observations:

- Committed requests retained exactly one simulated effect in 100/100 cases.
- Uncertain states retained zero simulated effects in 300/300 cases.
- Known "NOT_COMMITTED" requests produced one effect in 100/100 cases.
- Total trials: 500.
- Unexpected outcomes: 0.
- Checks passed: 6/6.
- Overall result: PASS.

4. Interpretation [I]

The observed behaviour is consistent with a fail-closed policy for the predefined uncertain statuses. The retry logic recognized committed requests, permitted retry for the explicitly known non-committed state, and returned "STATUS_UNCERTAIN" for pending, unknown, and partial states.

This supports the implemented decision rules within the local simulation.

5. Limitations

- Status values were supplied directly by the test; they were not recovered from a real system.
- Request records and effects were held in memory.
- No database, payment provider, external side effect, crash recovery, or distributed execution was tested.
- The test does not establish that a production system can determine commitment status correctly after an ambiguous failure.
- A real implementation would need authoritative reconciliation before deciding whether retrying an uncertain operation is safe.

6. Conclusion [V]/[I]

Observed conclusion [V]: All 500 cases matched the programmed expectations. All six checks passed, with zero unexpected outcomes.

Interpretation [I]: Explicitly separating committed, uncommitted, and uncertain states helps prevent blind retries in this model.

Unverified hypothesis [H]: A production implementation with durable records and trustworthy reconciliation could apply this policy across process failures and external systems; that remains untested.

LT Hub™ AgentGuard principle: AI may research, analyse, recommend and prepare. Humans retain authority over money, identity, sensitive information and irreversible decisions.

Next frontier: Test 92 — examine how the system should respond when a request record contains a malformed or missing status field.