from glom import glom, Check, Coalesce, SKIP
from pprint import pprint

target = {'answeredAt': '2019-08-23T21:11:04Z',
  'direction': 'Inbound',
  'disposition': 'Answered',
  'duration': 110867,
  'endedAt': '2019-08-23T21:12:55Z',
  'from': {'connectedAt': '2019-08-23T21:11:04Z',
   'departmentName': None,
   'deviceType': None,
   'disconnectedAt': '2019-08-23T21:12:55Z',
   'name': 'blah',
   'number': '1234567890',
   'number_e164': '1234567890',
   'serviceId': None,
   'userId': None},
  'initialQueueName': 'blah',
  'joinedLinkedIds': [],
  'legs': [{'departmentName': 'default',
    'deviceType': 'Unknown',
    'legType': 'Dial',
    'menuName': None,
    'menuOption': None,
    'menuPrompt': None,
    'number': '1234567890',
    'optionAction': None,
    'optionArg': None,
    'queueName': None,
    'serviceId': 327727,
    'timestamp': '2019-08-23T21:11:04Z',
    'userId': None},
   {'departmentName': 'default',
    'deviceType': 'Unknown',
    'legType': 'Answer',
    'menuName': None,
    'menuOption': None,
    'menuPrompt': None,
    'number': '1234567890',
    'optionAction': None,
    'optionArg': None,
    'queueName': None,
    'serviceId': 327727,
    'timestamp': '2019-08-23T21:11:04Z',
    'userId': None},
   {'departmentName': None,
    'deviceType': None,
    'legType': 'EnterIVR',
    'menuName': 'blah',
    'menuOption': None,
    'menuPrompt': None,
    'number': None,
    'optionAction': None,
    'optionArg': None,
    'queueName': None,
    'serviceId': None,
    'timestamp': '2019-08-23T21:11:05Z',
    'userId': None},
   {'departmentName': None,
    'deviceType': None,
    'legType': 'IVRSchedule',
    'menuName': 'Day',
    'menuOption': None,
    'menuPrompt': None,
    'number': None,
    'optionAction': None,
    'optionArg': None,
    'queueName': None,
    'serviceId': None,
    'timestamp': '2019-08-23T21:11:06Z',
    'userId': None},
   {'departmentName': None,
    'deviceType': None,
    'legType': 'EnterQueue',
    'menuName': None,
    'menuOption': None,
    'menuPrompt': None,
    'number': None,
    'optionAction': None,
    'optionArg': None,
    'queueName': 'blah',
    'serviceId': None,
    'timestamp': '2019-08-23T21:11:15Z',
    'userId': None},
   {'departmentName': None,
    'deviceType': None,
    'legType': 'Hangup',
    'menuName': None,
    'menuOption': None,
    'menuPrompt': None,
    'number': 'blah',
    'optionAction': None,
    'optionArg': None,
    'queueName': None,
    'serviceId': None,
    'timestamp': '2019-08-23T21:12:55Z',
    'userId': None}],
  'linkedId': 'some unique key',
  'startedAt': '2019-08-23T21:11:04Z',
  'to': {'connectedAt': '2019-08-23T21:11:04Z',
   'departmentName': 'default',
   'deviceType': 'Unknown',
   'disconnectedAt': '2019-08-23T21:12:55Z',
   'name': None,
   'number': '1234567890',
   'number_e164': '1234567890',
   'serviceId': 327727,
   'userId': None},
  'version': {'label': None, 'major': 4, 'minor': 2, 'point': 1}}

entries_spec = ('legs', 
                # [Check('legType', one_of=('Dial', 'EnterIVR'), default=SKIP)],
                [{'Client': Coalesce('menuName', default=''),
                    'Number': Coalesce('to.number', default=''),
                    'Linked ID': 'serviceId',
                    'Queue': 'queueName'}])
r = glom(target, entries_spec)
pprint(r)
print(type(entries_spec))