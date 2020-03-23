from UI import Console
from Controllers import Controller
from Repositories import Repository
from Validators import Validator


game_repo = Repository()
game_valid = Validator()
game_contr = Controller(game_repo, game_valid)
ui = Console(game_contr)
ui.run()