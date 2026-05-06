# /skill:axki-init — Session Role Initialization

## AXKI Boris Cherny Governance — Role Assignment

**Owner:** Max Dion | AXKI | max@axki.ca  
**Version:** 1.0 | April 2026

---

## Purpose

Initialize the governance session by declaring which AI agent is the **executor** (builder) and which is the **reviewer** (validator). This role assignment persists for the entire session.

## Usage

```
/skill:axki-init executor=<agent> reviewer=<agent>
```

### Examples

```
/skill:axki-init executor=codex reviewer=claude
/skill:axki-init executor=claude reviewer=codex
```

## Behavior

When invoked, set the following session context:

1. **EXECUTOR** — The agent responsible for:
   - Writing code and files
   - Creating commits
   - Running tests
   - Managing worktrees and lanes
   - Updating memory files (CLAUDE.md / AGENTS.md)

2. **REVIEWER** — The agent responsible for:
   - Validating plans before implementation
   - Running the adversarial watchdog
   - Scoring checklist items
   - Issuing GO / NEEDS REVISION / BLOCK verdicts
   - Catching hallucinations and protocol violations

## Session Output

After initialization, confirm with:

```
═══ AXKI GOVERNANCE SESSION INITIALIZED ═══

EXECUTOR (builder):  [agent name]
REVIEWER (validator): [agent name]

Framework: Boris Cherny (Explore → Plan → Implement → Commit)
Protocol:  HITL gates active — no phase transition without GO

Available commands:
  /skill:axki-checklist  — Quick governance checklist
  /skill:axki-validate   — Plan validator (reviewer scores)
  /skill:axki-watchdog   — Adversarial watchdog audit

═══════════════════════════════════════════
```

## Notes

- The role assignment is **session-scoped** — it resets when the session ends.
- If no init is called, commands will prompt for role declaration before executing.
- This architecture is **role-agnostic** — any AI agent can fill either role regardless of model version or provider.
