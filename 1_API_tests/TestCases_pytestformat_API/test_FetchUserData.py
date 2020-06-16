#Step by Step Rest API Testing using Python

import requests
#API URL
url="https://reqres.in/api/users?page=2"

def test_TC1():
    #SEND get request
    response=requests.get(url)
    print("response is:",response)
    print("-------------------------")

    # dispay response content
    print("dispay response content:",response.content)
    print("-------------------------")

    #displaying header
    print("display header:",response.headers)
    print("-------------------------")

    #asseting status code
    print("asserting")
    assert response.status_code == 200
    print("-------------------------")

    #fetching response hearder
    print("fetching response hearder:", response.headers)
    print("-------------------------")
    print("fetching details from header: ", response.headers.get("Date"))

    #fetch cookies/encoding/elapsed time
    print("fetch cookies:",response.cookies)
    print("-------------------------")
    print("fetch encoding:",response.encoding)
    print("-------------------------")
    print("fetch elapsed time:",response.elapsed)
    print("-------------------------")


def test_TC2():
    #SEND get request
    response=requests.get(url)
    print("response is:",response)
    print("-------------------------")

    # dispay response content
    print("dispay response content:",response.content)
    print("-------------------------")

    #displaying header
    print("display header:",response.headers)
    print("-------------------------")

    #asseting status code
    print("asserting")
    assert response.status_code == 200
    print("-------------------------")

    #fetching response hearder
    print("fetching response hearder:", response.headers)
    print("-------------------------")
    print("fetching details from header: ", response.headers.get("Date"))

    #fetch cookies/encoding/elapsed time
    print("fetch cookies:",response.cookies)
    print("-------------------------")
    print("fetch encoding:",response.encoding)
    print("-------------------------")
    print("fetch elapsed time:",response.elapsed)
    print("-------------------------")
