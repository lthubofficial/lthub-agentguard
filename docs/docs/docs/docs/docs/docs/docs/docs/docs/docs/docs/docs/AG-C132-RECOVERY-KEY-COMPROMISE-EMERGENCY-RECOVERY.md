AG-C132 — Recovery-Key Compromise and Emergency Recovery Simulation

Project: LT Hub™ AgentGuard
Test ID: AG-C132
Status: PASS — 18/18 checks passed
Failures: 0
Scope: Local Python simulation
Evidence classification: [V] Observed | [I] Interpretation | [H] Hypothesis

1. Objective

Investigate how a simulated recovery system behaves when its active cryptographic recovery key is compromised.

The test evaluates:

- Forgery using a compromised HMAC key.
- Emergency key revocation.
- Rejection of previously valid snapshots.
- Rejection of attacker-forged snapshots.
- Fail-closed behaviour while no replacement key is available.
- Installation and activation of a replacement key.
- Recovery using the replacement key.
- Rejection of invalid key material and tampered recovery data.

2. Test implementation

The simulation implemented:

- HMAC-SHA256 snapshot authentication.
- A simulated recovery-key authority.
- Active key identification.
- A compromised-key registry.
- A revoked-key registry.
- Emergency revocation.
- Replacement-key installation.
- Recovery snapshot validation.
- Fail-closed verification when no active trusted key is available.

Three local test keys were used: compromised, replacement, and unrelated.

3. Observed results

#| Test condition| Result
1| Original snapshot verifies before compromise response| PASS
2| Original snapshot recovers before compromise response| PASS
3| Compromised-key attacker forges valid HMAC| PASS — vulnerability reproduced
4| Forged snapshot reaches recovery before revocation| PASS — vulnerability reproduced
5| Emergency revocation succeeds| PASS
6| Compromised key recorded in compromise registry| PASS
7| Compromised key recorded as revoked| PASS
8| Previously valid snapshot rejected after revocation| PASS
9| Attacker-forged snapshot rejected after revocation| PASS
10| Recovery fails closed without replacement key| PASS
11| Replacement key installs successfully| PASS
12| Replacement key becomes active| PASS
13| Replacement key verifies newly signed snapshot| PASS
14| Recovery succeeds using replacement key| PASS
15| Revoked key identifier cannot be reinstalled| PASS
16| Unrelated key material rejected| PASS
17| Tampered replacement snapshot rejected| PASS
18| Malformed replacement snapshot cannot be recovered| PASS

4. Critical security finding

[V] Compromised-key forgery reproduced.

The simulation demonstrated that an attacker possessing the legitimate HMAC key could generate a matching authentication tag for a modified recovery snapshot.

The forged snapshot passed verification and reached the simulated recovery function before revocation.

This is expected HMAC behaviour when the signing key is compromised. It is not evidence of a cryptographic weakness in HMAC-SHA256 itself.

[V] Emergency revocation response observed.

Following simulated revocation:

- The original snapshot was rejected.
- The attacker-forged snapshot was rejected.
- Recovery failed closed while no replacement key was active.
- The replacement key was installed and activated.
- Recovery succeeded using a newly authenticated snapshot.

5. Evidence assessment

[V] All 18 checks passed with zero failures.

[I] The results demonstrate that the simulated authority enforced its defined compromise-response sequence, including revocation and replacement-key recovery.

[I] The most significant finding is that key compromise defeats the integrity guarantee provided by HMAC while the compromised key remains trusted.

6. Limitations

This simulation does not establish:

- Independent key custody.
- Hardware Security Module protection.
- Production key revocation.
- Secure key distribution.
- Secure replacement-key generation.
- Protection against privileged attackers.
- Durable or distributed revocation state.
- Protection against rollback of revocation records.
- Production disaster recovery.
- Real payment or transaction security.

The authority and keys remain inside the same Python process. The old key material remains in the simulated key dictionary after revocation; rejection is enforced through the revocation registry. The registry itself is not independently protected.

7. Conclusion

[V] AG-C132 completed with 18/18 checks passed.

[V] Possession of the compromised HMAC key permitted successful forgery before revocation.

[V] Emergency revocation prevented subsequent verification using that key in the simulation.

[I] The test provides evidence for simulated compromised-key detection, emergency revocation, and replacement recovery behaviour.

[H] Independent key custody, durable revocation records, and externally protected recovery authority may strengthen this architecture, but each requires separate implementation and testing.

AG-C132 is a local research simulation, not a production security certification.

8. LT Hub™ AgentGuard principle

Evidence before claims. Human oversight before consequential action.

Human Authority is a Security Boundary.