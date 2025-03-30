import time
from selenium import webdriver
from urban_routes_main_page import UrbanRoutesPage  # Import the POM class


def test_custom_bike_option():
    # Step 1: Open the app - update the URL after starting the server
    driver = webdriver.Chrome()
    driver.get('https://cnt-fb54dfc4-00e8-44d6-afed-f197da701aeb.containerhub.tripleten-services.com')

    # Create an instance of the page class
    urban_routes_page = UrbanRoutesPage(driver)

    # Use POM methods to perform actions on the page
    # Enter "From" and "To" locations.
    urban_routes_page.enter_from_location('East 2nd Street, 601')
    urban_routes_page.enter_to_location('1300 1st St')

    

    # Select the "Custom" option
    urban_routes_page.click_custom_option()
    time.sleep(2)  # Adding delay for visibility; optional

    # Click the "Bike" icon
    urban_routes_page.click_bike_icon()
    time.sleep(2)  # Adding delay for visibility; optional

    # Verify the Bike text is displayed correctly
    actual_value = urban_routes_page.get_bike_text()
    expected_value = "Bike"
    assert expected_value in actual_value, f"Expected '{expected_value}' , but got '{actual_value}'"
    driver.quit()


def test_duration_custom_bike_option():
    driver = webdriver.Chrome()
    driver.get('https://cnt-40f1fd73-8341-459a-8091-2b64d29eea26.containerhub.tripleten-services.com')

    urban_routes_page = UrbanRoutesPage(driver)

    # Use the "enter_locations" step to enter both locations
    ...

    # Select the "Custom" option
    ...
    time.sleep(2)

    # Select the "Bike" icon
    ...
    time.sleep(2)

    actual_value = ...
    expected_value = ...
    assert ...

    driver.quit()
