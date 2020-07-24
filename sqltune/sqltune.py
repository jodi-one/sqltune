'''
Created on Feb 18, 2018

@author: duke
'''
import os
import subprocess
import re
import glob
import argparse

class sqltune(object):
    '''
    classdocs
    '''
    db_user = ""
    db_pass = ""
    tns_alias = ""

    def __init__(self, l_db_user, l_db_pass, l_tns_alias):
        self.db_user = l_db_user
        self.db_pass = l_db_pass
        self.tns_alias = l_tns_alias
        self.tune()
        
    def tune(self):
        subprocess.call(["sql.exe" , "-cloudconfig", "C:\\Users\\dukev\\Google Drive\\jodi.one\\Wallet_QOL.zip",  self.db_user +"/"+self.db_pass+"@"+self.tns_alias , "@sql/awrrpt.sql"])
        list_of_files = glob.glob('*.html') # * means all if need specific format then *.csv
        latest_file = max(list_of_files, key=os.path.getctime)
        print( latest_file )
        self.processReport(latest_file)
    
    def processReport(self, l_report):
        fhconfig = open(l_report, "r")
        lines = fhconfig.readlines()
        fhconfig.close()
        for line in lines:
            sqlid = self.getSQLID(line)
            if sqlid != None:
                self.processSQLID(sqlid)
        
    
    def getSQLID(self, l_data):
        pattern = re.compile('<td scope="row" class=\'awrc\'><a class="awr" href="#[\w0-9]{1,}', re.IGNORECASE)
        matcher = re.search(pattern,l_data)
        try:
            return matcher.group().replace('<td scope="row" class=\'awrc\'><a class="awr" href="#','')
        except:
            return None
        
    def processSQLID(self, l_sqlid):
        subprocess.call(["sql.exe",  self.db_user +"/"+self.db_pass+"@"+self.tns_alias , "@sql/sql_monitor.sql",l_sqlid])

# parser = argparse.ArgumentParser(description='SQLTuning')
# parser.add_argument('--db_user', help="db_user")
# parser.add_argument('--db_pass', help="db_pass")
# parser.add_argument('--tns_alias', help="tns_alias")
# args  = parser.parse_args()
# sqltune = sqltune(args.db_user, args.db_pass, args.tns_alias)
sqltune = sqltune(os.environ.get('DB_MON_USR'), os.environ.get('DB_MON_PWD'), os.environ.get('DB_MON_URL'))
