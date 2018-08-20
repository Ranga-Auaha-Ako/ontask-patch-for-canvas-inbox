
What this will do:
It will add two additional fields in the send_email page, one is the column to be used as canvas_id in your table, and a tickbox to decide if a copy need to be sent to canvas.
the message sent to canvas inbox will be a plain text version(no attachment, just plain text, but formated in a similar way visually as the rich text sent by email)
note: there is no checking on if the column selected for canvas traget is a valid canvas_id, but nothing will happen if you sent a message to canvas api and the id is not valid. 


How to use :
1. install html2text

pip install html2text





2. backup old script and replace them with new one

rename //src/action/forms.py 			to 				//src/action/forms.py.old
rename //src/action/ops.py 			to 				//src/action/ops.py.old
rename //src/action/views_email.py 		to 				//src/action/views_email.py.old
rename //src/action/evaluate.py 		to 				//src/action/evaluate.py.old

copy and replace all files in this zip to //src/action/






3. change canvas params to yours
edit post_to_canvas_api.py
change "API_ENDPOINT" to your canvas endpoint,
change "access_token" to your canvas developer token