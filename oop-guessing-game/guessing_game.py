class GuessingGame():
    # Write your code here
    def __init__(self, answer):
        self.answer = answer
        self.found = False
        
    def guess(self, user_guess):
        if user_guess > self.answer:
            return "high"
        if user_guess < self.answer:
            return "low"
        if user_guess == self.answer:
            self.found = True
            return "correct"
        
    
    def solved(self):
        return self.found
    