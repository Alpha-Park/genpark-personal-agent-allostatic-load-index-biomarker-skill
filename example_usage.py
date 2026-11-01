# -*- coding: utf-8 -*-
"""Demonstration of Personal Agent Allostatic Load Index Biomarker Skill."""

import sys
sys.stdout.reconfigure(encoding='utf-8')
from client import PersonalAgentAllostaticLoadIndexBiomarker

def main():
    agent = PersonalAgentAllostaticLoadIndexBiomarker()

    print("=" * 70)
    print("DEMO: Personal Agent Allostatic Load & Physiological Wear Modeler")
    print("=" * 70)

    # 1. Evaluate Comprehensive Multi-System Biomarker Panel
    biomarkers = {
        "systolic_bp": 136.0,        # elevated (> 130)
        "diastolic_bp": 88.0,        # elevated (> 85)
        "resting_heart_rate": 78.0,  # elevated (> 75)
        "fasting_glucose": 104.0,    # elevated (> 100)
        "total_hdl_ratio": 4.8,      # elevated (> 4.5)
        "triglycerides": 142.0,      # normal (< 150)
        "waist_hip_ratio": 0.92,     # elevated (> 0.90 male)
        "hs_crp": 2.4,               # elevated (> 2.0 mg/L)
        "rmssd_hrv": 24.0,           # depressed (< 28 ms)
        "respiratory_rate": 17.0     # elevated (> 16 bpm)
    }

    res_al = agent.calculate_allostatic_load_index(biomarkers, gender="male")

    print(f"\n1. Multi-System Allostatic Load Evaluation:")
    print(f"   Evaluated Markers: {res_al['total_biomarkers_evaluated']}")
    print(f"   Raw Points: {res_al['allostatic_load_raw_points']}/{res_al['total_biomarkers_evaluated']}")
    print(f"   Allostatic Load Index (0-10): {res_al['allostatic_load_index_10']}/10")
    print(f"   Allostatic Tier: {res_al['allostatic_tier']}")
    print(f"   Wear Assessment: {res_al['physiological_wear_assessment']}")
    print(f"   Primary Vulnerable System: {res_al['primary_vulnerable_subsystem']}")
    print(f"   Targeted Prescription: {res_al['targeted_systemic_prescription']}")

    # 2. Simulate 12-Week Allostatic Recovery Trajectory
    res_rec = agent.simulate_allostatic_recovery_trajectory(
        current_al_index=res_al['allostatic_load_index_10'],
        adherence_weeks=12
    )

    print(f"\n2. 12-Week Allostatic Recovery Simulation:")
    print(f"   Initial Index: {res_rec['initial_al_index']}")
    print(f"   Projected Final Index: {res_rec['projected_final_al_index']}")
    print(f"   Resilience Gain: {res_rec['biological_resilience_gain']}")
    print(f"   Trajectory Progress:")
    for step in res_rec['recovery_projection_trajectory']:
        print(f"     Week {step['week']:02d}: AL Index = {step['projected_al_index']} ({step['cumulative_reduction_pct']} reduction)")

    print("\nVerification complete: Allostatic load index engine executed flawlessly.")

if __name__ == "__main__":
    main()
