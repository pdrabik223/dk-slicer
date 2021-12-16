; generated by PrusaSlicer 2.3.3+win64 on 2021-12-16 at 18:47:43 UTC

; 

; external perimeters extrusion width = 0.45mm
; perimeters extrusion width = 0.45mm
; infill extrusion width = 0.45mm
; solid infill extrusion width = 0.45mm
; top infill extrusion width = 0.40mm
; first layer extrusion width = 0.42mm

M73 P0 R0
M73 Q0 S0
M201 X1000 Y1000 Z200 E5000 ; sets maximum accelerations, mm/sec^2
M203 X200 Y200 Z12 E120 ; sets maximum feedrates, mm/sec
M204 P1250 R1250 T1250 ; sets acceleration (P, T) and retract acceleration (R), mm/sec^2
M205 X8.00 Y8.00 Z0.40 E4.50 ; sets the jerk limits, mm/sec
M205 S0 T0 ; sets the minimum extruding and travel feed rate, mm/sec
M107
;TYPE:Custom
M862.3 P "MK3S" ; printer model check
M862.1 P0.4 ; nozzle diameter check
M115 U3.10.0 ; tell printer latest fw version
G90 ; use absolute coordinates
M83 ; extruder relative mode
M104 S220 ; set extruder temp
M140 S60 ; set bed temp
M190 S60 ; wait for bed temp
M109 S220 ; wait for extruder temp
G28 W ; home all without mesh bed level
G80 ; mesh bed leveling
G1 Y-3.0 F1000.0 ; go outside print area
G92 E0.0
G1 X60.0 E9.0 F1000.0 ; intro line
M73 P14 R0
M73 Q14 S0
G1 X100.0 E12.5 F1000.0 ; intro line
G92 E0.0
M221 S95

; Don't change E values below. Excessive value can damage the printer.

G21 ; set units to millimeters
G90 ; use absolute coordinates
M83 ; use relative distances for extrusion
M900 K0.05 ; Filament gcode LA 1.5
M900 K30 ; Filament gcode LA 1.0
;LAYER_CHANGE
;Z:0.2
;HEIGHT:0.2
;BEFORE_LAYER_CHANGE
G92 E0.0
;0.2


