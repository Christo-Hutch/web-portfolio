def get_details():
    details_file = open("data/personal-details", "r")

    raw_details = details_file.read()

    details_list = raw_details.split(' - ')

    DETAILS = {}

    for i in range(0, len(details_list) // 2, 2):
        DETAILS[details_list[i]] = details_list[i + 1]

    return DETAILS