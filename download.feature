Feature: article interaction

  @fixture.browser.chrome
  Scenario: download article
    Given we are on the landing page
    When we select a random article
    And we download it
    Then file is accessible in the filesystem
