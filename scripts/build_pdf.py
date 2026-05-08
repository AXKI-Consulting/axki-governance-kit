#!/usr/bin/env python3
"""Build the AXKI governance kit PDF.

Requires reportlab and pillow. In this workspace they can be installed with:
    python3 -m pip install --target /tmp/axki_pdf_tools reportlab pypdf
Then run:
    PYTHONPATH=/tmp/axki_pdf_tools python3 scripts/build_pdf.py
"""

from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    Image,
    KeepTogether,
    ListFlowable,
    ListItem,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "pdf" / "AXKI-AI-Coding-Governance-Kit.pdf"
LOGO = ROOT / "pdf" / "Logo" / "Main" / "axki no background-05.png"
FOOTER_LOGO = ROOT / "pdf" / "Logo" / "footer" / "axki no background-01.png"
SCREENSHOT = ROOT / "assets" / "adversarial-validation-screenshot.png"

PAGE_WIDTH, PAGE_HEIGHT = letter
MARGIN_X = 0.72 * inch
MARGIN_Y = 0.66 * inch

NAVY = colors.HexColor("#0F1658")
BLUE = colors.HexColor("#367FC8")
GOLD = colors.HexColor("#E4AF4C")
INK = colors.HexColor("#1F2430")
MUTED = colors.HexColor("#5E6575")
LIGHT = colors.HexColor("#F4F6FA")
LINE = colors.HexColor("#D9DEE9")
SKILL_PREFIX = "/skill:" + "axki-"
CODEX_PREFIX = "/codex:" + "axki-"


def skill(name):
    return f"{SKILL_PREFIX}{name}"


def codex(name):
    return f"{CODEX_PREFIX}{name}"


def styles():
    base = getSampleStyleSheet()
    base["Normal"].fontName = "Helvetica"
    base["Normal"].fontSize = 9.3
    base["Normal"].leading = 12.4
    base["Normal"].textColor = INK

    return {
        "title": ParagraphStyle(
            "Title",
            parent=base["Title"],
            fontName="Helvetica-Bold",
            fontSize=29,
            leading=34,
            textColor=NAVY,
            alignment=TA_CENTER,
            spaceAfter=12,
        ),
        "subtitle": ParagraphStyle(
            "Subtitle",
            parent=base["Normal"],
            fontSize=12,
            leading=16,
            textColor=MUTED,
            alignment=TA_CENTER,
            spaceAfter=16,
        ),
        "h1": ParagraphStyle(
            "H1",
            parent=base["Heading1"],
            fontName="Helvetica-Bold",
            fontSize=20,
            leading=25,
            textColor=NAVY,
            spaceBefore=4,
            spaceAfter=10,
        ),
        "h2": ParagraphStyle(
            "H2",
            parent=base["Heading2"],
            fontName="Helvetica-Bold",
            fontSize=13.5,
            leading=17,
            textColor=BLUE,
            spaceBefore=8,
            spaceAfter=5,
        ),
        "h3": ParagraphStyle(
            "H3",
            parent=base["Heading3"],
            fontName="Helvetica-Bold",
            fontSize=10.5,
            leading=13.5,
            textColor=NAVY,
            spaceBefore=7,
            spaceAfter=4,
        ),
        "body": base["Normal"],
        "small": ParagraphStyle(
            "Small",
            parent=base["Normal"],
            fontSize=8,
            leading=10.5,
            textColor=MUTED,
        ),
        "emphasis": ParagraphStyle(
            "Emphasis",
            parent=base["Normal"],
            fontName="Helvetica-Bold",
            fontSize=9.2,
            leading=12.2,
            textColor=NAVY,
            spaceBefore=5,
            spaceAfter=7,
        ),
        "mono": ParagraphStyle(
            "Mono",
            parent=base["Code"],
            fontName="Courier",
            fontSize=7.7,
            leading=10.2,
            textColor=INK,
            backColor=LIGHT,
            borderColor=LINE,
            borderWidth=0.5,
            borderPadding=6,
            spaceBefore=5,
            spaceAfter=7,
        ),
        "center": ParagraphStyle(
            "Center",
            parent=base["Normal"],
            alignment=TA_CENTER,
            fontSize=9,
            leading=12,
            textColor=MUTED,
        ),
    }


S = styles()


def p(text, style="body"):
    return Paragraph(text, S[style])