M73 P23 R0
M73 Q23 S0
G1 E-0.80000 F2100.000
G1 Z0.400 F10800.000
;AFTER_LAYER_CHANGE
;0.2
G1 X49.190 Y26.281
M73 P25 R0
M73 Q26 S0
G1 Z0.200
M73 P26 R0
G1 E0.80000 F2100.000
M204 S1000
;TYPE:Skirt
;WIDTH:0.42
G1 F900
G1 X49.621 Y25.697 E0.02274
G1 X50.158 Y25.217 E0.02259
G1 X50.786 Y24.854 E0.02274
M73 Q27 S0
G1 X51.476 Y24.629 E0.02274
G1 X52.169 Y24.551 E0.02187
M73 P27 R0
G1 X57.219 Y24.551 E0.15835
M73 P28 R0
M73 Q28 S0
G1 X58.329 Y24.732 E0.03525
M73 Q29 S0
G1 X59.320 Y25.253 E0.03511
G1 X60.097 Y26.059 E0.03511
M73 P29 R0
G1 X60.580 Y27.069 E0.03511
G1 X60.722 Y27.981 E0.02893
M73 Q30 S0
G1 X60.720 Y33.211 E0.16401
M73 P31 R0
M73 Q31 S0
G1 X60.579 Y34.054 E0.02678
G1 X60.239 Y34.837 E0.02678
G1 X59.758 Y35.475 E0.02505
M73 Q32 S0
G1 X59.146 Y35.988 E0.02505
G1 X58.433 Y36.349 E0.02505
M73 P32 R0
G1 X57.657 Y36.539 E0.02505
G1 X51.993 Y36.560 E0.17761
M73 P33 R0
M73 Q34 S0
G1 X51.184 Y36.412 E0.02577
M73 P34 R0
G1 X50.436 Y36.083 E0.02562
G1 X49.798 Y35.602 E0.02505
G1 X49.286 Y34.990 E0.02505
G1 X48.925 Y34.277 E0.02505
M73 Q35 S0
G1 X48.734 Y33.501 E0.02505
M73 P35 R0
G1 X48.713 Y27.837 E0.17761
M73 P36 R0
M73 Q36 S0
G1 X48.861 Y27.028 E0.02577
G1 X49.166 Y26.335 E0.02374
M73 Q37 S0
G1 X49.230 Y27.112 F10800.000
M73 P37 R0
G1 F900
G1 X49.548 Y26.418 E0.02393
G1 X49.941 Y25.906 E0.02025
G1 X50.435 Y25.483 E0.02039
G1 X51.001 Y25.172 E0.02025
G1 X51.619 Y24.985 E0.02025
M73 Q38 S0
G1 X52.184 Y24.928 E0.01779
M73 P38 R0
G1 X57.219 Y24.928 E0.15788
M73 P39 R0
M73 Q39 S0
G1 X58.219 Y25.093 E0.03180
G1 X59.118 Y25.573 E0.03193
M73 Q40 S0
G1 X59.813 Y26.311 E0.03180
M73 P40 R0
G1 X60.235 Y27.233 E0.03180
G1 X60.345 Y28.002 E0.02434
G1 X60.342 Y33.207 E0.16322
M73 P41 R0
M73 Q42 S0
G1 X60.207 Y33.981 E0.02461
M73 P42 R0
G1 X59.882 Y34.699 E0.02474
G1 X59.446 Y35.256 E0.02216
G1 X58.893 Y35.702 E0.02229
G1 X58.253 Y36.013 E0.02229
M73 Q43 S0
G1 X57.560 Y36.171 E0.02229
G1 X52.014 Y36.184 E0.17389
M73 P44 R0
M73 Q44 S0
G1 X51.268 Y36.044 E0.02379
G1 X50.574 Y35.726 E0.02393
M73 Q45 S0
G1 X50.018 Y35.290 E0.02216
G1 X49.571 Y34.737 E0.02229
M73 P45 R0
G1 X49.261 Y34.097 E0.02229
G1 X49.102 Y33.404 E0.02229
G1 X49.090 Y27.858 E0.17389
M73 P46 R0
M73 Q47 S0
G1 X49.219 Y27.171 E0.02191
M73 P47 R0
G1 X49.590 Y27.243 F10800.000
G1 F900
G1 X49.901 Y26.565 E0.02337
G1 X50.257 Y26.122 E0.01784
G1 X50.696 Y25.761 E0.01784
G1 X51.201 Y25.498 E0.01784
M73 Q48 S0
G1 X51.749 Y25.344 E0.01784
G1 X57.219 Y25.305 E0.17151
M73 P49 R0
M73 Q49 S0
G1 X58.112 Y25.455 E0.02841
G1 X58.912 Y25.890 E0.02854
M73 Q50 S0
G1 X59.524 Y26.558 E0.02841
M73 P50 R0
G1 X59.887 Y27.392 E0.02854
G1 X59.969 Y28.021 E0.01988
G1 X59.965 Y33.198 E0.16232
M73 P51 R0
M73 Q51 S0
G1 X59.837 Y33.902 E0.02243
M73 Q52 S0
G1 X59.529 Y34.552 E0.02256
M73 P52 R0
G1 X59.135 Y35.033 E0.01950
G1 X58.643 Y35.414 E0.01950
G1 X58.078 Y35.674 E0.01950
G1 X57.469 Y35.801 E0.01950
G1 X52.038 Y35.807 E0.17028
M73 P54 R0
M73 Q54 S0
G1 X51.352 Y35.674 E0.02192
G1 X50.721 Y35.373 E0.02192
G1 X50.240 Y34.979 E0.01950
G1 X49.860 Y34.487 E0.01950
G1 X49.599 Y33.922 E0.01950
M73 Q55 S0
G1 X49.472 Y33.313 E0.01950
M73 P55 R0
G1 X49.466 Y27.883 E0.17028
M73 P56 R0
M73 Q56 S0
G1 X49.579 Y27.302 E0.01855
G1 X49.965 Y27.292 F10800.000
G1 F900
G1 X50.247 Y26.724 E0.01989
M73 Q57 S0
G1 X50.563 Y26.349 E0.01538
M73 P57 R0
G1 X50.949 Y26.046 E0.01538
G1 X51.389 Y25.830 E0.01538
G1 X51.864 Y25.708 E0.01538
G1 X57.218 Y25.682 E0.16787
M73 P58 R0
M73 Q58 S0
G1 X58.007 Y25.818 E0.02508
M73 Q59 S0
G1 X58.702 Y26.205 E0.02496
M73 P59 R0
G1 X59.231 Y26.800 E0.02496
G1 X59.534 Y27.536 E0.02496
G1 X59.592 Y28.035 E0.01574
G1 X59.589 Y33.181 E0.16134
M73 P60 R0
M73 Q61 S0
G1 X59.468 Y33.815 E0.02024
M73 P61 R0
G1 X59.182 Y34.393 E0.02024
G1 X58.836 Y34.798 E0.01668
G1 X58.408 Y35.115 E0.01668
G1 X57.917 Y35.330 E0.01680
G1 X57.395 Y35.429 E0.01668
G1 X52.066 Y35.431 E0.16707
M73 P63 R0
M73 Q63 S0
G1 X51.448 Y35.309 E0.01977
G1 X50.880 Y35.026 E0.01989
G1 X50.476 Y34.680 E0.01668
G1 X50.159 Y34.252 E0.01668
G1 X49.944 Y33.762 E0.01680
M73 Q64 S0
G1 X49.844 Y33.239 E0.01668
M73 P64 R0
G1 X49.842 Y27.910 E0.16707
M73 P65 R0
M73 Q65 S0
G1 X49.953 Y27.351 E0.01789
; printing object Body2 id:0 copy 0
;WIPE_START
G1 F8640.000
G1 X50.247 Y26.724 E-0.15985
G1 X50.563 Y26.349 E-0.11325
G1 X50.949 Y26.046 E-0.11325
G1 X51.389 Y25.830 E-0.11325
G1 X51.864 Y25.708 E-0.11325
M73 Q66 S0
G1 X52.502 Y25.705 E-0.14713
;WIPE_END
G1 E-0.04000 F2100.000
M73 P66 R0
G1 Z0.600 F10800.000
G1 X52.803 Y28.647
G1 Z0.200
M73 Q67 S0
G1 E0.80000 F2100.000
;TYPE:External perimeter
M73 P67 R0
G1 F900
G1 X56.626 Y28.647 E0.11986
M73 P68 R0
M73 Q68 S0
G1 X56.626 Y32.470 E0.11986
M73 P69 R0
M73 Q69 S0
G1 X52.803 Y32.470 E0.11986
M73 P70 R0
M73 Q70 S0
G1 X52.803 Y28.707 E0.11798
M73 P71 R0
M73 Q71 S0
G1 X52.700 Y28.261 F10800.000
G1 X52.480 Y28.325
G1 F900
G1 X53.222 Y28.270 E0.02332
G1 X56.209 Y28.270 E0.09364
M73 P72 R0
M73 Q72 S0
G1 X56.952 Y28.321 E0.02337
G1 X57.003 Y29.065 E0.02337
G1 X57.003 Y32.051 E0.09364
M73 P73 R0
M73 Q73 S0
G1 X56.949 Y32.793 E0.02332
G1 X56.207 Y32.847 E0.02332
G1 X53.222 Y32.847 E0.09358
M73 P74 R0
M73 Q74 S0
G1 X52.480 Y32.793 E0.02332
G1 X52.426 Y32.051 E0.02332
G1 X52.426 Y29.066 E0.09358
M73 P75 R0
M73 Q75 S0
G1 X52.476 Y28.384 E0.02144
G1 X52.835 Y28.509 F10800.000
; stop printing object Body2 id:0 copy 0
;WIPE_START
G1 F8640.000;_WIPE
G1 X53.222 Y28.270 E-0.17433
M73 Q76 S0
G1 F8640.000;_WIPE
G1 X55.759 Y28.270 E-0.58567
;WIPE_END
M73 P76 R0
G1 E-0.04000 F2100.000
G1 Z0.600 F10800.000
;TYPE:Custom
; Filament-specific end gcode
G4 ; wait
M221 S100 ; reset flow
M900 K0 ; reset LA

