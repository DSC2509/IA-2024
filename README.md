<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>README - Análisis Lógico de Clima y Visitas a Instituciones</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            max-width: 800px;
            margin: auto;
            padding: 20px;
            background-color: #fafafa;
        }
        h1, h2 {
            color: #1a1a1a;
        }
        p {
            color: #333;
        }
        code {
            background-color: #e8e8e8;
            padding: 3px 5px;
            border-radius: 4px;
            color: #d6336c;
        }
    </style>
</head>
<body>

    <h1>README - Análisis Lógico de Clima y Visitas a Instituciones</h1>
    
    <p>Este documento describe el archivo <strong>estudianteunimayor.py</strong>, que implementa una base de conocimiento en lógica proposicional. Este análisis permite determinar condiciones sobre el clima y las visitas de estudiantes a diferentes instituciones según las reglas establecidas.</p>

    <h2>Descripción de Variables</h2>
    <p>Las variables proposicionales que se utilizan en este archivo representan distintas condiciones, y son las siguientes:</p>
    <ul>
        <li><code>lluvia</code>: Representa la condición de que esté lloviendo.</li>
        <li><code>BBC</code>: Indica que los estudiantes visitan la institución BBC.</li>
        <li><code>Unimayor</code>: Indica que los estudiantes visitan la institución Unimayor.</li>
    </ul>

    <h2>Reglas Lógicas Definidas</h2>
    <p>Las reglas lógicas que se establecen en el archivo permiten hacer inferencias sobre el estado del clima y las visitas. Estas son:</p>

    <h3>1. Condición Clima y Visita a BBC</h3>
    <p>Si <code>no llueve</code>, entonces los estudiantes visitan BBC. Esta proposición se expresa como:</p>
    <p><code>¬lluvia → BBC</code></p>

    <h3>2. Regla de Visita Exclusiva</h3>
    <p>Los estudiantes visitan BBC o Unimayor, pero no ambos. Esto se expresa mediante una disyunción exclusiva:</p>
    <p><code>(BBC ∨ Unimayor) ∧ ¬(BBC ∧ Unimayor)</code></p>

    <h3>3. Condición Confirmada de Visita a Unimayor</h3>
    <p>Sabemos que los estudiantes visitaron Unimayor en el día. Esto se establece como:</p>
    <p><code>Unimayor</code></p>

    <h2>Objetivo de la Base de Conocimiento</h2>
    <p>Las proposiciones anteriores conforman una base de conocimiento, la cual nos permite hacer deducciones sobre el clima o las visitas. A partir de esta base, podemos hacer preguntas e inferir si ciertas condiciones son verdaderas o no.</p>

    <h2>Consultas y Conclusiones</h2>
    <p>Utilizando la base de conocimiento, se realizan consultas para obtener conclusiones sobre las siguientes situaciones:</p>
    <ul>
        <li>¿Podemos deducir que los estudiantes visitaron BBC hoy?</li>
        <li>¿Podemos concluir si está lloviendo o no?</li>
    </ul>

    <p>El archivo <strong>estudianteunimayor.py</strong> permite hacer estas consultas de forma programática, proporcionando respuestas basadas en la lógica proposicional definida.</p>

    <h2>Instrucciones de Uso</h2>
    <p>Para utilizar este archivo, simplemente ejecuta el script y observa los resultados de las inferencias en base a la lógica implementada. Las conclusiones serán mostradas de acuerdo a las reglas y proposiciones definidas en el código.</p>

</body>
</html>
