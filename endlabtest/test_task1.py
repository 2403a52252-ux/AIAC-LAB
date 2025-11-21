from task1 import summarize_doctor_notes
EXPECTED_MOCK = (
    "Chief Complaint: Patient reports headache and mild fever.\n"
    "History of Present Illness: Symptoms present for 2 days, no vomiting, mild fatigue.\n"
    "Diagnosis: Likely viral infection.\n"
    "Medications / Treatment Plan: Paracetamol 500mg, proper hydration, adequate rest.\n"
    "Follow-up Instructions: Return if symptoms worsen or persist beyond 3 days."
)

def test_mock_summary_exact_match():
    out = summarize_doctor_notes("Any input text here")
    assert out == EXPECTED_MOCK

def test_all_sections_present_and_in_order():
    out = summarize_doctor_notes("Different notes")
    lines = out.splitlines()
    assert len(lines) == 5
    assert lines[0].startswith("Chief Complaint:")
    assert lines[1].startswith("History of Present Illness:")
    assert lines[2].startswith("Diagnosis:")
    assert lines[3].startswith("Medications / Treatment Plan:")
    assert lines[4].startswith("Follow-up Instructions:")

def test_consistent_output_and_type_for_various_inputs():
    out1 = summarize_doctor_notes("")
    out2 = summarize_doctor_notes("Patient with cough and fever for 3 days")
    assert isinstance(out1, str) and isinstance(out2, str)
    assert out1 == out2 == EXPECTED_MOCK