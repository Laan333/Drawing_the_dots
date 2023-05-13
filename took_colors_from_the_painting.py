import colorgram


def took_colors(img: str, numbers_of_colors: int) -> list:
    """
        A function to take colors from a picture and return the data as a list of tuples.
        example: all_data_colors = took_colors("test_data",11)
    """
    colors = colorgram.extract(img, numbers_of_colors)
    list_of_colors = []
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        list_of_colors.append((r, g, b))
    return list_of_colors
