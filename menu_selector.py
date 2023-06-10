"""
이 모듈은 프로그램 텍스트 UI와 관련된 모듈이다
기능
1 : 지금까지의 모든 조건을 만족하는 주차장 리스트를 출력
2 : 조건에 맞게 주차장 리스트를 필터링
3 : 아직 미구현
4 : 프로그램 종료
"""
import file_manager as fm
import parking_spot_manager as psm

def start_process(path):

    lines = fm.read_file(path)
    spots = psm.str_list_to_class_list(lines)

    while True:
        print("---menu---")
        print("[1] print")
        print("[2] filter")
        print("[3] sort")
        print("[4] exit")
        select = int(input('type:'))
        if select == 1:
            """
            모든 조건을 만족하는 주차 리스트 출력
            """
            psm.print_spots(spots)
        elif select == 2:
            """
            필터링
            사용 가능한 조건
            1 : 이름
            2 : 도시
            3 : 시군구
            4 : 주차 유형
            5 : 위치 // 최소 위도, 최대 위도, 최소 경도, 최대 경도 순으로 입력
            """
            print("---filter by---")
            print("[1] name")
            print("[2] city")
            print("[3] district")
            print("[4] ptype")
            print("[5] location")
            select = int(input('type:'))
            if select == 1:
                keyword = input('type name:')
                spots = psm.filter_by_name(spots, keyword)
            elif select == 2:
                keyword = input('type city:')
                spots = psm.filter_by_city(spots, keyword)
            elif select == 3:
                keyword = input('type district:')
                spots = psm.filter_by_district(spots, keyword)
            elif select == 4:
                keyword = input('type ptype:')
                spots = psm.filter_by_ptype(spots, keyword)
            elif select == 5:
                min_lat = float(input('type min lat:'))
                max_lat = float(input('type max lat:'))
                min_lon = float(input('type min long:'))
                max_lon = float(input('type max long:'))
                locations = (min_lat, max_lat, min_lon, max_lon)
                spots = psm.filter_by_location(spots, locations)
            else:
                print("invalid input")
        elif select == 3:
            keywords = ['name', 'city', 'district', 'ptype', 'latitude', 'longitude']
            print("---sort by---")
            print(keywords)
            keyword = input('type keyword:')
            if keyword in keywords:
                print("not implemented yet")
                # fill this block
            else: print("invalid input")
        elif select == 4:
            print("Exit")
            break
        else:
            print("invalid input")