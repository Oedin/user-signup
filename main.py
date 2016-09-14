
import webapp2
import re
import cgi
form="""


<div id="container">
  <h1 > Sign up</h1>
  <div class="input_form">
  
    <form method="post">

        
        <div class="wrapper">
        <p> <label> User Name: </label> <input type="text" name ="uname" value="" > </p>
        <p> <label> Password: </label>  <input type="password" name="pass1" value="">   </p>
        <p> <label> Verify Password: </label> <input type="password" name="pass2" >  </p>
        <p> <label> Email: </label> <input type="email" name="email" value="">  </p>
        <p style="color:red;"> %(error)s </p>
        <p> <input id ="btn" type="submit"></p>
        </div>
        
        </form>
</div>
<style>
    #container{
    width: 700px;
    height: 400px;
    margin: auto;
    background-color:#e6ffe6;
    border-style: ridge;
    border-width: 2px;
    border-radius: 10px;
    }
    
    h1{
    margin-left: 100px;
    }
    .input_form{
    padding-left: 50px;
    width:600px;
    }
    
    p{
    margin-right: 50px;
    }
    
    label{
    font-size: 19px;
    margin-right: 250px;
    font-family:sans-serif;
    
    }
    
    input{
    width: 250px;
    font-size: 15px;
    margin-bottom: -10px;
    border-radius: 5px;
    height: 27px;
    }
    
    
    #btn{
    background-color:#339933;
    
    }
    
</style>
"""




    
def validate_uname(uname):
    if not re.match(r"^[a-zA-Z0-9_-]*$", uname):
        return False
    elif len(uname) < 3:
        return False
    elif uname=='':
        return False
    else:
        return uname

def validate_pass(pass1):
    if len(pass1) < 5:
        return False
    elif pass1=="":
        return False
    else:
        return pass1
    
def validate_pass2(pass1, pass2):
    if pass2 != pass1:
        return False
    else:
        return pass2
    

def validate_email(email):
    if not len(email) > 7:
        return False
    elif not re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email) != None:
            return False
    else:
        return email
    

class MainPage(webapp2.RequestHandler): 
    
    
    def write_form(self, error=""):
        self.response.out.write(form % {"error":error})
        
    def get(self):
        self.write_form()
        
        
    def post(self):
        is_error = False
        uname= self.request.get('uname')
        pass1 = self.request.get("pass1")
        pass2 = self.request.get("pass2")
        email= self.request.get("email")
        
        
        
        isError = False
        error=""
        if not validate_uname(uname):
            error ="* Check your user name"
            isError = True
        elif not validate_pass(pass1):
            error = ("* Check your password")
            isError = True
        elif pass1 != pass2:
            error = ("* Passwords don't match")
            isError = True
        elif not validate_email(email):
            error= ("* Check your email")
            isError = True
        
        if isError:
            self.write_form(error)
        else:
            self.response.out.write("Welcome " + uname)
    
   
        
        
app = webapp2.WSGIApplication([('/', MainPage)], debug=True)
