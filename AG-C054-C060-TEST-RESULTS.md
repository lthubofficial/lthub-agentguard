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

AG-C056 — Input and Output Limits

Test Record ID: AG-C056-TEST-001

Control reference: AG-C056 — Input and Output Limits

Evidence classification: [H] Proposed control; implementation and effectiveness not yet established by this record.

1. Implementation Status

Status: Unknown — pending evidence review.

Implementation evidence: Not yet recorded.

Input-size limit and units: Not yet established.

Output-size limit and units: Not yet established.

Processing-workload limits: Not yet established.

Enforcement point and scope: Not yet established.

Behaviour when a limit is reached: Not yet established.

2. Test Status

Status: Planned — test not yet evidenced as executed.

Test objective: Determine whether the intended system enforces documented input, output, and processing-workload limits and handles limit breaches according to policy.

Required test cases:

- Input below, at, and above the configured limit.
- Output within and beyond the configured limit, where safely testable.
- Processing workloads below and above documented bounds.
- Oversized or malformed inputs, where relevant to the control.
- Concurrent requests and retries, where applicable.
- Consistency of enforcement across relevant entry points or workflows.
- Appropriate logging or reporting when a limit is reached.

Define the test boundaries before execution. Use bounded test data and an authorised environment to avoid unnecessary resource use or provider charges.

3. Expected Behaviour

Inputs and outputs within configured bounds are handled according to the documented policy. Requests exceeding a limit are rejected, truncated, constrained, or otherwise handled according to the specified behaviour. Processing constraints are enforced where supported. Relevant outcomes and errors are recorded.

The observed behaviour must match the actual configured policy; do not assume that all providers or components support identical limits.

4. Acceptance Criteria

Before testing, document:

- Each applicable limit and its units.
- The component that enforces the limit.
- Whether the limit is applied before or after processing begins.
- Expected behaviour at and beyond the limit.
- Applicable handling for concurrent requests and retries.
- Required logs or events.
- Known provider or architecture limitations.

A test passes only when the observed result meets its predefined criteria within the documented scope.

5. Execution Results

Execution date and time: Not recorded.

Test environment: Not established.

Configuration and thresholds: Not recorded.

Actual test inputs and outputs: Not recorded.

Observed processing behaviour: Not recorded.

Errors, bypasses, or unsupported limits: Not recorded.

Test outcome: Not tested.

6. Evidence References

No implementation or execution evidence has yet been attached to this record.

When available, retain verified references to:

- Configuration or code showing the enforced limits.
- Test-case descriptions and bounded test data.
- Actual input and output measurements.
- Processing or usage records, where available.
- Relevant logs, errors, and limit-breach responses.
- Evidence of testing across applicable entry points or workflows.

Use actual evidence identifiers and verified paths or URLs. Redact credentials, personal information, and other sensitive data.

7. Findings

Current finding: [GAP] Implementation, configured thresholds, enforcement behaviour, and test results have not yet been recorded in this test record.

Follow-up: Identify the input, output, and workload limits supported by the intended system and determine how their enforcement can be verified.

8. Residual Risks

Limits may not cover every processing stage or entry point. Tokenization overhead, concurrent workloads, retries, delegated workflows, provider-side processing, and delayed rejection may create additional resource consumption. A limit on generated output does not necessarily limit the resources consumed before that output is produced.

Assess complementary controls such as rate limits, usage budgets, execution timeouts, resource monitoring, loop protection, and downstream action limits.

Conclusion: This record establishes a testing baseline only. It does not demonstrate that any limit is implemented, successfully enforced, or sufficient to prevent resource exhaustion.

AG-C057 — Execution Timeouts

Test Record ID: AG-C057-TEST-001

Control reference: AG-C057 — Execution Timeouts

Evidence classification: [H] Proposed control; implementation and effectiveness not yet established by this record.

1. Implementation Status

Status: Unknown — pending evidence review.

Implementation evidence: Not yet recorded.

Configured timeout duration and units: Not yet established.

Enforcement point: Not yet established.

Cancellation mechanism: Not yet established.

Cleanup and downstream-task behaviour: Not yet established.

2. Test Status

Status: Planned — test not yet evidenced as executed.

Test objective: Determine whether operations exceeding a documented execution-time limit are terminated, cancelled, or otherwise handled according to the configured policy.

Required test cases:

- An operation that completes within the timeout.
- An operation that approaches the timeout boundary.
- A controlled operation that exceeds the configured timeout.
- Cancellation and cleanup behaviour, where supported.
- The status of dependent or downstream tasks after a timeout.
- Retry behaviour following a timeout.
- External provider operations that may continue after the local client stops waiting, where applicable.

Use an authorised test environment and bounded operations. Avoid production disruption, unnecessary charges, and tests against third-party services without permission.

