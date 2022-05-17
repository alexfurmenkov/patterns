from typing import Optional


class PlayerType:
    """
    This class contains an internal state
    that is common for all players.
    In order to avoid creating it for every player,
    it is moved to a separate class and the instance is
    created only once.
    """

    def __init__(self, team: str):
        self._team = team  # read-only attribute
        # an example of how memory can be saved by initializing a heavy object attributes only once
        self._very_heavy_attr = list(range(10000000))

    @property
    def team(self):
        return self._team

    def shoot(self, weapon: str, x_coord: float, y_coord: float):
        print(
            f"Player [{self._team}] shooting from weapon {weapon}, target: ({x_coord}, {y_coord})"
        )


class Player:
    """
    Defines an external state that can be unique for each player.
    Holds a reference to PlayerType object.
    """

    def __init__(self, name: str, weapon: str, player_type_obj: PlayerType):
        self.name = name
        self.weapon = weapon
        self._player_type_obj = player_type_obj

    def shoot(self, x_coord: float, y_coord: float):
        self._player_type_obj.shoot(self.weapon, x_coord, y_coord)


class PlayerFactory:
    """
    Creates a PlayerType instance.
    In terms of memory efficiency, only one instance of
    PlayerType is created per type.
    """

    _existing_players = {}

    @classmethod
    def get_player_type(cls, player_team: str) -> PlayerType:
        player_to_return: Optional[PlayerType] = cls._existing_players.get(player_team)
        if not player_to_return:
            player_to_return = PlayerType(player_team)
            cls._existing_players[player_team] = player_to_return
        return player_to_return


if __name__ == "__main__":
    player_type = PlayerFactory.get_player_type("Terrorist")

    player_1 = Player("Aleksei", "AK-47", player_type)
    player_1.shoot(10.0, 23.5)

    player_2 = Player("John", "Desert Eagle", player_type)
    player_2.shoot(10.0, 23.5)