M104 S0 ; turn off temperature
M140 S0 ; turn off heatbed
M107 ; turn off fan
G1 Z30.2 ; Move print head up
M73 P86 R0
M73 Q86 S0
G1 X0 Y200 F3000 ; home X axis
M84 ; disable motors
M73 P100 R0
M73 Q100 S0
; filament used [mm] = 5.85
; filament used [cm3] = 0.01
; filament used [g] = 0.02
; filament cost = 0.00
; total filament used [g] = 0.02
; total filament cost = 0.00
; estimated printing time (normal mode) = 26s
; estimated printing time (silent mode) = 26s

; avoid_crossing_perimeters = 0
; avoid_crossing_perimeters_max_detour = 0
; bed_custom_model = 
; bed_custom_texture = 
; bed_shape = 0x0,250x0,250x210,0x210
; bed_temperature = 60
; before_layer_gcode = ;BEFORE_LAYER_CHANGE\nG92 E0.0\n;[layer_z]\n\n
; between_objects_gcode = 
; bottom_fill_pattern = monotonic
; bottom_solid_layers = 4
; bottom_solid_min_thickness = 0.5
; bridge_acceleration = 1000
; bridge_angle = 0
; bridge_fan_speed = 100
; bridge_flow_ratio = 0.95
; bridge_speed = 30
; brim_width = 0
; clip_multipart_objects = 1
; color_change_gcode = M600\nG1 E0.4 F1500 ; prime after color change
; compatible_printers_condition_cummulative = "printer_notes=~/.*PRINTER_VENDOR_PRUSA3D.*/ and printer_notes=~/.*PRINTER_MODEL_MK3.*/ and nozzle_diameter[0]==0.4";"! (printer_notes=~/.*PRINTER_VENDOR_PRUSA3D.*/ and printer_notes=~/.*PRINTER_MODEL_MK(2.5|3).*/ and single_extruder_multi_material)"
; complete_objects = 1
; cooling = 1
; cooling_tube_length = 5
; cooling_tube_retraction = 91.5
; default_acceleration = 1000
; default_filament_profile = "Prusament PLA"
; default_print_profile = 0.15mm QUALITY @MK3
; deretract_speed = 0
; disable_fan_first_layers = 1
; dont_support_bridges = 0
; draft_shield = 0
; duplicate_distance = 6
; elefant_foot_compensation = 0.2
; end_filament_gcode = "; Filament-specific end gcode"
; end_gcode = G4 ; wait\nM221 S100 ; reset flow\nM900 K0 ; reset LA\n{if print_settings_id=~/.*(DETAIL @MK3|QUALITY @MK3|@0.25 nozzle MK3).*/}M907 E538 ; reset extruder motor current{endif}\nM104 S0 ; turn off temperature\nM140 S0 ; turn off heatbed\nM107 ; turn off fan\n{if max_layer_z < max_print_height}G1 Z{z_offset+min(max_layer_z+30, max_print_height)}{endif} ; Move print head up\nG1 X0 Y200 F3000 ; home X axis\nM84 ; disable motors
; ensure_vertical_shell_thickness = 1
; external_perimeter_extrusion_width = 0.45
; external_perimeter_speed = 25
; external_perimeters_first = 0
; extra_loading_move = -2
; extra_perimeters = 0
; extruder_clearance_height = 20
; extruder_clearance_radius = 20
; extruder_colour = ""
; extruder_offset = 0x0
; extrusion_axis = E
; extrusion_multiplier = 1
; extrusion_width = 0.45
; fan_always_on = 1
; fan_below_layer_time = 100
; filament_colour = #FF8000
; filament_cooling_final_speed = 3.4
; filament_cooling_initial_speed = 2.2
; filament_cooling_moves = 4
; filament_cost = 25.4
; filament_density = 1.24
; filament_diameter = 1.75
; filament_load_time = 0
; filament_loading_speed = 28
; filament_loading_speed_start = 3
; filament_max_volumetric_speed = 15
; filament_minimal_purge_on_wipe_tower = 15
; filament_notes = ""
; filament_ramming_parameters = "120 100 6.6 6.8 7.2 7.6 7.9 8.2 8.7 9.4 9.9 10.0| 0.05 6.6 0.45 6.8 0.95 7.8 1.45 8.3 1.95 9.7 2.45 10 2.95 7.6 3.45 7.6 3.95 7.6 4.45 7.6 4.95 7.6"
; filament_settings_id = "Fiberlogy PLA - Copy"
; filament_soluble = 0
; filament_spool_weight = 0
; filament_toolchange_delay = 0
; filament_type = PLA
; filament_unload_time = 0
; filament_unloading_speed = 90
; filament_unloading_speed_start = 100
; filament_vendor = Fiberlogy
; fill_angle = 45
; fill_density = 15%
; fill_pattern = grid
; first_layer_acceleration = 1000
; first_layer_bed_temperature = 60
; first_layer_extrusion_width = 0.42
; first_layer_height = 0.2
; first_layer_speed = 30
; first_layer_temperature = 220
; full_fan_speed_layer = 4
; gap_fill_speed = 40
; gcode_comments = 0
; gcode_flavor = marlin
; gcode_label_objects = 1
; high_current_on_filament_swap = 0
; host_type = octoprint
; infill_acceleration = 1000
; infill_anchor = 2.5
; infill_anchor_max = 12
; infill_every_layers = 1
; infill_extruder = 1
; infill_extrusion_width = 0.45
; infill_first = 0
; infill_only_where_needed = 0
; infill_overlap = 25%
; infill_speed = 80
; inherits_cummulative = "0.20mm QUALITY @MK3";"Fiberlogy PLA";
; interface_shells = 0
; ironing = 1
; ironing_flowrate = 15%
; ironing_spacing = 0.1
; ironing_speed = 15
; ironing_type = top
; layer_gcode = ;AFTER_LAYER_CHANGE\n;[layer_z]
; layer_height = 0.2
; machine_limits_usage = emit_to_gcode
; machine_max_acceleration_e = 5000,5000
; machine_max_acceleration_extruding = 1250,1250
; machine_max_acceleration_retracting = 1250,1250
; machine_max_acceleration_x = 1000,960
; machine_max_acceleration_y = 1000,960
; machine_max_acceleration_z = 200,200
; machine_max_feedrate_e = 120,120
; machine_max_feedrate_x = 200,100
; machine_max_feedrate_y = 200,100
; machine_max_feedrate_z = 12,12
; machine_max_jerk_e = 4.5,4.5
; machine_max_jerk_x = 8,8
; machine_max_jerk_y = 8,8
; machine_max_jerk_z = 0.4,0.4
; machine_min_extruding_rate = 0,0
; machine_min_travel_rate = 0,0
; max_fan_speed = 100
; max_layer_height = 0.25
; max_print_height = 210
; max_print_speed = 200
; max_volumetric_speed = 0
; min_fan_speed = 100
; min_layer_height = 0.07
; min_print_speed = 15
; min_skirt_length = 4
; notes = 
; nozzle_diameter = 0.4
; only_retract_when_crossing_perimeters = 0
; ooze_prevention = 0
; output_filename_format = {input_filename_base}_{layer_height}mm_{filament_type[0]}_{printer_model}_{print_time}.gcode
; overhangs = 1
; parking_pos_retraction = 92
; pause_print_gcode = M601
; perimeter_acceleration = 800
; perimeter_extruder = 1
; perimeter_extrusion_width = 0.45
; perimeter_speed = 60
; perimeters = 2
; physical_printer_settings_id = 
; post_process = 
; print_settings_id = 0.20mm QUALITY @M3Squality
; printer_model = MK3S
; printer_notes = Don't remove the following keywords! These keywords are used in the "compatible printer" condition of the print and filament profiles to link the particular print and filament profiles to this printer profile.\nPRINTER_VENDOR_PRUSA3D\nPRINTER_MODEL_MK3\n
; printer_settings_id = Original Prusa i3 MK3S & MK3S+
; printer_technology = FFF
; printer_variant = 0.4
; printer_vendor = 
; raft_layers = 0
; remaining_times = 1
; resolution = 0
; retract_before_travel = 1
; retract_before_wipe = 0%
; retract_layer_change = 1
; retract_length = 0.8
; retract_length_toolchange = 4
; retract_lift = 0.4
; retract_lift_above = 0
; retract_lift_below = 209
; retract_restart_extra = 0
; retract_restart_extra_toolchange = 0
; retract_speed = 35
; seam_position = nearest
; silent_mode = 1
; single_extruder_multi_material = 0
; single_extruder_multi_material_priming = 0
; skirt_distance = 2
; skirt_height = 3
; skirts = 1
; slice_closing_radius = 0.049
; slowdown_below_layer_time = 15
; small_perimeter_speed = 25
; solid_infill_below_area = 0
; solid_infill_every_layers = 0
; solid_infill_extruder = 1
; solid_infill_extrusion_width = 0.45
; solid_infill_speed = 80
; spiral_vase = 0
; standby_temperature_delta = -5
; start_filament_gcode = "M900 K{if printer_notes=~/.*PRINTER_MODEL_MINI.*/ and nozzle_diameter[0]==0.6}0.12{elsif printer_notes=~/.*PRINTER_MODEL_MINI.*/ and nozzle_diameter[0]==0.8}0.06{elsif printer_notes=~/.*PRINTER_MODEL_MINI.*/}0.2{elsif nozzle_diameter[0]==0.8}0.01{elsif nozzle_diameter[0]==0.6}0.04{else}0.05{endif} ; Filament gcode LA 1.5\n{if printer_notes=~/.*PRINTER_MODEL_MINI.*/};{elsif printer_notes=~/.*PRINTER_HAS_BOWDEN.*/}M900 K200{elsif nozzle_diameter[0]==0.6}M900 K18{elsif nozzle_diameter[0]==0.8};{else}M900 K30{endif} ; Filament gcode LA 1.0"
; start_gcode = M862.3 P "[printer_model]" ; printer model check\nM862.1 P[nozzle_diameter] ; nozzle diameter check\nM115 U3.10.0 ; tell printer latest fw version\nG90 ; use absolute coordinates\nM83 ; extruder relative mode\nM104 S[first_layer_temperature] ; set extruder temp\nM140 S[first_layer_bed_temperature] ; set bed temp\nM190 S[first_layer_bed_temperature] ; wait for bed temp\nM109 S[first_layer_temperature] ; wait for extruder temp\nG28 W ; home all without mesh bed level\nG80 ; mesh bed leveling\nG1 Y-3.0 F1000.0 ; go outside print area\nG92 E0.0\nG1 X60.0 E9.0 F1000.0 ; intro line\nG1 X100.0 E12.5 F1000.0 ; intro line\nG92 E0.0\nM221 S{if layer_height<0.075}100{else}95{endif}\n\n; Don't change E values below. Excessive value can damage the printer.\n{if print_settings_id=~/.*(DETAIL @MK3|QUALITY @MK3).*/}M907 E430 ; set extruder motor current{endif}\n{if print_settings_id=~/.*(SPEED @MK3|DRAFT @MK3).*/}M907 E538 ; set extruder motor current{endif}
; support_material = 0
; support_material_angle = 0
; support_material_auto = 0
; support_material_buildplate_only = 0
; support_material_contact_distance = 0.2
; support_material_enforce_layers = 0
; support_material_extruder = 0
; support_material_extrusion_width = 0.35
; support_material_interface_contact_loops = 0
; support_material_interface_extruder = 0
; support_material_interface_layers = 2
; support_material_interface_spacing = 0.2
; support_material_interface_speed = 80%
; support_material_pattern = honeycomb
; support_material_spacing = 2
; support_material_speed = 50
; support_material_synchronize_layers = 0
; support_material_threshold = 55
; support_material_with_sheath = 0
; support_material_xy_spacing = 50%
; temperature = 220
; template_custom_gcode = 
; thin_walls = 0
; threads = 8
; thumbnails = 
; toolchange_gcode = 
; top_fill_pattern = monotonic
; top_infill_extrusion_width = 0.4
; top_solid_infill_speed = 40
; top_solid_layers = 5
; top_solid_min_thickness = 0.7
; travel_speed = 180
; use_firmware_retraction = 0
; use_relative_e_distances = 1
; use_volumetric_e = 0
; variable_layer_height = 1
; wipe = 1
; wipe_into_infill = 0
; wipe_into_objects = 0
; wipe_tower = 1
; wipe_tower_bridging = 10
; wipe_tower_no_sparse_layers = 0
; wipe_tower_rotation_angle = 0
; wipe_tower_width = 60
; wipe_tower_x = 170
; wipe_tower_y = 125
; wiping_volumes_extruders = 70,70
; wiping_volumes_matrix = 0
; xy_size_compensation = 0
; z_offset = 0
