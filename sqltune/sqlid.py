'''
Created on Feb 18, 2018

@author: duke
'''
import os
import subprocess
import re
import glob
import sys


class sqlid(object):
    '''
    classdocs
    '''
    db_user = ""
    db_pass = ""
    tns_alias = ""
    cloud_config = ""
    sql_binary = ""

    def __init__(self, l_db_user, l_db_pass, l_tns_alias, l_cloud_config):
        self.db_user = l_db_user
        self.db_pass = l_db_pass
        self.tns_alias = l_tns_alias
        self.cloud_config = l_cloud_config
        if sys.platform.startswith("win") :
            self.sql_binary = "sql.exe"
        else:
            self.sql_binary = "sql"
        self.tune()
        
    def tune(self):
        print( "using binary:" +self.sql_binary)
        if self.cloud_config is None :
            subprocess.call([self.sql_binary ,  self.db_user +"/"+self.db_pass+"@"+self.tns_alias , "@sql/awrsqrpt.sql"])
        else :
            subprocess.call([self.sql_binary , "-cloudconfig" , self.cloud_config,  self.db_user +"/"+self.db_pass+"@"+self.tns_alias , "@sql/awrsqrpt.sql"])

# parser = argparse.ArgumentParser(description='SQLTuning')
# parser.add_argument('--db_user', help="db_user")
# parser.add_argument('--db_pass', help="db_pass")
# parser.add_argument('--tns_alias', help="tns_alias")
# args  = parser.parse_args()
# sqltune = sqltune(args.db_user, args.db_pass, args.tns_alias)
sqlid = sqlid(os.environ.get('DB_MON_USR'), os.environ.get('DB_MON_PWD'), os.environ.get('DB_MON_URL'), os.environ.get('DB_MON_CLOUD_CONFIG'))
