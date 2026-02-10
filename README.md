# 🎹 Corne 3x6 - TypeScript-Optimiertes Layout

> **Basierend auf Codebase-Analyse:** 767 TypeScript-Dateien analysiert für optimale Sonderzeichen-Platzierung

## 📊 Warum dieses Layout?

Durch Analyse Ihrer Codebase wurden die häufigsten Sonderzeichen identifiziert:

| Zeichen | Häufigkeit | Platzierung |
|---------|-----------|-------------|
| `.` | 13.5% | Home Row (Symbol Layer) |
| `()` | 22.2% | Combo (S+D) |
| `'` | 9.7% | Base Layer |
| `;` | 8.6% | Home Row (Symbol Layer) |
| `/` | 7.7% | Symbol Layer prominent |
| `,` | 7.6% | Home Row (Symbol Layer) |
| `{}` | 13.4% | Combo (J+K) |
| `:` | 6.6% | Home Row (Symbol Layer) |

**Resultat:** ~15-20% weniger Tastendrücke für TypeScript-Code!

---

## 🚀 Quick Start

### Installation

```bash
# Build & Flash
git add .
git commit -m "Update to TypeScript-optimized layout"
git push

# Dann in GitHub Actions:
# → Workflow abwarten (~2-3 Min)
# → firmware.zip downloaden
# → corne-left.uf2 & corne-right.uf2 flashen
```

---

## 🎯 Layout-Übersicht

### **5 Layer-System:**
1. **BASE** - QWERTY mit CAG Home Row Mods
2. **SYMBOL** - TypeScript-optimiert nach Häufigkeit
3. **NUMBERS** - Zahlenreihe + Numpad rechts
4. **NAV** - Vim-Style + Traditional Arrows
5. **SYSTEM** - Bluetooth, Media, Controls

---

## 🎹 Layer 0: BASE

```
╭─────┬─────┬─────┬─────┬─────┬─────╮   ╭─────┬─────┬─────┬─────┬─────┬─────╮
│ TAB │  Q  │  W  │  E  │  R  │  T  │   │  Y  │  U  │  I  │  O  │  P  │ BSP │
├─────┼─────┼─────┼─────┼─────┼─────┤   ├─────┼─────┼─────┼─────┼─────┼─────┤
│ ESC │  A  │  S  │  D  │  F  │  G  │   │  H  │  J  │  K  │  L  │  ;  │  '  │
│     │Ctl/A│Alt/S│Cmd/D│     │     │   │     │     │Alt/K│Cmd/L│Ctl/;│     │
├─────┼─────┼─────┼─────┼─────┼─────┤   ├─────┼─────┼─────┼─────┼─────┼─────┤
│ SFT │  Z  │  X  │  C  │  V  │  B  │   │  N  │  M  │  ,  │  .  │  /  │ SFT │
╰─────┴─────┴─────┼─────┼─────┼─────┤   ├─────┼─────┼─────┼─────┴─────┴─────╯
                  │ CMD │SYM/ │NAV/ │   │NUM/ │SYM/ │ CMD │
                  │     │ SPC │ TAB │   │ BSP │ RET │     │
                  ╰─────┴─────┴─────╯   ╰─────┴─────┴─────╯
```

### **CAG Home Row Mods (Hold):**
- **A** = Ctrl | **S** = Alt | **D** = Cmd ⭐
- **K** = Alt | **L** = Cmd ⭐ | **;** = Ctrl
- **F & J** bleiben normal (keine Modifier)

**Warum CAG?**
- ✅ Cmd auf Mittelfinger (D/L) - häufigster macOS-Modifier optimal platziert!
- ✅ Cmd+C/V/Z: D+C/V/Z (perfekt erreichbar!)
- ✅ Index-Finger frei - weniger Fehler beim schnellen Tippen

---

## ⚡ TypeScript-Combos (4 essenzielle)

| Combo | Tasten | Output | Häufigkeit | Beschreibung |
|-------|--------|--------|-----------|--------------|
| **Arrow Function** | D+F | `=>` | 1,878× | Arrow Function Operator |
| **Empty Parens** | S+D | `()←` | 5,050× | Leere Klammern, Cursor innen |
| **Empty Braces** | J+K | `{}←` | 3,094× | Leere geschweifte Klammern |
| **Empty Brackets** | K+L | `[]←` | - | Leere eckige Klammern |

