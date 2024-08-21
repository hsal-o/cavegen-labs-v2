import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from views.app_view import AppView
from controllers.app_controller import AppController

if __name__ == "__main__":
    app_controller = AppController()
    app_view = AppView(app_controller)
    app_controller.set_view(app_view)

    app_view.mainloop()
