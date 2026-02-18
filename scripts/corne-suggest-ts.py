#!/usr/bin/env python3
"""
Corne Symbol Layout Suggester — TypeScript/TSX Edition
Adapted from clayto.com/2025/corne/ (original: Rust/Gemini)

Analyzes TypeScript/TSX source files to suggest an optimal two-layer
Corne keyboard symbol layout based on real symbol co-occurrence patterns.

Usage:
    python3 corne-suggest-ts.py /path/to/ts/project

Constraints built in:
    - Right-hand trigger (SYM = right thumb) → frequent symbols right
    - ( ) { } on right home row (hardcoded, most frequent)
    - Paired symbols adjacent: () [] {} <>
    - Symbols common in TS: . ' ; / : = - > < ? & | @ ` _ ! ~ ^ + % # $ *
"""

import argparse
from pathlib import Path
from collections import defaultdict, Counter
import sys

try:
    from pygments import lex
    from pygments.lexers import TypeScriptLexer, TsxLexer
    from pygments.token import Punctuation, Operator, Token
except ImportError:
    print(
        "Error: 'Pygments' required. Install with: pip install Pygments",
        file=sys.stderr,
    )
    sys.exit(1)

# Symbols excluded from the SYM layer analysis because they exist
# comfortably on BASE layer (right hand) or are handled by Prettier
BLACKLIST = {
    ",",  # BASE layer right hand, Prettier handles
    ".",  # BASE layer right hand — but still very frequent in SYM too
    ";",  # Prettier auto-inserts
    "'",  # already on BASE right pinky — but let's keep it for analysis
    '"',  # Prettier converts to '
}

# Symbols we want to keep on the LEFT side of the keyboard
# (less frequent or paired with common right-side symbols)
PREFER_LEFT = {"~", "^", "%", "#", "$", "@", "`", "\\", "!"}

# Key ergonomic scores for a 3×5 Corne half (per half, columns 0-4 left-to-right)
# Higher = better (more comfortable / stronger finger / less stretch)
# Layout: col 0=pinky, col 1=ring, col 2=middle, col 3=index, col 4=index-outer(inner col)
# For LEFT half: col 4 is the innermost (closest to center)
# For RIGHT half: col 0 is the innermost (closest to center)
KEY_SCORES = {
    # Left hand: col 0=pinky-outer, 1=pinky, 2=ring, 3=middle, 4=index
    ("L", 0, 0): 1,
    ("L", 0, 1): 3,
    ("L", 0, 2): 7,
    ("L", 0, 3): 8,
    ("L", 0, 4): 6,
    ("L", 1, 0): 2,
    ("L", 1, 1): 5,
    ("L", 1, 2): 9,
    ("L", 1, 3): 10,
    ("L", 1, 4): 7,
    ("L", 2, 0): 1,
    ("L", 2, 1): 2,
    ("L", 2, 2): 4,
    ("L", 2, 3): 5,
    ("L", 2, 4): 3,
    # Right hand: col 0=index, 1=index-outer, 2=middle, 3=ring, 4=pinky — wait, let's mirror:
    # col 0=inner-index, 1=middle, 2=ring, 3=pinky, 4=pinky-outer
    ("R", 0, 0): 8,
    ("R", 0, 1): 9,
    ("R", 0, 2): 7,
    ("R", 0, 3): 3,
    ("R", 0, 4): 1,
    ("R", 1, 0): 10,
    ("R", 1, 1): 10,
    ("R", 1, 2): 9,
    ("R", 1, 3): 5,
    ("R", 1, 4): 2,
    ("R", 2, 0): 5,
    ("R", 2, 1): 5,
    ("R", 2, 2): 4,
    ("R", 2, 3): 2,
    ("R", 2, 4): 1,
}

CORNE_KEYS = [(h, r, c) for h in ["L", "R"] for r in range(3) for c in range(5)]
NUM_KEYS_PER_LAYER = len(CORNE_KEYS)

# Pairs that should always be placed adjacent on the same hand
IMPORTANT_PAIRS = [("(", ")"), ("{", "}"), ("[", "]"), ("<", ">")]


def get_lexer(filepath: Path):
    if filepath.suffix == ".tsx":
        return TsxLexer()
    return TypeScriptLexer()


def extract_symbols(directory: Path) -> list[str]:
    all_symbols = []
    print(f"[*] Scanning for .ts / .tsx files in '{directory}'...")
    files = list(directory.rglob("*.ts")) + list(directory.rglob("*.tsx"))
    # Skip generated files, node_modules, dist, build
    files = [
        f
        for f in files
        if not any(
            part in f.parts
            for part in ("node_modules", "dist", "build", ".next", "coverage", "builds")
        )
    ]
    if not files:
        print(f"[!] No .ts/.tsx files found in {directory}", file=sys.stderr)
        sys.exit(1)
    print(f"[*] Found {len(files)} files.")
    for i, filepath in enumerate(files):
        print(f"\r[*] Processing {i + 1}/{len(files)}: {filepath.name:<40}", end="")
        try:
            code = filepath.read_text(encoding="utf-8")
            lexer = get_lexer(filepath)
            tokens = lex(code, lexer)
            for ttype, value in tokens:
                if (
                    ttype in Punctuation
                    or ttype in Operator
                    or ttype is Token.Punctuation
                    or ttype is Token.Operator
                ):
                    # Expand multi-char tokens to individual characters
                    all_symbols.extend(list(value))
        except Exception as e:
            print(f"\n[!] Error processing {filepath}: {e}", file=sys.stderr)
    print(f"\n[*] Done. Extracted {len(all_symbols)} symbol tokens.")
    return all_symbols


