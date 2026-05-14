# Simple classifier - SLM will be added later
# For now, this is a placeholder

class StudyClassifier:
    def __init__(self):
        print("Initializing classifier...")
    
    def predict(self, app_name, window_title, url, tab_title):
        # Simple rule-based for now
        # Later this will use DistilBERT
        
        productive_keywords = ['leetcode', 'github', 'vscode', 'pytorch', 'tensorflow', 'udemy', 'coursera']
        distracting_keywords = ['youtube shorts', 'instagram', 'facebook', 'twitter', 'netflix']
        
        text = (app_name + " " + window_title + " " + url + " " + tab_title).lower()
        
        for keyword in productive_keywords:
            if keyword in text:
                return {"label": "on_task", "confidence": 0.85}
        
        for keyword in distracting_keywords:
            if keyword in text:
                return {"label": "off_task", "confidence": 0.90}
        
        return {"label": "uncertain", "confidence": 0.50}
    
    def train(self, feedback_data):
        # Will be implemented with SLM later
        pass