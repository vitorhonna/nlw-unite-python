import pytest
from src.models.settings.connection import db_connection_handler
from .events_repository import EventsRepository


db_connection_handler.connect_to_db()


@pytest.mark.skip(reason="New register in database")
def test_insert_event():
    event = {
        "uuid": "my-uuid-234",
        "title": "Test Event",
        "details": "This is a test event",
        "slug": "test-event-slug-2",
        "maximum_attendees": 10
    }

    events_repository = EventsRepository()
    response = events_repository.insert_event(event)
    print(response)


@pytest.mark.skip(reason="Skip")
def test_get_event_by_id():
    event_id = "my-uuid-123"
    events_repository = EventsRepository()
    response = events_repository.get_event_by_id(event_id)
    print(response)
