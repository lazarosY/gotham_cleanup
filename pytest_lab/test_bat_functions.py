import pytest
from bat_functions import *


@pytest.fixture
def sample_vehicles() :
    return {
        'Batmobile': {'speed': 200, 'armor': 80},
        'Bat-sub': {'speed': 250, 'armor': 100},
        'Knightcrawler': {'speed': 150, 'armor': 300}
    }

def test_get_bat_vehicle(sample_vehicles):
    expected = [{'speed': 200, 'armor': 80},
                "Unknown vehicle: Bat-sub",
                "Unknown vehicle: Knightcrawler"
                ]
    result = get_bat_vehicle(sample_vehicles)
    assert result == expected
    
def test_calcluate_bat_power():
    assert calculate_bat_power(5) == 42*5
    assert calculate_bat_power(0) == 0
    assert calculate_bat_power(-1) == -42
    assert calculate_bat_power(5.791) == 42*5.791

@pytest.mark.parametrize("d0,d1,d2,dn,dg", [
    (0,1,2.7,-10,100)
])
def test_signal_strength(d0,d1,d2,dn,dg):
    assert signal_strength(d0) == 100
    assert signal_strength(d1) == 90
    assert signal_strength(d2) == 100 - 27
    assert signal_strength(dn) == 200
    assert signal_strength(dg) == 0
    
def test_fetch_joker_info(monkeypatch):
    mocked_data = {'mischief_level': 0, 'location': 'captured'}
    def mock_fetch():
        return mocked_data
    monkeypatch.setattr(__name__ + '.fetch_joker_info',mock_fetch)
    result = fetch_joker_info()
    assert result == {'mischief_level': 0, 'location': 'captured'}
