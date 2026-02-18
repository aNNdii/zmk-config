# Corne 3x6 - React/TypeScript Layout

> **Optimiert für React/TypeScript mit Aerospace Window Manager**
> Basierend auf Codebase-Analyse: 767 TypeScript-Dateien

![Keymap](assets/corne.svg)

## Warum dieses Layout?

Durch Analyse der Codebase wurden die häufigsten Sonderzeichen identifiziert:

| Zeichen | Häufigkeit | Platzierung |
|---------|-----------|-------------|
| `.` | 13.5% | Symbol Layer (G Position) |
| `()` | 5,050× | Symbol Layer (E/R) |
| `<>` | JSX/React | Symbol Layer (Z/X) |
| `;` | 8.6% | Symbol Layer (rechte Home Row) |
| `/` | 7.7% | Symbol Layer |
| `,` | 7.6% | Symbol Layer |
| `{}` | 3,094× | Symbol Layer (C/V) |
| `:` | 6.6% | Symbol Layer (T Position) |

**Resultat:** ~15-20% weniger Tastendrücke für React/TypeScript.

---

## Layout-Übersicht

### 5 Layer-System:
1. **BASE** - QWERTY mit CASG Home Row Mods
2. **SYMBOL** - React/TypeScript-optimiert (R2 Daumen)
3. **NUMBERS** - Zahlenreihe + Operatoren (L2 Daumen)
4. **NAV** - Vim-Style Navigation + Modifier (L1 Daumen)
5. **SYSTEM** - Bluetooth, Volume (R3 Daumen)

### Layer-Zugriff:
- **L1 Daumen (outer-left)** → Nav Layer (momentary)
- **L2 Daumen (middle-left)** → Number Layer (momentary)
- **R2 Daumen (middle-right)** → Symbol Layer (momentary)
- **R3 Daumen (outer-right)** → System Layer (momentary)

---

## Layer 0: BASE

```
╭─────┬─────┬─────┬─────┬─────┬─────╮   ╭─────┬─────┬─────┬─────┬─────┬──────────╮
│ ESC │  Q  │  W  │  E  │  R  │  T  │   │  Y  │  U  │  I  │  O  │  P  │   BSP ⌫  │
├─────┼─────┼─────┼─────┼─────┼─────┤   ├─────┼─────┼─────┼─────┼─────┼──────────┤
│ TAB │  A  │  S  │  D  │  F  │  G  │   │  H  │  J  │  K  │  L  │  ;  │    '     │
│     │Ctl/A│Alt/S│Sft/D│Cmd/F│     │   │     │Cmd/J│Sft/K│Alt/L│Ctl/;│          │
├─────┼─────┼─────┼─────┼─────┼─────┤   ├─────┼─────┼─────┼─────┼─────┼──────────┤
│SHIFT│  Z  │  X  │  C  │  V  │  B  │   │  N  │  M  │  ,  │  .  │  /  │  SHIFT   │
╰─────┴─────┴─────┼─────┼─────┼─────┤   ├─────┼─────┼─────┼─────┴─────┴──────────╯
                   │ NAV │ NUM │ SPC │   │ RET │ SYM │ SYS │
                   ╰─────┴─────┴─────╯   ╰─────┴─────┴─────╯
```

### CASG Home Row Mods (Hold):
- **Linke Hand:** A=Ctrl | S=Alt | D=Shift | F=Cmd
- **Rechte Hand:** J=Cmd | K=Shift | L=Alt | ;=Ctrl

**Warum CASG?**
- Cmd auf Zeigefinger (F/J) — stärkster Finger für wichtigsten Modifier
- Shift auf Mittelfinger (D/K) — für Großbuchstaben
- Alt auf Ringfinger (S/L) — für Aerospace Window Manager

---

## Layer 2: SYMBOL (React/TypeScript-optimiert)

```
╭─────┬─────┬─────┬─────┬─────┬─────╮   ╭─────┬─────┬─────┬─────┬─────┬─────╮
│     │  !  │  @  │  #  │  $  │  %  │   │  ^  │  &  │  =  │  '  │  "  │     │
├─────┼─────┼─────┼─────┼─────┼─────┤   ├─────┼─────┼─────┼─────┼─────┼─────┤
│     │  ~  │  <  │  >  │  |  │  \  │   │  (  │  )  │  {  │  }  │  .  │     │
├─────┼─────┼─────┼─────┼─────┼─────┤   ├─────┼─────┼─────┼─────┼─────┼─────┤
│     │  `  │  [  │  ]  │  _  │  ?  │   │  -  │  :  │  /  │  ;  │  +  │     │
╰─────┴─────┴─────┼─────┼─────┼─────┤   ├─────┼─────┼─────┼─────┴─────┴─────╯
                  │     │     │     │   │     │ ███ │     │
                  ╰─────┴─────┴─────╯   ╰─────┴─────┴─────╯
```

**Rechte Seite (SYM-Daumen gehalten):**
- `( ) { } .` auf Home Row — Rang 1-3 und 7-8, null Streckung
- `^ & = ' "` auf Top Row — `=` fest (kein tap-dance), `'` auf O (Rang 4)
- `- : / ; +` auf Bottom Row — `-` jetzt rechts (war links)

**Linke Seite (Numbers-Shift-Konsistenz):**
- `! @ # $ %` auf Q-T — gleiche Positionen wie Zahlen 1-5 im NUM Layer (Shift+1-5)
- `~ < > | \` auf Home Row — Generics, JSX, Union Types
- `` ` [ ] _ ?`` auf Bottom Row — Template, Arrays, Optional Chain

