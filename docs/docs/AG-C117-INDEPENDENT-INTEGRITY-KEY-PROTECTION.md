AG-C117 — Independent Integrity Key Protection Simulation

Project: LT Hub™ AgentGuard
Test ID: AG-C117
Test name: Independent Integrity Key Protection Simulation
Result: PASS — 12/12 checks passed, 0 failed
Scope: Local Python adversarial security simulation

1. Objective

Evaluate whether using an HMAC-SHA256 integrity tag with a separately modelled verification component detects configuration tampering that bypassed the unkeyed SHA-256 approach in AG-C116.

2. Test Method

The simulation used:

- HMAC-SHA256 for actor-configuration integrity verification.
- A separately modelled IntegrityAuthority component.
- A fixed test-only key.
- A trusted-reference store.
- Adversarial modification of actor configuration and integrity tags.

The test examined authorized updates, unauthorized updates, actor modification, invalid tags, dual modification, unkeyed SHA-256 forgery attempts, and recovery of legitimate updates after rejected attempts.

3. Execution Results

Measure| Result
Total checks| 12
Passed| 12
Failed| 0
Unexpected outcomes| 0

Execution result: PASS

All 12 supplied test cases produced their expected outcomes.

4. Key Security Findings

[V] Verified: The supplied execution output demonstrates that the simulation detected actor-only modification, invalid integrity tags, dual modification using the original tag, and an unkeyed SHA-256 forgery attempt.

[V] Verified: The simulated trusted reference remained unchanged after the tested dual-modification attempt.

[I] Interpretation: HMAC-SHA256 provides keyed integrity verification and is stronger than an unkeyed fingerprint when its secret key remains protected.

5. Comparison with Previous Tests

- AG-C115 demonstrated detection of actor-label changes using an unkeyed SHA-256 fingerprint.
- AG-C116 reproduced a bypass when both the actor label and its fingerprint were modified.
- AG-C117 demonstrated detection of the tested modifications when HMAC-SHA256 verification was used.

This is a progression in the simulated design, not proof of production security.

6. Security Limitations

This test does not establish:

- Genuine isolation of the verification component.
- Secure or hardware-backed key storage.
- Protection against key extraction.
- Protection against hostile code accessing the Python process.
- Real administrator authentication.
- Production-grade access control.
- Real payment-system integration.

The test key was fixed and available within the notebook environment. The verification component and store were modelled within the same Python process.

7. Conclusion

AG-C117 passed all 12 local simulation checks.

The results support the narrow conclusion that HMAC-SHA256 verification detected the tested configuration modifications when the original key remained unchanged and available to the verification component.

Further research is required to evaluate independently protected key storage and verification boundaries.

LT Hub™ AgentGuard principle: Evidence before claims. Human oversight before consequential action.