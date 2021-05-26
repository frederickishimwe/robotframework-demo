from oauthlib.oauth2 import LegacyApplicationClient
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib  import OAuth2Session
from requests.auth import HTTPBasicAuth
import argparse,urllib3
import json 
import os



def set_env_flag():
    os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = 'false'
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_token(client_id, scope, token_url, username, password, client_secret, verify_=False):
    token = None
    scope=None
    try:
        set_env_flag()
        print('Scope :', json.dumps(scope))
        oauth = OAuth2Session(client=LegacyApplicationClient(client_id=client_id), scope=scope) 
        token = oauth.fetch_token(token_url=token_url,username=username, password=password, client_id=client_id, client_secret=client_secret, verify=verify_)
    except Exception as e:
        raise e
    return token

def get_token_using_config(filename):
    file = open(filename)
    data =json.load(file)
    return get_token_using_json(data)

def auth(env, user,token_type='ref',auth_type='auth_frontend'):
    data = build_payload(env, user,token_type, auth_type)
    print('\n\n %s\n'%data)
    return get_token_using_json(data)

def get_token_using_json(data):
    c_id = data["client_id"]
    scope = data["scope"]
    token_url = data["token_url"]
    usrn = data["username"]
    pws = data["password"]
    c_secret = data["client_secret"]
    return get_token(c_id, scope, token_url, usrn, pws, c_secret)

def get_bearer_token(token):
    return "Bearer "+token["access_token"]

def build_payload(env_data, user_data,token_type,auth_type='auth_frontend'):
    auth = {}
    auth["client_id"] = env_data[auth_type]["client_id_jwt"] if token_type=='jwt' else env_data[auth_type]["client_id_ref"]
    auth["scope"] = env_data[auth_type]["scope"]
    auth["token_url"] = env_data[auth_type]["token_url"]
    auth["username"] = user_data["username"]
    auth["password"] = user_data["password"]
    auth["client_secret"] = env_data[auth_type]["client_secret"]
    return auth

def get_json_from_file(filename):
    file = open(filename)
    return json.load(file)

if __name__ == "__main__":
    ''' Read in arguements e.g. json file
        required files:
            url
            data in dictionary format
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('--env', default='../test_data/environments/staging.json', help='Environment to be used')    
    parser.add_argument('--user', default= '../test_data/config/users/test_user.json' , help='user to login with')

    args = parser.parse_args()
    
    env = args.env
    user = args.user
    # set_env_flag()

    env = get_json_from_file(env)
    user = get_json_from_file(user)
    # data = build_payload(env, user)
    
    print (auth(env, user,auth_type='auth_backend'))
    # print test_uat()