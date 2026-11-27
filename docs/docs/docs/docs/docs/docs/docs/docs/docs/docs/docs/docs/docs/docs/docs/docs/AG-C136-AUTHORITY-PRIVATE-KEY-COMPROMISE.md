AG-C136 — Authority Private-Key Compromise and Forged Approval Simulation

Project: LT Hub™ AgentGuard
Test ID: AG-C136
Status: Passed
Total checks: 15
Passed: 15
Failed: 0
Cryptographic mechanism: Ed25519
Environment: Local Python simulation

1. Objective

Evaluate the security consequences of an attacker obtaining a simulated recovery authority's Ed25519 private signing key.

Determine whether the compromised key can produce forged approval responses, whether the application can reject the compromised key after revocation, and whether a replacement authority can restore trusted approval operations.

2. Test implementation

The simulation included:

- A legitimate Ed25519 recovery authority.
- An application-side public-key verifier.
- A simulated attacker without the private signing key.
- Deliberate exposure of the authority's private key to simulate compromise.
- Forged approval generation.
- Application-side key revocation.
- Replacement authority generation.
- Validation of old and replacement signatures.
- Malformed and modified response rejection.
- Simulated authority unavailability.

3. Observed results

[V] Final execution results

Measurement| Result
Total checks| 15
Passed| 15
Failed| 0
Final outcome| PASS

3.1 Private-key compromise

The attacker without the authority private key could not forge an accepted approval.

After simulated private-key compromise, the attacker successfully generated a forged approval signature.

The application accepted this forged approval before revocation.

Result: PASS — attack successfully reproduced.

This is an important vulnerability demonstration. Possession of the trusted signing key allows an attacker to impersonate the authority in the tested architecture.

3.2 Revocation and recovery

The application rejected the compromised key after its simulated revocation.

The forged approval was also rejected after revocation.

A replacement authority successfully generated a new approval, which the application accepted.

The old compromised-key signature remained rejected after replacement.

3.3 Additional validation

The simulation also verified rejection of:

- An unrelated authority signing key.
- Malformed signatures.
- Modified signed responses.
- Approval attempts during authority unavailability.

4. Evidence assessment

[V] Observed

All 15 checks passed.

The simulation reproduced successful forgery using a compromised private signing key and demonstrated rejection after the application-side revocation operation.

A replacement authority successfully restored approval verification.

[I] Interpretation

The results reinforce two important security requirements:

1. Private signing keys must be protected against unauthorized extraction and use.
2. Compromised authority keys must be revocable through a trusted mechanism, with a controlled replacement process.

The simulation also illustrates that asymmetric cryptography alone cannot protect a system when its trusted private signing key is compromised.

5. Limitations

- Private-key compromise was deliberately simulated by exposing an in-memory Python object.
- Revocation was an application-side in-memory control.
- The revocation mechanism was not independently secured.
- No hardware security module, production key vault or external key-management service was tested.
- No independent authority process or remote infrastructure was used.
- No durable revocation registry or persistent key lifecycle was implemented.
- No production payment system or real AI-agent execution was tested.
- No independent security audit was performed.

6. Conclusion

AG-C136: PASS — All 15 compromise simulation checks passed.

The simulation successfully reproduced the ability to forge an authority approval after private-key compromise.

It also demonstrated that the tested application rejected the compromised key after revocation and accepted a replacement authority's approval.

These results support further research into independently protected revocation registries, private-key custody and secure authority replacement.

All findings are limited to the local Python simulation environment.

LT Hub™ AgentGuard

Evidence before claims. Human oversight before consequential action.

Human Authority is a Security Boundary.