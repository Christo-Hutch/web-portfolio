def get_details():
    details_file = open("data/personal-details.txt", "r")

    raw_details = details_file.read()

    details_list = raw_details.split(' - ')

    DETAILS = {}

    for i in range(0, len(details_list) // 2, 2):
        DETAILS[details_list[i].strip()] = details_list[i + 1].strip()

    return DETAILS