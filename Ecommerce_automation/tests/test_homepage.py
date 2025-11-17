def test_homepage_load(driver, base_url):
    driver.get(base_url)

    # Assert title
    assert "Toolshop" in driver.title

    # Verify navigation links
    driver.find_element("xpath", "//a[text()='Products']")
    driver.find_element("xpath", "//a[text()='Rentals']")
    driver.find_element("xpath", "//a[text()='Contact']")
