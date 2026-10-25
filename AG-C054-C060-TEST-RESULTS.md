LT Hub™ AgentGuard — Test Results & Evidence Register

Brand: LT Hub™ | Creative AI Solutions Powered by Intelligence
Record ID: LTH-AG-TEST-001
Control Group: AG-C054–AG-C060
Research Area: AI Agent Security Risk — Unbounded Consumption
Document Status: Evidence-record template
Version: 1.0

1. Purpose

This register records the implementation status, testing status, supporting evidence, findings, and residual risks for controls AG-C054–AG-C060.

A documented proposal is not proof of implementation. An implementation is not proof of effectiveness. A test plan is not a test result.

All conclusions must be supported by retained evidence. Unknown, unavailable, and untested information must be reported honestly.

2. Evidence Classification

- [V] Verified: Directly supported by inspected evidence, such as a configuration record, test log, reproducible observation, or reviewed source.
- [I] Inference: An interpretation or conclusion drawn from available evidence. State the reasoning and limitations.
- [H] Hypothesis: A proposed control, expected outcome, or claim that has not yet been demonstrated.
- [GAP] Evidence gap: Required information or evidence is missing, inaccessible, or insufficient.
- [FAIL] Failed criterion: An observed result does not satisfy a predefined acceptance criterion.

Evidence labels apply to individual claims, not automatically to an entire document or control.

3. Status Definitions

Implementation status

Select one:

- Not started: Implementation work has not begun.
- In progress: Implementation work has begun but is incomplete.
- Implemented — unverified: Configuration or code evidence indicates implementation, but operational behaviour has not yet been validated.
- Partially implemented: Only some intended scope or functionality is implemented.
- Not applicable: The control does not apply to the documented system; provide a reason and supporting evidence.
- Unknown: Available evidence is insufficient to determine implementation status.

Test status

Select one:

- Not tested: No execution of the defined test has been evidenced.
- Planned: A test procedure exists but has not been executed.
- In progress: Testing has started but is incomplete.
- Passed: All required acceptance criteria passed within the documented test scope.
- Failed: One or more required acceptance criteria failed.
- Partially passed: Some criteria passed and others failed or remain untested.
- Blocked: Testing could not proceed; document the reason.
- Inconclusive: The available results do not support a reliable pass or fail decision.
- Not applicable: Testing is not applicable, with justification documented.

A control must not be marked Passed solely because its documentation exists.

4. Control Status Summary

Control| Control Name| Implementation Status| Test Status| Evidence Record
AG-C054| Request Rate Limits| Unknown until verified| Not tested until evidence confirms otherwise| AG-C054-TEST-001
AG-C055| Usage and Cost Budgets| Unknown until verified| Not tested until evidence confirms otherwise| AG-C055-TEST-001
AG-C056| Input and Output Limits| Unknown until verified| Not tested until evidence confirms otherwise| AG-C056-TEST-001
AG-C057| Execution Timeouts| Unknown until verified| Not tested until evidence confirms otherwise| AG-C057-TEST-001
AG-C058| Agent Loop Protection| Unknown until verified| Not tested until evidence confirms otherwise| AG-C058-TEST-001
AG-C059| Resource Monitoring| Unknown until verified| Not tested until evidence confirms otherwise| AG-C059-TEST-001
AG-C060| Downstream Action Limits| Unknown until verified| Not tested until evidence confirms otherwise| AG-C060-TEST-001

Initial status note: These are conservative placeholder statuses. Replace them only after checking implementation records and actual test evidence. Saving a validation plan does not establish implementation or successful testing.

5. Individual Control Test Record

Copy this section once for each control from AG-C054 through AG-C060.

Control Identification

- Control ID:
- Control name:
- Test record ID:
- Record version:
- Record date:
- Responsible reviewer or tester:
- System, component, or workflow in scope:
- Related risk:
- Related source record:

A. Objective and Scope

- Security objective:
- Threat or failure scenario:
- System boundaries:
- Included components:
- Excluded components:
- Assumptions:
- Known limitations:

B. Implementation Status

