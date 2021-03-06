import random

import numpy as np

import conftest
from mjaigym.board.function.pai import Pai
from mjaigym.board.function.yaku_name import YAKU_CHANNEL_MAP
# from mjaigym.board.function.dfs_result import DfsResult
# from mjaigym.board.function.efficient_dfs import Dfs
from mjaigym.board.function.rs_shanten_analysis import RsShantenAnalysis
from mjaigym.board import Board
from mjaigym.board import BoardState
from mjaigymml.features.custom.feature_reach_dahai import FeatureReachDahai
from mjaigymml.features.custom.reach_dahai_oracle.dfsV0 import DfsV0


def test_horapoint_dfs():
    board = Board()

    # random step
    dahai_count = 0
    while True:
        state = board.get_state()
        if state.previous_action['type'] == "dahai":
            dahai_count += 1

        if dahai_count > 15 and state.previous_action['type'] == "tsumo":
            break

        actions = {}
        for i in range(4):
            furo_removed_actions = [a for a in state.possible_actions[i]
                                    if a['type'] in ['dahai', 'none']]
            actions[i] = random.choice(furo_removed_actions)
        board.step(actions)

    # 先読み特徴量のテスト
    target_player = state.previous_action['actor']

    extractor = DfsV0()
    result = np.zeros((extractor.get_length(), 34))
    board_state = board.get_state()

    fixed_tehai = [
        "1m", "2m", "3m", "4m", "5m", "6m", "7m", "8m",
        "1p", "1p", "1p",
        "E", "E",
        "C",
    ]
    # 手牌を入れ替える
    board_state.tehais[target_player] = Pai.from_list(fixed_tehai)
    print(board_state.tehais[target_player])
    # 親は別のプレーヤーにする
    board_state.state['oya'] = (target_player + 1) % 4

    print("before")
    print(result)
    output = result.copy()
    # 特徴量の計算
    extractor.calc(output, board_state, target_player)
    print("after")
    print(output)
    assert (result != output).any()

    # 一気通貫のテンパイ。あと9mが来れば一気通貫になる。不要牌C
    # （一気通貫、C、あと1枚）の場所にフラグが立っているか
    yaku_target_index = YAKU_CHANNEL_MAP["ikkitsukan"]
    print(yaku_target_index)
    assert output[
        yaku_target_index,
        Pai.from_str("C").id] == 1

    # （一気通貫、E、あと2枚）の場所にフラグが立っているか
    assert output[
        yaku_target_index + len(YAKU_CHANNEL_MAP),
        Pai.from_str("E").id] == 1

    # (8000点, C, あと1枚）の場所にフラグが立っているか
    point_target_index = extractor.target_points.index(7700)
    print("point_target_index", point_target_index)
    assert output[
        point_target_index +
        len(YAKU_CHANNEL_MAP) * extractor.DEPTH,  # 役部分を飛ばしている
        Pai.from_str("C").id] == 1


if __name__ == "__main__":
    test_horapoint_dfs()
