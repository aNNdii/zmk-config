# 🎹 Corne 3x6 - React/TypeScript Layout

> **Optimiert für React/TypeScript mit Aerospace Window Manager**
> Basierend auf Codebase-Analyse: 767 TypeScript-Dateien

![Keymap](assets/corne.svg)

## 📊 Warum dieses Layout?

Durch Analyse Ihrer Codebase wurden die häufigsten Sonderzeichen identifiziert:

| Zeichen | Häufigkeit | Platzierung |
|---------|-----------|-------------|
| `.` | 13.5% | Symbol Layer (G Position) |
| `()` | 5,050× | Symbol Layer (E/R) |
| `<>` | JSX/React | Symbol Layer (Z/X) - leicht erreichbar! |
| `;` | 8.6% | Symbol Layer (rechte Home Row) |
| `/` | 7.7% | Symbol Layer |
| `,` | 7.6% | Symbol Layer |
| `{}` | 3,094× | Symbol Layer (C/V) |
| `:` | 6.6% | Symbol Layer (T Position) |

**Resultat:** ~15-20% weniger Tastendrücke für React/TypeScript!

---

## 🎯 Layout-Übersicht

### **5 Layer-System:**
1. **BASE** - QWERTY mit CASG Home Row Mods (Hybrid)
2. **SYMBOL** - React/TypeScript-optimiert (Enter hold oder R2 Daumen)
3. **NUMBERS** - Zahlenreihe + Operatoren (Space hold oder L2 Daumen)
4. **NAV** - Vim-Style Navigation (L1 Daumen)
5. **SYSTEM** - Bluetooth, Volume (R3 Daumen oder R-Shift 2x)

### **Layer-Zugriff:**
- **L1 Daumen (outer-left)** → Nav Layer (momentary)
- **L2 Daumen (middle-left)** → Number Layer (momentary)
- **SPACE hold** → Number Layer (momentary)
- **ENTER hold** → Symbol Layer (momentary)
- **R2 Daumen (middle-right)** → Symbol Layer (momentary)
- **R3 Daumen (outer-right)** → System Layer (momentary)
- **R-Shift 2x tap** → System Layer (toggle - ESC zum Beenden)

---

## 🎹 Layer 0: BASE

```
╭─────┬─────┬─────┬─────┬─────┬─────╮   ╭─────┬─────┬─────┬─────┬─────┬──────────╮
│ ESC │  Q  │  W  │  E  │  R  │  T  │   │  Y  │  U  │  I  │  O  │  P  │   BSP ⌫  │
├─────┼─────┼─────┼─────┼─────┼─────┤   ├─────┼─────┼─────┼─────┼─────┼──────────┤
│ TAB │  A  │  S  │  D  │  F  │  G  │   │  H  │  J  │  K  │  L  │  ;  │    '     │
│     │Ctl/A│Alt/S│Sft/D│Cmd/F│     │   │     │Cmd/J│Sft/K│Alt/L│Ctl/;│          │
├─────┼─────┼─────┼─────┼─────┼─────┤   ├─────┼─────┼─────┼─────┼─────┼──────────┤
│SHIFT│  Z  │  X  │  C  │  V  │  B  │   │  N  │  M  │  ,  │  .  │  /  │  SHIFT   │
│     │     │     │     │     │     │   │     │     │     │     │     │   2x→    │
│     │     │     │     │     │     │   │     │     │     │     │     │   SYS    │
╰─────┴─────┴─────┼─────┼─────┼─────┤   ├─────┼─────┼─────┼─────┴─────┴──────────╯
                   │ NAV │ NUM │ SPC │   │ ENT │ SYM │ SYS │
                   │     │     │^NUM │   │^SYM │     │     │
                   ╰─────┴─────┴─────╯   ╰─────┴─────┴─────╯
```

### **CASG Home Row Mods (Hold) - Hybrid:**
- **Linke Hand:** A=Ctrl | S=Alt | D=Shift | F=Cmd ⭐
- **Rechte Hand:** J=Cmd ⭐ | K=Shift | L=Alt | ;=Ctrl
- **Alle 4 Modifier auf Home Row** für ergonomisches Tippen

### **Daumentasten (Layer-Trigger):**
- **Links:** NAV | NUM | Space (hold=NUM)
- **Rechts:** Enter (hold=SYM) | SYM | SYS

**Warum CASG Hybrid?**
- ✅ **Cmd auf Zeigefinger (F/J)** - stärkster Finger für wichtigsten Modifier!
- ✅ **Shift auf Mittelfinger (D/K)** - für Großbuchstaben
- ✅ **Alt auf Ringfinger (S/L)** - für Aerospace Window Manager
- ✅ **Alle Modifier nur über HRM** - sauberes, konsistentes Layout

