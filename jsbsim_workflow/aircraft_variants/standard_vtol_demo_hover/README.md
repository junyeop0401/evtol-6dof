# standard_vtol_demo_jsbsim

JSBSim standalone conversion of `standard_vtol_demo.xml`.

- `standard_vtol_demo.xml`: default model installed to JSBSim, using DATCOM aero from `jsbsim_aerodynamic_database.xml`.
- `standard_vtol_demo_datcom_aero.xml`: same DATCOM-aero model, kept as explicit variant.
- `standard_vtol_demo_demo_aero.xml`: same JSBSim standalone motor/FCS setup with the original demo aerodynamic block.
- `Aero_DATCOM.xml` and `Aero_Demo.xml`: extracted aero blocks for inspection and manual swapping.

Motor command path for JSBSim-only checks:

`fcs/esc-cmd-norm[0..4] -> fcs/motor-armed -> fcs/esc-cmd-armed[0..4] -> fcs/esc-out[0..4] -> external_reactions`

The default `fcs/motor-armed` value is `0.0`, so all five motors remain blocked until a JSBSim script sets it to `1.0`.