3. Expected Behaviour

Operations completing within the permitted duration follow the normal workflow. Operations exceeding the configured timeout trigger the documented timeout response.

Where cancellation is supported, verify whether it reaches the underlying operation rather than merely ending the local wait. Cleanup, downstream task handling, and retry behaviour should follow documented policy. Relevant timeout events and outcomes should be recorded.

A client-side timeout must not automatically be treated as proof that the underlying operation stopped.

4. Acceptance Criteria

Before testing, document:

- The timeout threshold and units.
- The operation or workflow covered.
- The enforcement point.
- The expected response when the timeout is reached.
- Whether cancellation propagates to the underlying operation.
- Required cleanup and downstream-task behaviour.
- Retry policy and required audit events.
- Known provider or architecture limitations.

A test passes only when the observed behaviour meets its predefined criteria within the tested scope.

5. Execution Results

Execution date and time: Not recorded.

Test environment: Not established.

Configured timeout: Not recorded.

Actual execution durations: Not recorded.

Observed termination or cancellation behaviour: Not recorded.

Cleanup and downstream-task results: Not recorded.

Evidence of underlying operations stopping: Not recorded.

Test outcome: Not tested.

6. Evidence References

No implementation or execution evidence has yet been attached to this record.

When available, retain verified references to:

- Timeout configuration or code.
- Test-case descriptions and execution timestamps.
- Observed operation durations.
- Timeout, cancellation, and cleanup logs.
- Downstream-task status and retry records.
- Provider responses or other evidence relevant to underlying operation termination.
- Errors, incomplete cancellations, and other deviations.

Use actual evidence identifiers and verified paths or URLs. Redact credentials, tokens, personal data, and other sensitive information.

7. Findings

Current finding: [GAP] Implementation, timeout configuration, cancellation behaviour, and test results have not yet been recorded in this test record.

Follow-up: Identify where timeouts are enforced and determine how termination, cancellation, cleanup, and downstream behaviour can be verified.

8. Residual Risks

A timeout may stop a client from waiting without stopping the underlying operation. Cleanup may fail, downstream tasks may continue, and automatic retries may duplicate work or increase resource consumption. Distributed workflows and external services may require independent cancellation, idempotency, and resource controls.

Assess complementary controls such as request rate limits, usage budgets, input/output limits, agent loop protection, resource monitoring, and downstream action limits.

Conclusion: This record establishes a testing baseline only. It does not demonstrate that timeouts are implemented, that cancellation succeeds, or that all underlying resource consumption stops at the timeout boundary.

AG-C058 — Agent Loop Protection

Test Record ID: AG-C058-TEST-001

Control reference: AG-C058 — Agent Loop Protection

Evidence classification: [H] Proposed control; implementation and effectiveness not yet established by this record.

1. Implementation Status

Status: Unknown — pending evidence review.

Implementation evidence: Not yet recorded.

Maximum iteration count: Not established.

Retry limit and termination rules: Not established.

Enforcement point: Not established.

Coverage of recursive, parallel, and delegated workflows: Not established.

2. Test Status

Status: Planned — test not yet evidenced as executed.

Test objective: Determine whether agent workflows stop or recover according to defined limits when they repeat actions, retry failures, recurse, or fail to make progress.

Required test cases:

- A normal workflow that completes successfully.
- A controlled repeated-action scenario.
- Repeated transient failures that trigger retries.
- A workflow that reaches its maximum iteration count.
- A recursive or delegated workflow, where applicable.
- Parallel workflows or concurrent retries, where applicable.
- Verification that termination does not leave unintended downstream actions running.

Use an authorised test environment with bounded operations. Avoid production disruption, unnecessary charges, and tests against third-party systems without permission.

3. Expected Behaviour

Normal workflows complete within their permitted limits. Repeated actions, retries, and iterations remain within documented bounds.

When a configured limit or termination condition is reached, the workflow stops or follows its documented recovery process. Relevant events, limit values, and termination reasons are recorded.

Where supported, verify whether cancellation also reaches delegated or downstream operations rather than merely stopping the main workflow.

4. Acceptance Criteria

Before testing, document:

- Maximum permitted iterations and retries.
- The scope of each limit.
- How repeated actions and recursive calls are handled.
- How limits apply across concurrent and delegated workflows.
- Expected behaviour when a limit is reached.
- Required cancellation, recovery, and logging behaviour.
- Known architecture or provider limitations.

A test passes only when observed behaviour meets predefined acceptance criteria within the tested scope.

5. Execution Results

Execution date and time: Not recorded.

Test environment: Not established.

Configured iteration and retry limits: Not recorded.

Observed iteration and retry counts: Not recorded.

Termination and recovery behaviour: Not recorded.

