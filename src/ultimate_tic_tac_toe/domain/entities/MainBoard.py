from http.client import HTTPException
from src.ultimate_tic_tac_toe.domain.entities.MiniBoard import MiniBoard


class MainBoard:
    def __init__(self):
        self.mainBoard = [[MiniBoard(3, 3, "X") for _ in range(3)] for _ in range(3)]
        self.winner = None

    def make_move_main_board(self, mini_board_row: int, mini_board_col: int, row: int, col: int) -> dict:
        mini_board = self.mainBoard[mini_board_row][mini_board_col]
        result = mini_board.make_move(row, col)

        if result["message"] == "Move completed":
            self.current_player = "O" if self.current_player == "X" else "X"
            winner = mini_board.check_winner()
            if winner:
                self.winner = winner
        return result

    def check_main_board_winner(self) ->str | None:
        for row in self.mainBoard:
            for mini_board in row:
                winner = mini_board.check_winner()
                if winner:
                    return winner
        return None

    def get_main_board_by_id(self, main_board_id: str):
        return self.dl.get(main_board_id)

    def delete_main_board_by_id(self, main_board_id: str):
        if main_board_id in self.dl:
            del self.dl[main_board_id]
            return True
        return False

    def delete_main_board(self, main_board_id: str):
        main_board = self.get_main_board_by_id(main_board_id)
        if not main_board:
            raise HTTPException(status_code=404, detail="Main board not found")
        success = self.delete_main_board_by_id(main_board_id)
        if success:
            return {"message": f"Main board with ID {main_board_id} has been successfully deleted"}
        else:
            raise HTTPException(status_code=500, detail="Error occurred while deleting main board")

