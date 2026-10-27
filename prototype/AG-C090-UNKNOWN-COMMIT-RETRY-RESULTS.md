Test 90 — Safe Retry When Commit Status Is Unknown

Project: LT Hub™ AgentGuard
Test ID: AG-C090
Status: PASS — 6/6 checks
Trials: 100 per scenario; 200 total
Test type: Local in-memory retry simulation

1. Objective

Evaluate whether retrying the same request ID and payload avoids a duplicate simulated effect when confirmation of an earlier operation is lost, while allowing a retry to proceed when the earlier operation did not commit.

2. Test scenarios

Scenario A — Commit occurred, confirmation lost

The operation was committed to an in-memory request registry and its effect log. The caller was then given a simulated "CONFIRMATION_LOST" outcome. A retry with the same request ID and payload was expected to return "ALREADY_COMMITTED".

Scenario B — Commit did not occur

The initial operation was skipped to simulate a pre-commit failure. The retry was expected to return "COMMITTED" and record one effect.

Both scenarios used request ID "REQ-090" and transaction "TX-090-A", amount 1000 ZAR, recipient "SUPPLIER-A".

3. Observed results [V]

- Trials per scenario: 100
- Committed but confirmation lost — recognized retries: 100/100
- Not committed — successful retries: 100/100
- Exactly one effect in committed cases: 100/100
- Exactly one effect in previously uncommitted cases: 100/100
- Request records matched the intended payload: 200/200
- Unexpected outcomes: 0
- Checks passed: 6/6
- Overall result: PASS

4. Interpretation [I]

The results are consistent with the intended retry behaviour in the local simulation. When the first operation had already been recorded, the retry was recognized without adding another effect. When the first operation had not been recorded, the retry committed one effect.

5. Limitations

- The request registry and effect log were in-memory Python objects.
- Confirmation loss and pre-commit failure were simulated through control flow, not real network or storage failures.
- No process restart, durable database, distributed worker, or external payment service was involved.
- The test does not establish exactly-once execution across external systems.
- The result depends on the simplified commit function used in the test.

6. Conclusion [V]/[I]

Observed conclusion [V]: All 200 scenario runs behaved as expected, and all six programmed checks passed.

Interpretation [I]: The local simulation supports retry recognition for an existing request and safe retry after a simulated pre-commit failure.

Unverified hypothesis [H]: A production implementation would need durable idempotency records and a reliable design for coordinating stored commit status with external side effects.

LT Hub™ AgentGuard principle: AI may research, analyse, recommend and prepare. Humans retain authority over money, identity, sensitive information and irreversible decisions.

Next frontier: Test 91 — examine recovery when a retry encounters an existing request record whose status is incomplete or uncertain.