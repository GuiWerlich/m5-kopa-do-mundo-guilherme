from exceptions import InvalidYearCupError, NegativeTitlesError, ImpossibleTitlesError

def data_processing(data: dict):
    first_cup_year = 1930
    limit_year = 2024
    event_count = 4
    
    years = []
    
    year = first_cup_year

    while year <= limit_year:
        years.append(year)
        year += event_count

    if data["titles"] < 0:
        raise NegativeTitlesError
    
    if data["titles"] > len(years):
        raise ImpossibleTitlesError
    
    if int(data["first_cup"][:4]) not in years:
        raise InvalidYearCupError   

    pass