def build_models(symbols: list[str]):
    chain = defaultdict(Counter)
    for s1, s2 in zip(symbols, symbols[1:]):
        chain[s1][s2] += 1

    graph = defaultdict(int)
    for s1, followers in chain.items():
        for s2, count in followers.items():
            edge = tuple(sorted((s1, s2)))
            graph[edge] += count

    return chain, graph


def print_frequency_analysis(chain, symbol_freq, top_n=20):
    print(f"\n## Symbol Frequency + Top Followers (top {top_n} symbols)")
    print("-" * 60)
    sorted_symbols = [s for s, _ in symbol_freq.most_common(top_n) if s in chain]
    for symbol in sorted_symbols:
        total = symbol_freq[symbol]
        followers = chain[symbol]
        top = followers.most_common(5)
        followers_str = ", ".join([f"'{f}'({c})" for f, c in top])
        print(f"  '{symbol}' ({total:>6}x) → {followers_str}")
    print("-" * 60)


def get_roll_neighbors(key, layout):
    hand, r, c = key
    neighbors = []
    if c > 0 and layout.get((hand, r, c - 1)) is not None:
        neighbors.append((hand, r, c - 1))
    if c < 4 and layout.get((hand, r, c + 1)) is not None:
        neighbors.append((hand, r, c + 1))
    return neighbors


def generate_layout(graph, symbols_to_place, symbol_freq, right_hand_bias=True):
    """
    Place symbols on a Corne half-layout.
    right_hand_bias: frequent symbols prefer right side (SYM = right thumb).
    """
    layout = {}
    unplaced = list(symbols_to_place)
    empty_keys = list(CORNE_KEYS)

    # --- Hardcoded placements for TypeScript ---
    # ( ) { } are the most frequent and go on right home row
    # Right home row positions: (R,1,0)=H (R,1,1)=J (R,1,2)=K (R,1,3)=L
    forced = {
        ("R", 1, 0): "(",
        ("R", 1, 1): ")",
        ("R", 1, 2): "{",
        ("R", 1, 3): "}",
    }
    for key, sym in forced.items():
        if sym in unplaced and key in empty_keys:
            layout[key] = sym
            unplaced.remove(sym)
            empty_keys.remove(key)

    # --- Place important pairs adjacent ---
    key_pair_locations = []
    for h in ["L", "R"]:
        for r in range(3):
            for c in range(4):
                k1, k2 = (h, r, c), (h, r, c + 1)
                if k1 in empty_keys and k2 in empty_keys:
                    score = KEY_SCORES[k1] + KEY_SCORES[k2]
                    key_pair_locations.append(((k1, k2), score))
    key_pair_locations.sort(key=lambda x: x[1], reverse=True)

    scored_pairs = []
    for s1, s2 in IMPORTANT_PAIRS:
        if s1 in unplaced and s2 in unplaced:
            co_score = graph.get(tuple(sorted((s1, s2))), 0)
            scored_pairs.append(((s1, s2), co_score))
    scored_pairs.sort(key=lambda x: x[1], reverse=True)

    for (s1, s2), _ in scored_pairs:
        for (k1, k2), _ in key_pair_locations:
            if k1 in empty_keys and k2 in empty_keys:
                # Prefer-left symbols go on left side
                if s1 in PREFER_LEFT and k1[0] != "L":
                    continue
                layout[k1] = s1
                layout[k2] = s2
                unplaced.remove(s1)
                unplaced.remove(s2)
                empty_keys.remove(k1)
                empty_keys.remove(k2)
                break

    # --- Place remaining symbols by roll score + ergonomic score ---
    while unplaced and empty_keys:
        best_score = -1
        best_sym, best_key = None, None
        for sym in unplaced:
            prefer_right = sym not in PREFER_LEFT
            for key in empty_keys:
                hand = key[0]
                # Penalize wrong-hand placement
                hand_bonus = 0
                if right_hand_bias:
                    hand_bonus = 2 if (prefer_right and hand == "R") else 0
                    hand_bonus = max(
                        hand_bonus, 1 if (not prefer_right and hand == "L") else 0
                    )

                roll_score = sum(
                    graph.get(tuple(sorted((sym, layout[nk]))), 0)
                    for nk in get_roll_neighbors(key, layout)
                )
                key_score = KEY_SCORES[key] * symbol_freq.get(sym, 1) * 0.01
                total = (
                    roll_score
                    + key_score
                    + hand_bonus * symbol_freq.get(sym, 1) * 0.005
                )
                if total > best_score:
                    best_score, best_sym, best_key = total, sym, key
        if best_key:
            layout[best_key] = best_sym
            unplaced.remove(best_sym)
            empty_keys.remove(best_key)
        else:
            break

    return layout


