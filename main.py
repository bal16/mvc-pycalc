from model import Model
from view import View


class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View(self)

    def main(self):
        self.view.main()

    def click_btn(self, caption):
        result = self.model.calculate(caption)

        self.view.value_var.set(result)


if __name__ == '__main__':
    App = Controller()
    App.main()