# Checkout: Validación de Entradas (Pago)

> **Objetivo:** practicar validación segura de entradas en backend
> (regex + reglas de negocio).\
> **Duración sugerida:** 30 min (clase) / **Entregable:**
> `validation.py`

------------------------------------------------------------------------

## ✅ ¿Qué vamos a construir?

Vamos a completar funciones de validación para los campos del formulario
de pago:

-   `card_number`
-   `exp_date`
-   `cvv`
-   `billing_email`
-   `name_on_card`

📌 Cada función debe devolver:

    (clean_value, error_message)

-   `clean_value`: valor normalizado (o `""` si falla)
-   `error_message`: `""` si pasa, o un mensaje si falla

⚠️ No modifiquen `validate_payment_form()`.

------------------------------------------------------------------------

## 📦 Entregable

Subir al repositorio de cada uno:

-   `validation.py`

------------------------------------------------------------------------

## 🧾 Reglas de validación

### 💳 card_number

-   Normalizar el input.
-   Eliminar espacios y guiones antes de validar.
-   Solo dígitos.
-   Longitud entre 13 y 19.
-   🧩 Opcional (no evaluable): validar con algoritmo de Luhn.

------------------------------------------------------------------------

### 📅 exp_date (MM/YY)

-   Formato estricto: MM/YY
-   Mes válido: 01--12
-   No puede estar vencida (comparar con fecha actual UTC).
-   Opcional: limitar fechas excesivamente lejanas.

------------------------------------------------------------------------

### 🔒 cvv

-   Solo dígitos.
-   Longitud 3 o 4.

------------------------------------------------------------------------

### ✉️ billing_email

-   Normalizar: strip() + lowercase
-   Máximo 254 caracteres.
-   Patrón básico de email válido.

------------------------------------------------------------------------

### 👤 name_on_card

-   Normalizar input.
-   Colapsar espacios múltiples.
-   Longitud 2--60.
-   Solo permitir:
    -   Letras (incluyendo acentos)
    -   Espacios
    -   Apóstrofes
    -   Guiones

------------------------------------------------------------------------

## 🧪 Casos de prueba
### Casos válidos

| Campo      | Entrada                | Resultado esperado |
|------------|------------------------|--------------------|
| Tarjeta    | 4111 1111 1111 1111    | Válida             |
| Tarjeta    | 5500000000000004       | Válida             |
| Expiración | 12/29                  | Válida (si no está vencida) |
| CVV        | 123                    | Válido             |
| CVV        | 1234                   | Válido             |
| Email      | john.doe@example.com   | Válido             |
| Nombre     | Juan Pérez             | Válido             |
| Nombre     | Anne-Marie O'Connor    | Válido             |

---

### Tarjetas inválidas

| Entrada               | Motivo esperado |
|-----------------------|-----------------|
| abcd                  | No son dígitos |
| 123456                | Muy corta |
| 4111111111111112      | Falla Luhn |
| 4111-1111-1111-111A   | Contiene letra |

---

### Fechas inválidas

| Entrada | Motivo esperado |
|---------|-----------------|
| 00/25   | Mes inválido |
| 13/25   | Mes inválido |
| 01/20   | Expirada |
| 1/25    | Formato incorrecto |
| 1229    | Formato incorrecto |

---

### CVV inválidos

| Entrada | Motivo esperado |
|---------|-----------------|
| 12      | Muy corto |
| 12345   | Muy largo |
| 12a     | Contiene letra |

---

### Emails inválidos

| Entrada             | Motivo esperado |
|---------------------|-----------------|
| test@               | Estructura inválida |
| @example.com        | Falta parte local |
| test@@example.com   | Formato incorrecto |
| (vacío)             | Campo vacío |

---

### Nombres inválidos

| Entrada    | Motivo esperado |
|------------|-----------------|
| J0hn       | Contiene número |
| (vacío)    | Campo vacío |
| A          | Muy corto |

---

## Criterios de evaluación

| Criterio                                 | Peso |
|------------------------------------------|------|
| Regex correctas                          | 25%  |
| Validación estructural de card_number    | 20%  |
| Validación correcta de exp_date          | 25%  |
| Validación correcta de CVV               | 10%  |
| Validación correcta de billing_email     | 10%  |
| Validación correcta de name_on_card      | 10%  |