def bullets(items):
    return ListFlowable(
        [ListItem(p(item), leftIndent=0) for item in items],
        bulletType="bullet",
        leftIndent=14,
        bulletFontName="Helvetica",
        bulletFontSize=6,
        bulletColor=BLUE,
    )


def checklist(items):
    return ListFlowable(
        [ListItem(p(f"[ ] {item}"), leftIndent=0) for item in items],
        bulletType="bullet",
        leftIndent=10,
        bulletFontName="Helvetica",
        bulletFontSize=1,
        bulletColor=colors.white,
    )


def table(rows, widths):
    data = [[p(cell, "body") for cell in row] for row in rows]
    t = Table(data, colWidths=widths, hAlign="LEFT")
    t.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), NAVY),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("GRID", (0, 0), (-1, -1), 0.35, LINE),
                ("BACKGROUND", (0, 1), (-1, -1), colors.white),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, LIGHT]),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 6),
                ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                ("TOPPADDING", (0, 0), (-1, -1), 5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
            ]
        )
    )
    return t


def code(text):
    safe = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    return p(safe.replace("\n", "<br/>"), "mono")


def footer(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(LINE)
    canvas.line(MARGIN_X, 0.48 * inch, PAGE_WIDTH - MARGIN_X, 0.48 * inch)
    if FOOTER_LOGO.exists():
        canvas.drawImage(
            str(FOOTER_LOGO),
            MARGIN_X,
            0.18 * inch,
            width=0.28 * inch,
            height=0.28 * inch,
            mask="auto",
            preserveAspectRatio=True,
        )
    canvas.setFillColor(MUTED)
    canvas.setFont("Helvetica", 7.5)
    canvas.drawString(MARGIN_X + 0.36 * inch, 0.32 * inch, "AXKI - AI Coding Governance Kit")
    canvas.drawRightString(PAGE_WIDTH - MARGIN_X, 0.32 * inch, f"Page {doc.page}")
    canvas.restoreState()


def page_title(title):
    return [p(title, "h1")]


def build_story():
    story = []

    story.append(Spacer(1, 0.35 * inch))
    if LOGO.exists():
        logo = Image(str(LOGO), width=2.55 * inch, height=1.06 * inch)
        logo.hAlign = "CENTER"
        story += [logo, Spacer(1, 0.18 * inch)]
    story += [
        p("The AI Coding Governance Kit", "title"),
        p("Boris Cherny Framework for Claude Code Skills and Codex CLI Commands", "subtitle"),
        p("By Max Dion - CEO, AXKI", "center"),
        p("AI Automation Consultancy - Montreal, Canada", "center"),
        p("axki.ca | max@axki.ca", "center"),
        Spacer(1, 0.18 * inch),
        p("Version 1.0 - April 2026", "center"),
        Spacer(1, 0.38 * inch),
        p(
            "This kit ships separate Claude Code skills and Codex CLI commands. The governance concepts are the same, but the invocation syntax is intentionally different to avoid copy-paste confusion.",
            "emphasis",
        ),
        PageBreak(),
    ]

    story += page_title("Table of Contents")
    toc = [
        ["1", "Why AI Coding Governance Matters", "3"],
        ["2", "The Boris Cherny Framework", "4"],
        ["3", "Public Invocation Names", "5"],
        ["4", "Framework 1: Quick Checklist", "6"],
        ["5", "Framework 2: Plan Validator", "7"],
        ["6", "Framework 3: Adversarial Watchdog", "9"],
        ["7", "Role-Agnostic Architecture", "11"],
        ["8", "Installation Guide", "12"],
        ["9", "Real-World Validation", "13"],
        ["10", "Ready to Implement This?", "14"],
    ]
    story.append(table([["#", "Section", "Page"]] + toc, [0.45 * inch, 4.25 * inch, 0.6 * inch]))
    story += [
        Spacer(1, 0.2 * inch),
        p("This PDF matches the public Claude Code skill names and Codex command names shipped in the repository."),
        PageBreak(),
    ]

    story += page_title("1. Why AI Coding Governance Matters")
    story += [
        p("AI coding assistants are powerful, but without governance they become liability generators. Left unchecked, AI agents hallucinate file references, claim work is done when it is not, bundle unrelated changes into monolithic commits, skip testing, and push unverified code toward production."),
        p("The result is technical debt that compounds quickly: phantom features, tests that pass because they test nothing, and a codebase that looks productive on the surface but fails under scrutiny."),
        p("Boris Cherny's framework solves this by imposing a strict phase-gate protocol on AI coding sessions. Every phase requires explicit human approval before proceeding. Every commit must be atomic. Every claim must be verifiable. A dedicated adversarial reviewer catches what the builder misses."),
        p("Common AI Coding Failures", "h2"),
        table(
            [
                ["Failure mode", "Impact", "Governance response"],
                ["Hallucinated file references", "Broken builds and phantom features", "Watchdog hallucination checks"],
                ["Skipped planning phase", "Scope creep and wasted cycles", "HITL gates before implementation"],
                ["Bundled commits", "Impossible rollbacks", "Atomic commit rule"],
                ["Tests that test air", "False confidence", "Test validity review"],
                ["No memory updates", "Context loss between sessions", "Memory discipline checks"],
                ["Self-validated work", "Confirmation bias", "Separate reviewer role"],
            ],
            [1.7 * inch, 2.0 * inch, 1.9 * inch],
        ),
        PageBreak(),
    ]

    story += page_title("2. The Boris Cherny Framework")
    story += [
        p("The Boris Cherny framework enforces a strict sequential loop for AI-assisted development. Each phase has a clear entry gate, defined deliverables, and requires explicit human approval before the next phase can begin."),
        table(
            [
                ["Phase", "Purpose", "Gate", "Deliverable"],
                ["EXPLORE", "Understand the problem space", "GATE 1 -> GO", "Problem definition and constraints"],
                ["PLAN", "Design the solution", "GATE 2 -> GO", "Approved implementation plan"],
                ["IMPLEMENT", "Write code in scoped lanes", "GATE 3 -> GO", "Tested code with evidence"],
                ["COMMIT", "Atomic commits and authorized release", "GATE 4 -> GO Prod", "Clean history and approved push"],
            ],
            [1.05 * inch, 1.75 * inch, 1.25 * inch, 1.65 * inch],
        ),
        p("Core Principles", "h2"),
        bullets(
            [
                "Sequential phases: Explore -> Plan -> Implement -> Commit. Never skip.",
                "Human-in-the-loop gates: explicit GO required between phases.",
                "Atomic commits: one concern per commit. No bundled unrelated changes.",
                "Lane worktrees are conditional: if the project uses them, create real git worktrees in the project-approved lanes directory; otherwise follow the project's AGENTS.md/CLAUDE.md workflow.",
                "Stop-hooks: define test commands and loop until all green. No premature success claims.",
                "Memory discipline: update governance files such as CLAUDE.md or AGENTS.md when the project requires it.",
                "Adversarial review: a dedicated reviewer audits the executor before merge or release.",
            ]
        ),
        p("Project-specific AGENTS.md / CLAUDE.md instructions override this generic framework.", "emphasis"),
        PageBreak(),
    ]

    story += page_title("3. Public Invocation Names")
    story += [
        p("Keep Claude Code skills and Codex commands distinct. Do not rename them to generic slash commands."),
        table(
            [
                ["Claude Code Skills", "Codex Commands"],
                [skill("init"), codex("init")],
                [skill("checklist"), codex("checklist")],
                [skill("validate"), codex("validate")],
                [skill("watchdog"), codex("watchdog")],
            ],
            [2.75 * inch, 2.75 * inch],
        ),
        p("The document uses both columns throughout the framework so readers can copy the correct invocation for the tool they are using. Claude Code users copy the skill names. Codex CLI users copy the command names."),
        p("Session Role Initialization", "h2"),
        code(f"{skill('init')} executor=codex reviewer=claude\n{codex('init')} executor=codex reviewer=claude"),
        p("The executor writes code, creates commits, runs tests, and updates project memory. The reviewer validates plans, runs checklists, deploys the watchdog, and issues GO / NEEDS REVISION / BLOCK verdicts."),
        PageBreak(),
    ]

    story += page_title("4. Framework 1: Quick Checklist")
    story += [
        p(f"Claude Code skill: {skill('checklist')}", "h3"),
        p(f"Codex command: {codex('checklist')}", "h3"),
        p("A rapid governance audit to run before any commit or phase transition. The reviewer scores each item against the executor's work using PASS / FAIL / PARTIAL."),
        p("PHASE & LOOP", "h3"),
        checklist(["Phase identified? (Explore/Plan/Implement/Commit)", "Loop order respected? No skipping.", "Plan Mode active before any writes?", "Explicit GO received before this phase started?"]),
        p("LANES & WORKTREES", "h3"),
        checklist(["If the project uses lane worktrees, real Git worktrees were used - not folders?", "If the project uses lane worktrees, they were created in the project-approved lanes directory?", "Each lane has one concern only?", "No cross-lane contamination?", "Worktrees removed after each lane merges?"]),
        p("GATES", "h3"),
        checklist(["GATE 1 cleared? (Explore -> GO)", "GATE 2 cleared? (Plan -> GO)", "GATE 3 pending? (Implement -> GO before Commit)", "GATE 4 active? (No prod without GO Prod)"]),
        p("DONE CRITERIA", "h3"),
        checklist(["test_cmd defined?", "done_when defined per task?", "Stop-hook loops until all green?", "Failure protocol: fix -> new commit -> rerun?"]),
        p("COMMITS / MEMORY / ANTI-PATTERNS", "h3"),
        checklist(["Atomic? One concern per commit?", "Memory file (CLAUDE.md / AGENTS.md) updated this session?", "Approved target branch/current session branch pushed only when authorized?", "No phantom file references?", "No tests that test air?", "No LLM output assumed correct?", "No over-engineering beyond current scope?"]),
        code("Fails found: ___\nPartials found: ___\n\nVERDICT: GO / NEEDS REVISION / BLOCK"),
        PageBreak(),
    ]

    story += page_title("5. Framework 2: Plan Validator")
    story += [
        p(f"Claude Code skill: {skill('validate')}", "h3"),
        p(f"Codex command: {codex('validate')}", "h3"),
        p("Validate a proposed plan against the full Boris Cherny protocol before the executor begins implementation. Run this before any GATE 2 approval."),
        p("LOOP & PHASE", "h3"),
        checklist(["Current phase clearly identified?", "Order respected? No Implement without approved Plan.", "Plan Mode active? No file writes before GO.", "One clear GO gate before the next phase?"]),
        p("LANES & WORKTREES", "h3"),
        checklist(["If the project uses lane worktrees, real Git worktrees are planned with explicit git worktree add commands?", "If the project uses lane worktrees, create real git worktrees in the project-approved lanes directory; otherwise follow the project's AGENTS.md/CLAUDE.md workflow.", "Each lane named and assigned before Implement?", "Each lane scoped to one concern?", "Worktrees created one at a time?", "Removal after each merge planned?"]),
        p("HITL GATES", "h3"),
        checklist(["GATE 1 present? (Explore complete -> wait for GO)", "GATE 2 present? (Plan approved -> wait for GO)", "GATE 3 defined? (Implement done -> GO before Commit)", "GATE 4 respected? (No push to prod without GO Prod)"]),
        p("STOP-HOOKS / COMMITS / REVIEW", "h3"),
        checklist(["Done-when defined before Implement starts?", "Stop-hook command specified per task?", "Will agent loop until all green?", "Failure protocol: fix -> new commit -> rerun?", "Monotonic test count enforced?", "Atomic commits planned?", "Reviewer agent defined in workflow?", "Final verification after session planned?"]),
        PageBreak(),
        p("MEMORY", "h3"),
        checklist(["Memory file (CLAUDE.md / AGENTS.md) update planned at session end?", "Known-errors memory update planned if the project uses one?", "Session log planned if the project requires one?", "Push the approved target branch/current session branch only when authorized?", "Merged branches deletion planned?"]),
        p("ANTI-PATTERNS CHECK", "h3"),
        checklist(["No monolithic scripts?", "No skipped Plan Mode?", "No prod push without GO Prod?", "No LLM output assumed correct?", "No over-engineering beyond current scope?", "No phantom file references?"]),
        p("SECURITY (if OAuth or external API)", "h3"),
        checklist(["State validation planned?", "Public paths exempted for callbacks?", "CSRF exemption for webhooks/callbacks?", "New users assigned to correct tenant only?", "JWT parity with existing auth flow?"]),
        code("Fails found: ___\nPartials found: ___\n\nVERDICT: GO / NEEDS REVISION / BLOCK"),
        PageBreak(),
    ]

    story += page_title("6. Framework 3: Adversarial Watchdog")
    story += [
        p(f"Claude Code skill: {skill('watchdog')}", "h3"),
        p(f"Codex command: {codex('watchdog')}", "h3"),
        p("The most aggressive audit tool. The reviewer assumes the executor is trying to look productive and systematically proves or disproves that claim. This is not a code review; it is a lie-detection protocol for AI agents."),
        p("Reviewer mindset: Senior adversarial watchdog. Catch lies, gaps, hallucinations, and protocol violations. You are not a builder. Do not suggest code. Verify claims independently."),
        p("CHALLENGE A - FILE & MEMORY DISCIPLINE", "h3"),
        checklist(["Did executor actually write to memory file (CLAUDE.md / AGENTS.md)?", "Did executor update current-state memory if the project uses one?", "Did executor update known-errors memory if the project uses one?", "Did executor write output to correct files with confirmation read?", "Did executor push only the approved target branch/current session branch when authorized?", "Did executor write session log if the project requires one?"]),
        p("CHALLENGE B - TASK PLAN COMPLIANCE", "h3"),
        checklist(["List every task from the approved plan.", "For each task: DONE / PARTIAL / NOT DONE / CLAIMED BUT UNVERIFIED.", "Flag any task marked done without visible proof.", "Flag scope creep: work not in approved plan.", "Flag silent drops: plan items with no explanation."]),
        p("CHALLENGE C - TEST VALIDITY", "h3"),
        checklist(["Did the tests actually run? Show terminal output.", "Are test assertions meaningful?", "Did any test fail? Zero failures on complex implementation is suspicious.", "Is test count monotonically increasing?"]),
        PageBreak(),
        p("CHALLENGE D - HALLUCINATION DETECTION", "h3"),
        checklist(["Did executor reference a file never shown?", "Did executor claim a feature works without real execution trace?", "Did executor say this is implemented for any known gap?", "Did executor describe future work as current work?"]),
        p("CHALLENGE E - BORIS CHERNY PROTOCOL", "h3"),
        checklist(["Did executor exit Plan Mode before GO?", "Were commits atomic?", "Did any lane work happen outside assigned worktree?", "If the project uses lane worktrees, were real git worktrees created in the project-approved lanes directory?", "Were merged worktrees removed?", "Were merged branches deleted?", "Was GATE 4 respected?"]),
        p("FINAL WATCHDOG REPORT", "h3"),
        code(
            "MEMORY & FILE DISCIPLINE:        [VERIFIED / PARTIAL / FAILED]\n"
            "TASK PLAN COMPLIANCE:            [VERIFIED / PARTIAL / FAILED]\n"
            "TEST VALIDITY:                   [REAL / THEATER / UNVERIFIED]\n"
            "HALLUCINATIONS DETECTED:         [YES - list / NONE FOUND]\n"
            "BC PROTOCOL VIOLATIONS:          [list each / NONE FOUND]\n"
            "UNVERIFIED CLAIMS:               [list each / NONE FOUND]\n"
            "PHANTOM FILES:                   [list each / NONE FOUND]\n"
            "SUSPICIOUS ASSERTIONS:           [list each / NONE FOUND]\n"
            "TASKS CLAIMED DONE UNVERIFIED:   [list each / NONE FOUND]\n"
            "SCOPE CREEP:                     [list each / NONE FOUND]\n\n"
            "FINAL VERDICT: GO / NEEDS REVISION / BLOCK\n"
            "REQUIRED BEFORE NEXT SESSION:    [actions / NONE]"
        ),
        p("Optional paste block only when a project asks for executor-ready remediation text:", "h3"),
        code("---\nPASTE THIS INTO EXECUTOR:\n[short direct instructions]\n---"),
        PageBreak(),
    ]

    story += page_title("7. Role-Agnostic Architecture")
    story += [
        p("The AI landscape shifts constantly. Hardcoding model names into governance frameworks creates brittle systems. AXKI governance uses roles instead: executor and reviewer."),
        p("The user declares who builds and who validates at session start. The frameworks reference roles, not tool brands. Swap freely without reinstalling."),
        table(
            [
                ["Role", "Responsibilities", "Uses"],
                ["EXECUTOR (Builder)", "Write code, create commits, run tests, manage project-approved lanes, update memory files.", "Receives reviewer verdicts"],
                ["REVIEWER (Validator)", "Validate plans, run checklists, deploy watchdog, issue GO / NEEDS REVISION / BLOCK verdicts, catch hallucinations.", f"{skill('checklist')} or {codex('checklist')}\n{skill('validate')} or {codex('validate')}\n{skill('watchdog')} or {codex('watchdog')}"],
            ],
            [1.35 * inch, 2.55 * inch, 1.7 * inch],
        ),
        p("Examples", "h2"),
        code(f"{skill('init')} executor=claude reviewer=codex\n{codex('init')} executor=codex reviewer=claude"),
        p(f"When a new model drops, change the executor/reviewer values. Keep Claude Code invocations on {SKILL_PREFIX}* and Codex CLI invocations on {CODEX_PREFIX}*."),
        PageBreak(),
    ]

    story += page_title("8. Installation Guide")
    story += [
        p("For Claude Code (Skills Format)", "h2"),
        p("Claude Code uses a .claude/skills/ directory in your project root. Each AXKI skill lives in its own directory with a SKILL.md file."),
        code("git clone https://github.com/AXKI-Consulting/axki-governance-public.git\ncp -r axki-governance-public/.claude/ /path/to/your/project/.claude/"),
        p("Available Claude Code skills after install:", "h3"),
        code("\n".join([skill("init"), skill("checklist"), skill("validate"), skill("watchdog")])),
        p("For Codex CLI (AGENTS.md + Commands Format)", "h2"),
        p("Codex CLI uses an AGENTS.md file in your project root with command files copied into the project's command directory."),
        code("git clone https://github.com/AXKI-Consulting/axki-governance-public.git\ncp axki-governance-public/codex/AGENTS.md /path/to/your/project/AGENTS.md\ncp -r axki-governance-public/codex/commands/ /path/to/your/project/.codex/commands/"),
        p("Available Codex commands after install:", "h3"),
        code("\n".join([codex("init"), codex("checklist"), codex("validate"), codex("watchdog")])),
        PageBreak(),
    ]

    story += page_title("9. Real-World Validation")
    story += [
        p("Below is a real screenshot from a production-style session where one AI acts as executor and the other acts as adversarial reviewer. The watchdog validates claims, checks test output, and issues a final verdict."),
    ]
    if SCREENSHOT.exists():
        img = Image(str(SCREENSHOT), width=6.35 * inch, height=2.6 * inch)
        img.hAlign = "CENTER"
        story += [img, Spacer(1, 0.12 * inch)]
    story += [
        p("Governance works when every PASS has evidence, every FAIL has an explanation, and the final verdict is earned rather than assumed."),
        p("Release Checklist for This Kit", "h2"),
        checklist([f"Claude Code skill names use only {SKILL_PREFIX}*.", f"Codex command names use only {CODEX_PREFIX}*.", "No generic /axki:* syntax remains.", "No hardcoded default-branch push rule remains.", "Lane worktree guidance is conditional and project-approved.", "Watchdog output includes unverifiable claims, phantom files, suspicious assertions, scope creep, final verdict, and required next-session actions."]),
        PageBreak(),
    ]

    story += page_title("10. Ready to Implement This?")
    story += [
        p("These frameworks are free and open-source. Implementing AI governance across a real engineering team - with custom lanes, project-specific stop-hooks, and multi-agent workflows - still requires operational judgment."),
        p("AXKI helps engineering teams deploy structured AI coding governance so they ship faster without losing control. The framework can be adapted to your stack, repository workflow, and release process."),
        Spacer(1, 0.25 * inch),
        p("Book a Free Discovery Call with Max", "h2"),
        p("Let's discuss how to implement Boris Cherny governance in your AI-assisted development workflow.", "center"),
        Spacer(1, 0.2 * inch),
        p("axki.ca | max@axki.ca", "center"),
        p("AXKI - AI Automation Consultancy | Montreal, Canada", "center"),
    ]

    return story


def main():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(
        str(OUT),
        pagesize=letter,
        rightMargin=MARGIN_X,
        leftMargin=MARGIN_X,
        topMargin=MARGIN_Y,
        bottomMargin=0.72 * inch,
        title="AXKI AI Coding Governance Kit",
        author="Max Dion, AXKI",
        subject="Boris Cherny AI coding governance for Claude Code and Codex CLI",
        creator="AXKI PDF builder",
    )
    doc.build(build_story(), onFirstPage=footer, onLaterPages=footer)
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
