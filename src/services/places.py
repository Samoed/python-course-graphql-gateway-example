import json

from models.places import PlaceModel


class PlacesService:
    """
    Сервис для работы с данными о любимых местах.
    """

    @staticmethod
    def get_places() -> list[PlaceModel]:
        """
        Получение списка любимых мест.

        :return:
        """

        result = []
        with open("fixtures/places.json", encoding="utf-8") as file:
            if data := json.load(file):
                result = [
                    PlaceModel(
                        id=place.get("id"),
                        latitude=place.get("latitude"),
                        longitude=place.get("longitude"),
                        description=place.get("description"),
                        country=place.get("country"),
                        city=place.get("city"),
                        locality=place.get("locality"),
                        created_at=place.get("created_at"),
                        updated_at=place.get("updated_at"),
                    )
                    for place in data.get("data", [])
                ]
        return result

    @staticmethod
    def get_place(place_id: int) -> PlaceModel | None:
        """
        Получение информации о любимом месте.

        :param place_id: Идентификатор любимого места.
        :return:
        """
        result = {place.id: place for place in PlacesService.get_places()}
        return result.get(place_id, None)
