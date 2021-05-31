import json, argparse, os, glob, random, uuid, datetime

class Util():
    def __init__(self,config_path='test_data'):
        self.config_path=config_path
    
    def importer(self, lib):
        print (lib)
        return map(__import__, lib)
        
    def create_folder(self, foldername):
        if not os.path.exists(foldername):
            os.makedirs(foldername)

    def get_guuid_str(self):
        return str(uuid.uuid4())
    
    def get_absolute(self,number):
        return abs(float(number))

    def get_json_files(self, path):
        ''' Getting all json files from a specified folder '''
        json_files = [pos_json for pos_json in os.listdir(path) if pos_json.endswith('.json')]
        return json_files

    def get_xml_files(self, path):
        ''' Getting all json files from a specified folder '''
        json_files = [pos_json for pos_json in os.listdir(path) if pos_json.endswith('.xml')]
        return json_files

    def get_random_guid(self):
        return str(uuid.uuid4())

    def get_random_guuid_by_length(self,string_length):
        return str(uuid.uuid4()).upper().replace("-","")[0:string_length]

    def _get_json_data(self,filename):
        ''' Getting data from json file and returning json object '''
        file = open(filename)
        return json.load(file)

    def get_json_data(self, filename):
        ''' Getting data from json file and returning json object '''
        file = open(filename)
        return json.load(file)

    def write_log(self, file, result):
        ''' Write results to a file'''
        try:
            file.write(str(result)+"\n")
            
        except Exception as e:
            print (e)
            return False
        return True 

    def write_to_file(self, file, result):
        ''' Write results to a file'''
        try:
            file = open(file,'w')
            file.write(result)
            
        except Exception as e:
            print (e)
            return False
        return True 


    def write_json_result(self, filename, result, action="w"):
        ''' Getting data from json file and returning json object '''
        try:
            file = open(filename, action)
            file.write(json.dumps(result))
            file.close()
        except Exception as e:
            print (e)
            return False
        return True

    def strip_string(self, string1, string2):
        string1 = "\\"+string1
        return re.sub(string1,"",string2)

    def remove_all_files(self, folder):
        files = glob.glob(folder+'/*')
        for f in files:
            os.remove(f)

    def get_path_name(self, folderName, fileName):
        ''' ConCat folder name and Filename return path '''
        return folderName+'/'+fileName

    def get_random_int(self, start, end):
        ''' Generate a random whole number bound by start inclusive, end exclusive '''
        return random.randint(0, end-1)

    def find(self, key, dictionary):
        for k, v in dictionary.iteritems():
            if k == key:
                yield v
            elif isinstance(v, dict):
                for result in self.find(key, v):
                    yield result
            elif isinstance(v, list):
                for d in v:
                    for result in self.find(key, d):
                        yield result

    def read_from_file(self, file):
        data=None
        print(file)
        try:
            file = open(file,'r')
            data=file.read()
            file.close()
        except Exception as e:
            print (e)
            return None
        return data

    def get_config_test_data(self, filename):
        return self.get_json_data('{0}/test_data/{1}.json'.format(self.config_path,filename))

    def get_test_data_json(self, filename):
        return self.get_json_data('{0}/test_data/{1}.json'.format(self.config_path,filename))

    def get_endpoints_json(self, endpoints):
        return self.get_json_data('{0}/{1}.json'.format(self.config_path,endpoints))
