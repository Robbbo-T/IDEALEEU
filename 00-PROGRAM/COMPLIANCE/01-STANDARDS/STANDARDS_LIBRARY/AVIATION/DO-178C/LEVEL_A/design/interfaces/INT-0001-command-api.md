# Interface Specification: Command API
ID: INT-0001-command-api
Version: 1.0.0
Schema Source: `/00-PROGRAM/platform/schemas/command_request.json` (hash: <hash>)
Linked Requirements: REQ-0100, REQ-0112
Design Elements: DES-0123-command-router, DES-0450-policy-evaluator
Tests: TST-0100, TST-0115 (contract), TST-0116 (auth)

## 1. Purpose
Accepts inbound commands from authorized clients for execution in critical domain.

## 2. Endpoint Surface
| Method | Path | Description | Auth | Rate Limit |
|--------|------|-------------|------|-----------|
| POST | /v1/command | Submit command request | OIDC + RBAC | 50/min per client |

## 3. Request Schema (Excerpt)
```json
{
  "id": "uuid",
  "type": "string",
  "payload": {},
  "receivedAt": "ISO-8601"
}
```
Full schema in source directory (generated types under `generated/types/command_request.ts`).

Validation:
- `type` must be member of enum (command_type.schema.json).
- Payload size constraint: <= 4096 bytes serialized.

## 4. Response Patterns
| Status | Body Schema | Condition |
|--------|-------------|-----------|
| 200 | command_response.json | Success |
| 400 | error.json | Validation failure |
| 403 | error.json | Authorization failure |
| 500 | error.json | Internal error |

## 5. Error Model
Typed error codes: `CMD_UNKNOWN`, `CMD_UNAUTHORIZED`, `CMD_PAYLOAD_INVALID`, `CMD_HANDLER_FAILURE`.

## 6. Security Controls
- Input validation at boundary (reject early).
- Authorization check (policy engine) before routing.
- Audit event emission with correlation ID (no PII).

## 7. Versioning & Compatibility
Backward-compatible additions only (new optional fields). Removal requires major version bump and PSAC update.

## 8. Performance & Reliability
Timeout: 100 ms (server). Retry guidance: client may retry idempotent commands with same `id`.

## 9. Logging & Tracing
Structured log fields: `command.id`, `command.type`, `tenant`, `correlationId`.
Redactions: payload content if marked sensitive by schema `x-sensitive: true`.

## 10. MC/DC Considerations
Branch points: validation success/fail, auth pass/fail, handler success/failure.
Test matrix enumerated in TST-0100..TST-0116.

## 11. Approval
Review recorded in `qa/interface_review_log.md`.
