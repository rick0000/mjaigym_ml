import numpy as np

from mjaigym_ml.features.custom.feature import Feature
from mjaigym.board import BoardState


class DiscardReachStateV0(Feature):

    def get_length(cls) -> int:
        return 24

    def calc(cls, result: np.array, board_state: BoardState, player_id: int):
        tsumogiri_start_index = board_state.reach_sutehais_index[player_id]
        if tsumogiri_start_index is None:
            return

        end_index = len(board_state.sutehais[player_id])
        if tsumogiri_start_index < end_index:
            result[tsumogiri_start_index:end_index, :] = 1
