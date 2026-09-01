"""secret-handshake-fn-commands-conformance-oracle -- deterministic CONFORMANCE oracle for `secret-handshake` (python).

WHAT THIS DECIDES: given a candidate callable and one canonical input, it decides whether the candidate
agrees with the proven reference. It is a *conformance* decider over a fixed, published corpus -- it does
not decide correctness in general, and it says nothing about inputs outside the corpus.

SCOPE (declared, so the boundary is visible rather than discovered): the corpus is the canonical Exercism
test data for this task, 8 input/output pairs, listed in `probes/probes.jsonl`. Inputs outside that
set are simply not covered; `decide` answers only about the input it is given.

PROVENANCE: the reference body comes from the Exercism reference solution for `secret-handshake` (MIT, Exercism);
the type annotations were added by harvest, the body is unchanged (checked at AST level). The capability
was PROVEN by the exercism testsuite (pin=2e18b75ae190678a) and re-executed by harvest in a sealed sandbox
(unshare -rn) -- verify-not-relay, not a copied ledger label.
"""

TASK = "secret-handshake"
CWE = "secret-handshake"          # a publish-motor egyseges mezonevet var; itt a feladat azonositoja


def decide(fn, value, expect):
    """PASS iff fn(value) == expect. Determinista, nincs halozat, nincs allapot."""
    try:
        return "PASS" if fn(value) == expect else "FAIL"
    except Exception:                                      # noqa: BLE001
        return "FAIL"


GESTURES = ['jump', 'close your eyes', 'double blink', 'wink']

def commands(binary_str: str) -> list:
    reverse, *bits = [digit == '1' for digit in binary_str]
    actions = [gesture for gesture, bit in zip(GESTURES, bits) if bit]
    return actions if reverse else actions[::-1]

REFERENCE = commands
