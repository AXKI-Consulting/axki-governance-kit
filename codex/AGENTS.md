# AGENTS.md - AXKI Boris Cherny Governance Plugin

## Owner
Max Dion | CEO, AXKI | max@axki.ca | https://axki.ca

## Framework
Boris Cherny AI Coding Governance (Explore -> Plan -> Implement -> Commit)

## Architecture: Role-Agnostic

This plugin uses a **role-agnostic** architecture. At session start, the user declares:
- **EXECUTOR** (builder) — the agent that writes code, creates commits, runs tests
- **REVIEWER** (validator) — the agent that audits, scores, and issues verdicts

Roles are declared via `/codex:axki-init` and persist for the session.

Claude Code uses skills. Codex uses commands. The governance concepts are the same, but the invocation syntax is intentionally different to avoid copy-paste confusion.

Project-specific AGENTS.md / CLAUDE.md instructions override this generic framework.

---

## Available Commands

| Command | File | Purpose |
|---------|------|---------|
| `/codex:axki-init` | `commands/codex-init.md` | Initialize executor/reviewer roles |
| `/codex:axki-checklist` | `commands/codex-checklist.md` | Quick governance checklist |
| `/codex:axki-validate` | `commands/codex-validator.md` | Plan validator |
| `/codex:axki-watchdog` | `commands/codex-watchdog.md` | Adversarial watchdog audit |

---

## Related Claude Code Skills

Use these only in Claude Code:

```text
/skill:axki-init
/skill:axki-checklist
/skill:axki-validate
/skill:axki-watchdog
```

Use the Codex commands above only in Codex CLI:

```text
/codex:axki-init
/codex:axki-checklist
/codex:axki-validate
/codex:axki-watchdog
```

---

## Core Principles

1. **Phases are sequential** — Explore → Plan → Implement → Commit. No skipping.
2. **HITL gates** — Human-in-the-loop GO required between every phase.
3. **Atomic commits** — One concern per commit. No bundling.
4. **Real worktrees when lanes are used** - if the project uses lane worktrees, create real git worktrees in the project-approved lanes directory; otherwise follow the project's AGENTS.md/CLAUDE.md workflow.
5. **Stop-hooks** — Loop until all tests green. No premature success claims.
6. **Memory discipline** — Update AGENTS.md / CLAUDE.md every session.
7. **Adversarial review** — Reviewer audits executor before merge.

---

## Session Protocol

```
1. /codex:axki-init executor=<agent> reviewer=<agent>
2. Explore phase -> GATE 1 -> GO
3. /codex:axki-validate (reviewer scores the plan)
4. Plan phase -> GATE 2 -> GO
5. Implement phase -> GATE 3 -> GO
6. /codex:axki-checklist (reviewer audits before commit)
7. Commit phase -> GATE 4 -> GO Prod
8. /codex:axki-watchdog (final adversarial audit)
```

---

## Anti-Patterns (Always Reject)

- Monolithic scripts
- Phantom file references
- "I wrote X" without proof of write
- Tests that test air (mock always true)
- LLM output assumed correct without verification
- Over-engineering beyond current scope
- Skipping Plan Mode
- Prod push without GO Prod