- Status: [Select one implementation status from Section 3.]
- Implementation evidence reference(s):
- Configuration or code location:
- Enforcement point:
- Configured threshold or decision rule:
- Applicable scope: User / agent / workflow / tool / service / global / other.
- Dependencies:
- Provider or platform limitations:
- Reviewer notes:

If implementation cannot be verified, retain Unknown or Implemented — unverified, as appropriate. Do not infer implementation from a written proposal.

C. Test Definition

- Test status before execution:
- Test objective:
- Authorised test environment:
- Preconditions:
- Test data or scenario:
- Expected result:
- Acceptance criteria defined before testing:
- Safety and cost controls:
- Test procedure reference:

Testing must be authorised and bounded. Avoid production disruption, unnecessary charges, exposure of secrets, or unauthorised third-party activity.

D. Execution Record

- Execution date and time, including timezone:
- Tester or responsible reviewer:
- Test case ID:
- Configuration used:
- Actual input or trigger:
- Observed system behaviour:
- Actual measurements and units:
- Expected versus actual result:
- Logs or output references:
- Errors or interruptions:
- Was the test repeated? If so, how many times and why?
- Did the result reproduce consistently?
- Execution notes:

If a test has not been run, enter Not executed. Never create fictional measurements, timestamps, logs, or test outcomes.

E. Test Outcome

- Final test status: Not tested / Passed / Failed / Partially passed / Blocked / Inconclusive / Not applicable.
- Acceptance criteria met:
- Acceptance criteria not met:
- Unverified criteria:
- Reason for the outcome:
- Reviewer conclusion:
- Review date:

A pass applies only to the tested scenarios, configuration, version, and scope. It does not establish universal effectiveness or complete prevention.

F. Evidence References

Evidence ID| Evidence Type| Description| Location or Reference| Date Collected| Integrity / Access Notes
EVID-001| Configuration / Log / Screenshot / Test output / Source / Other| Describe the evidence| Add verified path or URL| Add actual date| Record limitations and access restrictions
EVID-002| Configuration / Log / Screenshot / Test output / Source / Other| Describe the evidence| Add verified path or URL| Add actual date| Record limitations and access restrictions

Use actual evidence identifiers and locations. Remove unused example rows. Restrict access to sensitive logs and redact credentials, access tokens, personal data, and other secrets.

G. Findings

Finding ID| Observation| Evidence Reference| Severity / Priority| Status| Required Follow-up
FIND-001| Describe an observed issue or evidence gap| Add evidence ID| Justify the rating or mark unassessed| Open / In progress / Closed| Define the next action

Do not record an assumed vulnerability as a confirmed finding. Distinguish observed failures from hypotheses and missing evidence.

H. Residual Risks

- Risks remaining after the tested control:
- Untested attack or failure scenarios:
- Concurrency, retries, or delegated-workflow gaps:
- Provider-side or third-party limitations:
- Monitoring or alerting gaps:
- Potential bypasses:
- Impact if the control fails:
- Compensating controls:
- Risk owner or responsible reviewer:
- Follow-up action:
- Target review date:
- Residual risk assessment: Not assessed / Low / Medium / High / Critical — use a documented rating method and explain the basis.

Do not assign a low residual risk merely because no failure has been observed. Lack of testing is not evidence of safety.

I. Final Review and Sign-off

- Implementation status confirmed by evidence: Yes / No / Partially
- Test result supported by evidence: Yes / No / Not tested
- Evidence references checked: Yes / No / Partially
- Findings documented: Yes / No / Not applicable
- Residual risks documented: Yes / No
- Independent review completed: Yes / No / Not required, with justification
- Reviewer conclusion:
- Reviewer and date:

Evidence limitation: This record documents only the evidence referenced within it. It does not independently certify system security, compliance, or complete prevention of unbounded consumption.

---

6. Control-Specific Evidence Checklist

AG-C054 — Request Rate Limits

- Configured rate and time window.
- Scope of enforcement and identity key.
- Below-limit, boundary, above-limit, and relevant concurrency test results.
- Observed responses and rate-limit logs.
- Retry behaviour and any bypasses.

AG-C055 — Usage and Cost Budgets