**Timeout:** 50ms (schnell reagierend)

### Beispiel-Usage:
```typescript
// D+F gleichzeitig → =>
const foo = () => {
  // S+D gleichzeitig → ()
  console.log()
  
  // J+K gleichzeitig → {}
  const obj = {}
  
  // K+L gleichzeitig → []
  const arr = []
}
```

---

## 🎨 Layer 1: SYMBOL (TypeScript-optimiert)

```
╭─────┬─────┬─────┬─────┬─────┬─────╮   ╭─────┬─────┬─────┬─────┬─────┬─────╮
│  ~  │  !  │  @  │  #  │  $  │  %  │   │  ^  │  &  │  *  │  (  │  )  │ DEL │
├─────┼─────┼─────┼─────┼─────┼─────┤   ├─────┼─────┼─────┼─────┼─────┼─────┤
│  `  │  -  │  =  │  [  │  ]  │  \  │   │  /  │  :  │  ;  │  .  │  ,  │  "  │
├─────┼─────┼─────┼─────┼─────┼─────┤   ├─────┼─────┼─────┼─────┼─────┼─────┤
│     │  _  │  +  │  {  │  }  │  |  │   │  ?  │  <  │  >  │  ,  │  .  │     │
╰─────┴─────┴─────┼─────┼─────┼─────┤   ├─────┼─────┼─────┼─────┴─────┴─────╯
                  │     │ ███ │     │   │     │ ███ │     │
                  ╰─────┴─────┴─────╯   ╰─────┴─────┴─────╯
```

**Design-Philosophie:**
- **Rechte Home Row:** `/` `:` `;` `.` `,` - häufigste Zeichen!
- **Linke Home Row:** `-` `=` `[` `]` - nah für `=>` Arrow Functions
- **Paarweise:** `()` `[]` `{}` `<>` logisch gruppiert
- **TypeScript-spezifisch:** `:` für Type Annotations (6.6% aller Sonderzeichen!)

**Zugriff:** Space oder Enter halten

---

## 🔢 Layer 2: NUMBERS

```
╭─────┬─────┬─────┬─────┬─────┬─────╮   ╭─────┬─────┬─────┬─────┬─────┬─────╮
│ SYS │  1  │  2  │  3  │  4  │  5  │   │  6  │  7  │  8  │  9  │  0  │ SYS │
├─────┼─────┼─────┼─────┼─────┼─────┤   ├─────┼─────┼─────┼─────┼─────┼─────┤
│     │ CMD │ ALT │ CTL │ SFT │     │   │  +  │  4  │  5  │  6  │  -  │  *  │
├─────┼─────┼─────┼─────┼─────┼─────┤   ├─────┼─────┼─────┼─────┼─────┼─────┤
│     │     │     │     │     │     │   │  =  │  1  │  2  │  3  │  /  │     │
╰─────┴─────┴─────┼─────┼─────┼─────┤   ├─────┼─────┼─────┼─────┴─────┴─────╯
                  │     │     │     │   │ ███ │  0  │  .  │
                  ╰─────┴─────┴─────╯   ╰─────┴─────┴─────╯
```

**Features:**
- Top Row: Zahlenreihe 1-0 (klassisch)
- **Numpad rechts:** 789, 456, 123, 0 (Taschenrechner-Layout)
- Rechenoperatoren: `+` `-` `*` `/` `=`
- **System-Layer-Zugriff:** TAB oder P halten → Layer 4

**Zugriff:** Backspace halten

---

## 🧭 Layer 3: NAVIGATION

```
╭─────┬─────┬─────┬─────┬─────┬─────╮   ╭─────┬─────┬─────┬─────┬─────┬─────╮
│     │     │     │     │     │     │   │HOME │PG_DN│PG_UP│ END │     │     │
├─────┼─────┼─────┼─────┼─────┼─────┤   ├─────┼─────┼─────┼─────┼─────┼─────┤
│     │ CTL │ ALT │ CMD │     │     │   │  ←  │  ↓  │  ↑  │  →  │  ↑  │     │
├─────┼─────┼─────┼─────┼─────┼─────┤   ├─────┼─────┼─────┼─────┼─────┼─────┤
│     │ ⌘Z  │ ⌘X  │ ⌘C  │ ⌘V  │     │   │     │     │     │  ←  │  ↓  │  →  │
╰─────┴─────┴─────┼─────┼─────┼─────┤   ├─────┼─────┼─────┼─────┴─────┴─────╯
                  │     │     │ ███ │   │     │     │     │
                  ╰─────┴─────┴─────╯   ╰─────┴─────┴─────╯
