catalogo = {
    "consulta_1": {
        "question": "cuál fue la facturación mensual durante el año 2023?",
        "query": "SELECT strftime('%m', Fecha_de_documento), SUM(annexation_amount) FROM finanzas WHERE strftime('%Y', Fecha_de_documento) = '2023' GROUP BY strftime('%m', Fecha_de_documento);",
        "selected_tables": ["finanzas"],
        "selected_columns": ["finanzas-Fecha_de_documento", "finanzas-annexation_amount"],
        "reasoning": "Esta consulta agrupa la facturación mensual para el año 2023 sumando los montos por mes."
    },
    "consulta_2": {
        "question": "podes darme una comparación de los ejercicios fiscales?",
        "query": "SELECT Ejercicio_fiscal, SUM(annexation_amount) FROM finanzas GROUP BY Ejercicio_fiscal;",
        "selected_tables": ["finanzas"],
        "selected_columns": ["finanzas-Ejercicio_fiscal", "finanzas-annexation_amount"],
        "reasoning": "Se realiza una comparación de la facturación total por cada ejercicio fiscal."
    },
    "consulta_3": {
        "question": "cuál es la comparación semestral de facturación?",
        "query": "SELECT CASE WHEN CAST(strftime('%m', Fecha_de_documento) AS INTEGER) BETWEEN 1 AND 6 THEN 'Primer Semestre' ELSE 'Segundo Semestre' END AS semestre, SUM(annexation_amount) AS total_monto FROM finanzas GROUP BY semestre ORDER BY semestre;",
        "selected_tables": ["finanzas"],
        "selected_columns": ["finanzas-Fecha_de_documento", "finanzas-annexation_amount"],
        "reasoning": "Esta consulta compara la facturación entre el primer y segundo semestre del año actual."
    },
    "consulta_4": {
        "question": "sabes cuantas transacciones en dólares se realizaron este mes?",
        "query": "SELECT COUNT(Moneda) FROM finanzas WHERE Moneda = 'USD' AND strftime('%m', Fecha_de_documento) = strftime('%m', DATE('NOW')) AND strftime('%Y', Fecha_de_documento) = strftime('%Y', DATE('NOW'));",
        "selected_tables": ["finanzas"],
        "selected_columns": ["finanzas-Moneda", "finanzas-Fecha_de_documento"],
        "reasoning": "Esta consulta cuenta las transacciones realizadas en dólares durante el mes actual."
    },
    "consulta_5": {
        "question": "cual fue la facturacion mensual en el 2023?",
        "query": "SELECT strftime('%m', Fecha_de_documento), SUM(annexation_amount) FROM finanzas WHERE strftime('%Y', Fecha_de_documento) = '2023' GROUP BY strftime('%m', Fecha_de_documento);",
        "selected_tables": ["finanzas"],
        "selected_columns": ["finanzas-Fecha_de_documento", "finanzas-annexation_amount"],
        "reasoning": "Esta consulta agrupa la facturación mensual para el año 2023 sumando los montos por mes."
    },
    "consulta_5": {
        "question": "y en el 2024?",
        "query": "SELECT strftime('%m', Fecha_de_documento), SUM(annexation_amount) FROM finanzas WHERE strftime('%Y', Fecha_de_documento) = '2024' GROUP BY strftime('%m', Fecha_de_documento);",
        "selected_tables": ["finanzas"],
        "selected_columns": ["finanzas-Fecha_de_documento", "finanzas-annexation_amount"],
        "reasoning": "Esta consulta agrupa la facturación mensual para el año 2023 sumando los montos por mes."
    }
}