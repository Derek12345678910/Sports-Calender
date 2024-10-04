import importlib

def callmodule(sport, league):
    print(f"Looking for {sport} and {league} league")

    module = importlib.import_module(f'apimodules.{sport}.{league}', package=__name__)
    entry_point = getattr(module, 'league_input', None)

    if entry_point is None or not callable(entry_point):
        raise AttributeError(f"Module '{sport}' does not have a callable 'league_input' function")

    return entry_point()