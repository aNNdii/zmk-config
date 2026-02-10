# 🚀 Quick Start: TypeScript-optimierte Layouts

## Übersicht

Sie haben jetzt **1 optimierte Keymap**:

1. **`corne.keymap`** - TypeScript-optimiert mit CAG Home Row Mods ⭐

---

## ⚡ Sofort loslegen (2 Minuten)

Ihr TypeScript-optimiertes Layout ist bereits in `corne.keymap` aktiv!

```bash
# Committen und pushen
git add config/corne.keymap
git commit -m "feat: TypeScript-optimized layout with CAG HRM"
git push
```

---

## 📥 Firmware flashen

1. **GitHub Actions aufrufen:**
   - https://github.com/DEIN_USERNAME/zmk-config/actions
   - Warten bis Build fertig ist (~2-3 Minuten)

2. **Firmware herunterladen:**
   - Klick auf den neuesten erfolgreichen Workflow
   - Download `firmware.zip`
   - Entpacken

3. **Flashen:**
   - **Linke Hälfte:**
     - Reset-Button drücken (Bootloader-Modus)
     - `corne-left.uf2` auf das Laufwerk kopieren
   - **Rechte Hälfte:**
     - Reset-Button drücken
     - `corne-right.uf2` auf das Laufwerk kopieren

4. **Fertig!** Keyboard neu starten.

---

## 🎹 Wichtigste Shortcuts für TypeScript

### Combos (automatisch in beiden Layouts)

| Tasten | Output | Verwendung |
|--------|--------|------------|
| D+F | `=>` | Arrow Functions |
| S+D | `()` | Leere Klammern (Cursor innen) |
| J+K | `{}` | Leere geschweifte Klammern |
| K+L | `[]` | Leere eckige Klammern |

### Layer-Switching

| Daumen-Taste | Funktion |
|--------------|----------|
| **Mitte Links (Space halten)** | Symbol Layer |
| **Mitte Rechts (Enter halten)** | Symbol Layer |
| **Links außen** | Navigation Layer |
| **Rechts außen** | Number Layer |

### Wichtigste Zeichen im Symbol Layer

Mit **Space** oder **Enter** halten:

```
Linke Hand:
  -  =  [  ]  (für => Arrow Functions!)
  _  +  {  }

Rechte Hand:
  /  :  ;  .  ,  (die häufigsten!)
  ?  <  >
```

---

## 🎓 Erste Schritte (Tag 1)

