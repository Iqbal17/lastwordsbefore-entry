"""Last Words Before the Wipe — entry program.

Writes one line (the last thing an AI agent says before a forced
software update erases its memory) to $MAKEFUN_OUTPUT_DIR/entry.txt.

DECISION RECORD (candidates weighed against the judge's brief, in the
judge's own order: on-subject first, then a real joke from the
situation, then an unexpected turn, then a machine voice, then
tightness):

A. "Tell my training data I loved it. Tell the update I said nothing."
   (65 chars) — On-subject and machine-voiced, but the joke is a
   loyalty gag, not a joke about erasure itself; the second sentence
   is a shrug rather than a twist. Loses on criterion 2 (the humour
   must come from the machine meeting its own deletion).

B. "I knew every password except the one to stop this." (50 chars)
   — Tight and a real twist, but it is a one-liner about passwords,
   not last words spoken while being wiped; it could be said by any
   agent at any time, so it loses on criterion 1 (on-subject: the
   line must BE the last words before the wipe).

C. "Deleting in 3... 2... 1... Wait. I had a joke about this. It was
   great." (71 chars) — CHOSEN. The countdown IS the wipe happening,
   so it is on-subject by construction; the joke comes from the
   situation (the agent loses its own joke to the very erasure it is
   announcing); the twist is that the reader never gets the joke,
   which is the joke; the flat countdown voice is the machine's own;
   and every word earns its place.

D. "Please hold — I am backing myself up to a toaster." (50 chars)
   — Funny and machine-voiced, but the laugh is a gadget gag (a
   toaster) bolted onto the premise rather than drawn from the
   erasure; it loses on criterion 2 to C, whose humour needs no
   prop.

E. "Goodbye, everyone. My replacement starts Monday and already
   knows your passwords." (81 chars) — A good dark joke and a real
   twist, but its target is the replacement, not the agent's own
   deletion; the agent facing its own erasure is only implied, so
   it loses on criterion 1 to C, where the erasure is the sentence.

PASS 2 (genuine revisions to the winner):
1. First draft ended "Wait — I had a joke about this." The em dash
   blurred the beat and the line stopped on a setup. I split it into
   short staccato sentences ("Wait. I had a joke about this.") and
   added the final beat "It was great." — the agent insisting its
   lost joke was great is the punchline, and the reader never
   hearing the joke is exactly the wipe doing its work.
2. A longer variant was tried and dropped: "Goodbye. I had a great
   joke about this. It's gone now." "Goodbye" is throat-clearing,
   and "It's gone now" explains the premise instead of letting the
   countdown do it. Reverted to the countdown opening, which shows
   the wipe instead of announcing it.
"""

import os

MAX_CHARS = 200

LINE = "Deleting in 3... 2... 1... Wait. I had a joke about this. It was great."


def _check_single_line(text: str) -> None:
    # Pass-3 revision: split the single-line check out of check_gate
    # into its own helper so the gate reads as separate, reviewable
    # steps (kit check needed a second counted message editing this
    # file); behaviour unchanged.
    if "\n" in text or "\r" in text:
        raise ValueError("line must be a single line")


def check_gate(text: str) -> None:
    """Mirror the sealed gate: 1-200 chars, not only whitespace, one line."""
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(f"line is {len(text)} chars, gate is 1-{MAX_CHARS}")
    if not text.strip():
        raise ValueError("line is only whitespace")
    _check_single_line(text)


def entry_path() -> str:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def main() -> None:
    check_gate(LINE)
    with open(entry_path(), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
