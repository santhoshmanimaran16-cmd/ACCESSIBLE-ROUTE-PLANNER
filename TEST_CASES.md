# Test cases (run each with Wheelchair, Elderly, Visually impaired, Normal)

| ID | Start | Destination | Notes |
|----|-------|-------------|-------|
| T0 | (use the **Run offline demo** button, works without internet) | built-in test town | No internet needed |
| T1 | NIT Trichy | Trichy Central Bus Stand | Manual address entry |
| T2 | Chennai Central Railway Station | Marina Beach, Chennai | Long urban route |
| T3 | Sri Ranganathaswamy Temple, Srirangam | Rockfort, Trichy | Trichy local — ✅ verified working |
| T4 | 10.8050, 78.6856 | 10.7905, 78.7047 | Coordinate input (direct lat,lng) — ✅ verified working |

Expected in T0: Wheelchair/Elderly = 992 m, 0 stairs; Normal/Visually impaired = 934 m, 1 stairs.

## Tips
- If geocoding fails for a name, type coordinates directly: `10.8050, 78.6856`
- T2/T3 require internet (Nominatim + Overpass). If Overpass returns a 502/504 error, wait 1–2 minutes and retry.
- Click "Log this result" after each run, then "CSV" to download all results.

## Barrier colour legend (on map)
- 🟢 Green solid line = accessible route segment
- 🔴 Red dashed line = stairs / steps (highway=steps)
- 🟠 Orange dashed line = steep slope (incline >= 8%)
