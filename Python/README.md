# PetVet Assist - Clean Implementation

AI pet health triage assistant providing safe, non-diagnostic guidance.

## Quick Start

```bash
python petvet.py          # Run demo & tests
jupyter notebook petvet_notebook.ipynb  # Interactive notebook
```

## Usage

```python
from petvet import PetVetAssist

assistant = PetVetAssist()
result = assistant.triage("My dog has been vomiting for 2 days")

print(f"Urgency: {result.urgency}")      # HIGH/MEDIUM/LOW
print(f"Care: {result.vet_type}")        # emergency/general/monitor
print(f"Actions: {result.actions[0]}")   # First recommended action
```

## Features

✅ Symptom extraction from natural language  
✅ Risk-based urgency assessment  
✅ Safe guidance without diagnoses  
✅ Veterinary care recommendations  
✅ Daily wellness tasks  
❌ No medical diagnoses  
❌ No medication advice  

## Files

- `petvet.py` - Complete implementation (200 lines)
- `petvet_notebook.ipynb` - Interactive demo notebook
- `README.md` - This file

## Safety

Always includes veterinary consultation disclaimer. Conservative approach that errs on side of caution.

**⚠️ Not medical advice. Always consult a veterinarian.**