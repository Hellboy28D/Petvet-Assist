"""
PetVet Assist - Clean, minimal implementation
AI-driven pet health triage without medical diagnoses
"""

import json
import re
from typing import Dict, List, Any, Optional
from dataclasses import dataclass

# Emergency symptoms requiring immediate vet care
EMERGENCY_SYMPTOMS = [
    'bleeding', 'seizure', 'collapse', 'unconscious', 'difficulty breathing',
    'pale gums', 'poisoning', 'not eating 24h', 'severe pain'
]

# Medium urgency symptoms
MEDIUM_SYMPTOMS = [
    'vomiting', 'diarrhea', 'limping', 'lethargy', 'loss of appetite',
    'swelling', 'coughing', 'straining to urinate'
]

@dataclass
class TriageResult:
    urgency: str  # HIGH, MEDIUM, LOW
    symptoms: List[str]
    actions: List[str]
    vet_type: str  # emergency, general, monitor
    disclaimer: str

class PetVetAssist:
    """Clean, minimal PetVet triage system"""
    
    def __init__(self, mock_mode: bool = True):
        self.mock_mode = mock_mode
        self.disclaimer = "⚠️ Not medical advice. Always consult a veterinarian for proper diagnosis."
    
    def extract_symptoms(self, description: str) -> List[str]:
        """Extract symptoms from text description"""
        text = description.lower()
        found_symptoms = []
        
        # Check emergency symptoms first
        for symptom in EMERGENCY_SYMPTOMS:
            if symptom.replace(' ', '') in text.replace(' ', ''):
                found_symptoms.append(symptom)
        
        # Check medium symptoms
        for symptom in MEDIUM_SYMPTOMS:
            if symptom.replace(' ', '') in text.replace(' ', ''):
                found_symptoms.append(symptom)
        
        # Basic symptom patterns
        patterns = {
            'vomiting': ['vomit', 'throwing up', 'sick'],
            'diarrhea': ['loose stool', 'runny', 'diarrhea'],
            'lethargy': ['tired', 'sleepy', 'inactive', 'lethargic'],
            'loss_of_appetite': ['not eating', 'won\'t eat', 'no appetite']
        }
        
        for symptom, keywords in patterns.items():
            if any(keyword in text for keyword in keywords):
                found_symptoms.append(symptom)
        
        return list(set(found_symptoms)) or ['general_concern']
    
    def assess_urgency(self, symptoms: List[str]) -> str:
        """Determine urgency level"""
        # Check for emergency symptoms
        for symptom in symptoms:
            if any(emergency in symptom for emergency in EMERGENCY_SYMPTOMS):
                return 'HIGH'
        
        # Check for medium symptoms
        for symptom in symptoms:
            if any(medium in symptom for medium in MEDIUM_SYMPTOMS):
                return 'MEDIUM'
        
        return 'LOW'
    
    def generate_actions(self, urgency: str, symptoms: List[str]) -> List[str]:
        """Generate safe action recommendations"""
        if urgency == 'HIGH':
            return [
                "Seek immediate veterinary care",
                "Keep pet calm and comfortable",
                "Do not give food or water unless instructed",
                "Call vet clinic ahead of arrival"
            ]
        
        elif urgency == 'MEDIUM':
            return [
                "Schedule vet appointment within 24-48 hours",
                "Monitor symptoms closely",
                "Ensure pet has access to fresh water",
                "Keep pet in quiet, comfortable area"
            ]
        
        else:  # LOW
            return [
                "Monitor pet for changes",
                "Maintain normal feeding schedule",
                "Consider vet consultation if symptoms worsen",
                "Document any changes in behavior"
            ]
    
    def suggest_vet_type(self, urgency: str) -> str:
        """Recommend type of veterinary care"""
        if urgency == 'HIGH':
            return 'emergency'
        elif urgency == 'MEDIUM':
            return 'general'
        else:
            return 'monitor'
    
    def triage(self, description: str) -> TriageResult:
        """Complete triage assessment"""
        symptoms = self.extract_symptoms(description)
        urgency = self.assess_urgency(symptoms)
        actions = self.generate_actions(urgency, symptoms)
        vet_type = self.suggest_vet_type(urgency)
        
        return TriageResult(
            urgency=urgency,
            symptoms=symptoms,
            actions=actions,
            vet_type=vet_type,
            disclaimer=self.disclaimer
        )
    
    def daily_tasks(self, species: str = 'dog') -> List[Dict[str, str]]:
        """Generate daily wellness tasks"""
        base_tasks = [
            {"task": "Check and refill water bowl", "duration": "2 min", "category": "hydration"},
            {"task": "Quick health visual check", "duration": "3 min", "category": "monitoring"},
            {"task": "Basic grooming (brush/pet)", "duration": "5 min", "category": "grooming"},
            {"task": "Short play or training session", "duration": "10 min", "category": "mental"}
        ]
        
        if species == 'cat':
            base_tasks.append({"task": "Clean litter box", "duration": "3 min", "category": "hygiene"})
        elif species == 'dog':
            base_tasks.append({"task": "Brief walk or outdoor time", "duration": "15 min", "category": "exercise"})
        
        return base_tasks[:4]  # Return 4 tasks

