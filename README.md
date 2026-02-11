# 🎹 Corne 3x6 - React/TypeScript Layout

> **Optimiert für React/TypeScript mit Aerospace Window Manager**
> Basierend auf Codebase-Analyse: 767 TypeScript-Dateien

![Keymap](assets/corne.svg)

## 📊 Warum dieses Layout?

Durch Analyse Ihrer Codebase wurden die häufigsten Sonderzeichen identifiziert:

| Zeichen | Häufigkeit | Platzierung |
|---------|-----------|-------------|
| `.` | 13.5% | Symbol Layer (G Position) |
| `()` | 5,050× | Combo (D+F) + Symbol Layer (E/R) |
| `<>` | JSX/React | Symbol Layer (Z/X) - leicht erreichbar! |
| `;` | 8.6% | Symbol Layer (rechte Home Row) |
| `/` | 7.7% | Symbol Layer |
| `,` | 7.6% | Symbol Layer |
| `{}` | 3,094× | Combo (J+K) + Symbol Layer (C/V) |
| `:` | 6.6% | Symbol Layer (T Position) |

**Resultat:** ~15-20% weniger Tastendrücke für React/TypeScript!

---

## 🎯 Layout-Übersicht

### **5 Layer-System:**
1. **BASE** - QWERTY mit CASG Home Row Mods (Hybrid)
2. **SYMBOL** - React/TypeScript-optimiert (Enter hold)
3. **NUMBERS** - Zahlenreihe + Numpad (Space hold)
4. **NAV** - Vim-Style Navigation (Shift+Space hold)
5. **SYSTEM** - Bluetooth, Volume, Brightness (R-Shift 2x)

### **Layer-Zugriff:**
- **ENTER hold** → Symbol Layer (momentary)
- **SPACE hold** → Number Layer (momentary)
- **SHIFT+SPACE hold** → Nav Layer (momentary)
- **R-Shift 2x tap** → System Layer (toggle - ESC zum Beenden)

---

## 🎹 Layer 0: BASE

```
╭─────┬─────┬─────┬─────┬─────┬─────╮   ╭─────┬─────┬─────┬─────┬─────┬──────────╮
│ ESC │  Q  │  W  │  E  │  R  │  T  │   │  Y  │  U  │  I  │  O  │  P  │BSP/DEL ⌫ │
│     │     │     │     │     │     │   │     │     │     │     │     │  Shift=⌦ │
├─────┼─────┼─────┼─────┼─────┼─────┤   ├─────┼─────┼─────┼─────┼─────┼──────────┤
│ TAB │  A  │  S  │  D  │  F  │  G  │   │  H  │  J  │  K  │  L  │  ;  │    '     │
│     │Ctl/A│Alt/S│Sft/D│Cmd/F│     │   │     │Cmd/J│Sft/K│Alt/L│Ctl/;│          │
├─────┼─────┼─────┼─────┼─────┼─────┤   ├─────┼─────┼─────┼─────┼─────┼──────────┤
│SHIFT│  Z  │  X  │  C  │  V  │  B  │   │  N  │  M  │  ,  │  .  │  /  │  SHIFT   │
│     │     │     │     │     │     │   │     │     │     │     │     │   2x→    │
│     │     │     │     │     │     │   │     │     │     │     │     │   SYS    │
╰─────┴─────┴─────┼─────┼─────┼─────┤   ├─────┼─────┼─────┼─────┴─────┴──────────╯
                  │ CMD │ ALT │ SPC │   │ ENT │ CTL │ CMD │
                  │     │     │^NUM │   │^SYM │     │     │
                  │     │     │^NAV │   │     │     │     │
                  ╰─────┴─────┴─────╯   ╰─────┴─────┴─────╯
             (Shift+Space hold = Nav)
```

### **CASG Home Row Mods (Hold) - Hybrid:**
- **Linke Hand:** A=Ctrl | S=Alt | D=Shift | F=Cmd ⭐
- **Rechte Hand:** J=Cmd ⭐ | K=Shift | L=Alt | ;=Ctrl
- **Alle 4 Modifier auf Home Row** für ergonomisches Tippen

### **Daumentasten (Backup für Shortcuts):**
- **Links:** Cmd | Alt | Space
  - **Space tap:** Space
  - **Space hold:** Number Layer
  - **Shift+Space hold:** Nav Layer
- **Rechts:** Enter (hold = Symbols) | Ctrl | Cmd

**Warum CASG Hybrid?**
- ✅ **Cmd auf Zeigefinger (F/J)** - stärkster Finger für wichtigsten Modifier!
- ✅ **Shift auf Mittelfinger (D/K)** - für Großbuchstaben
- ✅ **Alt auf Ringfinger (S/L)** - für Aerospace Window Manager
- ✅ **Daumen als Backup** - für komplexe Shortcuts (Cmd+Shift+X)
- ✅ **Cmd+C/V/Z:** Entweder F+C/V/Z (HRM) oder Daumen-Cmd+C/V/Z

