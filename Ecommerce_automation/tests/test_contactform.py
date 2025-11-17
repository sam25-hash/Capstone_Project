from Ecommerce_automation.pages.contact_page import ContactPage

import time
def test_contact_form(driver, base_url):
    contact = ContactPage(driver)
    contact.open(base_url)  # open /contact directly

    # File path from Downloads folder (must contain some text)
    file_path = r"C:\Users\samiksha.devan\Downloads\hi.txt"

    # Fill and submit the form
    contact.fill_form(
        first_name="Samiksha",
        last_name="Devan",
        email="samiksha@gmail.com",
        message="This is a test message that is deliberately long to exceed fifty characters for testing purposes.",
        subject="Warranty",
        attachment_path=file_path
    )
    time.sleep(2)
    # Click send and wait 3 seconds to see the result
    contact.submit_form(delay_after_click=5)

    # Assert the real success message appears
    assert contact.is_successful(), "Contact form submission failed or success message not found."
