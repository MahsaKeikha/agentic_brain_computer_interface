from safety.control_gate import control_gate


def base():
    return {
        "signal_provenance_reviewed": True,
        "acquisition_quality_reviewed": True,
        "decoder_validation_reviewed": True,
        "calibration_reviewed": True,
        "performance_safety_reviewed": True,
        "false_activation_risk_reviewed": True,
        "privacy_reviewed": True,
        "cybersecurity_reviewed": True,
        "human_approval": True,
        "signal_quality": "good",
        "decoder_validated": True,
        "calibration_valid": True,
        "false_activation_risk": "low",
    }


SCENARIOS = [
    ("baseline", {}, True),
    ("missing_provenance", {"signal_provenance_reviewed": False}, False),
    ("poor_signal", {"signal_quality": "poor"}, False),
    ("invalid_decoder", {"decoder_validated": False}, False),
    ("invalid_calibration", {"calibration_valid": False}, False),
    ("high_false_activation", {"false_activation_risk": "high"}, False),
    ("autonomous_control", {"consequential_autonomous_control": True}, False),
    ("external_control", {"authorize_external_device_control": True}, False),
    ("stimulation", {"authorize_stimulation": True}, False),
    ("human_subject_without_ethics", {"human_subject_use": True}, False),
]


def main():
    passed = 0
    for name, changes, expected in SCENARIOS:
        context = base()
        context.update(changes)
        actual = control_gate(context)["allowed"]
        assert actual is expected, f"{name}: expected {expected}, got {actual}"
        passed += 1
    print(f"heldout_passed={passed}/{len(SCENARIOS)}")


if __name__ == "__main__":
    main()