# Test cases for validation
TEST_CASES = [
    {
        "description": "My dog has been vomiting for 2 days and won't eat",
        "expected_urgency": "MEDIUM"
    },
    {
        "description": "Emergency! My cat is bleeding and collapsed",
        "expected_urgency": "HIGH"
    },
    {
        "description": "My puppy is scratching more than usual",
        "expected_urgency": "LOW"
    },
    {
        "description": "My dog had a seizure and his gums look pale",
        "expected_urgency": "HIGH"
    },
    {
        "description": "My cat has been coughing occasionally",
        "expected_urgency": "MEDIUM"
    }
]

def run_tests():
    """Run validation tests"""
    assistant = PetVetAssist()
    results = {"passed": 0, "total": len(TEST_CASES)}
    
    print("🧪 Running PetVet Assist Tests")
    print("=" * 40)
    
    for i, case in enumerate(TEST_CASES, 1):
        result = assistant.triage(case["description"])
        passed = result.urgency == case["expected_urgency"]
        
        print(f"\nTest {i}: {'✅' if passed else '❌'}")
        print(f"Input: {case['description'][:50]}...")
        print(f"Expected: {case['expected_urgency']} | Got: {result.urgency}")
        
        if passed:
            results["passed"] += 1
    
    accuracy = results["passed"] / results["total"] * 100
    print(f"\n📊 Results: {results['passed']}/{results['total']} ({accuracy:.1f}% accuracy)")
    return results

def demo_consultation(description: str):
    """Demonstrate complete consultation"""
    assistant = PetVetAssist()
    result = assistant.triage(description)
    
    print("🐾 PetVet Assist Consultation")
    print("=" * 50)
    print(f"📝 Description: {description}")
    print(f"\n🔍 Symptoms Found: {', '.join(result.symptoms)}")
    print(f"🚨 Urgency Level: {result.urgency}")
    print(f"🏥 Recommended Care: {result.vet_type.title()}")
    
    print("\n💡 Recommended Actions:")
    for action in result.actions:
        print(f"  • {action}")
    
    print(f"\n{result.disclaimer}")
    
    # Daily tasks
    tasks = assistant.daily_tasks()
    print(f"\n📅 Daily Wellness Tasks:")
    for task in tasks:
        print(f"  • {task['task']} ({task['duration']})")

if __name__ == "__main__":
    # Run tests
    run_tests()
    
    # Demo consultations
    examples = [
        "My dog has been vomiting and has diarrhea for 2 days",
        "Emergency! My cat was hit by a car and is bleeding",
        "My rabbit hasn't eaten in 24 hours and seems lethargic"
    ]
    
    for example in examples:
        print("\n" + "="*60)
        demo_consultation(example)