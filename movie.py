class Movie:
    """
    Represents a movie with basic information and watch time behavior.
    """

    def __init__(self, title: str, genre: str, duration_minutes: int, is_family_friendly: bool):
        # data members
        self.title = title
        self.genre = genre
        self.duration_minutes = duration_minutes
        self.is_family_friendly = is_family_friendly

    def watch_time(self, preview_minutes: int) -> int:
        """
        Accepts preview minutes and returns total watch time.
        """
        return self.duration_minutes + preview_minutes

    def __str__(self) -> str:
        """
        Returns a readable string representation of the Movie object.
        """
        return f"{self.title} ({self.genre}) - {self.duration_minutes} minutes"
