# /codex:axki-checklist - Boris Cherny Quick Checklist

## AXKI Boris Cherny Governance - Quick Checklist

**Owner:** Max Dion | AXKI | max@axki.ca  
**Version:** 1.0 | April 2026  
**Role:** Executed by the REVIEWER agent

---

## Purpose

A rapid governance audit to run before any commit or phase transition. The **reviewer** scores each item against the executor's work.

Project-specific AGENTS.md / CLAUDE.md instructions override this generic framework.

## Usage

```
/codex:axki-checklist
```

## Instructions for the Reviewer

Score each item below. Use: PASS | FAIL | PARTIAL
Flag every FAIL and PARTIAL with a one-line explanation.  
Issue final verdict at the bottom.

---

## CHECKLIST

### PHASE & LOOP
- [ ] Phase identified? (Explore/Plan/Implement/Commit)
- [ ] Loop order respected? No skipping.
- [ ] Plan Mode active before any writes?
- [ ] Explicit GO received before this phase started?

### LANES & WORKTREES
- [ ] If the project uses lane worktrees, real Git worktrees were used - not folders?
- [ ] If the project uses lane worktrees, they were created in the project-approved lanes directory?
- [ ] Each lane has one concern only?
- [ ] No cross-lane contamination?
- [ ] Worktrees removed after each lane merges?

### GATES
- [ ] GATE 1 cleared? (Explore -> GO)
- [ ] GATE 2 cleared? (Plan -> GO)
- [ ] GATE 3 pending? (Implement -> GO before Commit)
- [ ] GATE 4 active? (No prod without GO Prod)

### DONE CRITERIA
- [ ] test_cmd defined?
- [ ] done_when defined per task?
- [ ] Stop-hook loops until all green?
- [ ] Failure protocol: fix -> new commit -> rerun?

### COMMITS
- [ ] Atomic? One concern per commit?
- [ ] No bundled commits?
- [ ] No half-open migrations?

### MEMORY & GOVERNANCE
- [ ] Memory file (CLAUDE.md / AGENTS.md) updated this session?
- [ ] Current state reflects actual state?
- [ ] Mistakes logged in known-errors memory if the project uses one?
- [ ] Session log written if the project requires one?
- [ ] Merged branches deleted?
- [ ] Approved target branch/current session branch pushed only when authorized?

### ANTI-PATTERNS
- [ ] No monolithic scripts?
- [ ] No phantom file references?
- [ ] No "I wrote X" without proof of write?
- [ ] No tests that test air (mock always true)?
- [ ] No LLM output assumed correct?
- [ ] No over-engineering beyond current scope?

---

## VERDICT

```
Fails found: ___
Partials found: ___

VERDICT: GO / NEEDS REVISION / BLOCK
```

---

## Notes

- This checklist is run by the **reviewer** agent (as declared in `/codex:axki-init`).
- If roles have not been initialized, prompt the user to run `/codex:axki-init` first.
- The executor should NOT self-score - that defeats the purpose of adversarial governance.
