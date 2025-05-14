from app import create_app
from app.db import Base, engine
from app.models.ad import Ad

app = create_app()

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)  # создаём таблицы при первом запуске
    app.run(debug=True, host="0.0.0.0", port=5000)

