import requests,json

alpha_vantage_api_key = "4NE2ALTFPGT83V3S"

def Populate_Sector_Performances():

    # base_url variable that stores the base url
    base_url = "https://www.alphavantage.co/query?function=SECTOR"

    # main_url variable that stores complete url with API key
    main_url = base_url + "&apikey=" + alpha_vantage_api_key

    # Debug the main_url
    print(main_url)

    # get method of requests module
    # return response object
    req_ob = requests.get(main_url)

    # json method return json format
    # data into python dictionary data type.

    # result contains list of nested dictionaries
    result = req_ob.json()

    print(type(result))
    print(result)

Populate_Sector_Performances()
