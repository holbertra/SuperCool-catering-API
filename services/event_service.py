from models.event import Event, EventSchema
from datetime import datetime

event_schema = EventSchema()

def create_event(data, new_client):   #Called from event_controller.py
    print(f'Entering create_event()')
    print(f'data:{data}')
    print(f'new_client:{new_client}')
    new_event = Event(
        title=data['title'],
        menu_choice=data['menu_choice'],
        ev_date=data['ev_date'],
        client_id=new_client,
        date_created=datetime.utcnow(),
        last_modified=datetime.utcnow() 
    )
    try:
        new_event.save()
        message = 'Event saved successfully'
        return message, 200
    except Exception as e:
        return str(e), 400
#    return "Created new event"

def edit_event(evnt_id, data):    # called from event_controller.py::event_id(evnt_id)
    x = Event.get_one_event(evnt_id)   # get_one_event() defined in event.py
    updated = x.update(x, data)
    new_event = event_schema.dump(updated)
    return new_event

def delete_event(evnt_id):
    x = Event.get_one_event(evnt['id'])
    x.delete()
    return 'Deleted'

def fetch_one_event(evnt_id):
    x = Event.get_one_event(evnt_id)
    event_posts = event_schema.dump(x)
    return  event_posts

def fetch_events():
    x = Event.get_all_events()  # defined as static method in Class Event
    all_events = event_schema.dump(x, many=True)
    return all_events

def get_event(data, user):
    return 'Event retrieved successfully'