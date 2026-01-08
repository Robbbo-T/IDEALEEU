# Low-Level Design: Command Router
ID: DES-0123-command-router
Baseline: draft
Author: ...
Reviewer (Independent): ...
Linked Requirements: REQ-0100, REQ-0112
Planned Tests: TST-0100, TST-0101, TST-0102

## 1. Purpose
Routes validated command requests to appropriate handler modules ensuring isolation, authorization, and deterministic execution order.

## 2. Inputs & Preconditions
- Validated `CommandRequest` object (schema hash: <hash>)
- Caller context with auth claims
- System state snapshot (readonly)

## 3. Outputs & Postconditions
- Handler response object or standardized error
- Emitted audit event (INT-0005-audit-stream)

## 4. Data Structures
```ts
export interface CommandRequest {
  id: string; // UUID
  type: CommandType; // enum
  payload: Record<string, unknown>;
  receivedAt: string; // ISO timestamp
}
```
Constraints: `payload` validated by schema; size <= 4 KiB.

## 5. Control Flow (Pseudo)
1. Lookup handler map by `type`.
2. Check authorization policy (DES-0450-policy-evaluator).
3. Acquire deterministic execution slot (monotonic sequence).
4. Invoke pure handler logic (no I/O inside).
5. Package response; emit audit event.
6. Return success/failure.

## 6. State & Side Effects
- No persistent state mutation.
- Side effects isolated in step 5 (audit emission via messaging adapter).

## 7. Error Handling
| Condition | Error Type | Propagation | Logged? |
|-----------|-----------|-------------|---------|
| Unknown Command Type | ValidationError | Return 4xx | Yes (redacted) |
| Unauthorized | AuthorizationError | Return 403 | Yes |
| Handler Fault | HandlerExecutionError | Return 5xx | Yes |

## 8. Concurrency & Determinism
Single-thread logical path enforced by sequence allocator (DES-0300-sequence-manager). No shared mutable state.

## 9. Performance Budget
Max latency: 2.5 ms worst-case (REQ-0500).
Handler invocation must remain O(1) on lookup; map keyed by enum.

## 10. Safety Considerations
Ensures only authorized commands reach critical functions preventing hazard HAZ-2001 (unsafe actuation).

## 11. Trace Links
REQ-0100 (Routing correctness), REQ-0112 (Authorization enforcement).
Tests: TST-0100 (correct dispatch), TST-0101 (unauthorized rejection), TST-0102 (latency budget).

## 12. Verification Notes
- Unit tests use injected handler registry (dependency injection).
- MC/DC focus: branching on type, authorization, fault path.
- Structural coverage expectation 100%; no defensive unreachable branches planned.

## 13. Open Items
| Item | Description | Needed By |
|------|-------------|-----------|
| PERF-01 | Instrument latency measurement harness | Before integration tests |
| COVER-01 | MC/DC condition mapping doc | Before coverage campaign |

## 14. Approval
Signatures recorded in `qa/design_review_log.md`.