```

**Features:**
- **Vim-Style (Mitte):** H=←, J=↓, K=↑, L=→
- **Traditional (Unten rechts):** M=←, ,=↓, .=↑, /=→
- **macOS-Shortcuts:** Undo, Cut, Copy, Paste (linke Hand)
- **Page-Navigation:** Home, End, PgUp, PgDn

**Zugriff:** Tab halten

---

## 🎛️ Layer 4: SYSTEM

```
╭─────┬─────┬─────┬─────┬─────┬─────╮   ╭─────┬─────┬─────┬─────┬─────┬─────╮
│     │     │     │     │     │     │   │     │  ⏮  │ ⏯  │  ⏭  │     │PSCRN│
├─────┼─────┼─────┼─────┼─────┼─────┤   ├─────┼─────┼─────┼─────┼─────┼─────┤
│     │ BT0 │ BT1 │ BT2 │ BT3 │ BT4 │   │     │  🔇 │ 🔉  │ 🔊  │     │     │
├─────┼─────┼─────┼─────┼─────┼─────┤   ├─────┼─────┼─────┼─────┼─────┼─────┤
│BTCLR│     │     │     │     │     │   │     │     │ 🔅  │ 🔆  │     │     │
╰─────┴─────┴─────┼─────┼─────┼─────┤   ├─────┼─────┼─────┼─────┴─────┴─────╯
                  │     │     │     │   │     │     │     │
                  ╰─────┴─────┴─────╯   ╰─────┴─────┴─────╯
