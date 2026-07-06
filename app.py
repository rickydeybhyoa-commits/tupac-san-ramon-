Python
import tkinter as tk
from tkinter import messagebox

# ==============================================================================
# BASE DE DATOS (Pega aquí tus 169 procedimientos)
# ==============================================================================
DATOS_TUPA = [
    {
        "id": "1",
        "numero": "1.0",
        "procedimiento": "INSCRIPCIÓN ORDINARIA DE NACIMIENTO DENTRO DE LOS 60 DÍAS",
        "sustento": "SUB GERENCIA DE REGISTRO CIVIL - PROCEDIMIENTOS ADMINISTRATIVOS",
        "requisitos": [
            "1.0 Certificado de Nacido Vivo expedido por Profesional Competente o constancia otorgada por persona autorizada por el Ministerio de Salud.",
            "2.0 Declaración Jurada de la Autoridad Política, Judicial o Administrativa en caso de no haber centro de salud.",
            "3.0 Presencia de los padres o de uno de ellos con DNI vigente."
        ],
        "derecho_tramite": "GRATUITO",
        "plazo": "Inmediato (Automático)",
        "inicio": "Sub Gerencia de Registro Civil",
        "autoridad": "Sub Gerente de Registro Civil",
        "reconsideracion": "Sub Gerente de Registro Civil",
        "apelacion": "Gerencia Municipal"
    },
    {
        "id": "2",
        "numero": "149",
        "procedimiento": "PERMISO DE OPERACIÓN A PERSONAS JURÍDICAS PARA PRESTAR EL SERVICIO CON VEHÍCULOS MENORES",
        "sustento": "GERENCIA DE TRÁNSITO Y TRANSPORTE URBANO\nLey N° 27181 - Ley General de Transporte y Tránsito Terrestre.\nLey N° 27972 - Ley Orgánica de Municipalidades.",
        "requisitos": [
            "1.0 Solicitud bajo la forma de Declaración Jurada dirigida al Alcalde.",
            "2.0 Copia simple de la Constitución de la Empresa inscrita en Registros Públicos (SUNARP).",
            "3.0 Copia simple del RUC activo de la persona jurídica.",
            "4.0 Copia simple de los documentos de propiedad de los vehículos (Tarjeta de Propiedad / Tarjeta de Identificación Vehicular).",
            "5.0 Copia de Seguro Obligatorio de Accidentes de Tránsito (SOAT) vigente.",
            "6.0 Certificado de constatación de características de las unidades emitido por el área técnica.",
            "7.0 Pago de derecho de trámite por inspección y emisión."
        ],
        "derecho_tramite": "1.5% UIT (S/. 57.00 aprox.)",
        "plazo": "15 Días hábiles",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Tránsito y Transporte Urbano",
        "reconsideracion": "Gerente de Tránsito y Transporte Urbano",
        "apelacion": "Gerencia Municipal"
    },
    {
        "id": "3",
        "numero": "2.0",
        "procedimiento": "COMPLEMENTACIÓN ALIMENTARIA MUNICIPAL PCAM - ADMISIÓN AL PCAM",
        "sustento": "Ley Nº 27767, Ley del Programa Nacional Complementario de Asistencia Alimentaria.\nD.S 002-2004-MINDES, Reglamento de la Ley.",
        "requisitos": [
            "1.0 Copia simple de la Resolución de Reconocimiento de la OSB emitido por la Municipalidad de San Ramón.",
            "2.0 Copia simple del Padrón de Socias Activas (como mínimo de 15 socias).",
            "3.0 Copia simple del DNI vigente de las socias activas.",
            "4.0 Copia simple del DNI vigente de los miembros del Consejo Directivo o Junta Directiva.",
            "5.0 Croquis de ubicación del OSB.",
            "6.0 Determinar el lugar donde la OSB recepcionará y atenderá el reparto de los productos pertenecientes al PCAM."
        ],
        "derecho_tramite": "GRATUITO",
        "plazo": "15 Días hábiles",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Desarrollo Social y Humano",
        "reconsideracion": "Gerente de Desarrollo Social y Humano",
        "apelacion": "Gerente Municipal"
    },
    {
        "id": "4",
        "numero": "3.0",
        "procedimiento": "INSCRIPCIÓN EXTEMPORÁNEA DE NACIMIENTO PARA MAYORES DE 18 AÑOS DE EDAD",
        "sustento": "BASE LEGAL\n- Ley N° 26497\n- D.S N° 015-98-PCM\n- Res. Jefatural N° 128-98-RENIEC \"Cartilla para Registrador\"\n- Ley N° 28720 que modifica el Art 20 del CC\n- Ley N° 29467\n- Guia de Procedimientos - RENIEC GP-271-GRC/SGGTRC/004\n- Ley N° 27444\n- Resolución Jefatural N° 359-2010-RENIEC Calificación Registral para Oficinas Autorizadas",
        "requisitos": [
            "1. Solicitud dirigida al Sub Gerente de Registro Civil peticionando la inscripción.",
            "2. Certificado de Nacido Vivo (en cualquiera de sus modalidades: certificado expedido por profesional competente o por declaración jurada de la autoridad que haya confirmado el nacimiento y/o Constancia de Parto de la autoridad que haya confirmado el nacimiento).",
            "3. Adjuntar cualquiera de los siguientes documentos:\n   - Partida de Bautismo.\n   - Certificado de Matrícula Escolar, con mención de los grados cursados (Certificado de Estudios o Constancia de Estudios).\n   - Certificado de Antecedentes Policiales u homologación de huella dactilar, efectuada por la Policía Nacional del Perú.",
            "4. Presencia del Solicitante (s) acompañado (s) con su DNI vigente.",
            "5. Declaración Jurada de 2 Testigos Mayores de Edad No Familiares del Mayor de Edad.",
            "6. Presentación del DNI vigente de los Testigos.",
            "7. Constancia de No Inscripción de Nacimiento otorgada por el Registro Civil del lugar donde nació el Mayor de Edad o en donde reside de acuerdo a su DNI.",
            "8. Certificado de antecedentes policiales u homologación de huellas dactilares (PNP).",
            "9. Certificado Domiciliario"
        ],
        "derecho_tramite": "GRATUITO",
        "plazo": "10 Días hábiles",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Sub Gerente de Registro Civil",
        "reconsideracion": "Sub Gerente de Registro Civil (Plazo Presentación: 15 días hábiles / Resolución: 30 días hábiles)",
        "apelacion": "RENIEC (Plazo Presentación: 15 días hábiles / Resolución: 30 días hábiles)"
    },
    {
        "id": "5",
        "numero": "4.0",
        "procedimiento": "INSCRIPCIÓN DE HIJO EXTRAMATRIMONIAL EFECTUADO POR UNO SOLO DE LOS PADRES",
        "sustento": "BASE LEGAL\n- Artículo 388° del Código Civil.\n- Ley N° 28720, Ley que Modifica los Artículos 20° y 21° del Código Civil.\n- Ley N° 26497.\n- D.S. N° 015-98-PCM.\n- Guia de Procedimientos - RENIEC GP-271-GRC/SGGTRC/004",
        "requisitos": [
            "1. La presencia del Único Padre que realiza la inscripción, acompañado con su respectivo DNI.",
            "2. Declaración Jurada de Presunto (a) Progenitor (a) al Amparo de la Ley N° 28720.",
            "3. Ficha de Datos Personales de la RENIEC del Presunto (a) Progenitor (a)."
        ],
        "derecho_tramite": "GRATUITO",
        "plazo": "Inmediato (Automático)",
        "inicio": "Sub Gerencia de Registro Civil",
        "autoridad": "Sub Gerente de Registro Civil",
        "reconsideracion": "-",
        "apelacion": "-"
    },
{
        "id": "6",
        "numero": "5.0",
        "procedimiento": "RECONOCIMIENTO DE PATERNIDAD VOLUNTARIA POSTERIOR A LA INSCRIPCIÓN DE NACIMIENTO",
        "sustento": "BASE LEGAL\n- Ley N° 27972 (27.05.03). Arts. 40 y 73.\n- Ley N° 27444 (11.04.01). Arts. 44 y 45.\n- Ley N° 29462 (28.11.04). Art. 2.\n- Ley N° 29060 (07.07.07). Arts. 1 y 2.\n- Ley N° 26497 (12.07.95). Arts. 44 y 55.\n- Decreto Supremo N° 156-2004-EF (15.11.04). Art. 68.\n- Código Civil, Decreto Legislativo N° 295 (24.07.84). Arts. 388 al 402.\n- Decreto Supremo N° 015-98-PCM (25.04.98). Arts. 3, 65, 67, 68 y 70.\n- Resolución Jefatural N° 023-96-JEF (11.04.96). Art. 1.",
        "requisitos": [
            "1 Formato de solicitud (distribución gratuita o de libre reproducción).",
            "2 La presencia del Padre y de la Madre; con su respectivo DNI vigente.",
            "3 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "0.4342% UIT (S/. 16.50 aprox.)",
        "plazo": "Inmediato (Automático)",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Sub Gerente de Registro Civil",
        "reconsideracion": "-",
        "apelacion": "-"
    },
    {
        "id": "7",
        "numero": "6.0",
        "procedimiento": "RECONOCIMIENTO DE PATERNIDAD MEDIANTE ESCRITURA PÚBLICA O TESTAMENTO",
        "sustento": "BASE LEGAL\n- Artículo 390° del Código Civil (Pub. 25-07-1984)\n- Artículo 36° del D.S. N° 015-98-PCM, Reglamento Inscripciones del Registro Nacional de Identificación y Estado (Pub. 25-04-1998)\n- Ley N° 26497, (Pub. 12-07-1995)\n- Ley N° 27972, (Pub. 27-05-2003)\n- Ley N° 27444, (Pub. 11-04-2001)\n- Ley N° 29060, (Pub. 07-07-2007)",
        "requisitos": [
            "1 Formato de solicitud (distribución gratuita o de libre reproducción).",
            "2 Presentación del DNI vigente.",
            "3 Copia certificada u original de la escritura pública o del testamento",
            "4 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "1.3211% UIT (S/. 50.20 aprox.)",
        "plazo": "10 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Sub Gerente de Registro Civil",
        "reconsideracion": "Sub Gerente de Registro Civil (Plazo de Presentación: 15 Días hábiles. Plazo de Resolución: 30 Días hábiles.)",
        "apelacion": "RENIEC (Plazo de Presentación: 15 Días hábiles. Plazo de Resolución: 30 Días hábiles.)"
    },
{
        "id": "8",
        "numero": "7.0",
        "procedimiento": "RECONOCIMIENTO DE PATERNIDAD POR DECLARACIÓN JUDICIAL Y/O NOTARIAL",
        "sustento": "BASE LEGAL\n- Ley N° 26497, (Pub. 12-07-1995)\n- D.S. N° 015-98-PCM, (Pub. 25-04-1998)\n- Ley N° 27972, (Pub. 27-05-2003)\n- Ley N° 27444, (Pub. 11-04-2001)\n- Ley N° 29060, (Pub. 07-07-2007)",
        "requisitos": [
            "1 Copia certificada u original de la Sentencia Consentida o Ejecutoriada y/o de la Resolución expedida por el Notario.",
            "2 Presentación del DNI vigente.",
            "3 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "1.3211% UIT (S/. 50.20 aprox.)",
        "plazo": "Inmediato (Automático)",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Sub Gerente de Registro Civil",
        "reconsideracion": "-",
        "apelacion": "-"
    },
    {
        "id": "9",
        "numero": "8.0",
        "procedimiento": "INSCRIPCIÓN DE ADOPCIÓN PARA EL MAYOR DE EDAD",
        "sustento": "BASE LEGAL\n- Artículo 377° al 379° del Código Civil (Pub. 25-07-1984)\n- Ley N° 26497, (Pub. 12-07-1995)\n- D.S. N° 015-98-PCM, (Pub. 25-04-1998)\n- Ley N° 27972, (Pub. 27-05-2003)\n- Ley N° 27444, (Pub. 11-04-2001)\n- Ley N° 29060, (Pub. 07-07-2007)",
        "requisitos": [
            "1 Partes judiciales con sentencia consentida y/o ejecutoriada por duplicado",
            "2 La persona que presenta el parte deberá presentar solicitud y DNI.",
            "3 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "1.3158% UIT (S/. 50.00 aprox.)",
        "plazo": "10 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Sub Gerente de Registro Civil",
        "reconsideracion": "Sub Gerente de Registro Civil (Plazo de Presentación: 15 Días hábiles. Plazo de Resolución: 30 Días hábiles.)",
        "apelacion": "RENIEC (Plazo de Presentación: 15 Días hábiles. Plazo de Resolución: 30 Días hábiles.)"
    },
    {
        "id": "10",
        "numero": "9.0",
        "procedimiento": "INSCRIPCIÓN DE ADOPCIÓN PARA EL MENOR DE EDAD",
        "sustento": "BASE LEGAL\n- Artículo 377° al 379° del Código Civil (Pub. 25-07-1984)\n- Ley N° 26497, (Pub. 12-07-1995)\n- D.S. N° 015-98-PCM, (Pub. 25-04-1998)\n- Ley N° 27972, (Pub. 27-05-2003)\n- Ley N° 27444, (Pub. 11-04-2001)\n- Ley N° 29060, (Pub. 07-07-2007)",
        "requisitos": [
            "1 Partes judiciales con sentencia consentida y/o ejecutoriada por duplicado",
            "2 La persona que presenta el parte deberá presentar solicitud y DNI.",
            "3 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "1.3158% UIT (S/. 50.00 aprox.)",
        "plazo": "10 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Sub Gerente de Registro Civil",
        "reconsideracion": "Sub Gerente de Registro Civil (Plazo de Presentación: 15 Días hábiles. Plazo de Resolución: 30 Días hábiles.)",
        "apelacion": "RENIEC (Plazo de Presentación: 15 Días hábiles. Plazo de Resolución: 30 Días hábiles.)"
    },
{
        "id": "11",
        "numero": "10.0",
        "procedimiento": "INSCRIPCIÓN ORDINARIA DE DEFUNCIÓN",
        "sustento": "BASE LEGAL\n- Ley N° 27972 (27.05.03). Arts. 40 y 73.\n- Ley N° 27444 (11.04.01). Arts. 44 y 45.\n- Ley N° 29462 (28.11.04). Art. 2.\n- Ley N° 29060 (07.07.07). Arts. 1 y 2.\n- Ley N° 26497 (12.07.95). Arts. 44 y 55.\n- Decreto Supremo N° 156-2004-EF (15.11.04). Art. 68.\n- Decreto Supremo N° 015-98-PCM (25.04.98). Arts. 3, 49, 50, 53, 65, 67, 70 y 98.\n- Resolución Jefatural N° 782-JNAC-RENIEC (26.11.09)\n- Resolución Jefatural N° 023-96-JEF (11.04.96). Art. 1.",
        "requisitos": [
            "1 Certificado Médico de Defunción expedido por el profesional competente (original con sello y firma), de no haber en la localidad un médico, se requiere la Declaración Jurada de la autoridad Policial, judicial o religiosa confirmando el deceso.",
            "2 Presentación del DNI del declarante.",
            "3 Presentación del DNI del occiso."
        ],
        "derecho_tramite": "GRATUITO",
        "plazo": "Inmediato (Automático)",
        "inicio": "Sub Gerencia de Registro Civil",
        "autoridad": "Sub Gerente de Registro Civil",
        "reconsideracion": "-",
        "apelacion": "-"
    },
    {
        "id": "12",
        "numero": "11.0",
        "procedimiento": "INSCRIPCIÓN VÍA POLICIAL (EN CASO DE MUERTE VIOLENTA)",
        "sustento": "BASE LEGAL\n- Ley N° 27972 (27.05.03). Arts. 40 y 73.\n- Ley N° 27444 (11.04.01). Arts. 44 y 45.\n- Ley N° 29462 (28.11.04). Art. 2.\n- Ley N° 29060 (07.07.07). Arts. 1 y 2.\n- Ley N° 26497 (12.07.95). Arts. 44 y 55.\n- Decreto Supremo N° 156-2004-EF (15.11.04). Art. 68.\n- Decreto Supremo N° 015-98-PCM (25.04.98). Arts. 3, 49, 50, 53, 65, 67, 70 y 98.\n- Resolución Jefatural N° 782-JNAC-RENIEC (26.11.09)\n- Resolución Jefatural N° 023-96-JEF (11.04.96). Art. 1.",
        "requisitos": [
            "1 Certificado Médico de Defunción expedido por el médico legista competente (original con sello y firma).",
            "2 Original o copia certificada del Parte Policial de ser necesario.",
            "3 Documento de Identidad del fallecido o constancia de inscripción expedido por la RENIEC."
        ],
        "derecho_tramite": "GRATUITO",
        "plazo": "10 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Sub Gerente de Registro Civil",
        "reconsideracion": "Sub Gerente de Registro Civil (Plazo de Presentación: 15 Días hábiles. Plazo de Resolución: 30 Días hábiles.)",
        "apelacion": "RENIEC (Plazo de Presentación: 15 Días hábiles. Plazo de Resolución: 30 Días hábiles.)"
    },
{
        "id": "13",
        "numero": "12.0",
        "procedimiento": "INSCRIPCIÓN DE DEFUNCIÓN POR MANDATO JUDICIAL",
        "sustento": "BASE LEGAL\n- Ley N° 27972 (27.05.03). Arts. 40 y 73.\n- Ley N° 27444 (11.04.01). Arts. 44 y 45.\n- Ley N° 29462 (28.11.04). Art. 2.\n- Ley N° 29060 (07.07.07). Arts. 1 y 2.\n- Ley N° 26497 (12.07.95). Arts. 44 y 55.\n- Decreto Supremo N° 156-2004-EF (15.11.04). Art. 68.\n- Decreto Supremo N° 015-98-PCM (25.04.98). Arts. 3, 49, 50, 53, 65, 67, 70 y 98.\n- Informe Defensorial N° DP/AAE-2006-017 (17.03.06).\n- Resolución Jefatural N° 023-96-JEF (11.04.96). Art. 1.",
        "requisitos": [
            "1 Oficio de la autoridad competente solicitando la inscripción.",
            "2 Copia certificada u original de la Sentencia consentida o ejecutoriada.",
            "3 Documento de Identidad del fallecido o constancia de inscripción expedido por la RENIEC."
        ],
        "derecho_tramite": "GRATUITO",
        "plazo": "Inmediato (Automático)",
        "inicio": "Sub Gerencia de Registro Civil",
        "autoridad": "Sub Gerente de Registro Civil",
        "reconsideracion": "-",
        "apelacion": "-"
    },
    {
        "id": "14",
        "numero": "13.0",
        "procedimiento": "INSCRIPCIÓN DE DEFUNCIÓN FETAL",
        "sustento": "BASE LEGAL\n- Ley N° 26497, (Pub. 12-07-1995)\n- D.S. N° 015-98-PCM, (Pub. 25-04-1998)\n- Ley N° 27972, (Pub. 27-05-2003)\n- Ley N° 27444, (Pub. 11-04-2001)\n- Ley N° 29060, (Pub. 07-07-2007)",
        "requisitos": [
            "1 Certificado original de Defunción Fetal expedido por profesional competente.",
            "2 Presentación del DNI vigente del Declarante."
        ],
        "derecho_tramite": "GRATUITO",
        "plazo": "Inmediato (Automático)",
        "inicio": "Sub Gerencia de Registro Civil",
        "autoridad": "Sub Gerente de Registro Civil",
        "reconsideracion": "-",
        "apelacion": "-"
    },
    {
        "id": "15",
        "numero": "14.0",
        "procedimiento": "INSCRIPCIÓN DE MATRIMONIO EN ARTÍCULO MORTIS (PELIGRO DE MUERTE)",
        "sustento": "BASE LEGAL\n- Ley N° 27972 (27.05.03). Arts. 40 y 73.\n- Ley N° 27444 (11.04.01). Arts. 44 y 45.\n- Ley N° 29462 (28.11.04). Art. 2.\n- Ley N° 29060 (07.07.07). Arts. 1 y 2.\n- Ley N° 26497 (12.07.95). Arts. 44 y 55.\n- Código Civil, Decreto Legislativo N° 295 (24.07.84). Arts. 260 y 268.\n- Decreto Supremo N° 156-2004-EF (15.11.04). Art. 68.\n- Decreto Supremo N° 015-98-PCM (25.04.98). Arts. 3, 44, 65, 67, 70 y 98.\n- Resolución Jefatural N° 023-96-JEF (11.04.96). Art. 1.",
        "requisitos": [
            "1 Acta expedida por el párroco que celebró el matrimonio.",
            "2 Expediente matrimonial.",
            "3 Presentación del Documento Nacional de Identidad."
        ],
        "derecho_tramite": "GRATUITO",
        "plazo": "10 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Sub Gerente de Registro Civil",
        "reconsideracion": "Sub Gerente de Registro Civil (Plazo de Presentación: 15 Días hábiles. Plazo de Resolución: 30 Días hábiles.)",
        "apelacion": "RENIEC (Plazo de Presentación: 15 Días hábiles. Plazo de Resolución: 30 Días hábiles.)"
    },
{
        "id": "16",
        "numero": "15.0",
        "procedimiento": "INSCRIPCIÓN DE MATRIMONIO CELEBRADO EN EL EXTRANJERO",
        "sustento": "BASE LEGAL\n- Ley N° 27972 (27.05.03). Arts. 40 y 73.\n- Ley N° 27444 (11.04.01). Arts. 44 y 45.\n- Ley N° 29462 (28.11.04). Art. 2.\n- Ley N° 29060 (07.07.07). Arts. 1 y 2.\n- Ley N° 26497 (12.07.95). Arts. 44 y 55.\n- Decreto Supremo N° 156-2004-EF (15.11.04). Art. 68.\n- Decreto Supremo N° 015-98-PCM (25.04.98). Arts. 3, 47, 65, 67, 70 y 98.\n- Resolución Jefatural N° 023-96-JEF (11.04.96). Art. 1.",
        "requisitos": [
            "1 Partida de matrimonio original visada por el Cónsul Peruano del país de origen y legalizada por el Ministerio de Relaciones Exteriores del Perú con traducción oficial en el Perú del ser el caso.",
            "2 Presentación del Documento Nacional de Identidad."
        ],
        "derecho_tramite": "GRATUITO",
        "plazo": "15 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Sub Gerente de Registro Civil",
        "reconsideracion": "Sub Gerente de Registro Civil (Plazo de Presentación: 15 Días hábiles. Plazo de Resolución: 30 Días hábiles.)",
        "apelacion": "RENIEC (Plazo de Presentación: 15 Días hábiles. Plazo de Resolución: 30 Días hábiles.)"
    },
    {
        "id": "17",
        "numero": "16.0",
        "procedimiento": "INSCRIPCIÓN DE MATRIMONIO POR MANDATO JUDICIAL",
        "sustento": "BASE LEGAL\n- Ley N° 27972 (27.05.03). Arts. 40 y 73.\n- Ley N° 27444 (11.04.01). Arts. 44 y 45.\n- Ley N° 29462 (28.11.04). Art. 2.\n- Ley N° 29060 (07.07.07). Arts. 1 y 2.\n- Ley N° 26497 (12.07.95). Arts. 44 y 55.\n- Decreto Supremo N° 156-2004-EF (15.11.04). Art. 68.\n- Decreto Supremo N° 015-98-PCM (25.04.98). Arts. 3, 43, 65, 67 y 70.\n- Resolución Jefatural N° 023-96-JEF (11.04.96). Art. 1.\n- Informe Defensorial N° DP/AAE-2006-017 (17.03.06).",
        "requisitos": [
            "1 Oficio de la autoridad competente solicitando la inscripción",
            "2 Copia certificada u original de la Sentencia Consentida o Ejecutoriado",
            "3 Presentación del Documento Nacional de Identidad."
        ],
        "derecho_tramite": "GRATUITO",
        "plazo": "Inmediato (Automático)",
        "inicio": "Sub Gerencia de Registro Civil",
        "autoridad": "Sub Gerente de Registro Civil",
        "reconsideracion": "-",
        "apelacion": "-"
    },
{
        "id": "18",
        "numero": "17.0",
        "procedimiento": "ANOTACIONES MARGINALES EN PARTIDA DE NACIMIENTO, MATRIMONIO Y DEFUNCIÓN",
        "sustento": "BASE LEGAL\n- Ley N° 27972 (27.05.03). Arts. 40 y 73.\n- Ley N° 27444 (11.04.01). Arts. 44 y 45.\n- Ley N° 29462 (28.11.04). Art. 2.\n- Ley N° 29060 (07.07.07). Arts. 1 y 2.\n- Ley N° 26497 (12.07.95). Arts. 44 y 55.\n- Decreto Supremo N° 156-2004-EF (15.11.04). Art. 68.\n- Decreto Supremo N° 015-98-PCM (25.04.98). Arts. 3, 65, 67 y 70.\n- Resolución Jefatural N° 023-96-JEF (11.04.96). Art. 1.\n- Informe Defensorial N° DP/AAE-2006-017 (17.03.06).\n- Decreto Legislativo N° 1049 (26.06.08).",
        "requisitos": [
            "Por mandato judicial:\n   1 Formato de solicitud (distribución gratuita o de libre reproducción).\n   2 Copia certificada u original de la Sentencia Consentida o Ejecutoriada.\n   3 Copia del Documento Nacional de Identidad del solicitante.",
            "Por parte notarial:\n   1 Formato de solicitud (distribución gratuita o de libre reproducción).\n   2 Copia certificada del documento Notarial u original.\n   3 Copia de Documento Nacional de Identidad del solicitante.",
            "Por Rectificación Administrativo:\n   1 Formato de solicitud (distribución gratuita o de libre reproducción).\n   2 Copia del acta que consigna el error, omisión y enmendadura:\n     a. Cuando se determine algún error en la inscripción\n     b. Cuando se haya omitido alguna información relativa a la inscripción",
            "1 Por cualquiera de las tres modalidades el Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "1.4158% UIT (S/. 53.80 aprox.)",
        "plazo": "15 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Sub Gerente de Registro Civil",
        "reconsideracion": "Sub Gerente de Registro Civil (Plazo de Presentación: 15 Días hábiles. Plazo de Resolución: 30 Días hábiles.)",
        "apelacion": "RENIEC (Plazo de Presentación: 15 Días hábiles. Plazo de Resolución: 30 Días hábiles.)"
    },
{
        "id": "19",
        "numero": "18.0",
        "procedimiento": "RECTIFICACIÓN ADMINISTRATIVA DE ACTA DE NACIMIENTO, MATRIMONIO O DEFUNCIÓN, POR ERROR Y OMISIÓN",
        "sustento": "BASE LEGAL\n- Ley N° 27972 (27.05.03). Arts. 40 y 73.\n- Ley N° 27444 (11.04.01). Arts. 44 y 45.\n- Ley N° 29462 (28.11.04). Art. 2.\n- Ley N° 29060 (07.07.07). Arts. 1 y 2.\n- Ley N° 26497 (12.07.95). Arts. 44 y 55.\n- Decreto Supremo N° 156-2004-EF (15.11.04). Art. 68.\n- Decreto Supremo N° 015-98-PCM (25.04.98). Arts. 3, 65, 67, 70, 71, 72, 97 y 98.\n- Resolución Jefatural N° 023-96-JEF (11.04.96). Art. 1.\n- Resolución Jefatural N° 0594-2009-JNAC RENIEC (11.04.96).",
        "requisitos": [
            "ATRIBUIBLE AL REGISTRADOR:\n   1 Formato de solicitud (distribución gratuita o de libre reproducción).\n   2 Copia de Documento Nacional de Identidad del solicitante.\n   3 Copia del documento a rectificar.\n   4 Copia del Edicto en Diario de mayor circulación de la Región, cuando se declara procedente la solicitud.",
            "NO ATRIBUIBLE AL REGISTRADOR:\n   1 Formato de solicitud (distribución gratuita o de libre reproducción).\n   2 Copia de Documento Nacional de Identidad del solicitante.\n   3 Pago por el Derecho de la Tasa Administrativa:\n   4 Copia del Edicto en Diario de mayor circulación de la Región, cuando se declara procedente la solicitud.\n   5 Copia, según sea el caso, de los siguientes documentos, en forma adicional:\n\n   Acta de Nacimiento:\n   1 Copia certificada del acta de nacimiento de los padres o partida de bautismo de estos, en este último caso inscrito antes del 14 de noviembre de 1936.\n   2 Copia certificada del acta de nacimiento del declarante o partida de bautismo en en último caso inscritas antes del 14 de noviembre de 1936.\n\n   Acta de Matrimonio:\n   1 Copia certificada del acta de nacimiento de los contrayentes o partida o partida de bautismo de éstos, en este último caso inscrito antes del 14 de noviembre de 1936.\n   2 Copia certificada de nacimiento de testigos o partida de bautismos de estos, en este último caso inscrito antes del 14 de noviembre de 1936.\n\n   Acta de Defunción:\n   1 Copia certificada del acta de nacimiento del difunto.\n   2 Constancia de inscripción del RENIEC.\n   3 Copia certificada del acta de nacimiento de los padres o partida de bautismo de éstos, en este último caso inscrita antes del 14 de noviembre de 1936.\n   4 Copia certificada del acta del acta de matrimonio del difunto.\n   5 Copia certificada del acta de nacimiento del cónyuge o partida de bautismo de éste ultimo caso inscrita antes del 14 de noviembre de 1936."
        ],
        "derecho_tramite": "1.0526% UIT (S/. 40.00 aprox.)",
        "plazo": "15 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Sub Gerente de Registro Civil",
        "reconsideracion": "Sub Gerente de Registro Civil (Plazo de Presentación: 15 Días hábiles. Plazo de Resolución: 30 Días hábiles.)",
        "apelacion": "RENIEC (Plazo de Presentación: 15 Días hábiles. Plazo de Resolución: 30 Días hábiles.)"
    },
{
        "id": "20",
        "numero": "19.0",
        "procedimiento": "APERTURA DE PLIEGO MATRIMONIAL",
        "sustento": "BASE LEGAL\n- Ley N° 27972 (27.05.03). Arts. 20, 40 y 44.\n- Ley N° 27444 (11.04.01). Arts. 44 y 45.\n- Código Civil, Decreto Legislativo N° 295 (24.07.84). Arts. 241, 244, 248, 250, 261, 264 y 265.\n- Ley N° 26497 (12.07.95). Arts. 7 y 26.\n- Resolución Jefatural N° 023-96-JEF (11.04.96). Art. 1.\n- Convenio de la Haya sobre Convenio que suprime la exigencia de legalización de documentos públicos extranjeros (apostilla), aprobado mediante Resolución Legislativa 29445.",
        "requisitos": [
            "REQUISITOS GENERALES:\n   1 Acta de nacimiento legible de cada uno de los contrayentes o dispensa judicial.\n   2 Copia autenticada por fedatario municipal del Documento Nacional de Identidad de los contrayentes y exhibición de los originales en la ceremonia\n   3 Copia autenticada por fedatario municipal del Documento Nacional de Identidad de dos testigos y exhibición de los originales en la ceremonia.\n   4 Declaración jurada de los testigos de conocer a los contrayentes.\n   5 Certificado médico de los contrayentes (vigencia tres meses luego de su expedición).\n   6 Declaración Jurada del estado civil actual de los contrayentes\n   7 Declaración jurada de domicilio de cada contrayente.\n   8 Por cualquiera de las modalidades el Pago por el Derecho de la Tasa Administrativa:",
            "REQUISITOS ADICIONALES SEGÚN CORRESPONDA:\n\n   PARA MENORES DE EDAD\n   1 Autorización expresa de los padres, de no existir éstos últimos, de los ascendientes y a falta de éstos la autorización judicial, conforme lo indica el artículo 244 del Código Civil.\n\n   PARA DIVORCIADOS (AS)\n   1 Partida de matrimonio con la inscripción del divorcio o anulación del matrimonio anterior.\n   2 Copia autenticada por fedatario municipal del Documento Nacional de Identidad en el que figure el estado civil actualizado.\n   3 Declaración jurada de no administrar bienes de hijos menores.\n\n   PARA VIUDOS (AS)\n   1 Partida de defunción de cónyuge fallecido.\n   2 Copia autenticada por fedatario municipal del Documento Nacional de Identidad en el que figure el estado civil actualizado.\n\n   PARA EXTRANJEROS (AS)\n   1 Partida de nacimiento y/o certificado de naturalización según corresponda, visado por el Cónsul peruano en el país de origen, legalizado por el Ministerio de Relaciones Exteriores o apostillado, con traducción oficial de ser el caso.\n   2 Copia de pasaporte y/o carné de extranjería autenticado por fedatario municipal.\n   3 En caso de ser divorciado, presentará partida de matrimonio anterior con la disolución o sentencia del divorcio, con las visaciones respectivas, o apostillado.\n\n   PARA MATRIMONIOS POR PODER\n   1 Poder por Escritura Pública inscrito en los Registros Públicos. Si el poder fue otorgado en el extranjero debe estar visado por el Cónsul peruano del país donde lo dió el poderdante, debiendo legalizarlo en el Ministerio de Relaciones Exteriores y con traducción oficial de ser el caso.\n   2 Copia autenticada por fedatario municipal del Documento Nacional de Identidad del apoderado.\n   Nota: Con posterioridad a la presentación del expediente, se deberá cumplir con la publicación del edicto matrimonial o gestionar la dispensa de publicación del mismo."
        ],
        "derecho_tramite": "1.3184% UIT (S/. 50.10 aprox.)",
        "plazo": "Inmediato (Automático)",
        "inicio": "Sub Gerencia de Registro Civil",
        "autoridad": "Sub Gerente de Registro Civil",
        "reconsideracion": "-",
        "apelacion": "-"
    },
{
        "id": "21",
        "numero": "20.0",
        "procedimiento": "COPIA CERTIFICADA DE ACTA DE NACIMIENTO, MATRIMONIO O DEFUNCIÓN Y EXTRACTO DE LAS INSCRIPCIONES",
        "sustento": "BASE LEGAL\n- Ley N° 27972 (27.05.03). Arts. 40 y 44.\n- Ley N° 27444 (11.04.01). Arts. 37, 40, 44 y 45.\n- Decreto Supremo N° 156-2004-EF (15.11.04). Art. 68.\n- Decreto Supremo N° 015-98-PCM (25.04.98). Arts. 4, 62, 63, 64 y 97.\n- Resolución Jefatural N° 023-96-JEF (11.04.96). Art. 1.",
        "requisitos": [
            "1 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "0.3421% UIT (S/. 13.00 aprox.)",
        "plazo": "Inmediato (Automático)",
        "inicio": "Sub Gerencia de Registro Civil",
        "autoridad": "Sub Gerente de Registro Civil",
        "reconsideracion": "-",
        "apelacion": "-"
    },
    {
        "id": "22",
        "numero": "21.0",
        "procedimiento": "COPIA CERTIFICADA DE DOCUMENTOS INSERTOS QUE OBRAN EN EL ARCHIVO DE REGISTROS CIVILES",
        "sustento": "BASE LEGAL\n- Ley N° 27972 (27.05.03). Arts. 40 y 44.\n- Ley N° 27444 (11.04.01). Arts. 37, 40, 44 y 45.\n- Decreto Supremo N° 156-2004-EF (15.11.04). Art. 68.\n- Resolución Jefatural N° 023-96-JEF (11.04.96). Art. 1.",
        "requisitos": [
            "1 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "0.5263% UIT (S/. 20.00 aprox.)",
        "plazo": "Inmediato (Automático)",
        "inicio": "Sub Gerencia de Registro Civil",
        "autoridad": "Sub Gerente de Registro Civil",
        "reconsideracion": "-",
        "apelacion": "-"
    },
{
        "id": "23",
        "numero": "22.0",
        "procedimiento": "LEGALIZACIÓN DE PARTIDA PARA EL EXTRANJERO (INCLUYE EXPEDICIÓN DE PARTIDA DE NACIMIENTO, MATRIMONIO O DE DEFUNCIÓN)",
        "sustento": "BASE LEGAL\n- Ley N° 27972 (27.05.03). Arts. 40 y 44.\n- Ley N° 27444 (11.04.01). Arts. 37, 40, 44 y 45.\n- Decreto Supremo N° 156-2004-EF (15.11.04). Art. 68.\n- Resolución Jefatural N° 023-96-JEF (11.04.96). Art. 1.",
        "requisitos": [
            "1 Copia de la Constancia de inscripción de tenerse.",
            "2 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "0.5263% UIT (S/. 20.00 aprox.)",
        "plazo": "Inmediato (Automático)",
        "inicio": "Sub Gerencia de Registro Civil",
        "autoridad": "Sub Gerente de Registro Civil",
        "reconsideracion": "-",
        "apelacion": "-"
    },
    {
        "id": "24",
        "numero": "23.0",
        "procedimiento": "EXHIBICIÓN DE EDICTOS MATRIMONIALES TRAMITADOS EN OTROS MUNICIPIOS",
        "sustento": "BASE LEGAL\n- Ley N° 27972 (27.05.03). Arts. 40 y 44.\n- Ley N° 27444 (11.04.01). Arts. 37, 40, 44 y 45.\n- Decreto Supremo N° 156-2004-EF (15.11.04). Art. 68.\n- Resolución Jefatural N° 023-96-JEF (11.04.96). Art. 1.",
        "requisitos": [
            "1 Presentación del edicto matrimonial.",
            "2 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "0.5474% UIT (S/. 20.80 aprox.)",
        "plazo": "Inmediato (Automático)",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Sub Gerente de Registro Civil",
        "reconsideracion": "-",
        "apelacion": "-"
    },
    {
        "id": "25",
        "numero": "24.0",
        "procedimiento": "REPROGRAMACIÓN DE FECHA DE MATRIMONIO (PEDIDO EFECTUADO CON ANTICIPACIÓN)",
        "sustento": "BASE LEGAL\n- Ley N° 27972 (27.05.03). Arts. 40 y 44.\n- Ley N° 27444 (11.04.01). Arts. 37, 40, 44 y 45.\n- Decreto Supremo N° 156-2004-EF",
        "requisitos": [
            "1 Solicitud según formulario (Libre reproducción).",
            "2 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "0.5237% UIT (S/. 19.90 aprox.)",
        "plazo": "Inmediato (Automático)",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Sub Gerente de Registro Civil",
        "reconsideracion": "-",
        "apelacion": "-"
    },
{
        "id": "26",
        "numero": "25.0",
        "procedimiento": "CONSTANCIA DE NO INSCRIPCION DE NACIMIENTOS",
        "sustento": "BASE LEGAL\n- Ley Nº 26427\n- D.S Nº 015-98-PCM",
        "requisitos": [
            "1 Solicitud dirigida a la Oficina de Registros Civiles",
            "2 Copia autenticada del documento de identidad vigente del solicitante",
            "3 Copia del Certificado de nacido vivo expedido por el nosocomio correspondiente o declaración jurada si en caso haya extraviado el Certificado de nacido vivo",
            "4 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "0.3947% UIT (S/. 15.00 aprox.)",
        "plazo": "Inmediato (Automático)",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Sub Gerente de Registro Civil",
        "reconsideracion": "-",
        "apelacion": "-"
    },
    {
        "id": "27",
        "numero": "26.0",
        "procedimiento": "CONSTANCIA DE ESTADO CIVIL",
        "sustento": "BASE LEGAL\n- Ley Nº 26427\n- D.S Nº 015-98-PCM",
        "requisitos": [
            "1 Solicitud dirigida a la Oficina de Registros Civiles",
            "2 Copia autenticada del documento de identidad vigente (Debe consignar domicilio en San Ramón o de ser el caso presentar declaración jurada de domicilio). En caso de extranjeros, carné de extranjería",
            "3 En caso de viudez presentar partida de defunción del cónyuge",
            "4 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "0.4053% UIT (S/. 15.40 aprox.)",
        "plazo": "Inmediato (Automático)",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Sub Gerente de Registro Civil",
        "reconsideracion": "-",
        "apelacion": "-"
    },
    {
        "id": "28",
        "numero": "27.0",
        "procedimiento": "COPIA CERTIFICADA DE PARTIDA DE NACIMIENTO PARA SERVICIO MILITAR",
        "sustento": "BASE LEGAL\n- Ley Nº 26427\n- D.S Nº 015-98-PCM",
        "requisitos": [
            "1 Indicar el nombre y fecha de nacimiento del Titular",
            "2 Presentación del DNI del solicitante"
        ],
        "derecho_tramite": "GRATUITO",
        "plazo": "Inmediato (Automático)",
        "inicio": "Sub Gerencia de Registro Civil",
        "autoridad": "Sub Gerente de Registro Civil",
        "reconsideracion": "-",
        "apelacion": "-"
    },
    {
        "id": "29",
        "numero": "28.0",
        "procedimiento": "DISPENSA DE PUBLICACIÓN DE EDICTOS (TOTAL O PARCIAL)",
        "sustento": "BASE LEGAL\n- Ley Nº 26497\n- D.S Nº 015-98-PCM",
        "requisitos": [
            "1 Solicitud dirigida a la Oficina de Registros Civiles señalando los motivos de la dispensa",
            "2 Adjuntar documentos que acrediten las causas razonables para la solicitud",
            "3 Copia legalizada o autenticada del documento de identidad vigente",
            "4 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "0.5474% UIT (S/. 20.80 aprox.)",
        "plazo": "10 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Sub Gerente de Registro Civil",
        "reconsideracion": "-",
        "apelacion": "-"
    },
{
        "id": "30",
        "numero": "29.0",
        "procedimiento": "CELEBRACIÓN DE MATRIMONIO EN DÍA LABORABLE (LUNES A VIERNES)",
        "sustento": "BASE LEGAL\n- Código Civil, Decreto Legislativo Nº 295 (24.07.84). Arts. 241, 244, 248, 250, 261, 264 y 265.",
        "requisitos": [
            "1 Pronunciamiento favorable de la apertura del pliego matrimonial",
            "2 Pago por el Derecho de la Tasa Administrativa:\n\n   En el local Municipal:\n   * Con presencia del Alcalde y/o autoridad que delega: 1.8947% UIT (S/. 72.00 aprox.)\n   * Con presencia del Registrador: 1.4132% UIT (S/. 53.70 aprox.)\n\n   Fuera del Local Municipal (dentro del Distrito):\n   * Con presencia del Alcalde y/o autoridad que delega: 6.5763% UIT (S/. 249.90 aprox.)\n   * Con presencia del Registrador: 5.7895% UIT (S/. 220.00 aprox.)\n\n   Fuera del Local Municipal (fuera del Distrito):\n   * Con presencia del Alcalde y/o autoridad que delega: 11.4974% UIT (S/. 436.90 aprox.)\n   * Con presencia del Registrador: 10.5263% UIT (S/. 400.00 aprox.)"
        ],
        "derecho_tramite": "Variable según modalidad",
        "plazo": "Inmediato (Automático)",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Sub Gerente de Registro Civil",
        "reconsideracion": "-",
        "apelacion": "-"
    },
    {
        "id": "31",
        "numero": "30.0",
        "procedimiento": "CELEBRACIÓN DE MATRIMONIO EN DÍA NO LABORABLE",
        "sustento": "BASE LEGAL\n- Código Civil, Decreto Legislativo Nº 295 (24.07.84). Arts. 241, 244, 248, 250, 261, 264 y 265.",
        "requisitos": [
            "1 Pronunciamiento favorable de la apertura del pliego matrimonial",
            "2 Pago por el Derecho de la Tasa Administrativa:\n\n   En el Local de la Municipalidad:\n   * Con presencia del Alcalde y/o autoridad que delega: 6.5289% UIT (S/. 248.10 aprox.)\n   * Con presencia del Registrador: 6.5263% UIT (S/. 248.00 aprox.)\n\n   Fuera del Local Municipal (dentro del Distrito):\n   * Con presencia del Alcalde y/o autoridad que delega: 7.6605% UIT (S/. 291.10 aprox.)\n   * Con presencia del Registrador: 7.3816% UIT (S/. 280.50 aprox.)\n\n   Fuera del Local Municipal (fuera del Distrito):\n   * Con presencia del Alcalde y/o autoridad que delega: 11.7789% UIT (S/. 447.60 aprox.)\n   * Con presencia del Registrador: 11.6289% UIT (S/. 441.90 aprox.)"
        ],
        "derecho_tramite": "Variable según modalidad",
        "plazo": "Inmediato (Automático)",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Sub Gerente de Registro Civil",
        "reconsideracion": "-",
        "apelacion": "-"
    },
{
        "id": "32",
        "numero": "31.0",
        "procedimiento": "PRESENTACIÓN DE DECLARACIÓN JURADA PARA LA INSCRIPCIÓN (IMPUESTO PREDIAL)",
        "sustento": "BASE LEGAL\n- TUO de la Ley de Tributación Municipal, Decreto Supremo Nº 156-2004-EF y modificatorias (15.11.04). Arts. 14 .\n- TUO del Código Tributario, Decreto Supremo Nº 135-99-EF y modificatorias (19.08.99). Art. 88.",
        "requisitos": [
            "1 Presentar el formulario proporcionado por la Municipalidad",
            "2 Exhibir el documento de identidad del propietario o de su representante, de ser el caso, y presentar copia simple del mismo.",
            "3 Exhibir el último recibo de luz, agua, cable o teléfono del domicilio del propietario.",
            "4 En el caso de representación, presentar poder específico en documento público o privado con firma legalizada ante notario.",
            "5 En caso de inscripción de predios* realizado por el propietario debe exhibir el original y presentar copia simple del documento que sustente la adquisición:\n   a) Compra: Contrato de compraventa.\n   b) Donación: Escritura pública de donación.\n   c) Herencia: Partida de defunción, declaratoria de herederos, testamento, sentencia o escritura pública que señala la división y partición de los bienes.\n   d) Remate: Resolución Judicial o Administrativa consentida mediante la cual se adjudica el bien\n   e) Permuta: Contrato de permuta.\n   e) Fusión: Copia literal de la inscripción en Registros Públicos donde conste la fecha de vigencia del acuerdo de fusión\n   f) En los demás casos, documento que acredite la propiedad.",
            "6 En caso de inscripción de predios realizada por poseedores, cuando la existencia del propietario no pudiera ser determinada, exhibir el original y presentar copia simple de los documentos que acrediten su calidad de posesionario, tales como, certificado de posesión, Declaración Jurada de los vecinos, recibo de agua, luz o teléfono y de ser necesario otros documentos que la Administración le solicite.",
            "7 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "0.2868% UIT (S/. 10.90 aprox.)",
        "plazo": "Inmediato (Automático)",
        "inicio": "Sub Gerencia de Registro y Recaudación",
        "autoridad": "Sub Gerente de Registro y Recaudación",
        "reconsideracion": "-",
        "apelacion": "-"
    },
{
        "id": "33",
        "numero": "32.0",
        "procedimiento": "PRESENTACIÓN DE DECLARACIÓN JURADA RECTIFICATORIA QUE AUMENTA O MANTIENE LA BASE IMPONIBLE",
        "sustento": "BASE LEGAL\n- TUO del Código Tributario, Decreto Supremo N° 135-99-EF y modificatorias (19.08.99). Art. 88.\n- TUO de la Ley de Tributación Municipal, Decreto Supremo N° 156-2004-EF y modificatorias (15.11.04). Arts. 14 .",
        "requisitos": [
            "1 Presentar el formulario proporcionado por la Municipalidad",
            "2 Exhibir el documento de identidad del propietario o de su representante, de ser el caso, y presentar copia simple del mismo.",
            "3 En el caso de representación, presentar poder específico en documento público o privado con firma legalizada ante notario.",
            "4 Exhibir original y presentar copia simple de los documentos sustentatorios de la rectificación realizada de ser necesario.",
            "5 Adicionalmente, podrá presentar el resultado de la inspección realizada (Ficha de Inspección Predial)."
        ],
        "derecho_tramite": "GRATUITO",
        "plazo": "Inmediato (Automático)",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Sub Gerente de Registro y Recaudación",
        "reconsideracion": "-",
        "apelacion": "-"
    },
    {
        "id": "34",
        "numero": "33.0",
        "procedimiento": "PRESENTACIÓN DE DECLARACIÓN JURADA RECTIFICATORIA QUE DISMINUYE LA BASE IMPONIBLE",
        "sustento": "BASE LEGAL\n- TUO del Código Tributario, Decreto Supremo N° 135-99-EF y modificatorias (19.08.99). Art. 88.\n- TUO de la Ley de Tributación Municipal, Decreto Supremo N° 156-2004-EF y modificatorias (15.11.04). Arts. 14 .",
        "requisitos": [
            "1 Presentar el formulario proporcionado por la Municipalidad",
            "2 Exhibir el documento de identidad del propietario o de su representante, de ser el caso, y presentar copia simple del mismo.",
            "3 En el caso de representación, presentar poder específico en documento público o privado con firma legalizada ante notario.",
            "4 Exhibir original y presentar copia simple de los documentos sustentatorios de la rectificación realizada de ser necesario.",
            "5 Adicionalmente, podrá presentar el resultado de la inspección realizada (Ficha de Inspección Predial).",
            "6 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "1.1632% UIT (S/. 44.20 aprox.)",
        "plazo": "30 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Sub Gerente de Registro y Recaudación",
        "reconsideracion": "Sub Gerente de Registro y Recaudación (Plazo de Presentación: 15 Días hábiles. Plazo de Resolución: 30 Días hábiles.)",
        "apelacion": "Gerente de Rentas (Plazo de Presentación: 15 Días hábiles. Plazo de Resolución: 30 Días hábiles.)"
    },
    {
        "id": "35",
        "numero": "34.0",
        "procedimiento": "PRESENTACIÓN DE DECLARACIÓN JURADA DE TRANSFERENCIA O DESCARGO (BAJA IMPUESTO PREDIAL)",
        "sustento": "BASE LEGAL\n- TUO de la Ley de Tributación Municipal, Decreto Supremo N° 156-2004-EF y modificatorias (15.11.04). Arts. 14 .\n- TUO del Código Tributario, Decreto Supremo N° 135-99-EF y modificatorias (19.08.99). Art. 88.",
        "requisitos": [
            "1 Presentar el formulario proporcionado por la Municipalidad",
            "2 Exhibir el documento de identidad del propietario o de su representante, de ser el caso, y presentar copia simple del mismo.",
            "3 En el caso de representación, presentar poder específico en documento público o privado con firma legalizada ante notario.",
            "4 Exhibir original y presentar copia simple del documento que acredite la transferencia o descargo.",
            "5 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "0.1526% UIT (S/. 5.80 aprox.)",
        "plazo": "Inmediato (Automático)",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Sub Gerente de Registro y Recaudación",
        "reconsideracion": "-",
        "apelacion": "-"
    },
{
        "id": "36",
        "numero": "35",
        "procedimiento": "PRESENTACIÓN DE DECLARACIÓN JURADA DE CAMBIO DE DOMICILIO FISCAL Y/O DATOS DEL CONTRIBUYENTE (Tipo de documento de identidad, nombres y apellidos, denominación o razón social, teléfonos, correo electrónico, estado civil, actividad económica, nombre comercial, entre otros)",
        "sustento": "BASE LEGAL\nTUO del Código Tributario, Decreto Supremo Nº 135-99-EF y modificatorias (19.08.99). Arts. 11 y 88.",
        "requisitos": [
            "1 Presentar formularios proporcionados por la Municipalidad",
            "2 Exhibir el documento de identidad del propietario o de su representante, de ser el caso, y presentar copia simple del mismo.",
            "3 En el caso de representación, presentar poder específico en documento público o privado con firma legalizada ante notario.",
            "4 Exhibir el último recibo de luz, agua, cable o teléfono del domicilio del propietario; excepto cuando el domicilio pueda ser verificado por personal de la Municipalidad.",
            "5 Exhibir el original y presentar copia simple del documento que acredite la actualización de datos del contribuyente.",
            "6 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "0.2763% UIT",
        "plazo": "Evaluación Previa - Automático",
        "inicio": "Unidad de Tránsito Documentario",
        "autoridad": "Sub Gerente de Registro y Recaudación",
        "reconsideracion": "-",
        "apelacion": "-"
    },
{
        "id": "37",
        "numero": "36",
        "procedimiento": "SOLICITUD DE INAFECTACIÓN DEL IMPUESTO PREDIAL",
        "sustento": "BASE LEGAL\n- Artículo 17 del TUO de la Ley de Tributación Municipal DS 156-2004-EF (15/11/2004)\n- Acuerdo entre el Estado Peruano y la Santa Sede suscrito el 19 de julio de 1980\n- Resolución Ministerial Nº 377-2003-JUS",
        "requisitos": [
            "REQUISITOS GENERALES",
            "1 Solicitud simple firmada por el contribuyente o su representante",
            "2 Exhibir el documento de identidad del contribuyente o del representante de ser el caso",
            "3 En caso de representación, deberá adjuntar poder en documento público o privado con firma legalizada ante notario o certificada por fedatario de la Municipalidad. Si se trata de una persona jurídica deberá presentar además copia simple de la vigencia de poder con una antigüedad de 30 Días",
            "4 Pago por el Derecho de la Tasa Administrativa:",
            "REQUISITOS ESPECIFICOS",
            "1. Gobiernos extranjeros en condición de reciprocidad",
            "a) Constancia emitida por el Ministerio de Relaciones Exteriores que lo reconozcan como gobierno extranjero en condición de reciprocidad",
            "b) Declaración jurada que señale que la totalidad del predio se encuentra destinado a residencias de sus representantes diplomáticos o al funcionamiento de oficinas dependientes de sus embajadas, legaciones o consulado",
            "2. Organismos internacionales reconocidos por el gobierno",
            "a. Constancia emitida por el Ministerio de Relaciones Exteriores que lo reconozcan como organismo internacional",
            "b. Declaración Jurada que señale que la totalidad del predio sirve de sede",
            "3. Sociedad de Beneficencia",
            "a. Declaración Jurada que señale que la totalidad del predio no produce rentas y se encuentra destinado a sus fines específicos",
            "4. Entidades Religiosas",
            "a) Copia legalizada, por notario o certificada por fedatario de la Municipalidad, de la certificación emitida por el arzobispado correspondiente, que la reconoce como una comunidad o jurisdicción integrante de la iglesia católica",
            "5. Entidades religiosas (no catolica)",
            "a. Constancia de inscripción en el registro nacional de confesiones distintas a la católica, del Ministerio de justicia",
            "6. Entidades públicas destinadas a prestar servicios médicos asistenciales",
            "a. Copia simple de la norma de creación; o copia legalizada por notario público o certificada por fedatario de la Municipalidad de la información registrada en RUC expedida por la SUNAT",
            "7. Centros Educativos y Universidades",
            "a. Copia legalizada por notario público o certificada por fedatario de la Municipalidad de la autorización expedida por el Ministerio de Educación",
            "8. Organizaciones Políticas",
            "a. Constancia original expedida por el jurado nacional de elecciones que lo acredita como organización política",
            "9. Organización de personas con discapacidad",
            "a. Resolución expedida por el CONADIS que lo reconozca como organización de personas con discapacidad",
            "10. Sindicatos",
            "a. Constancia expedida por el Ministerio de Trabajo y Promoción del Empleo que lo acredite como organización sindical",
            "11. Predios declarados monumentos integrantes del Patrimonio Cultural de la Nación por el INC",
            "a. Copia legalizada por notario público o certificada por fedatario de la Municipalidad de la Resolución expedida por el INC que reconoce el predio como patrimonio cultural",
            "b. Declaración jurada que señale que la totalidad del predio es dedicado a casa habitación o sede de instituciones sin fines de lucro, o resolución de la Municipalidad que lo declare inhabitable"
        ],
        "derecho_tramite": "0.4211% UIT",
        "plazo": "Evaluación Previa - 30 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Sub Gerente de Registro y Recaudación",
        "reconsideracion": "Sub Gerente de Registro y Recaudación\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente de Rentas\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
{
        "id": "38",
        "numero": "37",
        "procedimiento": "SOLICITUD DE BENEFICIO TRIBUTARIO PARA PENSIONISTA (DESCUENTO DE 50 UIT DE LA BASE IMPONIBLE DEL IMPUESTO PREDIAL)",
        "sustento": "BASE LEGAL\nTUO de la Ley de Tributación Municipal, Decreto Supremo Nº 156-2004-EF y modificatorias (15.11.04). Art. 19.",
        "requisitos": [
            "1 Presentar solicitud firmada por el solicitante o representante legal.",
            "2 Exhibir el documento de identidad del propietario o de su representante, de ser el caso.",
            "3 En el caso de representación, presentar poder específico en documento público o privado con firma legalizada ante notario o certificada por fedatario de la Municipalidad.",
            "4 Exhibir el original y presentar copia simple de la Resolución o documento que le confiere la calidad de pensionista.",
            "5 Exhibir el original y presentar copia simple de la última boleta de pago o liquidación de pensión (ingreso bruto no mayor a 1UIT).",
            "6 Presentar certificado negativo y/o positivo de propiedad emitido por la SUNARP.",
            "7 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "0.4158% UIT",
        "plazo": "Evaluación Previa - 30 Días",
        "inicio": "Unidad de Tránsito Documentario",
        "autoridad": "Sub Gerente de Registro y Recaudación",
        "reconsideracion": "Sub Gerente de Registro y Recaudación\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente de Rentas\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
    {
        "id": "39",
        "numero": "38",
        "procedimiento": "SOLICITUD DE PRESCRIPCIÓN EN MATERIA TRIBUTARIA",
        "sustento": "BASE LEGAL\n- TUO del Código Tributario, Decreto Supremo Nº 135-99-EF y modificatorias (19.08.99). Arts. 162 y 163.\n- Sentencia del Tribunal Constitucional recaída en el Expediente Nº 3741-2004-AA/TC (del 14.11.05).\n- Resolución Nº 0039-2007/TDC-INDECOPI",
        "requisitos": [
            "1 Presentar solicitud firmada por el solicitante o representante legal.",
            "2 En el caso de representación, presentar poder específico en documento público o privado con firma legalizada ante notario o certificada por fedatario de la Municipalidad.",
            "3 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "0.4132% UIT",
        "plazo": "Evaluación Previa - 30 Días",
        "inicio": "Unidad de Tránsito Documentario",
        "autoridad": "Sub Gerente de Registro y Recaudación",
        "reconsideracion": "Sub Gerente de Registro y Recaudación\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente de Rentas\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
    {
        "id": "40",
        "numero": "39",
        "procedimiento": "SOLICITUD DE DEVOLUCIÓN EN MATERIA TRIBUTARIA",
        "sustento": "BASE LEGAL\nTUO del Código Tributario, Decreto Supremo Nº 135-99-EF y modificatorias (19.08.99). Arts. 38º, 162 y 163.",
        "requisitos": [
            "1 Presentar solicitud firmada por el solicitante o representante legal.",
            "2 En el caso de representación, presentar poder específico en documento público o privado con firma legalizada ante notario o certificada por fedatario de la Municipalidad.",
            "3 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "0.1605% UIT",
        "plazo": "Evaluación Previa - 30 Días",
        "inicio": "Unidad de Tránsito Documentario",
        "autoridad": "Sub Gerente de Registro y Recaudación",
        "reconsideracion": "Sub Gerente de Registro y Recaudación\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente de Rentas\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
    {
        "id": "41",
        "numero": "40",
        "procedimiento": "SOLICITUD DE COMPENSACIÓN EN MATERIA TRIBUTARIA",
        "sustento": "BASE LEGAL\nTUO del Código Tributario, Decreto Supremo Nº 135-99-EF y modificatorias (19.08.99). Arts. 40º, 162 y 163.",
        "requisitos": [
            "1 Presentar solicitud firmada por el solicitante o representante legal.",
            "2 En el caso de representación, presentar poder específico en documento público o privado con firma legalizada ante notario o certificada por fedatario de la Municipalidad.",
            "3 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "0.1789% UIT",
        "plazo": "Evaluación Previa - 30 Días",
        "inicio": "Unidad de Tránsito Documentario",
        "autoridad": "Sub Gerente de Registro y Recaudación",
        "reconsideracion": "Sub Gerente de Registro y Recaudación\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente de Rentas\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
{
        "id": "42",
        "numero": "41",
        "procedimiento": "FRACCIONAMIENTO DE DEUDAS TRIBUTARIAS",
        "sustento": "BASE LEGAL\n- TUO del Código Tributario, Decreto Supremo Nº 135-99-EF y modificatorias (19.08.99). Art. 36.\n- Ordenanza Nº 035,-2008-MDSR",
        "requisitos": [
            "1 Presentar solicitud, firmada por el deudor, tercero legitimado o representante legal.",
            "2 Exhibir el original y presentar copia simple del recibo de agua, luz, teléfono o cable",
            "3 Cancelar la primera cuota del fraccionamiento correspondiente.",
            "4 En caso de pensionistas: exhibir el original de la boleta de pago del mes anterior",
            "5 En el caso de representación, presentar poder con firma legalizada ante notario.",
            "6 Presentar copia certificada o autenticada por fedatario de la Municipalidad del cargo de la solicitud de desistimiento, en caso la deuda materia de acogimiento registre medio impugnatorio o solicitudes no contenciosas ante entidad distinta a la municipalidad.",
            "7 De corresponder, adjuntar o formalizar las garantías conforme lo establece el Reglamento de Fraccionamiento de la Municipalidad.",
            "8 No registrar cuotas vencidas impagas de otros fraccionamientos de la misma naturaleza en los últimos doce (12) meses.",
            "9 No registrar en los últimos doce (12) meses otros fraccionamientos de la misma naturaleza respecto de los cuales haya operado la pérdida por falta de pago.",
            "10 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "0.1763% UIT",
        "plazo": "Automático",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Sub Gerente de Registro y Recaudación",
        "reconsideracion": "-",
        "apelacion": "-"
    },
    {
        "id": "43",
        "numero": "42",
        "procedimiento": "PRESENTACIÓN DE DECLARACIÓN JURADA PARA COMUNICAR EL BOLETAJE O SIMILARES, EN CASO DEL IMPUESTO A LOS ESPECTÁCULOS PÚBLICOS NO DEPORTIVOS",
        "sustento": "BASE LEGAL\n- TUO de la Ley de Tributación Municipal, Decreto Supremo Nº 156-2004-EF y modificatorias (15.11.04). Art. 55.\n- Ley que promueve el desarrollo de espectáculos públicos no deportivos, Ley Nº 29168 (20.12.07).\n- TUO del Código Tributario, Decreto Supremo Nº 135-99-EF y modificatorias (19.08.99). Art. 88.",
        "requisitos": [
            "1 Presentar declaración jurada firmada por el agente perceptor o representante legal.",
            "2 En el caso de representación, presentar poder específico en documento público o privado con firma legalizada ante notario.",
            "3 En caso de espectáculos temporales y eventuales, acreditar el depósito de una garantía equivalente al 15% del impuesto calculado sobre la capacidad o aforo del local donde se realizará el espectáculo"
        ],
        "derecho_tramite": "GRATUITO",
        "plazo": "Automático",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Sub Gerente de Registro y Recaudación",
        "reconsideracion": "-",
        "apelacion": "-"
    },
    {
        "id": "44",
        "numero": "43",
        "procedimiento": "LIQUIDACIÓN DE IMPUESTO A LOS JUEGOS",
        "sustento": "BASE LEGAL\nTUO de la Ley de Tributación Municipal, Decreto Supremo Nº 156-2004-EF y modificatorias (15.11.04). Arts. 50 y 51.",
        "requisitos": [
            "1 Presentar formato de liquidación del impuesto firmado por el contribuyente, agente de retención o representante legal.",
            "2 En el caso de representación, presentar poder específico en documento público o privado con firma legalizada ante notario."
        ],
        "derecho_tramite": "GRATUITO",
        "plazo": "Automático",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Sub Gerente de Registro y Recaudación",
        "reconsideracion": "-",
        "apelacion": "-"
    },
    {
        "id": "45",
        "numero": "44",
        "procedimiento": "LIQUIDACIÓN DEL IMPUESTO A LOS ESPECTÁCULOS PÚBLICOS NO DEPORTIVOS",
        "sustento": "BASE LEGAL\nTUO de la Ley de Tributación Municipal, Decreto Supremo Nº 156-2004-EF y modificatorias (15.11.04). Arts. 56 y 57.",
        "requisitos": [
            "1 Presentar formato de liquidación firmado por la persona que organiza el espectáculo o representante legal.",
            "2 En el caso de representación, presentar poder específico en documento público o privado con firma legalizada ante notario."
        ],
        "derecho_tramite": "GRATUITO",
        "plazo": "Automático",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Sub Gerente de Registro y Recaudación",
        "reconsideracion": "-",
        "apelacion": "-"
    },
{
        "id": "46",
        "numero": "45",
        "procedimiento": "LIQUIDACIÓN DE PAGO DEL IMPUESTO DE ALCABALA",
        "sustento": "BASE LEGAL\nArtículos 24 y 25 del TUO de la Ley de Tributación Municipal, D.S. 156-2004-EF",
        "requisitos": [
            "1 Juego de Formularios de Declaración Jurada del Impuesto de Alcabala debidamente llenados",
            "2 Copia fedateada del DNI vigente de la persona que realice el trámite; en caso de representación ésta deberá ser acreditada mediante poder con documento público o privado y firma legalizada notarialmente o fedateado por la Municipalidad",
            "3 Presentar copia simple del documento en el que consta la transferencia de propiedad",
            "4 Copia simple del Autovalúo (Impuesto Predial) del año en que se realizó la transferencia"
        ],
        "derecho_tramite": "GRATUITO",
        "plazo": "Automático",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Sub Gerente de Registro y Recaudación",
        "reconsideracion": "-",
        "apelacion": "-"
    },
    {
        "id": "47",
        "numero": "46",
        "procedimiento": "INAFECTACIÓN DEL IMPUESTO DE ALCABALA",
        "sustento": "BASE LEGAL\nArtículos 27 y 28 del TUO de la Ley de Tributación Municipal, D.S. 156-2004-EF",
        "requisitos": [
            "1 Solicitud cumpliendo con los requisitos generales de presentación",
            "2 Copia fedateada del DNI vigente de la persona que realice el trámite; en caso de representación ésta deberá ser acreditada mediante poder con documento público o privado y firma legalizada",
            "3 Presentar copia simple del documento en el que consta la transferencia de propiedad",
            "4 Copia simple del Autovalúo (Impuesto Predial) del año en que se realizó la transferencia",
            "5 Presentar los documentos que sustenten la inafectación",
            "6 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "0.3184% UIT",
        "plazo": "Evaluación Previa - 30 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Sub Gerente de Registro y Recaudación",
        "reconsideracion": "Sub Gerente de Registro y Recaudación\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente de Rentas\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
    {
        "id": "48",
        "numero": "47",
        "procedimiento": "RECURSO DE RECLAMACIÓN",
        "sustento": "BASE LEGAL\nTUO del Código Tributario, Decreto Supremo Nº 135-99-EF y modificatorias (19.08.99). Arts. 124, 132 al 137 y 142.",
        "requisitos": [
            "1 Presentar escrito fundamentado, firmado por el recurrente o representante legal, debidamente autorizado por abogado hábil.",
            "2 En el caso de representación, presentar poder específico en documento público o privado con firma legalizada ante notario o certificada por fedatario de la Municipalidad.",
            "3 Acreditar el pago de la deuda no reclamada en caso de la Resolución de Determinación y de Multa o el íntegro de la contenida en una Orden de Pago, actualizada a la fecha de pago.",
            "4 En caso de extemporaneidad (Resolución de Determinación, de Multa y Orden de Pago), acreditar el pago de la totalidad de la deuda o presentar carta fianza bancaria o financiera por el monto de la deuda actualizada hasta por seis (06) meses posteriores ala fecha de interposición del recurso"
        ],
        "derecho_tramite": "GRATUITO",
        "plazo": "Evaluación Previa - 9 Meses",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Rentas",
        "reconsideracion": "-",
        "apelacion": "Tribunal Fiscal"
    },
    {
        "id": "49",
        "numero": "48",
        "procedimiento": "RECURSO DE RECLAMACIÓN CONTRA RESOLUCIÓN DE PÉRDIDA DE FRACCIONAMIENTO EN MATERIA TRIBUTARIA",
        "sustento": "BASE LEGAL\nTUO del Código Tributario, Decreto Supremo Nº 135-99-EF y modificatorias (19.08.99). Arts. 124, 132 al 137 y 142.",
        "requisitos": [
            "1 Presentar escrito fundamentado firmado por el recurrente o representante legal, de ser el caso, debidamente autorizado por abogado hábil.",
            "2 En el caso de representación, presentar poder específico en documento público o privado con firma legalizada ante notario o certificada por fedatario de la Municipalidad."
        ],
        "derecho_tramite": "GRATUITO",
        "plazo": "Evaluación Previa - 9 Meses",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Rentas",
        "reconsideracion": "-",
        "apelacion": "Tribunal Fiscal"
    },
{
        "id": "50",
        "numero": "49",
        "procedimiento": "RECURSO DE APELACIÓN DE RESOLUCIÓN QUE RESUELVE RECURSO DE RECLAMACIÓN",
        "sustento": "BASE LEGAL\nTUO del Código Tributario, Decreto Supremo Nº 135-99-EF y modificatorias (19.08.99). Arts. 143 al 146.",
        "requisitos": [
            "1 Presentar escrito fundamentado firmado por el recurrente o representante legal, de ser el caso, debidamente autorizado por abogado hábil.",
            "2 En el caso de representación, presentar poder específico en documento público o privado con firma legalizada ante notario o certificada por fedatario de la Municipalidad.",
            "3 Pago de la deuda no apelada.",
            "4 En el caso de extemporaneidad, acreditar el pago de la totalidad de la deuda o presentar carta fianza bancaria o financiera por el monto de la deuda actualizada hasta por seis (06) meses posteriores a la fecha de presentación del recurso"
        ],
        "derecho_tramite": "GRATUITO",
        "plazo": "Evaluación Previa - 30 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Rentas",
        "reconsideracion": "-",
        "apelacion": "-"
    },
    {
        "id": "51",
        "numero": "50",
        "procedimiento": "RECURSO DE APELACIÓN DE PURO DERECHO",
        "sustento": "BASE LEGAL\nTUO del Código Tributario, Decreto Supremo Nº 135-99-EF y modificatorias (19.08.99). Arts. 146 y 151.",
        "requisitos": [
            "1 Presentar escrito fundamentado firmado por el recurrente o representante legal, de ser el caso, debidamente autorizado por abogado hábil.",
            "2 En el caso de representación, presentar poder específico en documento público o privado con firma legalizada ante notario o certificada por fedatario de la Municipalidad.",
            "3 Pago de la deuda no apelada.",
            "4 En el caso de extemporaneidad, acreditar el pago de la totalidad de la deuda o presentar carta fianza bancaria o financiera por el monto de la deuda actualizada hasta por seis (06) meses posteriores a la fecha de presentación del recurso"
        ],
        "derecho_tramite": "GRATUITO",
        "plazo": "Evaluación Previa - 30 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Rentas",
        "reconsideracion": "-",
        "apelacion": "-"
    },
    {
        "id": "52",
        "numero": "51",
        "procedimiento": "RECURSO DE APELACIÓN DE DENEGATORIA DE COMPENSACIÓN, INAFECTACIÓN O PRESCRIPCIÓN",
        "sustento": "BASE LEGAL\nTUO del Código Tributario, Decreto Supremo Nº 135-99-EF y modificatorias (19.08.99). Arts. 143 al 146.",
        "requisitos": [
            "1 Presentar escrito fundamentado firmado por el recurrente o representante legal, de ser el caso, debidamente autorizado por abogado hábil.",
            "2 En el caso de representación, presentar poder específico en documento público o privado con firma legalizada ante notario o certificada por fedatario de la Municipalidad."
        ],
        "derecho_tramite": "GRATUITO",
        "plazo": "Evaluación Previa - 30 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Rentas",
        "reconsideracion": "-",
        "apelacion": "-"
    },
{
        "id": "53",
        "numero": "52",
        "procedimiento": "CONSTANCIA DE A) NO ADEUDO DEL IMPUESTO PREDIAL Y/O ALCABALA B) NO ADEUDO DE ARBITRIOS MUNICIPALES C) DE INAFECTACIÓN AL IMPUESTO PREDIAL Y ALCABALA D) DE PAGOS DE TRIBUTOS",
        "sustento": "BASE LEGAL\n- Ley del Procedimiento Administrativo General, Ley Nº 27444 y modificatorias (11.04.01). Arts. 37, 107 y 110.\n- TUO de la Ley de Tributación Municipal, Decreto Supremo Nº 156-2004-EF y modificatorias (15.11.04). Art. 7.",
        "requisitos": [
            "1 Presentar solicitud firmada por el solicitante o tercero interesado.",
            "2 Exhibir el documento de identidad del contribuyente o del representante de ser el caso. En caso de representación, deberá adjuntar poder en documento público o privado con firma legalizada ante notario o certificada por fedatario de la Municipalidad. Si se trata de una persona jurídica deberá además presentar copia simple de la vigencia de poder con antigüedad no mayor de 30 días",
            "3 En caso de solicitar constancia de no adeudo del impuesto predial, no debe tener deuda pendiente de pago por ningún concepto tributario a la fecha en que se presenta la solicitud",
            "4 Por cualquiera de las modalidades el Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "0.4658% UIT",
        "plazo": "Automático",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Sub Gerente de Registro y Recaudación",
        "reconsideracion": "-",
        "apelacion": "-"
    },
    {
        "id": "54",
        "numero": "53",
        "procedimiento": "EXPEDICIÓN DE ESTADO DE CUENTA DE TRIBUTOS (DETALLE DE DEUDA PENDIENTE Y PAGADA)",
        "sustento": "BASE LEGAL\nLey del Procedimiento Administrativo General, Ley Nº 27444 y modificatorias (11.04.01). Arts. 37, 107 y 110.",
        "requisitos": [
            "1 Solicitud consignando datos del administrado o establecimiento"
        ],
        "derecho_tramite": "GRATUITO",
        "plazo": "Automático",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Sub Gerente de Registro y Recaudación",
        "reconsideracion": "-",
        "apelacion": "-"
    },
    {
        "id": "55",
        "numero": "54",
        "procedimiento": "REIMPRESIÓN DE DJ, HR, HIA Y HL - IMPUESTO PREDIAL Y ARBITRIOS (Declaración Jurada, Hoja de Resumen, Hoja Informativa de Arbitrios y Hoja de Liquidación)",
        "sustento": "BASE LEGAL\nLey del Procedimiento Administrativo General, Ley Nº 27444 y modificatorias (11.04.01). Arts. 37, 107 y 110.",
        "requisitos": [
            "1 Exhibir el documento de identidad del propietario o de su representante, de ser el caso.",
            "2 En caso de representación, presentar poder específico en documento público o privado con firma legalizada ante notario.",
            "3 Actualizar el domicilio fiscal",
            "4 Pago por el Derecho de la Tasa Administrativa - Por Predio:"
        ],
        "derecho_tramite": "0.2447% UIT",
        "plazo": "Automático",
        "inicio": "Sub Gerencia de Registro y Recaudación",
        "autoridad": "Sub Gerente de Registro y Recaudación",
        "reconsideracion": "-",
        "apelacion": "-"
    },
{
        "id": "56",
        "numero": "55",
        "procedimiento": "DUPLICADO DE DDJJ EJERCICIO VIGENTE",
        "sustento": "BASE LEGAL\nLey del Procedimiento Administrativo General, Ley Nº 27444 y modificatorias (11.04.01). Arts. 37, 107 y 110.",
        "requisitos": [
            "1 Exhibir original del documento de identidad del propietario o de su reprentante",
            "2 En caso de representación, presentar poder específico en documento público o privado, con firma legalizada ante notario.",
            "3 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "0.2711% UIT",
        "plazo": "Automático",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Sub Gerente de Registro y Recaudación",
        "reconsideracion": "-",
        "apelacion": "-"
    },
    {
        "id": "57",
        "numero": "56",
        "procedimiento": "SOLICITUD DE LEVANTAMIENTO DE INFORMACIÓN PREDIAL",
        "sustento": "BASE LEGAL\n- Ley del Procedimiento Administrativo General, Ley Nº 27444 y modificatorias (11.04.01). Arts. 37 y 107.\n- TUO de la Ley de Tributación Municipal, Decreto Supremo Nº 156-2004-EF y modificatorias (15.11.04).",
        "requisitos": [
            "1 Presentar solicitud firmada por el solicitante o representante legal de ser el caso.",
            "2 En caso de representación, presentar poder específico en documento público o privado con firma legalizada ante notario.",
            "3 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "0.8368% UIT",
        "plazo": "Automático",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Sub Gerente de Fiscalización Tributaria",
        "reconsideracion": "-",
        "apelacion": "-"
    },
{
        "id": "58",
        "numero": "57",
        "procedimiento": "LICENCIA DE FUNCIONAMIENTO PARA ESTABLECIMIENTOS CON UN ÁREA DE HASTA 100 M2 Y CON UNA CAPACIDAD NO MAYOR DE ALMACENAMIENTO DE 30% DEL ÁREA TOTAL DEL LOCAL CON ITSDC BÁSICA EX POST",
        "sustento": "BASE LEGAL\n- Ley Nº 27972 (27.05.03). Arts. 40 y 81 numeral 1.8.\n- Ley Nº 27444 (11.04.01). Arts. 44 y 45.\n- Decreto Supremo Nº 156-2004-EF (15.11.04). Art. 68.\n- Ley Nº 29060 (07.07.07). Arts. 1 y 2.\n- Ley Nº 28976 (05.02.07). Arts. 7, 8 numeral 1, 11 y 15.\n- Decreto Supremo Nº 066-2007-PCM (05.08.07). Arts. 2, 8, 9 numeral 2, 10 y 8va. Disposición Complementaria y Final.",
        "requisitos": [
            "REQUISITOS GENERALES",
            "1 Formato de solicitud (distribución gratuita o de libre reproducción) con carácter de Declaración Jurada, que incluye lo siguiente:",
            "- Número de RUC y DNI o Carné de Extranjería del solicitante, tratándose de personas jurídicas o naturales, según corresponda.",
            "- Número del DNI o Carné de Extranjería del representante legal, en caso de persona jurídica, u otros entes colectivos, o tratándose de personas naturales que actúe mediante representación.",
            "2 Poder vigente del representante legal, en el caso de personas jurídicas u otros entes colectivos. Carta poder con firma legalizada en caso de persona natural.",
            "3 Declaración Jurada de Observancia de Condiciones de Seguridad, para establecimientos con un área hasta 100 m2 y capacidad de almacenamiento no mayor de 30% del área total del local.",
            "4 Pago por el Derecho de la Tasa Administrativa:",
            "REQUISITOS ESPECÍFICOS",
            "Adicionalmente, de ser el caso, según sea el giro del establecimiento se presentará lo siguiente:",
            "1 Copia simple del título profesional en caso de servicios relacionados con la salud.",
            "2 Informar sobre el número de estacionamiento de acuerdo a la normativa vigente, en la Declaración Jurada.",
            "3 Copia simple de la autorización sectorial respectiva en el caso de aquellas actividades que conforme a Ley la requieran de manera previa al otorgamiento de la licencia de funcionamiento.",
            "4 Copia simple de la autorización expedida por el INC, conforme a la Ley Nº 28296, Ley General del Patrimonio Cultural de la Nación."
        ],
        "derecho_tramite": "6.5158% UIT",
        "plazo": "Evaluación Previa - 15 Días",
        "inicio": "Unidad de Tránsito Documentario",
        "autoridad": "Gerente de Rentas",
        "reconsideracion": "Gerente de Rentas\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente Municipal\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
{
        "id": "59",
        "numero": "58",
        "procedimiento": "LICENCIA DE FUNCIONAMIENTO PARA ESTABLECIMIENTOS CON UN ÁREA MÁS DE 100 M2 HASTA 500 M2 CON ITSDC BÁSICA EX ANTE",
        "sustento": "BASE LEGAL\n- Ley Nº 27972 (27.05.03). Arts. 40 y 81 numeral 1.8.\n- Ley Nº 27444 (11.04.01). Arts. 44 y 45.\n- Decreto Supremo Nº 156-2004-EF (15.11.04). Art. 68.\n- Ley Nº 29060 (07.07.07). Arts. 1 y 2.\n- Ley Nº 28976 (05.02.07). Arts. 7, 8 numerales 1 y 2, y 11 y 15.\n- Decreto Supremo Nº 066-2007-PCM (05.08.07). Arts. 2, 8, 9 numeral 2 y 39.",
        "requisitos": [
            "REQUISITOS GENERALES",
            "1 Formato de solicitud (distribución gratuita o de libre reproducción) con carácter de Declaración Jurada, que incluye lo siguiente:",
            "- Número de RUC y DNI o Carné de Extranjería del solicitante, tratándose de personas jurídicas o naturales, según corresponda.",
            "- Número del DNI o Carné de Extranjería del representante legal, en caso de persona jurídica, u otros entes colectivos, o tratándose de personas naturales que actúe mediante representación.",
            "2 Poder vigente del representante legal, en el caso de personas jurídicas u otros entes colectivos. Carta poder con firma legalizada en caso de persona natural.",
            "3 Pago por el Derecho de la Tasa Administrativa:",
            "REQUISITOS ESPECÍFICOS",
            "Adicionalmente, de ser el caso, según sea el giro del establecimiento se presentará lo siguiente:",
            "1 Copia simple del título profesional en caso de servicios relacionados con la salud.",
            "2 Informar sobre el número de estacionamiento de acuerdo a la normativa vigente, en la Declaración Jurada.",
            "3 Copia simple de la autorización sectorial respectiva en el caso de aquellas actividades que conforme a Ley la requieran de manera previa al otorgamiento de la licencia de funcionamiento.",
            "4 Copia simple de la autorización expedida por el INC, conforme a la Ley Nº 28296, Ley General del Patrimonio Cultural de la Nación.",
            "--------------------------------------------------",
            "📌 NOTAS PARA EL CIUDADANO",
            "• Edificaciones, recintos o instalaciones de hasta 2 niveles de terreno o calzada desde 101 m2 hasta 500 m2 como: tiendas, talleres mecánicos, establecimiento de hospedaje, restaurantes, cafeterías, edificaciones de salud.",
            "• Pubs-karaokes, licorerías, bar, ferreterías con un área hasta 500 m2.",
            "• Instituciones educativas hasta 2 niveles, con un área hasta 500 m2 y con un máximo de 200 alumnos por turno.",
            "• Cabinas de internet con un máximo de 20 computadoras.",
            "• Gimnasios hasta un área de 500 m2 y que sólo cuente con máquinas mecánicas.",
            "• Agencias bancarias, oficinas administrativas, entre otras de evaluación similar hasta 500 m2 y que cuenten con un máximo de 20 computadoras.",
            "• Playas de estacionamiento, granjas, entre otros que sean de un solo nivel y sin techar."
        ],
        "derecho_tramite": "7.2289% UIT",
        "plazo": "Evaluación Previa - 15 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Rentas",
        "reconsideracion": "Gerente de Rentas\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente Municipal\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
{
        "id": "60",
        "numero": "59",
        "procedimiento": "LICENCIA DE FUNCIONAMIENTO PARA ESTABLECIMIENTOS CON UN ÁREA DE MÁS DE 500 M2 Y NO COMPRENDIDOS EN LAS CATEGORIAS ANTERIORES",
        "sustento": "BASE LEGAL\n- Ley Nº 27972 (27.05.03). Arts. 40 y 81 numeral 1.8.\n- Ley Nº 27444 (11.04.01). Arts. 44 y 45.\n- Decreto Supremo Nº 156-2004-EF (15.11.04). Art. 68.\n- Ley Nº 29060 (07.07.07). Arts. 1 y 2.\n- Ley Nº 28976 (05.02.07). Arts. 7, 8 numerales 1 y 3, y 11 y 15.\n- Decreto Supremo Nº 066-2007-PCM (05.08.07). Arts. 2, 8, 10, 11 y 39.\n- Manual para la Ejecución de Inspecciones Técnicas de Seguridad en Defensa Civil. Numeral 1.1.3.",
        "requisitos": [
            "REQUISITOS GENERALES",
            "1 Formato de solicitud (distribución gratuita o de libre reproducción) con carácter de Declaración Jurada, que incluye lo siguiente:",
            "- Número de RUC y DNI o Carné de Extranjería del solicitante, tratándose de personas jurídicas o naturales, según corresponda.",
            "- Número del DNI o Carné de Extranjería del representante legal, en caso de persona jurídica, u otros entes colectivos, o tratándose de personas naturales que actúe mediante representación.",
            "2 Poder vigente del representante legal, en el caso de personas jurídicas u otros entes colectivos. Carta poder con firma legalizada en caso de persona natural.",
            "3 Certificado de la Inspección Técnica de Seguridad en Defensa Civil (ITSDC) de Detalle o Multidisciplinaria.",
            "4 Pago por el Derecho de la Tasa Administrativa:",
            "REQUISITOS ESPECÍFICOS",
            "Adicionalmente, de ser el caso, según sea el giro del establecimiento se presentará lo siguiente:",
            "1 Copia simple del título profesional en caso de servicios relacionados con la salud.",
            "2 Informar sobre el número de estacionamiento de acuerdo a la normativa vigente, en la Declaración Jurada.",
            "3 Copia simple de la autorización sectorial respectiva en el caso de aquellas actividades que conforme a Ley la requieran de manera previa al otorgamiento de la licencia de funcionamiento.",
            "4 Copia simple de la autorización expedida por el INC, conforme a la Ley Nº 28296, Ley General del Patrimonio Cultural de la Nación.",
            "--------------------------------------------------",
            "📌 NOTAS PARA EL CIUDADANO:",
            "Giros aplicables que requieren una ITSDC de Detalle",
            "- Edificaciones, recintos o instalaciones de más de 2 niveles de terreno o calzada con un área mayor de 500 m2 como: tiendas, talleres mecánicos, establecimiento de hospedaje, restaurantes, cafeterías, edificaciones de salud, playas de estacionamiento, entre otros afines.",
            "- Pubs-karaokes, licorerías, bar, ferreterías con un área más de 500 m2.",
            "- Industrias livianas y medianas, cualquiera sea el área con que cuenten.",
            "- Cines, teatros, auditorios, centro de convenciones, entre otros afines, cualquiera sea el área con que cuenten.",
            "- Centros de diversión cualquiera sea el área con que cuente, tales como: salas de juegos de casinos y/o máquinas tragamonedas, telepódromos, bingos, discotecas, salsotecas, salsódromos, peñas, café teatros, clubes nocturnos, salas de juegos eléctricos y/o electrónicos, entre otros afines.",
            "- Agencias bancarias, oficinas administrativas, entre otras de evaluación similar, con un área mayor a 500 m2 y un número mayor de 20 computadoras.",
            "- Instituciones educativas con un área mayor a 500 m2 o más de 2 niveles desde el nivel de terreno o calzada o más de 200 alumnos por turno.",
            "- Cabinas de internet con un número mayor de 20 computadoras.",
            "- Gimnasios que cuenten con máquinas eléctricas y/o electrónicas, cualquiera sea el área con que cuente.",
            "Giros aplicables que requieren una ITSDC Multidisciplinaria",
            "- Edificaciones, instalaciones o recintos donde se utilicen, almacenen, fabriquen, o comercialicen materiales y/o residuos peligrosos que representen riesgo para la población.",
            "- En el caso de industrias, si éstas se encuentran ubicadas cerca de zonas urbanas (viviendas familiares) y que por la naturaleza de los procesos industriales o de almacenamiento, utilizan y/o generan materiales y/o residuos peligrosos, inflamables, tóxicos, reactivos, corrosivos y/o radiactivos."
        ],
        "derecho_tramite": "2.5342% UIT",
        "plazo": "Evaluación Previa - 15 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Rentas",
        "reconsideracion": "Gerente de Rentas\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente Municipal\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
{
        "id": "61",
        "numero": "60",
        "procedimiento": "LICENCIA DE FUNCIONAMIENTO CORPORATIVAS PARA: MERCADOS DE ABASTO, GALERÍAS Y CENTROS COMERCIALES",
        "sustento": "BASE LEGAL\n- Ley Nº 27972 (27.05.03). Arts. 40 y 81 numeral 1.8.\n- Ley Nº 27444 (11.04.01). Arts. 44 y 45.\n- Decreto Supremo Nº 156-2004-EF (15.11.04). Art. 68.\n- Ley Nº 29060 (07.07.07). Arts. 1 y 2.\n- Ley Nº 28976 (05.02.07). Arts. 2, 7, 8, 9, 10, 11 y 15.\n- Decreto Supremo Nº 066-2007-PCM (05.08.07). Arts. 2, 8, 9 y 10 numeral 4.",
        "requisitos": [
            "REQUISITOS GENERALES",
            "1 Formato de solicitud (distribución gratuita o de libre reproducción) con carácter de Declaración Jurada, que incluye lo siguiente:",
            "- Número de RUC y DNI o Carné de Extranjería del solicitante, tratándose de personas jurídicas o naturales, según corresponda.",
            "- Número del DNI o Carné de Extranjería del representante legal, en caso de persona jurídica, u otros entes colectivos, o tratándose de personas naturales que actúe mediante representación.",
            "2 Poder vigente del representante legal, en el caso de personas jurídicas u otros entes colectivos. Carta poder con firma legalizada en caso de persona natural.",
            "3 Inspección Técnica de Seguridad en Defensa Civil de Detalle.",
            "4 Pago por el Derecho de la Tasa Administrativa:",
            "REQUISITOS ESPECÍFICOS",
            "Adicionalmente, de ser el caso, según sea el giro que se desarrolle en la galería, mercado o centro comercial se presentará lo siguiente:",
            "1 Copia simple del título profesional en caso de servicios relacionados con la salud.",
            "2 Informar sobre el número de estacionamiento de acuerdo a la normativa vigente, en la Declaración Jurada.",
            "3 Copia simple de la autorización sectorial respectiva en el caso de aquellas actividades que conforme a Ley la requieran de manera previa al otorgamiento de la licencia de funcionamiento.",
            "4 Copia simple de la autorización expedida por el INC, conforme a la Ley Nº 28296, Ley General del Patrimonio Cultural de la Nación.",
            "--------------------------------------------------",
            "📌 NOTAS PARA EL CIUDADANO:",
            "- Los mercados de abasto y galerías comerciales deben contar con una sola licencia de funcionamiento de forma corporativa, la cual es extendida a favor del ente colectivo, razón o denominación social que los represente o la junta de propietarios, de ser el caso.",
            "- A los módulos o stands que forman parte del mercado o de la galería, según corresponda les será exigibles una Inspección Técnica de Seguridad en Defensa Civil, Ex Post o Multidisciplinaria según corresponda, al otorgamiento de la licencia de funcionamiento."
        ],
        "derecho_tramite": "2.9184% UIT",
        "plazo": "Evaluación Previa - 15 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Rentas",
        "reconsideracion": "Gerente de Rentas\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente Municipal\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
{
        "id": "62",
        "numero": "61",
        "procedimiento": "LICENCIA DE FUNCIONAMIENTO PARA CESIONARIOS HASTA 500 M2 DE ÁREA",
        "sustento": "BASE LEGAL\n- Ley Nº 27972 (27.05.03). Arts. 40 y 81 numeral 1.8.\n- Ley Nº 27444 (11.04.01). Arts. 44 y 45.\n- Decreto Supremo Nº 156-2004-EF (15.11.04). Art. 68.\n- Ley Nº 29060 (07.07.07). Arts. 1 y 2.\n- Ley Nº 28976 (05.02.07). Arts. 3, 7, 8, 11 y 15.\n- Decreto Supremo Nº 066-2007-PCM (05.08.07). Arts. 2, 8 y 9.",
        "requisitos": [
            "1 Formato de solicitud (distribución gratuita o de libre reproducción) con carácter de Declaración Jurada, que incluye lo siguiente:",
            "- Número de RUC y DNI o Carné de Extranjería del solicitante, tratándose de personas jurídicas o naturales, según corresponda.",
            "- Número del DNI o Carné de Extranjería del representante legal, en caso de persona jurídica u otros entes colectivos, o tratándose de personas naturales que actúe mediante representación.",
            "- El número de la licencia de Funcionamiento.",
            "2 Poder vigente del representante legal, en el caso de personas jurídicas u otros entes colectivos. Carta poder con firma legalizada en caso de persona natural.",
            "3 Autorización con firma legalizada, del titular de la licencia de funcionamiento del establecimiento en el que se desarrollará la actividad comercial.",
            "4 Copia fedatada del contrato de cesión.",
            "5 Copia simple de la autorización sectorial respectiva en el caso de aquellas actividades que conforme a Ley se requieran de manera previa al otorgamiento de la licencia.",
            "6 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "2.5605% UIT",
        "plazo": "Evaluación Previa - 15 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Rentas",
        "reconsideracion": "Gerente de Rentas\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente Municipal\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
    {
        "id": "63",
        "numero": "62",
        "procedimiento": "VARIACIÓN DE ÁREA COMERCIAL",
        "sustento": "BASE LEGAL\n- Ley Nº 27972 (27.05.03). Arts. 40 y 81 numeral 1.8.\n- Ley Nº 27444 (11.04.01). Arts. 44 y 45.\n- Decreto Supremo Nº 156-2004-EF (15.11.04). Art. 68.\n- Ley Nº 29060 (07.07.07). Arts. 1 y 2.\n- Ley Nº 28976 (05.02.07). Arts. 3, 7, 8, 11 y 15.\n- Decreto Supremo Nº 066-2007-PCM (05.08.07). Arts. 2, 8, 9 y 10.\n- Resolución Nº 0155-2010/CEB-INDECOPI (01.07.2010). Literal E.2.",
        "requisitos": [
            "1 Formato de solicitud (distribución gratuita o de libre reproducción) con carácter de Declaración Jurada, que incluye lo siguiente:",
            "- Número de RUC y DNI o Carné de Extranjería del solicitante, tratándose de personas jurídicas o naturales, según corresponda.",
            "- Número del DNI o Carné de Extranjería del representante legal, en caso de persona jurídica u otros entes colectivos, o tratándose de personas naturales que actúe mediante representación.",
            "- Número de la licencia de funcionamiento",
            "2 Poder vigente del representante legal, en el caso de personas jurídicas u otros entes colectivos. Carta poder con firma legalizada en caso de persona natural.",
            "3 Pago del derecho de trámite.",
            "- En caso de realización de ITSDC a cargo de la municipalidad (costo de inspección incluido) [6.5079% UIT]",
            "- En caso de realización de ITSDC a cargo de INDECI (se debe presentar certificado) [2.5553% UIT]",
            "--------------------------------------------------",
            "📌 NOTAS PARA EL CIUDADANO:",
            "En el caso que la variación del área comercial origine el cambio del tipo de ITSDC al cual inicialmente estaba sujeto el establecimiento, se tendrá que realizar la inspección técnica que corresponda."
        ],
        "derecho_tramite": "Ver Requisitos (6.5079% UIT / 2.5553% UIT)",
        "plazo": "Evaluación Previa - 15 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Rentas",
        "reconsideracion": "Gerente de Rentas\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente Municipal\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
{
        "id": "64",
        "numero": "63",
        "procedimiento": "AMPLIACIÓN DE GIRO COMPATIBLE",
        "sustento": "BASE LEGAL\n- Ley Nº 27972 (27.05.03). Arts. 40 y 81 numeral 1.8.\n- Ley Nº 27444 (11.04.01). Arts. 44 y 45.\n- Decreto Supremo Nº 156-2004-EF (15.11.04). Art. 68.\n- Ley Nº 29060 (07.07.07). Arts. 1 y 2.\n- Ley Nº 28976 (05.02.07). Arts. 3, 7, 8, 11 y 15.\n- Decreto Supremo Nº 066-2007-PCM (05.08.07). Arts. 2, 8 y 9.\n- Resolución Nº 0155-2010/CEB-INDECOPI (01.07.2010). Literal E.2.",
        "requisitos": [
            "1 Formato de solicitud (distribución gratuita o de libre reproducción) con carácter de Declaración Jurada, que incluye lo siguiente:",
            "- Número de RUC y DNI o Carné de Extranjería del solicitante, tratándose de personas jurídicas o naturales, según corresponda.",
            "- Número del DNI o Carné de Extranjería del representante legal, en caso de persona jurídica u otros entes colectivos, o tratándose de personas naturales que actúe mediante representación.",
            "- Número de la licencia de funcionamiento.",
            "2 Poder vigente del representante legal, en el caso de personas jurídicas u otros entes colectivos. Carta poder con firma legalizada en caso de persona natural.",
            "3 Copia simple de la autorización sectorial respectiva, en el caso de aquellos giros a ampliar conforme a Ley la requieran de manera previa a la autorización de la ampliación.",
            "4 Pago del derecho de trámite.",
            "- En caso de realización de ITSDC a cargo de la municipalidad (costo de inspección incluido) [6.5026% UIT]",
            "- En caso de realización de ITSDC a cargo de INDECI (se debe presentar certificado) [2.5553% UIT]",
            "--------------------------------------------------",
            "📌 NOTAS PARA EL CIUDADANO:",
            "En el caso que la ampliación del giro comercial origine el cambio del tipo de ITSDC al cual inicialmente estaba sujeto el establecimiento se tendrá que realizar la inspección técnica que corresponda."
        ],
        "derecho_tramite": "Ver Requisitos (6.5026% UIT / 2.5553% UIT)",
        "plazo": "Evaluación Previa - 15 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Rentas",
        "reconsideracion": "Gerente de Rentas\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente Municipal\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
    {
        "id": "65",
        "numero": "64",
        "procedimiento": "AUTORIZACIÓN TEMPORAL PARA USO DE RETIRO MUNICIPAL (EJEM. VEREDAS) CON FINES COMERCIALES PARA ESTABLECIMIENTOS CON LICENCIA DE FUNCIONAMIENTO",
        "sustento": "BASE LEGAL\n- Ley Nº 27972 (27.05.03). Arts. 40 y 81 numeral 1.8.\n- Ley Nº 27444 (11.04.01). Arts. 44 y 45.\n- Decreto Supremo Nº 156-2004-EF (15.11.04). Art. 68.\n- Ley Nº 29060 (07.07.07). Arts. 1 y 2.\n- Ley Nº 28976 (05.02.07). Arts. 3, 7, 8, 11 y 15.\n- Decreto Supremo Nº 066-2007-PCM (05.08.07). Arts. 2, 8 y 9.\n- Decreto Supremo Nº 011-2006-VIVIENDA, (08.05.06 y 08.06.06). Art. Único de la Norma G. 040.",
        "requisitos": [
            "1 Formato de solicitud (distribución gratuita o de libre reproducción) con carácter de Declaración Jurada, que incluye lo siguiente:",
            "- Número de RUC y DNI o Carné de Extranjería del solicitante, tratándose de personas jurídicas o naturales, según corresponda.",
            "- Número del DNI o Carné de Extranjería del representante legal, en caso de persona jurídica u otros entes colectivos, o tratándose de personas naturales que actúe mediante representación.",
            "- Número de la licencia de funcionamiento.",
            "2 Poder vigente del representante legal, en el caso de personas jurídicas u otros entes colectivos. Carta poder con firma legalizada en caso de persona natural.",
            "3 Autorización de la Junta de Propietarios del predio en que se encuentra el local comercial para el giro solicitado si se encuentra bajo régimen de propiedad exclusiva y propiedad común o autorización del propietario, de ser el caso.",
            "4 Plano de distribución incluyendo mobiliario a escala 1:50 con ubicación de mobiliario.",
            "5 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "1.9842% UIT",
        "plazo": "Evaluación Previa - 15 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Rentas",
        "reconsideracion": "Gerente de Rentas\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente Municipal\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
{
        "id": "66",
        "numero": "65",
        "procedimiento": "CESE DE ACTIVIDADES COMERCIALES, INDUSTRIALES Y/O DE SERVICIOS, DE USO DE RETIRO MUNICIPAL Y/O ANUNCIOS PUBLICITARIOS",
        "sustento": "BASE LEGAL\n- Ley Nº 27972 (27.05.03). Arts. 40 y 81 numeral 1.8.\n- Ley Nº 27444 (11.04.01). Arts. 44 y 45.\n- Decreto Supremo Nº 156-2004-EF (15.11.04). Art. 68.\n- Ley Nº 29060 (07.07.07). Arts. 1 y 2.\n- Ley Nº 28976 (05.02.07). Arts. 3, 8, 11 y 12.",
        "requisitos": [
            "1 Formato de solicitud (distribución gratuita o de libre reproducción) en la que se solicita el cese, incluyendo la siguiente información, según corresponda:",
            "- Número de RUC y DNI o Carné de Extranjería del solicitante, tratándose de personas jurídicas o naturales, según corresponda.",
            "- Número del DNI o Carné de Extranjería del representante legal, en caso de persona jurídica u otros entes colectivos, o tratándose de personas naturales que actúe mediante representación.",
            "- Número de la licencia de funcionamiento.",
            "2 Poder vigente del representante legal, en el caso de personas jurídicas u otros entes colectivos. Carta poder con firma legalizada en caso de persona natural.",
            "3 En caso de un tercero acreditar legítimo interés.",
            "4 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "0.2000% UIT",
        "plazo": "Automático",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Rentas",
        "reconsideracion": "-",
        "apelacion": "-"
    },
{
        "id": "67",
        "numero": "66.1",
        "procedimiento": "MODIFICACIÓN DE DATOS DE LA LICENCIA DE FUNCIONAMIENTO MANTENIENDO EL ÁREA Y GIRO - POR CAMBIO DE RAZÓN SOCIAL",
        "sustento": "BASE LEGAL\n- Ley Nº 27972 (27.05.03). Arts. 40 y 81 numeral 1.8.\n- Ley Nº 27444 (11.04.01). Arts. 44 y 45.\n- Decreto Supremo Nº 156-2004-EF (15.11.04). Art. 68.\n- Ley Nº 29060 (07.07.07). Arts. 1 y 2.\n- Ley Nº 28976 (05.02.07). Arts. 3, 8, 11 y 12.\n- Ley 29566 (28.07.10). Art. 5.\n- Resolución Nº 0155-2010/CEB-INDECOPI (01.07.2010), literal E.2.",
        "requisitos": [
            "1 Formato de solicitud (distribución gratuita o de libre reproducción) con carácter de Declaración Jurada, que incluye lo siguiente:",
            "- Número de RUC y DNI o Carné de Extranjería del solicitante, tratándose de personas jurídicas o naturales, según corresponda.",
            "- Número del DNI o Carné de Extranjería del representante legal, en caso de persona jurídica u otros entes colectivos.",
            "- Información de la nueva razón social y documento que lo acredite.",
            "- Número de la licencia de funcionamiento.",
            "2 Poder vigente del representante legal, en el caso de personas jurídicas u otros entes colectivos. Carta poder con firma legalizada en caso de persona natural.",
            "3 Copia de la Escritura Pública de cambio de la denominación o razón social o ficha registral según sea el caso.",
            "4 Copia del RUC actual.",
            "5 Pago por el Derecho de la Tasa Administrativa:",
            "--------------------------------------------------",
            "📌 NOTAS PARA EL CIUDADANO:",
            "El derecho de trámite se establece en función al costo de reproducción del certificado de licencia de funcionamiento."
        ],
        "derecho_tramite": "6.3632% UIT",
        "plazo": "Automático",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Rentas",
        "reconsideracion": "-",
        "apelacion": "-"
    },
    {
        "id": "68",
        "numero": "66.2",
        "procedimiento": "MODIFICACIÓN DE DATOS DE LA LICENCIA DE FUNCIONAMIENTO MANTENIENDO EL ÁREA Y GIRO - POR CAMBIO DE OTROS DATOS VINCULADOS CON LA LICENCIA",
        "sustento": "BASE LEGAL\n- Ley Nº 27972 (27.05.03). Arts. 40 y 81 numeral 1.8.\n- Ley Nº 27444 (11.04.01). Arts. 44 y 45.\n- Decreto Supremo Nº 156-2004-EF (15.11.04). Art. 68.\n- Ley Nº 28976 (05.02.07). Arts. 3 y 8.",
        "requisitos": [
            "1 Formato de solicitud (distribución gratuita o de libre reproducción) con carácter de Declaración Jurada, que incluye lo siguiente:",
            "- Número de RUC y DNI o Carné de Extranjería del solicitante, tratándose de personas jurídicas o naturales, según corresponda.",
            "- Número del DNI o Carné de Extranjería del representante legal, en caso de persona jurídica u otros entes colectivos, o tratándose de personas naturales que actúe mediante representación.",
            "- Información de los datos a modificar o actualizar adjuntando los documentos que lo sustenten.",
            "- El número de la licencia de Funcionamiento.",
            "2 Poder vigente del representante legal, en el caso de personas jurídicas u otros entes colectivos. Carta poder con firma legalizada en caso de persona natural.",
            "3 En caso de un tercero acreditar legítimo interés.",
            "4 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "6.3632% UIT",
        "plazo": "Automático",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Rentas",
        "reconsideracion": "-",
        "apelacion": "-"
    },
{
        "id": "69",
        "numero": "67",
        "procedimiento": "AUTORIZACIÓN DE FUNCIONAMIENTO DE KIOSKO DE DIARIOS Y REVISTAS EN ZONAS AUTORIZADAS",
        "sustento": "BASE LEGAL\n- Ley Nº 27972 (27.05.03). Arts. 40 y 81.\n- Ley Nº 27444 (11.04.01). Arts. 44 y 45.\n- Decreto Supremo Nº 156-2004-EF (15.11.04). Art. 68.",
        "requisitos": [
            "1 Formato de solicitud (distribución gratuita o de libre reproducción) con carácter de Declaración Jurada indicando la siguiente información: nombre, número de DNI, domicilio.",
            "2 Declaración Jurada de domicilio.",
            "3 Declaración Jurada de no tener antecedentes policiales y penales.",
            "4 Croquis de ubicación del kioskos",
            "5 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "1.3289% UIT",
        "plazo": "Evaluación Previa - 30 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Rentas",
        "reconsideracion": "Gerente de Rentas\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente Municipal\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
    {
        "id": "70",
        "numero": "68",
        "procedimiento": "AUTORIZACIÓN PARA EVENTOS Y/O ESPECTÁCULOS PÚBLICOS NO DEPORTIVOS REALIZADOS EN LA VÍA PÚBLICA O LUGARES NO CONFINADOS (ABIERTOS AL PÚBLICO) EVENTUALES COMO: - FERIAS GASTRONÓMICAS - FERIAS ARTESANALES - FERIAS COSTUMBRISTAS, OTRAS",
        "sustento": "BASE LEGAL\n- Ley Nº 27972 (27.05.03). Arts. 40 y 81 numeral 1.8.\n- Ley Nº 27444 (11.04.01). Arts. 34, 35, 44 y 45.\n- Ley Nº 29060 (07.07.07). 1era. Disposición Transitoria, Complementaria y Final.\n- Decreto Supremo Nº 156-2004-EF (15.11.04). Art. 68.\n- Decreto Supremo Nº 066-2007-PCM (05.08.07). Art. 12.",
        "requisitos": [
            "1 Formato de solicitud (distribución gratuita o de libre reproducción) con carácter de Declaración Jurada, que incluye lo siguiente:",
            "- Número de RUC y DNI o Carné de Extranjería del solicitante, tratándose de personas jurídicas o naturales, según corresponda.",
            "- Número del DNI o Carné de Extranjería del representante legal, en caso de persona jurídica u otros entes colectivos, o tratándose de personas naturales que actúe mediante representación.",
            "2 Poder vigente del representante legal, en el caso de personas jurídicas u otros entes colectivos. Carta poder con firma legalizada en caso de persona natural.",
            "3 Plano de Distribución.",
            "4 Memoria descriptiva de las instalaciones.",
            "5 Declaración Jurada asumiendo el compromiso de no ocasionar daños a la propiedad pública o mobiliario urbano.",
            "6 Plan de Protección y Seguridad",
            "7 Pago por el Derecho de la Tasa Administrativa:",
            "--------------------------------------------------",
            "📌 NOTAS PARA EL CIUDADANO:",
            "- Los eventos y/o espectáculos públicos realizados en la vía pública o lugares no confinados no están sujetos al procedimiento de ITSDC, correspondiendo a los órganos del Gobierno Local en materia de Defensa Civil emitir un pronunciamiento sobre el cumplimiento o incumplimiento de las normas de seguridad en materia de Defensa Civil vigente. Art. 12 del Decreto Supremo Nº 066-2007-PCM."
        ],
        "derecho_tramite": "6.4737% UIT",
        "plazo": "Evaluación Previa - 30 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Rentas",
        "reconsideracion": "Gerente de Rentas\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente Municipal\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
{
        "id": "71",
        "numero": "69",
        "procedimiento": "AUTORIZACIÓN ANUAL PARA LA OCUPACIÓN DE LAS VÍAS PÚBLICAS PARA FINES DE COMERCIO Y/O SERVICIO AMBULATORIO",
        "sustento": "BASE LEGAL\nOrdenanza Municipal Nº 032-2009-MDSR, por el cual se aprueba el Reglamento para la Actividad comercial de Ferias en el Distrito de San Ramón",
        "requisitos": [
            "1 Solicitud con carácter de Declaración Jurada, que incluye lo siguiente:",
            "- Nombres y Apellidos",
            "- Número del DNI",
            "- Domicilio",
            "2 Dos fotografías tamaño carnet",
            "3 Especificar el lugar exacto de ocupación de la vía pública",
            "4 Presentación de DNI",
            "5 Pago por el Derecho de la Tasa Administrativa:",
            "--------------------------------------------------",
            "📌 NOTAS PARA EL CIUDADANO:",
            "Cada ambulante debe estar debidamente afiliado a una Asociación para acceder a la autorización asimismo deberá portar su fotochek expedido por la Municipalidad."
        ],
        "derecho_tramite": "0.2632% UIT",
        "plazo": "Evaluación Previa - 15 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Rentas",
        "reconsideracion": "Gerente de Rentas\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente Municipal\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
    {
        "id": "72",
        "numero": "70.1",
        "procedimiento": "AUTORIZACIÓN PARA EVENTOS Y/O ESPECTÁCULOS PÚBLICOS CON UNA AFLUENCIA MENOR O IGUAL A 3000 PERSONAS REALIZADAS EN RECINTOS O EDIFICACIONES AFINES A SU DISEÑO Y CUENTEN CON LICENCIA DE FUNCIONAMIENTO",
        "sustento": "BASE LEGAL\n- Ley Nº 27972 (27.05.03). Arts. 40 y 81 numeral 1.8.\n- Ley Nº 27444 (11.04.01). Arts. 34, 35, 44 y 45.\n- Ley Nº 29060 (07.07.07).",
        "requisitos": [
            "1 Formato de solicitud (distribución gratuita o de libre reproducción) con carácter de Declaración Jurada, que incluye lo siguiente:",
            "- Número de RUC y DNI o Carné de Extranjería del solicitante, tratándose de personas jurídicas o naturales, según corresponda.",
            "- Número del DNI o Carné de Extranjería del representante legal, en caso de persona jurídica u otros entes colectivos, o tratándose de personas naturales que actúe mediante representación.",
            "2 Poder vigente del representante legal, en el caso de personas jurídicas u otros entes colectivos. Carta poder con firma legalizada en caso de persona natural.",
            "3 Declaración jurada de la cantidad de boletaje o similar a utilizar con una anticipación de 7 Días antes de la puesta a disposición del público.",
            "4 En caso que el evento se realice en forma eventual se deberá presentar adicionalmente: Depósito de una garantía equivalente del 15% del impuesto calculado sobre la base capacidad o aforo, en caso que el evento se realice en forma eventual.",
            "5 Pago por el Derecho de la Tasa Administrativa:",
            "--------------------------------------------------",
            "📌 NOTAS PARA EL CIUDADANO:",
            "- Las instalaciones, edificaciones o recintos diseñados para la realización de espectáculos y/o eventos, en las cuales se realicen actividades afines a su diseño no requieren una ITSDC previa a cada evento y/o espectáculo, sólo será necesaria la realización de una Visita de Defensa Civil Art. 12 del Decreto Supremo Nº 066-2007-PCM.",
            "- El local donde se realice el evento deberá contar previamente con su respectivo certificado de inspección Técnica de Seguridad en Defensa Civil vigente. Art. 8 del Decreto Supremo Nº 066-2007-PCM.",
            "- El organizador y/o promotor deberá solicitar previa al evento y/o espectáculo la Visita de Defensa Civil en un plazo que no podrá exceder los 7 Días hábiles antes de la fecha de su realización Art. 12 del Decreto Supremo Nº 066-2007-PCM.",
            "- El costo de la Visita se encuentra incluida en el monto del derecho de trámite, por que dicha actividad se encuentra dentro del parámetro de las inspecciones de hasta 3000 personas que es de competencia de la Municipalidad. Art. 13 del Decreto Supremo Nº 066-2007-PCM."
        ],
        "derecho_tramite": "2.0711% UIT",
        "plazo": "Evaluación Previa - 30 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Rentas",
        "reconsideracion": "Gerente de Rentas\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente Municipal\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
{
        "id": "73",
        "numero": "70.2",
        "procedimiento": "REALIZADAS EN RECINTOS O LOCALES NO AFINES A SU DISEÑO",
        "sustento": "BASE LEGAL\n- Ley Nº 27972 (27.05.03). Arts. 40 y 81 numeral 1.8.\n- Ley Nº 27444 (11.04.01). Arts. 34, 35, 44 y 45.\n- Ley Nº 29060 (07.07.07).\n- Decreto Supremo Nº 156-2004-EF (15.11.04). Arts. 55 y 68.\n- Decreto Supremo Nº 066-2007-PCM (05.08.07). Arts. 10, 12, 13 y 39.",
        "requisitos": [
            "1 Formato de solicitud (distribución gratuita o de libre reproducción) con carácter de Declaración Jurada, que incluye lo siguiente:",
            "- Número de RUC y DNI o Carné de Extranjería del solicitante, tratándose de personas jurídicas o naturales, según corresponda.",
            "- Número del DNI o Carné de Extranjería del representante legal, en caso de persona jurídica u otros entes colectivos, o tratándose de personas naturales que actúe mediante representación.",
            "2 Poder vigente del representante legal, en el caso de personas jurídicas u otros entes colectivos. Carta poder con firma legalizada en caso de persona natural.",
            "3 Declaración jurada de la cantidad de boletaje o similar a utilizar con una anticipación de 7 Días antes de la puesta a disposición del público.",
            "4 Depósito de una garantía equivalente del 15% del impuesto calculado sobre la base capacidad o aforo en caso que el evento se realice en forma eventual.",
            "5 Pago por el Derecho de la Tasa Administrativa:",
            "--------------------------------------------------",
            "📌 NOTAS PARA EL CIUDADANO:",
            "El organizador y/o promotor deberá solicitar previa al evento y/o espectáculo la Visita de Defensa Civil en un plazo que no podrá exceder los 7 Días hábiles antes de la fecha de su realización Art. 12 del Decreto Supremo Nº 066-2007-PCM.",
            "El costo de la inspección se encuentra incluida en el monto del derecho de trámite, debido que la actividad de la inspección hasta 3000 personas se encuentra a cargo de la Municipalidad. Art. 13 del Decreto Supremo Nº 066-2007-PCM."
        ],
        "derecho_tramite": "2.2553% UIT",
        "plazo": "Evaluación Previa - 30 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Rentas",
        "reconsideracion": "Gerente de Rentas\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente Municipal\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
    {
        "id": "74",
        "numero": "71.1",
        "procedimiento": "AUTORIZACIÓN PARA EVENTOS Y/O ESPECTÁCULOS PÚBLICOS CON UNA AFLUENCIA MAYOR A 3000 PERSONAS - REALIZADAS EN RECINTOS O EDIFICACIONES AFINES A SU DISEÑO Y CUENTEN CON LICENCIA DE FUNCIONAMIENTO",
        "sustento": "BASE LEGAL\n- Ley Nº 27972 (27.05.03). Arts. 40 y 81 numeral 1.8.\n- Ley Nº 27444 (11.04.01). Arts. 34, 35, 44 y 45.\n- Ley Nº 29060 (07.07.07).\n- Decreto Supremo Nº 156-2004-EF (15.11.04). Arts. 55 y 68.\n- Decreto Supremo Nº 066-2007-PCM (05.08.07). Arts. 10, 12, 13 y 39.",
        "requisitos": [
            "1 Formato de solicitud (distribución gratuita o de libre reproducción) con carácter de Declaración Jurada, que incluye lo siguiente:",
            "- Número de RUC y DNI o Carné de Extranjería del solicitante, tratándose de personas jurídicas o naturales, según corresponda.",
            "- Número del DNI o Carné de Extranjería del representante legal, en caso de persona jurídica u otros entes colectivos, o tratándose de personas naturales que actúe mediante representación.",
            "2 Poder vigente del representante legal, en el caso de personas jurídicas u otros entes colectivos. Carta poder con firma legalizada en caso de persona natural.",
            "3 Documento que acredite la Visita de Defensa Civil realizada por INDECI.",
            "4 Declaración jurada de la cantidad de boletaje o similar a utilizar con una anticipación de 7 Días antes de la puesta a disposición del público.",
            "5 En caso que el evento se realiza en forma eventual se deberá presentar adicionalmente: Depósito de una garantía equivalente del 15% del impuesto calculado sobre la base capacidad o aforo.",
            "6 Pago por el Derecho de la Tasa Administrativa:",
            "--------------------------------------------------",
            "📌 NOTAS PARA EL CIUDADANO:",
            "- Las instalaciones, edificaciones o recintos diseñadas para la realización de espectáculos y/o eventos, en las cuales se realicen actividades afines a su diseño no requieren una ITSDC previa a cada evento y/o espectáculo, sólo será necesaria la realización de una Visita de Defensa Civil Art. 12 del Decreto Supremo Nº 066-2007-PCM.",
            "- El local donde se realice el evento deberá contar previamente con su respectivo certificado de inspección Técnica de Seguridad en Defensa Civil vigente. Art. 8 del Decreto Supremo Nº 066-2007-PCM.",
            "- El organizador y/o promotor deberá solicitar previa al evento y/o espectáculo la Visita de Defensa Civil en un plazo que no podrá exceder los 7 Días hábiles antes de la fecha de su realización Art. 12 del Decreto Supremo Nº 066-2007-PCM."
        ],
        "derecho_tramite": "1.0000% UIT",
        "plazo": "Evaluación Previa - 30 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Rentas",
        "reconsideracion": "Gerente de Rentas\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente Municipal\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
{
        "id": "75",
        "numero": "71.2",
        "procedimiento": "REALIZADAS EN RECINTOS O LOCALES NO AFINES A SU DISEÑO",
        "sustento": "BASE LEGAL\n- Ley Nº 27972 (27.05.03). Arts. 40 y 81 numeral 1.8.\n- Ley Nº 27444 (11.04.01). Arts. 34, 35, 44 y 45.\n- Ley Nº 29060 (07.07.07).\n- Decreto Supremo Nº 156-2004-EF (15.11.04). Arts. 55 y 68.\n- Decreto Supremo Nº 066-2007-PCM (05.08.07). Arts. 10, 12, 13 y 39.",
        "requisitos": [
            "1 Formato de solicitud (distribución gratuita o de libre reproducción) con carácter de Declaración Jurada, que incluye lo siguiente:",
            "- Número de RUC y DNI o Carné de Extranjería del solicitante, tratándose de personas jurídicas o naturales, según corresponda.",
            "- Número del DNI o Carné de Extranjería del representante legal, en caso de persona jurídica u otros entes colectivos, o tratándose de personas naturales que actúe mediante representación.",
            "2 Poder vigente del representante legal, en el caso de personas jurídicas u otros entes colectivos. Carta poder con firma legalizada en caso de persona natural.",
            "3 Certificado de Inspección Técnica de Seguridad de Defensa Civil emitida por INDECI.",
            "4 Declaración jurada de la cantidad de boletaje o similar a utilizar con una anticipación de 7 Días antes de la puesta a disposición del público.",
            "5 En caso que el evento se realiza en forma eventual se deberá presentar adicionalmente: Depósito de una garantía equivalente del 15% del impuesto calculado sobre la base capacidad o aforo.",
            "6 Pago por el Derecho de la Tasa Administrativa:",
            "--------------------------------------------------",
            "📌 NOTAS PARA EL CIUDADANO:",
            "El organizador y/o promotor deberá solicitar previa al evento y/o espectáculo la Visita de Defensa Civil en un plazo que no podrá exceder los 7 Días hábiles antes de la fecha de su realización Art. 12 del Decreto Supremo Nº 066-2007-PCM."
        ],
        "derecho_tramite": "1.2158% UIT",
        "plazo": "Evaluación Previa - 30 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Rentas",
        "reconsideracion": "Gerente de Rentas\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente Municipal\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
{
        "id": "76",
        "numero": "72",
        "procedimiento": "AFICHES O BANDEROLAS DE CAMPAÑAS Y EVENTOS TEMPORALES (HASTA TRES MESES) - AFICHES O CARTELES - BANDEROLAS - GIGANTOGRAFÍAS - PASACALLES",
        "sustento": "BASE LEGAL\n- Ley Nº 27972 (27.05.03). Arts. 40 y 79 numeral 1.4.4.\n- Ley Nº 27444 (11.04.01). Arts. 34, 35, 44 y 45.\n- Ley Nº 29060 (07.07.07).\n- Decreto Supremo Nº 156-2004-EF (15.11.04). Art. 68.\n- Resolución Nº 0148-2008/CEB-INDECOPI (13.09.2008).",
        "requisitos": [
            "1 Solicitud según formulario (distribución gratuita o de libre reproducción).",
            "2 Presentar las vistas siguientes:\na) Arte o diseño del anuncio o aviso publicitario con sus dimensiones.\nb) Una fotografía en la cual se aprecie el entorno urbano y el bien o edificación donde se ubicará el elemento de publicidad exterior y/o anuncio.",
            "3 Copia de la Autorización Municipal de funcionamiento vigente, si se ubica en un establecimiento que opera fuera de la jurisdicción del municipio.",
            "4 Copia simple del documento de identidad del solicitante o representante legal.",
            "5 Carta poder con firma legalizada, en caso de representación.",
            "6 Copia del acta de la Junta o Asamblea de Propietarios de los bienes de dominio privado sujetos al régimen de propiedad exclusiva y común, en la que la mitad más uno de los Propietarios autorizan la ubicación del elemento de publicidad exterior y/o anuncio. En caso de no existir Junta o Asamblea de Propietarios, podrá presentar documentos de autorización suscrito por la mitad más uno de sus propietarios de corresponder.",
            "7 Pago por el Derecho de la Tasa Administrativa:",
            "--------------------------------------------------",
            "📌 NOTAS PARA EL CIUDADANO:",
            "- Son Gratuitos los Anuncios y avisos publicitarios que identifican entidades públicas, organismos internacionales, templos, conventos y establecimientos similares de organizaciones religiosas de todas las denominaciones, así como los centros educativos, sólo respecto al nombre y en una sola ubicación.",
            "- Son Gratuitos la información temporal de actividades religiosas, culturales, recreativas, deportivas, cívicas y benéficas; todas ellas, de carácter no lucrativo. Así como la publicidad institucional de entidades públicas."
        ],
        "derecho_tramite": "1.3421% UIT",
        "plazo": "Automático",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Rentas",
        "reconsideracion": "-",
        "apelacion": "-"
    },
{
        "id": "77",
        "numero": "73",
        "procedimiento": "DUPLICADO DE CERTIFICADO DE LICENCIA DE FUNCIONAMIENTO",
        "sustento": "BASE LEGAL\n- Ley Nº 27972 (27.05.03). Arts. 40 y 81 numeral 1.8.\n- Ley Nº 27444 (11.04.01). Arts. 44, 45 y 160.\n- Decreto Supremo Nº 156-2004-EF (15.11.04). Art. 68.\n- Ley Nº 28976 (05.02.07). Arts. 3 y 8.",
        "requisitos": [
            "1 Formato de solicitud (distribución gratuita o de libre reproducción), en el cual se debe indicar el número del certificado de la licencia de funcionamiento cuyo duplicado se solicita.",
            "2 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "0.5684% UIT",
        "plazo": "Automático",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Rentas",
        "reconsideracion": "-",
        "apelacion": "-"
    },
    {
        "id": "78",
        "numero": "74",
        "procedimiento": "TERCERÍA DE PROPIEDAD ANTE COBRANZA DE OBLIGACIONES TRIBUTARIAS",
        "sustento": "BASE LEGAL\n- TUO de la Ley de Procedimiento de Ejecución Coactiva, Decreto Supremo Nº 018-2008-JUS (06.12.08). Arts. 20 y 36.\n- Ley del Procedimiento Administrativo General, Ley Nº 27444 y modificatorias (11.04.01). Art. 35.",
        "requisitos": [
            "1 Presentar solicitud de tercería dirigido al Ejecutor Coactivo en el que se consignará lo siguiente:\na) Nombres y apellidos o denominación o razón social, número de documento de identidad y/o número de RUC del solicitante y/o de su representante, de ser el caso.\nb) Domicilio real o procesal del solicitante dentro del radio urbano de la Provincia de Chanchamayo\nc) Fundamentar la solicitud de tercería, indicando el bien afectado.\nd) Firma del solicitante y/o representante legal, de ser el caso.",
            "2 Exhibir original del último recibo de agua, luz o teléfono.",
            "3 En el caso de representación, presentar poder específico en documento público o privado con firma legalizada ante notario o certificada por fedatario de la Municipalidad.",
            "4 Presentar copia legalizada notarialmente o autenticada por fedatario de la Municipalidad del documento privado de fecha cierta, documento público u otro documento, que acredite fehacientemente la propiedad de los bienes antes de haberse trabado la medida cautelar"
        ],
        "derecho_tramite": "GRATUITO",
        "plazo": "Evaluación Previa - 30 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Ejecutor Coactivo",
        "reconsideracion": "-",
        "apelacion": "Tribunal Fiscal"
    },
    {
        "id": "79",
        "numero": "75",
        "procedimiento": "RECURSO DE APELACIÓN DE RESOLUCIONES QUE DENIEGAN TERCERÍAS EN MATERIA TRIBUTARIA",
        "sustento": "BASE LEGAL\n- TUO de la Ley de Procedimiento de Ejecución Coactiva, Decreto Supremo Nº 018-2008-JUS (06.12.08). Arts. 20 y 36.\n- Ley del Procedimiento Administrativo General, Ley Nº 27444 y modificatorias (11.04.01).",
        "requisitos": [
            "1 Escrito presentado ante el Ejecutor Coactivo y dirigido al Tribunal Fiscal, consignando lo siguiente:\na) Nombres y apellidos o denominación o razón social del recurrente o de su representante, de ser el caso.\nb) Domicilio real o procesal del recurrente.\nc) Petición concretamente expresada.\nd) Firma del recurrente o representante legal, de ser el caso; debidamente autorizado por abogado hábil",
            "2 En el caso de representación, presentar poder específico en documento público o privado con firma legalizada ante notario o certificada por fedatario de la Municipalidad."
        ],
        "derecho_tramite": "GRATUITO",
        "plazo": "Evaluación Previa - 30 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Ejecutor Coactivo",
        "reconsideracion": "-",
        "apelacion": "Tribunal Fiscal"
    },
{
        "id": "80",
        "numero": "76",
        "procedimiento": "SOLICITUD DE SUSPENSIÓN DE COBRANZA COACTIVA DE OBLIGACIONES TRIBUTARIAS",
        "sustento": "BASE LEGAL\nTUO de la Ley de Procedimiento de Ejecución Coactiva, Decreto Supremo Nº 018-2008-JUS (06.12.08). Arts. 31.",
        "requisitos": [
            "1 Presentar solicitud firmada por el solicitante o representante legal.",
            "2 En el caso de representación, presentar poder específico en documento público o privado con firma legalizada ante notario o certificada por fedatario de la Municipalidad.",
            "Adicionalmente se deberá:",
            "3 En caso de prescripción: Señalar número y fecha de la resolución mediante la cual se declara prescrita la deuda en cobranza.",
            "4 En caso de cobranza dirigida contra persona distinta al obligado, acreditar que no es el obligado.",
            "5 En caso de recurso administrativo presentado dentro del plazo de ley, señalar número de expediente y fecha de presentación.",
            "6 De encontrarse sometido a un procedimiento concursal o ser una empresa del sistema financiera en liquidación\nEn caso de procedimiento concursal\na) Presentar la publicación de la declaración de insolvencia.\nb) Presentar copia simple del Plan de Reestructuración o del Acuerdo Global de Financiamiento\nc) El administrado o un tercero podrá comunicar el estado de quiebra presentando copia simple de la Resolución de Quiebra Judicial.\n\nEn caso de Disolución y Liquidación de un administrado bajo supervisión de la SBS\na) Señalar fecha de la publicación de la Resolución de Disolución y Liquidación emitida por la SBS",
            "7 En caso de empresas estatales comprendidas en los supuestos del Decreto Ley 25604, debe presentarse la decisión o acuerdo de PROINVERSIÓN en que se especifique la modalidad de promoción de inversión privada y la intangibilidad de los bienes de la empresa.",
            "8 En caso de demanda de amparo o demanda contencioso administrativa, adjuntar copia certificada por el axuliar jurisdiccional de la resolución favorable al administrado",
            "9 En caso de Revisión Judicial, adjuntar copia del cargo de presentación de la demanda, con el sello de recepción del Poder Judicial.",
            "10 En caso de recurso de queja ante el Tribunal Fiscal, señalar número y fecha de la Resolución mediante la cual se declara fundada la queja o se dispone la suspensión temporal del procedimiento",
            "11 En caso de existir pagos ante otra Municipalidad por conflictos de competencia, adjuntar copia legalizada notarialmente o autenticada por Fedatario de la Municipalidad de los recibos que acrediten el pago."
        ],
        "derecho_tramite": "GRATUITO",
        "plazo": "15 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Ejecutor Coactivo",
        "reconsideracion": "-",
        "apelacion": "-"
    },
{
        "id": "81",
        "numero": "77",
        "procedimiento": "TERCERÍA DE PROPIEDAD ANTE COBRANZA DE OBLIGACIONES NO TRIBUTARIAS",
        "sustento": "BASE LEGAL\n- TUO de la Ley de Procedimiento de Ejecución Coactiva, Decreto Supremo Nº 018-2008-JUS (06.12.08). Art. 20.\n- Ley del Procedimiento Administrativo General, Ley Nº 27444 y modificatorias (11.04.01).\n- Sentencia del Tribunal Constitucional recaída en el Expediente Nº 3741-2004-AA/TC (del 14.11.05).",
        "requisitos": [
            "1 Presentar solicitud firmado por el solicitante o representante legal",
            "2 El Domicilio real o procesal del solicitante debe estar dentro del radio urbano de la Provincia de Chanchamayo",
            "3 Exhibir el original del último recibo de agua, luz o teléfono.",
            "4 En el caso de representación, presentar poder general formalizado mediante designación de persona cierta en el escrito, o mediante carta poder con firma del administrado.",
            "5 Presentar copia legalizada notarialmente o autenticada por fedatario de la Municipalidad del documento privado de fecha cierta, documento público u otro documento, que acredite fehacientemente la propiedad de los bienes antes de haberse trabado la medida cautelar."
        ],
        "derecho_tramite": "GRATUITO",
        "plazo": "Evaluación Previa - 30 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Ejecutor Coactivo",
        "reconsideracion": "-",
        "apelacion": "-"
    },
{
        "id": "82",
        "numero": "78",
        "procedimiento": "SOLICITUD DE SUSPENSIÓN DE COBRANZA COACTIVA DE OBLIGACIONES NO TRIBUTARIAS",
        "sustento": "BASE LEGAL\n- TUO de la Ley de Procedimiento de Ejecución Coactiva, Decreto Supremo Nº 018-2008-JUS (06.12.08). Art. 16.\n- Sentencia del Tribunal Constitucional recaída en el Expediente Nº 3741-2004-AA/TC (del 14.11.05).",
        "requisitos": [
            "1 Presentar solicitud firmado por el solicitante o representante legal",
            "2 El Domicilio real o procesal del solicitante debe estar dentro del radio urbano de la Provincia de Chanchamayo",
            "3 En el caso de representación, presentar poder general formalizado mediante designación de persona cierta en el escrito, o mediante carta poder con firma del administrado.",
            "Adicionalmente:",
            "4 En caso de prescripción: Señalar número y fecha de la resolución mediante la cual se declara prescrita la deuda en cobranza.",
            "5 En caso de cobranza dirigida contra persona distinta al obligado, acreditar que no es el obligado.",
            "6 En caso de recurso administrativo presentado dentro del plazo de ley: Señalar número de expediente y fecha de presentación.",
            "7 De encontrarse sometido a un procedimiento concursal o ser una empresa del sistema financiera en liquidación\n\nEn caso de procedimiento concursal\na) Presentar la publicación de la declaración de insolvencia.\nb) Presentar copia simple del Plan de Reestructuración o del Acuerdo Global de financiamiento\nc) El administrado o un tercero podrá comunicar el estado de quiebra presentando copia simple de la Resolución de Quiebra Judicial.\n\nEn caso de Disolución y Liquidación de un administrado bajo supervisión de la SBS\na) Señalar fecha de la publicación de la Resolución de Disolución y Liquidación emitida por la SBS",
            "8 En caso de empresas estatales comprendidas en los supuestos del Decreto Ley 25604, debe presentarse la decisión o acuerdo de PROINVERSIÓN en que se especifique la modalidad de promoción de inversión privada y la intangibilidad de los bienes de la empresa.",
            "9 En caso de demanda de amparo o demanda contencioso administrativa, adjuntar copia certificada por el auxiliar jurisdiccional de la resolución favorable al administrado.",
            "10 En caso de Revisión Judicial, adjuntar copia de la demanda con el sello de recepción del Poder Judicial"
        ],
        "derecho_tramite": "GRATUITO",
        "plazo": "Evaluación Previa - 8 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Ejecutor Coactivo",
        "reconsideracion": "-",
        "apelacion": "-"
    },
{
        "id": "84",
        "numero": "80.1",
        "procedimiento": "LICENCIA DE EDIFICACIÓN: MODALIDAD A - LA CONSTRUCCIÓN DE UNA VIVIENDA UNIFAMILIAR DE HASTA 120 M2 CONTRUIDOS, SIEMPRE QUE CONSTITUYA LA ÚNICA EDIFICACIÓN EN EL LOTE",
        "sustento": "BASE LEGAL\n- Ley de Regulación de Habilitaciones Urbanas y de Edificaciones, Ley Nº 29090 y modificatorias (25.09.07). Arts. 10, 25 y 31.\n- Reglamento de Licencias de Habilitación Urbana y Licencias de Edificación, Decreto Supremo Nº 024-2008-VIVIENDA y modificatorias (27.09.08). Arts. 42, 47 y 50.\n- Reglamento de Verificación Administrativa y Técnica, Decreto Supremo Nº 026-2008-VIVIENDA y modificatorias (27.09.08). Art. 11 numeral a).\n- Ley que modifica diversas disposiciones con el objeto de mejorar el clima de inversión y facilitar el cumplimiento de obligaciones tributarias, Ley Nº 29566 (28.07.10). Arts. 5 y 6.",
        "requisitos": [
            "1 FUE por triplicado, debidamente suscrito.",
            "2 Documentación que acredite que cuenta con derecho a edificar y represente al titular, en caso que el solicitante de la licencia de edificación no sea el propietario del predio.",
            "3 Si el solicitante es una persona jurídica se acompañará la respectiva constitución de la empresa y copia literal del poder expedidos por el Registro de Personas Jurídicas, vigente al momento de presentación de los documentos",
            "4 Declaración Jurada de habilitación de los profesionales que suscriben la documentación técnica técnica.",
            "5 Firma del solicitante y de los profesionales responsables del proyecto, en los planos presentados para todos los trámites.",
            "6 Documentación técnica por duplicado, compuesta por los planos de ubicación, arquitectura, estructuras, instalaciones sanitarias y eléctricas.",
            "7 Pago por el Derecho de la Tasa Administrativa:",
            "--------------------------------------------------",
            "⚠️ NO ESTÁN CONSIDERADAS EN ESTA MODALIDAD:",
            "1) Las obras de edificación en bienes inmuebles que constituyan Patrimonio Cultural de la Nación declarado por el Instituto Nacional de Cultura-INC, e incluidas en la lista a la que se hace referencia en el inciso f) del Art.3 numeral 2 de la Ley Nº 29090.",
            "2) Las Obras que requieran la ejecución de sótanos o semisotanos, o una profundidad de excavación mayor a 1.50 m. y colinden con edificaciones existentes. En dicho caso debe tramitarse la licencia de edificación bajo la Modalidad B.",
            "--------------------------------------------------",
            "📌 NOTAS PARA EL CIUDADANO:",
            "Para el caso de edificación de vivienda unifamiliar de hasta 120 m2 construidos y siempre que sea la única edificación que se construya en el lote, se podrá optar por la adquisición de los planos del Banco de Proyectos de la Municipalidad respectiva."
        ],
        "derecho_tramite": "2.7737% UIT",
        "plazo": "Evaluación Previa - 10 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Desarrollo Urbano y Territorial",
        "reconsideracion": "Gerente de Desarrollo Urbano y Territorial\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente Municipal\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
{
        "id": "85",
        "numero": "80.2",
        "procedimiento": "LICENCIA DE EDIFICACIÓN: MODALIDAD A - LA AMPLIACIÓN DE UNA VIVIENDA UNIFAMILIAR CUYA EDIFICACIÓN ORIGINAL CUENTE CON LICENCIA DE CONSTRUCCIÓN O DECLARATORIA DE FÁBRICA Y/O EDIFICACIÓN, Y LA SUMATORIA DEL ÁREA CONSTRUIDA DE AMBAS NO SUPERE LOS 200 M2.",
        "sustento": "BASE LEGAL\n- Ley de Regulación de Habilitaciones Urbanas y de Edificaciones, Ley Nº 29090 y modificatorias (25.09.07). Arts. 10, 25 y 31.\n- Reglamento de Licencias de Habilitación Urbana y Licencias de Edificación, Decreto Supremo Nº 024-2008-VIVIENDA y modificatorias (27.09.08). Arts. 42, 47 y 50.\n- Reglamento de Verificación Administrativa y Técnica, Decreto Supremo Nº 026-2008-VIVIENDA y modificatorias (27.09.08). Art. 11 numeral a).\n- Ley que modifica diversas disposiciones con el objeto de mejorar el clima de inversión y facilitar el cumplimiento de obligaciones tributarias, Ley Nº 29566 (28.07.10). Arts. 5 y 6.",
        "requisitos": [
            "1 FUE por triplicado, debidamente suscrito.",
            "2 Documentación que acredite que cuenta con derecho a edificar y represente al titular, en caso que el solicitante de la licencia de edificación no sea el propietario del predio.",
            "3 Si el solicitante es una persona jurídica se acompañará la respectiva constitución de la empresa y copia literal del poder expedidos por el Registro de Personas Jurídicas, vigente al momento de presentación de los documentos.",
            "4 Declaración Jurada de habilitación de los profesionales que suscriben la documentación técnica.",
            "5 Presentar copia literal de la inscripción de la declaratoria de edificación y/o fábrica junto con los planos respectivos. De haber sido emitidos por otra entidad, copia de la Licencia y/o Conformidad o Conformidad o Financiación Conformidad o Finalización de Obra con los planos correspondientes",
            "6 Firma del solicitante y de los profesionales responsables del proyecto, en los planos presentados para todos los trámites.",
            "7 Documentación técnica por duplicado, compuesta por los planos de ubicación, arquitectura, estructuras, instalaciones sanitarias y eléctricas.",
            "8 Pago por el Derecho de la Tasa Administrativa:",
            "--------------------------------------------------",
            "⚠️ NO ESTÁN CONSIDERADAS EN ESTA MODALIDAD:",
            "1) Las obras de edificación en bienes inmuebles que constituyan Patrimonio Cultural de la Nación declarado por el Instituto Nacional de Cultura-INC, e incluidas en la lista a la que se hace referencia en el inciso f) del Art.3 numeral 2 de la Ley Nº 29090.",
            "2) Las Obras que requieran la ejecución de sótanos o semisotanos, o una profundidad de excavación mayor a 1.50 m. y colinden con edificaciones existentes. En dicho caso debe tramitarse la licencia de edificación bajo la Modalidad B."
        ],
        "derecho_tramite": "4.3079% UIT",
        "plazo": "Evaluación Previa - 10 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Desarrollo Urbano y Territorial",
        "reconsideracion": "Gerente de Desarrollo Urbano y Territorial\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente Municipal\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
{
        "id": "86",
        "numero": "80.3",
        "procedimiento": "LICENCIA DE EDIFICACIÓN: MODALIDAD A - LA REMODELACIÓN DE UNA VIVIENDA UNIFAMILIAR SIN MODIFICACIÓN ESTRUCTURAL, NI CAMBIO DE USO, NI AUMENTO DE ÁREA CONSTRUIDA",
        "sustento": "BASE LEGAL\n- Ley de Regulación de Habilitaciones Urbanas y de Edificaciones, Ley Nº 29090 y modificatorias (25.09.07). Arts. 10, 25 y 31.\n- Reglamento de Licencias de Habilitación Urbana y Licencias de Edificación, Decreto Supremo Nº 024-2008-VIVIENDA y modificatorias (27.09.08). Arts. 42, 47 y 50.\n- Reglamento de Verificación Administrativa y Técnica, Decreto Supremo Nº 026-2008-VIVIENDA y modificatorias (27.09.08). Art. 11 numeral a).\n- Ley que modifica diversas disposiciones con el objeto de mejorar el clima de inversión y facilitar el cumplimiento de obligaciones tributarias, Ley Nº 29566 (28.07.10). Arts. 5 y 6.",
        "requisitos": [
            "1 FUE por triplicado, debidamente suscrito.",
            "2 Documentación que acredite que cuenta con derecho a edificar y represente al titular, en caso que el solicitante de la licencia de edificación no sea el propietario del predio",
            "3 Si el solicitante es una persona jurídica se acompañará la respectiva constitución de la empresa y copia literal del poder expedidos por el Registro de Personas Jurídicas, vigente al momento de presentación de los documentos.",
            "4 Declaración Jurada de habilitación de los profesionales que suscriben la documentación técnica",
            "5 Presentar copia literal de la inscripción de la declaratoria de edificación y/o fábrica junto con los planos respectivos. De haber sido emitidos por otra entidad, copia de la Licencia y/o Conformidad o Finalización de Obra con los planos correspondientes.",
            "6 Firma del solicitante y de los profesionales responsables del proyecto, en los planos presentados para todos los trámites.",
            "7 Documentación técnica por duplicado, compuesta por los planos de ubicación, arquitectura, estructuras, instalaciones sanitarias y eléctricas",
            "8 Pago por el Derecho de la Tasa Administrativa:",
            "--------------------------------------------------",
            "⚠️ NO ESTÁN CONSIDERADAS EN ESTA MODALIDAD:",
            "1) Las obras de edificación en bienes inmuebles que constituyan Patrimonio Cultural de la Nación declarado por el Instituto Nacional de Cultura-INC, e incluidas en la lista a la que se hace referencia en el inciso f) del Art.3 numeral 2 de la Ley Nº 29090.",
            "2) Las Obras que requieran la ejecución de sótanos o semisotanos, o una profundidad de excavación mayor a 1.50 m. y colinden con edificaciones existentes. En dicho caso debe tramitarse la licencia de edificación bajo la Modalidad B."
        ],
        "derecho_tramite": "4.3079% UIT",
        "plazo": "Evaluación Previa - 10 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Desarrollo Urbano y Territorial",
        "reconsideracion": "Gerente de Desarrollo Urbano y Territorial\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente Municipal\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
{
        "id": "87",
        "numero": "80.4",
        "procedimiento": "LICENCIA DE EDIFICACIÓN: MODALIDAD A - AMPLIACIONES CONSIDERADAS OBRAS MENORES SEGÚN LO ESTABLECIDO EN EL REGLAMENTO NACIONAL DE EDIFICACIONES",
        "sustento": "BASE LEGAL\n- Ley de Regulación de Habilitaciones Urbanas y de Edificaciones, Ley Nº 29090 y modificatorias (25.09.07). Arts. 10, 25 y 31.\n- Reglamento de Licencias de Habilitación Urbana y Licencias de Edificación, Decreto Supremo Nº 024-2008-VIVIENDA y modificatorias (27.09.08). Arts. 42, 47 y 50.\n- Ley que modifica diversas disposiciones con el objeto de mejorar el clima de inversión y facilitar el cumplimiento de obligaciones tributarias, Ley Nº 29566 (28.07.10). Arts. 5 y 6.",
        "requisitos": [
            "1 FUE por triplicado, debidamente suscrito.",
            "2 Documentación que acredite que cuenta con derecho a edificar y represente al titular, en caso que el solicitante de la licencia de edificación no sea el propietario del predio.",
            "3 Si el solicitante es una persona jurídica se acompañará la respectiva constitución de la empresa y copia literal del poder expedidos por el Registro de Personas Jurídicas, vigente al momento de presentación de los documentos",
            "4 Declaración Jurada de habilitación de los profesionales que suscriben la documentación técnica",
            "5 Copia literal de la inscripción de la declaratoria de edificación y/o fábrica junto con los planos respectivos. De haber sido emitidos por otra entidad, copia de la Licencia y/o Conformidad o Finalización de Obra con los planos correspondientes.",
            "6 Firma del solicitante y de los profesionales responsables del proyecto, en los planos presentados para todos los trámites.",
            "7 Documentación técnica por duplicado, compuesta por los planos de ubicación y arquitectura.",
            "8 Pago por el Derecho de la Tasa Administrativa:",
            "--------------------------------------------------",
            "⚠️ NO ESTÁN CONSIDERADAS EN ESTA MODALIDAD:",
            "1) Las obras de edificación en bienes inmuebles que constituyan Patrimonio Cultural de la Nación declarado por el Instituto Nacional de Cultura-INC, e incluidas en la lista a la que se hace referencia en el inciso f) del Art.3 numeral 2 de la Ley Nº 29090.",
            "2) Las Obras que requieran la ejecución de sótanos o semisotanos, o una profundidad de excavación mayor a 1.50 m. y colinden con edificaciones existentes. En dicho caso debe tramitarse la licencia de edificación bajo la Modalidad B."
        ],
        "derecho_tramite": "1.8816% UIT",
        "plazo": "Evaluación Previa - 10 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Desarrollo Urbano y Territorial",
        "reconsideracion": "Gerente de Desarrollo Urbano y Territorial\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente Municipal\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
{
        "id": "88",
        "numero": "80.5",
        "procedimiento": "LICENCIA DE EDIFICACIÓN: MODALIDAD A - LA DEMOLICIÓN TOTAL DE EDIFICACIONES MENORES DE 5 PISOS DE ALTURA, SIEMPRE QUE NO REQUIERAN EL USO DE EXPLOSIVOS",
        "sustento": "BASE LEGAL\nLey de Regulación de Habilitaciones Urbanas y de Edificaciones, Ley Nº 29090 y modificatorias (25.09.07). Arts. 10, 25 y 31.\nReglamento de Licencias de Habilitación Urbana y Licencias de Edificación, Decreto Supremo Nº 024-2008-VIVIENDA y modificatorias (27.09.08). Arts. 42, 47 y 50.\nLey que modifica diversas disposiciones con el objeto de mejorar el clima de inversión y facilitar el cumplimiento de obligaciones tributarias, Ley Nº 29566 (28.07.10). Arts. 5 y 6.",
        "requisitos": [
            "1 FUE por triplicado, debidamente suscrito.",
            "2 Documentación que acredite que cuenta con derecho a edificar y represente al titular, en caso que el solicitante de la licencia de edificación no sea el propietario del predio.",
            "3 Si el solicitante es una persona jurídica se acompañará la respectiva constitución de la empresa y copia literal del poder expedidos por el Registro de Personas Jurídicas, vigente al momento de presentación de los documentos.",
            "4 Declaración Jurada de habilitación de los profesionales que suscriben la documentación técnica",
            "5 Copia literal de la inscripción de la declaratoria de edificación y/o fábrica junto con los planos respectivos. De haber sido emitidos por otra entidad, copia de la Licencia y/o Conformidad o Finalización de Obra con los planos correspondientes.",
            "6 En el supuesto de que la fábrica no se encuentre inscrita, se deberá presentar la Licencia y/o Conformidad o Finalización de Obra, así como los planos de ubicación, localización y de planta del levantamiento de la edificación, sin perjuicio de las sanciones que la Municipalidad considere.",
            "7 En el caso de demoliciones totales inscritas en el Registro de Predios, se acreditará que sobre el bien no recaigan cargas y/o gravámenes, en su defecto, se acreditará la autorización del titular de la carga o gravámen.",
            "8 Firma del solicitante y de los profesionales responsables del proyecto, en los planos presentados presentados para todos los trámites.",
            "9 Documentación técnica por duplicado, compuesta por los planos de ubicación y arquitectura.",
            "10 Pago por el Derecho de la Tasa Administrativa:",
            "--------------------------------------------------",
            "📌 NOTAS PARA EL CIUDADANO:",
            "Las edificaciones a demoler no deben constituir parte integrante del Patrimonio Cultural de la Nación."
        ],
        "derecho_tramite": "2.8368% UIT",
        "plazo": "Evaluación Previa - 10 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Desarrollo Urbano y Territorial",
        "reconsideracion": "Gerente de Desarrollo Urbano y Territorial\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente Municipal\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
{
        "id": "89",
        "numero": "80.6",
        "procedimiento": "LICENCIA DE EDIFICACIÓN: MODALIDAD A - LA CONSTRUCCIÓN DE CERCOS DE MÁS DE 20 METROS DE LONGITUD, SIEMPRE QUE EL INMUEBLE NO SE ENCUENTRE BAJO EL RÉGIMEN DE UNIDADES INMOBILIARIAS DE PROPIEDAD EXCLUSIVA Y DE PROPIEDAD COMÚN, DE ACUERDO A LA LEGISLACIÓN DE LA MATERIA",
        "sustento": "BASE LEGAL\n- Ley de Regulación de Habilitaciones Urbanas y de Edificaciones, Ley Nº 29090 y modificatorias (25.09.07). Arts. 10, 25 y 31.\n- Reglamento de Licencias de Habilitación Urbana y Licencias de Edificación, Decreto Supremo Nº 024-2008-VIVIENDA y modificatorias (27.09.08). Arts. 42, 47 y 50.\n- Ley que modifica diversas disposiciones con el objeto de mejorar el clima de inversión y facilitar el cumplimiento de obligaciones tributarias, Ley Nº 29566 (28.07.10). Arts. 5 y 6.",
        "requisitos": [
            "1 FUE por triplicado, debidamente suscrito.",
            "2 Documentación que acredite que cuenta con derecho a edificar y represente al titular, en caso que el solicitante de la licencia de edificación no sea el propietario del predio.",
            "3 Si el solicitante es una persona jurídica se acompañará la respectiva constitución de la empresa y copia literal del poder expedidos por el Registro de Personas Jurídicas, vigente al momento de presentación de los documentos.",
            "4 Declaración Jurada de habilitación de los profesionales que suscriben la documentación técnica.",
            "5 Copia literal de la inscripción de la declaratoria de edificación y/o fábrica junto con los planos respectivos. De haber sido emitidos por otra entidad, copia de la Licencia y/o Conformidad o Finalización de Obra con los planos correspondientes.",
            "6 Firma del solicitante y de los profesionales responsables del proyecto, en los planos presentados para todos los trámites.",
            "7 Documentación técnica por duplicado, compuesta por:\na) Planos de ubicación, arquitectura y estructuras.\nb) Planos de instalaciones sanitarias y eléctricas de ser el caso.",
            "8 Pago por el Derecho de la Tasa Administrativa:",
            "--------------------------------------------------",
            "⚠️ NO ESTÁN CONSIDERADAS EN ESTA MODALIDAD:",
            "1) Las obras de edificación en bienes inmuebles que constituyan Patrimonio Cultural de la Nación declarado por el Instituto Nacional de Cultura-INC, e incluidas en la lista a la que se hace referencia en el inciso f) del Art.3 numeral 2 de la Ley Nº 29090.",
            "2) Las Obras que requieran la ejecución de sótanos o semisotanos, o una profundidad de excavación mayor a 1.50 m. y colinden con edificaciones existentes. En dicho caso debe tramitarse la licencia de edificación bajo la Modalidad B."
        ],
        "derecho_tramite": "3.7289% UIT",
        "plazo": "Evaluación Previa - 10 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Desarrollo Urbano y Territorial",
        "reconsideracion": "Gerente de Desarrollo Urbano y Territorial\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente Municipal\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
{
        "id": "90",
        "numero": "81.1",
        "procedimiento": "LICENCIA DE EDIFICACIÓN: MODALIDAD B - LAS EDIFICACIONES PARA FINES DE VIVIENDA UNIFAMILIAR, MULTIFAMILIAR, QUINTA O CONDOMINIOS DE VIVIENDA UNIFAMILIAR Y/O MULTIFAMILIAR NO MAYORES A CINCO (05) PISOS, SIEMPRE QUE EL PROYECTO TENGA UN MÁXIMO DE 3,000 M2 DE ÁREA CONSTRUIDA",
        "sustento": "BASE LEGAL\n- Ley de Regulación de Habilitaciones Urbanas y de Edificaciones, Ley Nº 29090 y modificatorias (25.09.07). Arts. 10, 25 y 31.\n- Reglamento de Licencias de Habilitación Urbana y Licencias de Edificación, Decreto Supremo Nº 024-2008-VIVIENDA y modificatorias (27.09.08). Arts. 42, 47 y 51.\n- Ley que modifica diversas disposiciones con el objeto de mejorar el clima de inversión y facilitar el cumplimiento de obligaciones tributarias, Ley Nº 29566 (28.07.10). Arts. 5 y 6.",
        "requisitos": [
            "1 FUE por triplicado, debidamente suscrito.",
            "2 Documentación que acredite que cuenta con derecho a edificar y represente al titular, en caso que el solicitante de la licencia de edificación no sea el propietario del predio.",
            "3 Si el solicitante es una persona jurídica se acompañará la respectiva constitución de la empresa y copia literal del poder expedidos por el Registro de Personas Jurídicas, vigente al momento de presentación de los documentos",
            "4 Declaración Jurada de habilitación de los profesionales que suscriben la documentación técnica",
            "5 Firma del solicitante y de los profesionales responsables del proyecto, en los planos presentados para todos los trámites.",
            "6 Certificados de Factibilidad de Servicios, para Obra Nueva de vivienda Multifamiliar o ampliación de Vivienda Unifamiliar a Multifamiliar o fines diferentes al de vivienda.",
            "7 Documentación técnica, por duplicado, la misma que estará compuesta por:\n- Plano de ubicación y localización según formato.\n- Planos de Arquitectura, Estructuras, Instalaciones Sanitarias, Eléctricas y otras, de ser el caso, firmados y sellados por los profesionales responsables del proyecto y por el propietario, acompañando las memorias justificativas por especialidad.\n- De ser el caso, plano de sostenimiento de excavaciones de acuerdo con lo establecido en artículo 33 de la Norma E 050 del RNE acompañado de la memoria descriptiva que precise las características de la obra, además de las edificaciones colindantes indicando el número de pisos y sótanos, complementando con fotos.\n- Estudio de Mecánica de Suelos, según los casos que establece el RNE.",
            "8 Póliza CAR (Todo Riesgo Contratista) o la Póliza de Responsabilidad Civil, para las edificaciones multifamiliares y condominios de vivienda unifamiliar o multifamiliar, contemplados en los literales a) y c) del numeral 42.2 del artículo 42 del Decreto Supremo Nº 024-2008-VIVIENDA, con una cobertura por daños materiales y personales a terceros y personales a terceros y como complemento al Seguro Complementario de Trabajo de Riesgo previsto en la Ley Nº 26790, Ley de Modernización de la Seguridad Social en Salud.\nLa Póliza debe estar vigente durante todo el periodo de ejecución de la obra y es exigida por la Municipalidad el día previo al inicio de los trabajos.",
            "9 Pago por el Derecho de la Tasa Administrativa:",
            "--------------------------------------------------",
            "⚠️ NO ESTÁN CONSIDERADAS EN ESTA MODALIDAD:",
            "1) Las obras de edificación en bienes inmuebles que constituyan Patrimonio Cultural de la Nación declarado por el INC, e incluidas en la lista a la que se hace referencia en el inciso f) del artículo 3 numeral 2 de la Ley Nº 29090."
        ],
        "derecho_tramite": "4.3079% UIT",
        "plazo": "Evaluación Previa - 15 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Desarrollo Urbano y Territorial",
        "reconsideracion": "Gerente de Desarrollo Urbano y Territorial\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente Municipal\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
{
        "id": "91",
        "numero": "81.2",
        "procedimiento": "LICENCIA DE EDIFICACIÓN: MODALIDAD B - LAS OBRAS DE AMPLIACIÓN O REMODELACIÓN DE UNA EDIFICACIÓN EXISTENTE CON MODIFICACIÓN ESTRUCTURAL, AUMENTO DE ÁREA CONSTRUIDA O CAMBIO DE USO, (LAS AMPLIACIONES PROCEDERÁN SOLO CUANDO LA EDIFICACIÓN EXISTENTE MANTENGA EL USO RESIDENCIAL)",
        "sustento": "BASE LEGAL\n- Ley de Regulación de Habilitaciones Urbanas y de Edificaciones, Ley Nº 29090 y modificatorias (25.09.07). Arts. 10, 25 y 31.\n- Reglamento de Licencias de Habilitación Urbana y Licencias de Edificación, Decreto Supremo Nº 024-2008-VIVIENDA y modificatorias (27.09.08). Arts. 42, 47 y 51.\n- Ley que modifica diversas disposiciones con el objeto de mejorar el clima de inversión y facilitar el cumplimiento de obligaciones tributarias, Ley Nº 29566 (28.07.10). Arts. 5 y 6.",
        "requisitos": [
            "1 FUE por triplicado, debidamente suscrito.",
            "2 Documentación que acredite que cuenta con derecho a edificar y represente al titular, en caso que el solicitante de la licencia de edificación no sea el propietario del predio.",
            "3 Si el solicitante es una persona jurídica se acompañará la respectiva constitución de la empresa y copia literal del poder expedidos por el Registro de Personas Jurídicas, vigente al momento de presentación de los documentos.",
            "4 Declaración Jurada de habilitación de los profesionales que suscriben la documentación técnica.",
            "5 Para los casos de remodelaciones y ampliaciones, se presentará la copia literal de la inscripción de la declaratoria de edificación y/o fábrica junto con los planos respectivos. De haber sido emitidos por otra entidad, copia de la Licencia y/o Conformidad o Finalización de Obra con los planos correspondientes.",
            "6 Firma del solicitante y de los profesionales responsables del proyecto, en los planos presentados para todos los trámites.",
            "7 Certificados de Factibilidad de Servicios, para Obra Nueva de vivienda Multifamiliar o ampliación de Vivienda Unifamiliar a Multifamiliar o fines diferentes al de vivienda.",
            "8 Documentación técnica, por duplicado, la misma que estará compuesta por:\n- Plano de ubicación y localización según formato.\n- Planos de Arquitectura, Estructuras, Instalaciones Sanitarias, Eléctricas y otras, de ser el caso, firmados y sellados por los profesionales responsables del proyecto y por el propietario, acompañando las memorias justificativas por especialidad.\n- De ser el caso, plano de sostenimiento de excavaciones de acuerdo con lo establecido en el artículo 33 de la Norma E 050 del RNE acompañado de la memoria descriptiva que precise las características de la obra, además de las edificaciones colindantes indicando el número de pisos y sótanos, complementando con fotos.\n- Estudio de Mecánica de Suelos, según los casos que establece el RNE.",
            "9 Póliza CAR (Todo Riesgo Contratista) o la Póliza de Responsabilidad Civil, para las edificaciones multifamiliares y condominios de vivienda unifamiliar o multifamily, contemplados en los literales a) y c) del numeral 42.2 del artículo 42 del Decreto Supremo Nº 024-2008-VIVIENDA, con una cobertura por daños materiales y personales a terceros y como complemento al Seguro Complementario de Trabajo de Riesgo previsto en la Ley Nº 26790, Ley de Modernización de la Seguridad Social en Salud. La Póliza debe estar vigente durante todo el periodo de ejecución de la obra y es exigida por la Municipalidad el día previo al inicio de los trabajos",
            "10 Pago por el Derecho de la Tasa Administrativa:",
            "--------------------------------------------------",
            "⚠️ NO ESTÁN CONSIDERADAS EN ESTA MODALIDAD:",
            "1) Las obras de edificación en bienes inmuebles que constituyan Patrimonio Cultural de la Nación declarado por el INC, e incluidas en la lista a la que se hace referencia en el inciso f) del artículo 3 numeral 2 de la Ley Nº 29090."
        ],
        "derecho_tramite": "5.5632% UIT",
        "plazo": "Evaluación Previa - 15 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Desarrollo Urbano y Territorial",
        "reconsideracion": "Gerente de Desarrollo Urbano y Territorial\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente Municipal\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
{
        "id": "92",
        "numero": "81.3",
        "procedimiento": "LICENCIA DE EDIFICACIÓN: MODALIDAD B - EN CASO DE DEMOLICIONES PARCIALES",
        "sustento": "BASE LEGAL\n- Ley de Regulación de Habilitaciones Urbanas y de Edificaciones, Ley Nº 29090 y modificatorias (25.09.07). Arts. 10, 25 y 31.\n- Reglamento de Licencias de Habilitación Urbana y Licencias de Edificación, Decreto Supremo Nº 024-2008-VIVIENDA y modificatorias (27.09.08). Arts. 42, 47 y 51.\n- Ley que modifica diversas disposiciones con el objeto de mejorar el clima de inversión y facilitar el cumplimiento de obligaciones tributarias, Ley Nº 29566 (28.07.10). Arts. 5 y 6.",
        "requisitos": [
            "1 FUE por triplicado, debidamente suscrito.",
            "2 Documentación que acredite que cuenta con derecho a edificar y represente al titular, en caso que el solicitante de la licencia de edificación no sea el propietario del predio.",
            "3 Si el solicitante es una persona jurídica se acompañará la respectiva constitución de la empresa y copia literal del poder expedidos por el Registro de Personas Jurídicas, vigente al momento de presentación de los documentos.",
            "4 Declaración Jurada de habilitación de los profesionales que suscriben la documentación técnica",
            "5 Copia literal de la inscripción de la declaratoria de edificación y/o fábrica junto con los planos respectivos. De haber sido emitidos por otra entidad, copia de la Licencia y/o Conformidad o Finalización de Obra con los planos correspondientes.",
            "6 En el supuesto de que la fábrica no se encuentre inscrita, se deberá presentar la Licencia y/o Conformidad o Finalización de Obra, así como los planos de ubicación, localización y de planta del levantamiento de la edificación, sin perjuicio de las sanciones que la Municipalidad considere.",
            "7 Firma del solicitante y de los profesionales responsables del proyecto, en los planos presentados para todos los trámites.",
            "8 Certificados de Factibilidad de Servicios, para Obra Nueva de vivienda Multifamiliar o ampliación de Vivienda Unifamiliar a Multifamiliar o fines diferentes al de vivienda.",
            "9 Documentación técnica, por duplicado, la misma que estará compuesta por:\n- Plano de ubicación y localización según formato.\n- Planos de Arquitectura, Estructuras, Instalaciones Sanitarias, Eléctricas y otras, de ser el caso, firmados y sellados por los profesionales responsables del proyecto y por el propietario, acompañando las memorias justificativas por especialidad\n- De ser el caso, plano de sostenimiento de excavaciones de acuerdo con lo establecido en el artículo 33 de la Norma E 050 del RNE acompañado de la memoria descriptiva que precise las características de la obra, además de las edificaciones colindantes indicando el número de pisos y sótanos, complementando con fotos.\n- Estudio de Mecánica de Suelos, según los casos que establece el RNE.",
            "10 Póliza CAR (Todo Riesgo Contratista) o la Póliza de Responsabilidad Civil, para las edificaciones multifamiliares y condominios de vivienda unifamiliar o multifamiliar, contemplados en los literales a) y c) del numeral 42.2 del artículo 42 del Decreto Supremo Nº 024-2008-VIVIENDA, con una cobertura por daños materiales y personales a terceros y como complemento al Seguro Complementario de Trabajo de Riesgo previsto en la Ley Nº 26790, Ley de Modernización de la Seguridad Social en Salud. La Póliza debe estar vigente durante todo el periodo de ejecución de la obra y es exigida por la Municipalidad el día previo al inicio de los trabajos.",
            "11 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "3.1763% UIT",
        "plazo": "Evaluación Previa - 15 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Desarrollo Urbano y Territorial",
        "reconsideracion": "Gerente de Desarrollo Urbano y Territorial\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente Municipal\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
{
        "id": "93",
        "numero": "81.4",
        "procedimiento": "LICENCIA DE EDIFICACIÓN: MODALIDAD B - LA CONSTRUCCIÓN DE CERCOS EN INMUEBLES QUE SE ENCUENTREN BAJO EL RÉGIMEN DE UNIDADES INMOBILIARIAS DE PROPIEDAD EXCLUSIVA Y DE PROPIEDAD COMÚN, DE ACUERDO A LA LEGISLACIÓN DE LA MATERIA",
        "sustento": "BASE LEGAL\n- Ley de Regulación de Habilitaciones Urbanas y de Edificaciones, Ley Nº 29090 y modificatorias (25.09.07). Arts. 10, 25 y 31.\n- Reglamento de Licencias de Habilitación Urbana y Licencias de Edificación, Decreto Supremo Nº 024-2008-VIVIENDA y modificatorias (27.09.08). Arts. 42, 47 y 51.\n- Ley que modifica diversas disposiciones con el objeto de mejorar el clima de inversión y facilitar el cumplimiento de obligaciones tributarias, Ley Nº 29566 (28.07.10). Arts. 5 y 6.",
        "requisitos": [
            "1 FUE por triplicado, debidamente suscrito.",
            "2 Documentación que acredite que cuenta con derecho a edificar y represente al titular, en caso que el solicitante de la licencia de edificación no sea el propietario del predio.",
            "3 Si el solicitante es una persona jurídica se acompañará la respectiva constitución de la empresa y copia literal del poder expedidos por el Registro de Personas Jurídicas, vigente al momento de presentación de los documentos.",
            "4 Declaración Jurada de habilitación de los profesionales que suscriben la documentación técnica",
            "5 Copia literal de la inscripción de la declaratoria de edificación y/o fábrica junto con los planos respectivos. De haber sido emitidos por otra entidad, copia de la Licencia y/o Conformidad o Finalización de Obra con los planos",
            "6 Firma del solicitante y de los profesionales responsables del proyecto, en los planos presentados para todos los trámites.",
            "7 Certificados de Factibilidad de Servicios, para Obra Nueva de vivienda Multifamiliar o ampliación de Vivienda Unifamiliar a Multifamiliar o fines diferentes al de vivienda.",
            "8 Documentación técnica, por duplicado, la misma que estará compuesta por:\n- Plano de ubicación y localización según formato.\n- Planos de Arquitectura, Estructuras, Instalaciones Sanitarias, Eléctricas y otras, de ser el caso, firmados y sellados por los profesionales responsables del proyecto y por el propietario, acompañando las memorias justificativas por especialidad.\n- De ser el caso, plano de sostenimiento de excavaciones de acuerdo con lo establecido en el art. 33 de la Norma E 050 del RNE acompañado de la memoria descriptiva que precise las características de la obra, además de las edificaciones colindantes indicando el número de pisos y sótanos complementando con fotos.\n- Estudio de Mecánica de Suelos, según los casos que establece el RNE.",
            "9 Pago por el Derecho de la Tasa Administrativa:",
            "--------------------------------------------------",
            "⚠️ NO ESTÁN CONSIDERADAS EN ESTA MODALIDAD:",
            "1) Las obras de edificación en bienes inmuebles que constituyan Patrimonio Cultural de la Nación declarado por el INC, e incluidas en la lista a la que se hace referencia en el inciso f) del artículo 3 numeral 2 de la Ley Nº 29090."
        ],
        "derecho_tramite": "4.4158% UIT",
        "plazo": "Evaluación Previa - 15 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Desarrollo Urbano y Territorial",
        "reconsideracion": "Gerente de Desarrollo Urbano y Territorial\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente Municipal\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
{
        "id": "94",
        "numero": "82.1",
        "procedimiento": "LICENCIA DE EDIFICACIÓN: MODALIDAD C (APROBACIÓN CON EVALUACIÓN PREVIA DEL PROYECTO POR LA COMISIÓN TÉCNICA) - LAS EDIFICACIONES PARA FINES DE VIVIENDA MULTIFAMILIAR, QUINTA O CONDOMINIOS QUE INCLUYAN VIVIENDA MULTIFAMILIAR DE MÁS DE 5 PISOS Y/O MÁS DE 3,000 M2 DE ÁREA CONSTRUIDA.",
        "sustento": "BASE LEGAL\n- Ley de Regulación de Habilitaciones Urbanas y de Edificaciones, Ley Nº 29090 y modificatorias (25.09.07). Arts. 10, 25 y 31.\n- Reglamento de Licencias de Habilitación Urbana y Licencias de Edificación, Decreto Supremo Nº 024-2008-VIVIENDA y modificatorias (27.09.08). Arts. 42, 47, 51 y 54\n- Ley que modifica diversas disposiciones con el objeto de mejorar el clima de inversión y facilitar el cumplimiento de obligaciones tributarias, Ley Nº 29566 (28.07.10). Arts. 5 y 6.",
        "requisitos": [
            "1 FUE por triplicado, debidamente suscrito.",
            "2 Documentación que acredite que cuenta con derecho a edificar y represente al titular, en caso que el solicitante de la licencia de edificación no sea el propietario del predio.",
            "3 Si el solicitante es una persona jurídica se acompañará la respectiva constitución de la empresa y copia literal del poder expedidos por el Registro de Personas Jurídicas, vigente al momento de presentación de los documentos.",
            "4 Declaración Jurada de habilitación de los profesionales que suscriben la documentación técnica",
            "5 Firma del solicitante y de los profesionales responsables del proyecto, en los planos presentados para todos los trámites.",
            "6 Certificados de Factibilidad de Servicios, para Obra Nueva de vivienda Multifamiliar o ampliación de Vivienda Unifamiliar a Multifamiliar o fines diferentes al de vivienda.",
            "7 Documentación técnica, por duplicado, la misma que estará compuesta por:\n- Plano de ubicación y localización según formato.\n- Planos de Arquitectura, Estructuras, Instalaciones Sanitarias, Eléctricas y otras, de ser el caso, firmados y sellados por los profesionales responsables del proyecto y por el propietario, acompañando las memorias justificativas por especialidad.\n- De ser el caso, plano de sostenimiento de excavaciones de acuerdo con lo establecido en el art. 33 de la Norma E 050 del RNE acompañado de la memoria descriptiva que precise las características de la obra, además de las edificaciones colindantes indicando el número de pisos y sótanos, complementando con fotos\n- Estudio de Mecánica de Suelos, según los casos que establece el RNE.",
            "8 Póliza CAR (Todo Riesgo Contratista) o la Póliza de Responsabilidad Civil, para las edificaciones multifamiliares y condominios de vivienda unifamiliar o multifamiliar, contemplados en los literales a) y c) del numeral 42.2 del artículo 42 del Decreto Supremo Nº 024-2008-VIVIENDA, con una cobertura por daños materiales y personales a terceros y como complemento al Seguro Complementario de Trabajo de Riesgo previsto en la Ley Nº 26790, Ley de Modernización y de la Seguridad Social en Salud\nLa Póliza debe estar vigente durante todo el periodo de ejecución de la obra y es exigida por la Municipalidad el día previo al inicio de los trabajos.",
            "9 Estudios de Impacto ambiental y vial en los casos que se requiera.",
            "10 El Dictamen Conforme del Anteproyecto con los planos respectivos, según corresponda.",
            "11 En caso de proyectos de gran magnitud, los planos podrán ser presentados en secciones con escala conveniente que permita su fácil lectura, conjuntamente con el plano del proyecto integral.",
            "12 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "11.7421% UIT",
        "plazo": "Evaluación Previa - 25 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Desarrollo Urbano y Territorial",
        "reconsideracion": "Gerente de Desarrollo Urbano y Territorial\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente Municipal\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
{
        "id": "95",
        "numero": "82.2",
        "procedimiento": "LICENCIA DE EDIFICACIÓN: MODALIDAD C (APROBACIÓN CON EVALUACIÓN PREVIA DEL PROYECTO POR LA COMISIÓN TÉCNICA) - LAS EDIFICACIONES PARA FINES DIFERENTES DE VIVIENDA A EXCEPCIÓN DE LAS PREVISTAS EN LA MODALIDAD D",
        "sustento": "BASE LEGAL\n- Ley de Regulación de Habilitaciones Urbanas y de Edificaciones, Ley Nº 29090 y modificatorias (25.09.07). Arts. 10, 25 y 31.\n- Reglamento de Licencias de Habilitación Urbana y Licencias de Edificación, Decreto Supremo Nº 024-2008-VIVIENDA y modificatorias (27.09.08). Arts. 42, 47, 51 y 54\n- Ley que modifica diversas disposiciones con el objeto de mejorar el clima de inversión y facilitar el cumplimiento de obligaciones tributarias, Ley Nº 29566 (28.07.10). Arts. 5 y 6.",
        "requisitos": [
            "1 FUE por triplicado, debidamente suscrito.",
            "2 Documentación que acredite que cuenta con derecho a edificar y represente al titular, en caso que el solicitante de la licencia de edificación no sea el propietario del predio.",
            "3 Si el solicitante es una persona jurídica se acompañará la respectiva constitución de la empresa y copia literal del poder expedidos por el Registro de Personas Jurídicas, vigente al momento de presentación de los documentos.",
            "4 Declaración Jurada de habilitación de los profesionales que suscriben la documentación técnica",
            "5 Firma del solicitante y de los profesionales responsables del proyecto, en los planos presentados para todos los trámites.",
            "6 Certificados de Factibilidad de Servicios, para Obra Nueva de vivienda Multifamiliar o ampliación de Vivienda Unifamiliar a Multifamiliar o fines diferentes al de vivienda.",
            "7 Documentación técnica, por duplicado, la misma que estará compuesta por:\n- Plano de ubicación y localización según formato.\n- Planos de Arquitectura, Estructuras, Instalaciones Sanitarias, Eléctricas y otras, de ser el caso, firmados y sellados por los profesionales responsables del proyecto y por el propietario, acompañando las memorias justificativas por especialidad.\n- De ser el caso, plano de sostenimiento de excavaciones de acuerdo con lo establecido en el art. 33 de la Norma E 050 del RNE acompañado de la memoria descriptiva que precise las características de la obra, además de las edificaciones colindantes indicando el número de pisos y sótanos, complementando con fotos.\n- Estudio de Mecánica de Suelos, según los casos que establece el RNE.",
            "8 Póliza CAR (Todo Riesgo Contratista) o la Póliza de Responsabilidad Civil, para las edificaciones multifamiliares y condominios de vivienda unifamiliar o multifamiliar, contemplados en los literales a) y c) del numeral 42.2 del artículo 42 del Decreto Supremo Nº 024-2008-VIVIENDA, con una cobertura por daños materiales y personales a terceros y como complemento al Seguro Complementario de Trabajo de Riesgo previsto en la Ley Nº 26790, Ley de Modernización de la Seguridad Social en Salud.\nLa Póliza debe estar vigente durante todo el periodo de ejecución de la obra y es exigida por la Municipalidad el día previo al inicio de los trabajos.",
            "9 Estudios de Impacto ambiental y vial en los casos que se requiera.",
            "10 El Dictamen Conforme del Anteproyecto con los planos respectivos, según corresponda.",
            "11 En caso de proyectos de gran magnitud, los planos podrán ser presentados en secciones con escala conveniente que permita su fácil lectura, conjuntamente con el plano del proyecto integral.",
            "12 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "11.7421% UIT",
        "plazo": "Evaluación Previa - 25 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Desarrollo Urbano y Territorial",
        "reconsideracion": "Gerente de Desarrollo Urbano y Territorial\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente Municipal\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
{
        "id": "96",
        "numero": "82.3",
        "procedimiento": "LICENCIA DE EDIFICACIÓN: MODALIDAD C (APROBACIÓN CON EVALUACIÓN PREVIA DEL PROYECTO POR LA COMISIÓN TÉCNICA) - LAS EDIFICACIONES DE USO MIXTO CON VIVIENDA",
        "sustento": "BASE LEGAL\n- Ley de Regulación de Habilitaciones Urbanas y de Edificaciones, Ley Nº 29090 y modificatorias (25.09.07). Arts. 10, 25 y 31.\n- Reglamento de Licencias de Habilitación Urbana y Licencias de Edificación, Decreto Supremo Nº 024-2008-VIVIENDA y modificatorias (27.09.08). Arts. 42, 47, 51 y 54\n- Ley que modifica diversas disposiciones con el objeto de mejorar el clima de inversión y facilitar el cumplimiento de obligaciones tributarias, Ley Nº 29566 (28.07.10). Arts. 5 y 6.",
        "requisitos": [
            "1 FUE por triplicado, debidamente suscrito.",
            "2 Documentación que acredite que cuenta con derecho a edificar y represente al titular, en caso que el solicitante de la licencia de edificación no sea el propietario del predio.",
            "3 Si el solicitante es una persona jurídica se acompañará la respectiva constitución de la empresa y copia literal del poder expedidos por el Registro de Personas Jurídicas, vigente al momento de presentación de los documentos.",
            "4 Declaración Jurada de habilitación de los profesionales que suscriben la documentación técnica",
            "5 Firma del solicitante y de los profesionales responsables del proyecto, en los planos presentados para todos los trámites.",
            "6 Certificados de Factibilidad de Servicios, para Obra Nueva de vivienda Multifamiliar o ampliación de Vivienda Unifamiliar a Multifamiliar o fines diferentes al de vivienda.",
            "7 Documentación técnica, por duplicado, la misma que estará compuesta por:\n- Plano de ubicación y localización según formato.\n- Planos de Arquitectura, Estructuras, Instalaciones Sanitarias, Eléctricas y otras, de ser el caso, firmados y sellados por los profesionales responsables del proyecto y por el propietario, acompañando las memorias justificativas por especialidad.\n- De ser el caso, plano de sostenimiento de excavaciones de acuerdo con lo establecido en el art. 33 de la Norma E 050 del RNE acompañado de la memoria descriptiva que precise las características de la obra, además de las edificaciones colindantes indicando el número de pisos y sótanos, complementando con fotos.\n- Estudio de Mecánica de Suelos, según los casos que establece el RNE.",
            "8 Póliza CAR (Todo Riesgo Contratista) o la Póliza de Responsabilidad Civil, para las edificaciones multifamiliares y condominios de vivienda unifamiliar o multifamiliar, contemplados en los literales a) y c) del numeral 42.2 del artículo 42 del Decreto Supremo Nº 024-2008-VIVIENDA, con una cobertura por daños materiales y personales a terceros y como complemento al Seguro Complementario de Trabajo de Riesgo previsto en la Ley Nº 26790, Ley de Modernización de la Seguridad Social en Salud.\nLa Póliza debe estar vigente durante todo el periodo de ejecución de la obra y es exigida por la Municipalidad el día previo al inicio de los trabajos.",
            "9 Estudios de Impacto ambiental y vial en los casos que se requiera.",
            "10 El Dictamen Conforme del Anteproyecto con los planos respectivos, según corresponda.",
            "11 En caso de proyectos de gran magnitud, los planos podrán ser presentados en secciones con escala conveniente que permita su fácil lectura, conjuntamente con el plano del proyecto integral.",
            "12 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "4.5737% UIT",
        "plazo": "Evaluación Previa - 25 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Desarrollo Urbano y Territorial",
        "reconsideracion": "Gerente de Desarrollo Urbano y Territorial\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente Municipal\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
{
        "id": "97",
        "numero": "82.4",
        "procedimiento": "LICENCIA DE EDIFICACIÓN: MODALIDAD C (APROBACIÓN CON EVALUACIÓN PREVIA DEL PROYECTO POR LA COMISIÓN TÉCNICA) - LAS INTERVENCIONES QUE SE DESARROLLEN EN BIENES CULTURALES INMUEBLES PREVIAMENTE DECLARADOS.",
        "sustento": "BASE LEGAL\n- Ley de Regulación de Habilitaciones Urbanas y de Edificaciones, Ley Nº 29090 y modificatorias (25.09.07). Arts. 10, 25 y 31.\n- Reglamento de Licencias de Habilitación Urbana y Licencias de Edificación, Decreto Supremo Nº 024-2008-VIVIENDA y modificatorias (27.09.08). Arts. 42, 47, 51 y 54\n- Ley que modifica diversas disposiciones con el objeto de mejorar el clima de inversión y facilitar el cumplimiento de obligaciones tributarias, Ley Nº 29566 (28.07.10). Arts. 5 y 6.",
        "requisitos": [
            "1 FUE por triplicado, debidamente suscrito.",
            "2 Documentación que acredite que cuenta con derecho a edificar y represente al titular, en caso que el solicitante de la licencia de edificación no sea el propietario del predio.",
            "3 Si el solicitante es una persona jurídica se acompañará la respectiva constitución de la empresa y copia literal del poder expedidos por el Registro de Personas Jurídicas, vigente al momento de presentación de los documentos.",
            "4 Declaración Jurada de habilitación de los profesionales que suscriben la documentación técnica",
            "5 Firma del solicitante y de los profesionales responsables del proyecto, en los planos presentados para todos los trámites.",
            "6 Certificados de Factibilidad de Servicios, para Obra Nueva de vivienda Multifamiliar o ampliación de Vivienda Unifamiliar a Multifamiliar o fines diferentes al de vivienda.",
            "7 Documentación técnica, por duplicado, la misma que estará compuesta por:\n- Plano de ubicación y localización según formato.\n- Planos de Arquitectura, Estructuras, Instalaciones Sanitarias, Eléctricas y otras, de ser el caso, firmados y sellados por los profesionales responsables del proyecto y por el propietario, acompañando las memorias justificativas por especialidad.\n- De ser el caso, plano de sostenimiento de excavaciones de acuerdo con lo establecido en el art. 33 de la Norma E 050 del RNE acompañado de la memoria descriptiva que precise las características de la obra, además de las edificaciones colindantes indicando el número de pisos y sótanos, complementando con fotos.\n- Estudio de Mecánica de Suelos, según los casos que establece el RNE.",
            "8 Póliza CAR (Todo Riesgo Contratista) o la Póliza de Responsabilidad Civil, para las edificaciones multifamiliares y condominios de vivienda unifamiliar o multifamiliar, contemplados en los literales a) y c) del numeral 42.2 del artículo 42 del Decreto Supremo Nº 024-2008-VIVIENDA, con una cobertura por daños materiales y personales a terceros y como complemento al Seguro Complementario de Trabajo de Riesgo previsto en la Ley Nº 26790, Ley de Modernización de la Seguridad Social en Salud\nLa Póliza debe estar vigente durante todo el periodo de ejecución de la obra y es exigida por la Municipalidad el día previo al inicio de los trabajos.",
            "9 Estudios de Impacto ambiental y vial en los casos que se requiera.",
            "10 El Dictamen Conforme del Anteproyecto con los planos respectivos, según corresponda.",
            "11 En caso de proyectos de gran magnitud, los planos podrán ser presentados en secciones con escala conveniente que permita su fácil lectura, conjuntamente con el plano del proyecto integral.",
            "12 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "13.9684% UIT",
        "plazo": "Evaluación Previa - 25 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Desarrollo Urbano y Territorial",
        "reconsideracion": "Gerente de Desarrollo Urbano y Territorial\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente Municipal\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
{
        "id": "98",
        "numero": "82.5",
        "procedimiento": "LICENCIA DE EDIFICACIÓN: MODALIDAD C (APROBACIÓN CON EVALUACIÓN PREVIA DEL PROYECTO POR LA COMISIÓN TÉCNICA) - LAS EDIFICACIONES PARA LOCALES COMERCIALES, CULTURALES, CENTROS DE DIVERSIÓN Y SALAS DE ESPECTÁCULOS, QUE INDIVIDUALMENTE O EN CONJUNTO CUENTEN CON UN MÁXIMO DE 30,000 M2 DE ÁREA CONSTRUIDA.",
        "sustento": "BASE LEGAL\n- Ley de Regulación de Habilitaciones Urbanas y de Edificaciones, Ley Nº 29090 y modificatorias (25.09.07). Arts. 10, 25 y 31.\n- Reglamento de Licencias de Habilitación Urbana y Licencias de Edificación, Decreto Supremo Nº 024-2008-VIVIENDA y modificatorias (27.09.08). Arts. 42, 47, 51 y 54\n- Ley que modifica diversas disposiciones con el objeto de mejorar el clima de inversión y facilitar el cumplimiento de obligaciones tributarias, Ley Nº 29566 (28.07.10). Arts. 5 y 6.",
        "requisitos": [
            "1 FUE por triplicado, debidamente suscrito.",
            "2 Documentación que acredite que cuenta con derecho a edificar y represente al titular, en caso que el solicitante de la licencia de edificación no sea el propietario del predio.",
            "3 Si el solicitante es una persona jurídica se acompañará la respectiva constitución de la empresa y copia literal del poder expedidos por el Registro de Personas Jurídicas, vigente al momento de presentación de los documentos.",
            "4 Declaración Jurada de habilitación de los profesionales que suscriben la documentación técnica",
            "5 Firma del solicitante y de los profesionales responsables del proyecto, en los planos presentados para todos los trámites.",
            "6 Certificados de Factibilidad de Servicios, para Obra Nueva de vivienda Multifamiliar o ampliación de Vivienda Unifamiliar a Multifamiliar o fines diferentes al de vivienda.",
            "7 Documentación técnica, por duplicado, la misma que estará compuesta por:\n- Plano de ubicación y localización según formato.\n- Planos de Arquitectura, Estructuras, Instalaciones Sanitarias, Eléctricas y otras, de ser el caso, firmados y sellados por los profesionales responsables del proyecto y por el propietario, acompañando las memorias justificativas por especialidad.\n- De ser el caso, plano de sostenimiento de excavaciones de acuerdo con lo establecido en el artículo 33 de la Norma E 050 del RNE acompañado de la memoria descriptiva que precise las características de la obra, además de las edificaciones colindantes indicando el número de pisos y sótanos, complementando con fotos.\n- Estudio de Mecánica de Suelos, según los casos que establece el RNE.",
            "8 Póliza CAR (Todo Riesgo Contratista) o la Póliza de Responsabilidad Civil, para las edificaciones multifamiliares y condominios de vivienda unifamiliar o multifamiliar, contemplados en los literales a) y c) del numeral 42.2 del artículo 42 del Decreto Supremo Nº 024-2008-VIVIENDA, con una cobertura por daños materiales y personales a terceros y como complemento al Seguro Complementario de Trabajo de Riesgo previsto en la Ley Nº 26790, Ley de Modernización de la Seguridad  Social en Salud.\nLa Póliza debe estar vigente durante todo el periodo de ejecución de la obra y es exigida por la Municipalidad el día previo al inicio de los trabajos.",
            "9 Estudios de Impacto ambiental y vial en los casos que se requiera.",
            "10 El Dictamen Conforme del Anteproyecto con los planos respectivos, según corresponda.",
            "11 En caso de proyectos de gran magnitud, los planos podrán ser presentados en secciones con escala conveniente que permita su fácil lectura, conjuntamente con el plano del proyecto integral.",
            "12 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "11.7421% UIT",
        "plazo": "Evaluación Previa - 25 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Desarrollo Urbano y Territorial",
        "reconsideracion": "Gerente de Desarrollo Urbano y Territorial\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente Municipal\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
{
        "id": "99",
        "numero": "82.6",
        "procedimiento": "LICENCIA DE EDIFICACIÓN: MODALIDAD C (APROBACIÓN CON EVALUACIÓN PREVIA DEL PROYECTO POR LA COMISIÓN TÉCNICA) - LAS EDIFICACIONES PARA MERCADOS QUE CUENTEN CON UN MÁXIMO DE 15,000 M2 DE ÁREA CONSTRUIDA.",
        "sustento": "BASE LEGAL\n- Ley de Regulación de Habilitaciones Urbanas y de Edificaciones, Ley Nº 29090 y modificatorias (25.09.07). Arts. 10, 25 y 31.\n- Reglamento de Licencias de Habilitación Urbana y Licencias de Edificación, Decreto Supremo Nº 024-2008-VIVIENDA y modificatorias (27.09.08). Arts. 42, 47, 51 y 54.\n- Ley que modifica diversas disposiciones con el objeto de mejorar el clima de inversión y facilitar el cumplimiento de obligaciones tributarias, Ley Nº 29566 (28.07.10). Arts. 5 y 6.",
        "requisitos": [
            "1 FUE por triplicado, debidamente suscrito.",
            "2 Documentación que acredite que cuenta con derecho a edificar y represente al titular, en caso que el solicitante de la licencia de edificación no sea el propietario del predio.",
            "3 Si el solicitante es una persona jurídica se acompañará la respectiva constitución de la empresa y copia literal del poder expedidos por el Registro de Personas Jurídicas, vigente al momento de presentación de los documentos.",
            "4 Declaración Jurada de habilitación de los profesionales que suscriben la documentación técnica.",
            "5 Firma del solicitante y de los profesionales responsables del proyecto, en los planos presentados para todos los trámites.",
            "6 Certificados de Factibilidad de Servicios, para Obra Nueva de vivienda Multifamiliar o ampliación de Vivienda Unifamiliar a Multifamiliar o fines diferentes al de vivienda.",
            "7 Documentación técnica, por duplicado, la misma que estará compuesta por:\n- Plano de ubicación y localización según formato.\n- Planos de Arquitectura, Estructuras, Instalaciones Sanitarias, Eléctricas y otras, de ser el caso, firmados y sellados por los profesionales responsables del proyecto y por el propietario, acompañando las memorias justificativas por especialidad.\n- De ser el caso, plano de sostenimiento de excavaciones de acuerdo con lo establecido en el artículo 33 de la Norma E 050 del RNE acompañado de la memoria descriptiva que precise las características de la obra, además de las edificaciones colindantes indicando el número de pisos y sótanos, complementando con fotos.\n- Estudio de Mecánica de Suelos, según los casos que establece el RNE.",
            "8 Póliza CAR (Todo Riesgo Contratista) o la Póliza de Responsabilidad Civil, para las edificaciones multifamiliares y condominios de vivienda unifamiliar o multifamiliar, contemplados en los literales a) y c) del numeral 42.2 del artículo 42 del Decreto Supremo Nº 024-2008-VIVIENDA, con una cobertura por daños materiales y personales a terceros y como complemento al Seguro Complementario de Trabajo de Riesgo previsto en la Ley Nº 26790, Ley de Modernización de la Seguridad Social en Salud.\nLa Póliza debe estar vigente durante todo el periodo de ejecución de la obra y es exigida por la Municipalidad el día previo al inicio de los trabajos.",
            "9 Estudios de Impacto ambiental y vial en los casos que se requiera.",
            "10 El Dictamen Conforme del Anteproyecto con los planos respectivos, según corresponda.",
            "11 En caso de proyectos de gran magnitud, los planos podrán ser presentados en secciones con escala conveniente que permita su fácil lectura, conjuntamente con el plano del proyecto integral.",
            "12 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "11.7421% UIT",
        "plazo": "Evaluación Previa - 25 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Desarrollo Urbano y Territorial",
        "reconsideracion": "Gerente de Desarrollo Urbano y Territorial\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente Municipal\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
{
        "id": "100",
        "numero": "82.7",
        "procedimiento": "LICENCIA DE EDIFICACIÓN: MODALIDAD C (APROBACIÓN CON EVALUACIÓN PREVIA DEL PROYECTO POR LA COMISIÓN TÉCNICA) - LOCALES PARA ESPECTÁCULOS DEPORTIVOS DE HASTA 20,000 OCUPANTES.",
        "sustento": "BASE LEGAL\n- Ley de Regulación de Habilitaciones Urbanas y de Edificaciones, Ley Nº 29090 y modificatorias (25.09.07). Arts. 10, 25 y 31.\n- Reglamento de Licencias de Habilitación Urbana y Licencias de Edificación, Decreto Supremo Nº 024-2008-VIVIENDA y modificatorias (27.09.08). Arts. 42, 47, 51 y 54\n- Ley que modifica diversas disposiciones con el objeto de mejorar el clima de inversión y facilitar el cumplimiento de obligaciones tributarias, Ley Nº 29566 (28.07.10). Arts. 5 y 6.",
        "requisitos": [
            "1 FUE por triplicado, debidamente suscrito.",
            "2 Documentación que acredite que cuenta con derecho a edificar y represente al titular, en caso que el solicitante de la licencia de edificación no sea el propietario del predio.",
            "3 Si el solicitante es una persona jurídica se acompañará la respectiva constitución de la empresa y copia literal del poder expedidos por el Registro de Personas Jurídicas, vigente al momento de presentación de los documentos.",
            "4 Declaración Jurada de habilitación de los profesionales que suscriben la documentación técnica",
            "5 Firma del solicitante y de los profesionales responsables del proyecto, en los planos presentados para todos los trámites.",
            "6 Certificados de Factibilidad de Servicios, para Obra Nueva de vivienda Multifamiliar o ampliación de Vivienda Unifamiliar a Multifamiliar o fines diferentes al de vivienda.",
            "7 Documentación técnica, por duplicado, la misma que estará compuesta por:\n- Plano de ubicación y localización según formato.\n- Planos de Arquitectura, Estructuras, Instalaciones Sanitarias, Eléctricas y otras, de ser el caso, firmados y sellados por los profesionales responsables del proyecto y por el propietario, acompañando las memorias justificativas por especialidad.\n- De ser el caso, plano de sostenimiento de excavaciones de acuerdo con lo establecido en el artículo 33 de la Norma E 050 del RNE acompañado de la memoria descriptiva que precise las características de la obra, además de las edificaciones colindantes indicando el número de pisos y sótanos, complementando con fotos.\n- Estudio de Mecánica de Suelos, según los casos que establece el RNE.",
            "8 Póliza CAR (Todo Riesgo Contratista) o la Póliza de Responsabilidad Civil, para las edificaciones multifamiliares y condominios de vivienda unifamiliar o multifamiliar, contemplados en los literales a) y c) del numeral 42.2 del artículo 42 del Decreto Supremo Nº 024-2008-VIVIENDA, con una cobertura por daños materiales y cobertura por daños materiales y personales a terceros y como complemento al Seguro Complementario de Trabajo de Riesgo previsto en la Ley Nº 26790, Ley de Modernización de la Seguridad Social en Salud.\nLa Póliza debe estar vigente durante todo el periodo de ejecución de la obra y es exigida por la Municipalidad el día previo al inicio de los trabajos.",
            "9 Estudios de Impacto ambiental y vial en los casos Estudios de Impacto ambiental y vial en los casos que se requiera.",
            "10 El Dictamen Conforme del Anteproyecto con los planos respectivos, según corresponda.",
            "11 En caso de proyectos de gran magnitud, los planos podrán ser presentados en secciones con escala conveniente que permita su fácil lectura conjuntamente con el plano del proyecto integral.",
            "12 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "11.7421% UIT",
        "plazo": "Evaluación Previa - 25 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Desarrollo Urbano y Territorial",
        "reconsideracion": "Gerente de Desarrollo Urbano y Territorial\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente Municipal\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
{
        "id": "101",
        "numero": "82.8",
        "procedimiento": "LICENCIA DE EDIFICACIÓN: MODALIDAD C (APROBACIÓN CON EVALUACIÓN PREVIA DEL PROYECTO POR LA COMISIÓN TÉCNICA) - EN CASO DE REMODELACIÓN, AMPLIACIÓN O PUESTA EN VALOR HISTÓRICO",
        "sustento": "BASE LEGAL\n- Ley de Regulación de Habilitaciones Urbanas y de Edificaciones, Ley Nº 29090 y modificatorias (25.09.07). Arts. 10, 25 y 31.\n- Reglamento de Licencias de Habilitación Urbana y Licencias de Edificación, Decreto Supremo Nº 024-2008-VIVIENDA y modificatorias (27.09.08). Arts. 42, 47, 51 y 54.\n- Ley que modifica diversas disposiciones con el objeto de mejorar el clima de inversión y facilitar el cumplimiento de obligaciones tributarias, Ley Nº 29566 (28.07.10). Arts. 5 y 6.",
        "requisitos": [
            "1 FUE por triplicado, debidamente suscrito.",
            "2 Documentación que acredite que cuenta con derecho a edificar y represente al titular, en caso que el solicitante de la licencia de edificación no sea el propietario del predio.",
            "3 Si el solicitante es una persona jurídica se acompañará la respectiva constitución de la empresa y copia literal del poder expedidos por el Registro de Personas Jurídicas, vigente al momento de presentación de los documentos.",
            "4 Declaración Jurada de habilitación de los profesionales que suscriben la documentación técnica",
            "5 Para los casos de remodelaciones y ampliaciones, se presentará la copia literal de la inscripción de la declaratoria de edificación y/o fábrica junto con los planos respectivos. De haber sido emitidos por otra entidad, copia de la Licencia y/o Conformidad o Finalización de Obra con los planos correspondientes.",
            "6 Firma del solicitante y de los profesionales responsables del proyecto, en los planos presentados para todos los trámites.",
            "7 Certificados de Factibilidad de Servicios, para Obra Nueva de vivienda Multifamiliar o ampliación de Vivienda Unifamiliar a Multifamiliar o fines diferentes al de vivienda.",
            "8 Documentación técnica, por duplicado, la misma que estará compuesta por:\n- Plano de ubicación y localización según formato.\n- Planos de Instalaciones Sanitarias , Eléctricas y otras, de ser el caso, firmados y sellados por los profesionales responsables del proyecto y por el propietario, acompañando las memorias justificativas por especialidad.\n- De ser el caso, plano de sostenimiento de excavaciones de acuerdo con lo establecido en el artículo 33 de la Norma E 050 del RNE acompañado de la memoria descriptiva que precise las características de la obra, además de las edificaciones colindantes indicando el número de pisos y sótanos, complementando con fotos.\n- Estudio de Mecánica de Suelos, según los casos que establece el RNE.",
            "9 Póliza CAR (Todo Riesgo Contratista) o la Póliza de Responsabilidad Civil, para las edificaciones multifamiliares y condominios de vivienda unifamiliar o multifamiliar, contemplados en los literales a) y c) del numeral 42.2 del artículo 42 del Decreto Supremo Nº 024-2008-VIVIENDA, con una cobertura por daños materiales y personales a terceros y como complemento al Seguro Complementario de Trabajo de Riesgo previsto en la Ley Nº 26790, Ley de Modernización de la Seguridad Social en Salud.\nLa Póliza debe estar vigente durante todo el periodo de ejecución de la obra y es exigida por la Municipalidad el día previo al inicio de los trabajos.",
            "10 Estudios de Impacto ambiental y vial en los casos que se requiera.",
            "11 El Dictamen Conforme del Anteproyecto con los planos respectivos, según corresponda.",
            "12 En caso de proyectos de gran magnitud, los planos podrán ser presentados en secciones con escala conveniente que permita su fácil lectura, conjuntamente con el plano del proyecto integral.",
            "13 Declaración Jurada de inscripción de declaratoria de fábrica o edificación, en su defecto, el Certificado de Conformidad o Finalización de Obra, o la Licencia de Obra o de Construcción de la edificación existente, expedida con una anticipación no mayor a treinta (30) Días hábiles.",
            "14 Planos de planta, de arquitectura diferenciados con su memoria descriptiva, de acuerdo a lo siguiente:\n- Levantamiento de la fábrica o edificación existente graficandose con achurado a 45 los elementos a eliminar\n- Fábrica o edificación resultante, graficandose con achurado a 45, perpendicular al anterior los elementos a edificar.\n- Para las obras de Puesta en Valor Histórico, se deberá graficar en los planos los elementos arquitectonicos con valor historico monumental propios de la edificación, identificandolos claramente y diferenciandose aquellos que seran objeto de restauración, reconstrucción o conservación, en su caso.",
            "15 Planos de estructura acompañados de memoria justificativa; obligatorio en los casos de remodelación, ampliación o reparación y cuando sea necesario en los demas tipos de obra.\nEn cualquier caso, se diferenciaran claramente los elementos estructurales existentes, los que se eliminarán y los nuevos, y se detallarán adecuadamente los empalmes.",
            "16 Planos de instalaciones, cuando sea necesario acompañados de memoria justificativa, en cuyo caso:\n- Se diferenciarán claramente los puntos y salidas existentes, los que se eliminarán y los nuevos, detallando adecuadamente los empalmes.\n- Se evaluará la factibilidad de servicios teniendo en cuenta la ampliación de cargas de electricidad y de dotación de agua.",
            "17 Autorización de la Junta de Propietarios para proyectos en inmuebles sujetos al Regimen de Unidades Inmobiliarias de Propiedad Exclusiva y de propiedad comun.",
            "18 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "14.0026% UIT",
        "plazo": "Evaluación Previa - 25 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Desarrollo Urbano y Territorial",
        "reconsideracion": "Gerente de Desarrollo Urbano y Territorial\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente Municipal\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
{
        "id": "102",
        "numero": "82.9",
        "procedimiento": "LICENCIA DE EDIFICACIÓN: MODALIDAD C (APROBACIÓN CON EVALUACIÓN PREVIA DEL PROYECTO POR LA COMISIÓN TÉCNICA) - EN CASO SE SOLICITE LA LICENCIA DE ALGÚN TIPO DE DEMOLICIÓN NO CONTEMPLADO EN LA MODALIDAD A O B",
        "sustento": "BASE LEGAL\n- Ley de Regulación de Habilitaciones Urbanas y de Edificaciones, Ley Nº 29090 y modificatorias (25.09.07). Arts. 10, 25 y 31.\n- Reglamento de Licencias de Habilitación Urbana y Licencias de Edificación, Decreto Supremo Nº 024-2008-VIVIENDA y modificatorias (27.09.08). Arts. 42, 47, 51 y 54.\n- Ley que modifica diversas disposiciones con el objeto de mejorar el clima de inversión y facilitar el cumplimiento de obligaciones tributarias, Ley Nº 29566 (28.07.10). Arts. 5 y 6.",
        "requisitos": [
            "1 FUE por triplicado, debidamente suscrito.",
            "2 Documentación que acredite que cuenta conderecho a edificar y represente al titular, en caso que que el solicitante de la licencia de edificación no sea el propietario del predio.",
            "3 Si el solicitante es una persona jurídica se acompañará la respectiva constitución de la empresa y copia literal del poder expedidos por el Registro de Personas Jurídicas, vigente al momento de presentación de los documentos.",
            "4 Declaración Jurada de habilitación de los profesionales que suscriben la documentación técnica",
            "5 Copia literal de la inscripción de la declaratoria de edificación y/o fábrica junto con los planos respectivos. De haber sido emitidos por otra entidad, copia de la Licencia y/o Conformidad o Finalizaciónde Obra con los planos correspondientes.",
            "6 Firma del solicitante y de los profesionales Firma del solicitante y de los profesionales responsables del proyecto, en los planos presentados para todos los trámites",
            "7 En el caso que la edificación no se encuentre inscrita en el Registro de Predios, se deberá presentar Licencia de Construcción o de Obra Conformidad de Obra o Declaratoria de Fábrica o de Edificación, con los planos correspondientes.",
            "8 Plano de Localización y Ubicación.",
            "9 Planos de Planta a escala 1/75, dimensionados adecuadamente, en el que se delineará las zonas de la fábrica o edificación a demoler, así como del perfil y alturas de los inmuebles colindantes a las zonas de la fábrica o edificación a demoler hasta una distancia de 1.50 m de los límites de propiedad.",
            "10 Plano de cerramiento del predio, cuando se trate de demolición total.",
            "11 En el caso de uso de explosivos, autorizaciones de las autoridades competentes (DISCAMEC, Comando Conjunto de las Fuerzas Armadas y Defensa Civil), Póliza Car (Todo Riesgo Contratista) o Póliza de Responsabilidad Civil y copia del cargo de carta a los propietarios y/o ocupantes de las edificaciones colindantes, comunicándoles las fechas y horas en que se efectuarán las detonaciones",
            "12 Para los casos de demoliciones, parciales o totales cuya fábrica no se encuentra inscrita Licencia y/o Conformidad o Finalización de obras, plano de ubicación y localización, y plano de planta del levantamiento de edificación, sin perjuicio de las sanciones que la Municipalidad considere",
            "13 En el caso de demoliciones totales inscritas en el Registro de Predios, se acreditará que sobre el bien no recaigan cargas y/o gravámenes, en su defecto, se acreditará la autorización del titular de la carga o gravámen.",
            "14 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "5.3553% UIT",
        "plazo": "Evaluación Previa - 25 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Desarrollo Urbano y Territorial",
        "reconsideracion": "Gerente de Desarrollo Urbano y Territorial\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente Municipal\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
{
        "id": "103",
        "numero": "83.1",
        "procedimiento": "LICENCIA DE EDIFICACIÓN: MODALIDAD D (APROBACIÓN CON EVALUACIÓN PREVIA DEL PROYECTO POR LA COMISIÓN TÉCNICA) - EDIFICACIONES PARA FINES DE INDUSTRIA.",
        "sustento": "BASE LEGAL\nLey de Regulación de Habilitaciones Urbanas y de Edificaciones, Ley Nº 29090 y modificatorias (25.09.07). Arts. 10, 25 y 31.\nReglamento de Licencias de Habilitación Urbana y Licencias de Edificación, Decreto Supremo Nº 024-2008-VIVIENDA y modificatorias (27.09.08). Arts. 42, 47, 51 y 54\nLey que modifica diversas disposiciones con el objeto de mejorar el clima de inversión y facilitar el cumplimiento de obligaciones tributarias, Ley Nº 29566 (28.07.10). Arts. 5 y 6.",
        "requisitos": [
            "1 FUE por triplicado, debidamente suscrito.",
            "2 Documentación que acredite que cuenta con derecho a edificar y represente al titular, en caso que el solicitante de la licencia de edificación no sea el propietario del predio.",
            "3 Si el solicitante es una persona jurídica se acompañará la respectiva constitución de la empresa y copia literal del poder expedidos por el Registro de Personas Jurídicas, vigente al momento de presentación de los documentos.",
            "4 Declaración Jurada de habilitación de los profesionales que suscriben la documentación técnica",
            "5 Firma del solicitante y de los profesionales responsables del proyecto, en los planos presentados para todos los trámites.",
            "6 Certificados de Factibilidad de Servicios, para Obra Nueva de vivienda Multifamiliar o ampliación de Vivienda Unifamiliar a Multifamiliar o fines diferentes al de vivienda.",
            "7 Documentación técnica, por duplicado, la misma que estará compuesta por:\n- Plano de ubicación y localización según formato.\n- Planos de Arquitectura, Estructuras, Instalaciones Sanitarias, Eléctricas y otras, de ser el caso, firmados y sellados por los profesionales responsables del proyecto y por el propietario, acompañando las memorias justificativas por especialidad.\n- De ser el caso, plano de sostenimiento de excavaciones de acuerdo con lo establecido en artículo 33 de la Norma E 050 del RNE acompañado de la memoria descriptiva que precise las características de la obra, además de las edificaciones colindantes indicando el número de pisos y sótanos, complementando con fotos.\n- Estudio de Mecánica de Suelos, según los casos que establece el RNE.",
            "8 Póliza CAR (Todo Riesgo Contratista) o la Póliza de Responsabilidad Civil, para las edificaciones multifamiliares y condominios de vivienda unifamiliar o multifamiliar, contemplados en los literales a) y c) del numeral 42.2 del artículo 42 del Decreto Supremo Nº 024-2008-VIVIENDA, con una cobertura por daños materiales y personales a terceros y como complemento al Seguro Complementario de Trabajo de Riesgo previsto en la Ley Nº 26790, Ley de Modernización de la Seguridad Social en Salud.\nLa Póliza debe estar vigente durante todo el periodo de ejecución de la obra y es exigida por la Municipalidad el día previo al inicio de los trabajos.",
            "9 Estudios de Impacto ambiental y vial en los casos que se requiera.",
            "10 El Dictamen Conforme del Anteproyecto con los planos respectivos, según corresponda.",
            "11 En caso de proyectos de gran magnitud, los planos podrán ser presentados en secciones con escala conveniente que permita su fácil lectura, conjuntamente con el plano del proyecto integral.",
            "12 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "14.0868% UIT",
        "plazo": "Evaluación Previa - 25 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Desarrollo Urbano y Territorial",
        "reconsideracion": "Gerente de Desarrollo Urbano y Territorial\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente Municipal\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
{
        "id": "104",
        "numero": "83.2",
        "procedimiento": "LICENCIA DE EDIFICACIÓN: MODALIDAD D (APROBACIÓN CON EVALUACIÓN PREVIA DEL PROYECTO POR LA COMISIÓN TÉCNICA) - LAS EDIFICACIONES PARA FINES EDUCATIVOS, SALUD, HOSPEDAJE, ESTABLECIMIENTOS DE EXPENDIO DE COMBUSTIBLE Y TERMINALES DE TRANSPORTE",
        "sustento": "BASE LEGAL\nLey de Regulación de Habilitaciones Urbanas y de Edificaciones, Ley Nº 29090 y modificatorias (25.09.07). Arts. 10, 25 y 31.\nReglamento de Licencias de Habilitación Urbana y Licencias de Edificación, Decreto Supremo Nº 024-2008-VIVIENDA y modificatorias (27.09.08). Arts. 42, 47, 51 y 54\nLey que modifica diversas disposiciones con el objeto de mejorar el clima de inversión y facilitar el cumplimiento de obligaciones tributarias, Ley Nº 29566 (28.07.10). Arts. 5 y 6.",
        "requisitos": [
            "1 FUE por triplicado, debidamente suscrito.",
            "2 Documentación que acredite que cuenta con derecho a edificar y represente al titular, en caso que el solicitante de la licencia de edificación no sea el propietario del predio.",
            "3 Si el solicitante es una persona jurídica se acompañará la respectiva constitución de la empresa y copia literal del poder expedidos por el Registro de Personas Jurídicas, vigente al momento de presentación de los documentos.",
            "4 Declaración Jurada de habilitación de los profesionales que suscriben la documentación técnica",
            "5 Firma del solicitante y de los profesionales responsables del proyecto, en los planos presentados para todos los trámites.",
            "6 Certificados de Factibilidad de Servicios, para Obra Nueva de vivienda vivienda Multifamiliar o ampliación de Vivienda Unifamiliar a Multifamiliar o fines diferentes al de vivienda.",
            "7 Documentación técnica, por duplicado, la misma que estará compuesta por:\n- Plano de ubicación y localización según formato.\n- Planos de Arquitectura, Estructuras, Instalaciones Sanitarias, Eléctricas y otras, de ser el caso, firmados y sellados por los profesionales responsables del proyecto y por el propietario, acompañando las memorias justificativas por especialidad.\n- De ser el caso, plano de sostenimiento de excavaciones de acuerdo con lo establecido en el artículo 33 de la Norma E 050 del RNE acompañado de la memoria descriptiva que precise las características de la obra, además de las edificaciones colindantes indicando el número de pisos y sótanos, complementando con fotos.\n- Estudio de Mecánica de Suelos, según los casos que establece el RNE.",
            "8 Póliza CAR (Todo Riesgo Contratista) o la Póliza de Responsabilidad Civil, para las edificaciones multifamiliares y condominios de vivienda unifamiliar o multifamiliar, contemplados en los literales a) y c) del numeral 42.2 del artículo 42 del Decreto Supremo Nº 024-2008-VIVIENDA, con una cobertura por daños materiales y personales a terceros y como complemento al Seguro Complementario de Trabajo de Riesgo previsto en la Ley Nº 26790, Ley de Modernización de la Seguridad Social en Salud.\nLa Póliza debe estar vigente durante todo el periodo de ejecución de la obra y es exigida por la Municipalidad el día previo al inicio de los trabajos.",
            "9 Estudios de Impacto ambiental y vial en los casos que se requiera.",
            "10 El Dictamen Conforme del Anteproyecto con los planos respectivos, según corresponda.",
            "11 En caso de proyectos de gran magnitud, los planos podrán ser presentados en secciones con escala conveniente que permita su fácil lectura, conjuntamente con el plano del proyecto integral.",
            "12 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "14.0026% UIT",
        "plazo": "Evaluación Previa - 25 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Desarrollo Urbano y Territorial",
        "reconsideracion": "Gerente de Desarrollo Urbano y Territorial\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente Municipal\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
{
        "id": "105",
        "numero": "84",
        "procedimiento": "CONFORMIDAD DE OBRA Y DECLARATORIA DE EDIFICACIÓN SIN VARIACIÓN MODALIDAD A, B, C y D",
        "sustento": "BASE LEGAL\nReglamento de Licencias de Habilitación Urbana y Licencias de Edificación, Decreto Supremo Nº 024-2008-VIVIENDA y modificatorias (27.09.08). Art. 62.",
        "requisitos": [
            "1 La sección del FUE correspondiente a la Conformidad de Obra y Declaratoria de Edificación, por triplicado.",
            "2 Declaración jurada firmada por el profesional responsable de obra, manifestando que la obra se ha realizado conforme a los planos aprobados con la licencia de edificación.",
            "3 Solo para edificaciones para fines de vivienda multifamiliar, la dependencia municipal podrá extender la Conformidad de Obra, a solicitud del administrado a nivel de caso habitable, entendiendo así al inmueble que cuente con las siguientes características: Estructuras, muros, revocados, falsos pisos y/o contrapisos terminados, techos, instalaciones sanitarias, eléctricas, instalaciones de gas, de ser el caso, todas en funcionamiento; aparatos sanitarios, puertas y ventanas y ventanas exteriores con vidrios o cristales colocados, puerta de baño, obras exteriores y fachadas. De contar con áreas comunes, con el equipamiento de ascensores, sistema de bombeo de agua contra incendio y agua potable en completo servicio y uso; y no presentar impedimento de circulación horizontal y vertical de las personas a través de pasadizos y escaleras.",
            "4 Presentar la sección de Declaratoria de Edificación del FUE, con datos y planos correspondientes a la licencia por triplicado.",
            "5 Pago por el Derecho de la Tasa Administrativa:\nModalidad A\nModalidad B\nModalidad C\nModalidad D"
        ],
        "derecho_tramite": "Modalidad A: 2.2421% UIT\nModalidad B: 2.6263% UIT\nModalidad C: 2.7579% UIT\nModalidad D: 3.1211% UIT",
        "plazo": "Evaluación Previa - 5 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Desarrollo Urbano y Territorial",
        "reconsideracion": "Gerente de Desarrollo Urbano y Territorial\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente Municipal\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
    {
        "id": "106",
        "numero": "85",
        "procedimiento": "CONFORMIDAD DE OBRA Y DECLARATORIA DE EDIFICACIÓN CON VARIACIÓN MODALIDAD A, B, C y D",
        "sustento": "BASE LEGAL\nReglamento de Licencias de Habilitación Urbana y Licencias de Edificación, Decreto Supremo Nº 024-2008-VIVIENDA y modificatorias (27.09.08). Art. 63.",
        "requisitos": [
            "1 Sección de conformidad de obra del FUE, debidamente suscrito y por triplicado, consignado los datos que indica.",
            "2 En caso el titular del derecho a edificar sea una persona distinta a quien obtuvo la licencia de edificación deberá presentar:\na) FUE por triplicado, debidamente suscrito.\nb) Documentación que acredite que cuenta con derecho a edificar y represente al titular, en caso que el solicitante de la licencia de edificación no sea el propietario del predio.\nc) Si el solicitante es una persona jurídica se acompañará la respectiva constitución de la empresa y copia literal del poder expedidos por el Registro de Personas Jurídicas, vigente al momento de presentación de los documentos.",
            "3 Comprobante de pago de los derechos de revisión de planos de replanteo y de inspección correspondientes, cancelados.",
            "4 Planos de replanteo: un juego de copias de los planos de ubicación y de replanteo de arquitectura (plantas, cortes y elevaciones) con las mismas especificaciones de los planos del proyecto aprobado. Estos planos deberá estar firmados por el titular, el profesional responsable de la obra y una carta que acredite la autorización del proyectista original para realizar las modificaciones, que será será conservados por la municipalidad como parte del expediente una vez concluido el trámite.",
            "5 Declaración jurada de habilitación del profesional responsable.",
            "6 Pago por el Derecho de la Tasa Administrativa:\nModalidad A\nModalidad B\nModalidad C\nModalidad D"
        ],
        "derecho_tramite": "Modalidad A: 2.7237% UIT\nModalidad B: 3.0789% UIT\nModalidad C: 3.9105% UIT\nModalidad D: 4.2342% UIT",
        "plazo": "Evaluación Previa - 11 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Desarrollo Urbano y Territorial",
        "reconsideracion": "Gerente de Desarrollo Urbano y Territorial\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente Municipal\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
{
        "id": "107",
        "numero": "86",
        "procedimiento": "ANTEPROYECTO EN CONSULTA",
        "sustento": "BASE LEGAL\n- Reglamento de Licencias de Habilitación Urbana y Licencias de Edificación, Decreto Supremo Nº 024-2008-VIVIENDA y modificatorias (27.09.08). Art. 52.\n- Ley que modifica diversas disposiciones con el objeto de mejorar el clima de inversión y facilitar el cumplimiento de obligaciones tributarias, Ley Nº 29566 (28.07.10). Arts. 5 y 6.",
        "requisitos": [
            "1 FUE debidamente suscrito",
            "2 Plano de ubicación y localización",
            "3 Planos de arquitectura en escala 1/100",
            "4 Planos de seguridad y evacuación amoblados cuando se requiera la intervención de los delegados Ad Hoc del INDECI o el CGBVP.",
            "5 Declaración jurada de habilitación de los profesionales que suscriben la documentación técnica",
            "6 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "2.2974% UIT",
        "plazo": "Evaluación Previa - 8 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Desarrollo Urbano y Territorial",
        "reconsideracion": "Gerente de Desarrollo Urbano y Territorial\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente Municipal\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
    {
        "id": "108",
        "numero": "87",
        "procedimiento": "CERTIFICADO DE PARÁMETROS URBANÍSTICOS Y EDIFICATORIOS",
        "sustento": "BASE LEGAL\n- Ley de Regulación de Habilitaciones Urbanas y de Edificaciones, Ley Nº 29090 y modificatorias (25.09.07). Art 14 numeral 2",
        "requisitos": [
            "1 FUE debidamente suscrito",
            "2 Croquis de ubicación",
            "3 Pago por el Derecho de la Tasa Administrativa:",
            "--------------------------------------------------",
            "📌 NOTA: NO ES REQUISITO PARA OBTENER LICENCIA DE EDIFICACIONES",
            "📌 NOTAS PARA EL CIUDADANO:\nNo es requisito para obtener Licencia de Edificaciones"
        ],
        "derecho_tramite": "1.4763% UIT",
        "plazo": "Evaluación Previa - 5 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Desarrollo Urbano y Territorial",
        "reconsideracion": "Gerente de Desarrollo Urbano y Territorial\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente Municipal\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
    {
        "id": "109",
        "numero": "88",
        "procedimiento": "REVALIDACIÓN DE LICENCIA DE EDIFICACIÓN",
        "sustento": "BASE LEGAL\n- Ley de Regulación de Habilitaciones Urbanas y de Edificaciones, Ley Nº 29090 y modificatorias (25.09.07). Art. 11.\n- Reglamento de Licencias de Habilitación Urbana y Licencias de Edificación, Decreto Supremo Nº 024-2008-VIVIENDA y modificatorias (27.09.08). Art. 4.",
        "requisitos": [
            "1 Solicitud simple indicando número de expediente y licencia de edificación, firmada por el interesado",
            "2 FUE - Parte 1 (en original) con el cual se otorgó la Licencia de Edificación.",
            "3 Fotografías (con fechador) que muestren el nivel de avance de la edificación",
            "4 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "0.9500% UIT",
        "plazo": "Evaluación Previa - 10 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Desarrollo Urbano y Territorial",
        "reconsideracion": "Gerente de Desarrollo Urbano y Territorial\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente Municipal\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
{
        "id": "110",
        "numero": "89",
        "procedimiento": "PRÓRROGA DE LA LICENCIA DE EDIFICACIÓN",
        "sustento": "BASE LEGAL\nLey de Regulación de Habilitaciones Urbanas y de Edificaciones, Ley Nº 29090 y modificatorias (25.09.07). Art. 11.",
        "requisitos": [
            "1 Solicitud simple firmada por el solicitante.",
            "2 Copia de la licencia otorgada o consignar el número y la fecha de la licencia de edificación otorgada.",
            "--------------------------------------------------",
            "📌 NOTAS PARA EL CIUDADANO:",
            "La prorroga deberá solicitarse dentro de los 30 Días calendarios anteriores al vencimiento de la licencia otorgada."
        ],
        "derecho_tramite": "GRATUITO",
        "plazo": "Automático",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Desarrollo Urbano y Territorial",
        "reconsideracion": "",
        "apelacion": ""
    },
    {
        "id": "111",
        "numero": "90",
        "procedimiento": "LICENCIA DE HABILITACIÓN URBANA: MODALIDAD B",
        "sustento": "BASE LEGAL\n- Ley de Regulación de Habilitaciones Urbanas y de Edificaciones, Ley Nº 29090 y modificatorias (25.09.07). Arts. 10, 16 y 31.\n- Reglamento de Licencias de Habilitación Urbana y Licencias de Edificación, Decreto Supremo Nº 024-2008-VIVIENDA y modificatorias (27.09.08). Arts. 17, 25 y 32.\n- Ley que modifica diversas disposiciones con el objeto de mejorar el clima de inversión y facilitar el cumplimiento de obligaciones tributarias, Ley Nº 29566 (28.07.10). Arts. 5 y 6.",
        "requisitos": [
            "REQUISITOS GENERALES:",
            "1 FUHU por triplicado debidamente suscrito.",
            "2 Copia literal de dominio expedido por el Registro de Predios con una anticipación no mayor de 30 días naturales.",
            "3 En caso que el solicitante de la licencia de habilitación urbana no sea el propietario del predio, se deberá presentar además la documentación que acredita que cuenta con derecho a habilitar y, de ser el caso, a edificar.",
            "4 Si el solicitante es una persona jurídica se acompañará vigencia de poder expedida por el Registro de Personas Jurídicas con una anticipación no mayor a treinta (30) Días naturales.",
            "5 Declaración jurada de habilitación de los profesionales que suscriben la documentación técnica",
            "6 Pago por el Derecho de la Tasa Administrativa:",
            "REQUISITOS ESPECÍFICOS:",
            "1 Certificado de zonificación y vías.",
            "2 Certificado de factibilidad de servicios de agua, alcantarillado y de energía eléctrica, los que se acreditarán con los documentos que, para dicho fin, otorguen las empresas privadas o entidades públicas prestadoras de tales servicios.",
            "3 Declaración Jurada de inexistencia de feudatarios.",
            "4 Documentación técnica, por triplicado, firmada por el solicitante y los profesionales responsables del diseño de acuerdo a lo siguiente:\n- Plano de ubicación y localización del terreno con coordenadas UTM (Universal Transversal Mercator) gereferenciado a la red geodésica nacional, referida al datum oficial.\n- Plano perimétrico y topográfico\n- Plano de trazado y lotización con indicación de lotes, aportes, vías y secciones de vías, ejes de trazo y habilitaciones colindantes, en caso sea necesario para comprender la integración con el entorno; plano de pavimentos, con indicación de curvas de nivel cada metro.\n- Plano de ornamentación de parques, referentes al diseño, ornamentación y equipamiento de las áreas de recreación pública de ser el caso.\n- Memoria descriptiva.",
            "5 Planeamiento integral, en los casos que se requiera de acuerdo con el RNE.",
            "6 Estudio de Impacto Ambiental, según sea el caso.",
            "7 Certificado de inexistencia de restos arqueológicos, en aquellos casos en que el perímetro del área a habilitar se superponga con un área previamente declarada como parte integrante del Patrimonio Cultural de la Nación.",
            "8 Estudio de mecánica de suelos",
            "--------------------------------------------------",
            "⚠️ SE SUJETAN A ESTA MODALIDAD:",
            "a) Las habilitaciones urbanas de unidades prediales no mayores de cinco (05) hectáreas que constituyan islas rústicas y que conformen un lote único, siempre y cuando el lote no se encuentre afecto al Plan Vial Provincial o Metropolitano.",
            "b) Las habilitaciones urbanas de predios que cuenten con un Planeamiento Integral aprobado con anterioridad."
        ],
        "derecho_tramite": "10.7184% UIT",
        "plazo": "Evaluación Previa - 20 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Desarrollo Urbano y Territorial",
        "reconsideracion": "Gerente de Desarrollo Urbano y Territorial\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente Municipal\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
{
        "id": "112",
        "numero": "91",
        "procedimiento": "LICENCIA DE HABILITACIÓN URBANA MODALIDAD C (APROBACIÓN CON EVALUACIÓN PREVIA DEL PROYECTO POR LA COMISIÓN TÉCNICA)",
        "sustento": "BASE LEGAL\n- Ley de Regulación de Habilitaciones Urbanas y de Edificaciones, Ley Nº 29090 y modificatorias (25.09.07). Arts. 10, 16 y 31.\n- Reglamento de Licencias de Habilitación Urbana y Licencias de Edificación, Decreto Supremo Nº 024-2008-VIVIENDA y modificatorias (27.09.08). Arts. 17, 25, 32 y 33.\n- Ley que modifica diversas disposiciones con el objeto de mejorar el clima de inversión y facilitar el cumplimiento de obligaciones tributarias, Ley Nº 29566 (28.07.10). Arts. 5 y 6.",
        "requisitos": [
            "REQUISITOS GENERALES:",
            "1 FUHU por triplicado debidamente suscrito.",
            "2 Copia literal de dominio expedido por el Registro de Predios con una anticipación no mayor de 30 días naturales.",
            "3 En caso que el solicitante de la licencia de habilitación urbana no sea el propietario del predio, se deberá presentar además la documentación que acredita que cuenta con derecho a habilitar y, de ser el caso, a edificar.",
            "4 Si el solicitante es una persona jurídica se acompañará vigencia de poder expedida por el Registro de Personas Jurídicas con una anticipación no mayor a treinta (30) Días naturales.",
            "5 Declaración jurada de habilitación de los profesionales que suscriben la documentación técnica",
            "6 Pago por el Derecho de la Tasa Administrativa:",
            "REQUISITOS ESPECÍFICOS:",
            "1 Certificado de zonificación y vías",
            "2 Certificado de factibilidad de servicios de agua, alcantarillado y de energía eléctrica, los que se acreditarán con los documentos que, para dicho fin, otorguen las empresas privadas o entidades públicas prestadoras de tales servicios.",
            "3 Declaración Jurada de inexistencia de feudatarios.",
            "4 Documentación técnica, por triplicado, firmada por el solicitante y los profesionales responsables del diseño de acuerdo a lo siguiente:\n- Plano de ubicación y localización del terreno con coordenadas UTM (Universal Transversal Mercator) gereferenciado a la red geodésica nacional, referida al datum oficial.\n- Plano perimétrico y topográfico.\n- Plano de trazado y lotización con indicación de lotes, aportes, vías y secciones de vías, ejes de trazo y habilitaciones colindantes, en caso sea necesario para comprender la integración con el entorno; plano de pavimentos, con indicación de curvas de nivel cada metro.\n- Plano de ornamentación de parques, referentes al diseño, ornamentación y equipamiento de las áreas de recreación pública de ser el caso.\n- Memoria descriptiva.",
            "5 Planeamiento integral, en los casos que se requiera de acuerdo con el RNE.",
            "6 Estudio de Impacto Ambiental, según sea el caso.",
            "7 Certificado de inexistencia de restos arqueológicos, en aquellos casos en que el perímetro del área a habilitar se superponga con un área previamente declarada como parte integrante del Patrimonio Cultural de la Nación.",
            "8 Estudio de mecánica de suelos",
            "9 Estudio de Impacto Vial para las obras contempladas en los literales a) y c) del numeral 17.3 del artículo 17 del Decreto Supremo Nº 024-2008-VIVIENDA y modificatorias.",
            "--------------------------------------------------",
            "⚠️ SE SUJETAN A ESTA MODALIDAD:",
            "a) Las habilitaciones urbanas que se vayan a ejecutar por etapas con sujeción a un Planeamiento Integral.",
            "b) Las habilitaciones urbanas con construcción simultánea que soliciten venta garantizada de lotes.",
            "c) Las habilitaciones urbanas con construcción simultánea de viviendas en las que el número, dimensiones de lotes a habilitar y tipo de viviendas a edificar se definan en el proyecto, siempre que su finalidad sea la venta de viviendas edificadas."
        ],
        "derecho_tramite": "19.4105% UIT",
        "plazo": "Evaluación Previa - 45 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Desarrollo Urbano y Territorial",
        "reconsideracion": "Gerente de Desarrollo Urbano y Territorial\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente Municipal\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
{
        "id": "113",
        "numero": "92",
        "procedimiento": "LICENCIA DE HABILITACIÓN URBANA MODALIDAD D (APROBACIÓN CON EVALUACIÓN PREVIA DEL PROYECTO POR LA COMISIÓN TÉCNICA)",
        "sustento": "BASE LEGAL\n- Ley de Regulación de Habilitaciones Urbanas y de Edificaciones, Ley Nº 29090 y modificatorias (25.09.07). Arts. 10, 16 y 31.\n- Reglamento de Licencias de Habilitación Urbana y Licencias de Edificación, Decreto Supremo Nº 024-2008-VIVIENDA y modificatorias (27.09.08). Arts. 17, 25, 32 y 33.\n- Ley que modifica diversas disposiciones con el objeto de mejorar el clima de inversión y facilitar el cumplimiento de obligaciones tributarias, Ley Nº 29566 (28.07.10). Arts. 5 y 6.",
        "requisitos": [
            "REQUISITOS GENERALES:",
            "1 FUHU por triplicado debidamente suscrito.",
            "2 Copia literal de dominio expedido por el Registro de Predios con una anticipación no mayor de 30 días naturales.",
            "3 En caso que el solicitante de la licencia de habilitación urbana no sea el propietario del predio, se deberá presentar además la documentación que acredita que cuenta con derecho a habilitar y, de ser el caso, a edificar",
            "4 Si el solicitante es una persona jurídica se acompañará vigencia de poder expedida por el Registro de Personas Jurídicas con una anticipación no mayor a treinta (30) Días naturales.",
            "5 Declaración jurada de habilitación de los profesionales que suscriben la documentación técnica",
            "6 Pago por el Derecho de la Tasa Administrativa:",
            "REQUISITOS ESPECÍFICOS:",
            "1 Certificado de zonificación y vías.",
            "2 Certificado de factibilidad de servicios de agua, alcantarillado y de energía eléctrica, los que se acreditarán con los documentos que, para dicho fin, otorguen las empresas privadas o entidades públicas prestadoras de tales servicios.",
            "3 Declaración Jurada de inexistencia de feudatarios.",
            "4 Documentación técnica, por triplicado, firmada por el solicitante y los profesionales responsables del diseño de acuerdo a lo siguiente:\n- Plano de ubicación y localización del terreno con coordenadas UTM (Universal Transversal Mercator) gereferenciado a la red geodésica nacional, referida al datum oficial.\n- Plano perimétrico y topográfico.\n- Plano de trazado y lotización con indicación de lotes, aportes, vías y secciones de vías, ejes de trazo y habilitaciones colindantes, en caso sea necesario para comprender la integración con el entorno; plano de pavimentos, con indicación de curvas de nivel cada metro.\n- Plano de ornamentación de parques, referentes al diseño, ornamentación y equipamiento de las áreas de recreación pública de ser el caso.\n- Memoria descriptiva.",
            "5 Planeamiento integral, en los casos que se requiera de acuerdo con el RNE.",
            "6 Estudio de Impacto Ambiental, según sea el caso.",
            "7 Certificado de inexistencia de restos arqueológicos, en aquellos casos en que el perímetro del área a habilitar se superponga con un área previamente declarada como parte integrante del Patrimonio Cultural de la Nación",
            "8 Estudio de mecánica de suelos",
            "9 Estudio de Impacto Víal para las obras contempladas en los literales a) y c) del numeral 17.3 del artículo 17 del Decreto Supremo Nº 024-2008-VIVIENDA y modificatorias.",
            "--------------------------------------------------",
            "⚠️ SE SUJETAN A ESTA MODALIDAD:",
            "a) Las habilitaciones urbanas de predios que no colinden con áreas urbanas o que dichas áreas aledañas cuenten con proyectos de habilitación urbana aprobados y no ejecutados, por tanto, la habilitación urbana del predio requiera de la formulación de un Planeamiento Integral.",
            "b) Las habilitaciones urbanas de predios que colinden con Zonas Arqueológicas, inmuebles previamente declarados como bienes culturales, o con Áreas Naturales Protegidas.",
            "c) Para fines industriales, comerciales o usos especiales."
        ],
        "derecho_tramite": "19.4105% UIT",
        "plazo": "Evaluación Previa - 45 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Desarrollo Urbano y Territorial",
        "reconsideracion": "Gerente de Desarrollo Urbano y Territorial\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente Municipal\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
{
        "id": "114",
        "numero": "93",
        "procedimiento": "RECEPCIÓN DE OBRAS DE HABILITACIÓN URBANA",
        "sustento": "BASE LEGAL\n- Ley de Regulación de Habilitaciones Urbanas y de Edificaciones, Ley Nº 29090 y modificatorias (25.09.07). Arts. 19 y 31.\n- Reglamento de Licencias de Habilitación Urbana y Licencias de Edificación, Decreto Supremo Nº 024-2008-VIVIENDA y modificatorias (27.09.08). Arts. 25 y 36.\n- Ley que modifica diversas disposiciones con el objeto de mejorar el clima de inversión y facilitar el cumplimiento de obligaciones tributarias, Ley Nº 29566 (28.07.10). Arts. 5 y 6.",
        "requisitos": [
            "1 FUHU por triplicado debidamente suscrito.",
            "2 Copia literal de dominio expedido por el Registro de Predios con una anticipación no mayor de 30 días naturales.",
            "3 En caso que el solicitante de la licencia de habilitación urbana no sea el propietario del predio, se deberá presentar además la documentación que acredita que cuenta con derecho a habilitar y, de ser el caso, a edificar.",
            "4 Si el solicitante es una persona jurídica se acompañará vigencia de poder expedida por el Registro de Personas Jurídicas con una anticipación no mayor a treinta (30) Días naturales.",
            "5 Declaración jurada de habilitación de los profesionales que suscriben la documentación técnica",
            "6 La sección del FUHU correspondiente a la Recepción de Obra, por cuadruplicado. En caso que el titular del derecho a habilitar sea persona distinta a la que inició el procedimiento de habilitación urbana, deberá presentar los documentos señalados en los literales b, c y d del art. 16° de la Ley N° 29090, según corresponda.",
            "7 Documentos emitidos por las entidades prestadoras de los servicios públicos otorgando conformidad de obra a las obras de servicio.",
            "8 Copia legalizada notarialmente de las minutas que acrediten la transferencia de las áreas de aportes a las entidades receptoras.",
            "8.1 O comprobantes de pago de la redención de los mismos de ser el caso.",
            "9 En caso de que exista modificaciones al proyecto de Habilitación Urbana se deberán presentar en cuadruplicado y debidamente suscritos por el profesional responsable de la obra y el solicitante.",
            "9.1 Adjuntando carta del proyectista original autorizando las modificaciones, junto con la declaración jurada de habilitación del profesional que suscribe.",
            "9.2 - Plano de replanteo de trazado y lotización.\n- Plano de ornamentación de parques, cuando se requiera.\n- Memoria descriptiva que contenga el replanteo.",
            "10 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "6.7553% UIT",
        "plazo": "Evaluación Previa - 11 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Desarrollo Urbano y Territorial",
        "reconsideracion": "Gerente de Desarrollo Urbano y Territorial\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente Municipal\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
{
        "id": "115",
        "numero": "94",
        "procedimiento": "REGULARIZACIÓN DE HABILITACIONES URBANAS EJECUTADAS",
        "sustento": "BASE LEGAL\n- D.S. Nº 024-2008-VIVIENDA – Artículos 38, 39 y 40 (27.09.08)\n- Ley Nº 29090, Artículo 23º (25.03.07)\n- D.S. Nº 003-2010-VIVIENDA, Artículo 25º, 40º (07.02.10)",
        "requisitos": [
            "1 FUHU por triplicado debidamente suscrito.",
            "2 Copia literal de dominio expedida por el Registro de Predios con una anticipación no mayor a 30 Días naturales",
            "3 En caso que el solicitante de la licencia de habilitación urbana no sea el propietario del predio, se deberá presentar además la documentación que acredita que cuenta con derecho a habilitar y, de ser el caso, a edificar.",
            "4 Si el solicitante es una persona jurídica se acompañará vigencia de poder expedida por el Registro de Personas Jurídicas con una anticipación no mayor a treinta (30) Días naturales.",
            "5 Boleta de Habilitación de los profesionales que suscriben la documentación técnica",
            "6 Pago por el Derecho de la Tasa Administrativa:",
            "7 Certificado de Zonificación y Vías",
            "8 Plano de ubicación, con la localización del terreno",
            "9 Plano de lotización, conteniendo el perímetro del terreno, el diseño de la lotización, de las vías, aceras y bermas; y las áreas correspondientes a los aportes normados.",
            "9.1 Asimismo, se deberá indicar los lotes ocupados y la altura de las edificaciones existentes. La autorización deberá estar en concordancia con el Plan de Desarrollo Urbano aprobados por la Municipalidad Provincial correspondiente.",
            "10 Memoria descriptiva, indicando las manzanas, las áreas de los lotes, la numeración y los aportes",
            "11 Copia legalizada notarialmente de las minutas que acrediten la transferencia de las áreas de aportes a las entidades receptoras de los mismos",
            "11.1 O comprobantes de pago de la redención de los mismos, de ser el caso",
            "12 Declaración jurada suscrita por el solicitante de la habilitación y el profesional responsable de la obra, en la que conste que las obras han sido ejecutados, total o parcialmente",
            "12.1 En caso que se cuente con estudios preliminares aprobados, no corresponde presentar los documentos de los literales 7), 8) y 9), debiendo presentar en su reemplazo:",
            "12.2 a) Resolución y planos de los estudios preliminares aprobados\nb) Planos de Replanteo de la Habilitación Urbana"
        ],
        "derecho_tramite": "10.8579% UIT",
        "plazo": "Evaluación Previa - 17 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Desarrollo Urbano y Territorial",
        "reconsideracion": "Gerente de Desarrollo Urbano y Territorial\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente Municipal\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
{
        "id": "116",
        "numero": "95",
        "procedimiento": "INDEPENDIZACIÓN O PARCELACIÓN DE TERRENOS RÚSTICOS",
        "sustento": "BASE LEGAL\n- Ley de Regulación de Habilitaciones Urbanas y de Edificaciones, Ley Nº 29090 y modificatorias (25.09.07). Art. 31.\n- Reglamento de Licencias de Habilitación Urbana y Licencias de Edificación, Decreto Supremo Nº 024-2008-VIVIENDA y modificatorias (27.09.08). Arts. 25, 27 y 28.\n- Ley que modifica diversas disposiciones con el objeto de mejorar el clima de inversión y facilitar el cumplimiento de obligaciones tributarias, Ley Nº 29566 (28.07.10). Arts. 5 y 6.",
        "requisitos": [
            "1 FUHU por triplicado debidamente suscrito.",
            "2 Copia literal de dominio expedido por el Registro de Predios con una anticipación no mayor de 30 dias naturales.",
            "3 En caso que el solicitante de la licencia de habilitación urbana no sea el propietario del predio, se deberá presentar además la documentación que acredita que cuenta con derecho a habilitar y, de ser el caso, a edificar.",
            "4 Si el solicitante es una persona jurídica se acompañará vigencia de poder expedida por el Registro de Personas Jurídicas con una anticipación no mayor a treinta (30) Días naturales.",
            "5 Declaración jurada de habilitación de los profesionales que suscriben la documentación técnica",
            "6 Certificado de zonificación y vías expedido por la Municipalidad Provincial.",
            "7 Declaración Jurada de inexistencia de feudatarios.",
            "8 Documentación técnica por triplicado compuesta por:",
            "8.1 - Plano de ubicación y localización del terreno matriz con coordenadas UTM, referidas al sistema Geodésico Oficial",
            "8.2 - Plano de planeamiento integral con la propuesta de integración a la trama urbana más cercana señalando el perímetro y el relieve con curvas de nivel, usos de suelo y aportes normativos",
            "8.3 georeferenciado al Sistema Geodésico Oficial, en concordancia con el Plan de Desarrollo Urbano aprobado por la Municipalidad Provincial correspondiente",
            "8.4 - Plano del Predio Rustico matriz, indicando perímetro, linderos, áreas, curvas de nivel y nomenclatura original, según antecedentes registrales, georeferenciado al Sistema Geodésico Oficial.",
            "8.5 - Plano de Independización, señalando la parcela independizada y la(s) parcela (s) remanente (s) indicando perímetro, linderos, área, curvas de nivel y nomenclatura original según ante-",
            "8.6 cedentes registrales georeferenciado al Sistema Geodésico Oficial. Cuando corresponda, el plano de parcelación identificara el número de parcelas con los sufijos del predio matriz.",
            "8.7 - Memoria descriptiva indicando áreas, linderos y medidas perimétricas del predio matriz del área independizada y del área remanente.",
            "9 Certificado de inexistencia de restos arqueológicos (emitido por el INC) en aquellos casos en que el perímetro del terreno a independizar se superponga o colinde con una área previamente decla- rada como Patrimonio Cultural de la Nación.",
            "10 En caso se solicite la independización de predio rústicos y la habilitación urbana conjuntamente y en un solo procedimiento, la Comisión Técnica verificará ambos procedimientos simultáneamente.",
            "11 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "4.3342% UIT",
        "plazo": "Evaluación Previa - 10 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Desarrollo Urbano y Territorial",
        "reconsideracion": "Gerente de Desarrollo Urbano y Territorial\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente Municipal\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
{
        "id": "117",
        "numero": "96",
        "procedimiento": "SUBDIVISIÓN DE LOTE URBANO",
        "sustento": "BASE LEGAL\n- Ley de Regulación de Habilitaciones Urbanas y de Edificaciones, Ley Nº 29090 y modificatorias (25.09.07). Art. 31.\n- Reglamento de Licencias de Habilitación Urbana y Licencias de Edificación, Decreto Supremo Nº 024-2008-VIVIENDA y modificatorias (27.09.08). Arts. 25, 29, 30 y 31.\n- Ley que modifica diversas disposiciones con el objeto de mejorar el clima de inversión y facilitar el cumplimiento de obligaciones tributarias, Ley Nº 29566 (28.07.10). Arts. 5 y 6.",
        "requisitos": [
            "1 FUHU por triplicado debidamente suscrito.",
            "2 Copia literal de dominio expedido por el Registro de Predios con una anticipación no mayor de 30 dias naturales.",
            "3 En caso que el solicitante de la licencia de habilitación urbana no sea el propietario del predio, se deberá presentar además la documentación que acredita que cuenta con derecho a habilitar y, de ser el caso, a edificar.",
            "4 Si el solicitante es una persona jurídica se acompañará vigencia de poder expedida por el Registro de Personas Jurídicas con una anticipación no mayor a treinta (30) Días naturales.",
            "5 Declaración jurada de habilitación de los profesionales que suscriben la documentación técnica",
            "6 Documentación técnica por triplicado compuesta por:",
            "6.1 -Plano de ubicación y localización del lote materia de subdivisión",
            "6.2 -Plano del lote a subdividir, señalando el área, linderos, medidas perimétricas y nomenclatura, según los antecedentes registrales.",
            "6.3 -Plano de la subdivisión señalando áreas, linderos, medidas perimétricas y nomenclatura de cada sublote propuesto resultante.",
            "6.4 -Memoria descriptiva, indicando áreas, linderos y medidas perimétricas del lote de subdivisión y de los sublotes propuestos resultantes.",
            "6.5 Estos documentos deben estar firmados por el solicitante y el profesional responsable del proyecto",
            "7 Pago por el Derecho de la Tasa Administrativa:",
            "--------------------------------------------------",
            "📌 NOTAS PARA EL CIUDADANO:",
            "En caso se solicite la subdivisión de un lote que cuente con obras de Habilitación Urbana inconclusas, dichas obras deberan ser ejecutadas y recepcionadas en el mismo procedimiento"
        ],
        "derecho_tramite": "2.5368% UIT",
        "plazo": "Evaluación Previa - 10 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Desarrollo Urbano y Territorial",
        "reconsideracion": "Gerente de Desarrollo Urbano y Territorial\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente Municipal\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
{
        "id": "118",
        "numero": "97",
        "procedimiento": "AUTORIZACIÓN PARA APERTURA, MODIFICACIÓN Y CLAUSURA DE PUERTAS Y VENTANAS",
        "sustento": "BASE LEGAL\n- Ley de Regulación de Habilitaciones Urbanas y de Edificaciones, Ley Nº 29090 y modificatorias (25.09.07). Art. 31.\n- Reglamento de Licencias de Habilitación Urbana y Licencias de Edificación, Decreto Supremo Nº 024-2008-VIVIENDA y modificatorias (27.09.08). Arts. 25, 29, 30 y 31\n- Ley que modifica diversas disposiciones con el objeto de mejorar el clima de inversión y facilitar el cumplimiento de obligaciones tributarias, Ley Nº 29566 (28.07.10). Arts. 5 y 6.",
        "requisitos": [
            "1 Solicitud dirigida al Alcalde cumpliendo con los requisitos generales de presentación",
            "2 Copia autenticada del título de propiedad",
            "3 Copia simple del Plano de Ubicación",
            "4 Copia del comprobante de Pago por el Derecho de Asignación de Numeración de Finca (por cada puerta)",
            "5 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "0.9289% UIT",
        "plazo": "Evaluación Previa - 7 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Desarrollo Urbano y Territorial",
        "reconsideracion": "Gerente de Desarrollo Urbano y Territorial\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente Municipal\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
    {
        "id": "119",
        "numero": "98",
        "procedimiento": "AUTORIZACIÓN PARA LA EXTRACCIÓN DE MATERIALES DE LOS ALVEOLOS O CAUCES DE LOS RIOS",
        "sustento": "BASE LEGAL\n- Ley Nº 28221, Ley que regula el Derecho de Extracción de los Álveolos o Cauces de los Ríos por las Municipalidades (Pub. 11-05-2004)\n- Ley Nº 27444, Ley de Procedimiento Administrativo General (Pub. 11-04-2011)",
        "requisitos": [
            "1 Solicitud dirigida al Alcalde cumpliendo con los requisitos generales de presentación, señalando y adjuntando los siguientes documentos.",
            "1.1 - El tipo de material a extraerse y el Volumen del mismo expresado en m3",
            "1.2 - El Cauce y la Zona de Extracción, así como los puntos de acceso y salidad del cauce expresado en base a coordenadas UTM",
            "1.3 - Planos a escala 1/5000 UTM de aspectos mencionados en el requisitos anterior",
            "1.4 - Ubicación de las instalaciones de clasificación y acopio de los hubiera",
            "1.5 - Sistema de extracción y las características de la maquinaria utilizada",
            "2 Estudio de impacto ambiental",
            "3 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "1.8684% UIT",
        "plazo": "Evaluación Previa - 10 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Desarrollo Urbano y Territorial",
        "reconsideracion": "Gerente de Desarrollo Urbano y Territorial\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente Municipal\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
{
        "id": "120",
        "numero": "99.1",
        "procedimiento": "AUTORIZACIÓN PARA LA UBICACIÓN DE ELEMENTOS DE PUBLICIDAD EXTERIOR Y/O ANUNCIOS EN: PANELES MONUMENTALES: - SIMPLES - UNIPOLARES",
        "sustento": "BASE LEGAL\n- Ley Nº 27972 (27.05.03). Arts. 40 y 79 numeral 1.4.4.\n- Ley Nº 27444 (11.04.01). Arts. 34, 35, 44 y 45.\n- Ley Nº 29060 (07.07.07).\n- Decreto Supremo Nº 156-2004-EF (15.11.04). Art. 68.\n- Resolución Nº 0148-2008/CEB-INDECOPI (13.09.2008).",
        "requisitos": [
            "1 Solicitud según formulario (distribución gratuita o de libre reproducción).",
            "2 Presentar las vistas siguientes:",
            "2.1 a) Arte o diseño del anuncio o aviso publicitario con sus dimensiones.",
            "2.2 b) Una fotografía en la cual se aprecie el entorno urbano y el bien o edificación donde se ubicará el elemento de publicidad exterior y/o anuncio.",
            "2.3 c) Fotomontaje o posicionamiento virtual del elemento de publicidad exterior y/o anuncio para el que se solicita autorización, en el cual se aprecie el entorno urbano y el bien o edificación donde se ubicará.",
            "3 Copia de la Autorización Municipal de funcionamiento vigente, si se ubica en un establecimiento que opera fuera de la jurisdicción del municipio.",
            "4 Copia simple del documento de identidad del solicitante o representante legal.",
            "5 Carta poder con firma legalizada, en caso de ser representación.",
            "6 Copia del acta de la Junta o Asamblea de Propietarios de los bienes de dominio privado sujetos al régimen de propiedad exclusiva y común, en la que la mitad más uno de los Propietarios autorizan la ubicación del elemento de publicidad exterior y/o anuncio.",
            "6.1 En caso de no existir Junta o Asamblea de Propietarios, podrá presentar documentos de autorizan suscrito por la mitad más uno de sus propietarios de corresponder.",
            "7 Plano de Ubicación con coordenadas UTM, a a escala 1/500 o 1/250, y Esquema de Localización, a escala 1/5,000. Se indicarán las distancias de la arista más saliente del panel y del eje de la base al borde exterior de la pista. Debe adjuntar el archivo digitalizado del plano.",
            "8 Especificaciones Técnicas y Plano de Estructuras a escala conveniente, refrendados por un Ingeniero Civil",
            "9 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "2.5579% UIT",
        "plazo": "Evaluación Previa - 30 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Desarrollo Urbano y Territorial",
        "reconsideracion": "Gerente de Desarrollo Urbano y Territorial\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente Municipal\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
{
        "id": "121",
        "numero": "99.2",
        "procedimiento": "AVISOS PUBLICITARIOS CON UN ÁREA DE EXHIBICIÓN HASTA 12 M2. - LUMINOSOS - ILUMINADOS - ESPECIALES",
        "sustento": "BASE LEGAL\n- Ley Nº 27972 (27.05.03). Arts. 40 y 79 numeral 1.4.4.\n- Ley Nº 27444 (11.04.01). Arts. 34, 35, 44 y 45.\n- Ley Nº 29060 (07.07.07).\n- Decreto Supremo Nº 156-2004-EF (15.11.04). Art. 68.\n- Resolución Nº 0148-2008/CEB-INDECOPI (13.09.2008).",
        "requisitos": [
            "1 Solicitud según formulario (distribución gratuita o de libre reproducción).",
            "2 Presentar las vistas siguientes:",
            "2.1 a) Arte o diseño del anuncio o aviso publicitario con sus dimensiones.",
            "2.2 b) Una fotografía en la cual se aprecie el entorno urbano y el bien o edificación donde se ubicará el elemento de publicidad exterior y/o anuncio.",
            "2.3 c) Fotomontaje o posicionamiento virtual del elemento de publicidad exterior y/o anuncio para el que se solicita autorización, en el cual se aprecie el entorno urbano y el bien o edificación donde se ubicará.",
            "3 Copia de la Autorización Municipal de funcionamiento vigente, si se ubica en un establecimiento que opera fuera de la jurisdicción del municipio.",
            "4 Copia simple del documento de identidad del solicitante o representante legal.",
            "5 Carta poder con firma legalizada, en caso de ser representación.",
            "6 Copia del acta de la Junta o Asamblea de Propietarios de los bienes de dominio privado sujetos al régimen de propiedad exclusiva y común, en la que la mitad más uno de los Propietarios autorizan la ubicación del elemento de publicidad exterior y/o anuncio.",
            "6.1 En caso de no existir Junta o Asamblea de Propietarios, podrá presentar documentos de autorización suscrito por la mitad más uno de sus propietarios de corresponder.",
            "7 En caso de anuncios en dominio público, presentar copia de la carta de factibilidad de conexión eléctrica por la empresa prestadora de servicios correspondiente.",
            "8 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "2.9316% UIT",
        "plazo": "Evaluación Previa - 30 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Desarrollo Urbano y Territorial",
        "reconsideracion": "Gerente de Desarrollo Urbano y Territorial\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente Municipal\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
    {
        "id": "122",
        "numero": "100",
        "procedimiento": "CERTIFICADO CATASTRAL",
        "sustento": "BASE LEGAL\n- Ley Nº 27972 (27.05.03). Arts. 40 y 79 numeral 3.3.\n- Ley Nº 27444 (11.04.01). Arts. 34, 35, 44 y 45.\n- Ley Nº 29060 (07.07.07).\n- Decreto Supremo Nº 156-2004-EF (15.11.04). Art. 68.\n- Ley Nº 28294 (21.07.04). Art. 14 numeral 5.\n- Decreto Supremo Nº 005-2006-JUS (12.02.08). Arts. 3 literal f), 39, 41 y 42.",
        "requisitos": [
            "1 Formato de solicitud (distribución gratuita o de libre reproducción).",
            "2 Copia simple del documento (DNI/CE) del titular.",
            "3 De actuar como representante, adjuntar carta poder vigente (persona natural, poder simple y persona jurídica, copia fedateada del poder notarial) y copia simple de su documento (DNI/CE).",
            "4 Copia fedateada de la ficha registral del predio, en caso de no estar registrado el predio a nombre del titular, documento que acredite la propiedad.",
            "5 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "1.5605% UIT",
        "plazo": "Automático",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Desarrollo Desarrollo Urbano y Territorial",
        "reconsideracion": "",
        "apelacion": ""
    },
{
        "id": "123",
        "numero": "101",
        "procedimiento": "FICHA ÚNICA CATASTRAL",
        "sustento": "BASE LEGAL\n- Ley Nº 27972 (27.05.03). Arts. 40 y 79 numeral 3.3.\n- Ley Nº 27444 (11.04.01). Art. 34, 35, 44 y 45.\n- Ley Nº 29060 (07.07.07).\n- Decreto Supremo Nº 156-2004-EF (15.11.04). Art. 68.\n- Ley Nº 28294 (21.07.04). Art. 18.\n- Decreto Supremo Nº 005-2006-JUS (12.02.08). Arts. 3 literal f) y 44.\n- Resolución Nº 001-2007-SNCP-CNC (16.07.07).",
        "requisitos": [
            "1 Formato de solicitud (distribución gratuita o de libre reproducción).",
            "2 Copia simple del documento (DNI/CE) del titular.",
            "3 De actuar como representante, adjuntar carta poder vigente (persona natural, poder simple y persona jurídica, copia fedateada del poder notarial) y copia simple de su documento (DNI/CE)",
            "4 Copia fedateada de la ficha registral del predio, en caso de no estar registrado el predio a nombre del titular, documento que acredite la propiedad.",
            "5 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "1.5368% UIT",
        "plazo": "Automático",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Desarrollo Urbano y Territorial",
        "reconsideracion": "",
        "apelacion": ""
    },
    {
        "id": "124",
        "numero": "102",
        "procedimiento": "RECTIFICACIÓN DE FICHA CATASTRAL",
        "sustento": "BASE LEGAL\n- Ley Nº 27972 (27.05.03). Arts. 40 y 79 numeral 3.3.\n- Ley Nº 27444 (11.04.01). Art. 34, 35, 44 y 45.\n- Ley Nº 29060 (07.07.07).\n- Decreto Supremo Nº 156-2004-EF (15.11.04). Art. 68.\n- Ley Nº 28294 (21.07.04). Art. 15 numeral 1, y 18.\n- Decreto Supremo Nº 005-2006-JUS (12.02.08). Arts. 3 literal f) y 44.\n- Resolución Nº 001-2007-SNCP-CNC (16.07.07).",
        "requisitos": [
            "1 Formato de solicitud (distribución gratuita o de libre reproducción), en el cual se debe indicar la información a rectificar, adjuntando los información a rectificar, adjuntando los documentos que sustenten la rectificación.",
            "2 Copia simple del documento (DNI/CE) del titular.",
            "3 De actuar como representante, adjuntar carta poder vigente (persona natural poder simple y persona jurídica, copia fedateada del poder notarial), y copia simple de su documento (DNI/CE).",
            "4 Copia fedateada de la ficha registral del predio, en caso de no estar registrado el predio a nombre del titular, documento que acredite la propiedad.",
            "5 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "1.0342% UIT",
        "plazo": "Evaluación Previa - 30 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Desarrollo Urbano y Territorial",
        "reconsideracion": "Gerente de Desarrollo Urbano y Territorial\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente Municipal\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
{
        "id": "125",
        "numero": "103",
        "procedimiento": "ACTUALIZACIÓN DE LA INFORMACIÓN CATASTRAL",
        "sustento": "BASE LEGAL\n- Ley Nº 27972 (27.05.03). Arts. 40 y 79 numeral 3.3.\n- Ley Nº 27444 (11.04.01). Art. 34, 35, 44 y 45.\n- Ley Nº 29060 (07.07.07).\n- Decreto Supremo Nº 156-2004-EF (15.11.04). Art. 68.\n- Ley Nº 28294 (21.07.04). Art. 15 numeral 1, y 18.\n- Decreto Supremo Nº 005-2006-JUS (12.02.08). Arts. 3 lineal f) y 45.\n- Resolución Nº 001-2007-SNCP-CNC (16.07.07).",
        "requisitos": [
            "1 Formato de solicitud (distribución gratuita o de libre reproducción), en el cual se debe indicar la información a actualizar, adjuntando los documentos que sustenten la actualización.",
            "2 Copia simple del documento (DNI/CE) del titular.",
            "3 De actuar como representante, adjuntar carta poder vigente (persona natural poder simple y persona jurídica, copia fedateada del poder notarial), y copia simple de su documento (DNI/CE).",
            "4 Copia fedateada de la ficha registral del predio, en caso de no estar registrado el predio a nombre del titular, documento que acredite la propiedad.",
            "5 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "0.9237% UIT",
        "plazo": "Automático",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Desarrollo Urbano y Territorial",
        "reconsideracion": "",
        "apelacion": ""
    },
    {
        "id": "126",
        "numero": "104",
        "procedimiento": "CERTIFICADO DE JURISDICCIÓN",
        "sustento": "BASE LEGAL\n- Ley Nº 27972 (27.05.03). Arts. 40 y 79 numeral 3.3.\n- Ley Nº 27444 (11.04.01). Art. 34, 35, 44 y 45.\n- Ley Nº 29060 (07.07.07).\n- Decreto Supremo Nº 156-2004-EF (15.11.04). Art. 68.\n- Ley Nº 28294 (21.07.04). Art. 15 numeral 1, y 18.\n- Decreto Supremo Nº 005-2006-JUS (12.02.08). Arts. 3 literal f), 40 y 41.\n- Resolución Nº 248-2008-SUNARP-SN (30.08.08). Art. 56.",
        "requisitos": [
            "1 Formato de solicitud (distribución gratuita o de libre reproducción).",
            "2 Copia simple del documento (DNI/CE) del titular.",
            "3 De actuar como representante, adjuntar carta poder vigente (persona natural poder simple y persona jurídica, copia fedateada del poder notarial), y copia simple de su documento (DNI/CE).",
            "4 Plano de ubicación.",
            "5 Copia fedateada del documento que acredita la propiedad inscrita en la SUNARP u otro documento que acredita la propiedad o posesión,indicando que el predio se encuentra en el Distrito.",
            "6 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "1.2974% UIT",
        "plazo": "Evaluación Previa - 30 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Desarrollo Urbano y Territorial",
        "reconsideracion": "Gerente de Desarrollo Urbano y Territorial\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente Municipal\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
{
        "id": "127",
        "numero": "105",
        "procedimiento": "CERTIFICADO DE NOMENCLATURA VIAL",
        "sustento": "BASE LEGAL\n- Ley Nº 27972 (27.05.03). Arts. 40 y 79 numeral 3.3.\n- Ley Nº 27444 (11.04.01). Art. 34, 35, 44 y 45.\n- Ley Nº 29060 (07.07.07).\n- Decreto Supremo Nº 156-2004-EF (15.11.04). Art. 68.\n- Ley Nº 28294 (21.07.04). Art. 15 numeral 1, y 18.\n- Decreto Supremo Nº 005-2006-JUS (12.02.08). Arts. 3 literal f), 40 y 41.\n- Resolución Nº 248-2008-SUNARP-SN (30.08.08). Art. 57.",
        "requisitos": [
            "1 Formato de solicitud (distribución gratuita o de libre reproducción).",
            "2 Copia simple del documento (DNI/CE) del titular.",
            "3 De actuar como representante, adjuntar carta poder vigente (persona natural poder simple y persona jurídica, copia fedateada del poder notarial), y copia simple de su documento (DNI/CE).",
            "4 Plano de ubicación.",
            "5 Copia fedateada de documentos que acredita la propiedad inscrita en la SUNARP u otro documento que acredite la propiedad, de ser el caso.",
            "6 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "1.5684% UIT",
        "plazo": "Automático",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Desarrollo Urbano y Territorial",
        "reconsideracion": "",
        "apelacion": ""
    },
    {
        "id": "128",
        "numero": "106.1",
        "procedimiento": "CERTIFICADO DE NUMERACIÓN PARA: NUEVA EDIFICACIÓN",
        "sustento": "BASE LEGAL\n- Ley Nº 27972 (27.05.03). Arts. 40 y 79 numeral 3.3.\n- Ley Nº 27444 (11.04.01). Art. 34, 35, 44 y 45.\n- Ley Nº 29060 (07.07.07).\n- Decreto Supremo Nº 156-2004-EF (15.11.04). Art. 68.\n- Ley Nº 28294 (21.07.04). Art. 15 numeral 1, y 18.\n- Decreto Supremo Nº 005-2006-JUS (12.02.08). Arts. 3 literal f), 40 y 41.\n- Resolución Nº 248-2008-SUNARP-SN (30.08.08). Art. 58.\n- Ley Nº 29090 (25.09.07). Art. 33 y modificatoria .\n- Ley Nº 29476 (18.12.09). Art. 15.\n- Decreto Supremo Nº 024-2008-VIVIENDA (27.09.08). Art. 49.\n- Decreto Supremo Nº 003-2010-VIVIENDA (07.02.10).",
        "requisitos": [
            "1 Formato de solicitud (distribución gratuita o de libre reproducción).",
            "2 Copia simple del documento (DNI/CE) del titular.",
            "3 De actuar como representante, adjuntar carta poder vigente (persona natural poder simple y persona jurídica, copia fedateada del poder notarial), y copia simple de su documento (DNI/CE).",
            "4 Copia fedateada de documentos que acredita la propiedad inscrita en la SUNARP.",
            "5 Copia de Licencia de Edificación, conformidad o Finalización de obra, o Declaratoria de Edificación.",
            "6 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "1.1816% UIT",
        "plazo": "Evaluación Previa - 15 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Desarrollo Urbano y Territorial",
        "reconsideracion": "Gerente de Desarrollo Urbano y Territorial\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente Municipal\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
{
        "id": "129",
        "numero": "106.2",
        "procedimiento": "CERTIFICADO DE NUMERACIÓN PARA: EDIFICACIÓN SANEADA Y CONCLUIDA",
        "sustento": "BASE LEGAL\n- Ley Nº 27972 (27.05.03). Arts. 40 y 79 numeral 3.3.\n- Ley Nº 29060 (07.07.07).\n- Decreto Supremo Nº 156-2004-EF (15.11.04). Art. 68. y 18.\n- Decreto Supremo Nº 005-2006-JUS (12.02.08). Arts. 3 literal f), 40 y 41.\n- Resolucion Nº 248-2008-SUNARP-SN (30.08.08). Art. 58\n- Ley Nº 29090 (25.09.07). Art. 33 y modificatoria .\n- Ley Nº 29476 (18.12.09). Art. 15.\n- Decreto Supremo Nº 024-2008-VIVIENDA (27.09.08). Art. 49.\n- Decreto Supremo Nº 003-2010-VIVIENDA (07.02.10).",
        "requisitos": [
            "1 Formato de solicitud (distribución gratuita o de libre reproducción).",
            "2 Copia simple del documento (DNI/CE) del titular.",
            "3 De actuar como representante, adjuntar carta poder vigente (persona natural poder simple y persona jurídica, copia fedateada del poder notarial), y copia simple de su documento (DNI/CE).",
            "4 Copia fedateada de documentos que acredite la propiedad inscrita en la SUNARP.",
            "4.1 En caso requiera nueva asignación de numeración.",
            "4.2 Acreditar el saneamiento del nuevo ingreso (Numeración Exterior) y/o unidad inmobiliaria (Numeración Interior).",
            "4.3 En caso de tener varias numeraciones asignadas con anterioridad.",
            "4.4 Acreditar que registralmente sigue inscrito con una sola unidad inmobiliaria.",
            "5 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "1.9632% UIT",
        "plazo": "Evaluación Previa - 15 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Desarrollo Urbano y Territorial",
        "reconsideracion": "Gerente de Desarrollo Urbano y Territorial\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente Municipal\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
    {
        "id": "130",
        "numero": "107",
        "procedimiento": "CONSTANCIA DE POSESIÓN PARA FINES DEL OTORGAMIENTO DE SERVICIOS BÁSICOS",
        "sustento": "BASE LEGAL\n- Ley Nº 27972 (27.05.03). Arts. 40 y 79 numeral 3.5.\n- Ley Nº 27444 (11.04.01). Art. 34, 35, 44 y 45.\n- Ley Nº 29060 (07.07.07).\n- Decreto Supremo Nº 156-2004-EF (15.11.04). Art. 68.\n- Ley Nº 28687 (17.03.06). Art. 24, 25 y 26.\n- Decreto Supremo Nº 017-2006-VIVIENDA (27.07.06). Arts. 27, 28 y 29.",
        "requisitos": [
            "1 Formato de solicitud (distribución gratuita o de libre reproducción). Indicando nombre, dirección y número de DNI, o solicitud simple.",
            "2 Presentación de DNI.",
            "3 Plano simple de ubicación del Predio.",
            "4 Acta de verificación de posesión efectiva del predio emitida por un funcionario de la municipalidad distrital correspondiente y suscrita por todos los colindantes del predio o acta policial de posesión suscrita por todos los colindantes de dicho predio.",
            "5 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "1.5316% UIT",
        "plazo": "Evaluación Previa - 30 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Desarrollo Urbano y Territorial",
        "reconsideracion": "Gerente de Desarrollo Urbano y Territorial\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente Municipal\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
{
        "id": "131",
        "numero": "108",
        "procedimiento": "SOLICITUD DE DECLARACIÓN DE PREDIO TUGURIZADO",
        "sustento": "BASE LEGAL\n- Ley Nº 27972 (27.05.03). Arts. 40 y 79 numeral 4.2.\n- Ley Nº 27444 (11.04.01). Arts. 34, 35, 44 y 45.\n- Ley Nº 29060 (07.07.07).\n- Decreto Supremo Nº 156-2004-EF (15.11.04). Art. 68.\n- Ley Nº 29415 (02.10.09). Arts. 5 literal d), 24 y 25.\n- Decreto Supremo Nº 011-2010-VIVIENDA. (30.10.10).",
        "requisitos": [
            "1 Solicitud dirigida a funcionario competente debidamente firmada.",
            "2 Documento que acredite estado de vulnerabilidad:",
            "2.1 - En caso la edificación tenga más de cuarenta años, deberá presentar documento que acredite que la edificación presenta una vulnerabilidad física, alta o muy alta según los criterios de INDECI.",
            "2.2 - En caso la edificación tenga menos de cuarenta años, deberá presentar documento que acredite que ésta no se ajusta a las normas de edificación y atenta contra la vida y la salud de los moradores y vecinos por hacinamiento humano, entre otros; y que, la edificación carezca de ventilación e iluminación natural o artificial, o que cuente con ellas pero de modo inadecuado",
            "2.3 - En caso de edificaciones que atenten contra la vida y la salud de los moradores y vecinos por hacinamiento humano, grave afectación de las paredes y estructuras principales, entre otros, de acuerdo con las normas técnica aprobadas por la OMS y normas de sanidad vigentes, deberá presentar documento que acredite dicha situación emitido por autoridad competente.",
            "2.4 - En caso de edificaciones que carezcan de iluminación natural o artificial o que cuente con ellas pero de modo inadecuado, según normatibidad de la materia, deberá presentar documento que acredite dicha situación, emitido por autoridad competente.",
            "3 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "1.4368% UIT",
        "plazo": "Evaluación Previa - 30 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Desarrollo Urbano y Territorial",
        "reconsideracion": "Gerente de Desarrollo Urbano y Territorial\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente Municipal\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
    {
        "id": "132",
        "numero": "109",
        "procedimiento": "SOLICITUD PARA IDENTIFICACIÓN Y DECLARACIÓN DE ÁREAS DE TRATAMIENTO",
        "sustento": "BASE LEGAL\n- Ley Nº 27972 (27.05.03). Arts. 40 y 79 numeral 4.2.\n- Ley Nº 27444 (11.04.01). Arts. 34, 35, 44 y 45.\n- Ley Nº 29060 (07.07.07).\n- Decreto Supremo Nº 156-2004-EF (15.11.04). Art. 68.\n- Ley Nº 29415 (02.10.09). Arts. 6.\n- Decreto Supremo Nº 011-2010-VIVIENDA (30.10.10). Arts. del 4 al 17.",
        "requisitos": [
            "1 Solicitud dirigida a funcionario competente debidamente firmada, presentada por propietarios de los predios, grupos de moradores/poseedores de los predios, promotoores o empresarios privados.",
            "2 Documento que acredite la propiedad, posesión o documento que acredite el interés para desarrollar proyecto de renovación urbana según corresponda.",
            "3 Plano de ubicación de la microzona o zona del área de tratamiento.",
            "4 Documento técnico que sustente el estado tugurizado de los predios.",
            "5 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "1.4368% UIT",
        "plazo": "Evaluación Previa - 30 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Desarrollo Urbano y Territorial",
        "reconsideracion": "Gerente de Desarrollo Urbano y Territorial\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente Municipal\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
{
        "id": "131",
        "numero": "108",
        "procedimiento": "SOLICITUD DE DECLARACIÓN DE PREDIO TUGURIZADO",
        "sustento": "BASE LEGAL\n- Ley Nº 27972 (27.05.03). Arts. 40 y 79 numeral 4.2.\n- Ley Nº 27444 (11.04.01). Arts. 34, 35, 44 y 45.\n- Ley Nº 29060 (07.07.07).\n- Decreto Supremo Nº 156-2004-EF (15.11.04). Art. 68.\n- Ley Nº 29415 (02.10.09). Arts. 5 literal d), 24 y 25.\n- Decreto Supremo Nº 011-2010-VIVIENDA. (30.10.10).",
        "requisitos": [
            "1 Solicitud dirigida a funcionario competente debidamente firmada.",
            "2 Documento que acredite estado de vulnerabilidad:",
            "2.1 - En caso la edificación tenga más de cuarenta años, deberá presentar documento que acredite que la edificación presenta una vulnerabilidad física, alta o muy alta según los criterios de INDECI.",
            "2.2 - En caso la edificación tenga menos de cuarenta años, deberá presentar documento que acredite que ésta no se ajusta a las normas de edificación y atenta contra la vida y la salud de los moradores y vecinos por hacinamiento humano, entre otros; y que, la edificación carezca de ventilación e iluminación natural o artificial, o que cuente con ellas pero de modo inadecuado",
            "2.3 - En caso de edificaciones que atenten contra la vida y la salud de los moradores y vecinos por hacinamiento humano, grave afectación de las paredes y estructuras principales, entre otros, de acuerdo con las normas técnica aprobadas por la OMS y normas de sanidad vigentes, deberá presentar documento que acredite dicha situación emitido por autoridad competente.",
            "2.4 - En caso de edificaciones que carezcan de iluminación natural o artificial o que cuente con ellas pero de modo inadecuado, según normatibidad de la materia, deberá presentar documento que acredite dicha situación, emitido por autoridad competente.",
            "3 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "1.4368% UIT",
        "plazo": "Evaluación Previa - 30 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Desarrollo Urbano y Territorial",
        "reconsideracion": "Gerente de Desarrollo Urbano y Territorial\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente Municipal\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
    {
        "id": "132",
        "numero": "109",
        "procedimiento": "SOLICITUD PARA IDENTIFICACIÓN Y DECLARACIÓN DE ÁREAS DE TRATAMIENTO",
        "sustento": "BASE LEGAL\n- Ley Nº 27972 (27.05.03). Arts. 40 y 79 numeral 4.2.\n- Ley Nº 27444 (11.04.01). Arts. 34, 35, 44 y 45.\n- Ley Nº 29060 (07.07.07).\n- Decreto Supremo Nº 156-2004-EF (15.11.04). Art. 68.\n- Ley Nº 29415 (02.10.09). Arts. 6.\n- Decreto Supremo Nº 011-2010-VIVIENDA (30.10.10). Arts. del 4 al 17.",
        "requisitos": [
            "1 Solicitud dirigida a funcionario competente debidamente firmada, presentada por propietarios de los predios, grupos de moradores/poseedores de los predios, promotoores o empresarios privados.",
            "2 Documento que acredite la propiedad, posesión o documento que acredite el interés para desarrollar proyecto de renovación urbana según corresponda.",
            "3 Plano de ubicación de la microzona o zona del área de tratamiento.",
            "4 Documento técnico que sustente el estado tugurizado de los predios.",
            "5 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "1.4368% UIT",
        "plazo": "Evaluación Previa - 30 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Desarrollo Urbano y Territorial",
        "reconsideracion": "Gerente de Desarrollo Urbano y Territorial\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente Municipal\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
{
        "id": "133",
        "numero": "110",
        "procedimiento": "SOLICITUD EFECTUADA POR LOS MORADORES / POSEEDORES A FIN DE SER DECLARADOS APTOS PARA CONFORMAR UNA ASOCIACIÓN DE VIVIENDA",
        "sustento": "BASE LEGAL\n- Ley Nº 29415 (02.10.09). Art.18 Segundo Párrafo.\n- Decreto Supremo Nº 011-2010-VIVIENDA (30.10.10). Arts. 20.",
        "requisitos": [
            "1 Solicitud colectiva dirigida a funcionario competente presentada por los moradores/ poseedores de cada predio previamente empadronado en la Municipalidad, debidamente suscrita por cada uno de los solicitantes.",
            "2 Declaración jurada de cada uno de los moradores / poseedores manifestando su condición de encontrarse expedito para ser declarados aptos de conformar una asociación de vivienda con fines de Renovación Urbana.",
            "3 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "1.4368% UIT",
        "plazo": "Evaluación Previa - 30 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Desarrollo Urbano y Territorial",
        "reconsideracion": "Gerente de Desarrollo Urbano y Territorial\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente Municipal\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
    {
        "id": "134",
        "numero": "111",
        "procedimiento": "AUTORIZACIÓN PARA LA INSTALACIÓN DE INFRAESTRUCTURA NECESARIA PARA LA PRESTACION SE SERV. DE TELECOMUNICACIONES (NO INCLUYE NINGÚN TIPO DE CANALIZACIÓN SUBTERRÁNEA)",
        "sustento": "BASE LEGAL\n- Ley Orgánica de Municipalidades, Ley Nº 27972 (27.05.03). Art. 79.\n- Ley para la expansión de infraestructura en Telecomunicaciones, Ley Nº 29022 (20.05.07). Arts. 2, literal c, 5 y 7.\n- Reglamento de la Ley Nº 29022, Decreto Supremo Nº 039-2007-MTC (13.11.07). Arts. 4, 6, 11 y 12.\n- TUO de la Ley de Telecomunicaciones, Decreto Supremo Nº 013-93-TCC (06.05.93). Art. 33.\n- Decreto Legislativo que establece medidas para propiciar la inversión en materia de servicios públicos y obras públicas de infraestructura, Decreto Legislativo Nº 1014 (16.05.08).",
        "requisitos": [
            "1 Carta simple del Operador dirigida al titular de la entidad.",
            "2 Copia de la resolución emitida por el Ministerio mediante la cual se otorga concesión al Operador para prestar el servicio público de telecomunicaciones expedida por el Ministerio o en el caso de las empresas de valor añadido, de la resolución a que se refiere el artículo 33 del TUO de la Ley de Telecomunicaciones.",
            "3 De ser el caso memoria descriptiva y planos de ubicación detallando las características físicas y técnicas de las instalaciones materia de trámite, suscritos por un ingeniero civil y/o electrónico o de telecomunicaciones, según corresponda, ambos colegiados, adjuntando el certificado de inscripción y habilidad vigentes expedido por el Colegio de Ingenieros del Perú.",
            "4 Cronograma de avance de obra.",
            "5 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "7.3368% UIT",
        "plazo": "Evaluación Previa - 30 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Desarrollo Urbano y Territorial",
        "reconsideracion": "Gerente de Desarrollo Urbano y Territorial\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente Municipal\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
{
        "id": "133",
        "numero": "110",
        "procedimiento": "SOLICITUD EFECTUADA POR LOS MORADORES / POSEEDORES A FIN DE SER DECLARADOS APTOS PARA CONFORMAR UNA ASOCIACIÓN DE VIVIENDA",
        "sustento": "BASE LEGAL\n- Ley Nº 29415 (02.10.09). Art.18 Segundo Párrafo.\n- Decreto Supremo Nº 011-2010-VIVIENDA (30.10.10). Arts. 20.",
        "requisitos": [
            "1 Solicitud colectiva dirigida a funcionario competente presentada por los moradores/ poseedores de cada predio previamente empadronado en la Municipalidad, debidamente suscrita por cada uno de los solicitantes.",
            "2 Declaración jurada de cada uno de los moradores / poseedores manifestando su condición de encontrarse expedito para ser declarados aptos de conformar una asociación de vivienda con fines de Renovación Urbana.",
            "3 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "1.4368% UIT",
        "plazo": "Evaluación Previa - 30 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Desarrollo Urbano y Territorial",
        "reconsideracion": "Gerente de Desarrollo Urbano y Territorial\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente Municipal\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
    {
        "id": "134",
        "numero": "111",
        "procedimiento": "AUTORIZACIÓN PARA LA INSTALACIÓN DE INFRAESTRUCTURA NECESARIA PARA LA PRESTACION SE SERV. DE TELECOMUNICACIONES (NO INCLUYE NINGÚN TIPO DE CANALIZACIÓN SUBTERRÁNEA)",
        "sustento": "BASE LEGAL\n- Ley Orgánica de Municipalidades, Ley Nº 27972 (27.05.03). Art. 79.\n- Ley para la expansión de infraestructura en Telecomunicaciones, Ley Nº 29022 (20.05.07). Arts. 2, literal c, 5 y 7.\n- Reglamento de la Ley Nº 29022, Decreto Supremo Nº 039-2007-MTC (13.11.07). Arts. 4, 6, 11 y 12.\n- TUO de la Ley de Telecomunicaciones, Decreto Supremo Nº 013-93-TCC (06.05.93). Art. 33.\n- Decreto Legislativo que establece medidas para propiciar la inversión en materia de servicios públicos y obras públicas de infraestructura, Decreto Legislativo Nº 1014 (16.05.08).",
        "requisitos": [
            "1 Carta simple del Operador dirigida al titular de la entidad.",
            "2 Copia de la resolución emitida por el Ministerio mediante la cual se otorga concesión al Operador para prestar el servicio público de telecomunicaciones expedida por el Ministerio o en el caso de las empresas de valor añadido, de la resolución a que se refiere el artículo 33 del TUO de la Ley de Telecomunicaciones.",
            "3 De ser el caso memoria descriptiva y planos de ubicación detallando las características físicas y técnicas de las instalaciones materia de trámite, suscritos por un ingeniero civil y/o electrónico o de telecomunicaciones, según corresponda, ambos colegiados, adjuntando el certificado de inscripción y habilidad vigentes expedido por el Colegio de Ingenieros del Perú.",
            "4 Cronograma de avance de obra.",
            "5 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "7.3368% UIT",
        "plazo": "Evaluación Previa - 30 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Desarrollo Urbano y Territorial",
        "reconsideracion": "Gerente de Desarrollo Urbano y Territorial\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente Municipal\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
{
        "id": "135",
        "numero": "112",
        "procedimiento": "AUTORIZACIÓN PARA AMPLIACIÓN DE REDES SUBTERRÁNEAS O CASOS ESPECIALES EN ÁREA DE USO PÚBLICO (TELECOMUNICACIONES)",
        "sustento": "BASE LEGAL\n- Ley Orgánica de Municipalidades, Ley Nº 27972 (27.05.03). Art. 79.\n- Ley para la expansión de infraestructura en Telecomunicaciones, Ley Nº 29022 (20.05.07). Arts. 2, literal c, 5 y 7.\n- Reglamento de la Ley Nº 29022, Decreto Supremo Nº 039-2007-MTC (13.11.07). Arts. 4, 6, 11 y 12.\n- TUO de la Ley de Telecomunicaciones, Decreto Supremo Nº 013-93-TCC (06.05.93). Art. 33.\n- Decreto Legislativo que establece medidas para propiciar la inversión en materia de servicios públicos y obras públicas de infraestructura, Decreto Legislativo Nº 1014 (16.05.08).",
        "requisitos": [
            "1 Carta simple del Operador dirigida al titular de la entidad.",
            "2 Copia de la resolución emitida por el Ministerio mediante la cual se otorga concesión al Operador para prestar el servicio público de telecomunicaciones expedida por el Ministerio o en el caso de las empresas de valor añadido, de la resolución a que se refiere el artículo 33 del TUO de la Ley de Telecomunicaciones.",
            "3 De ser el caso memoria descriptiva y planos de ubicación detallando las características físicas y técnicas de las instalaciones materia de trámite, suscritos por un ingeniero civil y/o electrónico o de telecomunicaciones, según corresponda, ambos colegiados, adjuntando el certificado de inscripción y habilidad vigentes expedido por el Colegio de Ingenieros del Perú",
            "4 Cronograma de avance de obra.",
            "5 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "5.4895% UIT",
        "plazo": "Evaluación Previa - 30 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Desarrollo Urbano y Territorial",
        "reconsideracion": "Gerente de Desarrollo Urbano y Territorial\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente Municipal\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
    {
        "id": "136",
        "numero": "113",
        "procedimiento": "AUTORIZACIÓN PARA INSTALACIÓN DE CABINAS TELEFÓNICAS EN ÁREA DE USO PÚBLICO (NO INCLUYE NINGÚN TIPO DE CANALIZACIÓN SUBTERRÁNEA)",
        "sustento": "BASE LEGAL\n- Ley Orgánica de Municipalidades, Ley Nº 27972 (27.05.03). Art. 79.\n- Ley para la expansión de infraestructura en Telecomunicaciones, Ley Nº 29022 (20.05.07). Arts. 2, literal c, 5 y 7.\n- Reglamento de la Ley Nº 29022, Decreto Supremo Nº 039-2007-MTC (13.11.07). Arts. 4, 6, 11 y 12.\n- TUO de la Ley de Telecomunicaciones, Decreto Supremo Nº 013-93-TCC (06.05.93). Art. 33.\n- Decreto Legislativo que establece medidas para propiciar la inversión en materia de servicios públicos y obras públicas de infraestructura, Decreto Legislativo Nº 1014 (16.05.08).",
        "requisitos": [
            "1 Carta simple del Operador dirigida al titular de la entidad.",
            "2 Copia de la resolución emitida por el Ministerio mediante la cual se otorga concesión al Operador para prestar el servicio público de telecomunicaciones expedida por el Ministerio o en el caso de las empresas de valor añadido, de la resolución a que se refiere el artículo 33 del TUO de la Ley de Telecomunicaciones.",
            "3 De ser el caso memoria descriptiva y planos de ubicación detallando las características físicas y técnicas de las instalaciones materia de trámite, suscritos por un ingeniero civil y/o electrónico o de telecomunicaciones, según corresponda, ambos colegiados, adjuntando el certificado de inscripción y habilidad vigentes expedido por el Colegio de Ingenieros del Perú",
            "4 Cronograma de avance de obra.",
            "5 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "4.1763% UIT",
        "plazo": "Evaluación Previa - 30 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Desarrollo Urbano y Territorial",
        "reconsideracion": "Gerente de Desarrollo Urbano y Territorial\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente Municipal\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
{
        "id": "137",
        "numero": "114",
        "procedimiento": "AUTORIZACIÓN PARA LA CONSTRUCCIÓN DE CÁMARA SUBTERRÁNEA EN ÁREA DE USO PÚBLICO (TELECOMUNICACIONES)",
        "sustento": "BASE LEGAL\n- Ley Orgánica de Municipalidades, Ley Nº 27972 (27.05.03). Art. 79.\n- Ley para la expansión de infraestructura en Telecomunicaciones, Ley Nº 29022 (20.05.07). Arts. 2, literal c, 5 y 7.\n- Reglamento de la Ley Nº 29022, Decreto Supremo Nº 039-2007-MTC (13.11.07). Arts. 4, 6, 11 y 12.\n- TUO de la Ley de Telecomunicaciones, Decreto Supremo Nº 013-93-TCC (06.05.93). Art. 33.\n- Decreto Legislativo que establece medidas para propiciar la inversión en materia de servicios públicos y obras públicas de infraestructura, Decreto Legislativo Nº 1014 (16.05.08).",
        "requisitos": [
            "1 Carta simple del Operador dirigida al titular de la entidad.",
            "2 Copia de la resolución emitida por el Ministerio mediante la cual se otorga concesión al Operador para prestar el servicio público de telecomunicaciones expedida por el Ministerio o en el caso de las empresas de valor añadido, de la resolución a que se refiere el artículo 33 del TUO de la Ley de Telecomunicaciones.",
            "3 De ser el caso memoria descriptiva y planos de ubicación detallando las características físicas y técnicas de las instalaciones materia de trámite, suscritos por un ingeniero civil y/o electrónico o de telecomunicaciones, según corresponda, ambos colegiados, adjuntando el certificado de inscripción y habilidad vigentes expedido por el Colegio de Ingenieros del Perú.",
            "4 Cronograma de avance de obra.",
            "5 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "4.1763% UIT",
        "plazo": "Evaluación Previa - 30 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Desarrollo Urbano y Territorial",
        "reconsideracion": "Gerente de Desarrollo Urbano y Territorial\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente Municipal\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
    {
        "id": "138",
        "numero": "115",
        "procedimiento": "AUTORIZACIÓN PARA CONSTRUCCIÓN Y/O REFACCIÓN DE SARDINELES Y VEREDAS EN ÁREA DE USO PÚBLICO",
        "sustento": "BASE LEGAL\n- Ley Orgánica de Municipalidades, Ley Nº 27972 (27.05.03). Art. 79.\n- Ley del Procedimiento Administrativo General, Ley Nº 27444 y modificatorias (11.04.01). Art. 35.",
        "requisitos": [
            "1 Solicitud simple dirigida al titular de la entidad.",
            "2 Plano general de planta a escala 1:100 ó 1:50.",
            "3 Memoria descriptiva.",
            "4 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "2.0289% UIT",
        "plazo": "Evaluación Previa - 30 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Desarrollo Urbano y Territorial",
        "reconsideracion": "Gerente de Desarrollo Urbano y Territorial\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente Municipal\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
    {
        "id": "139",
        "numero": "116",
        "procedimiento": "AUTORIZACIÓN PARA CONSTRUCCIÓN DE BUZONES DE DESAGUE EN ÁREA DE USO PÚBLICO (REDES PRINCIPALES)",
        "sustento": "BASE LEGAL\n- Ley Orgánica de Municipalidades, Ley Nº 27972 (27.05.03). Art. 79.\n- Decreto Legislativo que establece medidas para propiciar la inversión en materia de servicios públicos y obras públicas de infraestructura, Decreto Legislativo Nº 1014 (16.05.08). Art. 5.",
        "requisitos": [
            "1 Solicitud simple dirigida al titular de la entidad.",
            "2 Planos de ubicación y planta detallando características físicas y técnicas (firmado por ingeniero civil y sanitario) aprobadas por la empresa concesionaria del servicio público.",
            "3 Certificado de inscripción y habilidad vigente expedido por el Colegio de Ingenieros del Perú.",
            "4 Memoria descriptiva.",
            "5 Cronograma de avance de obra.",
            "6 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "2.9263% UIT",
        "plazo": "Evaluación Previa - 30 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Desarrollo Urbano y Territorial",
        "reconsideracion": "Gerente de Desarrollo Urbano y Territorial\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente Municipal\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
{
        "id": "140",
        "numero": "117",
        "procedimiento": "AUTORIZACIÓN EN ÁREA DE USO PÚBLICO PARA INSTALACIÓN DOMICILIARIA DEL SERVICIO DE AGUA, DESAGUE, ENERGÍA ELÉCTRICA Y TELECOMUNICACIONES",
        "sustento": "BASE LEGAL\n- Ley Orgánica de Municipalidades, Ley Nº 27972 (27.05.03). Art. 79.\n- Decreto Legislativo que establece medidas para propiciar la inversión en materia de servicios públicos y obras públicas de infraestructura, Decreto Legislativo Nº 1014 (16.05.08). Arts. 4 y 5.\n- Ley para la expansión de infraestructura en Telecomunicaciones, Ley Nº 29022 (20.05.07).\n- Reglamento de la Ley Nº 29022, Decreto Supremo Nº 039-2007-MTC (13.11.07).",
        "requisitos": [
            "1 Solicitud simple dirigida al titular de la entidad.",
            "2 Planos de ubicación y planta detallando características físicas y técnicas.",
            "3 Memoria descriptiva.",
            "4 Cronograma de avance de obra.",
            "5 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "0.9500% UIT",
        "plazo": "Evaluación Previa - 30 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Desarrollo Urbano y Territorial",
        "reconsideracion": "Gerente de Desarrollo Urbano y Territorial\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente Municipal\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
    {
        "id": "141",
        "numero": "118",
        "procedimiento": "AUTORIZACIÓN PARA REUBICACIÓN Y/O CAMBIO DE POSTES, ANCLAJE EN ÁREA DE USO PÚBLICO PARA EL SERVICIO DE TELECOMUNICACIONES",
        "sustento": "BASE LEGAL\n- Ley Orgánica de Municipalidades, Ley Nº 27972 (27.05.03). Art. 79.\n- Ley para la expansión de infraestructura en Telecomunicaciones, Ley Nº 29022 (20.05.07). Arts. 2, literal c, 5 y 7.\n- Reglamento de la Ley Nº 29022, Decreto Supremo Nº 039-2007-MTC (13.11.07). Arts. 4, 6, 11 y 12.\n- TUO de la Ley de Telecomunicaciones, Decreto Supremo Nº 013-93-TCC (06.05.93). Art. 33.\n- Decreto Legislativo que establece medidas para propiciar la inversión en materia de servicios públicos y obras públicas de infraestructura, Decreto Legislativo Nº 1014 (16.05.08).",
        "requisitos": [
            "1 Carta simple del Operador dirigida al titular de la entidad.",
            "2 Copia de la resolución emitida por el Ministerio mediante la cual se otorga concesión al Operador para prestar el servicio público de telecomunicaciones expedida por el Ministerio o en el caso de las empresas de valor añadido, de la resolución a que se refiere el artículo 33 del TUO de la Ley de Telecomunicaciones.",
            "3 De ser el caso memoria descriptiva y planos de ubicación detallando las características físicas y técnicas de las instalaciones materia de trámite, suscritos por un ingeniero civil y/u electrónico o de telecomunicaciones, según corresponda, ambos colegiados, adjuntando el certificado de inscripción y habilidad vigentes expedido por el Colegio de Ingenieros del Perú.",
            "4 Cronograma de avance de obra.",
            "5 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "5.7605% UIT",
        "plazo": "Evaluación Previa - 30 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Desarrollo Urbano y Territorial",
        "reconsideracion": "Gerente de Desarrollo Urbano y Territorial\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente Municipal\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
{
        "id": "142",
        "numero": "119",
        "procedimiento": "AUTORIZACIÓN PARA MANTENIMIENTO DE CABLEADO AÉREO DE TELECOMUNICACIONES EXISTENTE EN AREA DE USO PUBLICO",
        "sustento": "BASE LEGAL\n- Ley Orgánica de Municipalidades, Ley Nº 27972 (27.05.03). Art. 79.\n- Ley para la expansión de infraestructura en Telecomunicaciones, Ley Nº 29022 (20.05.07). Arts. 2, literal c, 5 y 7.\n- Reglamento de la Ley Nº 29022, Decreto Supremo Nº 039-2007-MTC (13.11.07). Arts. 4, 6, 11 y 12.\n- TUO de la Ley de Telecomunicaciones, Decreto Supremo Nº 013-93-TCC (06.05.93). Art. 33.\n- Decreto Legislativo que establece medidas para propiciar la inversión en materia de servicios públicos y obras públicas de infraestructura, Decreto Legislativo Nº 1014 (16.05.08).",
        "requisitos": [
            "1 Carta simple del Operador dirigida al titular de la entidad.",
            "2 Copia de la resolución emitida por el Ministerio mediante la cual se otorga concesión al Operador para prestar el servicio público de telecomunicaciones expedida por el Ministerio o en el caso de las empresas de valor añadido, de la resolución a que se refiere el artículo 33 del TUO de la Ley de Telecomunicaciones.",
            "3 De ser el caso memoria descriptiva y planos de ubicación detallando las características físicas y técnicas de las instalaciones materia de trámite, suscritos por un ingeniero civil y/o electrónico o de telecomunicaciones, según corresponda, ambos colegiados, adjuntando el certificado de inscripción y habilidad vigentes expedido por el Colegio de Ingenieros del Perú.",
            "4 Cronograma de avance de obra.",
            "5 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "4.1816% UIT",
        "plazo": "Evaluación Previa - 30 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Desarrollo Urbano y Territorial",
        "reconsideracion": "Gerente de Desarrollo Urbano y Territorial\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente Municipal\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
    {
        "id": "143",
        "numero": "120",
        "procedimiento": "AUTORIZACIÓN PARA LA OCUPACIÓN DE ÁREA DE USO PÚBLICO CON CERCO DE OBRAS PARA MATERIALES DE CONSTRUCCIÓN E INSTALACIONES PROVISIONALES DE CASETAS U OTRAS",
        "sustento": "BASE LEGAL\n- Ley Orgánica de Municipalidades, Ley Nº 27972 (27.05.03). Art. 79.\n- Decreto Legislativo que establece medidas para propiciar la inversión en materia de servicios públicos y obras públicas de infraestructura, Decreto Legislativo Nº 1014 (16.05.08).",
        "requisitos": [
            "1 Solicitud simple dirigida al titular de la entidad.",
            "2 Planos de ubicación y planta detallando características físicas y técnicas (firmado por ingeniero civil, electricista o de telecomunicaciones).",
            "3 Memoria descriptiva.",
            "4 Copia simple de la Licencia de Obra.",
            "5 Cronograma de avance de obra.",
            "6 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "2.4842% UIT",
        "plazo": "Evaluación Previa - 30 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Desarrollo Urbano y Territorial",
        "reconsideracion": "Gerente de Desarrollo Urbano y Territorial\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente Municipal\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
{
        "id": "144",
        "numero": "121",
        "procedimiento": "CERTIFICADO DE CONFORMIDAD DE OBRA VINCULADO A LOS SERVICIOS PÚBLICOS DE TELECOMUNICACIONES Y/O ELÉCTRICOS",
        "sustento": "BASE LEGAL\n- Ley Orgánica de Municipalidades, Ley Nº 27972 (27.05.03). Art. 79.\n- Ley para la expansión de infraestructura en Telecomunicaciones, Ley Nº 29022 (20.05.07). Art. 5.\n- Reglamento de la Ley Nº 29022, Decreto Supremo Nº 039-2007-MTC (13.11.07). Art. 14.",
        "requisitos": [
            "1 Solicitud dirigida al titular de la entidad.",
            "2 Certificado de calidad de obra (original o copia visado por fedatario de la Municipalidad).",
            "3 Plano de ubicación y planta detallando características físicas y técnicas del área a ocupar (firmado por profesional correspondiente y sólo cuando se ha variado la obra)",
            "4 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "4.7158% UIT",
        "plazo": "Evaluación Previa - 30 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Desarrollo Urbano y Territorial",
        "reconsideracion": "Gerente de Desarrollo Urbano y Territorial\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente Municipal\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
    {
        "id": "145",
        "numero": "122",
        "procedimiento": "AUTORIZACIÓN PARA LA REMODELACIÓN DEL ÁREA DE USO PÚBLICO (SARDINELES, BERMAS, JARDINES DE AISLAMIENTOS Y OTROS)",
        "sustento": "BASE LEGAL\n- Ley Orgánica de Municipalidades, Ley Nº 27972 (27.05.03). Art. 79.\n- Decreto Legislativo que establece medidas para propiciar la inversión en materia de servicios públicos y obras públicas de infraestructura, Decreto Legislativo Nº 1014 (16.05.08).",
        "requisitos": [
            "1 Solicitud simple dirigida al titular de la entidad.",
            "2 Planos de ubicación y planta detallando características físicas y técnicas del área a remodelar (firmado por ingeniero civil o arquitecto).",
            "3 Memoria descriptiva.",
            "4 Cronograma de avance de obra.",
            "5 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "1.7263% UIT",
        "plazo": "Evaluación Previa - 30 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Desarrollo Urbano y Territorial",
        "reconsideracion": "Gerente de Desarrollo Urbano y Territorial\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente Municipal\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
    {
        "id": "146",
        "numero": "123",
        "procedimiento": "AMPLIACIÓN DE AUTORIZACIÓN EN ÁREA DE USO PÚBLICO DE INSTALACIÓN DE REDES DE TELECOMUNICACIONES",
        "sustento": "BASE LEGAL\n- Ley Orgánica de Municipalidades, Ley Nº 27972 (27.05.03). Art. 79.\n- Ley para la expansión de infraestructura en Telecomunicaciones, Ley Nº 29022 (20.05.07). Arts. 2, literal c, 5 y 7.\n- Reglamento de la Ley Nº 29022, Decreto Supremo Nº 039-2007-MTC (13.11.07). Arts. 4, 6 y 11.",
        "requisitos": [
            "1 Carta simple del Operador dirigida al titular de la entidad.",
            "2 Cronograma de avance de obra.",
            "3 Plano general indicando ubicación, detallando características físicas y técnicas (firmado por profesional indicando saldo de obra).",
            "4 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "2.2237% UIT",
        "plazo": "Evaluación Previa - 30 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Desarrollo Urbano y Territorial",
        "reconsideracion": "Gerente de Desarrollo Urbano y Territorial\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente Municipal\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
{
        "id": "147",
        "numero": "124",
        "procedimiento": "AUTORIZACIÓN PARA INSTALACIÓN DE CABLEADO SUBTERRÁNEO (REDES DE TELECOMUNICACIONES, NO INCLUYE NINGÚN TIPO DE CANALIZACIÓN SUBTERRÁNEA)",
        "sustento": "BASE LEGAL\n- Ley Orgánica de Municipalidades, Ley Nº 27972 (27.05.03). Art. 79.\n- Ley para la expansión de infraestructura en Telecomunicaciones, Ley Nº 29022 (20.05.07). Arts. 2, literal c, 5 y 7.\n- Reglamento de la Ley Nº 29022, Decreto Supremo Nº 039-2007-MTC (13.11.07). Arts. 4, 6, 11 y 12.\n- TUO de la Ley de Telecomunicaciones, Decreto Supremo Nº 013-93-TCC (06.05.93). Art. 33.\n- Decreto Legislativo que establece medidas para propiciar la inversión en materia de servicios públicos y obras públicas de infraestructura, Decreto Legislativo Nº 1014 (16.05.08).",
        "requisitos": [
            "1 Carta simple del Operador dirigida al titular de la entidad.",
            "2 Copia de la resolución emitida por el Ministerio mediante la cual se otorga concesión al Operador para prestar el servicio público de telecomunicaciones expedida por el Ministerio o en el caso de las empresas de valor añadido, de la resolución a que se refiere el artículo 33 del TUO de la Ley de Telecomunicaciones.",
            "3 De ser el caso memoria descriptiva y planos de ubicación detallando las características físicas y técnicas de las instalaciones materia de trámite, suscritos por un ingeniero civil y/o electrónico o de telecomunicaciones, según corresponda, ambos colegiados, adjuntando el certificado de inscripción y habilidad vigentes expedido por el Colegio de Ingenieros del Perú.",
            "4 Cronograma de avance de obra.",
            "5 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "5.7605% UIT",
        "plazo": "Evaluación Previa - 30 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Desarrollo Urbano y Territorial",
        "reconsideracion": "Gerente de Desarrollo Urbano y Territorial\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente Municipal\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
    {
        "id": "148",
        "numero": "125",
        "procedimiento": "AUTORIZACIÓN PARA AMPLIACIÓN DE REDES SUBTERRÁNEAS O CASOS ESPECIALES EN ÁREA DE USO PÚBLICO NO VINCULADOS CON TELECOMUNICACIONES (AGUA, DESAGUE, ENERGÍA ELÉCTRICA, ETC)",
        "sustento": "BASE LEGAL\n- Ley Orgánica de Municipalidades, Ley Nº 27972 (27.05.03). Art. 79.\n- Decreto Legislativo que establece medidas para propiciar la inversión en materia de servicios públicos y obras públicas de infraestructura, Decreto Legislativo Nº 1014 (16.05.08). Art. 5.\n- TUO del Reglamento de Distribución del Gas Natural por Red de Ductos, Decreto Supremo Nº 040-2008-EM (22.07.08).\n- Ley de Concesiones Eléctricas, Ley Nº 25844 (19.11.92).\n- Ley General de Servicios de Saneamiento, Ley Nº 26338 (24.07.94).",
        "requisitos": [
            "1 Solicitud simple dirigida al titular de la entidad.",
            "2 Memoria descriptiva.",
            "3 Planos de ubicación y planta detallando características físicas y técnicas de las instalaciones (firmado por el profesional correspondiente).",
            "4 Certificado de inscripción y habilidad vigentes (expedido por el Colegio de Ingenieros del Perú).",
            "5 Cronograma de avance de obra.",
            "6 Pago por el Derecho de la Tasa Administrativa:",
            "--------------------------------------------------",
            "📌 NOTAS PARA EL CIUDADANO:",
            "No incluye instalaciones domiciliarias."
        ],
        "derecho_tramite": "5.7605% UIT",
        "plazo": "Evaluación Previa - 30 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Desarrollo Urbano y Territorial",
        "reconsideracion": "Gerente de Desarrollo Urbano y Territorial\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente Municipal\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
{
        "id": "149",
        "numero": "126",
        "procedimiento": "AMPLIACIÓN DE AUTORIZACIÓN PARA AMPLIACIÓN DE REDES SUBTERRÁNEAS O CASOS ESPECIALES EN ÁREA DE USO PÚBLICO NO VINCULADOS CON TELECOMUNICACIONES (AGUA, DESAGUE, ENERGÍA ELÉCTRICA, ETC)",
        "sustento": "BASE LEGAL\n- Ley Orgánica de Municipalidades, Ley Nº 27972 (27.05.03). Art. 79.\n- Decreto Legislativo que establece medidas para propiciar la inversión en materia de servicios públicos y obras públicas de infraestructura, Decreto Legislativo Nº 1014 (16.05.08). Art. 5.\n- TUO del Reglamento de Distribución del Gas Natural por Red de Ductos, Decreto Supremo Nº 040-2008-EM (22.07.08).\n- Ley de Concesiones Eléctricas, Ley Nº 25844 (19.11.92).\n- Ley General de Servicios de Saneamiento, Ley Nº 26338 (24.07.94).",
        "requisitos": [
            "1 Solicitud simple dirigida al titular de la entidad.",
            "2 Cronograma de avance de obra.",
            "3 Plano general indicando ubicación, detallando características físicas y técnicas (firmado por profesional indicando saldo de obra).",
            "4 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "4.7105% UIT",
        "plazo": "Evaluación Previa - 30 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Desarrollo Urbano y Territorial",
        "reconsideracion": "Gerente de Desarrollo Urbano y Territorial\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente Municipal\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
    {
        "id": "150",
        "numero": "127",
        "procedimiento": "CERTIFICADO DE CONFORMIDAD DE OBRA EN ÁREA DE USO PÚBLICO",
        "sustento": "BASE LEGAL\n- Ley Orgánica de Municipalidades, Ley Nº 27972 (27.05.03). Art. 79.\n- TUO de la Ley de Tributación Municipal, Decreto Supremo Nº 156-2004-EF y modificatorias (15.11.04). Art. 67.",
        "requisitos": [
            "1 Solicitud simple dirigida al titular de la entidad.",
            "2 Certificado de calidad de obra (original o copia visado por fedatario de la Municipalidad).",
            "3 Planos de ubicación y planta detallando características físicas y técnicas del área a ocupar (firmado por profesional correspondiente y sólo cuando se ha variado la obra)."
        ],
        "derecho_tramite": "GRATUITO",
        "plazo": "Evaluación Previa - 30 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Desarrollo Urbano y Territorial",
        "reconsideracion": "Gerente de Desarrollo Urbano y Territorial\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente Municipal\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
{
        "id": "151",
        "numero": "128",
        "procedimiento": "INSPECCIÓN OCULAR EN ÁREA DE USO PÚBLICO A SOLICITUD DE PARTE",
        "sustento": "BASE LEGAL\n- Ley Orgánica de Municipalidades, Ley Nº 27972 (27.05.03). Art. 79.",
        "requisitos": [
            "1 Solicitud simple dirigida al titular de la entidad.",
            "2 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "2.2500% UIT",
        "plazo": "Automático",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Desarrollo Urbano y Territorial",
        "reconsideracion": "",
        "apelacion": ""
    },
    {
        "id": "152",
        "numero": "129",
        "procedimiento": "RESELLADOS O AUTENTICACIÓN DE COPIA DE PLANOS APROBADOS",
        "sustento": "BASE LEGAL\n- Ley Orgánica de Municipalidades, Ley Nº 27972 (27.05.03). Art. 79.\n- Reglamento de Licencias de Habilitación Urbana y Licencias de Edificación, Decreto Supremo Nº 024-2008-VIVIENDA y modificatorias (27.09.08). Arts. 48, 58 y 61.",
        "requisitos": [
            "1 Solicitud dirigida a funcionario compente.",
            "2 Pago por el Derecho de la Tasa Administrativa:",
            "--------------------------------------------------",
            "📌 NOTAS PARA EL CIUDADANO:",
            "La primera copia de los planos es autenticada de forma gratuita."
        ],
        "derecho_tramite": "1.1474% UIT",
        "plazo": "Automático",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Desarrollo Urbano y Territorial",
        "reconsideracion": "",
        "apelacion": ""
    },
    {
        "id": "153",
        "numero": "130",
        "procedimiento": "CERTIFICADO DE HABITABILIDAD",
        "sustento": "BASE LEGAL\n- Ley Nº 27972 (27.05.03). Arts. 40 y 79 numeral 3.3.\n- Ley Nº 27444 (11.04.01). Arts. 34, 35, 44 y 45.\n- Ley Nº 29060 (07.07.07).\n- Decreto Supremo Nº 156-2004-EF (15.11.04). Art. 68.\n- Ley Nº 28294 (21.07.04). Art. 21.\n- Decreto Supremo Nº 005-2006-JUS",
        "requisitos": [
            "1 Formato de solicitud (distribución gratuita o de libre reproducción). Se debe incluir datos del predio.",
            "2 Copia simple del documento (DNI/CE) del titular.",
            "3 De actuar como representante, adjuntar carta poder vigente (persona natural, poder simple y persona jurídica, copia fedateada del poder notarial) y copia simple de su documento (DNI/CE).",
            "4 Copia fedateada de la ficha registral del predio, en caso de no estar registrado el predio a nombre del titular, documento que acredite la propiedad.",
            "5 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "1.1447% UIT",
        "plazo": "Automático",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Desarrollo Urbano y Territorial",
        "reconsideracion": "",
        "apelacion": ""
    },
    {
        "id": "154",
        "numero": "131",
        "procedimiento": "PLANO CATASTRAL (VISADO)",
        "sustento": "BASE LEGAL\n- Ley Nº 27972 (27.05.03). Arts. 40 y 79 numeral 3.3.\n- Ley Nº 27444 (11.04.01). Arts. 34, 35, 44 y 45.\n- Ley Nº 29060 (07.07.07).\n- Decreto Supremo Nº 156-2004-EF (15.11.04). Art. 68.\n- Ley Nº 28294 (21.07.04). Art. 21.\n- Decreto Supremo Nº 005-2006-JUS (12.02.08). Art. 3 literales f) y j).",
        "requisitos": [
            "1 Formato de solicitud (distribución gratuita o de libre reproducción). Se debe incluir datos del predio, respecto del cual se solicita el plano.",
            "2 Copia simple del documento (DNI/CE) del titular.",
            "3 De actuar como representante, adjuntar carta poder vigente (persona natural, poder simple y persona jurídica, copia fedateada del poder notarial) y copia simple de su documento (DNI/CE).",
            "4 Copia fedateada de la ficha registral del predio, en caso de no estar registrado el predio a nombre del titular, documento que acredite la propiedad.",
            "5 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "0.9316% UIT",
        "plazo": "Automático",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Desarrollo Urbano y Territorial",
        "reconsideracion": "",
        "apelacion": ""
    },
{
        "id": "151",
        "numero": "132",
        "procedimiento": "HOJA INFORMATIVA CATASTRAL",
        "sustento": "BASE LEGAL\n- Ley Nº 27972 (27.05.03). Arts. 40 y 79 numeral 3.3.\n- Ley Nº 27444 (11.04.01). Art. 34, 35, 44 y 45.\n- Ley Nº 29060 (07.07.07).\n- Decreto Supremo Nº 156-2004-EF (15.11.04). Art. 68.\n- Ley Nº 28294 (21.07.04). Art. 18.\n- Decreto Supremo Nº 005-2006-JUS (12.02.08). Arts. 3 literal f), 40 y 43.",
        "requisitos": [
            "1 Formato de solicitud (distribución gratuita o de libre reproducción), en el cual se debe indicar los datos del predio, respecto al cual se solicita la Hoja Informativa.",
            "2 Copia simple del documento (DNI/CE) del titular.",
            "3 De actuar como representante, adjuntar carta poder vigente (persona natural, poder simple y persona jurídica, copia fedateada del poder notarial) y copia simple de su documento (DNI/CE).",
            "4 Copia fedateada de la ficha registral del predio, en caso de no estar registrado el predio a nombre del titular, documento que acredite la propiedad.",
            "5 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "0.5237% UIT",
        "plazo": "Automático",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Desarrollo Urbano y Territorial",
        "reconsideracion": "",
        "apelacion": ""
    },
    {
        "id": "152",
        "numero": "133",
        "procedimiento": "CONSTANCIA DE FICHA CATASTRAL",
        "sustento": "BASE LEGAL\n- Ley Nº 27972 (27.05.03). Arts. 40 y 79 numeral 3.3.\n- Ley Nº 27444 (11.04.01). Art. 34, 35, 44 y 45.\n- Ley Nº 29060 (07.07.07).\n- Decreto Supremo Nº 156-2004-EF (15.11.04). Art. 68.\n- Ley Nº 28294 (21.07.04). Art. 15 numeral 1, y 18.\n- Decreto Supremo Nº 005-2006-JUS (12.02.08). Arts. 3 literal f) y 45.\n- Resolución Nº 001-2007-SNCP-CNC (16.07.07).",
        "requisitos": [
            "1 Formato de solicitud (distribución gratuita o de libre reproducción).",
            "2 Copia simple del documento (DNI/CE) del titular.",
            "3 De actuar como representante, adjuntar carta poder vigente (persona natural poder simple y persona jurídica, copia fedateada del poder notarial), y copia simple de su documento (DNI/CE).",
            "4 Copia fedateada de la ficha registral del predio, en caso de no estar registrado el predio a nombre del titular, documento que acredite la propiedad.",
            "5 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "0.7868% UIT",
        "plazo": "Automático",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Desarrollo Urbano y Territorial",
        "reconsideracion": "",
        "apelacion": ""
    },
    {
        "id": "153",
        "numero": "134",
        "procedimiento": "CONSTANCIA DE LINDEROS Y MEDIDAS PERIMÉTRICAS",
        "sustento": "BASE LEGAL\n- Ley Nº 27972 (27.05.03). Arts. 40 y 79 numeral 3.3.\n- Ley Nº 27444 (11.04.01). Art. 34, 35, 44 y 45.\n- Ley Nº 29060 (07.07.07).\n- Decreto Supremo Nº 156-2004-EF (15.11.04). Art. 68.\n- Ley Nº 28294 (21.07.04). Art. 15 numeral 1, y 18.\n- Decreto Supremo Nº 005-2006-JUS (12.02.08). Arts. 3 literal f), 40 y 41.",
        "requisitos": [
            "1 Formato de solicitud (distribución gratuita o de libre reproducción).",
            "2 Copia simple del documento (DNI/CE) del titular.",
            "3 De actuar como representante, adjuntar carta poder vigente (persona natural poder simple y persona jurídica, copia fedateada del poder notarial), y copia simple de su documento (DNI/CE).",
            "4 Plano único perimétrico con indicación de medidas y linderos que incluya ubicación y localización con coordenadas UTM 2 c/u.",
            "5 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "1.1816% UIT",
        "plazo": "Automático",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Desarrollo Urbano y Territorial",
        "reconsideracion": "",
        "apelacion": ""
    },
{
        "id": "154",
        "numero": "135",
        "procedimiento": "CERTIFICADO NEGATIVO CATASTRAL",
        "sustento": "BASE LEGAL\n- Ley Nº 27972 (27.05.03). Arts. 40 y 79 numeral 3.3.\n- Ley Nº 27444 (11.04.01). Art. 34, 35, 44 y 45.\n- Ley Nº 29060 (07.07.07).\n- Decreto Supremo Nº 156-2004-EF (15.11.04). Art. 68.\n- Ley Nº 28294 (21.07.04). Art. 15 numeral 1, y 18.\n- Decreto Supremo Nº 005-2006-JUS (12.02.08). Arts. 3 literal f) y 45.\n- Resolución Nº 001-2007-SNCP-CNC (16.07.07).",
        "requisitos": [
            "1 Formato de solicitud (distribución gratuita o de libre reproducción).",
            "2 Copia simple del documento (DNI/CE) del titular.",
            "3 De actuar como representante, adjuntar carta poder vigente (persona natural poder simple y persona jurídica, copia fedateada del poder notarial), y copia simple de su documento (DNI/CE).",
            "4 Copia fedateada de la ficha registral del predio, en caso de no estar registrado el predio a nombre del titular, documento que acredite la propiedad.",
            "5 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "1.2684% UIT",
        "plazo": "Automático",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Desarrollo Urbano y Territorial",
        "reconsideracion": "",
        "apelacion": ""
    },
    {
        "id": "155",
        "numero": "136",
        "procedimiento": "VISACIÓN DE PLANO Y MEMORIA DESCRIPTIVA CON FINES DE SANEAMIENTO",
        "sustento": "BASE LEGAL\n- Numeral 2 del Art. 505º del TUO del CPC, aprobado por RM 10-93-JUS (Pub. 23-04-1993)\n- Ley Nº 27444, Ley de Procedimiento Administrativo General (Pub. 11-04-2001)",
        "requisitos": [
            "1 Solicitud con carácter de Declaración Jurada, que incluye lo siguiente:",
            "1.1 - Nombres y Apellidos",
            "1.2 - Número del DNI",
            "1.3 - Domicilio",
            "2 Adjuntar copia del DNI o Carnte de Extranjería",
            "3 De actuar como representante, adjuntar carta poder vigente (persona natural poder simple y persona jurídica, copia fedateada del poder notarial), y copia simple de su documento (DNI/CE).",
            "4 Plano de Ubicación, Localización, Perimétrico suscrito por Profesional Habilitado (Arquitecto o Ingeniero Civil)",
            "5 Memoria descriptiva suscrita por Profesional Habilitado (Arquitecto o Ingeniero Civil)",
            "6 Copia fedateada que acredita la propiedad o posesión",
            "7 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "1.6921% UIT",
        "plazo": "Automático",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Desarrollo Urbano y Territorial",
        "reconsideracion": "",
        "apelacion": ""
    },
{
        "id": "156",
        "numero": "137",
        "procedimiento": "INSPECCIÓN TÉCNICA BÁSICA DE SEGURIDAD EN DEFENSA CIVIL EX POST HASTA 100 M2 Y CAPACIDAD DE ALMACENAMIENTO NO MAYOR A 30% DEL ÁREA TOTAL DEL LOCAL\n\nAPLICABLE, ENTRE OTROS, PARA:\n- CASO DE DENEGATORIA DE RENOVACIÓN DE CERTIFICADO A LOCAL QUE CUENTE CON LICENCIA DE FUNCIONAMIENTO\n- INSPECCIONES A MODULOS O STANDS QUE FORMEN PARTE DE GALERÍAS O MERCADOS AUTORIZADOS",
        "sustento": "BASE LEGAL\n- Ley Nº 27972 (27.05.03). Arts. 40 y 79 numeral 1.4.6.\n- Ley Nº 27444 (11.04.01). Arts. 34, 35, 44 y 45.\n- Ley Nº 29060 (07.07.07).\n- Decreto Supremo Nº 156-2004-EF (15.11.04). Art. 68.\n- Ley Nº 28976 (05.02.07). Art. 8 numeral 1.\n- Decreto Supremo Nº 066-2007-PCM (05.08.07). Arts. 1, 9 numeral 1, 18, 35, 39 y 10 ma. Disposición Complementaria y Final.\n- Manual para la Ejecución de Inspecciones Técnicas de Seguridad en Defensa Civil. Numeral 2.1.",
        "requisitos": [
            "1 Formato de solicitud (distribución gratuita o de libre reproducción) con carácter de Declaración Jurada.",
            "2 Declaración Jurada de Observancia de las condiciones de Seguridad, según aprobado por el Reglamento de Inspecciones.",
            "3 Pago por el Derecho de la Tasa Administrativa:",
            "--------------------------------------------------",
            "📌 NOTAS PARA EL CIUDADANO:",
            "- Corresponde a esta categoría los establecimientos de hasta 100 m2 y capacidad de almacenamiento no mayor del 30% del área total del local.",
            "- Se excluye de ésta categoría a los giros de pub - karaokes, licorerías, discotecas, bares, ferreterías, casinos, máquinas tragamonedas, juegos de azar o giros afines a los mismos; así como aquellos cuyo desarrollo implique el almacenamiento, uso o comercialización de productos tóxicos o cuyo desarrollo implique el almacenamiento, uso o comercialización de productos tóxicos o altamente inflamables.",
            "- De igual manera se excluye de esta categoría a aquellas edificaciones, instalaciones o recintos donde se utilicen, almacenen, fabriquen o comercialicen materiales y/o residuos peligrosos que representen riesgo para la población; así como aquellos que por la actividad que desarrollan pueden generar riesgo para la vida humana, patrimonio y el entorno.",
            "- También se excluyen aquellos giros que requieran de una ITSDC EX ANTE o de Detalle o Multidisciplinaria.",
            "- La vigencia del Certificado de Inspección Técnica de Seguridad en Defensa Civil se encuentra normado por el Manual de Ejecución de ITSDC aprobado mediante Directiva Nº 006-2003-INDECI/DNP/10.0 aprobado con R.J. Nº 067-2003-INDECI y modificado pf R.J. Nº 419-2004-INDECI y R.J. Nº 440-2005-INDECI."
        ],
        "derecho_tramite": "1.2000% UIT",
        "plazo": "Evaluación Previa - 7 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Sub Gerente de Defensa Civil",
        "reconsideracion": "Sub Gerente de Defensa Civil\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente de Desarrollo Urbano y Territorial\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
{
        "id": "157",
        "numero": "138",
        "procedimiento": "INSPECCIÓN TÉCNICA BÁSICA DE SEGURIDAD EN DEFENSA CIVIL EX ANTE MAYOR A 100 M2 HASTA 500 M2\n\nAPLICABLE, ENTRE OTROS, PARA:\n- CASO DE DENEGATORIA DE RENOVACIÓN DE CERTIFICADO A LOCAL QUE CUENTE CON LICENCIA DE FUNCIONAMIENTO\n- INSPECCIONES A MODULOS O STANDS QUE FORMEN PARTE DE GALERÍAS O MERCADOS AUTORIZADOS",
        "sustento": "BASE LEGAL\n- Ley Nº 27972 (27.05.03). Arts. 40 y 79 numeral 1.4.6.\n- Ley Nº 27444 (11.04.01). Arts. 34, 35, 44 y 45.\n- Ley Nº 29060 (07.07.07).\n- Decreto Supremo Nº 156-2004-EF (15.11.04). Art. 68.\n- Ley Nº 28976 (05.02.07). Art. 8 numeral 2.\n- Decreto Supremo Nº 066-2007-PCM (05.08.07). Arts. 1, 9 numeral 2, 18, 35, 39 y 10 ma. Disposición Complementaria y Final.\n- Manual para la Ejecución de Inspecciones Técnicas de Seguridad en Defensa Civil. Numeral 2.1.",
        "requisitos": [
            "1 Formato de solicitud (distribución gratuita o de libre reproducción) con carácter de Declaración Jurada.",
            "2 Cartilla de seguridad y/o plan de seguridad en Defensa Civil (incluye plano de Evacuación y circulación a escala 1/100, 1/200 ó 1/500.",
            "3 Plano de ubicación.",
            "4 Plano de distribución.",
            "5 Pago por el Derecho de la Tasa Administrativa:",
            "--------------------------------------------------",
            "📌 NOTAS PARA EL CIUDADANO:",
            "- Corresponden a ésta categoría las edificaciones, recintos o instalaciones de hasta dos niveles desde el nivel de terreno o calzada, con un área desde 101 m2 hasta 500 m2 , tales como:",
            "  Tiendas, stands, puestos, viviendas multifamiliares, pubs, karaoke, bares, licorerías, talleres mecánicos, establecimientos de hospedaje, restaurantes, cafeterías, edificación de salud, templos, bibliotecas, entre otros.",
            "  Instituciones Educativas Particulares, con las siguientes características: área menor o igual a 500 m2 y de hasta dos niveles desde el nivel de terreno o calzada, máximo 200 alumnos por turno.",
            "  Cabinas de Internet con un máximo de 20 computadoras.",
            "  Gimnasios con un área menor o igual a 500 m2 y que solo cuenten con máquinas mecánicas.",
            "  Agencias Bancarias, Oficinas Administrativas entre otras de evaluación similar con un área menor o igual a 500 m2 y que cuenten con un máximo de 20 computadoras.",
            "  Playas de Estacionamiento de un solo nivel sin techar; granjas, entre otros de similares características, cualquiera sea su área.",
            "  Licorerías, ferreterías con un área de hasta 500 m2.",
            "- Se excluye de ésta categoría a aquellas edificaciones, instalaciones o recintos donde se utilicen, almacenen, fabriquen o comercialicen materiales y/o residuos peligrosos que representen riesgo para la población; así como aquellos que por la actividad que desarrollan pueden generar riesgo para la vida humana, patrimonio y el entorno.",
            "- También se excluyen aquellos giros que requieran de una ITSDC EX ANTE o de Detalle o Multidisciplinaria.",
            "- La vigencia del Certificado de Inspección Técnica de Seguridad en Defensa Civil se encuentra normado por el Manual de Ejecución de ITSDC aprobado mediante Directiva Nº 006-2003-INDECI/DNP/10.0 aprobado con R.J. Nº 067-2003-INDECI y modificado pf R.J. Nº 419-2004-INDECI y R.J. Nº 440-2005-INDECI."
        ],
        "derecho_tramite": "4.1000% UIT",
        "plazo": "Evaluación Previa - 7 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Sub Gerente de Defensa Civil",
        "reconsideracion": "Sub Gerente de Defensa Civil\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente de Desarrollo Urbano y Territorial\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
{
        "id": "158",
        "numero": "139",
        "procedimiento": "RENOVACIÓN DEL CERTIFICADO DE INSPECCIÓN TÉCNICA BÁSICA DE SEGURIDAD EN DEFENSA CIVIL EX POST HASTA 100 M2 Y CAPACIDAD DE ALMACENAMIENTO NO MAYOR A 30% DEL ÁREA TOTAL DEL LOCAL",
        "sustento": "BASE LEGAL\n- Ley Nº 27972 (27.05.03). Arts. 40 y 79 numeral 1.4.6.\n- Ley Nº 27444 (11.04.01). Arts. 34, 35, 44 y 45.\n- Ley Nº 29060 (07.07.07).\n- Decreto Supremo Nº 156-2004-EF (15.11.04). Art. 68.\n- Ley Nº 28976 (05.02.07). Arts. 8 numerales 1 y 2, y 11 y 15.\n- Decreto Supremo Nº 066-2007-PCM (05.08.07). Arts. 1, 9 numeral 1, 18, 35, 38, 39, 40, 41 y 10ma. Disposición Complementaria y Final.\n- Manual para la Ejecución de Inspecciones Técnicas de Seguridad en Defensa Civil. Numeral 2.1.",
        "requisitos": [
            "1 Formulario Oficial de solicitud de renovación (distribución gratuita) que será entregado por el órgano ejecutante",
            "2 Declaración jurada de no haber realizado modificación alguna el objeto de inspección",
            "3 Cartilla de Seguridad, Plan de Seguridad en Defensa Civil o copia de Planes de Contingencia debidamente aprobados y actualizados, según corresponda",
            "4 Protocolos u otros documentos que hayan perdido vigencia y que forman parte del expediente en poder de la administración",
            "5 Pago por el Derecho de la Tasa Administrativa:",
            "--------------------------------------------------",
            "📌 NOTAS PARA EL CIUDADANO:",
            "El Artículo 41° del Decreto Supremo Nº 066-2007-PCM, establece que si en el procedimiento de renovación del Certificado de Inspección Técnica de seguridad en Defensa Civil, el órgano ejecutante de la ITSDC verifica que no se mantiene el cumplimiento de las normas de seguridad en materia de Defensa Civil, se emite el Informe Técnico correspondiente y se da por finalizado el procedimiento, debiendo el administrado tramitar una nueva inspección."
        ],
        "derecho_tramite": "1.4632% UIT",
        "plazo": "Evaluación Previa - 15 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Sub Gerente de Defensa Civil",
        "reconsideracion": "Sub Gerente de Defensa Civil\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente de Desarrollo Urbano y Territorial\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
{
        "id": "159",
        "numero": "140",
        "procedimiento": "RENOVACIÓN DEL CERTIFICADO DE INSPECCIÓN TÉCNICA BÁSICA DE SEGURIDAD EN DEFENSA CIVIL EX ANTE MAYOR A 100 M2 HASTA 500 M2",
        "sustento": "BASE LEGAL\n- Ley Nº 27972 (27.05.03). Arts. 40 y 79 numeral 1.4.6.\n- Ley Nº 27444 (11.04.01). Arts. 34, 35, 44 y 45.\n- Ley Nº 29060 (07.07.07).\n- Decreto Supremo Nº 156-2004-EF (15.11.04). Art. 68.\n- Ley Nº 28976 (05.02.07). Arts. 8 numerales 1 y 2, y 11 y 15.\n- Decreto Supremo Nº 066-2007-PCM (05.08.07). Arts. 1, 9 numeral 1, 18, 35, 38, 39, 40, 41 y 10ma. Disposición Complementaria y Final.\n- Manual para la Ejecución de Inspecciones Técnicas de Seguridad en Defensa Civil. Numeral 2.1.",
        "requisitos": [
            "1 Formulario Oficial de solicitud de renovación (distribución gratuita) que será entregado por el órgano ejecutante",
            "2 Declaración jurada de no haber realizado modificación alguna al objeto de inspección",
            "3 Cartilla de Seguridad, Plan de Seguridad en Defensa Civil o copia de Planes de Contingencia debidamente aprobados y actualizados, según corresponda",
            "4 Protocolos u otros documentos que hayan perdido vigencia y que forman parte del expediente en poder de la administración",
            "5 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "2.1158% UIT",
        "plazo": "Evaluación Previa - 15 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Sub Gerente de Defensa Civil",
        "reconsideracion": "Sub Gerente de Defensa Civil\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente de Desarrollo Urbano y Territorial\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
    {
        "id": "160",
        "numero": "141",
        "procedimiento": "LEVANTAMIENTO DE OBSERVACIONES EN LA INSPECCIÓN TÉCNICA BÁSICA DE SEGURIDAD EN DEFENSA CIVIL EX POST HASTA 100 M2 Y CAPACIDAD DE ALMACENAMIENTO NO MAYOR A 30% DEL ÁREA TOTAL DEL LOCAL",
        "sustento": "BASE LEGAL\n- Ley Nº 27972 (27.05.03). Arts. 40 y 79 numeral 1.4.6.\n- Ley Nº 27444 (11.04.01). Arts. 34, 35, 44 y 45.\n- Ley Nº 29060 (07.07.07).\n- Decreto Supremo Nº 156-2004-EF (15.11.04). Art. 68.\n- Ley Nº 28976 (05.02.07). Arts. 8 numerales 1 y 2, y 11 y 15.\n- Decreto Supremo Nº 066-2007-PCM (05.08.07). Arts. 1, 9 numeral 1, 18, 35, 38, 39, 40, 41 y 10ma. Disposición Complementaria y Final.\n- Manual para la Ejecución de Inspecciones Técnicas de Seguridad en Defensa Civil. Numeral 2.1.",
        "requisitos": [
            "1 Formulario Oficial de solicitud de levantamiento de observaciones (distribución gratuita) que será entregado por el órgano ejecutante",
            "2 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "0.8000% UIT",
        "plazo": "Evaluación Previa - 8 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Sub Gerente de Defensa Civil",
        "reconsideracion": "",
        "apelacion": ""
    },
{
        "id": "161",
        "numero": "142",
        "procedimiento": "LEVANTAMIENTO DE OBSERVACIONES EN LA INSPECCIÓN TÉCNICA BÁSICA DE SEGURIDAD EN DEFENSA CIVIL EX ANTE MAYOR A 100 M2 HASTA 500 M2",
        "sustento": "BASE LEGAL\n- Ley Nº 27972 (27.05.03). Arts. 40 y 79 numeral 1.4.6.\n- Ley Nº 27444 (11.04.01). Arts. 34, 35, 44 y 45.\n- Ley Nº 29060 (07.07.07).\n- Decreto Supremo Nº 156-2004-EF (15.11.04). Art. 68.\n- Ley Nº 28976 (05.02.07). Arts. 8 numerales 1 y 2, y 11 y 15.\n- Decreto Supremo Nº 066-2007-PCM (05.08.07). Arts. 1, 9 numeral 1, 18, 35, 38, 39, 40, 41 y 10ma. Disposición Complementaria y Final.\n- Manual para la Ejecución de Inspecciones Técnicas de Seguridad en Defensa Civil. Numeral 2.1.",
        "requisitos": [
            "1 Formulario Oficial de solicitud de levantamiento de observaciones (distribución gratuita) que será entregado por el órgano ejecutante",
            "2 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "2.2000% UIT",
        "plazo": "Evaluación Previa - 8 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Sub Gerente de Defensa Civil",
        "reconsideracion": "",
        "apelacion": ""
    },
    {
        "id": "162",
        "numero": "143",
        "procedimiento": "DUPLICADO DEL CERTIFICADO DE INSPECCIÓN TÉCNICA BÁSICA DE SEGURIDAD EN DEFENSA CIVIL",
        "sustento": "BASE LEGAL\n- Ley Nº 27972 (27.05.03). Arts. 40 y 79 numeral 1.4.6.\n- Ley Nº 27444 (11.04.01). Arts. 44, 45 y 160.\n- Decreto Supremo Nº 156-2004-EF (15.11.04) Art. 68.",
        "requisitos": [
            "1 Formato de solicitud (distribución gratuita o de libre reproducción), en el cual se debe indicar el número de certificado de Inspección Técnica cuyo duplicado se solicita",
            "2 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "0.8079% UIT",
        "plazo": "Automático",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Sub Gerente de Defensa Civil",
        "reconsideracion": "",
        "apelacion": ""
    },
{
        "id": "163",
        "numero": "144",
        "procedimiento": "ACCESO A LA INFORMACIÓN QUE POSEA O PRODUZCA LA MUNICIPALIDAD",
        "sustento": "BASE LEGAL\n- TUO de la Ley de Transparencia y Acceso a la Información Pública, Decreto Supremo Nº 043-2003-PCM (24.04.03). Art. 11.\n- Reglamento de la Ley de Transparencia y Acceso a la Información Pública, Decreto Supremo Nº 072-2003-PCM (07.08.03). Arts. 5 y 10.\n- Ley Nº 27444, (11.04.01)\n- Ley Nº 29060, (07.07.2007)\n- Ley Nº 27972, (25.05.2003)",
        "requisitos": [
            "1 Presentar Formato de Acceso a la Información Pública consignando la siguiente información:",
            "1.1 - Nombres y apellidos completos o razón social, número de documento nacional de identidad o número de RUC, domicilio del recurrente y del representante, según corresponda. Tratándose de menores de edad no será necesario indicar su documento de identidad",
            "1.2 - Número de teléfono y/o correo electrónico; de ser el caso.",
            "1.3 - Expresión concreta y precisa del pedido de información.",
            "1.4 - Fechas aproximadas en que la información se ha producido u obtenido.",
            "1.5 - Medio en que se requiere la información (copia simple, diskette, CD, etc.)",
            "1.6 - En caso el solicitante conozca la dependencia que posea la información, deberá indicarlo en la solicitud.",
            "1.7 - Firma del solicitante o huella digital, de no saber firmar o estar impedido de hacerlo",
            "2 El costo por derecho de reproducción de información se encontrará a cargo del administrado quien deberá determinar el medio en el que requiere la información (copia, en medio magnético, electrónico, etc) siendo los costos:",
            "2.1 a) En Copia Simple (unidad) - 0.0026%",
            "2.2 b) En Copia Fedateada (unidad) - 0.0026%",
            "2.3 c) Por CD (unidad) - 0.0395%",
            "--------------------------------------------------",
            "📌 NOTAS PARA EL CIUDADANO:",
            "- El derecho de trámite se establece en función al costo de reproducción del medio que contiene la información solicitada.",
            "- Conforme el Reglamento de la Ley de Transparencia y Acceso a la Información Pública, la información solicitada puede ser remitida a la dirección electrónica proporcionada por el solicitante en caso se haya considerado dicho medio para el acceso a la información pública.",
            "- Las Copias Fedateadas son para la tramitación de procedimientos internos ante la municipalidad."
        ],
        "derecho_tramite": "GRATUITO (Ver costos de reproducción)",
        "plazo": "Evaluación Previa - 7 Días (más 5 Días útiles de prórroga excepcional)",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Funcionario Responsable del Acceso a la Información Publica",
        "reconsideracion": "Funcionario Responsable del Acceso a la Información Publica\nPlazo de Presentation: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente Municipal\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
{
        "id": "163",
        "numero": "145",
        "procedimiento": "SOLICITUD DE BÚSQUEDA Y EXPEDICIÓN DE COPIA CERTIFICADA DE DOCUMENTOS",
        "sustento": "BASE LEGAL\n- Ley Nº 27444 (11.04.01). Arts. 37, 107 y 110.",
        "requisitos": [
            "1 Presentar solicitud firmada por el solicitante.",
            "2 En el caso de representación, presentar poder general formalizado mediante carta poder simple con firma del administrado.",
            "3 Pago por el Derecho de la Tasa Administrativa:",
            "Adicionalmente:",
            "a) Copia Certificada 1° hoja:",
            "b) Copia Certificada 2° hoja y adicionales:",
            "c) Copia Simple (Sin Certificar):",
            "--------------------------------------------------",
            "📌 NOTAS PARA EL CIUDADANO:",
            "- Las Copias Certificadas son para la tramitación de procedimientos internos y externos ante la municipalidad."
        ],
        "derecho_tramite": "0.2632% UIT\n\nAdicionalmente:\na) 0.1711% UIT\nb) 0.0921% UIT\nc) 0.0026% UIT",
        "plazo": "Automático",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Secretaria General",
        "reconsideracion": "",
        "apelacion": ""
    },
    {
        "id": "164",
        "numero": "146",
        "procedimiento": "SOLICITUD DE FEDATEO DE DOCUMENTOS",
        "sustento": "BASE LEGAL\n- Ley Nº 27444 (11.04.01). Arts. 37 y 107.",
        "requisitos": [
            "1 Presentar solicitud firmada por el solicitante.",
            "2 En el caso de representación, presentar poder general formalizado mediante carta poder simple con firma del administrado.",
            "3 Presentar copia del documento a autenticar.",
            "4 Exhibir el documento original objeto de autenticación.",
            "5 Exhibir el documento de identidad del solicitante o representante de ser el caso.",
            "--------------------------------------------------",
            "📌 NOTAS PARA EL CIUDADANO:",
            "- Solo para tramitación de procedimientos internos ante la municipalidad."
        ],
        "derecho_tramite": "GRATUITO",
        "plazo": "Automático",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Secretaria General",
        "reconsideracion": "",
        "apelacion": ""
    },
    {
        "id": "165",
        "numero": "147",
        "procedimiento": "RETIRO O DESGLOSE DE DOCUMENTACIÓN DEL EXPEDIENTE",
        "sustento": "BASE LEGAL\n- Ley Nº 27444 (11.04.01). Art. 153, numeral 2",
        "requisitos": [
            "1 Presentar solicitud firmada por el solicitante indicando los datos del documento que será objeto de desglose y el expediente en el que se encuentre.",
            "2 En el caso de representación, presentar poder general formalizado mediante carta poder simple con firma del administrado.",
            "3 Dejar copia autenticada por fedatario de la municipalidad del documento desglosado, sin alterar la foliatura general del expediente.",
            "4 Exhibir el documento de identidad del solicitante.",
            "5 Pago por el Derecho de la Tasa Administrativa:",
            "--------------------------------------------------",
            "📌 NOTAS PARA EL CIUDADANO:",
            "Deberá asentarse en el expediente la constancia por parte de la autoridad y el solicitante, del desglose efectuado, indicando fecha y folios."
        ],
        "derecho_tramite": "0.8789% UIT",
        "plazo": "Automático",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Secretaria General",
        "reconsideracion": "",
        "apelacion": ""
    },
    {
        "id": "166",
        "numero": "148",
        "procedimiento": "REACTIVACIÓN DE EXPEDIENTES ADMINISTRATIVOS DECLARADOS EN ABANDONO (NO MAYOR A UN AÑO DE ABANDONO)",
        "sustento": "BASE LEGAL\n- Art. 191 de la Ley Nº 27444, 11.Nov.2001",
        "requisitos": [
            "1 Solicitud dirigido a la Entidad",
            "2 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "0.8763% UIT",
        "plazo": "Automático",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Secretaria General",
        "reconsideracion": "",
        "apelacion": ""
    },
{
        "id": "167",
        "numero": "149",
        "procedimiento": "PERMISO DE OPERACIÓN A PERSONAS JURÍDICAS PARA PRESTAR EL SERVICIO CON VEHICULOS MENORES",
        "sustento": "BASE LEGAL\n- Ley Nº 27972 (27.05.03). Arts. 40 y 81 numeral 1.6.\n- Ley Nº 27444 (11.04.01). Arts. 34, 35, 44 y 45.\n- Ley Nº 29060 (07.07.07).\n- Decreto Supremo Nº 156-2004-EF (15.11.04). Art. 68.\n- Ley Nº 27189 (28.10.99). Arts. 2 y 3.\n- Ley Nº 27181 (08.10.99). Arts. 17 y 23.\n- Decreto Supremo Nº 025-2008-MTC (24.08.08). Arts. 4, 8, 12, 34, 47 y 1era. Disposición Complementaria y Final.\n- Decreto Supremo Nº 055-2010-MTC (02.12.10). Arts. 4, 7, 13, 14, 15, y 3ra. y 8va. Disposición Complementaria y Final.\n- Ordenanza Municipal Nº 017-2013-MDSR, Art. 13",
        "requisitos": [
            "1 Formato de solicitud (distribución gratuita o de libre reproducción) con carácter de Declaración indicando lo siguiente: Razón Social de la persona jurídica, RUC, domicilio, nombre y firma del representative legal",
            "2 Copia simple de la escritura pública de de Constitución de la persona jurídica inscrita en Registro Público",
            "3 Copia literal vigente de la partida registral expedida por la Oficina Registral correspondiente con una antigüedad mno mayor de treinta (30) Días a la fecha de la presentación de la solicitud",
            "4 Copia simple del documento nacional de identidad del representante legal",
            "5 Copia simple del certificado de vigencia de poder del representante legal de la empresa, expedido por la Oficina Registral correspondiente con una antigüedad no mayor de treinta (30) Días a la fecha de la presentación de la solicitud",
            "6 Copia simple de la tarjeta de identificación vehicular de cada uno de los vehículos ofertados (mínimo 10 unidades)",
            "7 Copia simple del Certificado de Inspección Técnica Vehicular vigente de cada uno de los vehículos ofertados, según corresponda",
            "8 Copia simple del SOAT vigente o Certificado contra Accidentes de Tránsito de cada uno de los vehículos ofertados",
            "9 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "1.8421% UIT",
        "plazo": "Evaluación Previa - 30 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Sub Gerente de Transportes y Seguridad Vial",
        "reconsideracion": "Sub Gerente de Transportes y Seguridad Vial\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente de Desarrollo Urbano y Territorial\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
{
        "id": "168",
        "numero": "150",
        "procedimiento": "RENOVACIÓN DE PERMISO DE OPERACIÓN A PERSONAS JURIDICAS PARA PRESTAR EL SERVICIO CON VEHICULOS MENORES",
        "sustento": "BASE LEGAL\n- Ley Nº 27972 (27.05.03). Arts. 40 y 81 numeral 1.6.\n- Ley Nº 27444 (11.04.01). Arts. 34, 35, 44 y 45.\n- Ley Nº 29060 (07.07.07).\n- Decreto Supremo Nº 156-2004-EF (15.11.04). Art. 68.\n- Ley Nº 27189 (28.10.99). Arts. 2 y 3.\n- Ley Nº 27181 (08.10.99). Arts. 17 y 23.\n- Decreto Supremo Nº 055-2010-MTC (02.12.10). Arts. 4, 13, 16, y 3ra. y 8va. Disposición Complementaria y Final.\n- Ordenanza Municipal Nº 017-2013-MDSR.",
        "requisitos": [
            "1 Formato de solicitud (distribución gratuita o de libre reproducción) con carácter de Declaracion indicando lo siguiente: Razón Social de la persona jurídica, RUC, domicilio, nombre y firma del representante legal",
            "2 Copia simple de la escritura pública de de Constitución de la persona jurídica inscrita en Registro Público",
            "3 Copia literal vigente de la partida registral expedida por la Oficina Registral correspondiente con una antigüedad mno mayor de treinta (30) Días a la fecha de l a presentación de la solicitud",
            "4 Copia simple del documento nacional de identidad del representante legal",
            "5 Copia simple de la tarjeta de identificación vehicular por cada vehículo ofertado, expedido por la SUNARP, como mínimo diez (10) unidades vehiculares",
            "6 Copia Simple de Certificado del SOAT o CAT vigente por cada vehículo ofertada",
            "7 Copia simple de Certificado de Inspección Técnica Vehicular - CITV por cada vehículo ofertado cuando corresponda",
            "8 Copia de la vigencia de poder del representante legal",
            "9 Copia de la planilla Electronica de sus trabajadores en vigencia",
            "10 Apertura de una cuenta corriente en una entidad bancaria y/o finaciera dentro de la localidad del Distrito de San Ramon, la misma que deberá ser presentada por Declación Jurada",
            "11 Copia de Licencia de Funcionamiento de la oficina administrativa de la persona jurídica",
            "12 Presentar por escrito los servicios que brinda a los comisionistas y la propuestas económica por el pago de uso de línea y otro cobros a realizar",
            "13 Designar un domicilio legal donde funcione sus oficinas en la que existirán mecanismos que permitiran el registro diario de las unidades vehiculares menores inscritas que se encuentren en servicio, pudiendo hacerse uso de tarjetas y/o kardex para el control diario de vehiculos que podrán ser objeto de inspección por parte del Inspector de Tránsito o Policía Municipal asignado al control del tránsito",
            "14 Presentar el Reglamento Interno de la Empresa",
            "15 Presentar copia del Registro Único de Contribuyentes (RUC) y reporte de su vigencia",
            "16 Que el Transportador Autorizado deberá contar con el Libro de Reclamaciones debiendo otorgar una copia de lo efectuado al usuario",
            "17 Pago por el Derecho de la Tasa Administrativa:",
            "--------------------------------------------------",
            "📌 NOTAS PARA EL CIUDADANO:",
            "La renovación de la autorización se debe solicitar dentro de los 30 Días anteriores a su vencimiento del permiso de operación de manera que exista continuidad entre el que vence y la renovación."
        ],
        "derecho_tramite": "5.1842% UIT",
        "plazo": "Evaluación Previa - 30 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Servicios Públicos Locales y Ecología",
        "reconsideracion": "Gerente de Servicios Públicos Locales y Ecología\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente Municipal\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
{
        "id": "169",
        "numero": "151",
        "procedimiento": "MODIFICACIÓN DEL REGISTRO MUNICIPAL DE VEHICULOS MENORES POR CAMBIO DE DATOS RESPECTO DEL:\n- TRANSPORTADOR AUTORIZADO\n- CONDUCTOR\n- VEHICULOS MENORES, INCLUYE BAJA DE VEHÍCULOS",
        "sustento": "BASE LEGAL\n- Ley Nº 27972 (27.05.03). Arts. 40 y 81 numeral 1.6.\n- Ley Nº 27444 (11.04.01). Arts. 34, 35, 44 y 45.\n- Ley Nº 29060 (07.07.07).\n- Decreto Supremo Nº 156-2004-EF (15.11.04). Art. 68.\n- Ley Nº 27181 (08.10.99). Arts. 17 y 23.\n- Ley Nº 27189 (28.10.99). Arts. 2 y 3.\n- Decreto Supremo Nº 055-2010-MTC (02.12.10). Arts. 4, 19 literal i) y 18va. Disposición Complementaria y Final.\n- Ordenanza Municipal Nº 017-2013-MDSR.",
        "requisitos": [
            "1 Formato de solicitud (distribución gratuita o de libre reproducción) con carácter de Declaración Jurada, indicando lo siguiente:",
            "1.1 - La Razón Social de la persona jurídica, RUC, domicilio, nombre y firma del representante legal",
            "1.2 - El número del Permiso de Operación otorgado y fecha de vencimiento de la autorización.",
            "1.3 - La información que se requiere actualizar o modificar.",
            "2 Documentos fedateados que sustentan la información que se requiere modificar o actualizar según corresponda.",
            "3 Certificado de vigencia de poder de la persona natural que representa a la persona jurídica solicitante, expedido por la Oficina Registral correspondiente, con una antigüedad no mayor de 15 Días a la fecha de la presentación de la solicitud, en caso que no se haya actualizado dicha información, de corresponder.",
            "4 Copia simple del DNI del representante, en caso que sea nuevo representante.",
            "5 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "0.6947% UIT",
        "plazo": "Evaluación Previa - 30 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Servicios Públicos Locales y Ecología",
        "reconsideracion": "Gerente de Servicios Públicos Locales y Ecología\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente Municipal\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
    {
        "id": "170",
        "numero": "152",
        "procedimiento": "MODIFICACIÓN DEL REGISTRO MUNICIPAL DE VEHICULOS MENORES POR CAMBIO DE DENOMINACIÓN O RAZÓN SOCIAL",
        "sustento": "BASE LEGAL\n- Ley Nº 27972 (27.05.03). Arts. 40 y 81 numeral 1.6.\n- Ley Nº 27444 (11.04.01). Arts. 34, 35, 44 y 45.\n- Ley Nº 29060 (07.07.07).\n- Decreto Supremo Nº 156-2004-EF (15.11.04). Art. 68.\n- Ley Nº 27181 (08.10.99). Arts. 17 y 23.\n- Ley Nº 27189 (28.10.99). Arts. 2 y 3.\n- Decreto Supremo Nº 055-2010-MTC (02.12.10). Arts. 4, 19 literal j), 23 y 18va. Disposición Complementaria y Final.\n- Ordenanza Municipal Nº 017-2013-MDSR.",
        "requisitos": [
            "1 Formato de solicitud (distribución gratuita o de libre reproducción) con carácter de Declaración Jurada, indicando lo siguiente:",
            "1.1 - La Razón Social de la persona jurídica, RUC, domicilio, nombre y firma del representante legal de la nueva persona jurídica.",
            "1.2 - Los datos de la razón social a modificar y el número del Permiso de Operación otorgado.",
            "2 Certificado de vigencia de poder de la persona natural que representa a la persona jurídica solicitante, expedido por la Oficina Registral correspondiente, con una antigüedad no mayor de 15 Días a la fecha de la presentación de la solicitud.",
            "3 Copia simple del DNI del representante.",
            "4 Copia simple de la Escritura Pública de cambio de la denominación o razón social.",
            "5 Copia literal vigente de la partida registral expedida por la Oficina Registral correspondiente, con una antigüedad no mayor de 30 Días calendarios.",
            "6 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "5.1447% UIT",
        "plazo": "Evaluación Previa - 30 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Servicios Públicos Locales y Ecología",
        "reconsideracion": "Gerente de Servicios Públicos Locales y Ecología\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente Municipal\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
{
        "id": "171",
        "numero": "153",
        "procedimiento": "SUSTITUCIÓN DE VEHICULO MENOR",
        "sustento": "BASE LEGAL\n- Ordenanza Municipal Nº 017-2013-MDSR, Art. 39",
        "requisitos": [
            "1 Solicitud firmada por el Gerente de la Persona Jurídica, dirigida al Alcalde indicando el número de Placa de Rodaje del vehículo",
            "2 Constancia de Baja",
            "3 Copia de la Tarjeta de Propiedad expedida por la SUNARP (fedateada)",
            "4 Copia fedateada del Seguro Obligatorio por Accidente de tránsito vigente - SOAT o CAT",
            "5 Copia fedateada de la Licencia de Conducir",
            "6 Certificación Técnica vigente",
            "7 Tarjeta de circulación original vigente, para el caso de enajenación",
            "8 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "0.7895% UIT",
        "plazo": "Evaluación Previa - 15 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Servicios Públicos Locales y Ecología",
        "reconsideracion": "Gerente de Servicios Públicos Locales y Ecología\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente Municipal\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
    {
        "id": "172",
        "numero": "154",
        "procedimiento": "TRASLADO DE VEHICULO A OTRA PERSONA JURIDICA",
        "sustento": "BASE LEGAL\n- Ordenanza Municipal Nº 017-2013-MDSR, Art. 41",
        "requisitos": [
            "1 Solicitud en la cual solicita su incorporación a otra Empresa Transportadora autorizada por la Municipalidad, consignando el motivo de su retiro de la transportadora autorizada de origen, su número interno del vehículo registrado, éste trámite lo hará el representante legal de la trans-portadora a la cual quiere incorporarse",
            "2 Constancia Notarial de retiro voluntario del Transportador Autorizado de origen",
            "3 Copia de la Tarjeta de Propiedad inscrita en SUNARP",
            "4 Presentación de DNI del propietario",
            "5 Copia de Certificación Técnica vigente",
            "6 Copia de la Póliza de seguro vigente SOAT o CAT",
            "7 Copia de la Licencia de Conducir",
            "8 El Propietario deberá presentar Constancia de Conformidad relacionado al Vehículo emitida por el Transportador Autorizado.",
            "9 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "0.7895% UIT",
        "plazo": "Evaluación Previa - 15 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Servicios Públicos Locales y Ecología",
        "reconsideracion": "Gerente de Servicios Públicos Locales y Ecología\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente Municipal\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
    {
        "id": "173",
        "numero": "155",
        "procedimiento": "SUSTITUCIÓN DE PROPIETARIO",
        "sustento": "BASE LEGAL\n- Ordenanza Municipal Nº 017-2013-MDSR, Art. 41",
        "requisitos": [
            "1 Solicitud dirigida al Alcalde especificando el trámite a realizar.",
            "2 Constancia de conformidad baja al propietario y/o del vehículo anterior emitida por el Transportador Autorizado.",
            "3 Presentación de DNI.",
            "4 Copia de la Tarjeta de Propiedad inscrita en SUNARP",
            "5 Copia de la Póliza de seguro vigente SOAT o CAT",
            "6 Copia de Certificación Técnica vigente",
            "7 Copia de la Licencia de Conducir",
            "8 Original de tarjeta de circulación",
            "9 Pago por el Derecho de la Tasa Administrativa:",
            "--------------------------------------------------",
            "📌 NOTAS PARA EL CIUDADANO:",
            "- Los Propietarios o comisionistas podrán ser sustituidos con otras personas naturales en los siguientes casos:",
            "  a) Tener una antigüedad no menor de seis meses (06) en la empresa inscrita y/o acumulación del tiempo de permanencia adjuntando cualquier medio probatorio que lo certifique.",
            "  b) Por enfermedad grave terminal previo Certificado Médico otorgado por el Instituto Nacional de Enfermedades Neoplásicas y/o discapacidad física (Invalidez permanente).",
            "  c) Por tener urgencia económica por muerte de un familiar hasta el segundo grado de consanguinidad, previa certificación correspondiente.",
            "  d) Además, el nuevo propietario debe presentar en los tres casos un documento notarial de cesión de uso y posesión del número de flota a su favor."
        ],
        "derecho_tramite": "0.7895% UIT",
        "plazo": "Evaluación Previa - 15 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Servicios Públicos Locales y Ecología",
        "reconsideracion": "Gerente de Servicios Públicos Locales y Ecología\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente Municipal\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
{
        "id": "174",
        "numero": "156",
        "procedimiento": "CERTIFICACIÓN TECNICA DE VEHICULO MENOR MOTORIZADO (POR UN AÑO)",
        "sustento": "BASE LEGAL\n- Ordenanza Municipal Nº 017-2013-MDSR, Art. 44",
        "requisitos": [
            "1 Tarjeta de Propiedad inscrita en SUNARP",
            "2 Licencia de Conducir",
            "3 Tarjeta de circulación vigente",
            "4 Poliza de seguro vigente - SOAT o CAT",
            "5 Certificado Técnico anterior",
            "6 Credencial de Educación Vial anterior",
            "7 Constancia de conformidad relacionado al vehículo menor (cotizaciones y/o repuestos",
            "8 Pago por el Derecho de la Tasa Administrativa:",
            "--------------------------------------------------",
            "📌 NOTAS PARA EL CIUDADANO:",
            "- La unidad vehicular autorizada que no pase la certificación técnica en las fechas programadas por la municipalidad deberá solicitar a través del Representante Legal del Transportador Autorizado la Certificación Técnica como rezagado, pagando un adicional del 1.5% de la UIT vigente. (Artículo 46° de la Ordenanza Municipal N° 017-2013-MDSR)"
        ],
        "derecho_tramite": "1.5789% UIT",
        "plazo": "Automático",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Sub Gerente de Transporte, Tránsito y Circulación Vial",
        "reconsideracion": "",
        "apelacion": ""
    },
    {
        "id": "175",
        "numero": "157",
        "procedimiento": "DESCARGO DE PAPELETA DE INFRACCIÓN",
        "sustento": "BASE LEGAL\n- Ley Nº 27972 (27.05.03). Arts. 40 y 81 numeral 1.6.\n- Ley Nº 27444 (11.04.01). Arts. 34, 35, 44 y 45.\n- Ley Nº 29060 (07.07.07).\n- Ley Nº 27181 (08.10.99).\n- Decreto Supremo Nº 055-2010-MTC.",
        "requisitos": [
            "1 Solicitud sustentando con fundamentos de hecho y derecho la improcedencia de la Papeleta de Infracción.",
            "2 Copia del original de la Papeleta de Infracción.",
            "3 Elementos de prueba que sustenten el descargo.",
            "4 Copia de la Tarjeta de Propiedad.",
            "5 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "0.3500% UIT",
        "plazo": "Evaluación Previa - 30 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Servicios Públicos Locales y Ecología",
        "reconsideracion": "Gerente de Servicios Públicos Locales y Ecología\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente Municipal\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
    {
        "id": "176",
        "numero": "158",
        "procedimiento": "RETIRO DE VEHÍCULO DEL DEPÓSITO MUNICIPAL POR INTERNAMIENTO",
        "sustento": "BASE LEGAL\n- Ley Nº 27972 (27.05.03). Arts. 40 y 81 numeral 1.6.\n- Ley Nº 27444 (11.04.01). Arts. 34, 35, 44 y 45.\n- Ley Nº 29060 (07.07.07).\n- Ley Nº 27181 (08.10.99).\n- Decreto Supremo Nº 055-2010-MTC.",
        "requisitos": [
            "1 Cancelación de la Papeleta de Infracción al Tránsito o por el Motivo que fue internado.",
            "2 Presentación de la Constancia de Internamiento de Vehículo",
            "3 Pago por el Derecho de la Tasa Administrativa:",
            "Adicionalmente por Guardianía:",
            "- Vehículo Menor Motorizado x Día:",
            "- Vehículo Mayor Motorizado x Día:"
        ],
        "derecho_tramite": "0.1263% UIT\n\nAdicionalmente por Guardianía:\n- Vehículo Menor Motorizado x Día: 0.0263% UIT\n- Vehículo Mayor Motorizado x Día: 0.0658% UIT",
        "plazo": "Automático",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Sub Gerente de Transporte, Tránsito y Circulación Vial",
        "reconsideracion": "",
        "apelacion": ""
    },
{
        "id": "177",
        "numero": "159",
        "procedimiento": "DUPLICADO DE CERTIFICADO DE PERMISO DE OPERACIÓN",
        "sustento": "BASE LEGAL\n- Ley Nº 27972 (27.05.03). Arts. 40 y 81 numeral 1.8.\n- Ley Nº 27444 (11.04.01). Arts. 44, 45 y 160.\n- Decreto Supremo Nº 156-2004-EF (15.11.04). Art. 68.\n- Decreto Supremo Nº 055-2010-MTC (02.12.10). Art. 4 y 18va. Disposición Complementaria y Final.",
        "requisitos": [
            "1 Formato de solicitud (distribución gratuita o de libre reproducción), en el cual se debe indicar el número del certificado de Permiso de Operación cuyo duplicado se solicita.",
            "2 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "1.3158% UIT",
        "plazo": "Automático",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Sub Gerente de Transporte, Tránsito y Circulación Vial",
        "reconsideracion": "",
        "apelacion": ""
    },
    {
        "id": "178",
        "numero": "160",
        "procedimiento": "TARJETA DE CIRCULACIÓN (POR UN AÑO)",
        "sustento": "BASE LEGAL\n- Ordenanza Municipal Nº 017-2013-MDSR, Art. 18",
        "requisitos": [
            "1 Copia de la Tarjeta de Propiedad instrita en SUNARP",
            "2 Copia del DNI del Propietario",
            "3 Copia de Certificación Técnica vigente",
            "4 Copia de la Póliza de Seguro vigente SOAT o CAT",
            "5 El vehículo deberá estar identificado con el logotipo y color de su empresa, numero de registro vehicular y placa de rodaje legible de acuerdo a las características establecidas en el presen-te Reglamento",
            "6 Copia de la Licencia de Conducir",
            "7 Pago por el Derecho de la Tasa Administrativa (ANUAL):",
            "--------------------------------------------------",
            "📌 NOTAS PARA EL CIUDADANO:",
            "El pago podrá ser realizada de forma fraccionada: Semestral / Trimestral"
        ],
        "derecho_tramite": "1.2763% UIT",
        "plazo": "Automático",
        "inicio": "Sub Gerencia de Transporte, Tránsito y Circulación Vial",
        "autoridad": "Sub Gerente de Transporte, Tránsito y Circulación Vial",
        "reconsideracion": "",
        "apelacion": ""
    },
    {
        "id": "179",
        "numero": "161",
        "procedimiento": "DUPLICADO DE TARJETA DE CIRCULACIÓN",
        "sustento": "BASE LEGAL\n- Ordenanza Municipal Nº 017-2013-MDSR, Art. 20",
        "requisitos": [
            "1 Solicitud de la Persona Jurídica indicando que solicita duplicado de la Tarjeta de Circulación señalando el número de la Placa de Rodaje, Número de Tarjeta de Circulación, Nº Interno del Vehículo, nombres y apellidos del propietario",
            "2 Copia fedateada de la Tarjeta de Propiedad",
            "3 Constancia de la denuncia Policial por pérdida o robo",
            "4 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "0.5316% UIT",
        "plazo": "Automático",
        "inicio": "Sub Gerencia de Transporte, Tránsito y Circulación Vial",
        "autoridad": "Sub Gerente de Transporte, Tránsito y Circulación Vial",
        "reconsideracion": "",
        "apelacion": ""
    },
    {
        "id": "180",
        "numero": "162",
        "procedimiento": "CREDENCIAL DEL CONDUCTOR",
        "sustento": "BASE LEGAL\n- Ordenanza Municipal Nº 017-2013-MDSR, Art. 23",
        "requisitos": [
            "1 Copia fedateada de la Licencia de conducir de la categoría respectiva",
            "2 Presentación de DNI",
            "3 Núnmero de Licencia de Conducir y DNI",
            "4 Domicilio del conductor",
            "5 Dos fotografías del conductor",
            "6 Sello y firma de la autoridad municipal competente",
            "7 Fecha de vencimiento",
            "8 Firma del conductor",
            "9 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "0.2658% UIT",
        "plazo": "Automático",
        "inicio": "Sub Gerencia de Transporte, Tránsito y Circulación Vial",
        "autoridad": "Sub Gerente de Transporte, Tránsito y Circulación Vial",
        "reconsideracion": "",
        "apelacion": ""
    },
{
        "id": "181",
        "numero": "163",
        "procedimiento": "DUPLICADO DEL CREDENCIAL DEL CONDUCTOR",
        "sustento": "BASE LEGAL\n- Ordenanza Nº 017-2013-MDSR, Art. 25",
        "requisitos": [
            "1 Solicitud de la Persona Jurídica indicando que solicita duplicado de credencial del conductor",
            "2 Dos (02) fotografías a color tamaño carné",
            "3 Constancia de denuncia Policial por pérdida o robo",
            "4 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "0.1447% UIT",
        "plazo": "Automático",
        "inicio": "Sub Gerencia de Transporte, Tránsito y Circulación Vial",
        "autoridad": "Sub Gerente de Transporte, Tránsito y Circulación Vial",
        "reconsideracion": "",
        "apelacion": ""
    },
    {
        "id": "182",
        "numero": "164",
        "procedimiento": "DUPLICADO DE STICKER",
        "sustento": "BASE LEGAL\n- Ordenanza Municipal Nº 017-2013-MDSR.",
        "requisitos": [
            "1 Solicitud de la persona jurídica indicando que solicita duplicado de stiker, donde considere el número de placa de rodaje, nombre y apellidos del propietario, número de la tarjeta de circula-ción",
            "2 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "0.1368% UIT",
        "plazo": "Automático",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Sub Gerente de Transporte, Tránsito y Circulación Vial",
        "reconsideracion": "",
        "apelacion": ""
    },
    {
        "id": "183",
        "numero": "165",
        "procedimiento": "EXPEDICIÓN DE RECORD DE PAPELETAS",
        "sustento": "BASE LEGAL\n- Ley Nº 27972 (27.05.03). Arts. 40 y 81 numeral 1.8.\n- Ley Nº 27444 (11.04.01). Arts. 44, 45 y 160.",
        "requisitos": [
            "1 Solicitud verbal especificando los datos del Conductor, Propietario del Vehículo o Número de Placa de Rodaje del Vehículo del cual se pretende obtener el record de papeletas.",
            "2 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "0.3947% UIT",
        "plazo": "Automático",
        "inicio": "Sub Gerencia de Transporte, Tránsito y Circulación Vial",
        "autoridad": "Sub Gerente de Transporte, Tránsito y Circulación Vial",
        "reconsideracion": "",
        "apelacion": ""
    },
    {
        "id": "184",
        "numero": "166",
        "procedimiento": "EXPEDICIÓN DE CARNÉ DE SALUBRIDAD",
        "sustento": "BASE LEGAL\n- Ley Nº 26842, Ley de Salud (Pub. 20.07.1997)\n- D.S. Nº 007-98-SA, Reglamento sobre Vigilancia y Control Sanitario de Alimentos y Bebidas (Pub. 25.09.1998)\n- Artículo 80º de la Ley Nº 27972, Ley Orgánica de Municipalidades",
        "requisitos": [
            "1 Una fotografía de frente tamaño carné",
            "2 Someterse al Examén Médico correspondiente en la Micro Red de San Ramón",
            "3 Pago por el Derecho de la Tasa Administrativa:"
        ],
        "derecho_tramite": "0.3211% UIT",
        "plazo": "Automático",
        "inicio": "Sub Gerencia de Medio Ambiente y Ecología",
        "autoridad": "Sub Gerente de Medio Ambiente y Ecología",
        "reconsideracion": "",
        "apelacion": ""
    },
{
        "id": "185",
        "numero": "167",
        "procedimiento": "RESELLADO DE CARNE DE SALUBRIDAD II SEMESTRE",
        "sustento": "BASE LEGAL\n- Ley Nº 26842, Ley de Salud (Pub. 20.07.1997)\n- D.S. Nº 007-98-SA, Reglamento sobre Vigilancia y Control Sanitario de Alimentos y Bebidas (Pub. 25.09.1998)\n- Artículo 80º de la Ley Nº 27972, Ley Orgánica de Municipalidades",
        "requisitos": [
            "1 Presentación del Carné de Salubridad"
        ],
        "derecho_tramite": "GRATUITO",
        "plazo": "Automático",
        "inicio": "Sub Gerencia de Medio Ambiente y Ecología",
        "autoridad": "Sub Gerente de Medio Ambiente y Ecología",
        "reconsideracion": "",
        "apelacion": ""
    },
    {
        "id": "186",
        "numero": "168",
        "procedimiento": "ADMISIÓN DE ORGANIZACIÓN SOCIAL DE BASE AL PROGRAMA DEL VASO DE LECHE",
        "sustento": "BASE LEGAL\n- Ley Nº 24059, Ley que crea el PVL en todos los Municipios Provinciales de la Republica Pub. 04.01.1985\n- Ley Nº 25307, Ley que declara prioritario el interés nacional la labor que realizan organizaciones en lo referido al servicio de apoyo alimentario que brindan las familias de menores recursos, Pub. 28.01.1991\n- Ley Nº 27470, Ley que establece normas complementarias para la ejecución del PVL, Pub. 03.06.2001",
        "requisitos": [
            "1 Solicitud dirigido al Alcalde con carácter de Declaración Jurada, peticionando la Adminisión al Pro-grama Social de Vaso de Leche",
            "2 Copia simple del Padrón de Socias",
            "3 Copia simple del DNI vigente de las socias activas",
            "4 Copia simple del DNI vigente de los miembros del Consejo Directivo o Junta Directiva",
            "5 Padrón de Beneficiarios según prioridades ajduntando la copia del DNI o Acta de Nacimiento de los Beneficiarios y la Tarjeta de Control, Crecimiento y Desarrollo del Niño",
            "6 Croquis simple de ubicación de la OSB",
            "7 Determinar el lugar donde la OSB recepcionará y atenderá el reparto de los productos pertenecien-al PVL",
            "--------------------------------------------------",
            "📌 NOTAS PARA EL CIUDADANO:",
            "- La Municipalidad verificará que la OSB cuente con la Resolución de Reconocimiento emitido por la Municipalidad.",
            "- Los beneficiarios serán niños de 0 a 6 años de edad, madres gestantes y en periodo de lactancia"
        ],
        "derecho_tramite": "GRATUITO",
        "plazo": "Evaluación Previa - 30 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Desarrollo Social y Humano",
        "reconsideracion": "Gerente de Desarrollo Social y Humano\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente Municipal\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
{
        "id": "187",
        "numero": "169",
        "procedimiento": "ADMISIÓN DE OSB AL PROGRAMA DE COMPLEMENTACIÓN ALIMENTARIA MUNICIPAL PCAM",
        "sustento": "BASE LEGAL\n- Ley Nº 27767, Ley del Programa Nacional Complementario de Asistencia Alimentaria, pub 27.06.2002\n- D.S 002-2004-MINDES, Reglamento de la Ley Nº 27767, pub. 25.05.2004\n- Ley Nº 27972, Ley Orgánica de Municipalidades",
        "requisitos": [
            "1 Solicitud dirigido al Alcalde cumpliendo con los requisitos generales de presentación, peticionando la Admisión al PCAM",
            "2 Copia simple de la Resolución de Reconocimiento de la OSB emitido por la Municipalidad de San Ramón",
            "3 Copia simple del Padrón de Socias Activas (como mínimo de 15 socias)",
            "4 Copia simple del DNI vigente de las socias activas",
            "5 Copia simple del DNI vigente de los miembros del Consejo Directivo o Junta Directiva",
            "6 Croquis de ubicación del OSB",
            "7 Determinar el lugar donde la OSB recepcionará y atenderá el reparto de los productos pertenecientes al PCAM",
            "8 Libro de Actas",
            "9 Cuaderno de Almacén",
            "10 Cuaderno de gastos diarios y raciones",
            "--------------------------------------------------",
            "📌 NOTAS PARA EL CIUDADANO:",
            "- La Organización deberá contar con un local adecuado para la recepción, almacenamiento y distribución de los alimentos"
        ],
        "derecho_tramite": "GRATUITO",
        "plazo": "Evaluación Previa - 30 Días",
        "inicio": "Unidad de Trámite Documentario",
        "autoridad": "Gerente de Desarrollo Social y Humano",
        "reconsideracion": "Gerente de Desarrollo Social y Humano\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles.",
        "apelacion": "Gerente Municipal\nPlazo de Presentación: 15 Días hábiles.\nPlazo de Resolución: 30 Días hábiles."
    },
]

class BuscadorTupaInstitucional:
    def __init__(self, root):
        self.root = root
        self.root.title("SISTEMA DE CONSULTA TUPA - MUNICIPALIDAD DE SAN RAMÓN")
        self.root.geometry("950x720")
        self.root.configure(bg="#F4F6F4")

        # Colores Institucionales
        self.VERDE_OSCURO = "#1E5631"
        self.VERDE_CLARO = "#4C9A2A"

        self.coincidencias = []
        self.indice = 0
        
        self.crear_interfaz()

    def crear_interfaz(self):
        # Cabecera
        frame_header = tk.Frame(self.root, bg=self.VERDE_OSCURO, height=80)
        frame_header.pack(fill="x")
        tk.Label(frame_header, text="🏛️ MUNICIPALIDAD DISTRITAL DE SAN RAMÓN", font=("Arial", 18, "bold"), fg="white", bg=self.VERDE_OSCURO).pack(pady=20)

        # Buscador
        frame_busqueda = tk.LabelFrame(self.root, text=" CRITERIOS DE BÚSQUEDA ", font=("Arial", 10, "bold"), bg="#FFFFFF", fg=self.VERDE_OSCURO, padx=15, pady=10)
        frame_busqueda.pack(fill="x", padx=20, pady=10)

        self.txt_buscar = tk.Entry(frame_busqueda, font=("Arial", 12), width=50)
        self.txt_buscar.pack(side="left", padx=10)
        tk.Button(frame_busqueda, text="🔍 BUSCAR", bg=self.VERDE_CLARO, fg="white", font=("Arial", 10, "bold"), command=self.buscar).pack(side="left", padx=10)

        # Resultados
        self.txt_ficha = tk.Text(self.root, font=("Arial", 11), bg="white", padx=20, pady=20, bd=0, state="disabled")
        self.txt_ficha.pack(fill="both", expand=True, padx=20, pady=10)
        
        # Panel de Botones Obligatorios (Navegación)
        frame_nav = tk.Frame(self.root, bg="#F4F6F4")
        frame_nav.pack(fill="x", padx=20, pady=15)

        self.btn_ant = tk.Button(frame_nav, text="⏮️ ANTERIOR", bg="#666666", fg="white", font=("Arial", 10, "bold"), command=self.anterior)
        self.btn_ant.pack(side="left", padx=5)

        self.lbl_info = tk.Label(frame_nav, text="Coincidencia: 0 de 0", bg="#F4F6F4", font=("Arial", 10, "bold"))
        self.lbl_info.pack(side="left", padx=20)

        self.btn_sig = tk.Button(frame_nav, text="SIGUIENTE ⏭️", bg="#666666", fg="white", font=("Arial", 10, "bold"), command=self.siguiente)
        self.btn_sig.pack(side="left", padx=5)

        btn_limpiar = tk.Button(frame_nav, text="🔄 NUEVA BÚSQUEDA", bg=self.VERDE_OSCURO, fg="white", font=("Arial", 10, "bold"), command=self.limpiar)
        btn_limpiar.pack(side="right", padx=5)

        # Etiquetas visuales
        self.txt_ficha.tag_configure("titulo", font=("Arial", 16, "bold"), foreground=self.VERDE_OSCURO)
        self.txt_ficha.tag_configure("subtitulo", font=("Arial", 12, "bold"), foreground=self.VERDE_CLARO)

    def buscar(self):
        termino = self.txt_buscar.get().lower()
        self.coincidencias = [i for i in DATOS_TUPA if termino in i["procedimiento"].lower() or termino in i["numero"]]
        self.indice = 0
        self.actualizar_vista()

    def actualizar_vista(self):
        self.txt_ficha.configure(state="normal")
        self.txt_ficha.delete("1.0", tk.END)
        
        if self.coincidencias:
            p = self.coincidencias[self.indice]
            self.txt_ficha.insert(tk.END, f"{p['procedimiento']}\n\n", "titulo")
            self.txt_ficha.insert(tk.END, "DETALLES INSTITUCIONALES:\n", "subtitulo")
            self.txt_ficha.insert(tk.END, f"Número: {p['numero']} | Plazo: {p['plazo']}\n")
            self.txt_ficha.insert(tk.END, f"Autoridad: {p['autoridad']}\n\n", "subtitulo")
            self.txt_ficha.insert(tk.END, "REQUISITOS:\n", "subtitulo")
            for r in p['requisitos']:
                self.txt_ficha.insert(tk.END, f"• {r}\n")
            self.lbl_info.config(text=f"Coincidencia: {self.indice + 1} de {len(self.coincidencias)}")
        else:
            self.txt_ficha.insert(tk.END, "No se encontraron resultados para la búsqueda.")
            self.lbl_info.config(text="Coincidencia: 0 de 0")
        
        self.txt_ficha.configure(state="disabled")

    def siguiente(self):
        if self.coincidencias and self.indice < len(self.coincidencias) - 1:
            self.indice += 1
            self.actualizar_vista()

    def anterior(self):
        if self.coincidencias and self.indice > 0:
            self.indice -= 1
            self.actualizar_vista()
            
    def limpiar(self):
        self.txt_buscar.delete(0, tk.END)
        self.coincidencias = []
        self.actualizar_vista()

if __name__ == "__main__":
    root = tk.Tk()
    app = BuscadorTupaInstitucional(root)
    root.mainloop()