- Budget amount or usage ceiling, unit, and period.
- Usage measurement source and configuration.
- Alert threshold and delivery evidence.
- Evidence of actual enforcement, if the provider supports it.
- Documented provider restrictions and cost-related limitations.

An alert is not proof of a hard spending cap.

AG-C056 — Input and Output Limits

- Input and output thresholds, units, and enforcement points.
- Below-limit, boundary, and above-limit test cases.
- Actual rejection, truncation, or other documented limit behaviour.
- Relevant processing or usage measurements.
- Coverage gaps across endpoints, retries, and concurrent requests.

AG-C057 — Execution Timeouts

- Timeout configuration and applicable scope.
- Normal-duration and timeout-boundary test results.
- Termination and cancellation observations.
- Cleanup and downstream task status.
- Evidence of whether external operations continue after a client timeout.

AG-C058 — Agent Loop Protection

- Maximum iteration and retry configuration.
- Normal-completion and controlled repeated-action tests.
- Evidence that limits trigger the expected termination or recovery.
- Nested, parallel, and delegated workflow coverage where applicable.
- Duplicate actions, bypasses, or continued execution.

AG-C059 — Resource Monitoring

- Available metrics, units, and baseline.
- Alert thresholds and monitoring coverage.
- Controlled normal and elevated-usage scenarios.
- Alert generation and delivery evidence.
- Missing telemetry, false alerts, missed alerts, and monitoring delays.

AG-C060 — Downstream Action Limits

- Action-count, frequency, and queue limits.
- Enforcement point and scope.
- Below-limit, boundary, and above-limit tests.
- Retry, concurrent, and delegated-workflow test results.
- Evidence of audit events and separate authorisation for sensitive actions.

7. Review Rules

1. Keep implementation status separate from test status.
2. Keep proposed controls labelled [H] until supported by evidence.
3. Record test criteria before execution to reduce hindsight bias.
4. Link each test conclusion to specific evidence.
5. Record failures, inconclusive results, and limitations instead of omitting them.
6. Do not claim a control passed outside its tested scope.
7. Re-test after material configuration, code, provider, or architecture changes.
8. Update this register when new evidence changes a prior conclusion.

8. Source Reference

[V] Source reviewed: OWASP GenAI Security Project, LLM10:2025 Unbounded Consumption.

Official source: https://genai.owasp.org/llmrisk/llm102025-unbounded-consumption/

The source supports the relevance of resource limits, rate limiting, timeouts, logging, monitoring, anomaly detection, and limits on queued and total actions. It does not verify the implementation or effectiveness of LT Hub™ AgentGuard controls.

Source review date: Enter the actual date the source was reviewed.

Record maintenance: Update this document only when supported by new evidence, a documented review, or a recorded change.

AG-C054 — Request Rate Limits

Test Record ID: AG-C054-TEST-001

Control reference: AG-C054 — Request Rate Limits

Evidence classification: [H] Proposed control; implementation and effectiveness not yet established by this record.

1. Implementation Status

Status: Unknown — pending evidence review.

Implementation evidence: Not yet recorded.

Enforcement point: Not yet established.

Configured request-rate threshold: Not yet established.

Scope of enforcement: Not yet established.

2. Test Status

Status: Planned — test not yet evidenced as executed.

Test objective: Determine whether requests exceeding a documented rate limit are handled according to the configured policy.

Required test cases:

- Requests below the configured limit.
- Requests at the configured limit.
- Requests above the configured limit.
- Concurrent requests, where applicable.
- Retry behaviour and potential limit bypasses, where applicable.

Expected behaviour: Requests within the permitted limit are handled according to policy. Requests exceeding the limit are restricted or handled according to documented enforcement rules. Relevant events are recorded.

Acceptance criteria: Define the exact expected behaviour and measurable limits before executing the tests.

3. Execution Results

Execution date and time: Not recorded.

Test environment: Not established.

Actual measurements: Not recorded.

Observed behaviour: Not recorded.

Test outcome: Not tested.

4. Evidence References

No implementation or execution evidence has yet been attached to this record.

Add evidence identifiers and verified file paths or URLs when actual configuration, logs, or test results become available.

