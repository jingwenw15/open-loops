# Behavioral evaluation

Run date: 2026-10-03

Four isolated Codex executions completed without timeouts and passed every critical criterion and ledger contract.

| Scenario | Result |
|---|---|
| Mixed-signal filtering | Pass |
| Resolution without duplication | Pass after a regression fix |
| Provisional assumption handling | Pass |
| No-op behavior | Pass |

The regression fix prevents an unchosen option inside a resolved decision from becoming a new deferred entry unless the user requests reconsideration or provides a concrete owner, date, or trigger.