Delegated or downstream task results: Not recorded.

Test outcome: Not tested.

6. Evidence References

No implementation or execution evidence has yet been attached to this record.

When available, retain verified references to:

- Configuration or code establishing iteration and retry limits.
- Test cases and execution timestamps.
- Workflow identifiers and observed iteration counts.
- Retry, termination, cancellation, and recovery logs.
- Delegated and downstream task outcomes.
- Resource-usage observations, where available.
- Errors, bypasses, unexpected continuation, or duplicate actions.

Use actual evidence identifiers and verified paths or URLs. Redact credentials, tokens, personal data, and other sensitive information.

7. Findings

Current finding: [GAP] Implementation, configured limits, enforcement scope, and test results have not yet been recorded in this test record.

Follow-up: Identify where iteration and retry limits are enforced, then determine how termination and downstream behaviour can be verified.

8. Residual Risks

A per-workflow iteration limit may not control aggregate consumption across parallel or delegated workflows. Retries may duplicate actions, and a stopped parent workflow may leave underlying tasks running. Limits alone may not prevent all resource exhaustion.

Assess complementary controls, including request rate limits, usage budgets, execution timeouts, resource monitoring, and downstream action limits.

Conclusion: This record establishes a testing baseline only. It does not demonstrate that loop protection is implemented, that workflows terminate correctly, or that resource consumption is fully controlled.

AG-C059 — Resource Monitoring

Test Record ID: AG-C059-TEST-001

Control reference: AG-C059 — Resource Monitoring

Evidence classification: [H] Proposed control; implementation and effectiveness not yet established by this record.

1. Implementation Status

Status: Unknown — pending evidence review.

Implementation evidence: Not yet recorded.

Monitored resources and metrics: Not established.

Alert thresholds and escalation rules: Not established.

Monitoring coverage and collection frequency: Not established.

Alert ownership and response procedure: Not established.

2. Test Status

Status: Planned — test not yet evidenced as executed.

Test objective: Determine whether relevant resource usage is observable, whether defined thresholds trigger the expected alerts, and whether monitoring gaps or abnormal consumption can be identified.

Required test cases:

- Confirm that expected resource metrics are collected.
- Check that normal activity is represented accurately.
- In an authorised test environment, generate bounded resource usage below a documented alert threshold.
- Test a controlled threshold crossing and verify the expected alert.
- Verify alert delivery and the documented response procedure.
- Check for missing, delayed, duplicated, or misleading monitoring events.
- Examine whether relevant usage across concurrent workflows is represented, where applicable.
- Check monitoring behaviour during collection failures or temporary monitoring outages.

Use controlled test conditions. Avoid production disruption, unnecessary charges, and tests against third-party systems without permission.

3. Expected Behaviour

The documented monitoring system collects the selected metrics at the specified frequency and scope. When a predefined threshold or anomaly rule is triggered, the expected alert or recorded event is generated and routed according to the documented procedure.

Monitoring gaps, collection failures, and alert-delivery failures should be identifiable where the system supports such detection. Evidence should distinguish a metric being collected from an alert being delivered and an operator taking action.

4. Acceptance Criteria

Before testing, document:

- The resources and metrics being monitored.
- The systems, workflows, and environments covered.
- Collection frequency and known reporting delays.
- Alert thresholds and decision rules.
- Expected alert destination and response procedure.
- How monitoring and alert-delivery failures are detected.
- Evidence-retention and access-control requirements.
- Known provider, infrastructure, and telemetry limitations.

A test passes only when observed results meet predefined acceptance criteria within the tested scope.

5. Execution Results

Execution date and time: Not recorded.

Test environment: Not established.

Metrics and thresholds tested: Not recorded.

Observed resource measurements: Not recorded.

Alert generation and delivery results: Not recorded.

Monitoring gaps or collection failures observed: Not recorded.

Test outcome: Not tested.

6. Evidence References

No implementation or execution evidence has yet been attached to this record.

When available, retain verified references to:

- Monitoring configuration and metric definitions.
- Alert thresholds and routing rules.
- Timestamped resource measurements.
- Test-case descriptions and execution timestamps.
- Alert-generation and delivery records.
- Relevant workflow or request identifiers.
- Monitoring outage, missing-data, and recovery records.
- Findings, deviations, and corrective actions.

Use actual evidence identifiers and verified paths or URLs. Redact credentials, tokens, personal data, and other sensitive information.

7. Findings

Current finding: [GAP] Monitoring coverage, metric definitions, thresholds, alert delivery, and test results have not yet been established by this record.

Follow-up: Identify the available monitoring mechanisms and define measurable criteria for detecting excessive resource consumption and verifying alert delivery.

8. Residual Risks

