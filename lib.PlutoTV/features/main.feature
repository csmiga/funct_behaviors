# -- FILE:features/main.feature

Feature: check and visit pluto.tv

    @browser.firefox
    Scenario: run a simple test at pluto.tv
        Given firefox web browser is installed
        When pluto.tv is reachable
        Then test pluto.tv main page
