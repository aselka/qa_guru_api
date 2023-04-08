import allure
from selene import have


@allure.story('Demowebshop tests')
@allure.feature('Login')
@allure.title("Successful auth")
def test_auth(app):
    app.open("")
    with allure.step('Check successful auth'):
        app.element(".account").should(have.text("bis-aselya@yandex.ru"))


@allure.story('Demowebshop tests')
@allure.feature('Wishlist')
@allure.title("Delete product from wishlist")
def test_delete_product_from_wishlist(demoshop, app):
    app.open("")
    with allure.step('Add product to wishlist'):
        demoshop.add_product_to_wishlist()
    with allure.step('Check delete product from wishlist'):
        app.element('.ico-wishlist').click()
        app.element('[name="removefromcart"]').click()
        app.element('[name="updatecart"]').click()
    with allure.step('Check delete product from wishlist'):
        app.element('.wishlist-content').should(have.text('The wishlist is empty!'))


@allure.story('Demowebshop tests')
@allure.feature('Wallet')
@allure.title("Add product to cart")
def test_add_product_to_cart(demoshop, app):
    app.open("")
    with allure.step("Check successful add to cart"):
        demoshop.add_product_to_cart()
        app.element(".ico-cart").click()
    with allure.step("Checking the cart has been added"):
        app.element(".product-name").should(have.text("Laptop"))


@allure.story('Demowebshop tests')
@allure.feature('Wallet')
@allure.title("Remove product to cart")
def test_delete_product_from_cart(demoshop, app):
    app.open("")
    with allure.step('Add product to cart'):
        demoshop.add_product_to_cart()
    with allure.step('Delete product from cart'):
        app.element('.ico-cart').click()
        app.element('[name="removefromcart"]').click()
        app.element('[name="updatecart"]').click()
    with allure.step("Checking the cart has been deleted"):
        app.element('.order-summary-content').should(have.text('Your Shopping Cart is empty!'))


@allure.story('Demowebshop tests')
@allure.feature('Logout')
@allure.title("Successful logout")
def test_logout(app):
    app.open("")
    with allure.step('Logout'):
        app.element('.ico-logout').click()
    with allure.step('Check successful logout'):
        app.element('.ico-login').should(have.text('Log in'))