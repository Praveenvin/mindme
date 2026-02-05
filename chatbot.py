"""
Chatbot utility for Mind Me mental health platform
Provides sentiment-based responses for user interactions
"""

class MindMeChatbot:
    """Simple chatbot for mental health support using sentiment analysis"""
    
    def __init__(self):
        self.positive_responses = [
            "That's wonderful! Keep up that positive energy.",
            "I'm glad to hear you're doing well!",
            "That's excellent news! Keep taking care of yourself.",
            "Your positivity is inspiring!",
        ]
        
        self.negative_responses = [
            "I'm sorry you're feeling this way. It's okay to have difficult days.",
            "Remember, challenging times are temporary. You've got this!",
            "It's important to acknowledge your feelings. Consider taking a break.",
            "Would you like to try some stress-relief activities? We have music and games.",
        ]
        
        self.neutral_responses = [
            "I'm here to listen and support you. Can you tell me more?",
            "Thank you for sharing. How are you feeling today?",
            "I'm interested in understanding your feelings better. What's on your mind?",
            "Let's explore how you're feeling. What would help you right now?",
        ]
        
        self.keywords = {
            'positive': ['happy', 'great', 'wonderful', 'excellent', 'good', 'amazing', 'fantastic', 'love', 'enjoy', 'excited'],
            'negative': ['sad', 'depressed', 'anxious', 'stressed', 'worried', 'bad', 'terrible', 'hate', 'angry', 'frustrated'],
        }
    
    def analyze_sentiment(self, user_input):
        """Analyze sentiment of user input (simple keyword-based approach for MVP)"""
        text = user_input.lower()
        
        for keyword in self.keywords['positive']:
            if keyword in text:
                return 'POSITIVE'
        
        for keyword in self.keywords['negative']:
            if keyword in text:
                return 'NEGATIVE'
        
        return 'NEUTRAL'
    
    def get_response(self, user_input):
        """Generate chatbot response based on user input sentiment"""
        if not user_input or not user_input.strip():
            return "I'm here to help. What's on your mind?"
        
        sentiment = self.analyze_sentiment(user_input)
        
        import random
        
        if sentiment == 'POSITIVE':
            return random.choice(self.positive_responses)
        elif sentiment == 'NEGATIVE':
            return random.choice(self.negative_responses)
        else:
            return random.choice(self.neutral_responses)


# Initialize chatbot instance
chatbot = MindMeChatbot()


def chat_with_user(user_message):
    """Public function to get chatbot response"""
    return chatbot.get_response(user_message)

