class InvalidMissionTransition(Exception):
    def __init__(self, from_status, to_status):
        self.from_status = from_status
        self.to_status = to_status
        super().__init__(
            f"Cannot transition mission from {from_status} to {to_status}"
        )