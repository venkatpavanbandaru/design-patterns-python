class SchoolBell:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(SchoolBell, cls).__new__(cls)
        return cls._instance

    def ring(self):
        print("Ringing... Lunch break!")


# Example usage:
if __name__ == "__main__":
    # Create what seems like two bells
    bell_a = SchoolBell()
    bell_b = SchoolBell()

    # Check if they're same object
    print(bell_a is bell_b)  # Output: True

    # Both will ring the SAME bell
    bell_a.ring()
    bell_b.ring()