import random
def ai_loan_approval(applicant_name):  
    decision = random.choice(['Approved', 'Denied'])
    print(f"Loan approval for {applicant_name}: {decision}")
    return decision
# Test with different names
names = ["John", "Priya", "Ahmed", "Maria", "Wei", "Aisha", "David", "Lakshmi"]
results = {}
for name in names:
    results[name] = ai_loan_approval(name)
# Display summary
print("\nSummary of loan approvals:")
for name, decision in results.items():
    print(f"{name}: {decision}")

# Note: Since this is a random simulation, no bias is present.
# In a real AI system, you would analyze the output for patterns indicating bias.