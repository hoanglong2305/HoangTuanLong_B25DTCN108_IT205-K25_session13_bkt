vehicle_list = []

while True:
    print('==============================================')
    print('        QUẢN LÍ BÃI XE - SMART PARKING        ')
    print('==============================================')
    print('1. Thêm xe mới vào bãi')
    print('2. Hiển thị danh sách xe trong bãi')
    print('3. Tìm kiếm xe theo mã (id)')
    print('4. Xóa xe khỏi bãi (khi xe ra)')
    print('5. Thoát chương trình')
    print('==============================================')

    choose = input('nhập lựa chọn của bạn: ')
    match choose:
        case '1':
            id = 0
            is_check = True
            while True:
                id += 1
                type_vehicle = input('Vui lòng nhập loại xe: ')
                
                if type_vehicle == '':
                    print('Yêu cầu nhập lại!')
                    is_check = False
                owner = input('Vui lòng nhập chủ xe: ')
                if owner == '':
                    print('Yêu cầu nhập lại')
                    is_check = False
                
                vehicle_list.append({
                    "id": id,
                    "type": type_vehicle,
                    "owner": owner
                })
                break
        case '2':
            if len(vehicle_list) == 0:
                print('Bãi xe hiện đang trống!')
            else:
                for vehicle in vehicle_list:
                    print(f'ID: {vehicle["id"]} | Loại xe: {vehicle["type"]} | Chủ xe: {vehicle["owner"]}')
        case '3':
            id_input = input('nhập id muốn tìm kiếm: ').strip()
            for search_vehicle in vehicle_list:
                if search_vehicle["id"] == id_input:
                    print(search_vehicle)
                else:
                    print(f'không tìm thấy xe có id {id_input}')
                
        case '4':
            id_input_delete = input('Nhập id muốn xóa: ')
            is_found = False
            for delete_vehicle in vehicle_list:
                if id_input_delete == delete_vehicle["id"]:
                    vehicle_list.remove(delete_vehicle)
                    is_found = True
                    break
                if is_found == False:
                    print('không tìm thấy để xóa')
        case _:
            print('Lựa chọn không hợp lệ. Vui lòng nhập lại')
            