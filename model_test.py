import json
from models import Summoner, LeagueEntry, Match, Timeline
import pytest

@pytest.fixture
def summoner_data():
    with open('json_files/summoner.json', 'r') as f:
        return json.load(f)

@pytest.fixture
def league_entries_data():
    with open('json_files/league_entries.json', 'r') as f:
        return json.load(f)

@pytest.fixture
def match_data():
    with open('json_files/match.json', 'r') as f:
        return json.load(f)

@pytest.fixture
def timeline_data():
    with open('json_files/timeline.json', 'r') as f:
        return json.load(f)

def test_summoner_model_validation(summoner_data):
    try:
        Summoner(**summoner_data)
    except Exception as e:
        pytest.fail(f"Failed to validate Summoner model: {e}")
    assert True

def test_league_entry_model_validation(league_entries_data):
    try:
        [LeagueEntry(**league_entry) for league_entry in league_entries_data]
    except Exception as e:
        pytest.fail(f"Failed to validate LeagueEntry model: {e}")
    assert True

def test_match_model_validation(match_data):
    try:
        Match(**match_data)
    except Exception as e:
        pytest.fail(f"Failed to validate Match model: {e}")
    assert True

def test_timeline_model_validation(timeline_data):
    try:
        Timeline(**timeline_data)
    except Exception as e:
        pytest.fail(f"Failed to validate Timeline model: {e}")
    assert True
