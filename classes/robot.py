class Robot:
    def __init__(self, colour: str, height: float, power: int):
        self.colour = colour
        self.height = height
        self.power = power
        self.health = 100
    
    def __str__(self) -> str:
        return f"{self.colour} {self.height} {self.power} {self.health}"

    def punch(self, robot: object) -> None:
        """Decreases the health of another robot

        Args:
            robot: the name of another robot object

        Returns:
            None
        """

        robot.health -= self.power

    def recharge(self) -> None:
        """Increses health by 10
        """

        self.health += 10
