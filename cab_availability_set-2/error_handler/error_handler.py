import json
from pydantic import PydanticValueError


class Messages(object):

    code_dict = {
        'E201' : "Task successfully executed",
        'E400' : "Server could not understand the request due to invalid request json",
        'E500' : "The request failed due to some internal error at the server end"

    }

# parent class to deal with Scraper error messages
class Error(PydanticValueError):
    def __init__(self, code, msg_template):
        self.code = code
        self.msg_template = msg_template
    
    def to_json(self):
        return json.dumps(dict(code=self.code,msg=self.msg_template),indent=4)

#returns success response message incase of all compliant files
class SuccessResponse(Error):
    def __init__(self):
        self.code = 201
        self.msg_template = Messages.code_dict['E201']   
        Error.__init__(self, self.code, self.msg_template)    

#returns json error message
class JsonSyntaxError(Error):
    def __init__(self):
        self.code = 400
        self.msg_template = Messages.code_dict['E400'] 
        Error.__init__(self, self.code, self.msg_template)   


#returns internal error if incase unexpected error occurs
class InternalServerError(Error):
    def __init__(self):
        self.code = 500
        self.msg_template = Messages.code_dict['E500']
        Error.__init__(self, self.code, self.msg_template)   

