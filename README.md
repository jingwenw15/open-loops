# Open Loops

Durable memory for the questions and decisions agents should not drop.

Open Loops is a Codex skill that turns consequential unresolved conversation threads into a compact Markdown ledger. It filters out casual questions, completed tasks, and already-settled decisions; reconciles later answers without duplicating entries; and keeps provisional assumptions visible.

## What it tracks

- Pending decisions and missing information
- Blocking questions and material risks
- Provisional assumptions used to keep work moving
- Resolutions, dates, and supporting evidence

By default, the ledger lives at `.worktrail/OPEN_LOOPS.md` in the current workspace.

## Install

Clone the repository into your personal Codex skills directory:

```sh
git clone https://github.com/jingwenw15/open-loops.git ~/.codex/skills/open-loops
```

Then invoke it explicitly or ask naturally:

```text
Use $open-loops to capture the unresolved decisions from this conversation.
Reconcile our open loops now that we chose PostgreSQL.
```

## Quality

The skill passed all four isolated behavioral scenarios covering mixed-signal filtering, resolution without duplication, provisional assumptions, and no-op behavior. See [evals/REPORT.md](evals/REPORT.md).

Run the dependency-free ledger contract tests with:

```sh
python3 -m unittest discover -s tests -v
```
