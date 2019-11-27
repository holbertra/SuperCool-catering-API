from flask import Blueprint, request, Response, json
from services.event_service import create_event, fetch_one_event, fetch_events
from flask_jwt_extended import jwt_required, get_jwt_identity

event_blueprint = Blueprint('event_api', __name__)

#new event route
@event_blueprint.route('/new', methods=['POST'])    # /event/new
@jwt_required
def new_event():
    print(f'execute new_event()')
    new_client = get_jwt_identity()
    data = request.json
    print(f'return create_event(data, new_client)')
    return create_event(data, new_client)   # create_event()func defined in event_service.py


#event /<id> route
@event_blueprint.route('/<int:evnt_id>', methods=['GET', 'PUT', 'DELETE'])
@jwt_required
def event_id(evnt_id):
    print(f'Enter event_id({evnt_id})')
    if request.method == 'GET':
        evnt = fetch_one_event(evnt_id)
        if evnt:
            return custom_response(evnt, 200)

        elif request.method == 'PUT':    
            data = request.json
            client = get_jwt_identity()
            evnt = fetch_one_event(evnt_id) 
            if str(client) == evnt['client_id']:   # client_id is column in events table 
                return custom_response(edit_event(evnt_id, data), 200) #edit_event defined in event_service.py    
            
            elif request.method == 'DELETE':
                client = get_jwt_identity()
                evnt = fetch_one_event(evnt_id)
                if str(client) == evnt['user_id']:
                    return custom_response(delete_event(evnt), 204) 

            else:
                return 'Method not allowed', 405

            
    return '/event/id route: Show event by ID num.'

#all events route
@event_blueprint.route('/all', methods=['GET'])
@jwt_required
def all_events():
    print(f'Enter all_events()')
    list_events = fetch_events()    #defined in event_service.py
    return custom_response(list_events, 200)

def custom_response(res, status_code):
    return Response(
        mimetype='application/json',
        response=json.dumps(res),
        status=status_code
    )
