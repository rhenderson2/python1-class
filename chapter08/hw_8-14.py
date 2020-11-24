# homework assignment section 8-14
def build_car(manufacturer, model, **car_info):
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info

car01 = build_car('honda', 'accord',
                  color='white',
                  type='sedan')
print(car01)
