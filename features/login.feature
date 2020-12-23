Feature: login

  Scenario Outline: login to figshare with invalid parameters
    Given <browser> is opened
    When load site
    And we log in with username "<username>" and password "<password>"
    Then invalid credentials shows up
    And close

  Examples: Browsers
  | browser | username | password |
  | firefox | email@gmail.com | drowssap |
  | chrome | drowssap@gmail.com | Bqk79730@yuoia.com |

  Scenario Outline: login to figshare with valid parameters
    Given <browser> is opened
    When load site
    And we log in with username "bqk79730@yuoia.com" and password "Bqk79730@yuoia.com"
    Then valid credentials shows up
    And logout
    And close

  Examples: Browsers
  | browser |
  | firefox |
  | chrome |