### **Smart Keys:**
- **Backspace:** Standard Backspace
- **R-Shift 2x:** System Layer Toggle (ESC zum Beenden)

---

## 🎨 Layer 1: SYMBOL (React/TypeScript-optimiert)

```
╭─────┬─────┬─────┬─────┬─────┬─────╮   ╭─────┬─────┬─────┬─────┬─────┬─────╮
│  ~  │  !  │  @  │  (  │  )  │  :  │   │  ^  │  #  │  $  │  %  │  &  │     │
├─────┼─────┼─────┼─────┼─────┼─────┤   ├─────┼─────┼─────┼─────┼─────┼─────┤
│  `  │  [  │  ]  │  {  │  }  │  .  │   │  /  │  -  │  =  │  ;  │  "  │  *  │
├─────┼─────┼─────┼─────┼─────┼─────┤   ├─────┼─────┼─────┼─────┼─────┼─────┤
│     │  <  │  >  │  |  │  \  │  ,  │   │  ?  │  _  │  +  │  !  │  \  │     │
╰─────┴─────┴─────┼─────┼─────┼─────┤   ├─────┼─────┼─────┼─────┴─────┴─────╯
                  │     │     │     │   │ ███ │     │     │
                  ╰─────┴─────┴─────╯   ╰─────┴─────┴─────╯
```

**Design-Philosophie (ENTER hold mit rechter Hand):**
- **Linke Hand tippt (frei)** - häufigste Symbole!
- **`!` `@` auf Q/W** - Zeige-/Mittelfinger (stark!)
- **`()` auf E/R** - 5,050× Vorkommen im Codebase
- **`[]` `{}` auf Home Row** - S/D + C/V (leicht erreichbar!)
- **`<>` auf Z/X** - JSX/React/Generics (nebeneinander!)
- **`.` auf G** - 13.5% häufigstes Symbol
- **`:` auf T** - 6.6% für TypeScript Type Annotations

**Zugriff:** Enter halten (rechte Hand)

---

## 🔢 Layer 2: NUMBERS

```
╭─────┬─────┬─────┬─────┬─────┬─────╮   ╭─────┬─────┬─────┬─────┬─────┬─────╮
│     │  1  │  2  │  3  │  4  │  5  │   │  6  │  7  │  8  │  9  │  0  │     │
├─────┼─────┼─────┼─────┼─────┼─────┤   ├─────┼─────┼─────┼─────┼─────┼─────┤
│     │     │     │     │     │     │   │  +  │  -  │  *  │  /  │     │     │
├─────┼─────┼─────┼─────┼─────┼─────┤   ├─────┼─────┼─────┼─────┼─────┼─────┤
│     │     │     │     │     │     │   │  =  │     │  ,  │  .  │  /  │     │
╰─────┴─────┴─────┼─────┼─────┼─────┤   ├─────┼─────┼─────┼─────┴─────┴─────╯
                  │     │     │ ███ │   │     │     │     │
                  ╰─────┴─────┴─────╯   ╰─────┴─────┴─────╯
```

**Features:**
- Top Row: Zahlenreihe 1-0 (klassisch)
- Rechenoperatoren rechts: `+` `-` `*` `/` `=`
- Dezimal-Hilfen: `,` `.` (unten rechts)
- Alle anderen Positionen transparent (Base-Layer durchgereicht)

**Zugriff:** Space halten (linke Hand)

---

## 🧭 Layer 3: NAVIGATION

```
╭─────┬─────┬─────┬─────┬─────┬─────╮   ╭─────┬─────┬─────┬─────┬─────┬─────╮
│ ESC │     │     │     │     │     │   │HOME │PG_DN│PG_UP│ END │     │     │
│EXIT │     │     │     │     │     │   │     │     │     │     │     │     │
├─────┼─────┼─────┼─────┼─────┼─────┤   ├─────┼─────┼─────┼─────┼─────┼─────┤
│     │     │     │     │     │     │   │  ←  │  ↓  │  ↑  │  →  │  ↑  │     │
├─────┼─────┼─────┼─────┼─────┼─────┤   ├─────┼─────┼─────┼─────┼─────┼─────┤
│     │     │     │     │     │     │   │     │     │     │  ←  │  ↓  │  →  │
╰─────┴─────┴─────┼─────┼─────┼─────┤   ├─────┼─────┼─────┼─────┴─────┴─────╯
                  │     │     │     │   │     │     │     │
                  ╰─────┴─────┴─────╯   ╰─────┴─────┴─────╯