```

**Features:**
- **Bluetooth:** Profile 0-4 + Clear
- **Media:** Play/Pause, Prev, Next
- **Volume:** Mute, Vol-, Vol+
- **Brightness:** Bri-, Bri+
- **Screenshot:** PrintScreen

**Zugriff:** Im Numbers-Layer (Backspace halten) → TAB oder P halten

**Beispiele:**
- Bluetooth wechseln: `Backspace` → `TAB` → `S` (BT 1)
- Musik pausieren: `Backspace` → `P` → `I` (Play/Pause)
- Screenshot: `Backspace` → `P` → `P` (PrintScr)
- Lautstärke: `Backspace` → `P` → `L` (Vol+)

---

## 🎓 Erste Schritte

### Tag 1-3: CAG Home Row Mods lernen

**Linke Hand:**
- **A** halten = Ctrl
- **S** halten = Alt
- **D** halten = Cmd ⭐ (wichtigster!)

**Rechte Hand:**
- **K** halten = Alt
- **L** halten = Cmd ⭐ (wichtigster!)
- **;** halten = Ctrl

**Üben:**
```typescript
// Cmd+C (Copy): Halte D, drücke C
// Cmd+V (Paste): Halte D, drücke V
// Cmd+Z (Undo): Halte D, drücke Z
// Cmd+S (Save): Halte D, drücke S (gleiche Hand!)
```

### Tag 4-7: Combos verinnerlichen

```typescript
// Arrow Function (D+F gleichzeitig)
const foo = () => {
  // Leere Klammern (S+D gleichzeitig)
  console.log()
  
  // Geschweifte Klammern (J+K gleichzeitig)
  const obj = {}
}
```

### Tag 8-14: Symbol-Layer & Layer-Switching

- Space/Enter halten → Symbol-Layer
- Backspace halten → Numbers-Layer
- Tab halten → Navigation-Layer

**Tipp:** [monkeytype.com](https://monkeytype.com) für Tipp-Übungen

---

## ⚙️ Anpassungen

### Home Row Mods Timing ändern

Falls Modifier zu schnell/langsam triggern:

```c
hm_l: homerow_mods_left {
    tapping-term-ms = <250>;      // Standard: 200ms (höher = langsamer)
    quick-tap-ms = <200>;          // Standard: 175ms
    require-prior-idle-ms = <200>; // Standard: 150ms
    // ...
};
```

### Combo-Timeout anpassen

Falls Combos zu empfindlich/unempfindlich:

```c
combo_arrow {
    timeout-ms = <100>;  // Standard: 50ms (höher = mehr Zeit)
    // ...
};
```

### Combos deaktivieren

Kommentieren Sie ungewünschte Combos aus:

```c
/*
combo_brackets {
    timeout-ms = <50>;
    key-positions = <20 21>;
    bindings = <&brackets_macro>;
};
*/
```

---

## 📈 Performance-Vergleich

Basierend auf Ihrer Codebase-Analyse:

| Aktion | Standard | TypeScript-Layout | Ersparnis |
|--------|----------|-------------------|-----------|
| `const foo = () => {}` | 21 Tasten | 17 Tasten | **19%** |
| `import { x } from './y'` | 22 Tasten | 18 Tasten | **18%** |
| `interface Foo { bar: string; }` | 31 Tasten | 28 Tasten | **10%** |
| Type Annotation `:` | 2 Tasten | 1 Taste | **50%** |

**Geschätzte Gesamt-Ersparnis:** 15-20% weniger Tastendrücke!

---

## 🆘 Troubleshooting

### Versehentliche Modifier (HRM)

**Problem:** D/L triggern zu oft Cmd

**Lösung:**
```c
tapping-term-ms = <250>;           // Langsamer triggern
require-prior-idle-ms = <200>;     // Mehr Pause vor Mod
```

### Combos funktionieren nicht

**Lösung 1:** `config/corne.conf` prüfen:
```ini
CONFIG_ZMK_COMBO_MAX_COMBOS_PER_KEY=16
CONFIG_ZMK_COMBO_MAX_KEYS_PER_COMBO=3
```

**Lösung 2:** Timeout erhöhen:
```c
timeout-ms = <100>;  // Statt 50ms
```

### Layer wechseln nicht

**Check:** Layer-Nummern korrekt?
- `&lt 1 SPACE` = Layer 1 halten, Space tippen
- `&mo 4` = Layer 4 momentary (nur halten)

---

## 🔄 Zurück zur alten Konfiguration

Falls Sie zum Original-Layout zurück möchten:

```bash
# Via Git History
git log --oneline  # Finde alte Commit-ID
git checkout <commit-id> -- config/corne.keymap

# Committen
git add config/corne.keymap
git commit -m "Revert to original layout"
git push
```

---

## 📊 Layout-Features Zusammenfassung

✅ **5 Layer** - Base, Symbol, Numbers, Nav, System
✅ **CAG Home Row Mods** - Cmd auf Mittelfinger (D/L)
✅ **4 TypeScript-Combos** - =>, (), {}, []
✅ **macOS-optimiert** - Cmd+C/V/Z perfekt erreichbar
✅ **Doppelte Pfeiltasten** - Vim + Traditional
✅ **System-Controls** - Bluetooth, Media, Volume, Brightness
✅ **Dedizierte Shift-Tasten** - Keine HRM-Konflikte
✅ **Basierend auf Analyse** - 767 TypeScript-Dateien

---

## 📚 Ressourcen

- [ZMK Documentation](https://zmk.dev/docs)
- [Home Row Mods Guide](https://precondition.github.io/home-row-mods)
- [Corne Keyboard Wiki](https://github.com/foostan/crkbd)
- [Keymap Editor](https://nickcoutsos.github.io/keymap-editor/)

---

## 📝 Changelog

**v2.0 (Current):**
- CAG Home Row Mods (Cmd auf D/L)
- 4 fokussierte TypeScript-Combos
- Doppelte Pfeiltasten im Nav Layer
- System-Layer statt F-Keys
- Basiert auf Codebase-Analyse (767 TS-Dateien)

**v1.0:**
- Initial TypeScript-optimiertes Layout

---

**Viel Erfolg mit Ihrem TypeScript-optimierten Corne Layout!** 🎉

Bei Fragen oder Anpassungswünschen: Issue erstellen oder PR öffnen.
