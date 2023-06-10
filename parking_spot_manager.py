"""
이 모듈은 주차장에 관한 정보를 다루는 모듈이다
내부 클래스로는 주차장 객체를 가리키는 parking_spot이 있다
함수로는 주차장 정보 문자열 리스트를 객체 리스트로 바꾸는 str_list_to_class_list
주차장 리스트를 출력하는 print_spots가 있다
"""
class parking_spot:
    """
    이 클래스는 한 주차장 객체를 가리키는 클래스이다
    이 클래스는 __item 이라는 딕셔너리를 객체 변수로 갖고 있다
    생성자는 이름 도시 구 주차유형 위도 경도를 받아서 객체 변수인 __item을 초기화 시킨다
    __item에는 오로지 get을 통해서만 접근할 수 있다
    객체를 문자열로 바꾸면 __str__에 의해 [이름(주차유형)] 도시 구(위도:x, 경도:y)의 형태로 바뀐다
    """
    # you have to implement 'constructor(생성자)' and 'get' method
    
    def __init__(self, name, city, district, ptype, longitude, latitude):
        """
        생성자
        매개변수로 이름, 도시, 구, 주차 유형, 경도, 위도가 있다
        객체 변수 __item을 초기화
        """
        self.__item = dict()
        self.__item['name'] = name
        self.__item['city'] = city
        self.__item['district'] = district
        self.__item['ptype'] = ptype
        self.__item['longitude'] = longitude
        self.__item['latitude'] = latitude

    def __str__(self):
        item = self.__item
        s  = f"[{item['name']}({item['ptype']})] "
        s += f"{item['city']} {item['district']}"
        s += f"(lat:{item['latitude']}, long:{item['longitude']})"
        return s
    
    def get(self, keyword = 'name'):
        """
        __item에서 특정 키에 대응하는 값을 반환한다
        매개변수로는 키를 받는다
        """
        return self.__item[keyword]

def str_list_to_class_list(str_list):
    """
    파일을 읽어서 만든 주차장 문자열 리스트를 받는다
    리스트의 원소 문자열을 주차장 객체인 parking_spot으로 변형하여 
    parking_spot 클래스 객체 리스트를 생성한 후 반환한다
    """
    parking_spot_list = list()
    for s in str_list:
        informations = s.split(',')
        spot = parking_spot(informations[1], informations[2], informations[3], informations[4], informations[5], informations[6])
        parking_spot_list.append(spot)
    return parking_spot_list

def print_spots(spots):
    """
    조건에 맞는 주차장의 수가 몇 개 있는지 출력하고
    주차장의 목록을 출력한다
    """
    print(f"---print elements({len(spots)})")
    for s in spots:
        print(s)


# 각 단계별로 테스트 (테스트할때 주석해제 후 사용)
if __name__ == '__main__':
    print("Testing the module...")
    # version#2
    import file_manager
    str_list = file_manager.read_file("./input/free_parking_spot_seoul.csv")
    spots = str_list_to_class_list(str_list)
    print_spots(spots)

    # version#3
    # spots = filter_by_district(spots, '동작')
    # print_spots(spots)
    
    # version#4
    # spots = sort_by_keyword(spots, 'name')
    # print_spots(spots)