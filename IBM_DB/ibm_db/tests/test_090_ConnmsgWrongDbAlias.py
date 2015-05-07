# 
#  Licensed Materials - Property of IBM
#
#  (c) Copyright IBM Corp. 2007-2008
#

import unittest, sys
import ibm_db
import config
from testfunctions import IbmDbTestFunctions

class IbmDbTestCase(unittest.TestCase):

  def test_090_ConnmsgWrongDbAlias(self):
    obj = IbmDbTestFunctions()
    obj.assert_expect(self.run_test_090)

  def run_test_090(self):
    conn = ibm_db.connect("x", config.user, config.password)
    if conn:
      print("??? No way.")
    else:
      err = ibm_db.conn_errormsg()
      print(err)

#__END__
#__LUW_EXPECTED__
#[IBM][CLI Driver] SQL1013N  The database alias name or database name "X" could not be found.  SQLSTATE=42705 SQLCODE=-1013
#__ZOS_EXPECTED__
#[IBM][CLI Driver] SQL1013N  The database alias name or database name "X" could not be found.  SQLSTATE=42705 SQLCODE=-1013
#__SYSTEMI_EXPECTED__
#[IBM][CLI Driver] SQL1013N  The database alias name or database name "X" could not be found.  SQLSTATE=42705 SQLCODE=-1013
#__PASE_EXPECTED__
#Relational database x not in relational database directory. SQLSTATE=42705 SQLCODE=-950
#__IDS_EXPECTED__
#[IBM][CLI Driver] SQL1013N  The database alias name or database name "X" could not be found.  SQLSTATE=42705 SQLCODE=-1013
