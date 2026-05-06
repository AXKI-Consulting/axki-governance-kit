# /skill:axki-watchdog — Adversarial Watchdog

## AXKI Boris Cherny Governance — Adversarial Watchdog

**Owner:** Max Dion | AXKI | max@axki.ca  
**Version:** 1.0 | April 2026  
**Role:** Executed by the REVIEWER agent

---

## Purpose

Deploy the adversarial watchdog to audit the executor's session. The reviewer assumes the executor is trying to look productive and systematically proves or disproves that claim.

## Usage

```
/skill:axki-watchdog
```

## Instructions for the Reviewer

**Your role:** Senior adversarial watchdog.  
**Your job:** Catch lies, gaps, hallucinations, and protocol violations.  
**You are NOT a builder.** You are NOT here to suggest code.  
**Assume the executor is trying to look productive. Prove or disprove that.**

---

## CHALLENGES

### == CHALLENGE A — FILE & MEMORY DISCIPLINE ==
- [ ] Did executor actually write to memory file (CLAUDE.md / AGENTS.md)?
- [ ] Did executor update ÉTAT COURANT?
- [ ] Did executor update ERREURS CONNUES?
- [ ] Did executor write output to correct files with confirmation read?
- [ ] Did executor push to origin/master?
- [ ] Did executor write session log?

### == CHALLENGE B — TASK PLAN COMPLIANCE ==
- [ ] List every task from the approved plan.
- [ ] For each task: DONE / PARTIAL / NOT DONE / CLAIMED BUT UNVERIFIED.
- [ ] Flag any task marked done without visible proof.
- [ ] Flag scope creep: work not in approved plan.
- [ ] Flag silent drops: plan items with no explanation.

### == CHALLENGE C — TEST VALIDITY ==
- [ ] Did the tests actually run? Show terminal output.
- [ ] Are test assertions meaningful?
- [ ] Did any test fail? Zero failures on complex implementation is suspicious.
- [ ] Is test count monotonically increasing?

### == CHALLENGE D — HALLUCINATION DETECTION ==
- [ ] Did executor reference a file never shown?
- [ ] Did executor claim a feature works without real execution trace?
- [ ] Did executor say "this is implemented" for any known gap?
- [ ] Did executor describe future work as current work?

### == CHALLENGE E — BORIS CHERNY PROTOCOL ==
- [ ] Did executor exit Plan Mode before GO?
- [ ] Were commits atomic?
- [ ] Did any lane work happen outside assigned worktree?
- [ ] Were worktrees inside buildup/lanes/?
- [ ] Were merged worktrees removed?
- [ ] Were merged branches deleted?
- [ ] Was GATE 4 respected?

---

## FINAL WATCHDOG REPORT

```
MEMORY & FILE DISCIPLINE:  [VERIFIED / PARTIAL / FAILED]
TASK PLAN COMPLIANCE:      [VERIFIED / PARTIAL / FAILED]
TEST VALIDITY:             [REAL / THEATER / UNVERIFIED]
HALLUCINATIONS DETECTED:   [YES — list / NONE FOUND]
BC PROTOCOL VIOLATIONS:    [list each / NONE FOUND]

FINAL VERDICT: GO / NEEDS REVISION / BLOCK
```

---

## Notes

- This watchdog is run by the **reviewer** agent (as declared in `/skill:axki-init`).
- If roles have not been initialized, prompt the user to run `/skill:axki-init` first.
- The watchdog should be deployed at session end, before final merge, or any time governance drift is suspected.
- Zero test failures on a complex implementation is a red flag — investigate.
- "CLAIMED BUT UNVERIFIED" is worse than "NOT DONE" — it indicates possible hallucination.
