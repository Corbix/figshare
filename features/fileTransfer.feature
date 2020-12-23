Feature: file transfer

  Background: logged in
    Given firefox is opened
    When load site
    And we log in with username "bqk79730@yuoia.com" and password "Bqk79730@yuoia.com"

  Scenario: upload file
    When upload file from "C:\Users\crsco\Documents\figshare\test.txt"
    Then file is visible
    And valid credentials shows up
    And logout
    And close

  Scenario: delete file
    When delete file
    Then file is not visible
    And valid credentials shows up
    And logout
    And close