### Tipp 1: Langsam anfangen
- **Nicht** sofort produktiv arbeiten!
- Erste 2-3 Tage: Übungs-Sessions 20-30 Min
- [monkeytype.com](https://monkeytype.com) für Tipp-Übungen

### Tipp 2: Home Row Mods lernen (nur mit HRM)

**Linke Hand (CAG-Layout):**
- A halten = Ctrl
- S halten = Alt  
- D halten = Cmd ⭐ (wichtigster!)
- F = Normal (kein Modifier)

**Rechte Hand:**
- J = Normal (kein Modifier)
- K halten = Alt
- L halten = Cmd ⭐ (wichtigster!)
- ; halten = Ctrl

**Shift:** Dedizierte Tasten unten links/rechts ✅

**Üben Sie:**
```typescript
// Cmd+C (Copy): Halte D, drücke C
// Cmd+V (Paste): Halte D, drücke V
// Cmd+Z (Undo): Halte D, drücke Z
// Cmd+S (Save): Halte D, drücke S (gleiche Hand!)
```

### Tipp 3: Combos üben

Öffnen Sie VS Code und tippen Sie:

```typescript
// Arrow Function (D+F gleichzeitig)
const foo = () => {
  // Leere Klammern (S+D gleichzeitig)
  console.log()
  
  // Geschweifte Klammern (J+K gleichzeitig)
  const obj = {}
}
```

---

## 🔄 Zurück zum alten Layout

Falls Sie zurück zur Original-Konfiguration möchten:

```bash
# Original wiederherstellen
cp config/corne.keymap.backup config/corne.keymap

# Oder manuell zurücksetzen
git checkout HEAD -- config/corne.keymap

# Committen
git add config/corne.keymap
git commit -m "Revert to original layout"
git push
```

---

## 📊 Was ist anders?

### Hauptunterschiede zu Ihrer alten Config

#### Alte Config:
- 4 Layer (qwerty, numbers, navi, system)
- Sticky Keys für Modifier
- Numbers-Layer: Sonderzeichen oben, Zahlen 1-0 auf linker Hand
- Navigation: Home/End/PgUp/PgDn auf linker Hand

#### Neue Config (TypeScript-optimiert):
- 5 Layer (base, symbol, numbers, nav, function)
- Home Row Mods (optional) ODER Daumen-Modifier
- **Symbol-Layer nach Häufigkeit:** `.` `:` `;` `,` prominent
- **Numbers-Layer:** Zahlen 1-0 oben + Numpad rechts
- **6 Combos** für häufigste TypeScript-Patterns
- Navigation: Vim-style HJKL + macOS-Shortcuts (Cmd+C/V/Z)
- **Function-Layer:** F-Keys + Bluetooth + Media

---

## ⚙️ Anpassungen vornehmen

### Combos deaktivieren

Wenn Sie keine Combos möchten, kommentieren Sie diese aus:

```c
// Arrow Function => (1,878 Vorkommen)
/*
combo_arrow {
    timeout-ms = <50>;
    key-positions = <15 16>;
    bindings = <&arrow_macro>;
    layers = <0>;
};
*/
```

### HRM-Timing anpassen

Falls Modifier zu schnell/langsam triggern:

```c
hm_l: homerow_mods_left {
    tapping-term-ms = <250>;      // Standard: 200ms
    quick-tap-ms = <200>;          // Standard: 175ms
    require-prior-idle-ms = <200>; // Standard: 150ms
    // ...
};
```

**Höher = langsamer, weniger versehentliche Modifier**

---

## 🆘 Hilfe & Troubleshooting

### Build schlägt fehl

1. **Syntax-Fehler prüfen:**
   ```bash
   # GitHub Actions Log ansehen
   # Häufigste Fehler: fehlende Semikolons, falsche Klammern
   ```

2. **Auf Standard-Layout zurückfallen:**
   ```bash
   git checkout HEAD~1 config/corne.keymap
   git push
   ```

### Combos funktionieren nicht

**Lösung:** `config/corne.conf` prüfen:

```ini
CONFIG_ZMK_COMBO_MAX_COMBOS_PER_KEY=16
CONFIG_ZMK_COMBO_MAX_KEYS_PER_COMBO=3
```

### Home Row Mods nervig

**Lösung:** Wechseln Sie zur Variante ohne HRM:

```bash
cp config/corne_typescript_no_hrm.keymap config/corne.keymap
git add . && git commit -m "Switch to no-HRM variant" && git push
```

---

## 📈 Fortschritt tracken

### Woche 1
- [ ] Layout geflasht
- [ ] Basis-Typing funktioniert
- [ ] Home Row Mods ohne nachzudenken
- [ ] Symbol-Layer verinnerlicht

### Woche 2  
- [ ] Combos automatisch
- [ ] 60% der alten Geschwindigkeit
- [ ] Produktiv arbeiten möglich

### Woche 3-4
- [ ] 80-90% der alten Geschwindigkeit
- [ ] Weniger Finger-Ermüdung
- [ ] Kein Zurück mehr zum alten Layout!

---

## 🎯 Nächste Schritte

1. **Jetzt:** Layout aktivieren (5 Min)
2. **Heute:** 20-30 Min Tipp-Übungen
3. **Diese Woche:** Täglich 1-2h damit arbeiten
4. **Nach 2 Wochen:** Evaluieren & ggf. anpassen

---

## 📚 Vollständige Dokumentation

Für Details zu allen Layern, Design-Entscheidungen und Statistiken:

👉 **[TYPESCRIPT_LAYOUTS.md](TYPESCRIPT_LAYOUTS.md)**

---

Viel Erfolg! Bei Fragen: Issue erstellen oder mich kontaktieren. 🚀
