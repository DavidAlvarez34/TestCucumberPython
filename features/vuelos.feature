Feature: Compra de pasajes
  Scenario: Usuario compra pasajes de avion en mi pagina
    Given usuario ingresa a la pagina demogru
    When usuario ingresa al apartado de vuelos
    And selecciona la fecha de ida
    And selecciona la fecha de vuelta
    And selecciona la Business Class
    And click en continuar
    Then compra exitosa