# Open Loops ledger format

Use this format when initializing or repairing `OPEN_LOOPS.md`. Preserve useful extra fields in an existing ledger rather than forcing a rewrite.

## Active entry

```markdown
### OL-001 — Decide the authentication scope

- **Status:** blocking
- **Kind:** decision
- **Owner:** user
- **Raised:** 2026-09-30
- **Why it matters:** Determines the authorization and data model.
- **Context:** The first release may support either individual or organization accounts.
- **Provisional assumption:** Individual accounts only.
- **Source:** Planning conversation, 2026-09-30.
```

`Owner`, `Context`, `Provisional assumption`, and `Source` are optional. Keep enough context that someone can understand the item without replaying the conversation.

## Closed entry

Retain the active fields and add:

```markdown
- **Resolved:** 2026-10-02
- **Resolution:** The first release supports individual accounts; organizations are deferred.
- **Evidence:** Accepted implementation plan in `docs/auth-plan.md`.
```

Use `obsolete` rather than `resolved` when changed scope or circumstances made the question irrelevant. Explain why in `Resolution`.

## Lifecycle

- `open`: consequential and awaiting information or a decision.
- `blocking`: prevents meaningful progress on identified work.
- `deferred`: intentionally postponed; include a review trigger or date when known.
- `resolved`: explicitly answered or settled by accepted work.
- `obsolete`: no longer relevant because the surrounding work changed.

Never recycle or renumber an ID. Use local dates in `YYYY-MM-DD` form. Update the document's `Last reconciled` date only after a meaningful reconciliation.

## Reconciliation checks

Before adding a candidate, ask:

1. Does an existing entry ask the same underlying question?
2. Was it answered later in the conversation or by an accepted artifact?
3. Is it actually a task with a known next step rather than an open loop?
4. Would losing it plausibly cause rework, delay, or a poor decision?
5. If it came from an option being deferred inside a resolved decision, is there an explicit request or concrete trigger to track reconsideration separately? If not, preserve it only in the resolution.
