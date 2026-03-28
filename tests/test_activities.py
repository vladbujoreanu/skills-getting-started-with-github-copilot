def test_root_redirects_to_static_index(client):
    # Arrange
    expected_location = "/static/index.html"

    # Act
    response = client.get("/", follow_redirects=False)

    # Assert
    assert response.status_code in (302, 307)
    assert response.headers["location"] == expected_location


def test_get_activities_returns_expected_payload_and_cache_headers(client):
    # Arrange
    expected_cache_control = "no-store, no-cache, must-revalidate, max-age=0"
    expected_pragma = "no-cache"
    expected_expires = "0"

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    body = response.json()
    assert "Chess Club" in body
    assert "participants" in body["Chess Club"]
    assert body["Chess Club"]["max_participants"] == 12
    assert response.headers["cache-control"] == expected_cache_control
    assert response.headers["pragma"] == expected_pragma
    assert response.headers["expires"] == expected_expires