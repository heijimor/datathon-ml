from app.controllers import recommend_controller

def handle(app):
  app.include_router(recommend_controller.router)