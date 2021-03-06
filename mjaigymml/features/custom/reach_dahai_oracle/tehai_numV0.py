import numpy as np

from mjaigym.board.mj_move import MjMove
from mjaigymml.features.custom.feature_reach_dahai_oracle \
    import FeatureReachDahaiOracle
from mjaigym.board import BoardState


class TehaiNumV0(FeatureReachDahaiOracle):

    def get_length(cls) -> int:
        return 4

    def calc(self, result: np.array, board_state: BoardState, player_id: int):

        nums = {}
        for pai in board_state.tehais[player_id]:
            if pai.id not in nums:
                nums[pai.id] = 0
            nums[pai.id] += 1

        for index, num in nums.items():
            result[:num, index] = 1
