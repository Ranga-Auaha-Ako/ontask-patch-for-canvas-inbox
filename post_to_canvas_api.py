
import requests
import json
class post_to_canvas_api():
    
    API_ENDPOINT = "https://canvas.auckland.ac.nz/api/v1/conversations"
    
    access_token = ''
   


    # data to be sent to api
   

    
    def set_payload(self, group_conversation,course,context_code,recipients,
        subject, message_body):
        self.payload = {'from_conversation_id':'',
            'scope':'',
            'filter':'',
            'group_conversation':group_conversation,
            'course':course,   
            'context_code':context_code,
            'recipients[]':recipients,
            'subject':subject,
            'bulk_message':'0',
            'user_note':'0',
            'media_comment_id':'',
            'media_comment_type':'',
            'body': message_body,
            
        }

    def post_to_conversation(self, access_token, payload):
        # header keypair
        headers ={
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Authorization': 'Bearer {}'.format(access_token),
        }
   
        # sending post request and saving response as response object

        return requests.post(url = self.API_ENDPOINT, data = self.payload, headers = headers)

