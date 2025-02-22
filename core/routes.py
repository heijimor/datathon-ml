from app.controllers import predict_controller

def handle(app):
  app.include_router(predict_controller.router)