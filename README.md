# Solar Assisted Hollow Cylinder Paddy Dryer

![Status](https://img.shields.io/badge/status-preliminary%20design-blue)
![University](https://img.shields.io/badge/Jadavpur%20University-ME%204.1-navy)
![Licence](https://img.shields.io/badge/licence-MIT-lightgrey)

Jadavpur University, Department of Mechanical Engineering  
Major project 4.1, Semester 7  
Parth Pariwandh, Roll 002311201078, Registration 16600007, Section A3  
Supervisor: Prof. Dulal Krishna Mandal  
Status date: 29 October 2026

This repository holds the design notes, the sizing code, and the progress record for the modified solar assisted hollow cylinder paddy dryer. It is a preliminary design. No prototype has been cut, and no drying rate has been measured.

## What the dryer is

Paddy sits in an annulus between a dark outer absorber and a perforated inner shell. Clean air enters a bottom plenum from a blower and a controllable heater, rises through the bed, and leaves at a top hood. Solar heat falls on the outer wall when the sun is available. A separate biomass chamber can warm the same clean air across a duct wall. Flue gas does not meet the grain. Direct fire under the cylinder is not part of the design.

## Two scales, kept separate

| Case | Batch | Shells | Air |
| --- | --- | --- | --- |
| Laboratory concept | about 24 kg | 400 mm / 220 mm | about 28 m3/h, first trial 40 to 45 C |
| One quintal case | 100 kg | about 670 mm / 250 mm | about 61 m3/h, 80 C is an alternate sum only |

The first trial air target is 40 to 45 C. Grain temperature is to stay below about 50 C. The 80 C figure is an alternate calculation of blower air. It is not a grain temperature and it is not the first trial setpoint.

## Carried numbers, 9 October and 29 October

For 100 kg from 22 percent to 14 percent wet basis:

- Water removed: 9.30 kg
- Dry solid: 78 kg
- Final grain mass: 90.7 kg
- Bed volume at 560 kg/m3: 0.179 m3
- Humidity pickup, assumed: 0.0253 kg/kg
- Dry air flow over 6 hours: 0.0170 kg/s, about 61 m3/h
- Superficial velocity: 0.057 m/s
- Useful heat: 24.9 MJ
- Average heater with 50 percent loss allowance: 1.7 kW
- Extra to heat air from 30 C to 80 C: 0.85 kW
- Heater rating is not frozen
- Bed pressure drop, Ergun order: about 65 Pa
- Fair sun on the wall: about 220 W

Run the numbers:

```bash
python design/sizing.py
```

## Layout

```
design/sizing.py     one quintal sizing, written out
design/NOTES.md      symbols, materials, open decisions
STATUS.md            progress as of 29 October 2026
```

## Open decisions

1. One air temperature strategy: 40 to 45 C for the first trial, with an independent cut out.
2. A consistent heater balance, so that the 1.7 kW and the 0.85 kW are not added twice.
3. Which scale is to be built: the 24 kg laboratory shell, or a later quintal shell.

## Licence

MIT. Estimates only. Not a tested plant.
