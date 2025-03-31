from selenium import webdriver
from urban_routes_main_page import UrbanRoutesPage


# Create a class for both tests
class TestUrbanRoutes:

    def test_drive_custom_camping_option(self):
        driver = webdriver.Chrome()
        driver.get('https://cnt-784b233b-3492-4228-8423-83e3047817c1.containerhub.tripleten-services.com')

        # Create an instance of the page class
        urban_routes_page = UrbanRoutesPage(driver)

        # Add implicit waits for web elements to have time to load
        driver.implicitly_wait(3)

        # Choose camping car step to enter "From", "To" and to click "custom_option",
        # "drive_icon", "book button", and "camping"
        ...

        # Check if the text displays "Audi A3 Sedan"
        actual_value = urban_routes_page.get_audi_text()
        expected_value = "Audi A3 Sedan"
        assert expected_value in actual_value, f"Expected '{expected_value}', but got '{actual_value}'"
        driver.quit()

    def test_add_driver_license_custom_camping_option(self):
        driver = webdriver.Chrome()
        driver.get('https://cnt-784b233b-3492-4228-8423-83e3047817c1.containerhub.tripleten-services.com')

        # Create an instance of the page class
        urban_routes_page = UrbanRoutesPage(driver)
        # Add implicit waits for web elements to have time to load
        driver.implicitly_wait(3)

        # Choose camping car step to enter "From", "To" and to click "custom_option",
        # "drive_icon", "book button", and "camping"
    def choose_camping_car(self, from_text, to_text):
        self.enter_from_location(from_text)
        self.enter_to_location(to_text)
        self.click_custom_option()
        self.click_drive_icon()
        self.click_book_button()
        self.click_camping()


        # Adding driver license step to click "add driver's license";
        # to enter "first_name", "last_name", "date_of_birth", "number"; and
        # to click "title" and "add button"
    def adding_driver_license(self, first_name, last_name, date_of_birth, number):
        self.click_add_driver_license()
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_date_of_birth(date_of_birth)
        self.enter_number(number)
        self.click_title()
        self.click_add_button()

        # Check that the licence has been added
        actual_value = urban_routes_page.get_verification_text()
        expected_value = "Thank you!"
        assert expected_value in actual_value, f"Expected '{expected_value}', but got '{actual_value}'"
        driver.quit()