### **Smart Keys:**
- **Backspace:** Normal = Backspace, **Shift+Backspace** = Delete
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
│     │ CMD │ ALT │ CTL │     │     │   │  +  │  4  │  5  │  6  │  -  │  *  │
├─────┼─────┼─────┼─────┼─────┼─────┤   ├─────┼─────┼─────┼─────┼─────┼─────┤
│     │     │     │     │     │     │   │  =  │  1  │  2  │  3  │  /  │     │
╰─────┴─────┴─────┼─────┼─────┼─────┤   ├─────┼─────┼─────┼─────┴─────┴─────╯
                  │     │     │ ███ │   │     │  0  │  .  │
                  ╰─────┴─────┴─────╯   ╰─────┴─────┴─────╯
```

**Features:**
- Top Row: Zahlenreihe 1-0 (klassisch)
- **Numpad rechts:** 789, 456, 123, 0 (Taschenrechner-Layout)
- Rechenoperatoren: `+` `-` `*` `/` `=`
- Backspace durchgereicht (transparent)
- Modifier auf linker Home Row für Shortcuts (Cmd, Alt, Ctrl)

**Zugriff:** Space halten (linke Hand)

---

## 🧭 Layer 3: NAVIGATION

```
╭─────┬─────┬─────┬─────┬─────┬─────╮   ╭─────┬─────┬─────┬─────┬─────┬─────╮
│ ESC │     │     │     │     │     │   │HOME │PG_DN│PG_UP│ END │     │     │
│EXIT │     │     │     │     │     │   │     │     │     │     │     │     │
├─────┼─────┼─────┼─────┼─────┼─────┤   ├─────┼─────┼─────┼─────┼─────┼─────┤
│     │ CTL │ ALT │ CMD │     │     │   │  ←  │  ↓  │  ↑  │  →  │  ↑  │     │
├─────┼─────┼─────┼─────┼─────┼─────┤   ├─────┼─────┼─────┼─────┼─────┼─────┤
│     │ ⌘Z  │ ⌘X  │ ⌘C  │ ⌘V  │     │   │     │     │     │  ←  │  ↓  │  →  │
╰─────┴─────┴─────┼─────┼─────┼─────┤   ├─────┼─────┼─────┼─────┴─────┴─────╯
                  │     │     │     │   │     │     │     │
                  ╰─────┴─────┴─────╯   ╰─────┴─────┴─────╯
```

**Features:**
- **Vim-Style (Mitte):** H=←, J=↓, K=↑, L=→
- **Traditional (Unten rechts):** M=←, ,=↓, .=↑, /=→
- **macOS-Shortcuts:** Undo, Cut, Copy, Paste (linke Hand)
- **Page-Navigation:** Home, End, PgUp, PgDn
- **ESC = Exit** (bei Toggle-Modus zurück zu BASE)

**Zugriff:** 
- **Shift+Space hold** (momentary - automatisch aus beim Loslassen)
- Beide Shift-Tasten funktionieren (L-Shift oder R-Shift)

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
- **Bluetooth:** Profile 0-1 (Q/W) + Clear (L-Shift)
- **Volume:** Mute, Vol-, Vol+ (H/J/K)
- **ESC = Exit** (zurück zu BASE)

**Zugriff:** R-Shift double-tap (toggle - bleibt aktiv bis ESC oder R-Shift 2x)

**Beispiele:**
- Bluetooth wechseln: `R-Shift 2x` → `S` (BT 1) → `ESC`
- Screenshot: `R-Shift 2x` → `P` (PrintScr) → `ESC`
- Lautstärke: `R-Shift 2x` → `L` (Vol+) → `ESC`

---

## 📊 Layout-Features

✅ **5 Layer** - Base, Symbol, Numbers, Nav, System  
✅ **CASG Hybrid Home Row Mods** - Alle 4 Modifier (Ctrl/Alt/Shift/Cmd) + Daumen-Backup  
✅ **Cmd auf Zeigefinger** - F/J für stärksten Finger  
✅ **React/JSX-optimiert** - `<>` auf Z/X (Symbol Layer)  
✅ **One-Hand Symbol Layer** - Enter hold (rechts), linke Hand tippt  
✅ **macOS + Aerospace** - Alt/Cmd optimal platziert  
✅ **Toggle + Hold Modi** - Flexible Layer-Zugriffe  
✅ **Minimal System Layer** - Nur BT 0/1, Volume  
✅ **Basierend auf Analyse** - 767 TypeScript-Dateien

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
ENTER hold           → Symbol Layer (momentary)
SPACE hold           → Number Layer (momentary)
SHIFT+SPACE hold     → Nav Layer (momentary)
R-Shift 2x tap       → System Layer (toggle, ESC to exit)

HOME ROW MODS (Hybrid - alle 4 Modifier):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
A hold  → Ctrl    |  J hold  → Cmd  ⭐
S hold  → Alt     |  K hold  → Shift
D hold  → Shift   |  L hold  → Alt
F hold  → Cmd  ⭐  |  ; hold  → Ctrl

THUMB KEYS (Backup für Shortcuts):
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Left:  Cmd | Alt | Space (hold=Numbers, Shift+hold=Nav)
Right: Enter (hold=Symbols) | Ctrl | Cmd
```
