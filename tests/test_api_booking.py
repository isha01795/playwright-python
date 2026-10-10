from playwright.sync_api import APIRequestContext, expect

def test_create_booking_api(api_request: APIRequestContext):
    booking_data = {
        "firstname": "Alex",
        "lastname": "Singh",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {"checkin": "2026-11-01", "checkout": "2026-11-05"},
        "additionalneeds": "Breakfast"
    }

    response = api_request.post("/booking", data=booking_data)
    assert response.status == 200

    response_json = response.json()
    assert "bookingid" in response_json
    assert response_json["booking"]["firstname"] == "Alex"