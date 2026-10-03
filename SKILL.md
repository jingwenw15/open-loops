---
name: open-loops
description: Maintain a durable Markdown ledger of consequential unresolved questions, pending decisions, blockers, and provisional assumptions from a conversation or project. Use when the user asks to capture, review, reconcile, close, or preserve open questions or loose ends. Do not use merely because an ordinary request contains questions.
---

# Open Loops

Keep unresolved work visible without turning the ledger into a transcript or generic task list.

## Choose the ledger

Use, in order:

1. A path explicitly named by the user.
2. An existing `OPEN_LOOPS.md` in the current workspace.
3. `.worktrail/OPEN_LOOPS.md` at the workspace root.

Before changing a ledger, read it and reconcile against its existing entries. If none exists, create one using [assets/OPEN_LOOPS.md](assets/OPEN_LOOPS.md). Do not create or update a ledger unless the user asks to capture or maintain open loops, or explicitly invokes this skill.

## Decide what belongs

Record an item only when its answer or resolution could change future work. Useful kinds are `decision`, `missing-information`, `blocker`, `risk`, and `follow-up`.

Exclude:

- questions already answered in the available conversation;
- rhetorical or conversational questions;
- ordinary tasks that have a clear next action;
- speculative curiosities with no likely consequence;
- secrets or transcript excerpts not needed to resume the work.

When the distinction is uncertain, prefer fewer, higher-value entries.

## Reconcile rather than append

- Match candidates to existing entries by meaning, not wording.
- Preserve stable IDs in the form `OL-001`; allocate the next unused number for a new entry.
- Update an existing entry when context, ownership, blocking state, or a provisional assumption changes.
- Use `open`, `blocking`, or `deferred` for active entries and `resolved` or `obsolete` for closed entries.
- Move closed entries under `Closed`; retain their resolution and resolution date.
- When a resolved decision says an unchosen option is deferred, keep that fact in the resolution. Do not automatically open a second entry for the deferred option. Create a separate follow-up only when the user explicitly asks to track reconsideration or provides a concrete owner, review date, or review trigger for it.
- Do not mark an item resolved from silence or a weak inference. An explicit user statement, accepted implementation, or cited artifact may resolve it.
- If work must proceed without an answer, record the assumption separately from the question and leave the loop active unless the assumption itself settles the decision.

For the complete entry shape and lifecycle rules, read [references/ledger-format.md](references/ledger-format.md) when creating, repairing, or substantially reorganizing a ledger.

## Report the result

After editing, state the ledger path and briefly report what was opened, changed, or closed. Surface blocking items first. If nothing consequential changed, say so and avoid a no-op rewrite.
