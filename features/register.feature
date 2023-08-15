Feature: Registro
  Scenario: Usuario se registra
    Given  usuario ingresa a la pagina demogru
    When usuario ingresa a la seccion de registro
    When usuario se registra en userInformation
    And click en enviar
    Then registro exitoso