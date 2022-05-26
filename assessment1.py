from bs4 import BeautifulSoup
from datetime import date, timedelta, datetime

today = date.today()

def changeXandY(X,Y):
    if (X < 0) or (Y < 0):
        print("Please enter valid X and Y value")
    # TODO additional error handling based on requirements    

    new_date_X= today + timedelta(X)
    new_data_Y= today +timedelta(Y)
    with open('test_payload1.xml', 'r') as f:
        data =f.read()

    BS_data = BeautifulSoup(data,"xml")
    tag = BS_data.DEPART
    tag.string = new_date_X.strftime('%Y%m%d')
      
    
    tag = BS_data.RETURN
    tag.string = new_data_Y.strftime('%Y%m%d')  

    f = open('test_payload_new.xml','w')
    f.write(BS_data.prettify())
    f.close()

changeXandY(-1,4)





