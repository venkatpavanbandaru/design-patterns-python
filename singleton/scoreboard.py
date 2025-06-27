class Scoreboard:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Scoreboard, cls).__new__(cls)
            cls._instance.total = 0
        return cls._instance

    def add_runs(self, runs):
        self.total += runs
        print(f"Added {runs} runs. Total: {self.total}")


# Example usage:
if __name__ == "__main__":
    # Create what seems like two scoreboards
    score_a = Scoreboard()
    score_b = Scoreboard()

    # Check if they're same object
    print(score_a is score_b)  # Output: True

    # Both will update the SAME scoreboard
    score_a.add_runs(4)
    score_b.add_runs(6)
    print(f"Final total: {score_a.total}")  # Output: Final total: 10