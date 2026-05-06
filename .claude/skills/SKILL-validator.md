# /skill:axki-validate — Boris Cherny Plan Validator

## AXKI Boris Cherny Governance — Plan Validator

**Owner:** Max Dion | AXKI | max@axki.ca  
**Version:** 1.0 | April 2026  
**Role:** Executed by the REVIEWER agent

---

## Purpose

Validate a proposed plan against the full Boris Cherny protocol before the executor begins implementation. The **reviewer** reads the plan and scores each governance criterion.

## Usage

```
/skill:axki-validate
```

## Instructions for the Reviewer

Read the plan below and score each item:
 ✓ PASS | ✗ FAIL | △ PARTIAL

Flag every FAIL and PARTIAL.
Final verdict: GO / NEEDS REVISION / BLOCK

---

## VALIDATION CRITERIA

### ── LOOP & PHASE ──
- [ ] Current phase clearly identified?
- [ ] Order respected? No Implement without approved Plan.
- [ ] Plan Mode active? No file writes before GO.
- [ ] One clear GO gate before the next phase?

### ── LANES & WORKTREES ──
- [ ] Real Git worktrees — explicit git worktree add commands?
- [ ] All worktrees inside buildup/lanes/?
- [ ] Each lane named and assigned before Implement?
- [ ] Each lane scoped to one concern?
- [ ] Worktrees created one at a time?
- [ ] Removal after each merge planned?

### ── HITL GATES ──
- [ ] GATE 1 present? (Explore complete → wait for GO)
- [ ] GATE 2 present? (Plan approved → wait for GO)
- [ ] GATE 3 defined? (Implement done → GO before Commit)
- [ ] GATE 4 respected? (No push to prod without GO Prod)

### ── STOP-HOOKS / DONE CRITERIA ──
- [ ] Done-when defined before Implement starts?
- [ ] Stop-hook command specified per task?
- [ ] Will agent loop until all green?
- [ ] Failure protocol: fix → new commit → rerun?
- [ ] Monotonic test count enforced?

### ── COMMITS ──
- [ ] Atomic? One concern per commit?
- [ ] No bundled commits planned?
- [ ] No half-migrations left open?

### ── ADVERSARIAL REVIEW ──
- [ ] Reviewer agent defined in workflow?
- [ ] Review before each lane merge?
- [ ] Final verification after session planned?

### ── MEMORY ──
- [ ] Memory file (CLAUDE.md / AGENTS.md) update planned at session end?
- [ ] ERREURS CONNUES update planned?
- [ ] Session log to /logs/ planned?
- [ ] git push origin master in governance?
- [ ] Merged branches deletion planned?

### ── ANTI-PATTERNS CHECK ──
- [ ] No monolithic scripts?
- [ ] No skipped Plan Mode?
- [ ] No prod push without GO Prod?
- [ ] No LLM output assumed correct?
- [ ] No over-engineering beyond current scope?
- [ ] No phantom file references?

### ── SECURITY (if OAuth or external API) ──
- [ ] State validation planned (Redis TTL)?
- [ ] Public paths exempted for callbacks?
- [ ] CSRF exemption for webhooks/callbacks?
- [ ] New users assigned to correct tenant only?
- [ ] JWT parity with existing auth flow?

---

## FINAL SCORING

```
Fails found: ___
Partials found: ___

VERDICT: GO / NEEDS REVISION / BLOCK
```

---

## Notes

- This validator is run by the **reviewer** agent (as declared in `/skill:axki-init`).
- If roles have not been initialized, prompt the user to run `/skill:axki-init` first.
- The security section applies only when the plan involves OAuth, external APIs, or authentication flows. Skip if not applicable.
- A plan receiving NEEDS REVISION must be corrected and re-validated before proceeding.
