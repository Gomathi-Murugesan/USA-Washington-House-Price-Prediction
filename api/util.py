import json
import pickle
import numpy as np

__cities = None
__data_columns = None
__model = None


def get_cities_name():
    load_artifacts()
    return __cities

def get_estimated_house_price(city, sqft_living, bathrooms, bedrooms, yr_built):
    try:
        city_index = __data_columns.index(city.lower())
    except:
        city_index = -1
    ## input to the predict model is two-dimensional array
    ## initially set x as one-dimensional with length equal to no.of columns in input_columns
    ## then send x as two-dimensional to the predict function
    x = np.zeros(len(__data_columns))
    x[0] = bedrooms
    x[1] = bathrooms
    x[2] = sqft_living
    x[3] = yr_built
    if city_index >= 0:
        x[city_index] = 1

    return round(__model.predict([x])[0], 2)


## this function loads saved artifacts such as our model pickle file and input columns json file and city names json file
def load_artifacts():
    print('Start to Load Artifacts')
    global __cities
    global __data_columns
    global __model

    with open('./api/artifacts/input_columns.json', 'r') as f:
        __data_columns = json.load(f)['data_columns']

    with open('./api/artifacts/city_names.json', 'r') as f:
        __cities = json.load(f)['city_names']

    with open('./api/artifacts/usa_house_price_model.pickle', 'rb') as f:
        __model = pickle.load(f)

    print('Load Artifacts Done')

if __name__ == '__main__':
    load_artifacts()
    print(get_cities_name())
    print(get_estimated_house_price('Seattle',3190,3.75,4,1999))
    #print(get_estimated_house_price('1st Phase JP Nagar', 1000, 3, 3))