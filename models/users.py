from werkzeug.security import generate_password_hash, check_password_hash
import datetime
import bcrypt
#from application import app
class users():
    users_list=[]

    def __init__(self,full_name,email,role,password,confirm_pwd):
        self.full_name=full_name
        self.email=email
        self.role=role
        self.password=password
        self.confirm_pwd=confirm_pwd
        self.user_id=len(users.users_list)+1
    
    def add_user(self):
        for us_er in users.users_list:
            if us_er['user_email']==self.email:
                return 'Email already exists'        
        if self.password==self.confirm_pwd:
            encoded_pw=self.password.encode()
            salt=bcrypt.gensalt()
            hashed_pswd = bcrypt.hashpw(encoded_pw, salt)
            user={'user_id':self.user_id,'user_fullname':self.full_name,'user_email':self.email,'user_role':self.role,'user_password':hashed_pswd}
            users.users_list.append(user)
            return 'The store attendant has been registered'   
        else:
            return 'Passwords do not match'  

    def get_users(self):
        if self.users_list:
            another_users_list=[]
            user_dict={}
            for u in self.users_list:
                user_dict.update({'User full name':u['user_fullname'],'Email':u['user_email'],'User role':u['user_role']})
                another_users_list.append(user_dict.copy())
            return another_users_list
        else:
            return 'There are no users yet'
    
    def login_user(self,email,password):
        for use_r in users.users_list:
            if use_r['user_email']==email:
                encoded_pw=password.encode()
                if bcrypt.hashpw(encoded_pw, use_r['user_password'])==use_r['user_password']:
                    #app.config['SECRET_KEY']='secret'
                    #token=jwt.encode({'user_id':use_r['user_id'],'exp':datetime.datetime.utcnow()+datetime.timedelta(minutes=30)})
                    return use_r
                else:
                    return 'Invalid password for user '+str(use_r['user_email'])
        return str(email)+' email wasn\'t found' 

        



        
        
      