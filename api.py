import json
import re
from simple_salesforce import Salesforce

with open('config.json','r') as f:
    data = json.load(f)
# instance_url ='https://jrigginassociatesinc-dev-ed.my.salesforce.com'
sf = Salesforce(
    username = data['username'],
    password = data['password'],
    security_token = data['security_token'],
    version='58.0'
)
temp =['efe','weg','weg','brer','rbreb','wewe','wegeg']
for rer in temp:
    print(rer,":",type(rer))

# query = "SELECT Id,Name FROM User"
# results=sf.query(query)
# for result in results['records']:
#     print("ID:",result["Id"])
# option = {
#     "WhoId":"0038c00002gIAPwAAO",
#     "OwnerId":"0058c00000AqpsyAAB",
#     "Subject":"Call",
#     "Description":"https://github.com/",
# }
# sf.Task.create(option)

# query = "SELECT OwnerId FROM Contact"
# results = sf.query(query)
# for result in results['records']:
#     print("OwnerId:",result['OwnerId'])
# // get#Page("0038c00002gIAPxAAO","0058c00000AqpsyAAB","45453","http://someplace.jraphones.com/someclientID/recordings/20230812.wav");



# $sf = new SalesforceFunctions($instanceUrl, $accessToken, "v58.0");

# $query = "SELECT Id FROM Task WHERE WhoId='0038c00002gIAPxAAO'";
# $results =$sf->query($query);
# foreach ($results['records'] as $result){
#     $sf->delete('Task',$result['Id']);
# }
"WhoId,WhatId,Subject,ActivityDate,Status,Priority,IsHighPriority,OwnerId,Description,IsDeleted,AccountId,IsClosed,CreatedDate,CreatedById,LastModifiedDate,LastModifiedById,SystemModstamp,IsArchived,CallDurationInSeconds,CallType,CallDisposition,CallObject,ReminderDateTime,IsReminderSet,RecurrenceActivityId,IsRecurrence,RecurrenceStartDateOnly,RecurrenceEndDateOnly,RecurrenceTimeZoneSidKey,RecurrenceType,RecurrenceInterval,RecurrenceDayOfWeekMask,RecurrenceDayOfMonth,RecurrenceInstance,RecurrenceMonthOfYear,RecurrenceRegeneratedType,TaskSubtype,CompletedDateTime"
# for result in results['records']:
#     # print("WhoId:",result["WhoId"])
#     # print("OwnerId:",result["OwnerId"])
#     # print("Subject:",result["Subject"])
#     print("Description:",result["Description"])
#     print("TaskSubtype:",result["TaskSubtype"])
# deel={"Id":"00T8c000050eVSNEA2"} 
# sf.Task.delete("00T8c000050dp7rEAA")
# option = {
#     "WhoId":"0038c00002gIAPxAAO",
#     "OwnerId":"0058c00000AqpsyAAB",
#     "Subject":"Call Recording",
#     "TaskSubtype":"Call",
#     "Status":"Completed",
#     "Description":"https://github.com/",
# }

# sf.Task.create(option)
# def getExten(callerID):

#     query = "SELECT Id,OwnerId,Phone,Name FROM Contact"
#     results=sf.query(query)
#     owner_id=""
#     for result in results['records']:
#         s=result['Phone']
#         if s is None:
#             continue
#         phoneNumber=re.sub("\D",'',s)
#         if int(float(phoneNumber)) == callerID:
#             contact_id = result['Id']
#             owner_id =result['OwnerId']
#             print(result['Name'])
#             break
#         else: 
#             continue
#     if contact_id is None:
#         return {"contactID":"0"}
#     else:
#         query ="SELECT Id, Name, Extension FROM USER WHERE Id='{}'".format(owner_id)
#         results = sf.query(query)
#         result =results['records'][0]
#         if result['Extension'] is not None:
#             return {"extension":result['Extension']}
#         else:
#             return {"extension":"0","name":result['Name'],"userID":result['Id']}

# value=getExten(7852416200)
# print(value)

    
# def getPage(contactID,recording_url):
#     print(instance_url)
#     url_template = instance_url+"/lightning/r/Contact/{}/view"
#     contact_url=url_template.format(contactID)
#     note_data={
#         'ParentId':contactID,
#         "Title": 'Record',
#         "Body":"https://"+ recording_url,
#     }
#     sf.Note.create(note_data)
#     print(contact_url)
    
# getPage('0038c00002gIAQ8AAO','github.com/')