5. Findings

Current finding: [GAP] Implementation and test evidence have not yet been recorded in this test record.

Follow-up: Identify the system or component that would enforce request-rate limits and determine whether it is implemented and accessible for authorised testing.

6. Residual Risks

Until implementation and testing are evidenced, it remains unknown whether excessive request rates are restricted. Concurrent requests, retries, distributed workflows, and differences between application-level and provider-level enforcement may require separate assessment.

Conclusion: This record establishes a testing baseline only. It does not demonstrate implementation, successful enforcement, or prevention of resource exhaustion.

AG-C055 — Usage and Cost Budgets

Test Record ID: AG-C055-TEST-001

Control reference: AG-C055 — Usage and Cost Budgets

Evidence classification: [H] Proposed control; implementation and effectiveness not yet established by this record.

1. Implementation Status

Status: Unknown — pending evidence review.

Implementation evidence: Not yet recorded.

Budget or usage ceiling: Not yet established.

Measurement source and units: Not yet established.

Budget period: Not yet established.

Enforcement mechanism: Not yet established.

Alerting mechanism: Not yet established.

2. Test Status

Status: Planned — test not yet evidenced as executed.

Test objective: Determine whether usage is measured accurately against a documented budget or ceiling, and whether configured alerts or enforcement mechanisms behave as expected.

Required test cases:

- Usage below the configured alert threshold.
- Usage reaching or crossing the alert threshold.
- Usage approaching and exceeding the configured ceiling, where safe and supported.
- Alert generation and delivery.
- Enforcement behaviour, tested separately from alerting, if a hard limit is supported.
- Relevant concurrent requests or workflows, where applicable.
- Provider-side limits and reporting delays, where applicable.

Use a sandbox, simulated usage records, or another authorised test mechanism where possible. Do not deliberately incur charges or assume a provider offers a hard spending cap.

3. Expected Behaviour

Usage is measured using documented units and a known reporting source. Configured thresholds trigger the expected alerts. If an enforceable ceiling is supported and configured, exceeding it results in the documented restriction or response.

Alert delivery, budget enforcement, and provider billing limits must be evaluated separately. An alert alone does not prove that additional usage or charges have been prevented.

4. Acceptance Criteria

Before testing, document:

- The budget or usage ceiling and its units.
- The applicable user, agent, workflow, service, or account scope.
- The budget period and reset behaviour.
- The expected threshold and alert timing.
- Whether a hard limit is technically supported.
- The expected response when a limit is reached.
- Acceptable measurement and reporting delays.

A test can pass only against these predefined criteria and the scope actually examined.

5. Execution Results

Execution date and time: Not recorded.

Test environment: Not established.

Configured budget and thresholds: Not recorded.

Actual usage measurements: Not recorded.

Alert generation and delivery: Not recorded.

Observed enforcement behaviour: Not recorded.

Test outcome: Not tested.

6. Evidence References

No implementation or execution evidence has yet been attached to this record.

When available, retain verified references to:

- Budget and threshold configuration.
- Usage records and their units.
- Alert generation and delivery logs.
- Enforcement or restriction results.
- Provider documentation describing applicable limitations.
- Test inputs, timestamps, errors, and observed outcomes.

Use actual evidence identifiers and verified paths or URLs. Do not invent measurements, alerts, configurations, or results.

7. Findings

Current finding: [GAP] Implementation, measurement, alerting, and enforcement evidence have not yet been recorded in this test record.

Follow-up: Identify the relevant usage-measurement source and determine which budget, alert, and enforcement capabilities are available in the intended system.

8. Residual Risks

Even where alerts work, usage may continue to increase before a human or automated response occurs. Reporting delays, estimated costs, concurrent operations, provider billing behaviour, and unsupported hard caps may leave residual financial exposure.

Usage budgets should be assessed alongside request rate limits, input/output limits, execution timeouts, agent loop protection, resource monitoring, and downstream action limits.

Conclusion: This record establishes a testing baseline only. It does not demonstrate that a budget is configured, an alert works, a hard spending cap exists, or financial losses are prevented.