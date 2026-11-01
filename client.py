# -*- coding: utf-8 -*-
"""Personal Agent Allostatic Load Index Biomarker Skill.

Zero-dependency Bruce McEwen multi-system physiological wear-and-tear indexer,
cardiometabolic-neuroendocrine strain evaluator, and allostatic recovery modeler.
"""

import math
from typing import Dict, List, Any, Optional

class PersonalAgentAllostaticLoadIndexBiomarker:
    """Multi-system physiological wear-and-tear modeler based on the Allostatic Load (AL)
    framework established by Bruce McEwen and Teresa Seeman."""

    def calculate_allostatic_load_index(
        self,
        biomarkers: Dict[str, float],
        gender: str = "male"
    ) -> Dict[str, Any]:
        """Calculates allostatic load index (0-10) across cardiovascular, metabolic,
        inflammatory, and autonomic biomarkers."""
        if not biomarkers:
            return {"error": "Empty biomarkers payload"}

        # Threshold definitions based on Seeman / McEwen clinical quartile benchmarks
        thresholds = {
            # Cardiovascular
            "systolic_bp": {"threshold": 130.0, "comp": ">", "system": "Cardiovascular"},
            "diastolic_bp": {"threshold": 85.0, "comp": ">", "system": "Cardiovascular"},
            "resting_heart_rate": {"threshold": 75.0, "comp": ">", "system": "Cardiovascular"},
            # Metabolic
            "fasting_glucose": {"threshold": 100.0, "comp": ">", "system": "Metabolic"},
            "total_hdl_ratio": {"threshold": 4.5, "comp": ">", "system": "Metabolic"},
            "triglycerides": {"threshold": 150.0, "comp": ">", "system": "Metabolic"},
            "waist_hip_ratio": {"threshold": 0.90 if gender.lower() == "male" else 0.85, "comp": ">", "system": "Metabolic"},
            # Inflammatory / Immune
            "hs_crp": {"threshold": 2.0, "comp": ">", "system": "Inflammatory"},
            # Autonomic / Neuroendocrine
            "rmssd_hrv": {"threshold": 28.0, "comp": "<", "system": "Autonomic / Neuroendocrine"},
            "respiratory_rate": {"threshold": 16.0, "comp": ">", "system": "Autonomic / Neuroendocrine"}
        }

        system_scores = {
            "Cardiovascular": {"points": 0, "total_eval": 0, "abnormal_markers": []},
            "Metabolic": {"points": 0, "total_eval": 0, "abnormal_markers": []},
            "Inflammatory": {"points": 0, "total_eval": 0, "abnormal_markers": []},
            "Autonomic / Neuroendocrine": {"points": 0, "total_eval": 0, "abnormal_markers": []}
        }

        total_points = 0
        markers_evaluated = 0

        for key, val in biomarkers.items():
            if key in thresholds:
                rule = thresholds[key]
                sys_name = rule["system"]
                system_scores[sys_name]["total_eval"] += 1
                markers_evaluated += 1

                is_abnormal = False
                if rule["comp"] == ">" and float(val) >= rule["threshold"]:
                    is_abnormal = True
                elif rule["comp"] == "<" and float(val) <= rule["threshold"]:
                    is_abnormal = True

                if is_abnormal:
                    total_points += 1
                    system_scores[sys_name]["points"] += 1
                    system_scores[sys_name]["abnormal_markers"].append({
                        "biomarker": key,
                        "value": val,
                        "clinical_threshold": f"{rule['comp']} {rule['threshold']}"
                    })

        # Normalize score to 10-point scale
        if markers_evaluated > 0:
            normalized_al_score = round((total_points / markers_evaluated) * 10.0, 1)
        else:
            normalized_al_score = 0.0

        if normalized_al_score <= 2.0:
            al_tier = "Low Allostatic Load / Optimal Physiological Resilience"
            wear_tier = "Minimal biological wear-and-tear; homeostatic adaptation intact"
        elif normalized_al_score <= 4.5:
            al_tier = "Moderate Allostatic Wear / Early Multisystem Strain"
            wear_tier = "Sub-clinical multi-organ stress burden; elevated fatigue vulnerability"
        elif normalized_al_score <= 7.0:
            al_tier = "High Allostatic Load / Systemic Dysregulation"
            wear_tier = "Chronic neuroendocrine and cardiometabolic exhaustion; accelerated biological aging"
        else:
            al_tier = "Critical Allostatic Overload"
            wear_tier = "Severe multisystem failure of adaptation; high cardiometabolic / burnout crisis risk"

        # Find highest-burden subsystem
        highest_system = max(
            system_scores.items(),
            key=lambda x: (x[1]["points"] / max(1, x[1]["total_eval"]))
        )
        highest_sys_name = highest_system[0] if highest_system[1]["points"] > 0 else "None (Resilient)"

        prescriptions = {
            "Cardiovascular": "Implement 150 min/week Zone 2 aerobic base building; execute daily sodium-potassium rebalancing (target 4.7g K+).",
            "Metabolic": "Enforce 12-hour intermittent fasting window; eliminate refined liquid carbohydrates; post-prandial 15-minute walks.",
            "Inflammatory": "Anti-inflammatory polyphenolic nutrition (omega-3 > 2g EPA/DHA daily); eliminate ultra-processed seed oils.",
            "Autonomic / Neuroendocrine": "Prioritize 8+ hours restorative sleep; 20-minute daily NSDR or resonant coherent breathwork (5.5 breaths/min).",
            "None (Resilient)": "Maintain current high-resilience habits and continuous baseline biomarker monitoring."
        }

        return {
            "allostatic_load_raw_points": total_points,
            "total_biomarkers_evaluated": markers_evaluated,
            "allostatic_load_index_10": normalized_al_score,
            "allostatic_tier": al_tier,
            "physiological_wear_assessment": wear_tier,
            "subsystem_burden_breakdown": system_scores,
            "primary_vulnerable_subsystem": highest_sys_name,
            "targeted_systemic_prescription": prescriptions.get(highest_sys_name, prescriptions["None (Resilient)"])
        }

    def simulate_allostatic_recovery_trajectory(
        self,
        current_al_index: float,
        adherence_weeks: int = 12
    ) -> Dict[str, Any]:
        """Simulates 12-week allostatic load reduction curve under multimodal lifestyle intervention."""
        decay_rate = 0.05  # weekly decay constant
        trajectory = []

        for week in range(0, adherence_weeks + 1, 2):
            proj_score = round(max(1.0, current_al_index * math.exp(-decay_rate * week)), 1)
            reduction_pct = round(((current_al_index - proj_score) / max(0.1, current_al_index)) * 100.0, 1)
            trajectory.append({
                "week": week,
                "projected_al_index": proj_score,
                "cumulative_reduction_pct": f"{reduction_pct}%"
            })

        return {
            "initial_al_index": current_al_index,
            "intervention_duration_weeks": adherence_weeks,
            "recovery_projection_trajectory": trajectory,
            "projected_final_al_index": trajectory[-1]["projected_al_index"],
            "biological_resilience_gain": f"+{round((current_al_index - trajectory[-1]['projected_al_index']) * 10.0, 1)}% Homeostatic Margin"
        }
