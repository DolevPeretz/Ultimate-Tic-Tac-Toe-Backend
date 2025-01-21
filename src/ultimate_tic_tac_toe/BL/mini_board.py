from src.ultimate_tic_tac_toe.domain.enums.current_player import Current_Player


class MiniBoard:
    def __init__(self):
        self.board = [["None" for _ in range(3)] for _ in range(3)]

    def print_board(self):
        for row in self.board:
            print(row)
        print()

    def make_move(self, x: int, y: int ,current_player: Current_Player ):
        if x < 0 or x > 2 or y < 0 or y > 2:
            raise ValueError("Not in the range ")
        if self.board[x][y] != "None":
            raise ValueError("The place alredy taken")
        self.board[x][y] = current_player.name
        return True
     


    def check_winner(self, player :Current_Player) -> bool:
       
        for row in self.board:
            if row[0] == row[1] == row[2] and row[0] == player:
                print(f"player {player}win MiniBoard Row !")
                return True

        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] and self.board[0][col] == player:
                print(f"player {player}win MiniBoard Col !")

                return True

        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] == player:
            print(f"player {player}win MiniBoard  !")

            return True

        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] == player:
            print(f"player {player}win MiniBoard  !")

            return True

        return False
    
    # def NoneSqure(self,x :int,y: int) ->list[int,int]:
    #     move=[]
    #     for x in range(3):
    #         for y in range(3):
    #             if self.board[x][y] == "None":
    #                 move.append(x)
    #     return move
        