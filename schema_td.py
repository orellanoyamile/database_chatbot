# Esquema descriptivo de relación tablas/columnas
finanzas_db = {
    "tabla_finanzas" : {
    "description_long": "Esta tabla contiene detalles de las transacciones financieras de la compañía, abarcando información sobre documentos financieros y su respectiva contabilización. Es esencial para realizar análisis financieros y auditorías internas, incluyendo detalles como la sociedad que registra la transacción, la moneda utilizada, el tipo de cambio aplicado, y otras métricas financieras. Abarca desde la fecha de documentación hasta la fecha de contabilización y otros atributos críticos como el tipo de documento, el número de documento, y el ejercicio fiscal asociado.",
    "description_short": "Esta tabla almacena detalles de transacciones financieras como documentos contables, fechas, tipos de cambio y datos de usuarios.",
    "columns": {
        "Sociedad": "Código de la sociedad en VARCHAR(10).",
        "Num_documento": "Número del documento contable, BIGINT.",
        "Ejercicio_fiscal": "Año del ejercicio fiscal, INT.",
        "Clase_de_documento": "Clase o tipo del documento contable, VARCHAR(5).",
        "Fecha_de_documento": "Fecha de creación del documento contable, DATE.",
        "Fe_contabilizacion": "Fecha en la que se contabiliza el documento, DATE.",
        "Periodo_contable": "Período contable en el que se registra el documento, INT.",
        "Fecha_de_entrada": "Fecha en la que el documento es ingresado en el sistema, DATE.",
        "Hora_de_entrada": "Hora exacta de ingreso del documento, TIME.",
        "Modificado_el": "Fecha de la última modificación del documento, DATE.",
        "Ult_actualizacion": "Fecha de la última actualización registrada del documento, DATE.",
        "Fecha_de_conversion": "Fecha en que se realiza la conversión monetaria, DATE.",
        "Nombre_del_usuario": "Nombre del usuario que ingresó o modificó el documento, VARCHAR(50).",
        "Codigo_transaccion": "Código de la transacción asociada, VARCHAR(10).",
        "Num_multisociedades": "Número asociado a varias sociedades, si aplica, VARCHAR(20).",
        "Referencia": "Referencia del documento, VARCHAR(50).",
        "Doc_periodico": "Indicador si el documento es periódico, VARCHAR(50).",
        "Ejercicio_contabilizacion_periodica": "Ejercicio fiscal para la contabilización periódica, INT.",
        "Sociedad_contabilizacion_periodica": "Sociedad que realiza la contabilización periódica, VARCHAR(10).",
        "Anulado_con": "Código del documento con el que se anuló, si aplica, VARCHAR(10).",
        "Ej": "Código abreviado del ejercicio fiscal, VARCHAR(10).",
        "Texto_cab_documento": "Texto descriptivo en la cabecera del documento, VARCHAR(255).",
        "Moneda": "Código de la moneda utilizada en el documento, VARCHAR(5).",
        "Tipo_de_cambio": "Tipo de cambio aplicado en la conversión de la moneda, DECIMAL(18,5).",
        "Moneda_del_grupo": "Moneda del grupo empresarial, VARCHAR(5).",
        "Tipo_de_cambio_de_la_moneda_del_grupo": "Tipo de cambio aplicado para la moneda del grupo, DECIMAL(18,5).",
        "Status_de_documento": "Estatus actual del documento, VARCHAR(10).",
        "Clase_doc_neto": "Clasificación del documento según si es neto o bruto, VARCHAR(10).",
        "CIA_no_planificados": "Código de la compañía no planificada asociada, si aplica, VARCHAR(10).",
        "Documento_cont_per_ant": "Referencia al documento contable del período anterior, VARCHAR(10).",
        "Oper_empresarial": "Descripción de la operación empresarial, VARCHAR(50).",
        "Juego_de_datos": "Descripción del set de datos utilizado, VARCHAR(50).",
        "Nombre_de_documento_en_archivo": "Nombre del documento tal como aparece en el archivo, VARCHAR(255).",
        "ID_de_extracto": "Identificación del extracto bancario asociado, VARCHAR(50).",
        "Clase_documento_interna": "Clase interna del documento, VARCHAR(10).",
        "Operacion_referencia": "Referencia de la operación financiera, VARCHAR(50).",
        "Clave_de_referencia": "Clave para identificar la referencia, VARCHAR(50).",
        "Entidad_CP": "Entidad de contrapartida, VARCHAR(50).",
        "Moneda_local": "Moneda local de la transacción, VARCHAR(5).",
        "Mon_local_2": "Segunda moneda local, si aplica, VARCHAR(5).",
        "Moneda_local_3": "Tercera moneda local, si aplica, VARCHAR(5).",
        "Tipo_de_cambio_2": "Segundo tipo de cambio aplicado, DECIMAL(18,5).",
        "TC_conversion_3": "Tercer tipo de cambio aplicado, DECIMAL(18,5).",
        "Moneda_inicial": "Moneda inicial de la transacción, VARCHAR(5).",
        "Fecha_de_conversion_1": "Primera fecha de conversión monetaria, DATE.",
        "Fecha_de_conversion_2": "Segunda fecha de conversión monetaria, DATE.",
        "Marca_para_anulacion": "Marca que indica si el documento está anulado, VARCHAR(10).",
        "Fecha_contab_inversa": "Fecha de contabilización inversa, DATE.",
        "Calcular_impuesto": "Indica si se debe calcular el impuesto, BOOLEAN.",
        "Tipo_de_moneda_ML2": "Tipo de moneda para la segunda moneda local, VARCHAR(5).",
        "Tipo_de_moneda_ML3": "Tipo de moneda para la tercera moneda local, VARCHAR(5).",
        "Tipo_de_cotizacion_1": "Tipo de cotización para la conversión de la primera moneda, DECIMAL(18,5).",
        "Tipo_de_cotizacion_2": "Tipo de cotización para la conversión de la segunda moneda, DECIMAL(18,5).",
        "Calcular_impuestos_sobre_imptes_neto": "Indica si se calculan impuestos sobre importes netos, BOOLEAN.",
        "Soc_desencadenante": "Sociedad que desencadena la transacción, VARCHAR(10).",
        "Detalles_impuestos_modificados": "Indica si los detalles de los impuestos fueron modificados, BOOLEAN.",
        "Status_transf_datos_a_release_siguiente": "Indica si los datos están listos para ser transferidos al siguiente release, BOOLEAN.",
        "Sistema_logico": "Sistema lógico asociado, VARCHAR(50).",
        "TC_para_impuestos": "Tipo de cambio aplicado para cálculos de impuestos, DECIMAL(18,5).",
        "TC_ValImponMoneDecl": "Tipo de cambio aplicado en la moneda declarada para valor imponible, DECIMAL(18,5).",
        "Numero_de_orden": "Número de orden de la transacción, INT.",
        "Pago_de_deudores_mediante_efecto_de_vto": "Indica si el pago de deudores se realiza mediante efecto de vencimiento, BOOLEAN.",
        "Motivo_cont_inversa": "Motivo de la contabilización inversa, VARCHAR(50).",
        "Autor_docum_prelim": "Autor del documento preliminar, VARCHAR(50).",
        "Fecha_registro_preliminar": "Fecha de registro del documento preliminar, DATE.",
        "Hora_reg_preliminar": "Hora de registro del documento preliminar, TIME.",
        "Reg_precio_Cod_T": "Código de registro de precio, VARCHAR(50).",
        "Numero_de_sucursal": "Número de sucursal asociada, VARCHAR(10).",
        "Cantidad_paginas": "Cantidad de páginas del documento, INT.",
        "Tp_doc": "Tipo de documento, VARCHAR(10).",
        "Doc_relev_flujo_de_caja": "Indica si el documento es relevante para el flujo de caja, BOOLEAN.",
        "Tipo_de_cotizacion": "Tipo de cotización para la conversión de monedas, DECIMAL(18,5).",
        "ID_sub_asign_internam_p_AWKEY": "ID sub asignación interna para AWKEY, VARCHAR(50).",
        "Entrada_en_diario_secundaria": "Indica si hay entrada en diario secundaria, BOOLEAN.",
        "Referencia_1_especifica_de_pais_region": "Referencia específica de país o región, VARCHAR(50).",
        "Paso_de_cierre_financiero": "Descripción del paso de cierre financiero, VARCHAR(50).",
        "annexation_amount": "Monto de anexión, DECIMAL(18,5).",
        "annexation_percentage": "Porcentaje de anexión, DECIMAL(5,3).",
        "Hora_modific": "Hora de la última modificación, TIME."
        }
    }
}