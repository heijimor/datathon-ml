from app.models.prediction_request import PredictionRequest

def model_predict(data: PredictionRequest) -> list[dict]:
  predictions = [
      {
        "title": "Ex-premiê Shinzo Abe morre após ser baleado no Japão",
        "url": "http://g1.globo.com/mundo/noticia/2022/07/08/ex-premie-shinzo-abe-morre-apos-ser-baleado-no-japao-diz-nhk.ghtml",
      },
      {
        "title": "Relator no STF, Fachin vota contra marco temporal para demarcação de terras indígenas",
        "url": "http://g1.globo.com/politica/noticia/2021/09/09/relator-no-stf-fachin-vota-contra-marco-temporal-para-demarcacao-de-terras-indigenas.ghtml",
      },
  ]
  return predictions