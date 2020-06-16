import json
import jsonpath
import requests


def test_Add_student_data():
    #URL
    API_URL = "http://thetestingworldapi.com/api/studentsDetails"
    # save request format in file
    f=open('4_TEST_API_StudentManagementSystem\\request_format.json','r')
    #convert the request to json format
    json_request =json.loads(f.read())
    #post the request 
    response = requests.post(API_URL,json_request)
    print(response.text)

def test_get_student_data():
    #URL
    API_URL = "http://thetestingworldapi.com/api/studentsDetails/489705"
    # sending request
    response = requests.get(API_URL)
    print(response.text)
    #  converting response to json format
    json_response = json.loads(response.text)
    id=jsonpath.jsonpath(json_response,'data.id')
    print(id)
    assert id[0]==489705

def test_update_student_data():
    #URL
    API_URL = "http://thetestingworldapi.com/api/studentsDetails/489705"
    # save request format in file
    f=open('4_TEST_API_StudentManagementSystem\\request_format.json','r')
    #convert the request to json format
    json_request =json.loads(f.read())
    #post the request 
    response = requests.put(API_URL,json_request)
    print(response.text)

    # to verify 
    # sending request
    response = requests.get(API_URL)
    print(response.text)
    #  converting response to json format
    json_response = json.loads(response.text)
    print(json_response)

    ##cmd command-- pytest 4_TEST_API_StudentManagementSystem\test_student_data.py -s