Monitoring does not itself prevent excessive resource consumption. Alerts may be delayed, incomplete, misconfigured, or ignored. Metrics may omit costs or activity occurring in external providers, parallel workflows, delegated agents, or downstream services.

Assess complementary controls, including request rate limits, usage and cost budgets, input/output limits, execution timeouts, agent loop protection, and downstream action limits.

Conclusion: This record establishes a testing baseline only. It does not demonstrate that monitoring is implemented, that alerts work, or that resource exhaustion will be prevented.

AG-C060 — Downstream Action Limits

Test Record ID: AG-C060-TEST-001

Control reference: AG-C060 — Downstream Action Limits

Evidence classification: [H] Proposed control; implementation and effectiveness not yet established by this record.

1. Implementation Status

Status: Unknown — pending evidence review.

Implementation evidence: Not yet recorded.

Maximum permitted actions: Not established.

Queue capacity and action-rate limits: Not established.

Enforcement point: Not established.

Coverage of parallel, retried, and delegated actions: Not established.

Approval requirements for sensitive or irreversible actions: Not established.

2. Test Status

Status: Planned — test not yet evidenced as executed.

Test objective: Determine whether limits on queued and executed actions are enforced across the defined workflow scope, including retries, parallel execution, and delegated tasks where applicable.

Required test cases:

- A workflow that executes fewer actions than the configured limit.
- A workflow that reaches the configured action limit.
- An attempt to exceed the action limit.
- Queue-capacity and queue-overflow behaviour.
- Parallel workflows attempting actions concurrently.
- Retry scenarios that could create duplicate actions.
- Delegated or nested workflows, where applicable.
- Verification that blocked actions do not execute downstream.
- Sensitive or irreversible actions that require independent human approval, where applicable.

Use an authorised test environment with harmless, reversible test actions. Do not use real payments, modify production systems, or trigger third-party actions without permission.

3. Expected Behaviour

Actions within the documented limits follow the permitted workflow. Attempts to exceed a limit are blocked, rejected, paused, or handled through a documented recovery procedure.

Queue limits and action limits should behave consistently under concurrent requests and retries within the tested scope. Where duplicate execution is possible, verify the documented safeguards and record any limitations.

Sensitive or irreversible actions must follow their required approval process. Reaching an action limit must not silently bypass approval or trigger an alternative unbounded execution path.

Relevant decisions, blocked actions, queue events, approvals, and execution outcomes should be recorded where supported.

4. Acceptance Criteria

Before testing, document:

- The action types covered by the control.
- Maximum action count and queue capacity.
- Whether limits apply per request, workflow, user, agent, tenant, or across the system.
- How limits behave during parallel execution, retries, and delegation.
- Expected queue-overflow and limit-exceeded behaviour.
- Duplicate-action prevention or idempotency requirements, where applicable.
- Human approval requirements for sensitive or irreversible actions.
- Required audit records and known architecture limitations.

A test passes only when observed behaviour meets predefined acceptance criteria within the tested scope.

5. Execution Results

Execution date and time: Not recorded.

Test environment: Not established.

Configured action and queue limits: Not recorded.

Observed action counts: Not recorded.

Queue-limit behaviour: Not recorded.

Concurrent, retry, and delegated-workflow results: Not recorded.

Approval enforcement results: Not recorded.

Test outcome: Not tested.

6. Evidence References

No implementation or execution evidence has yet been attached to this record.

When available, retain verified references to:

- Action-limit and queue configuration.
- Relevant code or enforcement rules.
- Test-case descriptions and execution timestamps.
- Workflow and action identifiers.
- Queue, rejection, approval, and execution logs.
- Records of retries, concurrent operations, and delegated actions.
- Evidence of blocked actions and duplicate-action checks.
- Errors, bypasses, deviations, and corrective actions.

Use actual evidence identifiers and verified paths or URLs. Redact credentials, tokens, personal data, and other sensitive information.

7. Findings

Current finding: [GAP] Implementation, configured limits, enforcement scope, approval behaviour, and test results have not yet been recorded in this test record.

Follow-up: Identify where downstream actions are authorised and executed. Define measurable limits and establish how blocked actions, queue behaviour, concurrency, retries, and approval enforcement can be verified.

8. Residual Risks

Limits enforced at only one layer may be bypassed by other execution paths. Parallel workflows can create aggregate activity beyond a per-workflow limit. Retries may duplicate actions, and a parent workflow may stop while downstream operations continue.

Action-count limits alone do not guarantee that each permitted action is safe or authorised. Independent approval, least-privilege access, idempotency safeguards, monitoring, and resource budgets may still be necessary.

Conclusion: This record establishes a testing baseline only. It does not demonstrate that downstream action limits are implemented, that prohibited actions are blocked, or that sensitive actions always require the correct approval.