def print_layout(layout, title):
    print(f"\n## {title}")
    print("=" * 70)
    # Map finger names for readability
    finger_l = ["pnky", "ring", " mid", " idx", " idx"]
    finger_r = [" idx", " mid", "ring", "pnky", "pnky"]

    def sym(h, r, c):
        return layout.get((h, r, c), " ")

    header = "  L-pnky ring  mid  idx  idx       idx  mid  ring pnky pnky  R"
    rows = []
    for r in range(3):
        row_name = ["TOP ", "HOME", "BOT "][r]
        left = "  ".join(f"{sym('L', r, c):^3}" for c in range(5))
        right = "  ".join(f"{sym('R', r, c):^3}" for c in range(5))
        rows.append(f"  {row_name}  [ {left} ]     [ {right} ]")

    border = "  " + "-" * 66
    print(border)
    for row in rows:
        print(row)
        print(border)

    # Print co-occurrence rolls summary
    print()


def print_roll_analysis(layout, graph, title):
    """Find and print the best roll combos in the layout."""
    print(f"  Roll combos in '{title}':")
    rolls = []
    for h in ["L", "R"]:
        for r in range(3):
            for c in range(4):
                k1, k2 = (h, r, c), (h, r, c + 1)
                s1, s2 = layout.get(k1), layout.get(k2)
                if s1 and s2:
                    score = graph.get(tuple(sorted((s1, s2))), 0)
                    if score > 0:
                        rolls.append((score, h, r, c, s1, s2))
    rolls.sort(reverse=True)
    for score, h, r, c, s1, s2 in rolls[:10]:
        row_name = ["top", "home", "bot"][r]
        hand = "right" if h == "R" else "left"
        print(f"    '{s1}{s2}'  {score:>6}x   ({hand} {row_name})")


def main():
    parser = argparse.ArgumentParser(
        description="Suggest a Corne symbol layer based on TypeScript/TSX code analysis."
    )
    parser.add_argument(
        "directory", type=str, help="Directory with TypeScript source files"
    )
    parser.add_argument(
        "--top",
        type=int,
        default=20,
        help="How many symbols to show in frequency report",
    )
    args = parser.parse_args()

    src_path = Path(args.directory)
    if not src_path.is_dir():
        print(f"Error: Not a directory: '{src_path}'", file=sys.stderr)
        sys.exit(1)

    all_symbols = extract_symbols(src_path)
    if not all_symbols:
        print("[!] No symbols extracted.", file=sys.stderr)
        sys.exit(1)

    chain, graph = build_models(all_symbols)

    # Only keep actual symbols/punctuation — exclude letters and digits
    VALID_SYMBOLS = set("!@#$%^&*()-_=+[]{}|;:<>,.?/`~\\'\"")
    all_unique = (set(all_symbols) - BLACKLIST) & VALID_SYMBOLS
    symbol_freq = Counter()
    for sym in all_symbols:
        if sym not in BLACKLIST and sym in VALID_SYMBOLS:
            symbol_freq[sym] += 1

    print_frequency_analysis(chain, symbol_freq, top_n=args.top)

    # Split into two groups: frequent (layer 1 = SYM layer) and rare (layer 2)
    # Take top 10 by frequency for the main SYM layer, rest overflow
    sorted_by_freq = [s for s, _ in symbol_freq.most_common() if s in all_unique]

    # Layer 1: the symbols we want on the primary SYM layer (top ~10 + forced pairs)
    # We allow up to NUM_KEYS_PER_LAYER symbols (10 per side = 30 total, but only 30 keys)
    layer1_syms = sorted_by_freq[:NUM_KEYS_PER_LAYER]
    layer2_syms = sorted_by_freq[NUM_KEYS_PER_LAYER:]

    print(f"\n[*] Layer 1 symbols ({len(layer1_syms)}): {' '.join(layer1_syms)}")
    print(
        f"[*] Layer 2 symbols ({len(layer2_syms)}): {' '.join(layer2_syms) if layer2_syms else '(none)'}"
    )

    print("\n[*] Generating layout...")
    layout = generate_layout(graph, layer1_syms, symbol_freq, right_hand_bias=True)

    print_layout(layout, "Suggested SYM Layer (TypeScript/TSX, right-thumb trigger)")
    print_roll_analysis(layout, graph, "SYM Layer")

    if layer2_syms:
        layout2 = generate_layout(
            graph, layer2_syms, symbol_freq, right_hand_bias=False
        )
        print_layout(
            layout2, "Overflow symbols (secondary layer or left-side additions)"
        )
        print_roll_analysis(layout2, graph, "overflow")


if __name__ == "__main__":
    main()
