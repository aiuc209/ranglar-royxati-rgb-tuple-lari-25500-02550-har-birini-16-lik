def rgb_to_hex(rgb_list):
    hex_list = []
    for rgb in rgb_list:
        hex_list.append('#{:02X}{:02X}{:02X}'.format(rgb[0], rgb[1], rgb[2]))
    return hex_list

rgb_list = [(255,0,0), (0,255,0), (0,0,255), (255,255,0), (255,0,255), (0,255,255)]
print(rgb_to_hex(rgb_list))
