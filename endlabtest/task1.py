def summarize_doctor_notes(doctor_notes: str) -> str:
    """
    Summarizes long doctor notes into a short structured clinical summary using
    a prompt-engineering template. This version uses a mock AI response.

    Parameters:
        doctor_notes (str): The full text of a doctor's note.

    Returns:
        str: A concise structured summary of the notes.
    """

    # Prompt that would normally be sent to an AI model
    # (kept here to show how prompt engineering is applied)
    prompt = f"""
    You are an AI medical summarization assistant. Convert the following detailed 
    doctor notes into a concise, structured clinical summary.

    Your output must strictly follow this format:

    Chief Complaint:
    History of Present Illness:
    Diagnosis:
    Medications / Treatment Plan:
    Follow-up Instructions:

    Rules:
    - Keep the summary short (3–6 bullet points per section).
    - Only use information present in the notes.
    - No assumptions.
    - Maintain clinical accuracy.
    - Use simple medical language.

    Doctor Notes:
    {doctor_notes}
    """

    # ------------------------------
    # MOCK AI RESPONSE (simulated output)
    # In a real scenario, this is where an API call would be made.
    # ------------------------------
    mock_summary = (
        "Chief Complaint: Patient reports headache and mild fever.\n"
        "History of Present Illness: Symptoms present for 2 days, no vomiting, mild fatigue.\n"
        "Diagnosis: Likely viral infection.\n"
        "Medications / Treatment Plan: Paracetamol 500mg, proper hydration, adequate rest.\n"
        "Follow-up Instructions: Return if symptoms worsen or persist beyond 3 days."
    )

    return mock_summary


