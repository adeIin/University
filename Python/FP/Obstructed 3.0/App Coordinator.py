from Presentation.UserInterface import Console
from Business.Services import GameService
from Infrastructure.Repositories import Repository
from Domain.Validators import Validator

gameRepo = Repository()
gameValid = Validator()

gameSrv = GameService(gameRepo, gameValid)

ui = Console(gameSrv)

ui.run()