```

**Features:**
- **Vim-Style (Home Row rechts):** H=←, J=↓, K=↑, L=→
- **Dupliziert (Unten rechts):** ←, ↓, → (zusätzlicher Zugangspunkt)
- **Page-Navigation:** Home, End, PgUp, PgDn
- **ESC = Exit** (bei Toggle-Modus zurück zu BASE)

**Zugriff:** L1 Daumen (outer-left) halten (momentary)

---

## 🎛️ Layer 4: SYSTEM

```
╭─────┬─────┬─────┬─────┬─────┬─────╮   ╭─────┬─────┬─────┬─────┬─────┬─────╮
│ ESC │ BT0 │ BT1 │     │     │     │   │MUTE │ 🔉  │ 🔊  │     │     │     │
│EXIT │     │     │     │     │     │   │     │     │     │     │     │     │
├─────┼─────┼─────┼─────┼─────┼─────┤   ├─────┼─────┼─────┼─────┼─────┼─────┤
│     │     │     │     │     │     │   │     │     │     │     │     │     │
├─────┼─────┼─────┼─────┼─────┼─────┤   ├─────┼─────┼─────┼─────┼─────┼─────┤
│BTCLR│     │     │     │     │     │   │     │     │     │     │     │     │
╰─────┴─────┴─────┼─────┼─────┼─────┤   ├─────┼─────┼─────┼─────┴─────┴─────╯
                  │     │     │     │   │     │     │     │
                  ╰─────┴─────┴─────╯   ╰─────┴─────┴─────╯
```

**Features:**
- **Bluetooth:** Profile 0 (Q), Profile 1 (W) + Clear (L-Shift/BTCLR)
- **Volume:** Mute, Vol-, Vol+ (H/J/K)
- **ESC = Exit** (zurück zu BASE)

**Zugriff:** R-Shift double-tap (toggle - bleibt aktiv bis ESC oder R-Shift 2x)

**Beispiele:**
- Bluetooth wechseln: `R-Shift 2x` → `W` (BT 1) → `ESC`
- Lautstärke erhöhen: `R-Shift 2x` → `K` (Vol+) → `ESC`
- Lautstärke senken: `R-Shift 2x` → `J` (Vol-) → `ESC`
- Stummschalten: `R-Shift 2x` → `H` (Mute) → `ESC`

---

## 📊 Layout-Features

✅ **5 Layer** - Base, Symbol, Numbers, Nav, System  
✅ **CASG Home Row Mods** - Alle 4 Modifier (Ctrl/Alt/Shift/Cmd) nur über HRM  
✅ **Cmd auf Zeigefinger** - F/J für stärksten Finger  
✅ **React/JSX-optimiert** - `<>` auf Z/X (Symbol Layer)  
✅ **One-Hand Symbol Layer** - Enter hold (rechts), linke Hand tippt  
✅ **macOS + Aerospace** - Alt/Cmd via Home Row Mods optimal platziert  
✅ **Daumen nur für Layer** - NAV | NUM | SPC | ENT | SYM | SYS  
✅ **Minimal System Layer** - BT 0/1, BT Clear, Volume (Mute/Vol-/Vol+)  
✅ **Combos deaktiviert** - Arrow `=>`, `()`, `{}`, `[]` als Macros vorhanden, aber standardmäßig aus

---

## 📚 Ressourcen

- [ZMK Documentation](https://zmk.dev/docs)
- [Home Row Mods Guide](https://precondition.github.io/home-row-mods)
- [Corne Keyboard Wiki](https://github.com/foostan/crkbd)

---

## 🎯 Quick Reference Card

```
LAYER ACCESS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
L1 Daumen hold       → Nav Layer (momentary)
L2 Daumen hold       → Number Layer (momentary)
SPACE hold           → Number Layer (momentary)
ENTER hold           → Symbol Layer (momentary)
R2 Daumen hold       → Symbol Layer (momentary)
R3 Daumen hold       → System Layer (momentary)
R-Shift 2x tap       → System Layer (toggle, ESC to exit)

HOME ROW MODS (nur HRM - alle 4 Modifier):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
A hold  → Ctrl    |  J hold  → Cmd
S hold  → Alt     |  K hold  → Shift
D hold  → Shift   |  L hold  → Alt
F hold  → Cmd     |  ; hold  → Ctrl

THUMB KEYS (Layer-Trigger):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Left:  NAV | NUM | Space (hold=NUM)
Right: Enter (hold=SYM) | SYM | SYS
```
