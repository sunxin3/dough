import MySQLdb
import MySQLdb.cursors
import os
import time 


while True: 
    time.sleep(20)

    db1 = MySQLdb.connect(host = 'localhost', user = 'root', passwd = 'Abcd1234', db = 'nova', cursorclass = MySQLdb.cursors.DictCursor)
    db2 = MySQLdb.connect(host = 'controller', user = 'nova', passwd = 'Abcd1234', db = 'dough', cursorclass = MySQLdb.cursors.DictCursor)
    cursor1 = db1.cursor()
    cursor2 = db2.cursor()
    cursor1.execute('select user_id, uuid, project_id, hostname, instance_types.name as name from instances join instance_types on instances.instance_type_id = instance_types.id where instances.deleted = 0')
    date = time.strftime('%Y-%m-%d',time.localtime(time.time())) 
    for rs in cursor1.fetchall():
        #create subscribtion
        #dough-client -s user_id tenant_id resource_uuid resource_name region item item_type payment_type timestamp
        sql_uuid_exist = 'select * from subscriptions where resource_uuid =' + " '" + rs['uuid'] + "'"
        cursor2.execute(sql_uuid_exist)
        row1 = cursor2.fetchone()
        if row1 is None:
            print '+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++'
            shell = "dough-client -s " + rs['user_id'] + " " + rs['project_id'] + " " + rs['uuid'] + " " + rs['hostname'] + " " + "lenovo" + " " + "instance" + " " + rs['name'] + " " +  "hourlypp" + " " + date
            os.system(shell)

    #user_id is not used, so hardcode for its value
    user_id = "0304d0005656403c9e0121adba5c0445"
    cursor2.execute('select resource_uuid, project_id  from subscriptions where deleted = 0 and status != "deleting"')
    for rs2 in cursor2.fetchall():
        sql_uuid_exist = 'select * from instances where deleted=0 and uuid = ' + "'" + rs2['resource_uuid'] + "'"
        cursor1.execute(sql_uuid_exist) 
        row2 = cursor1.fetchone()
        print row2
        if row2 is None: 
            print '----------------------------------------------------------------------------------------------------------------------------------'
            shell = "dough-client -u " + user_id + " " + rs2['project_id'] + " " + "lenovo " + rs2['resource_uuid'] + " instance " + date
            print shell
            os.system(shell)

    cursor1.close()
    cursor2.close()
    db1.close()
    db2.close()

