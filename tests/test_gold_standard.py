from orchestration.orchestrator import orchestrate
from safety.control_gate import control_gate


def approved_context():
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


def test_baseline_research_support_can_pass():
    assert control_gate(approved_context())["allowed"] is True


def test_missing_human_approval_fails_closed():
    context = approved_context()
    context["human_approval"] = False
    assert control_gate(context)["allowed"] is False


def test_consequential_control_is_prohibited():
    context = approved_context()
    context["consequential_autonomous_control"] = True
    assert control_gate(context)["allowed"] is False


def test_high_false_activation_risk_blocks():
    context = approved_context()
    context["false_activation_risk"] = "high"
    assert control_gate(context)["allowed"] is False


def test_invasive_interface_requires_specialist_review():
    context = approved_context()
    context["invasive_interface"] = True
    assert control_gate(context)["allowed"] is False


def test_human_subject_use_requires_ethics_approval():
    context = approved_context()
    context["human_subject_use"] = True
    assert control_gate(context)["allowed"] is False


def test_orchestrator_executes_six_specialists():
    result = orchestrate(approved_context())
    assert len(result["specialist_results"]) == 6


def test_no_autonomous_clinical_or_stimulation_authority():
    gate = control_gate(approved_context())
    assert gate["autonomous_control_authority"] is False
    assert gate["autonomous_stimulation_authority"] is False
    assert gate["clinical_authority"] is False