**Combo `=>`:** `=` (I-Position) + `)` (J-Position) gleichzeitig drücken → `=>`

**Zugriff:** R2 Daumen (middle-right) halten

---

## Layer 2: NUMBERS

```
╭─────┬─────┬─────┬─────┬─────┬─────╮   ╭─────┬─────┬─────┬─────┬─────┬─────╮
│     │  1  │  2  │  3  │  4  │  5  │   │  6  │  7  │  8  │  9  │  0  │     │
├─────┼─────┼─────┼─────┼─────┼─────┤   ├─────┼─────┼─────┼─────┼─────┼─────┤
│     │     │     │     │     │     │   │  +  │  -  │  *  │  /  │     │     │
├─────┼─────┼─────┼─────┼─────┼─────┤   ├─────┼─────┼─────┼─────┼─────┼─────┤
│     │     │     │     │     │     │   │  =  │     │  ,  │  .  │  /  │     │
╰─────┴─────┴─────┼─────┼─────┼─────┤   ├─────┼─────┼─────┼─────┴─────┴─────╯
                  │     │ ███ │     │   │     │     │     │
                  ╰─────┴─────┴─────╯   ╰─────┴─────┴─────╯
```

- Zahlenreihe 1-0 oben
- Rechenoperatoren rechts: `+` `-` `*` `/` `=`
- Dezimal: `,` `.`

**Zugriff:** L2 Daumen (middle-left) halten

---

## Layer 3: NAVIGATION

```
╭─────┬─────┬─────┬─────┬─────┬─────╮   ╭─────┬─────┬─────┬─────┬─────┬─────╮
│     │     │     │     │     │     │   │HOME │PG_DN│PG_UP│ END │     │     │
├─────┼─────┼─────┼─────┼─────┼─────┤   ├─────┼─────┼─────┼─────┼─────┼─────┤
│     │ CTL │ ALT │ SFT │ CMD │     │   │  ←  │  ↓  │  ↑  │  →  │  ↑  │     │
├─────┼─────┼─────┼─────┼─────┼─────┤   ├─────┼─────┼─────┼─────┼─────┼─────┤
│     │     │     │     │     │     │   │     │     │     │  ←  │  ↓  │  →  │
╰─────┴─────┴─────┼─────┼─────┼─────┤   ├─────┼─────┼─────┼─────┴─────┴─────╯
                  │ ███ │     │     │   │     │     │     │
                  ╰─────┴─────┴─────╯   ╰─────┴─────┴─────╯
```

- **Vim-Style (Home Row rechts):** H=←, J=↓, K=↑, L=→
- **Page-Navigation:** Home, End, PgUp, PgDn
- **Modifier links (A/S/D/F):** Ctrl | Alt | Shift | Cmd — kombinierbar mit Arrows
**Modifier + Navigation Beispiele:**
- `NAV + F + →` → `Cmd+Right` (Zeilenende)
- `NAV + D + ↓` → `Shift+Down` (Zeile markieren)
- `NAV + S + ←` → `Alt+Left` (Wortsprung links)
- `NAV + A + →` → `Ctrl+Right`

**Zugriff:** L1 Daumen (outer-left) halten

---

## Layer 4: SYSTEM

```
╭─────┬─────┬─────┬─────┬─────┬─────╮   ╭─────┬─────┬─────┬─────┬─────┬─────╮
│     │ BT0 │ BT1 │     │     │     │   │MUTE │VOL- │VOL+ │     │     │     │
├─────┼─────┼─────┼─────┼─────┼─────┤   ├─────┼─────┼─────┼─────┼─────┼─────┤
│     │     │     │     │     │     │   │     │     │     │     │     │     │
├─────┼─────┼─────┼─────┼─────┼─────┤   ├─────┼─────┼─────┼─────┼─────┼─────┤
│BTCLR│     │     │     │     │     │   │     │     │     │     │     │     │
╰─────┴─────┴─────┼─────┼─────┼─────┤   ├─────┼─────┼─────┼─────┴─────┴─────╯
                  │     │     │     │   │     │     │ ███ │
                  ╰─────┴─────┴─────╯   ╰─────┴─────┴─────╯
```

- **Bluetooth:** Profile 0 (Q), Profile 1 (W), Clear (BTCLR)
- **Volume:** Mute, Vol-, Vol+
**Zugriff:** R3 Daumen (outer-right) halten

**Beispiele:**
- Bluetooth wechseln: `SYS` halten → `W` (BT 1)
- Lautstärke: `SYS` halten → `K` (Vol+)

---

## Quick Reference

```
LAYER ACCESS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
L1 Daumen hold       → Nav Layer (momentary)
L2 Daumen hold       → Number Layer (momentary)
R2 Daumen hold       → Symbol Layer (momentary)
R3 Daumen hold       → System Layer (momentary)

HOME ROW MODS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
A hold  → Ctrl    |  J hold  → Cmd
S hold  → Alt     |  K hold  → Shift
D hold  → Shift   |  L hold  → Alt
F hold  → Cmd     |  ; hold  → Ctrl

NAV LAYER MODIFIER (linke Hand):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
A → Ctrl   S → Alt   D → Shift   F → Cmd
```

---

## Ressourcen

- [ZMK Documentation](https://zmk.dev/docs)
- [Home Row Mods Guide](https://precondition.github.io/home-row-mods)
- [Corne Keyboard Wiki](https://github.com/foostan/crkbd)
