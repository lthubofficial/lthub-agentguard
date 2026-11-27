AG-C118 — Same-Process Integrity Key Exposure and HMAC Forgery Simulation

Project: LT Hub™ AgentGuard
Test ID: AG-C118
Test name: Same-Process Integrity Key Exposure and HMAC Forgery Simulation
Result: PASS — 8/8 checks passed, 0 failed
Scope: Local Python adversarial security simulation

1. Objective

Evaluate whether an attacker with access to the simulated Python process can retrieve the HMAC integrity key, forge a valid integrity tag and modify the trusted actor identity without detection.

This test follows AG-C117, which demonstrated HMAC-based integrity verification while the original key remained unchanged and available to the verification component.

2. Test Method

The simulation used:

- HMAC-SHA256 integrity verification.
- A simulated IntegrityAuthority component.
- A test-only HMAC key.
- A simulated trusted actor configuration.
- Direct same-process access to the authority object's internal key.
- An attacker-controlled actor identity.
- Forged HMAC generation and tag replacement.

The test examined baseline verification, actor modification, key exposure, forged tag generation, acceptance of the modified identity and invalidation of the original tag.

3. Execution Results

Total checks: 8
Passed: 8
Failed: 0

Execution result: PASS — SAME-PROCESS KEY EXPOSURE AND FORGERY REPRODUCED.

All eight supplied test cases matched their expected outcomes.

4. Verified Findings

[V] Based on supplied execution output:

1. Baseline configuration verification succeeded.
2. Actor-only modification was detected.
3. The simulated integrity key was accessible through the store object's authority reference.
4. A forged HMAC matched the authority's verification result.
5. Replacing the original tag with the forged tag caused the modified actor identity to be accepted.
6. The attacker identity became the stored actor identity.
7. The original tag remained invalid for the modified actor.

5. Security Interpretation

[I] The test demonstrates that HMAC-based integrity verification is insufficient when potentially hostile code can retrieve the secret key and replace the integrity tag.

The cryptographic algorithm was not broken. The weakness arose from exposure of the secret key and access to the protected configuration within the same process.

This finding qualifies the result of AG-C117: keyed integrity verification is useful only when the key and verification authority are protected from the attacker.

6. Security Limitations

This was a local Python simulation only.

It did not test:

- Hardware-backed key protection.
- Operating-system process isolation.
- A remote verification service.
- Hardware security modules.
- Trusted execution environments.
- Production identity authentication.
- Real payment execution.
- Real-world compromise of an external key-management system.

The test key was deliberately accessible through the simulated object's internal attribute. This is evidence of exposure in the tested design, not evidence that every HMAC implementation is vulnerable.

7. Relationship to Previous Tests

- AG-C115: Unkeyed SHA-256 actor-configuration integrity monitoring.
- AG-C116: Dual modification bypass of actor configuration and unkeyed fingerprint.
- AG-C117: HMAC-SHA256 verification detected tested modifications while the original key remained unchanged.
- AG-C118: Same-process key exposure enabled HMAC forgery and reproduced an authorization-configuration bypass.

8. Conclusion

AG-C118 passed all eight simulation checks.

The supplied output demonstrates that an attacker able to access the simulated HMAC key and replace the integrity tag can forge a valid tag and alter the stored actor identity.

The next research requirement is to evaluate verification architectures in which the integrity key is not directly accessible to potentially hostile application code.

LT Hub™ principle: Evidence before claims. Human oversight before consequential action.