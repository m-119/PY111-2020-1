from typing import Union, Sequence


def stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    """
    Calculate min cost of getting to the top of stairway if agent can go on next or through one step.

    :param stairway: list of ints, where each int is a cost of appropriate step
    :return: minimal cost of getting to the top
    """

    vizited_stairway = {1: stairway[0],
                        2: stairway[1]}

    for step, coast in enumerate(stairway[2:], start=2):
        vizited_stairway[step + 1] = min(vizited_stairway[step],
                                         vizited_stairway[step - 1]) + coast

    return vizited_stairway[len(stairway)]

    print(stairway)
    return 0


