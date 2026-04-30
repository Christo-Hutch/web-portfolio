import re

def get_details():
    details_file = open("data/personal-details.txt", "r")

    raw_data = details_file.read()

    details_list = raw_data.split(' - ')

    DETAILS = {}

    for i in range(0, len(details_list) // 2, 2):
        DETAILS[details_list[i].strip()] = details_list[i + 1].strip()

    return DETAILS

def get_projects():
    PROJECTS = []
    
    try:
        with open("data/projects.txt", "r") as projects_file:
            raw_data = projects_file.read()
    except FileNotFoundError:
        return []

    project_chunks = raw_data.split('===')

    for chunk in project_chunks:
        lines = chunk.strip().split('\n')
        project = {}
        
        for line in lines:
            parts = line.split(' - ', 1)
            if len(parts) == 2:
                project[parts[0].strip()] = parts[1].strip()
        
        if project:
            PROJECTS.append(project)

    return PROJECTS

def get_journey():
    with open("data/my-journey.txt", "r") as journey_file:
        raw_data = journey_file.read()

    cleaned_data = re.sub(r'(?<!\n)\n(?!\n)', ' ', raw_data)
    sections = [s.strip() for s in cleaned_data.split('\n\n') if s.strip()]

    journey_dict = {}
    current_date = None

    for section in sections:
        if section.startswith("DATE ="):
            current_date = section.split("=")[1].strip()
            journey_dict[current_date] = []
        elif current_date:
            journey_dict[current_date].append(section)

    return journey_dict