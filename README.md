# Calculadora Científica

Este proyecto es una calculadora científica desarrollada en HTML, CSS y JavaScript. Permite realizar operaciones básicas y avanzadas, con un diseño adaptable que incluye un modo básico y un modo científico.

## Características

- **Modo Básico**:
  - Suma, resta, multiplicación y división.
  - Botón para limpiar la pantalla.
  - Botón para calcular el resultado.

- **Modo Científico**:
  - Potencias (`^`).
  - Raíz cuadrada (`√`).
  - Logaritmo natural (`log`).
  - Funciones trigonométricas: seno (`sin`), coseno (`cos`), tangente (`tan`).
  - Factorial (`!`).

- **Interfaz Adaptable**:
  - Cambia entre los modos básico y científico con botones dedicados.

## Estructura del Proyecto

El proyecto está organizado en los siguientes archivos:

- **HTML**: `index.html`
  - Contiene la estructura principal de la calculadora.
  - Incluye botones para las operaciones básicas y científicas.
  - Integra el archivo CSS para el diseño y el archivo JavaScript para la funcionalidad.

- **CSS**: `css/style.css`
  - Define el diseño visual de la calculadora.
  - Incluye estilos para los modos básico y científico.
  - Utiliza transiciones para cambiar entre modos.

- **JavaScript**: `js/calculadora.js`
  - Implementa la lógica de la calculadora.
  - Maneja las operaciones básicas y científicas.
  - Controla el cambio entre modos.

## Uso

1. **Abrir el Proyecto**:
   - Clona este repositorio en tu máquina local.
   - Abre el archivo `index.html` en tu navegador.

2. **Modo Básico**:
   - Usa los botones numéricos y de operaciones para realizar cálculos básicos.
   - Presiona `=` para obtener el resultado.
   - Usa `C` para limpiar la pantalla.

3. **Modo Científico**:
   - Cambia al modo científico presionando el botón `Científica`.
   - Usa las funciones avanzadas como potencias, raíces, logaritmos y trigonometría.

## Código Destacado

### Ejemplo de Operación Básica
```javascript
function setOperation(operation) {
  firstOperand = display.value;
  currentOperation = operation;
  display.value = '';
}
```

### Ejemplo de Operación Científica
```javascript
function sqrt() {
  display.value = Math.sqrt(parseFloat(display.value));
}
```
